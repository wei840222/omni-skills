import assert from "node:assert/strict";
import { mkdir, mkdtemp, readFile, rm } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { createFrozenFusionReplay } from "../scripts/harness_fusion.mjs";

const workspace = fileURLToPath(new URL("../../", import.meta.url));
const run = path.join(workspace, "experiments/datasets/harness-quality-20261025");
const frozenBytes = await readFile(path.join(run, "m0-query-probes.json"));
// Read only the allowed M0 retrieval observations/policies, never label files.
const frozen = JSON.parse(frozenBytes).raw_hitlists;
const parent = path.join(run, "replay-runtime/fusion-test-fixtures");
await mkdir(parent, { recursive: true });
const fixtureRoot = await mkdtemp(path.join(parent, "run-"));
const replay = await createFrozenFusionReplay({ config: frozen.policies, fixtureRoot });
test.after(async () => { await replay.close(); await rm(fixtureRoot, { recursive: true, force: true }); });
const names = replay.publicNames.slice(0, 8);
const document = (name, rank, suffix = "SKILL.md", semantic = 0.9) => ({ file: `qmd://skill-body/${name}/${suffix}`, body: `# Public frozen ${name}\nFixture content.`, score: 1 - rank / 100, explain: { vectorScores: [semantic], ftsScores: [] } });
function observation(meta = [], body = [], references = []) {
  return { query: "這是公開的融合演算法重播", rawHitlists: [["skill-meta", meta], ["skill-body", body], ["skill-references", references]].map(([collection, hits]) => ({ options: { collection, limit: 40, candidateLimit: 40, rerank: false, explain: true }, hits: hits.map((hit) => ({ ...hit, file: hit.file.replace("skill-body", collection) })) })) };
}

test("current-max exactly reproduces all five M0 skill rankings, scores, semantics and evidence", async () => {
  assert.equal(frozen.observations.length, 5);
  for (const original of frozen.observations) {
    const actual = await replay.rankFrozenCandidates({ observation: original, fusion: "current-max", poolLimit: 6 });
    assert.deepEqual(actual.skillHits, original.skillHits);
    assert.deepEqual(actual.retrievalCandidates, original.retrievalCandidates);
    assert.equal(actual.metadata.injectionCap, 6);
    assert.equal(actual.metadata.sourceCallsAreFrozen, true);
  }
});

test("six meta documents precede body rank one under unchanged current-max weights", async () => {
  const input = observation(names.slice(0, 6).map((name, index) => document(name, index, "meta.md")), [document(names[6], 0)]);
  const actual = await replay.rankFrozenCandidates({ observation: input, fusion: "current-max", poolLimit: 6 });
  assert.deepEqual(actual.skillHits.map((hit) => hit.name), names.slice(0, 6));
  assert.equal(actual.skillHits[5].score, 3 / 66);
  const larger = await replay.rankFrozenCandidates({ observation: input, fusion: "current-max", poolLimit: 10 });
  assert.equal(larger.skillHits[6].name, names[6]);
  assert.equal(larger.skillHits[6].score, 2 / 61);
  assert.equal(larger.metadata.injectionCap, 6);
});

test("skill-identity-sum combines corroboration across collections without relabeling", async () => {
  const input = observation(names.slice(0, 6).map((name, index) => document(name, index, "meta.md")), [document(names[5], 0)]);
  const current = await replay.rankFrozenCandidates({ observation: input, fusion: "current-max", poolLimit: 6 });
  const alternative = await replay.rankFrozenCandidates({ observation: input, fusion: "skill-identity-sum", poolLimit: 6 });
  assert.equal(current.skillHits[0].name, names[0]);
  assert.equal(alternative.skillHits[0].name, names[5]);
  assert.equal(alternative.skillHits[0].score, 3 / 66 + 2 / 61);
  assert.equal(alternative.skillHits[0].semanticScore, 0.9);
});

test("multiple reference files never sum within a collection or compress later document ranks", async () => {
  const input = observation([], [], [document(names[0], 0, "a.md", 0.4), document(names[0], 1, "b.md", 0.95), document(names[1], 2, "c.md", 0.8)]);
  const actual = await replay.rankFrozenCandidates({ observation: input, fusion: "skill-identity-sum", poolLimit: 20 });
  assert.equal(actual.skillHits[0].score, 1 / 61);
  assert.equal(actual.skillHits[0].semanticScore, 0.95);
  assert.equal(actual.skillHits[1].score, 1 / 63);
  assert.ok(actual.skillHits[0].evidence.length <= 3);
  assert.equal(actual.metadata.injectionCap, 6);
});

test("equal cross-collection contributions preserve source skill-name tie ordering", async () => {
  const meta = Array.from({ length: 38 }, (_, rank) => document(names[0], rank, `meta-${rank}.md`));
  meta.push(document(names[1], 38, "last-meta.md"));
  const body = Array.from({ length: 5 }, (_, rank) => document(names[2], rank, `body-${rank}.md`));
  body.push(document(names[3], 5, "last-body.md"));
  const tiedScore = 3 / 99;
  assert.equal(tiedScore, 2 / 66);
  for (const fusion of ["current-max", "skill-identity-sum"]) {
    const actual = await replay.rankFrozenCandidates({ observation: observation(meta, body), fusion, poolLimit: 6 });
    assert.deepEqual(actual.skillHits.filter((hit) => hit.score === tiedScore).map((hit) => hit.name), [names[1], names[3]].sort((left, right) => left.localeCompare(right)));
  }
});

test("identical reference paths retain original ranks but do not double count", async () => {
  const input = observation([], [], [document(names[0], 0, "a.md"), document(names[0], 1, "a.md"), document(names[1], 2, "b.md")]);
  const actual = await replay.rankFrozenCandidates({ observation: input, fusion: "skill-identity-sum", poolLimit: 6 });
  assert.equal(actual.skillHits[0].score, 1 / 61);
  assert.equal(actual.skillHits[1].score, 1 / 63);
});

test("labels cannot influence either fusion strategy and unsupported variants are rejected", async () => {
  const input = observation([document(names[0], 0, "meta.md")]);
  for (const fusion of ["current-max", "skill-identity-sum"]) {
    const left = await replay.rankFrozenCandidates({ observation: input, fusion, poolLimit: 6 });
    const right = await replay.rankFrozenCandidates({ observation: { ...input, expected: "UNUSED_LABEL", ground_truth_skill: names[7] }, fusion, poolLimit: 6 });
    assert.deepEqual(left, right);
  }
  await assert.rejects(replay.rankFrozenCandidates({ observation: input, fusion: "invented", poolLimit: 6 }), /fusion/);
  await assert.rejects(replay.rankFrozenCandidates({ observation: input, fusion: "current-max", poolLimit: 7 }), /poolLimit/);
});
