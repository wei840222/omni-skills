import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { mkdir, mkdtemp, readFile, readdir, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { capturePilot, stableHash } from "../scripts/capture_harness_pilot.mjs";

const root = fileURLToPath(new URL("../../", import.meta.url));
const fixturePath = path.join(root, "experiments/fixtures/harness_pilot_cases.json");
const fixtureBytes = await readFile(fixturePath);
const publicCases = JSON.parse(fixtureBytes).cases;
const partitions = { development: publicCases.slice(0, 120).map((row) => row.id), holdout: publicCases.slice(120).map((row) => row.id) };
const parent = path.join(root, "experiments/datasets/pilot-capture-tests");
await mkdir(parent, { recursive: true });
const sha = (value) => createHash("sha256").update(value).digest("hex");

async function setup(t, phase = "development") {
  const runDir = await mkdtemp(path.join(parent, "run-"));
  t.after(() => rm(runDir, { recursive: true, force: true }));
  const settings = { runDir, phase, expectedCasesSha256: sha(fixtureBytes), casePartitions: partitions,
    cases: publicCases.filter((row) => partitions[phase].includes(row.id)), policy: { fixture: true },
    models: { jev: "jev-latest", jevResolved: "jev-1.14.0", expansion: "gemini-3.5-flash-lite", expansionResolved: "gemini-3.5-flash-lite" },
    endpoints: Object.fromEntries(["embedding", "expansion", "jev"].map((key) => [key, { url: `https://example.invalid/${key}`, apiKey: "DO_NOT_SAVE_KEY" }])) };
  let calls = 0;
  const received = [];
  const dependencies = { fixturePath, prepareRuntime: async () => ({ pins: { installed: "fixed-source", corpus: "fixed-corpus" }, resolvedConfig: {}, rules: [] }),
    createTransport: () => Object.assign(async () => { throw new Error("No transport fixture configured"); }, { stats: { physicalAttempts: 0, cacheHits: 0, observations: [] } }),
    createAdapter: async () => ({ retrieve: async (input) => {
      calls++; received.push(input);
      return { query: input.query, status: "completed", rawHitlists: ["skill-meta", "skill-body", "skill-references"].map((collection) => ({ options: { collection, rerank: false, limit: 40 }, hits: [], stages: [] })), skillHits: [], requests: [], additionalSources: { experiences: "unavailable-not-imported", graph: "unavailable-not-imported" } };
    }, close: async () => {} }) };
  return { settings, dependencies, received, calls: () => calls };
}

test("development projects only public query/history and a full successful resume has zero calls", async (t) => {
  const fixture = await setup(t);
  fixture.settings.cases = fixture.settings.cases.map((row) => ({ ...row, expected: "LABEL_SENTINEL", kind: "LABEL_SENTINEL" }));
  const result = await capturePilot(fixture.settings, fixture.dependencies);
  assert.equal(result.status, "complete");
  assert.equal(result.cases.length, 120);
  assert.equal(fixture.calls(), 120);
  assert.ok(fixture.received.every((input) => Object.keys(input).every((key) => ["query", "conversation"].includes(key))));
  const checkpoint = await readFile(path.join(fixture.settings.runDir, "development/raw/p001.json"), "utf8");
  assert.equal(checkpoint.includes("LABEL_SENTINEL"), false);
  assert.equal(checkpoint.includes("DO_NOT_SAVE_KEY"), false);
  const cached = await capturePilot(fixture.settings, fixture.dependencies);
  assert.equal(cached.status, "cached-complete");
  assert.equal(fixture.calls(), 120);
});

test("phase membership, fixture SHA and public content mismatches stop before adapter creation", async (t) => {
  const fixture = await setup(t);
  await assert.rejects(capturePilot({ ...fixture.settings, expectedCasesSha256: "0".repeat(64) }, fixture.dependencies), /fixture/);
  const bad = structuredClone(fixture.settings); bad.cases[0].latest += " changed";
  await assert.rejects(capturePilot(bad, fixture.dependencies), /public case/);
  await assert.rejects(capturePilot({ ...fixture.settings, cases: fixture.settings.cases.slice(1) }, fixture.dependencies), /phase/);
  assert.equal(fixture.calls(), 0);
});

test("holdout requires the exact frozen challenger config and binds its case hash", async (t) => {
  const fixture = await setup(t, "holdout");
  fixture.settings.challengerConfigSha256 = "0".repeat(64);
  await assert.rejects(capturePilot(fixture.settings, fixture.dependencies));
  const challenger = { schema_version: 1, status: "frozen", m1CasesSha256: fixture.settings.expectedCasesSha256, m1LabelsSha256: "1".repeat(64), contractSha256: "2".repeat(64), baseline: { fusion: "current-max", poolLimit: 6, snippet: false }, challenger: { fusion: "skill-identity-sum", poolLimit: 10, snippet: false } };
  const bytes = JSON.stringify(challenger);
  await writeFile(path.join(fixture.settings.runDir, "challenger-config.json"), bytes);
  fixture.settings.challengerConfigSha256 = sha(bytes);
  const result = await capturePilot(fixture.settings, fixture.dependencies);
  assert.equal(result.cases.length, 60);
  await writeFile(path.join(fixture.settings.runDir, "challenger-config.json"), bytes + "\n");
  await assert.rejects(capturePilot(fixture.settings, fixture.dependencies), /challenger/);
  assert.equal(fixture.calls(), 60);
});

test("schema/unavailable status stops the phase and creates an immutable failed marker", async (t) => {
  const fixture = await setup(t);
  fixture.dependencies.createAdapter = async () => ({ retrieve: async () => ({ status: "unavailable" }), close: async () => {} });
  await assert.rejects(capturePilot(fixture.settings, fixture.dependencies), /stopped/);
  const failure = JSON.parse(await readFile(path.join(fixture.settings.runDir, "development/failed-run.json")));
  assert.equal(failure.status, "failed");
  await assert.rejects(capturePilot(fixture.settings, fixture.dependencies), /failed|pending/);
});

test("live PID and unresolved pending refuse resume; verified complete prefix resumes only new cases", async (t) => {
  const fixture = await setup(t);
  await capturePilot(fixture.settings, fixture.dependencies);
  const phaseDir = path.join(fixture.settings.runDir, "development");
  await rm(path.join(phaseDir, "raw-manifest.json"));
  for (const name of await readdir(path.join(phaseDir, "raw"))) if (!name.startsWith("p001.")) await rm(path.join(phaseDir, "raw", name));
  await assert.rejects(capturePilot(fixture.settings, fixture.dependencies), /live|PID/);
  const start = JSON.parse(await readFile(path.join(phaseDir, "run-start.json")));
  start.pid = 2147483647;
  await writeFile(path.join(phaseDir, "run-start.json"), JSON.stringify(start));
  const result = await capturePilot(fixture.settings, fixture.dependencies);
  assert.equal(result.status, "complete");
  assert.equal(fixture.calls(), 239); // one verified checkpoint was never replayed
  await rm(path.join(phaseDir, "raw-manifest.json"));
  await rm(path.join(phaseDir, "raw/p002.json"));
  await assert.rejects(capturePilot(fixture.settings, fixture.dependencies), /pending|prefix/);
});

test("tampered complete checkpoints cannot be reused or converted into misses", async (t) => {
  const fixture = await setup(t);
  await capturePilot(fixture.settings, fixture.dependencies);
  const filename = path.join(fixture.settings.runDir, "development/raw/p001.json");
  const checkpoint = JSON.parse(await readFile(filename)); checkpoint.input.latest = "changed";
  await writeFile(filename, JSON.stringify(checkpoint));
  await assert.rejects(capturePilot(fixture.settings, fixture.dependencies), /checkpoint/i);
  assert.equal(fixture.calls(), 120);
  assert.equal(typeof stableHash({ public: true }), "string");
});

test("consumer schema failure remains fatal even if QMD would catch it and return lexical hits", async (t) => {
  const fixture = await setup(t);
  fixture.dependencies.createTransport = () => Object.assign(async () => { throw new Error("consumer validation failed"); }, { stats: { physicalAttempts: 0, cacheHits: 0, observations: [] } });
  fixture.dependencies.createAdapter = async ({ fetchImpl }) => ({ retrieve: async ({ query }) => {
    try { await fetchImpl("https://qmd-reuse.invalid/v1/systemone", { method: "POST", body: '{}' }); } catch {}
    return { query, status: "completed", rawHitlists: ["skill-meta", "skill-body", "skill-references"].map((collection) => ({ options: { collection, rerank: false }, hits: [] })), additionalSources: { experiences: "unavailable-not-imported", graph: "unavailable-not-imported" } };
  }, close: async () => {} });
  await assert.rejects(capturePilot(fixture.settings, fixture.dependencies), /stopped/);
  assert.equal((await readdir(path.join(fixture.settings.runDir, "development/raw"))).length, 1);
});

test("per-case original service observations preserve unknown as null and use the global ledger mode", async (t) => {
  const fixture = await setup(t);
  fixture.dependencies.createTransport = ({ probe }) => {
    assert.equal(probe, false);
    const stats = { physicalAttempts: 0, cacheHits: 0, observations: [] };
    return Object.assign(async () => { stats.cacheHits++; stats.observations.push({ key: "public-cache-key", provider: "embedding", source: "cache", originalServiceMs: null, billedTokens: 12 }); return Response.json({ public: true }); }, { stats });
  };
  const factory = fixture.dependencies.createAdapter;
  fixture.dependencies.createAdapter = async ({ fetchImpl }) => {
    const adapter = await factory();
    return { ...adapter, retrieve: async (input) => { await fetchImpl("https://qmd-reuse.invalid/v1/embeddings", { method: "POST", body: '{}' }); return adapter.retrieve(input); } };
  };
  await capturePilot(fixture.settings, fixture.dependencies);
  const checkpoint = JSON.parse(await readFile(path.join(fixture.settings.runDir, "development/raw/p001.json")));
  assert.equal(checkpoint.transportObservations[0].originalServiceMs, null);
  assert.equal(checkpoint.transportCounts.cacheHits, 1);
  const cached = await capturePilot(fixture.settings, fixture.dependencies);
  assert.equal(cached.currentInvocationTransport.physicalAttempts, 0);
});
