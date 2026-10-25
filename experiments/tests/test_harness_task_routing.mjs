import test from 'node:test';
import assert from 'node:assert/strict';
import { createHash } from 'node:crypto';
import { mkdir, mkdtemp, readFile, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { captureTaskRouting, taskQuery } from '../scripts/capture_harness_tasks.mjs';
import { SNIPPET_POLICY } from '../scripts/select_harness_candidates.mjs';
import { createHostDecisionAdapter } from '../scripts/host_decision_adapter.mjs';
import { createControlledFetch } from '../scripts/controlled_model_fetch.mjs';
import { spawnSync } from 'node:child_process';

const root = fileURLToPath(new URL('../../', import.meta.url));
const hash = value => createHash('sha256').update(value).digest('hex');
const save = (name, value) => writeFile(name, JSON.stringify(value));
const taskPath = path.join(root, 'experiments/fixtures/harness_task_checks.json');
const taskBytes = await readFile(taskPath);
const tasks = JSON.parse(taskBytes).tasks.map(row => ({ id: row.id, publicTask: { id: row.id, ...row.public } }));
const empty = query => ({ query, status: 'completed', rawHitlists: ['skill-meta', 'skill-body', 'skill-references'].map(collection => ({ options: { collection, limit: 40, candidateLimit: 40, explain: true, rerank: false }, hits: [] })), additionalSources: { experiences: 'unavailable-not-imported', graph: 'unavailable-not-imported' }, relationEvidence: [] });

async function setup(t) {
  const base = path.join(root, 'experiments/datasets/task-routing-tests'); await mkdir(base, { recursive: true });
  const runDir = await mkdtemp(path.join(base, 'run-')); t.after(() => rm(runDir, { recursive: true, force: true }));
  const fixtureRelative = 'experiments/fixtures/harness_task_checks.json';
  const graderRelative = 'experiments/scripts/harness_task_checks.py';
  const freeze = { schema_version: 1, status: 'frozen', cases_sha256: 'a'.repeat(64), labels_sha256: 'b'.repeat(64), contract_sha256: 'c'.repeat(64), protocol_sha256: 'd'.repeat(64), artifacts: { [fixtureRelative]: hash(taskBytes), [graderRelative]: hash(await readFile(path.join(root, graderRelative))) } };
  const challenger = { schema_version: 1, status: 'frozen', m1CasesSha256: freeze.cases_sha256, m1LabelsSha256: freeze.labels_sha256, contractSha256: freeze.contract_sha256, protocolSha256: freeze.protocol_sha256, baseline: { fusion: 'current-max', poolLimit: 6, snippet: 'none' }, challenger: { fusion: 'current-max', poolLimit: 6, snippet: 'none' } };
  await save(path.join(runDir, 'm1-freeze.json'), freeze); await save(path.join(runDir, 'challenger-config.json'), challenger);
  const policy = { qmd: { timeoutMs: 15000 }, routing: { skills: { maxInjectedSkills: 6, relevanceThreshold: 0.4, search: { minCandidateScore: 0.3 } } } };
  await save(path.join(runDir, 'm0-query-probes.json'), { raw_hitlists: { policies: policy } });
  await save(path.join(runDir, 'm0-host-probes.json'), { status: 'complete', provenance: { mode: 'host-public-facade', sources: [] } });
  const settings = { stage: 'raw', runDir, tasks, expectedTaskChecksSha256: hash(taskBytes), m1FreezeSha256: hash(await readFile(path.join(runDir, 'm1-freeze.json'))), challengerConfigSha256: hash(await readFile(path.join(runDir, 'challenger-config.json'))), policy, timeoutMs: 8000, models: { embedding: 'text-embedding-3-small', dimension: 1536, expansion: 'gemini-3.5-flash-lite', expansionResolved: 'gemini-3.5-flash-lite', jev: 'jev-latest', jevResolved: 'jev-1.14.0' }, endpoints: Object.fromEntries(['embedding', 'expansion', 'jev'].map(key => [key, { url: `https://fake.invalid/${key}`, apiKey: 'SECRET_SENTINEL' }])) };
  let queries = 0, selectors = 0, ranks = 0;
  const deps = { prepareRuntime: async () => ({ pins: { fixed: true }, rules: [], resolvedConfig: {}, decodeIdentity() {}, docsRoot: '/public/docs', hostSourcePins: [] }),
    createTransport: options => { assert.equal(options.probe, false); return Object.assign(async () => { throw Error('No transport admitted in fake'); }, { stats: { physicalAttempts: 0, cacheHits: 0, observations: [] } }); },
    createRetrieval: async () => ({ retrieve: async ({ query }) => { queries++; return empty(query); }, close: async () => {} }),
    createReplay: async () => ({ rankFrozenCandidates: async () => { ranks++; return { candidateSkills: [{ name: 'fixture', description: 'Public synthetic candidate' }], candidateSources: { fixture: ['direct-retrieval'] }, relationEvidence: [], metadata: { injectionCap: 6 }, additionalSources: { experiences: 'unavailable-not-imported', graph: 'unavailable-not-imported' } }; }, close: async () => {} }),
    createHost: async () => ({ provenance: { sources: [] }, validateWireResponse() {}, buildSelectionBatch: params => ({ state: { latest_message: params.latest }, questions: params.candidateSkills.length ? { q: {} } : {} }), evaluateSelection: async (params, options) => { selectors++; assert.equal(options.timeoutMs, 8000); return { selection: { skills: ['fixture'], experiences: [] }, outcome: { status: 'ok' }, trace: { legacyCalls: 0 } }; }, close: async () => {} }) };
  return { settings, deps, counts: () => ({ queries, selectors, ranks }) };
}

test('12 shared queries, two frozen arms and exact completed reuse; no secrets/oracles in artifacts', async t => {
  const f = await setup(t);
  for (const stage of ['raw', 'prepare', 'select']) { const result = await captureTaskRouting({ ...f.settings, stage }, f.deps); assert.equal(result.status, 'complete'); }
  assert.deepEqual(f.counts(), { queries: 12, selectors: 24, ranks: 24 });
  for (const stage of ['raw', 'prepare', 'select']) assert.equal((await captureTaskRouting({ ...f.settings, stage }, f.deps)).status, 'cached-complete');
  assert.deepEqual(f.counts(), { queries: 12, selectors: 24, ranks: 24 });
  const checkpoint = await readFile(path.join(f.settings.runDir, 'task-routing/raw/t01.json'), 'utf8');
  assert.equal(checkpoint.includes('SECRET_SENTINEL'), false); assert.equal(checkpoint.includes('grader'), false);
  assert.deepEqual(JSON.parse(checkpoint).value.input.publicTask, tasks[0].publicTask);
  assert.equal(taskQuery(tasks[0].publicTask).includes('t01'), false);
  assert.equal(taskQuery(tasks[0].publicTask).includes('"examples"'), false);
  assert.equal(taskQuery(tasks[0].publicTask), taskQuery({ ...tasks[0].publicTask, artifact_contract: Object.fromEntries(Object.entries(tasks[0].publicTask.artifact_contract).reverse()) }));
});

test('task count, hidden nested fields, public changes, freeze and challenger mismatches stop before calls', async t => {
  const f = await setup(t);
  await assert.rejects(captureTaskRouting({ ...f.settings, tasks: tasks.slice(1) }, f.deps));
  const bad = structuredClone(f.settings); bad.tasks[0].publicTask.input_data.labels = ['hidden'];
  await assert.rejects(captureTaskRouting(bad, f.deps));
  const changed = structuredClone(f.settings); changed.tasks[0].publicTask.request += ' changed';
  await assert.rejects(captureTaskRouting(changed, f.deps));
  await assert.rejects(captureTaskRouting({ ...f.settings, challengerConfigSha256: '0'.repeat(64) }, f.deps));
  await assert.rejects(captureTaskRouting({ ...f.settings, m1FreezeSha256: '0'.repeat(64) }, f.deps));
  assert.equal(f.counts().queries, 0);
});

test('unavailable raw and pending fences never silently rerun or turn into empty success', async t => {
  const f = await setup(t); let calls = 0;
  f.deps.createRetrieval = async () => ({ retrieve: async () => { calls++; return { status: 'unavailable' }; }, close: async () => {} });
  await assert.rejects(captureTaskRouting(f.settings, f.deps));
  await assert.rejects(captureTaskRouting(f.settings, f.deps)); assert.equal(calls, 1);
});

test('tampered raw hash and incomplete prepare cannot feed selector', async t => {
  const f = await setup(t); await captureTaskRouting(f.settings, f.deps);
  await writeFile(path.join(f.settings.runDir, 'task-routing/raw/t01.json'), '{}');
  await assert.rejects(captureTaskRouting({ ...f.settings, stage: 'prepare' }, f.deps));
  assert.equal(f.counts().ranks, 0); assert.equal(f.counts().selectors, 0);
});

async function matched(f) {
  const filename = path.join(f.settings.runDir, 'challenger-config.json'); const config = JSON.parse(await readFile(filename));
  config.challenger = { fusion: 'current-max', poolLimit: 6, snippet: 'matched-reference', snippetPolicy: SNIPPET_POLICY };
  await save(filename, config); f.settings.challengerConfigSha256 = hash(await readFile(filename));
  f.deps.prepareRuntime = async () => ({ pins: { fixed: true }, rules: [], resolvedConfig: {}, docsRoot: '/public/docs', decodeIdentity: () => ({ skillName: 'fixture', relativePath: 'fixture/SKILL.md' }) });
  f.deps.createRetrieval = async () => ({ retrieve: async ({ query }) => { const value = empty(query); value.rawHitlists[1].hits.push({ filepath: 'qmd://skill-body/fixture/SKILL.md', score: 0.8, bestChunk: 'Matched public evidence. 😀'.repeat(30), body: 'NEVER_USE_FULL_BODY' }); return value; }, close: async () => {} });
}

test('matched arm uses exact strongest bestChunk helper and policy; arm tampering prevents cache reuse', async t => {
  const f = await setup(t); await matched(f);
  for (const stage of ['raw', 'prepare', 'select']) await captureTaskRouting({ ...f.settings, stage }, f.deps);
  const filename = path.join(f.settings.runDir, 'task-routing/select/challenger/t01.json'); const value = JSON.parse(await readFile(filename));
  assert.deepEqual(value.value.snippetProvenance.policy, SNIPPET_POLICY);
  assert.ok(value.value.snippetProvenance.utf8Bytes <= 2048);
  assert.ok(Buffer.byteLength(value.value.snippetProvenance.state.fixture) <= 320);
  assert.ok(value.value.snippetProvenance.state.fixture.startsWith('Matched public evidence.'));
  assert.equal(JSON.stringify(value).includes('NEVER_USE_FULL_BODY'), false);
  await writeFile(filename, '{}');
  await assert.rejects(captureTaskRouting({ ...f.settings, stage: 'select' }, f.deps), /Arm checkpoint/);
});

test('legal empty pools are explicit completed skips and never call host', async t => {
  const f = await setup(t); const original = f.deps.createReplay;
  f.deps.createReplay = async () => { const replay = await original(); const rank = replay.rankFrozenCandidates; replay.rankFrozenCandidates = async () => ({ ...await rank(), candidateSkills: [], candidateSources: {} }); return replay; };
  for (const stage of ['raw', 'prepare', 'select']) await captureTaskRouting({ ...f.settings, stage }, f.deps);
  assert.equal(f.counts().selectors, 0);
  const value = JSON.parse(await readFile(path.join(f.settings.runDir, 'task-routing/select/t01.json'))).value;
  assert.equal(value.arms.baseline.status, 'skipped-empty-pool'); assert.equal(value.arms.baseline.candidate_count, 0);
});

test('selector error is a preserved failure; a second distinct Jev intent is blocked before transport', async t => {
  const f = await setup(t);
  for (const stage of ['raw', 'prepare']) await captureTaskRouting({ ...f.settings, stage }, f.deps);
  f.deps.createHost = async () => ({ provenance: { sources: [] }, buildSelectionBatch: () => ({ questions: { q: {} } }), evaluateSelection: async () => ({ outcome: { status: 'unavailable' } }), close: async () => {} });
  await assert.rejects(captureTaskRouting({ ...f.settings, stage: 'select' }, f.deps));
  await assert.rejects(captureTaskRouting({ ...f.settings, stage: 'select' }, f.deps), /preserved/);
  const g = await setup(t); let physical = 0;
  g.deps.createTransport = () => Object.assign(async () => { physical++; return Response.json({}); }, { stats: { physicalAttempts: 0, cacheHits: 0, observations: [] } });
  g.deps.createRetrieval = async ({ fetchImpl }) => ({ retrieve: async ({ query }) => {
    for (const intent of [1, 2]) { try { await fetchImpl('https://qmd-reuse.invalid/v1/systemone', { method: 'POST', body: JSON.stringify({ model: 'jev-latest', intent }) }); } catch {} }
    return empty(query);
  }, close: async () => {} });
  await assert.rejects(captureTaskRouting(g.settings, g.deps)); assert.equal(physical, 1);
});

test('concurrent identical intent callbacks share one controlled attempt per public task', async t => {
  const f = await setup(t); let physical = 0;
  f.deps.createTransport = () => Object.assign(async () => { physical++; return Response.json({ public: 'fixture' }); }, { stats: { physicalAttempts: 0, cacheHits: 0, observations: [] } });
  f.deps.createRetrieval = async ({ fetchImpl }) => ({ retrieve: async ({ query }) => {
    const request = () => fetchImpl('https://qmd-reuse.invalid/v1/systemone', { method: 'POST', body: JSON.stringify({ model: 'jev-latest', query }) });
    const responses = await Promise.all([request(), request()]);
    assert.deepEqual(await responses[0].json(), await responses[1].json()); return empty(query);
  }, close: async () => {} });
  await captureTaskRouting(f.settings, f.deps); assert.equal(physical, 12);
});

test('adapter initialization has no transport authority before a case checkpoint exists', async t => {
  const f = await setup(t); let physical = 0;
  f.deps.createTransport = () => Object.assign(async () => { physical++; return Response.json({}); }, { stats: { physicalAttempts: 0, cacheHits: 0, observations: [] } });
  f.deps.createRetrieval = async ({ fetchImpl }) => { await fetchImpl('https://qmd-reuse.invalid/v1/systemone', { method: 'POST', body: '{}' }); throw Error('unreachable'); };
  await assert.rejects(captureTaskRouting(f.settings, f.deps)); assert.equal(physical, 0);
});

test('actual installed host plus controlled fake fetch bills only global ledger and validates cache identity', async t => {
  const f = await setup(t); await matched(f);
  const hostM0 = JSON.parse(await readFile(path.join(root, 'experiments/datasets/harness-quality-20261025/m0-host-probes.json')));
  await save(path.join(f.settings.runDir, 'm0-host-probes.json'), { status: 'complete', provenance: { mode: 'host-public-facade', sources: hostM0.provenance.sources } });
  const original = f.deps.createReplay;
  f.deps.createReplay = async () => { const replay = await original(); const rank = replay.rankFrozenCandidates; replay.rankFrozenCandidates = async options => { const value = await rank(options); return options.observation.query === taskQuery(tasks[0].publicTask) ? value : { ...value, candidateSkills: [], candidateSources: {} }; }; return replay; };
  for (const stage of ['raw', 'prepare']) await captureTaskRouting({ ...f.settings, stage }, f.deps);
  const limits = { request_cap: 2, providers: { jev: { requests: 2, tokens: 131072, usd_per_million: '0.042' } } };
  await save(path.join(f.settings.runDir, 'budget-limits.json'), limits);
  let nativeCalls = 0, actual;
  f.deps.createHost = async options => { actual = await createHostDecisionAdapter({ ...options, offline: true }); return actual; };
  f.deps.createTransport = options => { assert.equal(options.probe, false); return createControlledFetch(options); };
  f.deps.nativeFetch = async (_url, init) => {
    nativeCalls++; assert.equal(new Headers(init.headers).get('authorization'), 'Bearer SECRET_SENTINEL'); const body = JSON.parse(init.body);
    assert.equal(body.model, 'jev-latest');
    return Response.json({ model: 'jev-1.14.0', answers: Object.fromEntries(Object.keys(body.questions).map(id => [id, { type: 'noul', noul: 0.9 }])), usage: { input_tokens: 19, output_tokens: 2 } });
  };
  const result = await captureTaskRouting({ ...f.settings, stage: 'select' }, f.deps);
  assert.equal(result.status, 'complete'); assert.equal(nativeCalls, 2); assert.equal(result.currentInvocationTransport.physicalAttempts, 2);
  assert.ok(result.currentInvocationTransport.observations.every(row => row.billedTokens === 19 && row.originalServiceMs >= 0));
  const checkpoint = JSON.parse(await readFile(path.join(f.settings.runDir, 'task-routing/select/t01.json'))).value;
  assert.deepEqual(checkpoint.arms.baseline.selection.skills, ['fixture']); assert.equal(checkpoint.arms.challenger.trace.legacyCalls, 0);
  assert.equal(checkpoint.arms.baseline.outcome.result.model, 'jev-1.14.0');
  const summary = spawnSync(path.join(root, 'experiments/.venv/bin/python'), [path.join(root, 'experiments/scripts/model_budget.py'), '--ledger', path.join(f.settings.runDir, 'model-budget.sqlite'), '--limits', path.join(f.settings.runDir, 'budget-limits.json'), 'summary'], { encoding: 'utf8' });
  assert.equal(summary.status, 0); assert.equal(JSON.parse(summary.stdout).jev.attempts, 2); assert.equal(JSON.parse(summary.stdout).jev.observed_billed_tokens, 38);
  await assert.rejects(readFile(path.join(f.settings.runDir, 'probe-budget.sqlite')), /ENOENT/);
  assert.deepEqual(actual.provenance.network, { socketAttempts: 0, dnsAttempts: 0 });
  t.after(() => rm(path.dirname(actual.provenance.isolation.configPath), { recursive: true, force: true }));
});
