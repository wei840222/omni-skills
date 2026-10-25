/** Frozen public pilot raw retrieval capture. Credentials arrive on stdin only.
 * No Decision or labels enter this phase. Run in a fresh dedicated process.
 */
import { createHash, randomUUID } from "node:crypto";
import { mkdir, readFile, readdir, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createHarnessRetrievalAdapter, loadInstalledRetrievalSources } from "./harness_retrieval_adapter.mjs";
import { createControlledFetch } from "./controlled_model_fetch.mjs";
import { validateEmbeddings } from "./embed_public_gaps.mjs";
import { readJsonStdin } from "./json_stdin.mjs";

const root = fileURLToPath(new URL("../../", import.meta.url));
const capturedNativeFetch = globalThis.fetch; // Before model-bearing dynamic imports.
const fixture = path.join(root, "experiments/fixtures/harness_pilot_cases.json");
const sha = (value) => createHash("sha256").update(value).digest("hex");
const canonical = (value) => Array.isArray(value) ? value.map(canonical) : value && typeof value === "object" ? Object.fromEntries(Object.keys(value).sort().map((key) => [key, canonical(value[key])])) : value;
export const stableHash = (value) => sha(JSON.stringify(canonical(value)));
const readJson = async (filename) => JSON.parse(await readFile(filename, "utf8"));
const readOptional = async (filename) => { try { return await readJson(filename); } catch (error) { if (error.code === "ENOENT") return undefined; throw error; } };
const writeNew = (filename, data) => writeFile(filename, JSON.stringify(data, null, 2) + "\n", { flag: "wx" });
const hex = (value) => typeof value === "string" && /^[a-f0-9]{64}$/.test(value);

function project(row) {
  if (!row || !/^[A-Za-z0-9_-]+$/.test(row.id) || typeof row.latest !== "string" || !row.latest.trim()) throw new Error("Invalid public case");
  const result = { id: row.id, latest: row.latest };
  if (row.conversation !== undefined) {
    if (!Array.isArray(row.conversation) || row.conversation.some((turn) => !["user", "assistant"].includes(turn.role) || typeof (turn.text ?? turn.content) !== "string")) throw new Error("Invalid public case conversation");
    result.conversation = row.conversation.map((turn) => ({ role: turn.role, text: turn.text ?? turn.content }));
  }
  return result;
}

async function settingsGuard(settings, fixturePath) {
  if (!["development", "holdout"].includes(settings.phase)) throw new Error("Invalid phase");
  const runDir = path.resolve(settings.runDir);
  const relative = path.relative(path.join(root, "experiments/datasets"), runDir);
  if (!relative || relative.startsWith("..") || path.isAbsolute(relative)) throw new Error("Invalid run directory");
  const bytes = await readFile(fixturePath);
  if (sha(bytes) !== settings.expectedCasesSha256) throw new Error("Public fixture SHA mismatch");
  const parsed = JSON.parse(bytes); const rows = (parsed.cases ?? parsed).map(project);
  const all = new Map(rows.map((row) => [row.id, row]));
  const partitions = settings.casePartitions;
  if (rows.length !== 180 || all.size !== 180 || !Array.isArray(partitions?.development) || partitions.development.length !== 120 || !Array.isArray(partitions.holdout) || partitions.holdout.length !== 60 || new Set([...partitions.development, ...partitions.holdout]).size !== 180 || [...partitions.development, ...partitions.holdout].some((id) => !all.has(id))) throw new Error("Phase partitions must cover exactly120/60 public cases");
  const cases = settings.cases.map(project);
  if (stableHash(cases.map((row) => row.id)) !== stableHash(partitions[settings.phase])) throw new Error("Cases must exactly match the phase ID list and order");
  for (const row of cases) if (stableHash(row) !== stableHash(all.get(row.id))) throw new Error("Incoming public case content differs from the frozen fixture");
  const models = settings.models;
  if (models?.jev !== "jev-latest" || models.jevResolved !== "jev-1.14.0" || models.expansion !== "gemini-3.5-flash-lite" || models.expansionResolved !== "gemini-3.5-flash-lite" || (models.embedding !== undefined && models.embedding !== "text-embedding-3-small")) throw new Error("Pilot model identities differ from the frozen models");
  let challengerSha256 = null;
  if (settings.phase === "holdout") {
    const challengerBytes = await readFile(path.join(runDir, "challenger-config.json")); const challenger = JSON.parse(challengerBytes);
    if (!hex(settings.challengerConfigSha256) || sha(challengerBytes) !== settings.challengerConfigSha256 || challenger.schema_version !== 1 || challenger.status !== "frozen" || challenger.m1CasesSha256 !== settings.expectedCasesSha256 || !hex(challenger.m1LabelsSha256) || !hex(challenger.contractSha256) || [challenger.baseline, challenger.challenger].some((value) => !value || ["fusion", "poolLimit", "snippet"].some((key) => !Object.hasOwn(value, key)))) throw new Error("Holdout challenger freeze/hash mismatch");
    challengerSha256 = sha(challengerBytes); // Label/contract contents are never read.
  }
  return { runDir, cases, challengerSha256 };
}

async function snapshotHashes(directory) {
  const entries = [];
  async function visit(folder) { for (const entry of (await readdir(folder, { withFileTypes: true })).sort((a, b) => a.name.localeCompare(b.name, "en"))) { const filename = path.join(folder, entry.name); if (entry.isSymbolicLink()) throw new Error("Frozen public snapshot contains a symlink"); if (entry.isDirectory()) await visit(filename); else if (entry.isFile()) entries.push({ path: path.relative(directory, filename), sha256: sha(await readFile(filename)) }); } }
  await visit(directory); return sha(JSON.stringify(entries));
}

export async function preparePilotRuntime(settings) {
  globalThis.fetch = async () => { throw new Error("Pilot imports have no transport authority"); };
  const harness = path.join(os.homedir(), ".openclaw/extensions/skill-harness");
  const m0Bytes = await readFile(path.join(settings.runDir, "m0-query-probes.json"));
  const m0 = JSON.parse(m0Bytes).raw_hitlists;
  for (const source of m0.provenance.sources) {
    if (!source.path.startsWith(harness + path.sep) || sha(await readFile(source.path)) !== source.sha256) throw new Error("Critical installed source hash differs from M0");
  }
  const sources = await loadInstalledRetrievalSources({ offline: false });
  const buildBytes = await readFile(path.join(settings.runDir, "qmd-build.json")); const build = JSON.parse(buildBytes);
  const profile = path.join(settings.runDir, "qmd-public");
  const dbSha = sha(await readFile(path.join(profile, "skill-search.sqlite")));
  const docsSha = await snapshotHashes(path.join(profile, "docs"));
  if (!build.vector_ready || build.target_vector_rows !== 10443 || dbSha !== m0.profile.databaseSha256 || docsSha !== build.snapshot_files_sha256_after) throw new Error("Frozen public QMD profile differs from M0/build");
  const db = sources.openReadOnlyDatabase(path.join(profile, "skill-search.sqlite"));
  let documentSha;
  try {
    sources.loadSqliteVec(db);
    const state = db.prepare("SELECT status,model,dimension,fingerprint FROM embedding_index_state WHERE singleton=1").get();
    const vectors = db.prepare("SELECT COUNT(*) AS n FROM content_vectors cv JOIN vectors_vec vv ON vv.hash_seq=cv.hash || '_' || cv.seq WHERE cv.model=? AND cv.embed_fingerprint=?").get("text-embedding-3-small", state?.fingerprint ?? "").n;
    documentSha = sha(JSON.stringify(db.prepare("SELECT collection,path,title,hash FROM documents WHERE active=1 ORDER BY collection,path").all()));
    if (state?.status !== "ready" || state.model !== "text-embedding-3-small" || state.dimension !== 1536 || state.fingerprint !== m0.profile.embeddingFingerprint || vectors !== 10443 || documentSha !== build.target_documents_sha256_after) throw new Error("Frozen public document/vector identity mismatch");
  } finally { db.close(); }
  for (const name of await readdir(path.join(root, "skills"))) {
    let raw; try { raw = await readFile(path.join(root, "skills", name, "SKILL.md"), "utf8"); } catch (error) { if (["ENOENT", "ENOTDIR"].includes(error.code)) continue; throw error; }
    const parsed = sources.matter(raw); const body = parsed.content.trim();
    if (await readFile(path.join(profile, "docs/meta", sources.safePathSegment(name), "meta.md"), "utf8") !== `# ${name}\n\n${parsed.data.description.trim()}\n` || await readFile(path.join(profile, "docs/body", sources.safePathSegment(name), "SKILL.md"), "utf8") !== (body ? body + "\n" : "")) throw new Error("Current public skill metadata/body differs from frozen snapshot");
  }
  const { resolveConfig } = await import(pathToFileURL(path.join(harness, "dist/src/config.js")).href);
  const schema = await import(pathToFileURL(path.join(os.homedir(), ".openclaw/extensions/typesafe/dist/src/schema.js")).href);
  const endpoint = (model) => ({ model, baseUrl: "https://qmd-reuse.invalid/v1", apiKey: "offline-controlled-transport-placeholder" });
  const resolvedConfig = resolveConfig({ qmd: { timeoutMs: settings.policy.qmdTimeoutMs, embedding: { ...endpoint("text-embedding-3-small"), dimension: 1536 }, expansion: endpoint(settings.models.expansion), jev: endpoint(settings.models.jev) }, skills: { search: { collectionWeights: settings.policy.collectionWeights } }, routing: settings.policy.routing }, { env: {}, openClawConfig: {} });
  if (stableHash(resolvedConfig.routing.skills) !== stableHash(m0.policies.routing.skills) || resolvedConfig.qmd.timeoutMs !== m0.policies.qmd.timeoutMs || stableHash(resolvedConfig.skills.search.collectionWeights) !== stableHash(m0.policies.skills.search.collectionWeights) || settings.models.expansion !== m0.policies.qmd.expansion.model || settings.models.jev !== m0.policies.qmd.jev.model) throw new Error("Resolved pilot policy/models differ from M0");
  const rules = [
    { url: settings.endpoints.embedding.url, provider: "embedding", model: "text-embedding-3-small", resolvedModel: "text-embedding-3-small", validate: validateEmbeddings },
    { url: settings.endpoints.jev.url, provider: "jev", model: settings.models.jev, resolvedModel: settings.models.jevResolved, validate: (payload, body) => schema.parseResult(payload, schema.parseInput(body)) },
    { url: settings.endpoints.expansion.url, provider: "expansion", model: settings.models.expansion, resolvedModel: settings.models.expansionResolved, maxOutputTokens: 65536, outputBoundSource: "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite", validate: (payload) => { if (!Array.isArray(payload.choices) || typeof payload.choices[0]?.message?.content !== "string") throw new Error("Invalid expansion response"); } },
  ];
  const helpers = [fileURLToPath(import.meta.url), fileURLToPath(new URL("./harness_retrieval_adapter.mjs", import.meta.url)), fileURLToPath(new URL("./controlled_model_fetch.mjs", import.meta.url)), fileURLToPath(new URL("./embed_public_gaps.mjs", import.meta.url)), fileURLToPath(new URL("./json_stdin.mjs", import.meta.url))];
  return { resolvedConfig, rules, pins: { m0RawSha256: sha(m0Bytes), qmdBuildSha256: sha(buildBytes), installedSourceSha256: stableHash(m0.provenance.sources), profileDatabaseSha256: dbSha, publicSnapshotSha256: docsSha, publicDocumentsSha256: documentSha, helpers: await Promise.all(helpers.map(async (filename) => ({ path: filename, sha256: sha(await readFile(filename)) }))) } };
}

function observationGuard(value, input) {
  if (value?.status !== "completed" || value.query !== input.latest || !Array.isArray(value.rawHitlists) || value.rawHitlists.length !== 3 || new Set(value.rawHitlists.map((row) => row.options?.collection)).size !== 3 || value.rawHitlists.some((row) => !["skill-meta", "skill-body", "skill-references"].includes(row.options?.collection) || row.options.rerank !== false || !Array.isArray(row.hits) || row.hits.length > 40 || row.stages?.some((stage) => stage.stage === "onExpansionError")) || value.additionalSources?.experiences !== "unavailable-not-imported" || value.additionalSources?.graph !== "unavailable-not-imported") throw new Error("Raw observation status/schema/source validation failed");
  return Object.fromEntries(["query", "expansionContext", "requests", "rawHitlists", "skillHits", "latency_ms", "status", "nameCandidates", "matchedTokens", "retrievalCandidates", "unionPool", "candidateSkills", "candidateSources", "relationEvidence", "additionalSources"].filter((key) => key in value).map((key) => [key, value[key]]));
}
const alive = (pid) => { if (!Number.isInteger(pid) || pid <= 0) return true; try { process.kill(pid, 0); return true; } catch (error) { return error.code !== "ESRCH"; } };

export async function capturePilot(settings, { fixturePath = fixture, prepareRuntime = preparePilotRuntime, createAdapter = createHarnessRetrievalAdapter, createTransport = createControlledFetch, nativeFetch = capturedNativeFetch } = {}) {
  const checked = await settingsGuard(settings, fixturePath); settings = { ...settings, runDir: checked.runDir };
  const runtime = await prepareRuntime(settings);
  const binding = { phase: settings.phase, casesSha256: settings.expectedCasesSha256, partitionsSha256: stableHash(settings.casePartitions), selectedCasesSha256: stableHash(checked.cases), policySha256: stableHash(settings.policy), modelSha256: stableHash(settings.models), sourcePinsSha256: stableHash(runtime.pins), endpointSha256: stableHash(Object.fromEntries(["embedding", "expansion", "jev"].map((key) => [key, settings.endpoints[key].url]))), challengerConfigSha256: checked.challengerSha256 };
  const identity = stableHash(binding); const phaseDir = path.join(settings.runDir, settings.phase); const rawDir = path.join(phaseDir, "raw");
  await mkdir(rawDir, { recursive: true });
  const startPath = path.join(phaseDir, "run-start.json"); const start = await readOptional(startPath);
  if (start && start.captureIdentitySha256 !== identity) throw new Error("Existing phase identity differs; no automatic rerun");
  if (await readOptional(path.join(phaseDir, "failed-run.json"))) throw new Error("A failed phase is preserved; no automatic retry");
  const knownFiles = new Set(checked.cases.flatMap((row) => [`${row.id}.json`, `${row.id}.pending.json`]));
  if ((await readdir(rawDir)).some((name) => !knownFiles.has(name))) throw new Error("Unknown checkpoint/pending file");
  const completed = []; let gap = false;
  for (const input of checked.cases) {
    const reserved = await readOptional(path.join(rawDir, `${input.id}.pending.json`)); const checkpoint = await readOptional(path.join(rawDir, `${input.id}.json`));
    if (reserved && (!checkpoint || reserved.captureIdentitySha256 !== identity || reserved.caseInputSha256 !== stableHash(input))) throw new Error("Unresolved or different pending case");
    if (checkpoint) {
      const { checkpointContentSha256, ...content } = checkpoint;
      if (gap || !reserved || checkpointContentSha256 !== stableHash(content) || content.captureIdentitySha256 !== identity || content.caseInputSha256 !== stableHash(input) || stableHash(content.input) !== stableHash(input) || content.originalQueryStartedAt !== reserved.originalQueryStartedAt || content.status !== "complete") throw new Error("Checkpoint hash/input/prefix mismatch");
      observationGuard(content.rawHitlistObservation, input); completed.push({ input, checkpoint });
    } else gap = true;
  }
  const manifestPath = path.join(phaseDir, "raw-manifest.json"); const priorManifest = await readOptional(manifestPath);
  const indexRows = async () => Promise.all(checked.cases.map(async (row) => ({ id: row.id, file: `raw/${row.id}.json`, sha256: sha(await readFile(path.join(rawDir, `${row.id}.json`))) })));
  if (priorManifest) {
    if (priorManifest.status !== "complete" || priorManifest.captureIdentitySha256 !== identity || completed.length !== checked.cases.length || stableHash(priorManifest.cases) !== stableHash(await indexRows())) throw new Error("Complete manifest/checkpoint hash mismatch");
    return { ...priorManifest, status: "cached-complete", reusedCases: completed.length, currentInvocationTransport: { physicalAttempts: 0, cacheHits: 0, observations: [] } };
  }
  if (start && alive(start.pid)) throw new Error("Original capture PID is live or cannot be disproved");
  if (!start && completed.length) throw new Error("Checkpoint prefix has no original run-start");
  if (!start) await writeNew(startPath, { schema_version: 1, status: "running", pid: process.pid, startedAt: new Date().toISOString(), captureIdentitySha256: identity, binding, sourcePins: runtime.pins });
  else { await mkdir(path.join(phaseDir, "resumes"), { recursive: true }); await writeNew(path.join(phaseDir, "resumes", `${randomUUID()}.json`), { pid: process.pid, resumedAt: new Date().toISOString(), originalRunStartSha256: sha(await readFile(startPath)), captureIdentitySha256: identity, verifiedCompletePrefix: completed.map(({ input }) => input.id), matchingCompletePendingRecovered: completed.length }); }
  let adapter, transport, failed = false, current;
  try {
    if (completed.length < checked.cases.length) {
      transport = createTransport({ runDir: settings.runDir, endpoints: runtime.rules, nativeFetch, python: path.join(root, "experiments/.venv/bin/python"), probe: false });
      const logical = ["https://qmd-reuse.invalid/v1/embeddings", "https://qmd-reuse.invalid/v1/chat/completions", "https://qmd-reuse.invalid/v1/systemone"];
      const mapped = async (url, init) => {
        if (failed) throw new Error("Capture transport is stopped after its first failure");
        const key = ["embedding", "expansion", "jev"][logical.indexOf(String(url))];
        if (!key) { failed = true; throw new Error("Unexpected logical capture endpoint"); }
        const destination = settings.endpoints[key]; const headers = new Headers(init.headers); headers.delete("authorization"); if (destination.apiKey) headers.set("authorization", `Bearer ${destination.apiKey}`);
        try { const response = await transport(destination.url, { ...init, headers }); if (!response.ok) { failed = true; throw new Error("Capture transport returned HTTP failure"); } return response; } catch (error) { failed = true; throw error; }
      };
      adapter = await createAdapter({ root, profileDir: path.join(settings.runDir, "qmd-public"), dataRoot: path.join(settings.runDir, "replay-runtime"), resolvedConfig: runtime.resolvedConfig, fetchImpl: mapped, offline: false });
      for (const input of checked.cases.slice(completed.length)) {
        current = input; const originalQueryStartedAt = new Date().toISOString();
        await writeNew(path.join(rawDir, `${input.id}.pending.json`), { captureIdentitySha256: identity, caseInputSha256: stableHash(input), pid: process.pid, originalQueryStartedAt });
        const before = structuredClone(transport.stats);
        const observation = observationGuard(await adapter.retrieve({ query: input.latest, ...(input.conversation === undefined ? {} : { conversation: input.conversation }) }), input);
        if (failed) throw new Error("A model/schema failure was caught internally by retrieval");
        const content = { schema_version: 1, status: "complete", captureIdentitySha256: identity, caseInputSha256: stableHash(input), binding, input, originalQueryStartedAt, rawHitlistObservation: observation, transportObservations: structuredClone(transport.stats.observations?.slice(before.observations?.length ?? 0) ?? []), transportCounts: { physicalAttempts: transport.stats.physicalAttempts - before.physicalAttempts, cacheHits: transport.stats.cacheHits - before.cacheHits } };
        await writeNew(path.join(rawDir, `${input.id}.json`), { ...content, checkpointContentSha256: stableHash(content) });
      }
    }
    const manifest = { schema_version: 1, status: "complete", phase: settings.phase, completedAt: new Date().toISOString(), captureIdentitySha256: identity, binding, sourcePins: runtime.pins, cases: await indexRows(), currentInvocationTransport: transport?.stats ?? { physicalAttempts: 0, cacheHits: 0, observations: [] }, scope: "Frozen public raw retrieval only; no labels, Decision, private experience or graph imported." };
    await writeNew(manifestPath, manifest); return manifest;
  } catch {
    await writeNew(path.join(phaseDir, "failed-run.json"), { schema_version: 1, status: "failed", failedAt: new Date().toISOString(), caseId: current?.id ?? null, captureIdentitySha256: identity, binding, failure: "capture-transport-schema-or-checkpoint-failure", transport: transport?.stats ?? null });
    throw new Error("Pilot capture stopped; failed/pending artifacts preserved for inspection");
  } finally { await adapter?.close(); }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  readJsonStdin().then(capturePilot).then((result) => console.log(JSON.stringify({ status: result.status, phase: result.phase, cases: result.cases.length, currentInvocationTransport: result.currentInvocationTransport ?? null }))).catch(() => { console.error("Pilot capture stopped; inspect phase artifacts. Credentials/provider details omitted."); process.exitCode = 1; });
}
