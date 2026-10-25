import assert from "node:assert/strict";
import { mkdtemp, mkdir, readFile, writeFile, rm } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import {
  compatibleIdentity, createCacheTransport, installNetworkDeny, loadLibraries,
  exportMissingInputs, prepareProfile, resumeProfileOffline, validateVector,
} from "../scripts/prepare_harness_qmd.mjs";

const workspace = fileURLToPath(new URL("../../", import.meta.url));
const parent = path.join(workspace, "experiments/datasets/qmd-test-fixtures");
await mkdir(parent, { recursive: true });

test("cache transport requires exact public input and records misses before any network", async () => {
  const transport = createCacheTransport({ dimension: 2, cache: new Map([["Title\nbody", new Float32Array([1, 0])]]) });
  const init = { method: "POST", body: JSON.stringify({ model: "text-embedding-3-small", dimensions: 2, input: ["Title\nbody"] }) };
  const response = await transport.fetch("https://qmd-reuse.invalid/v1/embeddings", init);
  assert.deepEqual((await response.json()).data[0].embedding, [1, 0]);
  await assert.rejects(transport.fetch("https://qmd-reuse.invalid/v1/embeddings", { ...init, body: JSON.stringify({ model: "text-embedding-3-small", dimensions: 2, input: ["Title\nchanged"] }) }), /Cache miss/);
  await assert.rejects(transport.fetch("https://example.invalid/embeddings", init), /Offline/);
  assert.equal(transport.stats.cacheResponses, 1);
  assert.equal(transport.stats.cacheMissInputs, 1);
  assert.equal(transport.misses.size, 1);
});

test("vector validation rejects wrong dimensions, nonfinite and zero payloads", () => {
  assert.throws(() => validateVector(new Float32Array([1]), 2), /dimension/);
  assert.throws(() => validateVector(new Float32Array([1, NaN]), 2), /nonfinite/);
  assert.throws(() => validateVector(new Float32Array([0, 0]), 2), /zero/);
  assert.deepEqual([...validateVector(new Float32Array([1, 0]), 2)], [1, 0]);
});

test("actual QMD profile reuses document vectors through authorized embed transport", async (t) => {
  const temporary = await mkdtemp(path.join(parent, "reuse-"));
  t.after(() => rm(temporary, { recursive: true, force: true }));
  const root = path.join(temporary, "public");
  await mkdir(path.join(root, "skills/garden/references"), { recursive: true });
  await writeFile(path.join(root, "skills/garden/SKILL.md"), "---\nname: garden\ndescription: Grow plants\n---\n# Plants\nWater the basil.\n");
  await writeFile(path.join(root, "skills/garden/references/water.md"), "# Water\nWater when dry.\n");
  const guard = installNetworkDeny();
  const libraries = await loadLibraries();
  const sourceDocs = path.join(temporary, "source-docs");
  const collections = await libraries.writeSkillSnapshot({ docsRoot: sourceDocs, skills: [{ name: "garden", description: "Grow plants", location: path.join(root, "skills/garden/SKILL.md") }] });
  let seedRequests = 0;
  globalThis.fetch = async (_url, init) => {
    seedRequests++;
    const request = JSON.parse(init.body);
    return Response.json({ object: "list", model: request.model, data: request.input.map((_, index) => ({ object: "embedding", index, embedding: [1, ...Array(1535).fill(0)] })), usage: { prompt_tokens: 0, total_tokens: 0 } });
  };
  const sourceDb = path.join(temporary, "source.sqlite");
  const seed = await libraries.createStore({ dbPath: sourceDb, config: { collections, models: { embed_api_url: "https://qmd-reuse.invalid/v1", embed_api_model: "text-embedding-3-small", embed_dimension: 1536, embed_api_key: "offline-test-placeholder" } } });
  await seed.update();
  const seeded = await seed.embed({ chunkStrategy: "regex" });
  assert.equal(seeded.errors, 0);
  assert.ok(seedRequests > 0);
  await seed.close();
  const readonly = libraries.openReadOnlyDatabase(sourceDb);
  const identity = readonly.prepare("SELECT * FROM embedding_index_state WHERE singleton=1").get();
  assert.equal(compatibleIdentity(identity, libraries), true);
  assert.equal(compatibleIdentity({ ...identity, status: "building" }, libraries), false);
  assert.equal(compatibleIdentity({ ...identity, model: "voyage-4" }, libraries), false);
  assert.equal(compatibleIdentity({ ...identity, canonical_material: "{}" }, libraries), false);
  readonly.close();
  const result = await prepareProfile({ root, runDir: path.join(temporary, "target"), managedDbPath: sourceDb, expectedSkillCount: 1 });
  assert.equal(result.skill_count, 1);
  assert.equal(result.document_count, 3);
  assert.equal(result.missing_unique_inputs, 0);
  assert.equal(result.vector_ready, true);
  assert.equal(result.transport.cacheResponses > 0, true);
  assert.equal(result.embedding_result.errors, 0);
  assert.equal(result.transport.cacheMissInputs, 0);
  assert.equal(guard.socketAttempts, 0);
  assert.equal(guard.dnsAttempts, 0);

  // Keep the same public label but change its body. The source vector must not
  // be accepted by name/path alone, and the full target remains in the corpus.
  await writeFile(path.join(root, "skills/garden/SKILL.md"), "---\nname: garden\ndescription: Grow plants\n---\n# Plants\nA changed public body.\n");
  const changed = await prepareProfile({ root, runDir: path.join(temporary, "changed"), managedDbPath: sourceDb, expectedSkillCount: 1 });
  assert.equal(changed.skill_count, 1);
  assert.equal(changed.document_count, 3);
  assert.equal(changed.vector_ready, false);
  assert.equal(changed.missing_unique_inputs, 1);
  assert.equal(changed.transport.cacheResponses, 0);
  assert.equal(changed.missing_inputs[0].reason, "no_exact_public_document_identity");

  const changedDir = path.join(temporary, "changed");
  const exported = await exportMissingInputs({ runDir: changedDir });
  assert.equal(exported.input_count, 1);
  const supplementalPath = path.join(temporary, "supplement.json");
  const validSupplement = { model: "text-embedding-3-small", dimension: 1536, entries: exported.entries.map(({ input_sha256, input }) => ({ input_sha256, input, vector: [1, ...Array(1535).fill(0)] })) };
  const beforeRejectedResume = await readFile(path.join(changedDir, "qmd-public/skill-search.sqlite"));
  const wrongHash = structuredClone(validSupplement);
  wrongHash.entries[0].input_sha256 = "0".repeat(64);
  await writeFile(supplementalPath, JSON.stringify(wrongHash));
  await assert.rejects(resumeProfileOffline({ runDir: changedDir, managedDbPath: sourceDb, supplementPath: supplementalPath }), /hash/);
  const wrongDimension = structuredClone(validSupplement);
  wrongDimension.entries[0].vector.pop();
  await writeFile(supplementalPath, JSON.stringify(wrongDimension));
  await assert.rejects(resumeProfileOffline({ runDir: changedDir, managedDbPath: sourceDb, supplementPath: supplementalPath }), /dimension/);
  assert.deepEqual(await readFile(path.join(changedDir, "qmd-public/skill-search.sqlite")), beforeRejectedResume);
  await writeFile(supplementalPath, JSON.stringify(validSupplement));
  const resumed = await resumeProfileOffline({ runDir: changedDir, managedDbPath: sourceDb, supplementPath: supplementalPath });
  assert.equal(resumed.vector_ready, true);
  assert.equal(resumed.supplemental_inputs, 1);
  assert.equal(resumed.target_vector_rows, 3);
  assert.equal(resumed.target_documents_unchanged, true);
  assert.equal(resumed.snapshot_files_unchanged, true);
  assert.equal(resumed.transport.cacheMissInputs, 0);
  assert.ok(resumed.transport.cacheResponses > 0);

  // Corrupt only our synthetic source metadata; total_chunks is a reuse gate.
  const db = new libraries.Database(sourceDb);
  db.exec("UPDATE content_vectors SET total_chunks = 77");
  db.close();
  const invalid = await prepareProfile({ root, runDir: path.join(temporary, "invalid-layout"), managedDbPath: sourceDb, expectedSkillCount: 1 });
  assert.equal(invalid.vector_ready, false);
  assert.equal(invalid.reusable_unique_inputs, 0);
  assert.ok(invalid.missing_inputs.some((row) => row.reason === "missing_or_incompatible_vector_row"));
});

test("offline guard denies ambient fetch, sockets and DNS before SDK imports", async () => {
  const guard = installNetworkDeny();
  const net = await import("node:net");
  const dns = await import("node:dns");
  await assert.rejects(globalThis.fetch("https://example.invalid"), /Offline/);
  assert.throws(() => net.connect(9, "127.0.0.1"), /Offline/);
  assert.throws(() => dns.lookup("example.invalid", () => {}), /Offline/);
  assert.ok(guard.socketAttempts >= 1);
  assert.ok(guard.dnsAttempts >= 1);
});
