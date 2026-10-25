/** Frozen candidate selector replay. Explicit stdin settings; no labels or live config.
 * selectCandidates(settings, dependencies?) accepts the public phase cases and
 * replayCases [{id,params,rawHitlistObservation,matchedSnippets?}]. The fixture,
 * raw manifest/checkpoints, host sources, model and effective config are pinned.
 * settings.policy must match M0 raw_hitlists.policies; timeoutMs must be8000.
 * API keys are used only by the admitted in-memory transport callback.
 */
import { createHash, randomUUID } from "node:crypto";
import { mkdir, readFile, readdir, writeFile } from "node:fs/promises";
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";
import { createHostDecisionAdapter } from "./host_decision_adapter.mjs";
import { createControlledFetch } from "./controlled_model_fetch.mjs";
import { loadInstalledRetrievalSources } from "./harness_retrieval_adapter.mjs";
import { readJsonStdin } from "./json_stdin.mjs";

const root = fileURLToPath(new URL("../../", import.meta.url));
const native = globalThis.fetch;
const sha = (value) => createHash("sha256").update(value).digest("hex");
const canonical = (value) => Array.isArray(value) ? value.map(canonical) : value && typeof value === "object" ? Object.fromEntries(Object.keys(value).sort().map((key) => [key, canonical(value[key])])) : value;
export const stableHash = (value) => sha(JSON.stringify(canonical(value)));
const readJson = async (filename) => JSON.parse(await readFile(filename, "utf8"));
const optional = async (filename) => { try { return await readJson(filename); } catch (error) { if (error.code === "ENOENT") return undefined; throw error; } };
const writeNew = (filename, value) => writeFile(filename, JSON.stringify(value, null, 2) + "\n", { flag: "wx" });
const hex = (value) => typeof value === "string" && /^[a-f0-9]{64}$/.test(value);
const inside = (base, target) => { const relative = path.relative(base, target); return relative && !relative.startsWith("..") && !path.isAbsolute(relative); };
const alive = (pid) => { if (!Number.isInteger(pid) || pid <= 0) return true; try { process.kill(pid, 0); return true; } catch (error) { return error.code !== "ESRCH"; } };

export const SNIPPET_POLICY = Object.freeze({ version: 1, totalUtf8Bytes: 2048, perCandidateUtf8Bytes: 320,
  accounting: "JSON UTF-8 bytes of reference_matched_snippets value, including names and escaping",
  matching: "installed path identity; SDK bestChunk only; body/references before meta; score descending then collection/path; candidate-order allocation" });

function projectCase(row) {
  if (!row || !/^[A-Za-z0-9_-]+$/.test(row.id) || typeof row.latest !== "string" || !row.latest.trim()) throw new Error("Invalid public case");
  const result = { id: row.id, latest: row.latest };
  if (row.conversation !== undefined) {
    if (!Array.isArray(row.conversation) || row.conversation.some((turn) => !["user", "assistant"].includes(turn.role) || typeof (turn.text ?? turn.content) !== "string")) throw new Error("Invalid public conversation");
    result.conversation = row.conversation.map((turn) => ({ role: turn.role, text: turn.text ?? turn.content }));
  }
  return result;
}

export function selectionParams(input, params) {
  const strings = (values) => { if (!Array.isArray(values) || values.some((value) => typeof value !== "string")) throw new Error("Expected public string array"); return [...values]; };
  const records = (rows, fields) => (rows ?? []).map((row) => Object.fromEntries(fields.filter((key) => row[key] !== undefined).map((key) => {
    if (typeof row[key] !== "string") throw new Error("Candidate reference fields must be strings"); return [key, row[key]];
  })));
  const candidateSkills = records(params.candidateSkills, ["name", "description"]);
  if (candidateSkills.some((row) => !row.name || typeof row.description !== "string") || new Set(candidateSkills.map((row) => row.name)).size !== candidateSkills.length) throw new Error("Invalid candidate skill identities");
  return { latest: input.latest, ...(input.conversation === undefined ? {} : { conversation: input.conversation.map(({ role, text }) => ({ role, text })) }),
    candidateSkills,
    candidateExperiences: (params.candidateExperiences ?? []).map((row) => {
      if (typeof row.id !== "string" || typeof row.summary !== "string") throw new Error("Invalid explicit experience");
      return { id: row.id, summary: row.summary, skills: strings(row.skills) };
    }),
    candidateSources: Object.fromEntries(candidateSkills.map(({ name }) => [name, strings(params.candidateSources?.[name] ?? [])])),
    ...(params.visibleSkillNames === undefined ? {} : { visibleSkillNames: strings(params.visibleSkillNames) }),
    relatedEvidence: records(params.relatedEvidence, ["name", "from", "relation_type", "verification_status", "reason"]),
    relationEvidence: records(params.relationEvidence, ["skill", "from", "to", "from_description", "to_description", "relation_type", "verification_status", "reason"]),
  };
}

export function deriveMatchedSnippets({ candidateSkills, rawHitlistObservation, decodeIdentity, docsRoot }) {
  if (typeof decodeIdentity !== "function" || typeof docsRoot !== "string" || !Array.isArray(rawHitlistObservation?.rawHitlists)) throw new Error("Explicit frozen raw hits and installed path decoder are required");
  const matches = new Map(candidateSkills.map(({ name }) => [name, []]));
  for (const list of rawHitlistObservation.rawHitlists) {
    const collection = list.options?.collection;
    if (!["skill-meta", "skill-body", "skill-references"].includes(collection) || !Array.isArray(list.hits)) throw new Error("Invalid frozen hitlist collection");
    for (const hit of list.hits) {
      if (typeof hit.bestChunk !== "string" || !hit.bestChunk.trim() || !Number.isFinite(hit.score)) continue;
      for (const filepath of [hit.filepath, hit.file, hit.displayPath].filter((value) => typeof value === "string")) {
        const identity = decodeIdentity({ docsRoot, filepath, collection });
        if (!matches.has(identity.skillName)) continue;
        matches.get(identity.skillName).push({ skill: identity.skillName, collection, path: identity.relativePath ?? filepath,
          text: hit.bestChunk, chunkSha256: sha(hit.bestChunk), score: hit.score });
        break;
      }
    }
  }
  return candidateSkills.flatMap(({ name }) => {
    const ordered = matches.get(name).sort((a, b) => Number(a.collection === "skill-meta") - Number(b.collection === "skill-meta") || b.score - a.score || a.collection.localeCompare(b.collection, "en") || a.path.localeCompare(b.path, "en") || a.chunkSha256.localeCompare(b.chunkSha256, "en"));
    return ordered.length ? [ordered[0]] : [];
  });
}

export function buildReferenceSnippets(options) {
  const matched = deriveMatchedSnippets(options);
  if (!Array.isArray(options.matchedSnippets) || stableHash(options.matchedSnippets) !== stableHash(matched)) throw new Error("M3 requires explicitly supplied strongest raw matched bestChunk records");
  const state = {};
  for (const entry of matched) {
    let text = "";
    for (const point of entry.text) {
      const next = text + point;
      if (Buffer.byteLength(next) > SNIPPET_POLICY.perCandidateUtf8Bytes || Buffer.byteLength(JSON.stringify({ ...state, [entry.skill]: next })) > SNIPPET_POLICY.totalUtf8Bytes) break;
      text = next;
    }
    if (text) state[entry.skill] = text;
  }
  return { state, matched, policy: SNIPPET_POLICY, utf8Bytes: Buffer.byteLength(JSON.stringify(state)) };
}

export async function prepareSelectorRuntime(settings) {
  const sources = await loadInstalledRetrievalSources({ offline: false });
  if (!Array.isArray(settings.hostSourcePins) || !settings.hostSourcePins.length) throw new Error("Explicit installed host source pins are required");
  const allowedRoots = ["skill-harness", "typesafe"].map((name) => path.join(os.homedir(), ".openclaw/extensions", name));
  for (const pin of settings.hostSourcePins) {
    if (!allowedRoots.some((directory) => inside(directory, path.resolve(pin.path))) || !/\.(m?js|json)$/.test(pin.path) || !hex(pin.sha256) || sha(await readFile(pin.path)) !== pin.sha256) throw new Error("Installed host source pin mismatch");
  }
  const hostSourcePins = settings.hostSourcePins.map(({ path, sha256 }) => ({ path, sha256 }));
  return { pins: [...sources.sources, ...hostSourcePins], decodeIdentity: sources.skillIdentityFromDocsPath,
    hostSourcePins, docsRoot: path.join(settings.runDir, "qmd-public/docs") };
}

async function checkInputs(settings, fixturePath) {
  const runDir = path.resolve(settings.runDir);
  if (!inside(path.join(root, "experiments/datasets"), runDir) || !["development", "holdout"].includes(settings.phase)) throw new Error("Invalid selector run directory or phase");
  if (!/^[a-zA-Z0-9_-]+$/.test(settings.variant)) throw new Error("Explicit safe variant name required");
  const bytes = await readFile(fixturePath);
  if (sha(bytes) !== settings.expectedCasesSha256) throw new Error("Frozen public fixture SHA mismatch");
  const parsed = JSON.parse(bytes); const all = (parsed.cases ?? parsed).map(projectCase); const byId = new Map(all.map((row) => [row.id, row]));
  const partitions = settings.casePartitions;
  if (all.length !== 180 || byId.size !== 180 || partitions?.development?.length !== 120 || partitions.holdout?.length !== 60 || new Set([...partitions.development, ...partitions.holdout]).size !== 180 || [...partitions.development, ...partitions.holdout].some((id) => !byId.has(id))) throw new Error("Frozen phase partitions must cover exactly120/60 public cases");
  const cases = settings.cases.map(projectCase);
  if (stableHash(cases.map(({ id }) => id)) !== stableHash(partitions[settings.phase]) || cases.some((row) => stableHash(row) !== stableHash(byId.get(row.id)))) throw new Error("Phase cases differ from frozen public fixture/order");
  if (settings.models?.jev !== "jev-latest" || settings.models.jevResolved !== "jev-1.14.0" || typeof settings.endpoints?.jev?.url !== "string") throw new Error("Explicit frozen jev identity and endpoint required");
  const m0 = await readJson(path.join(runDir, "m0-query-probes.json"));
  const frozenPolicy = m0.raw_hitlists?.policies;
  if (!settings.policy || !frozenPolicy || stableHash(settings.policy) !== stableHash(frozenPolicy)) throw new Error("Selector policy differs from frozen M0 policy");
  const routing = frozenPolicy.routing;
  if (routing?.skills?.maxInjectedSkills !== 6 || routing.skills.relevanceThreshold !== 0.4 || routing.skills.search?.minCandidateScore !== 0.3) throw new Error("Frozen M0 policy must retain cap6, threshold0.4 and minCandidateScore0.3");
  if (settings.timeoutMs !== 8000) throw new Error("Selector timeout must match the frozen experiment timeout8000ms");
  if (!["none", "matched-reference"].includes(settings.config?.snippet) || ![6, 10, 20].includes(settings.config.poolLimit) || !["current-max", "skill-identity-sum"].includes(settings.config.fusion)) throw new Error("Unsupported frozen selector config");
  if (Object.hasOwn(settings.config, "routing")) throw new Error("Selector routing policy belongs in frozen settings.policy, not intervention config");
  if (settings.config.snippet === "matched-reference" && stableHash(settings.config.snippetPolicy) !== stableHash(SNIPPET_POLICY)) throw new Error("M3 snippet policy must be explicitly frozen in config");
  let challengerConfigSha256 = null;
  if (settings.phase === "holdout") {
    const frozenBytes = await readFile(path.join(runDir, "challenger-config.json")); const frozen = JSON.parse(frozenBytes);
    if (!hex(settings.challengerConfigSha256) || sha(frozenBytes) !== settings.challengerConfigSha256 || frozen.status !== "frozen" || frozen.m1CasesSha256 !== settings.expectedCasesSha256 || ![frozen.baseline, frozen.challenger].some((config) => stableHash(config) === stableHash(settings.config))) throw new Error("Holdout requires matching frozen challenger config SHA and variant");
    challengerConfigSha256 = sha(frozenBytes);
  }
  if (!Array.isArray(settings.replayCases) || stableHash(settings.replayCases.map(({ id }) => id)) !== stableHash(cases.map(({ id }) => id))) throw new Error("Explicit replay candidates must match public phase cases/order");
  const rawManifestBytes = await readFile(path.join(runDir, settings.phase, "raw-manifest.json"));
  const rawManifest = JSON.parse(rawManifestBytes);
  if (!hex(settings.expectedRawManifestSha256) || sha(rawManifestBytes) !== settings.expectedRawManifestSha256 || rawManifest.status !== "complete" || rawManifest.cases?.length !== cases.length) throw new Error("Frozen raw manifest hash/status mismatch");
  for (let index = 0; index < cases.length; index++) {
    const entry = rawManifest.cases[index]; const input = cases[index];
    if (entry.id !== input.id || entry.file !== `raw/${input.id}.json`) throw new Error("Raw manifest public case/order mismatch");
    const bytes = await readFile(path.join(runDir, settings.phase, entry.file)); const checkpoint = JSON.parse(bytes);
    const { checkpointContentSha256, ...content } = checkpoint;
    if (sha(bytes) !== entry.sha256 || checkpointContentSha256 !== stableHash(content) || content.status !== "complete" || stableHash(projectCase(content.input)) !== stableHash(input) || stableHash(content.rawHitlistObservation) !== stableHash(settings.replayCases[index].rawHitlistObservation)) throw new Error("Candidate replay differs from frozen raw checkpoint");
  }
  return { runDir, cases, challengerConfigSha256, rawManifestSha256: sha(rawManifestBytes),
    policy: structuredClone(frozenPolicy), routing: structuredClone(routing), timeoutMs: 8000 };
}

export async function selectCandidates(settings, { fixturePath = path.join(root, "experiments/fixtures/harness_pilot_cases.json"),
  prepareRuntime = prepareSelectorRuntime, createAdapter = createHostDecisionAdapter,
  createTransport = createControlledFetch, nativeFetch = native } = {}) {
  const checked = await checkInputs(settings, fixturePath); settings = { ...settings, runDir: checked.runDir };
  const runtime = await prepareRuntime(settings);
  const implementation = await Promise.all(["select_harness_candidates.mjs", "host_decision_adapter.mjs", "controlled_model_fetch.mjs", "json_stdin.mjs"].map(async (name) => ({ path: name, sha256: sha(await readFile(new URL(name, import.meta.url))) })));
  const inputs = checked.cases.map((input, index) => {
    const replay = settings.replayCases[index];
    if (replay.rawHitlistObservation?.query !== input.latest || !Array.isArray(replay.rawHitlistObservation.rawHitlists)) throw new Error("Candidates require frozen original-query raw hitlists");
    const params = selectionParams(input, replay.params);
    const snippets = settings.config.snippet === "matched-reference" ? buildReferenceSnippets({ ...replay, candidateSkills: params.candidateSkills, decodeIdentity: runtime.decodeIdentity, docsRoot: runtime.docsRoot }) : undefined;
    return { input, params, snippets, rawInputSha256: stableHash(replay.rawHitlistObservation) };
  });
  const binding = { phase: settings.phase, variant: settings.variant, publicCasesSha256: settings.expectedCasesSha256,
    phaseCasesSha256: stableHash(checked.cases), partitionsSha256: stableHash(settings.casePartitions), configSha256: stableHash(settings.config),
    exactReplayInputsSha256: stableHash(inputs), sourcePinsSha256: stableHash(runtime.pins), implementation,
    model: { jev: settings.models.jev, jevResolved: settings.models.jevResolved }, injectionCap: 6,
    timeoutMs: checked.timeoutMs, policySha256: stableHash(checked.policy), routingSha256: stableHash(checked.routing),
    rawManifestSha256: checked.rawManifestSha256,
    endpointSha256: stableHash(settings.endpoints.jev.url), challengerConfigSha256: checked.challengerConfigSha256 };
  const identity = stableHash(binding); const dir = path.join(settings.runDir, settings.phase, "selectors", settings.variant); const casesDir = path.join(dir, "cases");
  await mkdir(casesDir, { recursive: true });
  const startPath = path.join(dir, "run-start.json"); const start = await optional(startPath);
  if (start && start.selectorIdentitySha256 !== identity) throw new Error("Selector source/settings/input identity changed");
  if (await optional(path.join(dir, "failed-run.json"))) throw new Error("Failed selector run preserved; no automatic retry");
  const allowed = new Set(inputs.flatMap(({ input }) => [`${input.id}.json`, `${input.id}.pending.json`]));
  if ((await readdir(casesDir)).some((name) => !allowed.has(name))) throw new Error("Unexpected selector checkpoint file");
  let prefix = 0, gap = false;
  const results = [];
  for (const item of inputs) {
    const pending = await optional(path.join(casesDir, `${item.input.id}.pending.json`)); const checkpoint = await optional(path.join(casesDir, `${item.input.id}.json`));
    if (pending && (!checkpoint || pending.selectorIdentitySha256 !== identity || pending.inputSha256 !== stableHash(item))) throw new Error("Incomplete/different pending selector case; no automatic retry");
    if (checkpoint) {
      const { checkpointContentSha256, ...content } = checkpoint;
      if (gap || !pending || checkpointContentSha256 !== stableHash(content) || content.selectorIdentitySha256 !== identity || content.inputSha256 !== stableHash(item) || !["complete", "skipped-empty-pool"].includes(content.status)) throw new Error("Selector checkpoint prefix/hash mismatch");
      prefix++; results.push(checkpoint);
    } else gap = true;
  }
  const manifestPath = path.join(dir, "manifest.json"); const manifest = await optional(manifestPath);
  const indexRows = async () => Promise.all(inputs.map(async ({ input }) => ({ id: input.id, sha256: sha(await readFile(path.join(casesDir, `${input.id}.json`))) })));
  if (manifest) {
    if (prefix !== inputs.length || manifest.selectorIdentitySha256 !== identity || stableHash(manifest.cases) !== stableHash(await indexRows())) throw new Error("Selector complete manifest mismatch");
    return { ...manifest, status: "cached-complete", currentInvocationTransport: { physicalAttempts: 0, cacheHits: 0, observations: [] } };
  }
  if (start && alive(start.pid)) throw new Error("Previous selector PID is live or cannot be disproved");
  if (start) {
    let resumes = [];
    try { resumes = await readdir(path.join(dir, "resumes")); } catch (error) { if (error.code !== "ENOENT") throw error; }
    for (const name of resumes) {
      if (!/^[a-f0-9-]{36}\.json$/.test(name)) throw new Error("Unexpected selector resume record");
      const resume = await readJson(path.join(dir, "resumes", name));
      if (resume.selectorIdentitySha256 !== identity || resume.originalStartSha256 !== sha(await readFile(startPath)) || alive(resume.pid)) throw new Error("Prior selector resume PID is live/unverified or identity differs");
    }
  }
  if (!start && prefix) throw new Error("Selector prefix has no run-start");
  if (!start) await writeNew(startPath, { status: "running", pid: process.pid, selectorIdentitySha256: identity, binding, sourcePins: runtime.pins });
  else {
    await mkdir(path.join(dir, "resumes"), { recursive: true });
    await writeNew(path.join(dir, "resumes", `${randomUUID()}.json`), { pid: process.pid, selectorIdentitySha256: identity, originalStartSha256: sha(await readFile(startPath)), verifiedCompletePrefix: prefix });
  }
  let adapter, transport, failed = false, current;
  try {
    if (prefix < inputs.length) {
      transport = createTransport({ runDir: settings.runDir, python: path.join(root, "experiments/.venv/bin/python"), probe: false, nativeFetch,
        endpoints: [{ url: settings.endpoints.jev.url, provider: "jev", model: settings.models.jev, resolvedModel: "jev-1.14.0", validate: (payload, body) => adapter.validateWireResponse(payload, body) }] });
      const mapped = async (url, init) => {
        if (failed || String(url) !== "https://selector-replay.invalid/v1/systemone") throw new Error("Unadmitted selector transport");
        const headers = new Headers(init.headers); headers.delete("authorization");
        if (settings.endpoints.jev.apiKey) headers.set("authorization", `Bearer ${settings.endpoints.jev.apiKey}`);
        try { const response = await transport(settings.endpoints.jev.url, { ...init, headers }); if (!response.ok) { failed = true; throw new Error("Selector HTTP failure"); } return response; } catch (error) { failed = true; throw error; }
      };
      adapter = await createAdapter({ fixtureRoot: path.join(settings.runDir, "selector-runtime", randomUUID()), model: "jev-latest", providerConfig: { apiBaseUrl: "https://selector-replay.invalid/v1" }, fetchImpl: mapped, offline: false });
      if (runtime.hostSourcePins && adapter.provenance.sources.some((pin) => !runtime.hostSourcePins.some((expected) => expected.path === pin.path && expected.sha256 === pin.sha256))) throw new Error("Installed host facade differs from frozen source pins");
      for (const item of inputs.slice(prefix)) {
        current = item.input.id;
        const pending = { pid: process.pid, selectorIdentitySha256: identity, inputSha256: stableHash(item) };
        await writeNew(path.join(casesDir, `${current}.pending.json`), pending);
        const before = structuredClone(transport.stats); const batch = adapter.buildSelectionBatch(item.params);
        const candidateCount = item.params.candidateSkills.length;
        if (item.snippets) batch.state = { ...batch.state, reference_matched_snippets: item.snippets.state };
        const started = performance.now();
        const result = Object.keys(batch.questions).length ? await adapter.evaluateSelection(item.params, { batch,
          timeoutMs: checked.timeoutMs, routing: structuredClone(checked.routing) }) : { skipped: "empty-pool", trace: { fetchCalls: 0, hostCalls: 0, legacyCalls: 0 } };
        if (failed || (!result.skipped && (!result.selection || result.outcome?.status !== "ok"))) throw new Error("Selector unavailable, timeout or invalid result; not an accuracy observation");
        const content = { schema_version: 1, status: result.skipped ? "skipped-empty-pool" : "complete", candidate_count: candidateCount,
          selectorIdentitySha256: identity, inputSha256: stableHash(item), input: item.input, rawInputSha256: item.rawInputSha256,
          modelInputSha256: stableHash(batch), selection: result.selection ?? null, trace: result.trace, outcome: result.outcome ?? null,
          snippetProvenance: item.snippets ?? null, evaluationWallMs: performance.now() - started,
          transportObservations: structuredClone(transport.stats.observations.slice(before.observations.length)),
          transportCounts: { physicalAttempts: transport.stats.physicalAttempts - before.physicalAttempts, cacheHits: transport.stats.cacheHits - before.cacheHits } };
        const checkpoint = { ...content, checkpointContentSha256: stableHash(content) };
        await writeNew(path.join(casesDir, `${current}.json`), checkpoint); results.push(checkpoint);
      }
    }
    const manifest = { schema_version: 1, status: "complete", selectorIdentitySha256: identity, binding, cases: await indexRows(),
      skippedEmptyPools: results.filter((row) => row.status === "skipped-empty-pool").length,
      currentInvocationTransport: transport?.stats ?? { physicalAttempts: 0, cacheHits: 0, observations: [] }, scope: "Actual installed host selector replay; no label scoring" };
    await writeNew(manifestPath, manifest); return manifest;
  } catch {
    await writeNew(path.join(dir, "failed-run.json"), { status: "failed", selectorIdentitySha256: identity, caseId: current ?? null, failure: "selector-unavailable-transport-schema-or-checkpoint", transport: transport?.stats ?? null });
    throw new Error("Selector stopped; failed/pending artifacts preserved; no automatic retry");
  } finally { await adapter?.close(); }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const result = await selectCandidates(await readJsonStdin());
    console.log(JSON.stringify({ status: result.status, cases: result.cases.length, currentInvocationTransport: result.currentInvocationTransport }));
  } catch {
    console.error("Selector replay stopped; inspect preserved artifacts. Credentials/provider details omitted."); process.exitCode = 1;
  }
}
