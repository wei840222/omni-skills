/** Isolated public-skill QMD profile and exact managed-document vector preflight.
 * Run in a dedicated Node process. All remote paths deny by default; the only
 * admitted embedding responses come from an exact public-input memory map.
 */
import { createHash } from "node:crypto";
import { mkdir, readFile, readdir, realpath, writeFile } from "node:fs/promises";
import { createRequire, syncBuiltinESMExports } from "node:module";
import net from "node:net";
import tls from "node:tls";
import http from "node:http";
import https from "node:https";
import dgram from "node:dgram";
import dns from "node:dns";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const workspace = fileURLToPath(new URL("../../", import.meta.url));
const defaultHarness = path.join(os.homedir(), ".openclaw/extensions/skill-harness");
const offlineBase = "https://qmd-reuse.invalid/v1";
const model = "text-embedding-3-small";
const dimension = 1536;
const sha = (value) => createHash("sha256").update(value).digest("hex");
let guard;

export function installNetworkDeny() {
  if (!guard) {
    guard = { socketAttempts: 0, dnsAttempts: 0, deniedFetchAttempts: 0 };
    const denySocket = () => { guard.socketAttempts++; throw new Error("Offline QMD forbids sockets"); };
    const denyDns = () => { guard.dnsAttempts++; throw new Error("Offline QMD forbids DNS"); };
    net.Socket.prototype.connect = denySocket;
    net.connect = net.createConnection = tls.connect = dgram.createSocket = denySocket;
    http.request = http.get = https.request = https.get = denySocket;
    for (const key of Object.keys(dns)) {
      if ((key === "lookup" || key.startsWith("resolve") || key === "reverse") && typeof dns[key] === "function") dns[key] = denyDns;
    }
    for (const key of Object.keys(dns.promises)) {
      if ((key === "lookup" || key.startsWith("resolve") || key === "reverse") && typeof dns.promises[key] === "function") dns.promises[key] = denyDns;
    }
    for (const prototype of [dns.Resolver?.prototype, dns.promises.Resolver?.prototype]) {
      for (const key of Object.getOwnPropertyNames(prototype ?? {})) {
        if ((key.startsWith("resolve") || key === "reverse") && typeof prototype[key] === "function") prototype[key] = denyDns;
      }
    }
    syncBuiltinESMExports();
  }
  globalThis.fetch = async () => { guard.deniedFetchAttempts++; throw new Error("Offline QMD forbids ambient fetch"); };
  return guard;
}

export async function loadLibraries(harnessRoot = defaultHarness) {
  installNetworkDeny();
  const require = createRequire(path.join(harnessRoot, "package.json"));
  const qmdRoot = await realpath(path.join(harnessRoot, "node_modules/@wei840222/qmd"));
  const qmdPackage = JSON.parse(await readFile(path.join(qmdRoot, "package.json"), "utf8"));
  const qmdEntry = path.resolve(qmdRoot, qmdPackage.exports["."].import);
  const qmdDist = path.dirname(qmdEntry);
  const load = (filename) => import(pathToFileURL(filename).href);
  const [sdk, store, chunks, db, identity, openai, snapshot, matterModule] = await Promise.all([
    load(qmdEntry), load(path.join(qmdDist, "store.js")),
    load(path.join(qmdDist, "embedding/remote-chunking.js")), load(path.join(qmdDist, "db.js")),
    load(path.join(qmdDist, "embedding/identity.js")), load(path.join(qmdDist, "embedding/openai.js")),
    load(path.join(harnessRoot, "dist/src/qmd/skill-index.js")),
    load(require.resolve("gray-matter")),
  ]);
  const sourcePaths = [qmdEntry, path.join(qmdDist, "store.js"), path.join(qmdDist, "db.js"), path.join(qmdDist, "embedding/remote-chunking.js"), path.join(qmdDist, "embedding/identity.js"), path.join(qmdDist, "embedding/openai.js"), path.join(qmdDist, "embedding/config.js"), path.join(qmdDist, "embedding/remote-embedding.js"), path.join(qmdDist, "../package.json"), path.join(harnessRoot, "dist/src/qmd/skill-index.js"), path.join(harnessRoot, "dist/src/skills/paths.js")];
  return {
    ...sdk, hashContent: store.hashContent, extractTitle: store.extractTitle,
    canonicalEmbeddingBuildMaterial: store.canonicalEmbeddingBuildMaterial,
    ...chunks, ...db, endpointFreeIdentityMaterial: identity.endpointFreeIdentityMaterial,
    canonicalOpenAIEmbeddingIdentityMaterial: openai.canonicalOpenAIEmbeddingIdentityMaterial,
    writeSkillSnapshot: snapshot.writeSkillSnapshot, matter: matterModule.default,
    provenance: await Promise.all(sourcePaths.map(async (filename) => ({ path: filename, sha256: sha(await readFile(filename)) }))),
  };
}

export function validateVector(value, expectedDimension = dimension) {
  const vector = value instanceof Float32Array ? new Float32Array(value) : value instanceof Uint8Array
    ? new Float32Array(Uint8Array.from(value).buffer) : null;
  if (!vector || vector.length !== expectedDimension) throw new Error("Vector dimension mismatch");
  if ([...vector].some((number) => !Number.isFinite(number))) throw new Error("Vector contains nonfinite values");
  if (!vector.some((number) => number !== 0)) throw new Error("Vector is zero");
  return vector;
}

export function createCacheTransport({ cache = new Map(), dimension: expectedDimension = dimension } = {}) {
  const stats = { cacheResponses: 0, returnedVectors: 0, cacheMissInputs: 0, deniedRequests: 0 };
  const misses = new Map();
  const fetch = async (url, init) => {
    if (String(url) !== `${offlineBase}/embeddings` || init?.method !== "POST") {
      stats.deniedRequests++;
      throw new Error("Offline embedding transport denied an unexpected request");
    }
    const body = JSON.parse(init.body);
    if (body.model !== model || body.dimensions !== expectedDimension || !Array.isArray(body.input) || !body.input.length || body.input.some((input) => typeof input !== "string")) {
      stats.deniedRequests++;
      throw new Error("Offline embedding transport rejected request schema/model");
    }
    const missing = body.input.filter((input) => !cache.has(input));
    for (const input of missing) {
      stats.cacheMissInputs++;
      misses.set(sha(input), { input_sha256: sha(input), input_bytes: Buffer.byteLength(input) });
    }
    if (missing.length) throw new Error("Cache miss: remote embedding is forbidden");
    const vectors = body.input.map((input) => validateVector(cache.get(input), expectedDimension));
    stats.cacheResponses++;
    stats.returnedVectors += vectors.length;
    return Response.json({ object: "list", model, data: vectors.map((vector, index) => ({ object: "embedding", index, embedding: [...vector] })), usage: { prompt_tokens: 0, total_tokens: 0 } });
  };
  return { cache, fetch, stats, misses };
}

export function compatibleIdentity(state, libraries) {
  if (!state || state.status !== "ready" || state.provider_id !== "openai" || state.model !== model || state.dimension !== dimension || state.remote !== 1) return false;
  if (sha(state.canonical_material) !== state.fingerprint) return false;
  const expected = libraries.canonicalEmbeddingBuildMaterial(libraries.canonicalOpenAIEmbeddingIdentityMaterial(model, dimension), "regex");
  return libraries.endpointFreeIdentityMaterial(state.canonical_material) === libraries.endpointFreeIdentityMaterial(expected);
}

function inside(root, target) {
  const relative = path.relative(root, target);
  return relative !== "" && !relative.startsWith("..") && !path.isAbsolute(relative);
}

async function snapshotIdentity(runDir, db) {
  const docsRoot = path.join(runDir, "qmd-public/docs");
  const files = [];
  async function visit(directory) {
    for (const entry of (await readdir(directory, { withFileTypes: true })).sort((a, b) => a.name.localeCompare(b.name, "en"))) {
      const filename = path.join(directory, entry.name);
      if (entry.isSymbolicLink()) throw new Error("Public snapshot must not contain symlinks");
      if (entry.isDirectory()) await visit(filename);
      else if (entry.isFile()) files.push({ path: path.relative(docsRoot, filename), sha256: sha(await readFile(filename)) });
    }
  }
  await visit(docsRoot);
  const documents = db.prepare("SELECT collection,path,title,hash FROM documents WHERE active=1 ORDER BY collection,path").all();
  const fileHashes = new Map(files.map((file) => [file.path, file.sha256]));
  const folders = { "skill-meta": "meta", "skill-body": "body", "skill-references": "references" };
  for (const doc of documents) {
    const relative = path.join(folders[doc.collection] ?? "invalid", doc.path);
    if (fileHashes.get(relative) !== doc.hash) throw new Error("Target document content differs from its public snapshot file");
  }
  return { target_documents_sha256: sha(JSON.stringify(documents)), snapshot_files_sha256: sha(JSON.stringify(files)), document_count: documents.length, snapshot_file_count: files.length };
}

async function readPreflight(runDir, libraries) {
  const bytes = await readFile(path.join(runDir, "qmd-preflight.json"));
  const preflight = JSON.parse(bytes);
  if (preflight.model !== model || preflight.dimension !== dimension || preflight.chunk_strategy !== "regex") throw new Error("Preflight model/dimension/chunk strategy mismatch");
  if (JSON.stringify(preflight.provenance) !== JSON.stringify(libraries.provenance)) throw new Error("Installed QMD/snapshot source hashes changed since preflight");
  return { preflight, preflight_sha256: sha(bytes) };
}

function reconstructMissing(preflight, db, libraries) {
  const select = db.prepare("SELECT d.title,c.doc AS body FROM documents d JOIN content c ON c.hash=d.hash WHERE d.active=1 AND d.collection=? AND d.path=? AND d.hash=?");
  const inputs = [];
  const seen = new Set();
  for (const missing of preflight.missing_inputs) {
    const doc = select.get(missing.public_collection, missing.public_path, missing.content_hash);
    if (!doc || sha(doc.body) !== missing.content_hash) throw new Error("Missing-input public source identity changed");
    const title = libraries.extractTitle(doc.body, missing.public_path);
    const chunks = libraries.chunkRemoteDocumentByUtf8Bytes(doc.body, title);
    const chunk = chunks[missing.seq];
    if (doc.title !== title || !chunk || chunks.length !== missing.total_chunks) throw new Error("Missing-input title or chunk layout changed");
    const input = title ? `${title}\n${chunk.text}` : chunk.text;
    if (sha(input) !== missing.input_sha256 || Buffer.byteLength(input) !== missing.input_bytes || seen.has(missing.input_sha256)) throw new Error("Missing-input hash/bytes or uniqueness mismatch");
    seen.add(missing.input_sha256);
    inputs.push({ ...missing, input });
  }
  if (inputs.length !== preflight.missing_unique_inputs || inputs.reduce((sum, row) => sum + row.input_bytes, 0) !== preflight.missing_input_bytes) throw new Error("Missing-input denominator mismatch");
  return inputs;
}

export async function exportMissingInputs({ runDir, harnessRoot = defaultHarness }) {
  installNetworkDeny();
  runDir = path.resolve(runDir);
  if (!inside(path.join(workspace, "experiments/datasets"), runDir)) throw new Error("Output must be in workspace experiments/datasets");
  const libraries = await loadLibraries(harnessRoot);
  const { preflight, preflight_sha256 } = await readPreflight(runDir, libraries);
  const db = libraries.openReadOnlyDatabase(path.join(runDir, "qmd-public/skill-search.sqlite"));
  try {
    db.exec("PRAGMA query_only=ON");
    db.exec("BEGIN");
    const identity = await snapshotIdentity(runDir, db);
    const entries = reconstructMissing(preflight, db, libraries);
    const result = { schema_version: 1, created_at: new Date().toISOString(), model, dimension, preflight_sha256, ...identity, input_count: entries.length, input_bytes: entries.reduce((sum, entry) => sum + entry.input_bytes, 0), entries, scope: "Exact public target inputs only; no provider request or vector generation." };
    await writeFile(path.join(runDir, "missing-embedding-inputs.json"), JSON.stringify(result, null, 2) + "\n", { flag: "wx" });
    return result;
  } finally {
    db.exec("ROLLBACK");
    db.close();
  }
}

function offlineModels() {
  return { embed_provider: "openai", embed_api_url: offlineBase, embed_api_model: model, embed_dimension: dimension, embed_api_key: "offline-public-vector-reuse-placeholder", generate_api_url: offlineBase, generate_api_model: "offline-disabled", generate_api_key: "offline-placeholder", rerank_api_url: offlineBase, rerank_api_model: "offline-disabled", rerank_api_key: "offline-placeholder", jev_base_url: offlineBase, jev_api_model: "offline-disabled", jev_api_key: "offline-placeholder" };
}

function snapshotCollections(profileDir) {
  return {
    "skill-meta": { path: path.join(profileDir, "docs/meta"), pattern: "**/meta.md" },
    "skill-body": { path: path.join(profileDir, "docs/body"), pattern: "**/SKILL.md" },
    "skill-references": { path: path.join(profileDir, "docs/references"), pattern: "**/*", ignore: ["**/*.identity.json", "**/*.identity.yml"] },
  };
}

function validateSupplement(supplement, expectedInputs) {
  if (supplement.model !== model || supplement.dimension !== dimension || !Array.isArray(supplement.entries)) throw new Error("Supplement model/dimension/schema mismatch");
  const expected = new Map(expectedInputs.map((entry) => [entry.input_sha256, entry]));
  const vectors = new Map();
  for (const entry of supplement.entries) {
    const known = expected.get(entry.input_sha256);
    if (!known || vectors.has(entry.input_sha256) || typeof entry.input !== "string" || sha(entry.input) !== entry.input_sha256 || entry.input !== known.input || Buffer.byteLength(entry.input) !== known.input_bytes || (entry.input_bytes !== undefined && entry.input_bytes !== known.input_bytes)) throw new Error("Supplement input hash/bytes/required-set mismatch");
    if (!Array.isArray(entry.vector) || entry.vector.length !== dimension || entry.vector.some((value) => typeof value !== "number" || !Number.isFinite(value))) throw new Error("Supplement vector dimension/nonfinite mismatch");
    vectors.set(entry.input_sha256, { input: entry.input, vector: validateVector(new Float32Array(entry.vector)) });
  }
  if (vectors.size !== expected.size) throw new Error("Supplement required input set is incomplete");
  return vectors;
}

export async function resumeProfileOffline({ runDir, supplementPath, managedDbPath, mappingPath, harnessRoot = defaultHarness }) {
  const network = installNetworkDeny();
  runDir = path.resolve(runDir);
  if (!inside(path.join(workspace, "experiments/datasets"), runDir)) throw new Error("Output must be in workspace experiments/datasets");
  try {
    await readFile(path.join(runDir, "qmd-build.json"));
    throw new Error("qmd-build.json already exists; refusing another build");
  } catch (error) { if (error.code !== "ENOENT") throw error; }
  const libraries = await loadLibraries(harnessRoot);
  const { preflight, preflight_sha256 } = await readPreflight(runDir, libraries);
  const exportedBytes = await readFile(path.join(runDir, "missing-embedding-inputs.json"));
  const exported = JSON.parse(exportedBytes);
  if (exported.preflight_sha256 !== preflight_sha256 || exported.model !== model || exported.dimension !== dimension) throw new Error("Exported input/preflight identity mismatch");
  const supplementBytes = await readFile(supplementPath);
  const supplement = JSON.parse(supplementBytes);
  const profileDir = path.join(runDir, "qmd-public");
  const dbPath = path.join(profileDir, "skill-search.sqlite");
  const target = libraries.openReadOnlyDatabase(dbPath);
  let source, store;
  const cache = new Map();
  const transport = createCacheTransport({ cache });
  const mappingBefore = mappingPath ? await readFile(mappingPath) : undefined;
  let before, reuse, supplemental;
  try {
    target.exec("PRAGMA query_only=ON");
    target.exec("BEGIN");
    before = await snapshotIdentity(runDir, target);
    if (before.target_documents_sha256 !== exported.target_documents_sha256 || before.snapshot_files_sha256 !== exported.snapshot_files_sha256 || before.document_count !== preflight.document_count) throw new Error("Public target documents/snapshot changed since input export");
    const expectedInputs = reconstructMissing(preflight, target, libraries);
    if (JSON.stringify(expectedInputs) !== JSON.stringify(exported.entries)) throw new Error("Exported public inputs changed since reconstruction");
    supplemental = validateSupplement(supplement, expectedInputs);
    source = libraries.openReadOnlyDatabase(managedDbPath);
    source.exec("PRAGMA query_only=ON");
    libraries.loadSqliteVec(source);
    source.exec("BEGIN");
    reuse = await collectReuse(source, target, libraries, cache);
    if (!reuse.compatible) throw new Error("Managed source identity is no longer ready/compatible");
    for (const missing of reuse.missing) {
      if (!supplemental.has(missing.input_sha256)) throw new Error("Managed source coverage changed; an additional exact public input is unavailable");
    }
    source.exec("ROLLBACK");
    source.close();
    source = undefined;
    for (const { input, vector } of supplemental.values()) cache.set(input, vector);
  } finally {
    if (source) { try { source.exec("ROLLBACK"); } catch {} source.close(); }
    try { target.exec("ROLLBACK"); } catch {}
    target.close();
  }
  const mappingAfter = mappingPath ? await readFile(mappingPath) : undefined;
  try {
    globalThis.fetch = transport.fetch;
    store = await libraries.createStore({ dbPath, config: { collections: snapshotCollections(profileDir), models: offlineModels() } });
    const immediatelyBefore = await snapshotIdentity(runDir, store.internal.db);
    if (JSON.stringify(before) !== JSON.stringify(immediatelyBefore)) throw new Error("Public target changed before embedding build");
    const embedded = await store.embed({ chunkStrategy: "regex" });
    const after = await snapshotIdentity(runDir, store.internal.db);
    const targetState = store.internal.db.prepare("SELECT fingerprint,status,model,dimension,generation FROM embedding_index_state WHERE singleton=1").get();
    const vectorRows = store.internal.db.prepare("SELECT COUNT(*) AS n FROM content_vectors cv JOIN vectors_vec vv ON vv.hash_seq=(cv.hash || '_' || cv.seq) WHERE cv.model=? AND cv.embed_fingerprint=?").get(model, targetState?.fingerprint ?? "").n;
    const pending = store.internal.getHashesNeedingEmbedding();
    const preflightUnchanged = sha(await readFile(path.join(runDir, "qmd-preflight.json"))) === preflight_sha256;
    const documentStable = before.target_documents_sha256 === after.target_documents_sha256;
    const snapshotStable = before.snapshot_files_sha256 === after.snapshot_files_sha256;
    const ready = targetState?.status === "ready" && targetState.model === model && targetState.dimension === dimension && embedded.errors === 0 && vectorRows === preflight.target_chunk_occurrences && pending === 0 && transport.stats.cacheMissInputs === 0 && preflightUnchanged && documentStable && snapshotStable;
    const result = {
      schema_version: 1, created_at: new Date().toISOString(), status: ready ? "vector_ready" : "incomplete", vector_ready: ready,
      model, dimension, skill_count: preflight.skill_count, document_count: before.document_count,
      target_chunk_occurrences: preflight.target_chunk_occurrences, target_vector_rows: vectorRows, needs_embedding: pending,
      supplemental_inputs: supplemental.size, reused_unique_inputs: reuse.cache.size - supplemental.size,
      total_available_unique_inputs: cache.size, embedding_result: embedded,
      preflight_sha256, preflight_unchanged: preflightUnchanged,
      exported_inputs_sha256: sha(exportedBytes), supplemental_file_sha256: sha(supplementBytes),
      target_documents_sha256_before: before.target_documents_sha256, target_documents_sha256_after: after.target_documents_sha256,
      snapshot_files_sha256_before: before.snapshot_files_sha256, snapshot_files_sha256_after: after.snapshot_files_sha256,
      target_documents_unchanged: documentStable, snapshot_files_unchanged: snapshotStable,
      source_embedding_identity: { fingerprint: reuse.state.fingerprint, generation: reuse.state.generation, status: reuse.state.status, compatible: reuse.compatible },
      source_identity_differs_from_preflight: reuse.state.fingerprint !== preflight.source_embedding_identity.fingerprint || reuse.state.generation !== preflight.source_embedding_identity.generation,
      source_generation_at_preflight: preflight.source_embedding_identity.generation,
      mapping_sha256_before: mappingBefore ? sha(mappingBefore) : null, mapping_sha256_after: mappingAfter ? sha(mappingAfter) : null,
      mapping_stable_during_capture: mappingBefore ? mappingBefore.equals(mappingAfter) : null,
      target_embedding_identity: targetState,
      transport: { ...transport.stats, outbound_network_requests: 0, usage: "Local synthetic cache responses only; supplemental vector acquisition/billing belongs to its separate parent-controlled ledger." },
      network_guards: { ...network }, provenance: libraries.provenance,
      limits: ["Source database remains read-only; only exact public vectors and the explicit validated supplement enter the target build.", "The original preflight is preserved; live source generation differences are recorded separately.", "No query embeddings, expansion, host Decision or routing-quality score is produced."],
    };
    await writeFile(path.join(runDir, "qmd-build.json"), JSON.stringify(result, null, 2) + "\n", { flag: "wx" });
    if (!ready) throw new Error("Offline QMD embedding build did not satisfy readiness/identity checks");
    return result;
  } finally {
    if (store) await store.close();
    installNetworkDeny();
  }
}

async function publicSkills(root, matter) {
  const skills = [];
  for (const name of (await readdir(path.join(root, "skills"))).sort()) {
    const location = path.join(root, "skills", name, "SKILL.md");
    let raw;
    try { raw = await readFile(location, "utf8"); } catch (error) { if (error.code === "ENOENT" || error.code === "ENOTDIR") continue; throw error; }
    const parsed = matter(raw);
    if (parsed.data.name !== name || typeof parsed.data.description !== "string") throw new Error(`Invalid public skill metadata: ${name}`);
    skills.push({ name, description: parsed.data.description.trim(), location });
  }
  return skills;
}

async function collectReuse(source, target, libraries, cache) {
  const state = source.prepare("SELECT fingerprint, provider_id, model, dimension, remote, canonical_material, status, generation FROM embedding_index_state WHERE singleton=1").get();
  const compatible = compatibleIdentity(state, libraries);
  const docs = target.prepare("SELECT d.collection, d.path, d.title, d.hash, c.doc AS body FROM documents d JOIN content c ON c.hash=d.hash WHERE d.active=1 ORDER BY d.path,d.collection").all();
  const byHash = new Map();
  for (const doc of docs) {
    const values = byHash.get(doc.hash) ?? [];
    values.push(doc);
    byHash.set(doc.hash, values);
  }
  const exact = source.prepare("SELECT 1 AS present FROM documents d JOIN content c ON c.hash=d.hash WHERE d.active=1 AND d.collection=? AND d.path=? AND d.title=? AND d.hash=? AND c.doc=? LIMIT 1");
  const ambiguous = source.prepare("SELECT COUNT(*) AS n FROM documents WHERE active=1 AND hash=? AND title<>?");
  const vectors = source.prepare("SELECT cv.seq,cv.pos,cv.total_chunks,vv.embedding FROM content_vectors cv JOIN vectors_vec vv ON vv.hash_seq=(cv.hash || '_' || cv.seq) WHERE cv.hash=? AND cv.model=? AND cv.embed_fingerprint=? AND cv.total_chunks=? AND cv.seq>=0 AND cv.seq<? ORDER BY cv.seq");
  const missing = new Map();
  const conflicts = new Set();
  const documentRows = [];
  let targetChunks = 0;
  for (const [hash, aliases] of byHash) {
    // QMD embeds each unique content hash using MIN(document.path).
    const doc = aliases[0];
    const title = libraries.extractTitle(doc.body, doc.path);
    if (await libraries.hashContent(doc.body) !== hash) throw new Error("Target content hash does not match QMD hashContent");
    const chunks = libraries.chunkRemoteDocumentByUtf8Bytes(doc.body, title);
    targetChunks += chunks.length;
    const exactAliases = aliases.filter((alias) => alias.title === title && exact.get(alias.collection, alias.path, alias.title, hash, doc.body));
    const hasAmbiguousTitle = compatible && exactAliases.length ? ambiguous.get(hash, title).n !== 0 : false;
    const rows = compatible && exactAliases.length && !hasAmbiguousTitle ? vectors.all(hash, model, state.fingerprint, chunks.length, chunks.length) : [];
    const bySeq = new Map(rows.map((row) => [row.seq, row]));
    let reusable = 0;
    for (let seq = 0; seq < chunks.length; seq++) {
      const chunk = chunks[seq];
      const input = title ? `${title}\n${chunk.text}` : chunk.text;
      const inputHash = sha(input);
      let vector;
      const row = bySeq.get(seq);
      let reason = !compatible ? "incompatible_source_embedding_identity" : !exactAliases.length ? "no_exact_public_document_identity" : hasAmbiguousTitle ? "ambiguous_managed_title_provenance" : "missing_or_incompatible_vector_row";
      if (row && row.pos === chunk.pos && row.total_chunks === chunks.length) {
        try { vector = validateVector(row.embedding); } catch { reason = "invalid_vector_payload"; }
      }
      if (vector && !conflicts.has(input)) {
        const prior = cache.get(input);
        if (prior && !Buffer.from(prior.buffer, prior.byteOffset, prior.byteLength).equals(Buffer.from(vector.buffer, vector.byteOffset, vector.byteLength))) {
          conflicts.add(input);
          cache.delete(input);
          reason = "conflicting_exact_input_vectors";
        } else {
          cache.set(input, vector);
          reusable++;
          continue;
        }
      }
      const detail = { input_sha256: inputHash, input_bytes: Buffer.byteLength(input), content_hash: hash, seq, total_chunks: chunks.length, public_collection: doc.collection, public_path: doc.path, reason };
      missing.set(inputHash, detail);
    }
    documentRows.push({ content_hash: hash, public_collection: doc.collection, public_path: doc.path, title, alias_count: aliases.length, exact_managed_public_aliases: exactAliases.length, chunks: chunks.length, reusable_chunks: reusable });
  }
  // An identical public input can be reusable through another exact document.
  for (const input of cache.keys()) missing.delete(sha(input));
  return { cache, state, compatible, docs, byHash, targetChunks, documentRows, missing: [...missing.values()], conflicts: conflicts.size };
}

export async function prepareProfile({ root = workspace, runDir, managedDbPath, mappingPath, expectedSkillCount = 963, harnessRoot = defaultHarness }) {
  const network = installNetworkDeny();
  runDir = path.resolve(runDir);
  if (!inside(path.join(workspace, "experiments/datasets"), runDir)) throw new Error("Output must be in workspace experiments/datasets");
  const libraries = await loadLibraries(harnessRoot);
  const skills = await publicSkills(path.resolve(root), libraries.matter);
  if (skills.length !== expectedSkillCount) throw new Error(`Expected ${expectedSkillCount} public skills; observed ${skills.length}`);
  const mappingBefore = mappingPath ? await readFile(mappingPath) : undefined;
  if (mappingBefore) {
    const allowed = new Set(JSON.parse(mappingBefore).allowedSkillNames);
    if (skills.some((skill) => !allowed.has(skill.name))) throw new Error("Managed allowlist does not include every public target skill");
  }
  await mkdir(runDir, { recursive: true });
  const profileDir = path.join(runDir, "qmd-public");
  // Atomic mkdir refuses an existing partial or completed profile.
  await mkdir(profileDir);
  const cache = new Map();
  const transport = createCacheTransport({ cache });
  let store, source;
  try {
    const collections = await libraries.writeSkillSnapshot({ docsRoot: path.join(profileDir, "docs"), skills });
    globalThis.fetch = transport.fetch;
    store = await libraries.createStore({ dbPath: path.join(profileDir, "skill-search.sqlite"), config: { collections, models: offlineModels() } });
    const update = await store.update();
    source = libraries.openReadOnlyDatabase(managedDbPath);
    source.exec("PRAGMA query_only=ON");
    libraries.loadSqliteVec(source);
    source.exec("BEGIN");
    const reuse = await collectReuse(source, store.internal.db, libraries, cache);
    source.exec("ROLLBACK");
    source.close();
    source = undefined;
    const mappingAfter = mappingPath ? await readFile(mappingPath) : undefined;
    let embedded;
    if (!reuse.missing.length) {
      embedded = await store.embed({ chunkStrategy: "regex" });
      if (embedded.errors || transport.misses.size) throw new Error("Exact public-vector build unexpectedly encountered missing inputs");
    }
    // Check the published build state directly, without depending on diagnostics shape.
    const targetState = store.internal.db.prepare("SELECT fingerprint,status,model,dimension FROM embedding_index_state WHERE singleton=1").get();
    const result = {
      schema_version: 1, created_at: new Date().toISOString(),
      status: reuse.missing.length ? "blocked_missing_exact_public_vectors" : targetState?.status === "ready" ? "vector_ready" : "not_ready",
      vector_ready: reuse.missing.length === 0 && targetState?.status === "ready",
      skill_count: skills.length, document_count: reuse.docs.length, unique_content_hashes: reuse.byHash.size,
      target_chunk_occurrences: reuse.targetChunks, reusable_unique_inputs: cache.size,
      missing_unique_inputs: reuse.missing.length, missing_input_bytes: reuse.missing.reduce((sum, row) => sum + row.input_bytes, 0),
      total_unique_inputs: cache.size + reuse.missing.length, conflicting_vector_inputs: reuse.conflicts,
      model, dimension, chunk_strategy: "regex", remote_chunk_profile: libraries.REMOTE_EMBEDDING_CHUNK_PROFILE,
      source_embedding_identity: { compatible: reuse.compatible, fingerprint: reuse.state?.fingerprint, status: reuse.state?.status, model: reuse.state?.model, dimension: reuse.state?.dimension, generation: reuse.state?.generation, canonical_material_sha256: reuse.state ? sha(reuse.state.canonical_material) : null },
      source_access: "Read-only connection, query_only, pinned read transaction; SELECT only exact public document identities and their hash/seq vector payloads. No TTL cache or whole database is copied.",
      mapping_sha256_before: mappingBefore ? sha(mappingBefore) : null, mapping_sha256_after: mappingAfter ? sha(mappingAfter) : null,
      mapping_stable_during_capture: mappingBefore ? mappingBefore.equals(mappingAfter) : null,
      target_profile: profileDir, collection_counts: Object.fromEntries(store.internal.db.prepare("SELECT collection,COUNT(*) AS n FROM documents WHERE active=1 GROUP BY collection").all().map((row) => [row.collection, row.n])),
      update_result: update, embedding_result: embedded ?? null, target_embedding_identity: targetState ?? null,
      transport: { ...transport.stats, outbound_network_requests: 0, usage: "Synthetic cache replay response usage=0; no observed provider billing claim." }, network_guards: { ...network },
      provenance: libraries.provenance,
      missing_inputs: reuse.missing, public_document_coverage: reuse.documentRows,
      limits: ["Every target skill remains in the public corpus, including changed same-name bodies such as triage.", "Missing inputs are not sent to a provider; no full embedding build is attempted until every exact input is available.", "Reuse proves current exact normalized document/title/chunk identity and compatible model space; it does not identify the original private winning source path.", "The managed database transaction is consistent; the live runtime catalog is not frozen.", "No query embeddings, expansion, host Decision calls or routing-quality evaluation are performed."],
    };
    await writeFile(path.join(runDir, "qmd-preflight.json"), JSON.stringify(result, null, 2) + "\n", { flag: "wx" });
    return result;
  } finally {
    if (source) { try { source.exec("ROLLBACK"); } catch {} source.close(); }
    if (store) await store.close();
    installNetworkDeny();
  }
}

async function main() {
  const args = process.argv.slice(2);
  const value = (name, fallback) => { const index = args.indexOf(name); return index === -1 ? fallback : args[index + 1]; };
  if (!value("--run-dir")) throw new Error("--run-dir is required");
  if (args.includes("--export-missing")) {
    const result = await exportMissingInputs({ runDir: value("--run-dir"), harnessRoot: value("--harness-root", defaultHarness) });
    console.log(JSON.stringify({ output: path.join(value("--run-dir"), "missing-embedding-inputs.json"), input_count: result.input_count, input_bytes: result.input_bytes, model: result.model, dimension: result.dimension }, null, 2));
    return;
  }
  const runtime = value("--runtime-skills-dir", path.join(os.homedir(), ".openclaw/plugins/skill-harness/qmd/skills"));
  const mappingPath = path.join(runtime, "agents/main.json");
  const mapping = JSON.parse(await readFile(mappingPath, "utf8"));
  if (!/^[a-f0-9]{64}$/.test(mapping.fingerprint)) throw new Error("Invalid managed mapping fingerprint");
  const options = { root: value("--root", workspace), runDir: value("--run-dir"), mappingPath, managedDbPath: path.join(runtime, "indexes", mapping.fingerprint, "skill-search.sqlite"), harnessRoot: value("--harness-root", defaultHarness) };
  const result = value("--resume-with-supplement") ? await resumeProfileOffline({ ...options, supplementPath: value("--resume-with-supplement") }) : await prepareProfile(options);
  console.log(JSON.stringify(Object.fromEntries(["status", "skill_count", "document_count", "unique_content_hashes", "target_chunk_occurrences", "reusable_unique_inputs", "missing_unique_inputs", "missing_input_bytes", "vector_ready", "transport", "network_guards"].map((key) => [key, result[key]])), null, 2));
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) await main();
