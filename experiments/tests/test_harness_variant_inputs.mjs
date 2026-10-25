import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { prepareVariantInputs } from "../scripts/prepare_harness_variants.mjs";
import { stableHash } from "../scripts/capture_harness_pilot.mjs";
import { SNIPPET_POLICY } from "../scripts/select_harness_candidates.mjs";

const root = fileURLToPath(new URL("../../", import.meta.url));
const run = path.join(root, "experiments/datasets/harness-quality-20261025");
const parent = path.join(root, "experiments/datasets/variant-input-tests");
await mkdir(parent, { recursive: true });
const originalM0 = JSON.parse(await readFile(path.join(run, "m0-query-probes.json"), "utf8")).raw_hitlists;
const sha = (value) => createHash("sha256").update(value).digest("hex");
const empty = (query) => ({ query, status: "completed", rawHitlists: ["skill-meta", "skill-body", "skill-references"].map((collection) => ({ options: { collection, limit: 40, candidateLimit: 40, rerank: false, explain: true }, hits: [] })), additionalSources: { experiences: "unavailable-not-imported", graph: "unavailable-not-imported" }, relationEvidence: [] });

async function setup(t, { phase = "development", actualM0 = false } = {}) {
  const runDir = await mkdtemp(path.join(parent, "run-"));
  t.after(() => rm(runDir, { recursive: true, force: true }));
  const cases = Array.from({ length: 180 }, (_, index) => ({ id: `v${String(index + 1).padStart(3, "0")}`, latest: `這是第${index + 1}個公開案例` }));
  const realObservation = originalM0.observations[1];
  if (actualM0) cases[0].latest = realObservation.query;
  const fixturePath = path.join(runDir, "public-cases.json");
  const fixtureBytes = JSON.stringify({ cases }); await writeFile(fixturePath, fixtureBytes);
  const selected = phase === "development" ? cases.slice(0, 120) : cases.slice(120);
  const m0Bytes = JSON.stringify({ raw_hitlists: { policies: originalM0.policies, provenance: originalM0.provenance, profile: originalM0.profile } });
  await writeFile(path.join(runDir, "m0-query-probes.json"), m0Bytes);
  const sourcePins = { m0RawSha256: sha(m0Bytes) };
  const binding = { phase, casesSha256: sha(fixtureBytes), selectedCasesSha256: stableHash(selected), partitionsSha256: "1".repeat(64), policySha256: "2".repeat(64), sourcePinsSha256: stableHash(sourcePins), challengerConfigSha256: null };
  const identity = stableHash(binding);
  const rawDir = path.join(runDir, phase, "raw"); await mkdir(rawDir, { recursive: true });
  const entries = [];
  for (const [index, input] of selected.entries()) {
    const content = { schema_version: 1, status: "complete", captureIdentitySha256: identity, binding, caseInputSha256: stableHash(input), input, originalQueryStartedAt: "2026-10-25T00:00:00.000Z", rawHitlistObservation: actualM0 && index === 0 ? realObservation : empty(input.latest) };
    const bytes = JSON.stringify({ ...content, checkpointContentSha256: stableHash(content) });
    await writeFile(path.join(rawDir, `${input.id}.json`), bytes); entries.push({ id: input.id, file: `raw/${input.id}.json`, sha256: sha(bytes) });
  }
  const manifest = { schema_version: 1, status: "complete", phase, captureIdentitySha256: identity, binding, sourcePins, cases: entries };
  await writeFile(path.join(runDir, phase, "raw-manifest.json"), JSON.stringify(manifest));
  let calls = 0;
  const createReplay = async () => ({ close: async () => {}, rankFrozenCandidates: async ({ poolLimit, fusion }) => {
    calls++;
    return { skillHits: [{ name: "aave", score: 0.04, semanticScore: 0.9 }, { name: "academy", score: 0.03, semanticScore: 0.1 }], retrievalCandidates: [{ skillName: "aave", score: 0.9 }], nameCandidates: [], candidateSkills: [{ name: "aave", description: "Public scope", expected: "LABEL_SENTINEL" }], candidateSources: { aave: ["direct-retrieval"] }, relationEvidence: [], additionalSources: { experiences: "unavailable-not-imported", graph: "unavailable-not-imported" }, metadata: { fusion, poolLimit, injectionCap: 6 } };
  } });
  return { settings: { runDir, phase, expectedCasesSha256: sha(fixtureBytes), variant: { fusion: "current-max", poolLimit: 6, snippet: "none" } }, fixturePath, createReplay, calls: () => calls, cases, manifest };
}

async function rewriteCheckpoint(fixture, index, change) {
  const phaseDir = path.join(fixture.settings.runDir, fixture.settings.phase);
  const entry = fixture.manifest.cases[index]; const checkpoint = JSON.parse(await readFile(path.join(phaseDir, entry.file)));
  const { checkpointContentSha256, ...content } = checkpoint; change(content);
  const bytes = JSON.stringify({ ...content, checkpointContentSha256: stableHash(content) });
  await writeFile(path.join(phaseDir, entry.file), bytes); entry.sha256 = sha(bytes);
  await writeFile(path.join(phaseDir, "raw-manifest.json"), JSON.stringify(fixture.manifest));
}

test("public variant inputs bind raw hashes, project candidate fields and retain gate losses", async (t) => {
  const fixture = await setup(t);
  const result = await prepareVariantInputs(fixture.settings, { fixturePath: fixture.fixturePath, createReplay: fixture.createReplay });
  assert.equal(result.status, "complete"); assert.equal(result.replayCases.length, 120);
  assert.equal(result.replayCases[0].params.latest, fixture.cases[0].latest);
  assert.equal(result.timeoutMs, 8000);
  assert.deepEqual(result.policy, originalM0.policies);
  assert.deepEqual(result.replayCases[0].params.candidateExperiences, []);
  assert.equal(JSON.stringify(result).includes("LABEL_SENTINEL"), false);
  assert.deepEqual(result.candidateStages[0].semanticGateDropped.map((hit) => hit.name), ["academy"]);
  const before = fixture.calls();
  const cached = await prepareVariantInputs(fixture.settings, { fixturePath: fixture.fixturePath, createReplay: () => { throw new Error("Cached artifact must not construct replay"); } });
  assert.equal(cached.status, "cached-complete"); assert.equal(fixture.calls(), before);
});

test("checkpoint hash tampering and fixture mismatch stop before replay", async (t) => {
  const fixture = await setup(t);
  await assert.rejects(prepareVariantInputs({ ...fixture.settings, expectedCasesSha256: "0".repeat(64) }, { fixturePath: fixture.fixturePath, createReplay: fixture.createReplay }), /fixture/);
  await writeFile(path.join(fixture.settings.runDir, "development/raw/v001.json"), '{}');
  await assert.rejects(prepareVariantInputs(fixture.settings, { fixturePath: fixture.fixturePath, createReplay: fixture.createReplay }), /checkpoint/i);
  assert.equal(fixture.calls(), 0);
});

test("holdout only accepts the exact frozen baseline/challenger variant", async (t) => {
  const fixture = await setup(t, { phase: "holdout" });
  await assert.rejects(prepareVariantInputs(fixture.settings, { fixturePath: fixture.fixturePath, createReplay: fixture.createReplay }));
  const bytes = JSON.stringify({ schema_version: 1, status: "frozen", m1CasesSha256: fixture.settings.expectedCasesSha256, m1LabelsSha256: "1".repeat(64), contractSha256: "2".repeat(64), baseline: fixture.settings.variant, challenger: { fusion: "skill-identity-sum", poolLimit: 10, snippet: "none" } });
  await writeFile(path.join(fixture.settings.runDir, "challenger-config.json"), bytes);
  fixture.settings.challengerConfigSha256 = sha(bytes);
  fixture.manifest.binding.challengerConfigSha256 = sha(bytes);
  fixture.manifest.captureIdentitySha256 = stableHash(fixture.manifest.binding);
  for (let index = 0; index < fixture.manifest.cases.length; index++) await rewriteCheckpoint(fixture, index, (content) => { content.binding = fixture.manifest.binding; content.captureIdentitySha256 = fixture.manifest.captureIdentitySha256; });
  const result = await prepareVariantInputs(fixture.settings, { fixturePath: fixture.fixturePath, createReplay: fixture.createReplay });
  assert.equal(result.replayCases.length, 60);
  await assert.rejects(prepareVariantInputs({ ...fixture.settings, variant: { fusion: "current-max", poolLimit: 20, snippet: "none" } }, { fixturePath: fixture.fixturePath, createReplay: fixture.createReplay }), /challenger/);
});

test("matched-reference delegates exact bestChunk selection to the selector helper", async (t) => {
  const fixture = await setup(t); fixture.settings.variant.snippet = "matched-reference";
  await rewriteCheckpoint(fixture, 0, (content) => { content.rawHitlistObservation.rawHitlists[1].hits = [{ file: "qmd://skill-body/aave/SKILL.md", bestChunk: "Public strongest matched chunk.", body: "A different full body must not become the snippet.", score: 0.8 }]; });
  const result = await prepareVariantInputs(fixture.settings, { fixturePath: fixture.fixturePath, createReplay: fixture.createReplay });
  assert.deepEqual(result.config.snippetPolicy, SNIPPET_POLICY);
  assert.equal(result.replayCases[0].matchedSnippets[0].text, "Public strongest matched chunk.");
  assert.equal(result.replayCases[0].matchedSnippets[0].skill, "aave");
});

test("tampered complete artifacts and standalone pending markers cannot be reused", async (t) => {
  const fixture = await setup(t);
  const result = await prepareVariantInputs(fixture.settings, { fixturePath: fixture.fixturePath, createReplay: fixture.createReplay });
  const artifact = JSON.parse(await readFile(result.artifactPath)); artifact.replayCases[0].params.latest = "changed";
  await writeFile(result.artifactPath, JSON.stringify(artifact));
  await assert.rejects(prepareVariantInputs(fixture.settings, { fixturePath: fixture.fixturePath, createReplay: fixture.createReplay }), /hash\/input/);
  const second = await setup(t); await mkdir(path.join(second.settings.runDir, "development/variants"));
  await writeFile(path.join(second.settings.runDir, "development/variants/current-max-pool6-none.pending.json"), '{}');
  await assert.rejects(prepareVariantInputs(second.settings, { fixturePath: second.fixturePath, createReplay: second.createReplay }), /unfinished/);
  assert.equal(second.calls(), 0);
});

test("failed or unfinished variant markers never resume automatically", async (t) => {
  const fixture = await setup(t);
  await assert.rejects(prepareVariantInputs(fixture.settings, { fixturePath: fixture.fixturePath, createReplay: async () => { throw new Error("Fixture replay failure"); } }), /stopped/);
  await assert.rejects(prepareVariantInputs(fixture.settings, { fixturePath: fixture.fixturePath, createReplay: fixture.createReplay }), /failed|unfinished/);
  assert.equal(fixture.calls(), 0);
});

test("one actual frozen M0 observation is replayed through installed fusion without models", async (t) => {
  const fixture = await setup(t, { actualM0: true });
  const result = await prepareVariantInputs(fixture.settings, { fixturePath: fixture.fixturePath, profileDir: path.join(run, "qmd-public") });
  assert.deepEqual(result.candidateStages[0].skillHitsAfterPool, originalM0.observations[1].skillHits.map(({ name, score, semanticScore }) => ({ name, score, semanticScore: semanticScore ?? null })));
  assert.equal(result.replayCases[0].params.candidateExperiences.length, 0);
  assert.equal(result.candidateStages[0].injectionCap, 6);
});
