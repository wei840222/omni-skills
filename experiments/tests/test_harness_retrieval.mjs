import assert from "node:assert/strict";
import { mkdir, mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { createHarnessRetrievalAdapter, loadInstalledRetrievalSources } from "../scripts/harness_retrieval_adapter.mjs";

const workspace = fileURLToPath(new URL("../../", import.meta.url));
const parent = path.join(workspace, "experiments/datasets/harness-quality-20261025/replay-runtime/test-fixtures");
await mkdir(parent, { recursive: true });
const temporary = await mkdtemp(path.join(parent, "run-"));
const root = path.join(temporary, "public");
const profileDir = path.join(temporary, "profile");
const sources = await loadInstalledRetrievalSources({ offline: true });
const skills = [];
for (const name of ["garden", "database"]) {
  const location = path.join(root, "skills", name, "SKILL.md");
  await mkdir(path.dirname(location), { recursive: true });
  await writeFile(location, `---\nname: ${name}\ndescription: Work with ${name}\n---\n# ${name}\nHelp with ${name}.\n`);
  skills.push({ name, location, description: `Work with ${name}` });
}
const collections = await sources.writeSkillSnapshot({ docsRoot: path.join(profileDir, "docs"), skills });
globalThis.fetch = async (_url, init) => {
  const body = JSON.parse(init.body);
  return Response.json({ object: "list", model: body.model, data: body.input.map((_, index) => ({ object: "embedding", index, embedding: [1, ...Array(1535).fill(0)] })), usage: { prompt_tokens: 0, total_tokens: 0 } });
};
const seed = await sources.createStore({ dbPath: path.join(profileDir, "skill-search.sqlite"), config: { collections, models: { embed_provider: "openai", embed_api_url: "https://qmd-reuse.invalid/v1", embed_api_model: "text-embedding-3-small", embed_dimension: 1536, embed_api_key: "offline-fixture" } } });
await seed.update();
await seed.embed({ chunkStrategy: "regex" });
await seed.close();

const settings = {
  qmd: { timeoutMs: 10000, embedding: { model: "text-embedding-3-small", dimension: 1536 }, expansion: { model: "gemini-3.5-flash-lite" }, jev: { model: "jev-latest" } },
  skills: { search: { collectionWeights: { meta: 3, body: 2, references: 1 } } },
  routing: { skills: { maxInjectedSkills: 1, search: { minCandidateScore: 0.4, timeoutMs: 10000 }, nameMatch: { maxEditDistance: 2, minJaccardScore: 0.5, genericTokens: [] } } },
};
const payloads = [];
const callback = async (url, init) => {
  const body = JSON.parse(init.body);
  payloads.push({ url: String(url), body });
  if (String(url).endsWith("/embeddings")) return Response.json({ object: "list", model: body.model, data: body.input.map((_, index) => ({ object: "embedding", index, embedding: [1, ...Array(1535).fill(0)] })), usage: { prompt_tokens: 0, total_tokens: 0 } });
  if (String(url).endsWith("/systemone")) return Response.json({ model: body.model, answers: { strategy: { type: "choice", choice: "how_to_guide", confidence: 0.9 }, needs_hyde: { type: "noul", noul: 0.1 } }, usage: { input_tokens: 1, output_tokens: 1 } });
  if (String(url).endsWith("/chat/completions")) return Response.json({ choices: [{ message: { content: "lex: basil leaves\nvec: How do I grow healthy basil?" } }], usage: { prompt_tokens: 1, completion_tokens: 1 } });
  throw new Error("Unexpected fixture route");
};
const adapter = await createHarnessRetrievalAdapter({ root, profileDir, dataRoot: path.join(temporary, "managed"), resolvedConfig: settings, fetchImpl: callback, offline: true, fixture: true, expectedSkillCount: 2 });
test.after(async () => { await adapter.close(); await rm(temporary, { recursive: true, force: true }); });

test("actual three-collection query preserves raw hits before source skill max/cap", async () => {
  const result = await adapter.retrieve({ query: "expand: My basil leaves need help", expansionContext: "Public fixture: indoor herbs.", expected: "PRIVATE_LABEL_SENTINEL", ground_truth_skill: "PRIVATE_LABEL_SENTINEL" });
  assert.equal(result.status, "completed");
  assert.equal(result.rawHitlists.length, 3);
  assert.ok(result.rawHitlists.every(({ options }) => options.limit === 40 && options.candidateLimit === 40 && options.rerank === false && options.explain === true));
  assert.ok(result.rawHitlists.every(({ options }) => options.expansionContext === "Public fixture: indoor herbs."));
  assert.ok(result.skillHits.length <= 1);
  assert.ok(result.skillHits.every((hit) => typeof hit.semanticScore === "number" && hit.score !== hit.semanticScore));
  assert.ok(payloads.some(({ url }) => url.endsWith("/embeddings")));
  assert.ok(payloads.some(({ url }) => url.endsWith("/chat/completions")));
  assert.ok(payloads.some(({ url }) => url.endsWith("/systemone")));
  assert.ok(payloads.some(({ url, body }) => url.endsWith("/chat/completions") && body.messages[1].content.includes("<search_intent>")));
  assert.equal(JSON.stringify(payloads).includes("PRIVATE_LABEL_SENTINEL"), false);
  assert.equal(payloads.some(({ url }) => url.endsWith("/rerank")), false);
  assert.ok(result.rawHitlists.some(({ hits }) => hits.length > result.skillHits.length));
  const manifest = adapter.rawHitlistManifest();
  assert.equal(manifest.profile.publicSkillCount, 2);
  assert.equal(manifest.scope, "controlled-tiny-fixture");
  assert.equal(manifest.observations.length, 1);
  assert.ok(manifest.provenance.sources.length >= 6);
});

test("conversation expansion uses the installed pure hook export and actual name tokens", () => {
  const context = adapter.buildExpansionContext({ query: "garden", conversation: [{ role: "user", text: "My basil is indoors." }, { role: "assistant", text: "How much light does it receive?" }] });
  assert.ok(context.includes("Detected candidate skill terms in user query:\ngarden"));
  assert.ok(context.includes("- [user] My basil is indoors."));
  assert.ok(context.includes("- [assistant] How much light does it receive?"));
  assert.equal(adapter.rawHitlistManifest().provenance.contextHelper.export, "formatConversationExpansionContext");
});

test("actual rounded semantic gate precedes the actual source candidate union", () => {
  const result = adapter.candidatesFromHits({ query: "garden", skillHits: [{ name: "database", score: 0.99, semanticScore: 0.395, evidence: [{ collection: "skill-body", path: "SKILL.md", score: 0.99 }] }, { name: "garden", score: 1, semanticScore: 0.394 }] });
  assert.deepEqual(result.retrievalCandidates.map((entry) => entry.skillName), ["database"]);
  assert.equal(result.retrievalCandidates[0].score, 0.395);
  assert.deepEqual(new Set(result.candidateSkills.map((entry) => entry.name)), new Set(["garden", "database"]));
  // The installed union retains its full deduplicated pool. It does not apply
  // another maxInjectedSkills cap after QMD's direct retrieval cap.
  assert.equal(result.candidateSkills.length, 2);
});

test("empty query and disabled policy avoid model transports", async () => {
  const before = payloads.length;
  const empty = await adapter.retrieve({ query: "   " });
  assert.equal(empty.status, "empty-query");
  assert.equal(payloads.length, before);
  const disabled = adapter.candidatesFromHits({ query: "garden", skillHits: [], enabled: false });
  assert.deepEqual(disabled.candidateSkills, []);
  const disabledConfig = structuredClone(settings);
  disabledConfig.routing.skills.maxInjectedSkills = 0;
  const disabledAdapter = await createHarnessRetrievalAdapter({ root, profileDir, dataRoot: path.join(temporary, "managed-disabled"), resolvedConfig: disabledConfig, fetchImpl: callback, offline: true, fixture: true, expectedSkillCount: 2 });
  try {
    const result = await disabledAdapter.retrieve({ query: "garden" });
    assert.equal(result.status, "disabled");
    assert.deepEqual(result.candidateSkills, []);
    assert.equal(payloads.length, before);
  } finally { await disabledAdapter.close(); }
});

test("workspace managed layout retains regular directories/file and public-only mapping", async () => {
  const manifest = adapter.rawHitlistManifest();
  const mapping = JSON.parse(await readFile(manifest.profile.mappingPath, "utf8"));
  assert.deepEqual(mapping.allowedSkillNames, ["database", "garden"]);
  assert.equal(manifest.profile.model, "text-embedding-3-small");
  assert.equal(manifest.profile.dimension, 1536);
  assert.equal(manifest.provenance.network.socketAttempts, 0);
  assert.equal(manifest.provenance.network.dnsAttempts, 0);
});
