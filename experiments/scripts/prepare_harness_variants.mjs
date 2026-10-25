/** Frozen local candidate-input preparation. No labels, models or live config. */
import { createHash, randomUUID } from "node:crypto";
import { mkdir, readFile, readdir, rm, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createFrozenFusionReplay } from "./harness_fusion.mjs";
import { loadInstalledRetrievalSources } from "./harness_retrieval_adapter.mjs";
import { deriveMatchedSnippets, selectionParams, SNIPPET_POLICY } from "./select_harness_candidates.mjs";
import { stableHash } from "./capture_harness_pilot.mjs";
import { readJsonStdin } from "./json_stdin.mjs";

const root = fileURLToPath(new URL("../../", import.meta.url));
const canonicalRun = path.join(root, "experiments/datasets/harness-quality-20261025");
const sha = (value) => createHash("sha256").update(value).digest("hex");
const json = async (filename) => JSON.parse(await readFile(filename, "utf8"));
const optional = async (filename) => { try { return await json(filename); } catch (error) { if (error.code !== "ENOENT") throw error; } };
const writeNew = (filename, value) => writeFile(filename, JSON.stringify(value, null, 2) + "\n", { flag: "wx" });
const inside = (base, filename) => { const relative = path.relative(base, filename); return relative && !relative.startsWith("..") && !path.isAbsolute(relative); };
function project(row) {
  if (!/^[A-Za-z0-9_-]+$/.test(row?.id) || typeof row.latest !== "string" || !row.latest.trim()) throw new Error("Invalid public case");
  const result = { id: row.id, latest: row.latest };
  if (row.conversation !== undefined) { if (!Array.isArray(row.conversation) || row.conversation.some((turn) => !["user", "assistant"].includes(turn.role) || typeof (turn.text ?? turn.content) !== "string")) throw new Error("Invalid public conversation"); result.conversation = row.conversation.map((turn) => ({ role: turn.role, text: turn.text ?? turn.content })); }
  return result;
}

async function verifyInputs(settings, fixturePath) {
  const runDir = path.resolve(settings.runDir);
  if (!inside(path.join(root, "experiments/datasets"), runDir) || !["development", "holdout"].includes(settings.phase)) throw new Error("Invalid variant phase/run directory");
  const { fusion, poolLimit, snippet } = settings.variant ?? {};
  if (!["current-max", "skill-identity-sum"].includes(fusion) || ![6, 10, 20].includes(poolLimit) || !["none", "matched-reference"].includes(snippet)) throw new Error("Unsupported frozen variant");
  const config = { fusion, poolLimit, snippet, ...(snippet === "matched-reference" ? { snippetPolicy: SNIPPET_POLICY } : {}) };
  const fixtureBytes = await readFile(fixturePath);
  if (sha(fixtureBytes) !== settings.expectedCasesSha256) throw new Error("Public fixture SHA mismatch");
  const parsed = JSON.parse(fixtureBytes); const all = (parsed.cases ?? parsed).map(project); const byId = new Map(all.map((row) => [row.id, row]));
  if (all.length !== 180 || byId.size !== 180) throw new Error("Expected all180 unique public cases");
  const phaseDir = path.join(runDir, settings.phase);
  if (await optional(path.join(phaseDir, "failed-run.json"))) throw new Error("Failed raw capture cannot supply variant inputs");
  const rawBytes = await readFile(path.join(phaseDir, "raw-manifest.json")); const manifest = JSON.parse(rawBytes);
  if (manifest.status !== "complete" || manifest.phase !== settings.phase || manifest.binding?.phase !== settings.phase || manifest.cases?.length !== (settings.phase === "development" ? 120 : 60) || manifest.binding?.casesSha256 !== settings.expectedCasesSha256 || manifest.binding.sourcePinsSha256 !== stableHash(manifest.sourcePins) || manifest.captureIdentitySha256 !== stableHash(manifest.binding)) throw new Error("Frozen raw manifest status/phase/binding mismatch");
  const selected = manifest.cases.map(({ id }) => byId.get(id));
  if (selected.some((row) => !row) || new Set(selected.map(({ id }) => id)).size !== selected.length || stableHash(selected) !== manifest.binding.selectedCasesSha256) throw new Error("Exact selected phase cases/order differ from capture binding");
  const checkpoints = [];
  for (const [index, entry] of manifest.cases.entries()) {
    const input = selected[index];
    if (entry.file !== `raw/${input.id}.json`) throw new Error("Unsafe or unexpected raw checkpoint path");
    const bytes = await readFile(path.join(phaseDir, entry.file)); const checkpoint = JSON.parse(bytes); const { checkpointContentSha256, ...content } = checkpoint;
    const observation = content.rawHitlistObservation;
    if (sha(bytes) !== entry.sha256 || checkpointContentSha256 !== stableHash(content) || content.status !== "complete" || content.captureIdentitySha256 !== manifest.captureIdentitySha256 || stableHash(content.binding) !== stableHash(manifest.binding) || content.caseInputSha256 !== stableHash(input) || stableHash(content.input) !== stableHash(input) || observation?.status !== "completed" || observation.query !== input.latest || !Array.isArray(observation.rawHitlists) || observation.additionalSources?.experiences !== "unavailable-not-imported" || observation.additionalSources?.graph !== "unavailable-not-imported" || (observation.relationEvidence?.length ?? 0) !== 0 || ["expected", "ground_truth_skill", "acceptable_sets", "kind", "family", "labels", "pass"].some((key) => Object.hasOwn(observation, key))) throw new Error("Raw checkpoint hash/input/source mismatch");
    checkpoints.push(observation);
  }
  let challengerConfigSha256 = null;
  if (settings.phase === "holdout") {
    const bytes = await readFile(path.join(runDir, "challenger-config.json")); const frozen = JSON.parse(bytes);
    if (sha(bytes) !== settings.challengerConfigSha256 || frozen.schema_version !== 1 || frozen.status !== "frozen" || frozen.m1CasesSha256 !== settings.expectedCasesSha256 || !/^[a-f0-9]{64}$/.test(frozen.m1LabelsSha256) || !/^[a-f0-9]{64}$/.test(frozen.contractSha256) || ![frozen.baseline, frozen.challenger].some((value) => stableHash(value) === stableHash(config))) throw new Error("Holdout variant differs from frozen challenger config/hash");
    challengerConfigSha256 = sha(bytes);
    if (manifest.binding.challengerConfigSha256 !== challengerConfigSha256) throw new Error("Holdout raw capture used a different challenger freeze");
  }
  const m0Bytes = await readFile(path.join(runDir, "m0-query-probes.json")); const m0 = JSON.parse(m0Bytes).raw_hitlists;
  if (sha(m0Bytes) !== manifest.sourcePins?.m0RawSha256) throw new Error("M0 policy source differs from frozen raw capture");
  const installedRoot = path.join(os.homedir(), ".openclaw/extensions/skill-harness");
  for (const source of m0.provenance.sources) if (!inside(installedRoot, source.path) || !/\.(m?js|json)$/.test(source.path) || sha(await readFile(source.path)) !== source.sha256) throw new Error("Installed source differs from frozen M0 policy");
  return { runDir, phaseDir, config, selected, checkpoints, manifest, rawManifestSha256: sha(rawBytes), m0, m0Sha256: sha(m0Bytes), challengerConfigSha256 };
}

async function verifyPublicProfile(input, profileDir) {
  const expected = input.manifest.sourcePins.profileDatabaseSha256 ?? input.m0.profile?.databaseSha256;
  if (!expected || sha(await readFile(path.join(profileDir, "skill-search.sqlite"))) !== expected || expected !== input.m0.profile?.databaseSha256) throw new Error("Public profile differs from frozen raw capture/M0");
  const sources = await loadInstalledRetrievalSources({ offline: true });
  let count = 0;
  for (const name of await readdir(path.join(root, "skills"))) {
    let raw; try { raw = await readFile(path.join(root, "skills", name, "SKILL.md"), "utf8"); } catch (error) { if (["ENOENT", "ENOTDIR"].includes(error.code)) continue; throw error; }
    const parsed = sources.matter(raw); const body = parsed.content.trim(); count++;
    if (await readFile(path.join(profileDir, "docs/meta", sources.safePathSegment(name), "meta.md"), "utf8") !== `# ${name}\n\n${parsed.data.description.trim()}\n` || await readFile(path.join(profileDir, "docs/body", sources.safePathSegment(name), "SKILL.md"), "utf8") !== (body ? body + "\n" : "")) throw new Error("Public skill metadata/body differs from frozen profile");
  }
  if (count !== 963) throw new Error("Public profile must retain all963 skills");
}

export async function prepareVariantInputs(settings, { fixturePath = path.join(root, "experiments/fixtures/harness_pilot_cases.json"), createReplay = createFrozenFusionReplay, profileDir } = {}) {
  const input = await verifyInputs(settings, fixturePath);
  profileDir ??= path.join(input.runDir, "qmd-public");
  if (createReplay === createFrozenFusionReplay) await verifyPublicProfile(input, profileDir);
  const helperSources = await Promise.all(["prepare_harness_variants.mjs", "harness_fusion.mjs", "harness_retrieval_adapter.mjs", "select_harness_candidates.mjs", "capture_harness_pilot.mjs", "json_stdin.mjs"].map(async (filename) => ({ path: filename, sha256: sha(await readFile(new URL(filename, import.meta.url))) })));
  const binding = { phase: settings.phase, variant: input.config, publicCasesSha256: settings.expectedCasesSha256, selectedCasesSha256: stableHash(input.selected), rawManifestSha256: input.rawManifestSha256, policySha256: input.manifest.binding.policySha256, replayPolicySha256: stableHash(input.m0.policies), m0Sha256: input.m0Sha256, helperSources, challengerConfigSha256: input.challengerConfigSha256 };
  const identity = stableHash(binding); const name = `${input.config.fusion}-pool${input.config.poolLimit}-${input.config.snippet}`;
  const directory = path.join(input.phaseDir, "variants"); await mkdir(directory, { recursive: true });
  const artifactPath = path.join(directory, `${name}.json`); const pendingPath = path.join(directory, `${name}.pending.json`); const failurePath = path.join(directory, `${name}.failed.json`);
  if (await optional(failurePath)) throw new Error("A failed variant artifact is preserved; no automatic retry");
  const prior = await optional(artifactPath); const pending = await optional(pendingPath);
  if (prior) { const { artifactContentSha256, ...content } = prior; if (!pending || pending.inputIdentitySha256 !== identity || prior.status !== "complete" || prior.inputIdentitySha256 !== identity || artifactContentSha256 !== stableHash(content)) throw new Error("Cached variant hash/input identity mismatch"); return { ...prior, status: "cached-complete", artifactPath }; }
  if (pending) throw new Error("An unfinished variant artifact is preserved; no automatic retry");
  await writeNew(pendingPath, { schema_version: 1, inputIdentitySha256: identity, binding, startedAt: new Date().toISOString() });
  let replay, current, fixtureRoot;
  try {
    fixtureRoot = path.join(canonicalRun, "replay-runtime/variant-fixtures", randomUUID());
    replay = await createReplay({ config: input.m0.policies, root, profileDir, fixtureRoot });
    const snippets = input.config.snippet === "matched-reference" ? await loadInstalledRetrievalSources({ offline: true }) : undefined;
    const replayCases = [], candidateStages = [];
    for (const [index, source] of input.selected.entries()) {
      current = source.id; const observation = input.checkpoints[index];
      const ranked = await replay.rankFrozenCandidates({ observation, fusion: input.config.fusion, poolLimit: input.config.poolLimit });
      const top20 = input.config.poolLimit === 20 ? ranked : await replay.rankFrozenCandidates({ observation, fusion: input.config.fusion, poolLimit: 20 });
      if (ranked.metadata.injectionCap !== 6 || ranked.additionalSources?.experiences !== "unavailable-not-imported" || ranked.additionalSources?.graph !== "unavailable-not-imported" || ranked.relationEvidence.length) throw new Error("Replay changed frozen cap or unavailable additional sources");
      const params = selectionParams(source, { candidateSkills: ranked.candidateSkills, candidateSources: ranked.candidateSources, candidateExperiences: [], relationEvidence: ranked.relationEvidence });
      const matchedSnippets = snippets ? deriveMatchedSnippets({ candidateSkills: params.candidateSkills, rawHitlistObservation: observation, decodeIdentity: snippets.skillIdentityFromDocsPath, docsRoot: path.join(input.runDir, "qmd-public/docs") }) : undefined;
      replayCases.push({ id: source.id, params, rawHitlistObservation: observation, ...(matchedSnippets ? { matchedSnippets } : {}) });
      const passed = new Set(ranked.retrievalCandidates.map((row) => row.skillName)); const pool = new Set(ranked.skillHits.map((row) => row.name));
      candidateStages.push({ id: source.id, injectionCap: 6, directPoolLimit: input.config.poolLimit, rankCoverageLimit: 20, skillHitsAfterPool: ranked.skillHits.map(({ name, score, semanticScore }) => ({ name, score, semanticScore: semanticScore ?? null })), poolExcludedWithinTop20: top20.skillHits.filter((row) => !pool.has(row.name)).map(({ name }) => name), semanticGatePassed: [...passed], semanticGateDropped: ranked.skillHits.filter((row) => !passed.has(row.name)).map(({ name, semanticScore }) => ({ name, semanticScore: semanticScore ?? null, reason: semanticScore === undefined ? "missing-semantic-score" : "below-rounded-threshold" })), nameCandidates: ranked.nameCandidates.map((row) => row.skillName), unionCandidates: params.candidateSkills.map((row) => row.name), rankMetadata: ranked.metadata });
    }
    const content = { schema_version: 1, status: "complete", completedAt: new Date().toISOString(), inputIdentitySha256: identity, binding, phase: settings.phase, variant: name, config: input.config, policy: structuredClone(input.m0.policies), timeoutMs: 8000, expectedCasesSha256: settings.expectedCasesSha256, expectedRawManifestSha256: input.rawManifestSha256, challengerConfigSha256: input.challengerConfigSha256, cases: input.selected, replayCases, candidateStages, scope: "Frozen local candidate preparation only; no labels, quality results, Decision or model requests." };
    const artifact = { ...content, artifactContentSha256: stableHash(content) }; await writeNew(artifactPath, artifact); return { ...artifact, artifactPath };
  } catch {
    await writeNew(failurePath, { schema_version: 1, status: "failed", inputIdentitySha256: identity, caseId: current ?? null, failure: "frozen-input-or-replay-failure" }); throw new Error("Variant input preparation stopped; failed artifact preserved");
  } finally { await replay?.close(); if (fixtureRoot) await rm(fixtureRoot, { recursive: true, force: true }); }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  readJsonStdin().then(prepareVariantInputs).then((result) => console.log(JSON.stringify({ status: result.status, variant: result.variant, phase: result.phase, cases: result.replayCases.length, artifactPath: result.artifactPath, expectedRawManifestSha256: result.expectedRawManifestSha256 }))).catch(() => { console.error("Variant input preparation stopped; inspect frozen inputs/artifacts."); process.exitCode = 1; });
}
