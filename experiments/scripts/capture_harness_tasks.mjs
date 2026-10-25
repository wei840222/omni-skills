/** M4 routing capture only. Invoke raw, prepare, select in THREE fresh processes.
 * Settings/keys arrive on stdin; artifacts contain public inputs and hashes only.
 * Fusion's irreversible offline guards must never share a live-transport process.
 */
import { createHash, randomUUID } from 'node:crypto';
import { spawnSync } from 'node:child_process';
import { mkdir, readFile, readdir, realpath, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { preparePilotRuntime, stableHash } from './capture_harness_pilot.mjs';
import { createHarnessRetrievalAdapter } from './harness_retrieval_adapter.mjs';
import { createFrozenFusionReplay } from './harness_fusion.mjs';
import { createHostDecisionAdapter } from './host_decision_adapter.mjs';
import { createControlledFetch } from './controlled_model_fetch.mjs';
import { prepareSelectorRuntime, selectionParams, deriveMatchedSnippets, buildReferenceSnippets, SNIPPET_POLICY } from './select_harness_candidates.mjs';
import { readJsonStdin } from './json_stdin.mjs';

const root = fileURLToPath(new URL('../../', import.meta.url));
const canonicalRun = path.join(root, 'experiments/datasets/harness-quality-20261025');
const taskRelative = 'experiments/fixtures/harness_task_checks.json';
const graderRelative = 'experiments/scripts/harness_task_checks.py';
const native = globalThis.fetch; // Capture before any model-bearing dynamic import.
const sha = value => createHash('sha256').update(value).digest('hex');
const read = async name => JSON.parse(await readFile(name, 'utf8'));
const optional = async name => { try { return await read(name); } catch (e) { if (e.code !== 'ENOENT') throw e; } };
const writeNew = (name, value) => writeFile(name, JSON.stringify(value, null, 2) + '\n', { flag: 'wx' });
const inside = (base, target) => { const relative = path.relative(base, target); return relative && !relative.startsWith('..') && !path.isAbsolute(relative); };
const hex = value => typeof value === 'string' && /^[a-f0-9]{64}$/.test(value);
const zero = () => ({ physicalAttempts: 0, cacheHits: 0, observations: [] });
let processOwner;

export function taskQuery(publicTask) {
  const ordered = value => Array.isArray(value) ? value.map(ordered) : value && typeof value === 'object' ? Object.fromEntries(Object.keys(value).sort().map(key => [key, ordered(value[key])])) : value;
  return JSON.stringify({ request: publicTask.request, artifact_contract: ordered(publicTask.artifact_contract) });
}

function noHidden(value) {
  if (!value || typeof value !== 'object') return;
  for (const [key, item] of Object.entries(value)) {
    if (/^(expected|labels?|grader|oracle|source_refs|acceptable_sets|variant|ground_truth_skill)$/i.test(key)) throw Error('Nonpublic routing field');
    noHidden(item);
  }
}

function publicTasks() {
  // The trusted Python projection returns only public_task_input; no grader or
  // source-owner contents cross this process boundary into retrieval/selection.
  const result = spawnSync(path.join(root, 'experiments/.venv/bin/python'), ['-I', '-B', '-c',
    "import importlib.util,json,sys; s=importlib.util.spec_from_file_location('checks',sys.argv[1]); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); print(json.dumps([m.public_task_input('t%02d'%i) for i in range(1,13)],ensure_ascii=False))", path.join(root, graderRelative)],
  { cwd: root, encoding: 'utf8', timeout: 5000, maxBuffer: 256 * 1024, env: { PATH: '/usr/bin:/bin', PYTHONDONTWRITEBYTECODE: '1' } });
  if (result.status !== 0) throw Error('Public task projection failed');
  return JSON.parse(result.stdout);
}

export async function validateTaskRoutingSettings(settings) {
  if (!['raw', 'prepare', 'select'].includes(settings.stage)) throw Error('Explicit raw/prepare/select stage required');
  const runDir = path.resolve(settings.runDir ?? '');
  if (!inside(path.join(root, 'experiments/datasets'), runDir) || await realpath(runDir) !== runDir) throw Error('Unsafe routing run directory');
  const freezeBytes = await readFile(path.join(runDir, 'm1-freeze.json')); const freeze = JSON.parse(freezeBytes);
  if (sha(freezeBytes) !== settings.m1FreezeSha256 || freeze.schema_version !== 1 || freeze.status !== 'frozen') throw Error('M1 freeze mismatch');
  for (const key of ['cases_sha256', 'labels_sha256', 'contract_sha256', 'protocol_sha256']) if (!hex(freeze[key])) throw Error('M1 provenance missing');
  for (const relative of [taskRelative, graderRelative]) if (sha(await readFile(path.join(root, relative))) !== freeze.artifacts?.[relative]) throw Error('Frozen task source mismatch');
  if (freeze.artifacts[taskRelative] !== settings.expectedTaskChecksSha256) throw Error('Task fixture SHA mismatch');
  const projected = publicTasks();
  if (!Array.isArray(settings.tasks) || settings.tasks.length !== 12) throw Error('Exactly12 tasks required');
  const tasks = settings.tasks.map((row, index) => {
    noHidden(row);
    if (Object.keys(row).sort().join(',') !== 'id,publicTask' || row.id !== projected[index].id || stableHash(row.publicTask) !== stableHash(projected[index])) throw Error('Frozen public task/order mismatch');
    return structuredClone(row);
  });
  const challengerBytes = await readFile(path.join(runDir, 'challenger-config.json')); const challenger = JSON.parse(challengerBytes);
  if (sha(challengerBytes) !== settings.challengerConfigSha256 || challenger.schema_version !== 1 || challenger.status !== 'frozen' || challenger.m1CasesSha256 !== freeze.cases_sha256 || challenger.m1LabelsSha256 !== freeze.labels_sha256 || challenger.contractSha256 !== freeze.contract_sha256 || challenger.protocolSha256 !== freeze.protocol_sha256) throw Error('Challenger freeze mismatch');
  if (stableHash(challenger.baseline) !== stableHash({ fusion: 'current-max', poolLimit: 6, snippet: 'none' })) throw Error('Baseline config changed');
  const arms = Object.fromEntries(['baseline', 'challenger'].map(arm => {
    const config = challenger[arm];
    if (!config || !['current-max', 'skill-identity-sum'].includes(config.fusion) || ![6, 10, 20].includes(config.poolLimit) || !['none', 'matched-reference'].includes(config.snippet) || Object.keys(config).some(key => !['fusion', 'poolLimit', 'snippet', 'snippetPolicy'].includes(key)) || (config.snippet === 'matched-reference' && stableHash(config.snippetPolicy) !== stableHash(SNIPPET_POLICY))) throw Error('Unsupported frozen arm');
    return [arm, structuredClone(config)];
  }));
  const m0Bytes = await readFile(path.join(runDir, 'm0-query-probes.json')); const m0 = JSON.parse(m0Bytes).raw_hitlists;
  const hostBytes = await readFile(path.join(runDir, 'm0-host-probes.json')); const host = JSON.parse(hostBytes);
  const policy = m0?.policies; const skills = policy?.routing?.skills;
  if (stableHash(settings.policy) !== stableHash(policy) || skills?.maxInjectedSkills !== 6 || skills.relevanceThreshold !== 0.4 || skills.search?.minCandidateScore !== 0.3 || settings.timeoutMs !== 8000) throw Error('Frozen M0 policy/timeout mismatch');
  if (host.status !== 'complete' || host.provenance?.mode !== 'host-public-facade' || !Array.isArray(host.provenance.sources)) throw Error('M0 host provenance missing');
  const models = { embedding: 'text-embedding-3-small', dimension: 1536, expansion: 'gemini-3.5-flash-lite', expansionResolved: 'gemini-3.5-flash-lite', jev: 'jev-latest', jevResolved: 'jev-1.14.0' };
  if (stableHash(settings.models) !== stableHash(models)) throw Error('Frozen model identity mismatch');
  const endpoints = Object.fromEntries(['embedding', 'expansion', 'jev'].map(key => {
    const endpoint = settings.endpoints?.[key]; const url = new URL(endpoint?.url);
    if (url.protocol !== 'https:' || url.username || url.password || url.hash || url.search || (endpoint.apiKey !== undefined && typeof endpoint.apiKey !== 'string')) throw Error('Invalid explicit endpoint');
    return [key, url.href];
  }));
  const helpers = await Promise.all(['capture_harness_tasks.mjs', 'capture_harness_pilot.mjs', 'harness_fusion.mjs', 'select_harness_candidates.mjs', 'harness_retrieval_adapter.mjs', 'host_decision_adapter.mjs', 'controlled_model_fetch.mjs', 'json_stdin.mjs'].map(async name => ({ path: name, sha256: sha(await readFile(new URL(name, import.meta.url))) })));
  return { runDir, tasks, arms, hostSourcePins: host.provenance.sources, binding: { schema_version: 1, taskChecksSha256: settings.expectedTaskChecksSha256, publicTasksSha256: stableHash(tasks), m1FreezeSha256: sha(freezeBytes), challengerConfigSha256: sha(challengerBytes), m1CasesSha256: freeze.cases_sha256, m1LabelsSha256: freeze.labels_sha256, contractSha256: freeze.contract_sha256, protocolSha256: freeze.protocol_sha256, m0QuerySha256: sha(m0Bytes), m0HostSha256: sha(hostBytes), policySha256: stableHash(policy), models, arms, endpointSha256: stableHash(endpoints), helpers, admission: { maximumDistinctIntentJevBodies: 12, maximumDistinctSelectorJevBodies: 24 }, queryPolicy: 'public request + complete artifact_contract only; no id or example input_data; complete publicTask retained separately', additionalSources: { experiences: 'unavailable-not-imported', graph: 'unavailable-not-imported' } } };
}

async function prepareRuntime(settings, input) {
  if (input.runDir !== canonicalRun) throw Error('Live runtime requires the canonical run');
  const pilot = await preparePilotRuntime({ ...settings, policy: { qmdTimeoutMs: settings.policy.qmd.timeoutMs, collectionWeights: settings.policy.skills.search.collectionWeights, routing: settings.policy.routing } });
  const selector = await prepareSelectorRuntime({ ...settings, hostSourcePins: input.hostSourcePins });
  return { ...pilot, ...selector, pins: { retrieval: pilot.pins, host: selector.pins }, rules: pilot.rules, resolvedConfig: pilot.resolvedConfig };
}

/** Read-only preflight; installed imports have no transport authority. */
export async function verifyTaskRoutingSources(settings) {
  const input = await validateTaskRoutingSettings(settings);
  const runtime = await prepareRuntime(settings, input);
  return { status: 'verified', binding: input.binding, sourcePins: runtime.pins };
}

function observation(value, query) {
  if (value?.status !== 'completed' || value.query !== query || !Array.isArray(value.rawHitlists) || value.rawHitlists.length !== 3 || new Set(value.rawHitlists.map(row => row.options?.collection)).size !== 3 || value.rawHitlists.some(row => !['skill-meta', 'skill-body', 'skill-references'].includes(row.options?.collection) || row.options.limit !== 40 || row.options.candidateLimit !== 40 || row.options.explain !== true || row.options.rerank !== false || !Array.isArray(row.hits) || row.hits.length > 40 || row.stages?.some(stage => stage.stage === 'onExpansionError')) || value.additionalSources?.experiences !== 'unavailable-not-imported' || value.additionalSources?.graph !== 'unavailable-not-imported' || (value.relationEvidence?.length ?? 0)) throw Error('Raw retrieval unavailable or invalid');
  return value;
}

async function loadStage(directory, identity, expectedIds) {
  const manifest = await read(path.join(directory, 'manifest.json'));
  const { contentSha256, ...content } = manifest;
  if (contentSha256 !== stableHash(content) || manifest.identity !== stableHash(manifest.binding) || manifest.status !== 'complete' || (identity && manifest.identity !== identity) || stableHash(manifest.cases?.map(row => row.id)) !== stableHash(expectedIds)) throw Error('Stage manifest identity/hash mismatch');
  const start = await read(path.join(directory, 'run.pending.json'));
  if (start.identity !== manifest.identity || stableHash(start.binding) !== stableHash(manifest.binding)) throw Error('Original stage pending mismatch');
  const checkpoints = [];
  for (const row of manifest.cases) {
    const bytes = await readFile(path.join(directory, `${row.id}.json`)); const checkpoint = JSON.parse(bytes); const { contentSha256: hash, ...data } = checkpoint;
    const pending = await read(path.join(directory, `${row.id}.pending.json`));
    if (sha(bytes) !== row.sha256 || hash !== stableHash(data) || data.identity !== manifest.identity || pending.identity !== manifest.identity || data.inputSha256 !== pending.inputSha256) throw Error('Checkpoint hash/pending mismatch');
    if (data.value?.status !== 'complete' || data.value.input?.id !== row.id || stableHash(data.value.input) !== data.inputSha256) throw Error('Checkpoint public input/status mismatch');
    if (manifest.binding.stage === 'select') for (const arm of ['baseline', 'challenger']) {
      const armBytes = await readFile(path.join(directory, arm, `${row.id}.json`)); const armData = JSON.parse(armBytes); const { contentSha256: armSha, ...armContent } = armData;
      const reserved = await read(path.join(directory, arm, `${row.id}.pending.json`));
      if (sha(armBytes) !== data.value.arms?.[arm]?.checkpointSha256 || armSha !== stableHash(armContent) || armData.identity !== manifest.identity || reserved.identity !== manifest.identity || reserved.modelInputSha256 !== armData.value.modelInputSha256) throw Error('Arm checkpoint hash/pending mismatch');
    }
    checkpoints.push(data.value);
  }
  return { manifest, checkpoints, sha256: sha(await readFile(path.join(directory, 'manifest.json'))) };
}

/** API: captureTaskRouting(settings, optionalFakeDependencies) -> stage manifest.
 * Required settings: stage, runDir, tasks[{id,publicTask}], expectedTaskChecksSha256,
 * m1FreezeSha256, challengerConfigSha256, policy(full M0), timeoutMs:8000,
 * models(exact five identities + dimension:1536), endpoints{embedding,expansion,jev}:{url,apiKey?}.
 * Run raw -> prepare -> select in separate fresh Node invocations. No solver runs.
 */
export async function captureTaskRouting(settings, dependencies = {}) {
  const input = await validateTaskRoutingSettings(settings); const stage = settings.stage;
  if (!dependencies.prepareRuntime) {
    if (processOwner) throw Error('Use a fresh dedicated process for every routing stage');
    processOwner = stage;
  }
  const runtime = await (dependencies.prepareRuntime ?? prepareRuntime)(settings, input);
  const base = path.join(input.runDir, 'task-routing'); const ids = input.tasks.map(row => row.id);
  const prior = stage === 'raw' ? null : await loadStage(path.join(base, stage === 'prepare' ? 'raw' : 'prepare'), null, ids);
  if (prior && stableHash(prior.manifest.binding.common) !== stableHash(input.binding)) throw Error('Upstream stage binding differs');
  if (prior && prior.checkpoints.some((value, index) => stableHash(value.input) !== stableHash(input.tasks[index]))) throw Error('Upstream public task mismatch');
  const binding = { common: input.binding, sourcePins: runtime.pins, stage, upstreamSha256: prior?.sha256 ?? null };
  const identity = stableHash(binding); const directory = path.join(base, stage); await mkdir(directory, { recursive: true });
  if (await optional(path.join(directory, 'manifest.json'))) {
    const complete = await loadStage(directory, identity, ids);
    return { ...complete.manifest, status: 'cached-complete', currentInvocationTransport: zero() };
  }
  if ((await readdir(directory)).length) throw Error('Pending/failed routing stage preserved; no automatic rerun');
  await writeNew(path.join(directory, 'run.pending.json'), { identity, binding, pid: process.pid });
  let adapter, replay, transport, current, failed = false, activeUnit = false, admittedJevBody, admittedJevResponse;
  const createTransport = dependencies.createTransport ?? createControlledFetch;
  const runtimeRoot = path.join(canonicalRun, 'replay-runtime', `task-routing-${randomUUID()}`);
  const delta = before => ({ counts: { physicalAttempts: transport.stats.physicalAttempts - before.physicalAttempts, cacheHits: transport.stats.cacheHits - before.cacheHits }, observations: structuredClone(transport.stats.observations.slice(before.observations.length)) });
  const checkpoint = async (id, item, value) => writeNew(path.join(directory, `${id}.json`), (() => { const data = { identity, inputSha256: stableHash(item), value }; return { ...data, contentSha256: stableHash(data) }; })());
  const reserve = (id, item) => writeNew(path.join(directory, `${id}.pending.json`), { identity, inputSha256: stableHash(item), pid: process.pid });
  try {
    if (stage === 'prepare') replay = await (dependencies.createReplay ?? createFrozenFusionReplay)({ config: settings.policy, root, profileDir: path.join(input.runDir, 'qmd-public'), fixtureRoot: runtimeRoot });
    else {
      transport = createTransport({ runDir: input.runDir, endpoints: stage === 'raw' ? runtime.rules : [{ url: settings.endpoints.jev.url, provider: 'jev', model: 'jev-latest', resolvedModel: 'jev-1.14.0', validate: (payload, body) => adapter.validateWireResponse(payload, body) }], nativeFetch: dependencies.nativeFetch ?? native, python: path.join(root, 'experiments/.venv/bin/python'), probe: false });
      const mapped = async (url, init) => {
        const key = stage === 'select' ? (String(url) === 'https://selector-replay.invalid/v1/systemone' ? 'jev' : undefined) : ({ 'https://qmd-reuse.invalid/v1/embeddings': 'embedding', 'https://qmd-reuse.invalid/v1/chat/completions': 'expansion', 'https://qmd-reuse.invalid/v1/systemone': 'jev' })[String(url)];
        if (failed || !activeUnit || !key) { failed = true; throw Error('Unadmitted logical transport'); }
        if (key === 'jev') {
          const fingerprint = stableHash(JSON.parse(init.body));
          if (admittedJevBody && fingerprint !== admittedJevBody) { failed = true; throw Error('Only one distinct Jev request per task/arm'); }
          if (admittedJevResponse) return (await admittedJevResponse).clone();
          admittedJevBody = fingerprint;
        }
        const headers = new Headers(init.headers); headers.delete('authorization'); if (settings.endpoints[key].apiKey) headers.set('authorization', `Bearer ${settings.endpoints[key].apiKey}`);
        const request = async () => { try { const response = await transport(settings.endpoints[key].url, { ...init, headers }); if (!response.ok) throw Error('HTTP failure'); return response; } catch { failed = true; throw Error('Routing transport stopped'); } };
        if (key === 'jev') { admittedJevResponse = request(); return (await admittedJevResponse).clone(); }
        return request();
      };
      adapter = stage === 'raw' ? await (dependencies.createRetrieval ?? createHarnessRetrievalAdapter)({ root, profileDir: path.join(input.runDir, 'qmd-public'), dataRoot: runtimeRoot, resolvedConfig: runtime.resolvedConfig, fetchImpl: mapped, offline: false }) : await (dependencies.createHost ?? createHostDecisionAdapter)({ fixtureRoot: runtimeRoot, model: 'jev-latest', providerConfig: { apiBaseUrl: 'https://selector-replay.invalid/v1' }, fetchImpl: mapped, offline: false });
      if (stage === 'select' && adapter.provenance.sources.some(pin => !input.hostSourcePins.some(expected => expected.path === pin.path && expected.sha256 === pin.sha256))) throw Error('Host facade source differs from M0');
    }
    for (const [index, item] of input.tasks.entries()) {
      current = item.id; await reserve(current, item); const query = taskQuery(item.publicTask); const source = { id: current, latest: query };
      if (stage === 'raw') {
        admittedJevBody = undefined; admittedJevResponse = undefined;
        const before = structuredClone(transport.stats); activeUnit = true;
        const raw = observation(await adapter.retrieve({ query }), query); activeUnit = false;
        if (failed) throw Error('Caught internal retrieval transport failure');
        await checkpoint(current, item, { status: 'complete', input: item, rawHitlistObservation: raw, transport: delta(before) });
      } else if (stage === 'prepare') {
        const raw = observation(prior.checkpoints[index].rawHitlistObservation, query); const arms = {};
        for (const [arm, config] of Object.entries(input.arms)) {
          const ranked = await replay.rankFrozenCandidates({ observation: raw, fusion: config.fusion, poolLimit: config.poolLimit });
          if (ranked.metadata?.injectionCap !== 6 || ranked.additionalSources?.experiences !== 'unavailable-not-imported' || ranked.additionalSources?.graph !== 'unavailable-not-imported' || ranked.relationEvidence.length) throw Error('Frozen replay scope changed');
          const params = selectionParams(source, { candidateSkills: ranked.candidateSkills, candidateSources: ranked.candidateSources, candidateExperiences: [], relationEvidence: [] });
          const snippets = config.snippet === 'matched-reference' ? deriveMatchedSnippets({ candidateSkills: params.candidateSkills, rawHitlistObservation: raw, decodeIdentity: runtime.decodeIdentity, docsRoot: runtime.docsRoot }) : undefined;
          arms[arm] = { config, params, rankMetadata: ranked.metadata, ...(snippets ? { matchedSnippets: snippets } : {}) };
        }
        await checkpoint(current, item, { status: 'complete', input: item, rawHitlistObservation: raw, arms });
      } else {
        const prepared = prior.checkpoints[index]; const arms = {};
        for (const [arm, config] of Object.entries(input.arms)) {
          const armDir = path.join(directory, arm); await mkdir(armDir, { recursive: true });
          const data = prepared.arms[arm]; if (stableHash(data.config) !== stableHash(config)) throw Error('Prepared arm config differs');
          const params = selectionParams(source, data.params); const batch = adapter.buildSelectionBatch(params);
          const snippets = config.snippet === 'matched-reference' ? buildReferenceSnippets({ candidateSkills: params.candidateSkills, rawHitlistObservation: prepared.rawHitlistObservation, decodeIdentity: runtime.decodeIdentity, docsRoot: runtime.docsRoot, matchedSnippets: data.matchedSnippets }) : undefined;
          if (snippets) batch.state = { ...batch.state, reference_matched_snippets: snippets.state };
          const modelInputSha256 = stableHash(batch); await writeNew(path.join(armDir, `${current}.pending.json`), { identity, modelInputSha256 });
          admittedJevBody = undefined; admittedJevResponse = undefined;
          const before = structuredClone(transport.stats); const start = performance.now();
          activeUnit = true;
          const result = Object.keys(batch.questions).length ? await adapter.evaluateSelection(params, { batch, timeoutMs: 8000, routing: structuredClone(settings.policy.routing) }) : { skipped: 'empty-pool', trace: { hostCalls: 0, fetchCalls: 0, legacyCalls: 0 } };
          activeUnit = false;
          if (failed || (result.skipped ? (result.skipped !== 'empty-pool' || params.candidateSkills.length !== 0) : (!result.selection || result.outcome?.status !== 'ok')) || result.trace?.legacyCalls || result.trace?.hostCalls > 1 || result.trace?.fetchCalls > 1) throw Error('Selector unavailable or invalid');
          const value = { status: result.skipped ? 'skipped-empty-pool' : 'completed', candidate_count: params.candidateSkills.length, selection: result.selection ?? { skills: [], experiences: [] }, outcome: result.outcome ?? null, trace: result.trace ?? null, modelInputSha256, snippetProvenance: snippets ?? null, evaluationWallMs: performance.now() - start, transport: delta(before) };
          const armContent = { identity, value }; const filename = path.join(armDir, `${current}.json`); await writeNew(filename, { ...armContent, contentSha256: stableHash(armContent) });
          arms[arm] = { ...value, checkpointSha256: sha(await readFile(filename)) };
        }
        await checkpoint(current, item, { status: 'complete', input: item, arms });
      }
    }
    const cases = await Promise.all(ids.map(async id => ({ id, sha256: sha(await readFile(path.join(directory, `${id}.json`))) })));
    const content = { schema_version: 1, status: 'complete', identity, binding, cases, currentInvocationTransport: transport?.stats ?? zero(), scope: 'Twelve public task routing inputs, one shared raw retrieval and two frozen host arms; no agent solutions, grader outcomes, accuracy, production experience or graph claims.' };
    const manifest = { ...content, contentSha256: stableHash(content) }; await writeNew(path.join(directory, 'manifest.json'), manifest); return manifest;
  } catch {
    activeUnit = false;
    await writeNew(path.join(directory, 'failed-run.json'), { identity, status: 'failed', caseId: current ?? null, reason: 'routing-source-transport-schema-or-checkpoint-failure', transport: transport?.stats ?? null });
    throw Error('Task routing stopped; pending/failure preserved; no automatic retry');
  } finally { await adapter?.close(); await replay?.close(); }
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  readJsonStdin().then(captureTaskRouting).then(result => console.log(JSON.stringify({ status: result.status, stage: result.binding.stage, tasks: result.cases.length, artifactPath: path.join(canonicalRun, 'task-routing', result.binding.stage, 'manifest.json'), physicalAttempts: result.currentInvocationTransport.physicalAttempts, cacheHits: result.currentInvocationTransport.cacheHits }))).catch(() => { console.error('Task routing stopped; inspect task-routing checkpoints. Sensitive details omitted.'); process.exitCode = 1; });
}
