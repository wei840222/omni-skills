/** Installed skill-harness query retrieval over a frozen public QMD profile.
 * No native fetch is retained. The caller owns endpoint mapping, credentials,
 * external request admission and billing in its explicit transport callback.
 * Use a dedicated process; offline socket guards cannot be relaxed later.
 */
import { createHash } from "node:crypto";
import { link, lstat, mkdir, readFile, readdir, realpath, symlink, writeFile } from "node:fs/promises";
import { createRequire, syncBuiltinESMExports } from "node:module";
import net from "node:net";
import tls from "node:tls";
import dgram from "node:dgram";
import dns from "node:dns";
import os from "node:os";
import path from "node:path";
import { performance } from "node:perf_hooks";
import { fileURLToPath, pathToFileURL } from "node:url";

const workspace = fileURLToPath(new URL("../../", import.meta.url));
const canonicalRun = path.join(workspace, "experiments/datasets/harness-quality-20261025");
const replayRoot = path.join(canonicalRun, "replay-runtime");
const defaultHarness = path.join(os.homedir(), ".openclaw/extensions/skill-harness");
const logicalBase = "https://qmd-reuse.invalid/v1";
const embeddingModel = "text-embedding-3-small";
const dimension = 1536;
const digest = (value) => createHash("sha256").update(value).digest("hex");
const denyFetch = async () => { throw new Error("Retrieval fetch requires an admitted caller transport"); };
let network;

function inside(root, target) {
  const relative = path.relative(root, target);
  return relative !== "" && !relative.startsWith("..") && !path.isAbsolute(relative);
}

function denyNetwork(offline) {
  if (!offline && network?.installed) throw new Error("Offline socket guards are installed; use a fresh process for caller-controlled online transport");
  globalThis.fetch = denyFetch;
  if (!network) network = { socketAttempts: 0, dnsAttempts: 0 };
  if (offline && !network.installed) {
    const socket = () => { network.socketAttempts++; throw new Error("Offline retrieval forbids sockets"); };
    const lookup = () => { network.dnsAttempts++; throw new Error("Offline retrieval forbids DNS"); };
    net.Socket.prototype.connect = socket;
    net.connect = net.createConnection = tls.connect = dgram.createSocket = socket;
    for (const object of [dns, dns.promises]) {
      for (const key of Object.keys(object)) {
        if ((key.startsWith("resolve") || key === "lookup" || key === "reverse") && typeof object[key] === "function") object[key] = lookup;
      }
    }
    network.installed = true;
    syncBuiltinESMExports();
  }
  return network;
}

export async function loadInstalledRetrievalSources({ harnessRoot = defaultHarness, offline = true } = {}) {
  denyNetwork(offline);
  const require = createRequire(path.join(harnessRoot, "package.json"));
  const qmdRoot = await realpath(path.join(harnessRoot, "node_modules/@wei840222/qmd"));
  const qmdPackage = JSON.parse(await readFile(path.join(qmdRoot, "package.json"), "utf8"));
  const qmdDist = path.dirname(path.resolve(qmdRoot, qmdPackage.exports["."].import));
  const sourceRoot = path.join(harnessRoot, "dist/src");
  const files = {
    qmd: path.join(qmdDist, "index.js"), store: path.join(qmdDist, "store.js"), db: path.join(qmdDist, "db.js"),
    index: path.join(sourceRoot, "qmd/skill-index.js"), names: path.join(sourceRoot, "skills/name-index.js"),
    pool: path.join(sourceRoot, "skills/candidate-pool.js"), related: path.join(sourceRoot, "skills/related.js"), normalize: path.join(sourceRoot, "normalize.js"),
  };
  const loaded = Object.fromEntries(await Promise.all(Object.entries(files).map(async ([key, filename]) => [key, await import(pathToFileURL(filename).href)])));
  const matter = (await import(pathToFileURL(require.resolve("gray-matter")).href)).default;
  // Importing hooks/index.js also initializes the private default session
  // tracker. Load its self-contained exported function verbatim instead.
  const hookPath = path.join(sourceRoot, "hooks/index.js");
  const hookSource = await readFile(hookPath, "utf8");
  const contextExport = hookSource.match(/export function formatConversationExpansionContext\(params\) \{[\s\S]*?\n\}/)?.[0];
  if (!contextExport) throw new Error("Installed conversation expansion helper could not be isolated");
  const isolated = await import(`data:text/javascript;base64,${Buffer.from(contextExport).toString("base64")}`);
  const provenanceFiles = [...Object.values(files), path.join(sourceRoot, "qmd/rrf.js"), path.join(sourceRoot, "hooks/index.js"), path.join(qmdDist, "embedding/identity.js"), path.join(qmdDist, "embedding/remote-embedding.js"), path.join(qmdDist, "embedding/openai.js"), path.join(qmdDist, "remote-llm.js"), path.join(qmdDist, "remote-jev.js")];
  return { ...loaded.qmd, ...loaded.db, ...loaded.index, ...loaded.names, ...loaded.pool, ...loaded.related, ...loaded.normalize, hashContent: loaded.store.hashContent, canonicalEmbeddingBuildMaterial: loaded.store.canonicalEmbeddingBuildMaterial, matter,
    formatConversationExpansionContext: isolated.formatConversationExpansionContext,
    contextHelper: { source: hookPath, export: "formatConversationExpansionContext", fragmentSha256: digest(contextExport), mode: "source-isolated-verbatim-export-no-private-tracker-import" },
    sources: await Promise.all(provenanceFiles.map(async (filename) => ({ path: filename, sha256: digest(await readFile(filename)) }))),
  };
}

async function readPublicSkills(root, sources) {
  const skills = [];
  for (const name of (await readdir(path.join(root, "skills"))).sort()) {
    const location = path.join(root, "skills", name, "SKILL.md");
    let text;
    try { text = await readFile(location, "utf8"); } catch (error) { if (["ENOENT", "ENOTDIR"].includes(error.code)) continue; throw error; }
    const parsed = sources.matter(text);
    if (parsed.data.name !== name || typeof parsed.data.description !== "string") throw new Error("Invalid public skill metadata");
    skills.push({ name, description: parsed.data.description.trim(), location });
  }
  return skills;
}

async function validateProfile(profileDir, skills, sources) {
  const filename = path.join(profileDir, "skill-search.sqlite");
  const db = sources.openReadOnlyDatabase(filename);
  try {
    sources.loadSqliteVec(db);
    db.exec("PRAGMA query_only=ON");
    const state = db.prepare("SELECT status,model,dimension,fingerprint,canonical_material FROM embedding_index_state WHERE singleton=1").get();
    if (!state || state.status !== "ready" || state.model !== embeddingModel || state.dimension !== dimension || digest(state.canonical_material) !== state.fingerprint) throw new Error("Public profile embedding identity is not ready/compatible");
    const material = JSON.parse(state.canonical_material);
    const provider = JSON.parse(material.provider_identity);
    if (material.chunking.strategy !== "regex" || provider.provider !== "openai" || provider.model !== embeddingModel || provider.dimension !== dimension || provider.format !== "qmd-openai-embedding-v1" || provider.chunking.algorithm !== "qmd-utf8-window-v1") throw new Error("Public profile embedding format/chunk identity mismatch");
    const expected = new Set(skills.map((skill) => skill.name));
    const actual = new Set(db.prepare("SELECT DISTINCT substr(path,1,instr(path,'/')-1) AS segment FROM documents WHERE active=1").all().map((row) => decodeURIComponent(row.segment)));
    if (actual.size !== expected.size || [...actual].some((name) => !expected.has(name))) throw new Error("Public profile skill inventory mismatch");
    const metadataRows = db.prepare("SELECT COUNT(*) AS n FROM content_vectors WHERE model=? AND embed_fingerprint=?").get(embeddingModel, state.fingerprint).n;
    const vectorRows = db.prepare("SELECT COUNT(*) AS n FROM content_vectors cv JOIN vectors_vec vv ON vv.hash_seq=cv.hash || '_' || cv.seq WHERE cv.model=? AND cv.embed_fingerprint=?").get(embeddingModel, state.fingerprint).n;
    if (!vectorRows || vectorRows !== metadataRows) throw new Error("Public profile vector payload is incomplete");
    return { model: embeddingModel, dimension, vectorRows, embeddingFingerprint: state.fingerprint, databaseSha256: digest(await readFile(filename)) };
  } finally { db.close(); }
}

export async function prepareManagedRetrievalLayout({ root = workspace, profileDir = path.join(canonicalRun, "qmd-public"), dataRoot = replayRoot, fixture = false, expectedSkillCount = 963, sources, harnessRoot = defaultHarness, offline = true } = {}) {
  dataRoot = path.resolve(dataRoot);
  profileDir = path.resolve(profileDir);
  if (!(dataRoot === replayRoot || inside(replayRoot, dataRoot)) || !inside(workspace, profileDir)) throw new Error("Retrieval layout/profile must remain inside the workspace replay boundary");
  if (!fixture && expectedSkillCount !== 963) throw new Error("The public target must retain all 963 skills");
  if (!inside(workspace, await realpath(profileDir))) throw new Error("Public profile resolves outside the workspace");
  sources ??= await loadInstalledRetrievalSources({ harnessRoot, offline });
  const skills = await readPublicSkills(path.resolve(root), sources);
  if (skills.length !== expectedSkillCount) throw new Error(`Expected ${expectedSkillCount} public skills; observed ${skills.length}`);
  const identity = await validateProfile(profileDir, skills, sources);
  const fingerprint = digest(JSON.stringify({ allowedNames: skills.map((skill) => skill.name), databaseSha256: identity.databaseSha256, embeddingFingerprint: identity.embeddingFingerprint }));
  const managed = path.join(dataRoot, "qmd/skills");
  const indexRoot = path.join(managed, "indexes", fingerprint);
  const docsRoot = path.join(indexRoot, "docs");
  await mkdir(docsRoot, { recursive: true });
  for (const collection of ["meta", "body", "references"]) {
    const target = path.join(docsRoot, collection);
    const original = path.join(profileDir, "docs", collection);
    try { await symlink(original, target, "dir"); } catch (error) { if (error.code !== "EEXIST" || await realpath(target) !== await realpath(original)) throw error; }
  }
  const dbPath = path.join(indexRoot, "skill-search.sqlite");
  try { await link(path.join(profileDir, "skill-search.sqlite"), dbPath); } catch (error) { if (error.code !== "EEXIST" || digest(await readFile(dbPath)) !== identity.databaseSha256) throw error; }
  if (!(await lstat(indexRoot)).isDirectory() || !(await lstat(docsRoot)).isDirectory() || !(await lstat(dbPath)).isFile()) throw new Error("Managed read-only layout requires real directories and a regular database file");
  const mappingPath = path.join(managed, "agents/offline-eval.json");
  await mkdir(path.dirname(mappingPath), { recursive: true });
  const mapping = { schemaVersion: 1, fingerprint, allowedSkillNames: skills.map((skill) => skill.name) };
  const serialized = JSON.stringify(mapping, null, 2) + "\n";
  try { await writeFile(mappingPath, serialized, { flag: "wx" }); } catch (error) { if (error.code !== "EEXIST" || await readFile(mappingPath, "utf8") !== serialized) throw error; }
  return { dataRoot, profileDir, mappingPath, indexRoot, dbPath, fingerprint, publicSkillCount: skills.length, allowedNamesSha256: digest(JSON.stringify(mapping.allowedSkillNames)), ...identity, skills };
}

function effectiveConfig(input) {
  const qmd = input?.qmd;
  const policy = input?.routing?.skills;
  const weights = input?.skills?.search?.collectionWeights;
  if (qmd?.embedding?.model?.split("/").at(-1) !== embeddingModel || qmd.embedding.dimension !== dimension || !qmd.expansion?.model || !qmd.jev?.model || !Number.isFinite(qmd.timeoutMs) || qmd.timeoutMs <= 0) throw new Error("Explicit compatible QMD embedding/expansion/Jev models and timeout are required");
  if (!Number.isInteger(policy?.maxInjectedSkills) || policy.maxInjectedSkills < 0 || !Number.isFinite(policy.search?.minCandidateScore) || !Number.isFinite(policy.search?.timeoutMs) || policy.search.timeoutMs <= 0 || !Array.isArray(policy.nameMatch?.genericTokens) || !Number.isFinite(policy.nameMatch.minJaccardScore) || !Number.isInteger(policy.nameMatch.maxEditDistance)) throw new Error("Explicit resolved search and name-match policies are required");
  if (!["meta", "body", "references"].every((key) => Number.isFinite(weights?.[key]) && weights[key] > 0)) throw new Error("Explicit three-collection weights are required");
  const endpoint = (value, baseUrl = logicalBase) => ({ model: value.model, baseUrl, apiKey: "offline-controlled-transport-placeholder" });
  return { qmd: { timeoutMs: qmd.timeoutMs, embedding: { ...endpoint(qmd.embedding), dimension }, expansion: endpoint(qmd.expansion), jev: endpoint(qmd.jev, new URL(logicalBase).origin) }, skills: { search: { collectionWeights: { ...weights } } }, routing: { skills: structuredClone(policy) } };
}

export async function createHarnessRetrievalAdapter({ root = workspace, profileDir = path.join(canonicalRun, "qmd-public"), dataRoot = replayRoot, resolvedConfig, fetchImpl, fixture = false, expectedSkillCount = 963, offline = true, harnessRoot = defaultHarness } = {}) {
  if (typeof fetchImpl !== "function") throw new Error("An explicit caller-controlled transport callback is required");
  const config = effectiveConfig(resolvedConfig);
  const sources = await loadInstalledRetrievalSources({ harnessRoot, offline });
  const layout = await prepareManagedRetrievalLayout({ root, profileDir, dataRoot, fixture, expectedSkillCount, sources, offline });
  const { skills, ...profile } = layout;
  const observations = [];
  let active;
  let closed = false;
  let pending = Promise.resolve();
  const controlledFetch = async (url, init) => {
    if (!active) throw new Error("Query transport called outside an active retrieval");
    const endpoint = new URL(String(url));
    const body = JSON.parse(init.body);
      const kind = endpoint.pathname.endsWith("/embeddings") ? "query-embedding" : endpoint.pathname.endsWith("/chat/completions") ? "expansion" : endpoint.pathname.endsWith("/systemone") ? "query-intent" : undefined;
    if (endpoint.origin !== new URL(logicalBase).origin || init.method !== "POST" || !kind || (kind === "query-intent" && Object.keys(body.questions ?? {}).some((key) => !["strategy", "needs_hyde"].includes(key)))) throw new Error("Retrieval transport denied an unexpected endpoint or rerank request");
    const started = performance.now();
    const record = { kind, logical_url: String(url), request_sha256: digest(init.body), request_bytes: Buffer.byteLength(init.body), model: body.model, input_count: Array.isArray(body.input) ? body.input.length : undefined };
    active.requests.push(record);
    try { const response = await fetchImpl(url, init); record.status = response.status; return response; }
    finally { record.callback_ms = performance.now() - started; }
  };
  const factory = async (options) => {
    if (options.readOnly !== true || options.dbPath !== layout.dbPath) throw new Error("Installed index attempted an unexpected writable/store path");
    globalThis.fetch = controlledFetch;
    let store;
    try { store = await sources.createStore(options); } finally { globalThis.fetch = active ? controlledFetch : denyFetch; }
    const state = store.internal.db.prepare("SELECT fingerprint,status,model,dimension FROM embedding_index_state WHERE singleton=1").get();
    const configuredFingerprint = digest(sources.canonicalEmbeddingBuildMaterial(store.internal.embeddingProvider.canonicalIdentityMaterial(), "regex"));
    if (state?.status !== "ready" || state.fingerprint !== layout.embeddingFingerprint || configuredFingerprint !== state.fingerprint || state.model !== embeddingModel || state.dimension !== dimension) { await store.close(); throw new Error("Read-only query store/provider identity changed before search"); }
    return { ...store, search: async (options) => {
      if (!active || options.rerank !== false || options.includeHyde !== false) throw new Error("Installed retrieval query policy changed");
      const observed = { options: structuredClone(options), hits: [], stages: [] };
      const trace = active;
      trace.rawHitlists.push(observed);
      const started = performance.now();
      const hooks = Object.fromEntries(["onStrongSignal", "onExpansionDecision", "onExpansionError", "onExpandStart", "onExpand", "onEmbedStart", "onEmbedDone"].map((stage) => [stage, (...args) => observed.stages.push({ stage, at_ms: performance.now() - started, args })]));
      hooks.onRerankStart = () => { throw new Error("Unexpected rerank stage in installed retrieval"); };
      try { const hits = await store.search({ ...options, hooks }); observed.hits = structuredClone(hits); return hits; }
      finally { observed.wall_ms = performance.now() - started; }
    } };
  };
  const index = sources.createSkillQmdIndex({ dataRoot: layout.dataRoot, config: () => config, readOnly: true, createStore: factory });
  const normalizeCollection = (value) => ({ "skill-meta": "meta", "skill-body": "body", "skill-references": "references", meta: "meta", body: "body", references: "references" })[value?.trim().toLowerCase()];
  const matchNames = (query, enabled = config.routing.skills.maxInjectedSkills > 0) => enabled ? sources.matchAvailableSkillNamesWithTokens({ skills, input: query, options: config.routing.skills.nameMatch }) : { candidates: [], matchedTokens: [] };
  const buildExpansionContext = ({ query, conversation, nameMatch = matchNames(query) }) => {
    if (conversation !== undefined && (!Array.isArray(conversation) || conversation.some((turn) => !["user", "assistant"].includes(turn.role) || typeof turn.text !== "string"))) throw new Error("Conversation must contain explicit public user/assistant text turns");
    return sources.formatConversationExpansionContext({ conversation, candidateTokens: nameMatch.matchedTokens });
  };
  function candidatesFromHits({ query, skillHits, enabled = config.routing.skills.maxInjectedSkills > 0, controlledExperiences = [], controlledGraph = new Map(), nameMatch }) {
    const policy = config.routing.skills;
    const matched = nameMatch ?? matchNames(query, enabled);
    const nameCandidates = matched.candidates.map((candidate) => ({ ...candidate, collections: ["meta"], topCollection: "meta" }));
    const retrievalCandidates = enabled ? skillHits.flatMap((hit) => {
      if (hit.semanticScore === undefined || sources.roundToDecimals(hit.semanticScore, 2) < sources.roundToDecimals(policy.search.minCandidateScore, 2)) return [];
      const collections = [...new Set((hit.evidence ?? []).map((entry) => normalizeCollection(entry.collection)).filter(Boolean))];
      return [{ skillName: hit.name, score: hit.semanticScore, source: "direct-retrieval", collections: collections.length ? collections : undefined, topCollection: hit.evidence?.[0] ? normalizeCollection(hit.evidence[0].collection) : collections[0], evidence: hit.evidence }];
    }) : [];
    const union = sources.buildCandidateSkillsUnionPool({ visibleSkills: skills, nameCandidates, retrievalCandidates, maxInjectedSkills: policy.maxInjectedSkills });
    const related = sources.expandRelatedCandidates(union.candidateSkills, skills, controlledGraph);
    const superset = sources.buildSkillCandidateSuperset({ originals: union.candidateSkills, nameCandidates, retrievalCandidates, experiences: controlledExperiences, expanded: related.candidateSkills, expandedNames: related.added, visibleSkills: skills, enabled });
    return { nameCandidates, matchedTokens: matched.matchedTokens, retrievalCandidates, unionPool: union.pool, candidateSkills: superset.candidateSkills, candidateSources: superset.candidateSources,
      relationEvidence: sources.collectRelationEvidence(superset.candidateSkills, skills, controlledGraph),
      additionalSources: { experiences: controlledExperiences.length ? "controlled-fixture" : "unavailable-not-imported", graph: controlledGraph.size ? "controlled-fixture" : "unavailable-not-imported" } };
  }
  async function retrieveOne({ query, expansionContext, conversation, controlledExperiences = [], controlledGraph = new Map() }) {
    if (closed) throw new Error("Retrieval adapter is closed");
    if (typeof query !== "string" || (expansionContext !== undefined && typeof expansionContext !== "string")) throw new Error("Query/context must be explicit strings");
    const started = performance.now();
    const trace = { query, requests: [], rawHitlists: [], skillHits: [], latency_ms: {} };
    active = trace;
    // The installed TypeSafe SDK deliberately resolves ambient fetch at request
    // time; OpenAI/expansion providers capture it during store construction.
    // Both paths therefore stay within this same admitted query callback.
    globalThis.fetch = controlledFetch;
    try {
      const enabled = config.routing.skills.maxInjectedSkills > 0;
      if (!query.trim() || !enabled) {
        const result = { ...trace, status: !query.trim() ? "empty-query" : "disabled", ...candidatesFromHits({ query, skillHits: [], enabled: false }) };
        result.latency_ms.total = performance.now() - started;
        observations.push(result);
        return result;
      }
      const namesStarted = performance.now();
      const nameMatch = matchNames(query);
      trace.latency_ms.name_match = performance.now() - namesStarted;
      const context = expansionContext ?? buildExpansionContext({ query, conversation, nameMatch });
      if (context !== undefined) trace.expansionContext = context;
      const retrievalStarted = performance.now();
      let timer;
      const search = index.search({ agentId: "offline-eval", query, limit: config.routing.skills.maxInjectedSkills, includeEvidence: true, ...(context === undefined ? {} : { expansionContext: context }) });
      const outcome = await Promise.race([search.then((hits) => ({ hits })), new Promise((resolve) => { timer = setTimeout(() => resolve({ timeout: true }), config.routing.skills.search.timeoutMs); })]);
      clearTimeout(timer);
      trace.latency_ms.retrieval = performance.now() - retrievalStarted;
      if (outcome.timeout) { const drainStarted = performance.now(); await search; trace.latency_ms.drain = performance.now() - drainStarted; }
      trace.skillHits = outcome.hits ?? [];
      const gateStarted = performance.now();
      const candidates = candidatesFromHits({ query, skillHits: trace.skillHits, controlledExperiences, controlledGraph, nameMatch });
      trace.latency_ms.gate_union_related = performance.now() - gateStarted;
      trace.latency_ms.total = performance.now() - started;
      const result = { ...trace, status: outcome.timeout ? "timeout-drained" : outcome.hits === undefined ? "unavailable" : "completed", ...candidates };
      observations.push(result);
      return result;
    } finally { active = undefined; globalThis.fetch = denyFetch; }
  }
  const policies = { qmd: { timeoutMs: config.qmd.timeoutMs, embedding: { model: config.qmd.embedding.model, dimension, logicalBaseUrl: logicalBase }, expansion: { model: config.qmd.expansion.model, logicalBaseUrl: logicalBase }, jev: { model: config.qmd.jev.model, logicalBaseUrl: new URL(logicalBase).origin } }, skills: config.skills, routing: config.routing };
  const manifest = () => ({ schema_version: 1, scope: fixture ? "controlled-tiny-fixture" : "public-963-query-retrieval", profile, policies, provenance: { mode: "installed-createSkillQmdIndex-read-only", sources: sources.sources, contextHelper: sources.contextHelper, network: { socketAttempts: network.socketAttempts, dnsAttempts: network.dnsAttempts }, offline, gate_projection: "Exact installed hook roundToDecimals(score,2) comparison, followed by installed candidate-pool helpers; the full prompt hook is not executed.", model_transport: "Only supplied callback; logical offline URLs and request body remain unchanged; callback owns actual endpoint/auth/budget." }, observations: structuredClone(observations) });
  return {
    profile, candidatesFromHits, matchNames, buildExpansionContext,
    retrieve(input) { const work = pending.then(() => retrieveOne(input)); pending = work.catch(() => {}); return work; },
    rawHitlistManifest: manifest,
    async saveRawHitlistManifest(filename) { if (!inside(layout.dataRoot, path.resolve(filename))) throw new Error("Manifest must stay in the replay runtime"); await writeFile(filename, JSON.stringify(manifest(), null, 2) + "\n", { flag: "wx" }); },
    async close() { await pending; closed = true; await index.close(); globalThis.fetch = denyFetch; },
  };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  if (!process.argv.includes("--init-layout")) throw new Error("Only --init-layout CLI is provided; queries require an explicit caller transport/config API");
  const layout = await prepareManagedRetrievalLayout();
  console.log(JSON.stringify({ publicSkillCount: layout.publicSkillCount, fingerprint: layout.fingerprint, mappingPath: layout.mappingPath, vectorRows: layout.vectorRows, embeddingFingerprint: layout.embeddingFingerprint }, null, 2));
}
