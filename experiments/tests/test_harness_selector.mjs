import test from "node:test";
import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { mkdir, mkdtemp, readFile, readdir, rm, writeFile, unlink } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createControlledFetch } from "../scripts/controlled_model_fetch.mjs";
import { createHostDecisionAdapter } from "../scripts/host_decision_adapter.mjs";
import { SNIPPET_POLICY, buildReferenceSnippets, deriveMatchedSnippets, selectCandidates, selectionParams, stableHash } from "../scripts/select_harness_candidates.mjs";

const root = fileURLToPath(new URL("../..", import.meta.url));
const installed = path.join(os.homedir(), ".openclaw/extensions/skill-harness/dist/src");
const { buildSelectionBatch } = await import(pathToFileURL(path.join(installed, "classification/selection-batch.js")));
const { skillIdentityFromDocsPath } = await import(pathToFileURL(path.join(installed, "qmd/skill-index.js")));
const sha = (value) => createHash("sha256").update(value).digest("hex");
const readJson = async (filename) => JSON.parse(await readFile(filename, "utf8"));
const pins = [{ path: "synthetic-source", sha256: "a".repeat(64) }];
const prepareRuntime = async () => ({ pins, decodeIdentity: skillIdentityFromDocsPath, docsRoot: "/public/docs" });
const observation = (latest, hits = []) => ({ query: latest, rawHitlists: ["skill-meta", "skill-body", "skill-references"].map((collection) => ({ options: { collection, limit: 40, candidateLimit: 40, rerank: false, explain: true }, hits: hits.filter((hit) => hit.file.includes(`/${collection}/`)) })) });
const hit = (skill, collection, text, score = 0.8, filename = "SKILL.md") => ({ file: `qmd://${collection}/${skill}/${filename}`, bestChunk: text, score, body: "FORBIDDEN_FULL_BODY_FIRST240" });

async function fixture(t) {
  const parent = path.join(root, "experiments/datasets/selector-tests"); await mkdir(parent, { recursive: true });
  const dir = await mkdtemp(path.join(parent, "run-")); t.after(() => rm(dir, { recursive: true, force: true }));
  const cases = Array.from({ length: 180 }, (_, i) => ({ id: `p${String(i + 1).padStart(3, "0")}`, latest: `Public task ${i + 1}`, conversation: [{ role: "user", text: "Earlier public request" }] }));
  const bytes = JSON.stringify({ schema_version: 1, cases }); const fixturePath = path.join(dir, "public-cases.json"); await writeFile(fixturePath, bytes);
  const settings = { runDir: dir, phase: "development", variant: "baseline", expectedCasesSha256: sha(bytes),
    cases: cases.slice(0, 120), casePartitions: { development: cases.slice(0, 120).map(({ id }) => id), holdout: cases.slice(120).map(({ id }) => id) },
    config: { fusion: "current-max", poolLimit: 6, snippet: "none" }, models: { jev: "jev-latest", jevResolved: "jev-1.14.0" },
    timeoutMs: 8000, policy: { qmd: { timeoutMs: 15000 }, skills: { search: { collectionWeights: { meta: 3, body: 2, references: 1 } } },
      routing: { skills: { relevanceThreshold: 0.4, maxInjectedSkills: 6, search: { minCandidateScore: 0.3, timeoutMs: 15000 } } } },
    endpoints: { jev: { url: "https://fake.invalid/v1/systemone", apiKey: "SENTINEL_SECRET" } },
    replayCases: cases.slice(0, 120).map((input, i) => ({ id: input.id,
      params: { latest: "SENTINEL_WRONG_LATEST", conversation: [{ role: "assistant", text: "SENTINEL_WRONG_CONTEXT" }], expected: "SENTINEL_LABEL", family: "SENTINEL_FAMILY",
        candidateSkills: i < 2 ? [{ name: "alpha", description: "Public alpha scope", expected: "SENTINEL_NESTED" }] : [], candidateSources: { alpha: ["direct-retrieval"] } },
      rawHitlistObservation: observation(input.latest),
    })) };
  const limits = { request_cap: 200, providers: { jev: { requests: 200, tokens: 13_107_200, usd_per_million: "0.042" } } };
  await writeFile(path.join(dir, "budget-limits.json"), JSON.stringify(limits));
  await writeFile(path.join(dir, "m0-query-probes.json"), JSON.stringify({ raw_hitlists: { policies: settings.policy } }));
  async function freezeRaw() {
    const phaseDir = path.join(dir, settings.phase); const raw = path.join(phaseDir, "raw"); await mkdir(raw, { recursive: true });
    const entries = [];
    for (const input of settings.cases) {
      const replay = settings.replayCases.find(({ id }) => id === input.id);
      const content = { status: "complete", input, rawHitlistObservation: replay.rawHitlistObservation };
      const data = JSON.stringify({ ...content, checkpointContentSha256: stableHash(content) });
      await writeFile(path.join(raw, `${input.id}.json`), data);
      entries.push({ id: input.id, file: `raw/${input.id}.json`, sha256: sha(data) });
    }
    const data = JSON.stringify({ status: "complete", cases: entries }); await writeFile(path.join(phaseDir, "raw-manifest.json"), data);
    settings.expectedRawManifestSha256 = sha(data);
  }
  await freezeRaw(); return { dir, settings, fixturePath, cases, freezeRaw };
}

function fakeAdapterFactory(seen, { unavailable = false } = {}) {
  return async ({ fetchImpl }) => ({ provenance: { sources: [] }, buildSelectionBatch,
    validateWireResponse(payload, body) { assert.deepEqual(Object.keys(payload.answers), Object.keys(body.questions)); assert.equal(payload.model, "jev-1.14.0"); },
    async evaluateSelection(params, { batch, routing, timeoutMs }) {
      seen.push(structuredClone(batch)); assert.equal(routing.skills.maxInjectedSkills, 6);
      assert.equal(routing.skills.relevanceThreshold, 0.4); assert.equal(routing.skills.search.minCandidateScore, 0.3); assert.equal(timeoutMs, 8000);
      if (unavailable) return { outcome: { status: "unavailable", reason: "deadline" } };
      const body = { model: "jev-latest", state: batch.state, questions: Object.fromEntries(Object.keys(batch.questions).map((id) => [id, { type: "noul" }])) };
      const response = await fetchImpl("https://selector-replay.invalid/v1/systemone", { method: "POST", body: JSON.stringify(body) });
      const payload = await response.json();
      return { selection: { skills: params.candidateSkills.map(({ name }) => name), experiences: [] },
        outcome: { status: "ok", result: payload }, trace: { hostCalls: 1, fetchCalls: 1, legacyCalls: 0 } };
    }, async close() {} });
}

function fakeFetch(calls, probability = 0.9) {
  return async (_url, init) => {
    calls.push(init); assert.equal(new Headers(init.headers).get("authorization"), "Bearer SENTINEL_SECRET");
    const body = JSON.parse(init.body);
    assert.equal(JSON.stringify(body).includes("SENTINEL"), false);
    return Response.json({ model: "jev-1.14.0", answers: Object.fromEntries(Object.keys(body.questions).map((id) => [id, { type: "noul", noul: probability }])), usage: { input_tokens: 123, output_tokens: 5 } });
  };
}

test("matched snippets use installed exact identity and bestChunk, with deterministic UTF8 budgets", () => {
  const candidateSkills = Array.from({ length: 10 }, (_, i) => ({ name: `skill-${i}`, description: "Public" }));
  const hits = candidateSkills.flatMap(({ name }) => [hit(name, "skill-meta", "wrong meta", 1), hit(name, "skill-references", "繁😀".repeat(100), 0.8, "z.md"), hit(name, "skill-body", "正😀".repeat(100), 0.9)]);
  hits.push(hit("skill-0-extra", "skill-body", "SUBSTRING_IDENTITY_MUST_NOT_MATCH", 100));
  const raw = observation("Public", hits);
  const options = { candidateSkills, rawHitlistObservation: raw, decodeIdentity: skillIdentityFromDocsPath, docsRoot: "/public/docs" };
  const matchedSnippets = deriveMatchedSnippets(options);
  assert.equal(matchedSnippets.length, 10); assert.equal(matchedSnippets[0].text, "正😀".repeat(100));
  const snippets = buildReferenceSnippets({ ...options, matchedSnippets });
  assert.ok(snippets.utf8Bytes <= 2048); assert.ok(Object.keys(snippets.state).length < 10);
  for (const text of Object.values(snippets.state)) { assert.ok(Buffer.byteLength(text) <= 320); assert.equal(text.includes("�"), false); }
  assert.deepEqual(snippets, buildReferenceSnippets({ ...options, matchedSnippets }));
  assert.throws(() => buildReferenceSnippets({ ...options, matchedSnippets: [{ ...matchedSnippets[0], text: hits[0].body }] }), /explicitly supplied/);
});

test("selection projection and M3 preserve actual questions/conversation/associations", () => {
  const input = { latest: "Current", conversation: [{ role: "user", text: "Earlier", expected: "SENTINEL" }] };
  const params = selectionParams(input, { candidateSkills: [{ name: "alpha", description: "Scope", labels: "SENTINEL" }], candidateExperiences: [{ id: "exp", summary: "Public", skills: ["alpha"], expected: "SENTINEL" }], relationEvidence: [{ skill: "alpha", from: "alpha", to: "beta", reason: "Public reason", expected: "SENTINEL" }] });
  const batch = buildSelectionBatch(params); const enriched = structuredClone(batch); enriched.state.reference_matched_snippets = { alpha: "Matched" };
  assert.deepEqual(enriched.questions, batch.questions); const { reference_matched_snippets, ...state } = enriched.state; assert.deepEqual(state, batch.state);
  assert.equal(JSON.stringify(batch).includes("SENTINEL"), false);
  assert.deepEqual(batch.state.conversation_context, [{ role: "user", text: "Earlier" }]);
  assert.deepEqual(batch.state.skill_candidates[0].experience_ids, ["exp"]);
});

test("single variant runs controlled host calls, skips empty pools, and complete cache reuses zero attempts", async (t) => {
  const f = await fixture(t); const calls = [], seen = []; let transports = 0;
  const deps = { fixturePath: f.fixturePath, prepareRuntime, createAdapter: fakeAdapterFactory(seen), nativeFetch: fakeFetch(calls),
    createTransport(options) { transports++; assert.equal(options.probe, false); return createControlledFetch(options); } };
  const result = await selectCandidates(f.settings, deps);
  assert.equal(result.status, "complete"); assert.equal(result.skippedEmptyPools, 118); assert.equal(calls.length, 2);
  assert.equal(result.currentInvocationTransport.physicalAttempts, 2);
  assert.ok(result.currentInvocationTransport.observations.every((row) => row.billedTokens === 123 && row.originalServiceMs >= 0));
  assert.equal(seen[0].state.latest_message, "Public task 1"); assert.equal(seen[0].state.conversation_context[0].text, "Earlier public request");
  const checkpoint = await readJson(path.join(f.dir, "development/selectors/baseline/cases/p003.json"));
  assert.equal(checkpoint.status, "skipped-empty-pool"); assert.equal(checkpoint.candidate_count, 0);
  const cached = await selectCandidates(f.settings, deps);
  assert.equal(cached.status, "cached-complete"); assert.equal(cached.currentInvocationTransport.physicalAttempts, 0); assert.equal(calls.length, 2); assert.equal(transports, 1);
  const start = await readFile(path.join(f.dir, "development/selectors/baseline/run-start.json"), "utf8"); assert.equal(start.includes("SENTINEL_SECRET"), false);
  const changed = structuredClone(f.settings); changed.config.poolLimit = 10;
  await assert.rejects(selectCandidates(changed, deps), /identity changed/);
});

test("timeout/unavailable leaves pending failure and cannot become an accuracy result or auto retry", async (t) => {
  const f = await fixture(t); const calls = [];
  const deps = { fixturePath: f.fixturePath, prepareRuntime, createAdapter: fakeAdapterFactory([], { unavailable: true }), nativeFetch: fakeFetch(calls) };
  await assert.rejects(selectCandidates(f.settings, deps), /preserved/);
  assert.equal(calls.length, 0);
  const directory = path.join(f.dir, "development/selectors/baseline");
  assert.ok((await readdir(path.join(directory, "cases"))).includes("p001.pending.json"));
  assert.equal((await readdir(path.join(directory, "cases"))).includes("p001.json"), false);
  await assert.rejects(selectCandidates(f.settings, deps), /no automatic retry/);
});

test("resume requires a verified dead PID and complete prefix; cache retains original service/tokens", async (t) => {
  const f = await fixture(t); const calls = [], seen = [];
  const deps = { fixturePath: f.fixturePath, prepareRuntime, createAdapter: fakeAdapterFactory(seen), nativeFetch: fakeFetch(calls) };
  await selectCandidates(f.settings, deps);
  const directory = path.join(f.dir, "development/selectors/baseline");
  const original = await readJson(path.join(directory, "cases/p002.json"));
  await unlink(path.join(directory, "manifest.json"));
  for (const input of f.settings.cases.slice(1)) {
    await unlink(path.join(directory, `cases/${input.id}.json`));
    await unlink(path.join(directory, `cases/${input.id}.pending.json`));
  }
  await assert.rejects(selectCandidates(f.settings, deps), /PID is live/);
  const startPath = path.join(directory, "run-start.json"); const start = await readJson(startPath);
  assert.throws(() => process.kill(2147483647, 0), { code: "ESRCH" });
  await writeFile(startPath, JSON.stringify({ ...start, pid: 2147483647 }));
  const resumed = await selectCandidates(f.settings, deps);
  assert.equal(calls.length, 2); assert.equal(resumed.currentInvocationTransport.physicalAttempts, 0); assert.equal(resumed.currentInvocationTransport.cacheHits, 1);
  const checkpoint = await readJson(path.join(directory, "cases/p002.json"));
  assert.equal(checkpoint.transportObservations[0].source, "cache");
  assert.equal(checkpoint.transportObservations[0].originalServiceMs, original.transportObservations[0].originalServiceMs);
  assert.equal(checkpoint.transportObservations[0].billedTokens, 123);
});

test("M3 replay adds only matched snippets and raw checksum tampering is rejected", async (t) => {
  const f = await fixture(t); f.settings.variant = "m3";
  f.settings.config = { ...f.settings.config, snippet: "matched-reference", snippetPolicy: SNIPPET_POLICY };
  for (const replay of f.settings.replayCases) {
    replay.rawHitlistObservation = observation(replay.rawHitlistObservation.query, [hit("alpha", "skill-body", "Explicit matched chunk")]);
    replay.matchedSnippets = deriveMatchedSnippets({ candidateSkills: replay.params.candidateSkills, rawHitlistObservation: replay.rawHitlistObservation, decodeIdentity: skillIdentityFromDocsPath, docsRoot: "/public/docs" });
  }
  await f.freezeRaw(); const seen = [];
  const deps = { fixturePath: f.fixturePath, prepareRuntime, createAdapter: fakeAdapterFactory(seen), nativeFetch: fakeFetch([]) };
  await selectCandidates(f.settings, deps);
  assert.deepEqual(seen[0].state.reference_matched_snippets, { alpha: "Explicit matched chunk" });
  assert.equal(JSON.stringify(seen[0]).includes("FORBIDDEN_FULL_BODY"), false);
  const altered = structuredClone(f.settings); altered.replayCases[0].rawHitlistObservation.query = "Different original query";
  await assert.rejects(selectCandidates(altered, deps), /frozen raw checkpoint/);
});

test("holdout is bound to challenger SHA and raw manifest before any transport", async (t) => {
  const f = await fixture(t); f.settings.phase = "holdout"; f.settings.cases = f.cases.slice(120);
  f.settings.replayCases = f.settings.cases.map((input) => ({ id: input.id, params: { candidateSkills: [] }, rawHitlistObservation: observation(input.latest) })); await f.freezeRaw();
  const frozen = { status: "frozen", m1CasesSha256: f.settings.expectedCasesSha256, baseline: f.settings.config, challenger: { ...f.settings.config, poolLimit: 10 } };
  const bytes = JSON.stringify(frozen); await writeFile(path.join(f.dir, "challenger-config.json"), bytes);
  const deps = { fixturePath: f.fixturePath, prepareRuntime, createAdapter: fakeAdapterFactory([]), nativeFetch: async () => { throw new Error("No transport for empty holdout pools"); } };
  f.settings.challengerConfigSha256 = "a".repeat(64); await assert.rejects(selectCandidates(f.settings, deps), /challenger/);
  f.settings.challengerConfigSha256 = sha(bytes); const result = await selectCandidates(f.settings, deps); assert.equal(result.skippedEmptyPools, 60);
});

test("M0 policy and 8000ms selector timeout are mandatory before runtime or transport", async (t) => {
  const f = await fixture(t); let runtimeCalls = 0;
  const deps = { fixturePath: f.fixturePath, prepareRuntime: async () => { runtimeCalls++; return prepareRuntime(); }, nativeFetch: async () => { throw new Error("No model call"); } };
  for (const change of [
    (value) => { value.policy.routing.skills.relevanceThreshold = 0.6; },
    (value) => { value.policy.routing.skills.search.minCandidateScore = 0.8; },
    (value) => { delete value.policy; },
    (value) => { value.timeoutMs = 5000; },
    (value) => { value.timeoutMs = 300000; },
    (value) => { delete value.timeoutMs; },
  ]) {
    const settings = structuredClone(f.settings); change(settings);
    await assert.rejects(selectCandidates(settings, deps), /policy|8000/);
  }
  assert.equal(runtimeCalls, 0);
});

test("real installed host facade and strict wire validator work through fake controlled fetch", async (t) => {
  const f = await fixture(t); const calls = [];
  let host;
  const result = await selectCandidates(f.settings, { fixturePath: f.fixturePath, prepareRuntime,
    createAdapter: async (options) => {
      host = await createHostDecisionAdapter({ ...options, offline: true });
      const evaluate = host.evaluateSelection.bind(host);
      host.evaluateSelection = (params, options) => { assert.equal(options.timeoutMs, 8000); assert.deepEqual(options.routing, f.settings.policy.routing); return evaluate(params, options); };
      return host;
    }, nativeFetch: fakeFetch(calls, 0.5) });
  assert.equal(calls.length, 2); assert.equal(result.currentInvocationTransport.physicalAttempts, 2);
  const checkpoint = await readJson(path.join(f.dir, "development/selectors/baseline/cases/p001.json"));
  assert.deepEqual(checkpoint.selection.skills, ["alpha"]); assert.equal(checkpoint.trace.hostCalls, 1); assert.equal(checkpoint.trace.legacyCalls, 0);
  assert.equal(checkpoint.outcome.result.model, "jev-1.14.0");
  const body = JSON.parse(calls[0].body);
  assert.throws(() => host.validateWireResponse({ model: "jev-1.14.0", usage: { input_tokens: 1 }, answers: { unknown: { type: "noul", noul: 0.9 } } }, body));
  assert.equal(host.buildSelectionBatch, buildSelectionBatch);
});
