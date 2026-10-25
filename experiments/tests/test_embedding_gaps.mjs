import test from "node:test";
import assert from "node:assert/strict";
import { validateEmbeddings } from "../scripts/embed_public_gaps.mjs";

test("gap vectors require complete unique response indices and finite nonzero 1536 dimensions", () => {
  const body = { input: ["public-a", "public-b"] };
  const vector = Array(1536).fill(0); vector[0] = 1;
  const good = { data: [{ index: 1, embedding: vector }, { index: 0, embedding: vector }] };
  assert.doesNotThrow(() => validateEmbeddings(good, body));
  for (const data of [good.data.slice(0, 1), [good.data[0], good.data[0]],
    [{ index: 0, embedding: Array(1536).fill(0) }, good.data[0]],
    [{ index: 0, embedding: [1] }, good.data[0]],
    [{ index: 0, embedding: Array(1536).fill(Infinity) }, good.data[0]]]) {
    assert.throws(() => validateEmbeddings({ data }, body));
  }
});
