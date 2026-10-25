import test from "node:test";
import assert from "node:assert/strict";
import { Readable } from "node:stream";
import { readJsonStdin } from "../scripts/json_stdin.mjs";

test("JSON stdin preserves UTF8 characters at every buffer boundary", async () => {
  const expected = { text: "public 中文 — café 🎀", nested: ["來源", "\n"] };
  const bytes = Buffer.from(JSON.stringify(expected));
  for (let boundary = 1; boundary < bytes.length; boundary++) {
    const input = Readable.from([bytes.subarray(0, boundary), bytes.subarray(boundary)]);
    assert.deepEqual(await readJsonStdin(input), expected);
  }
});

test("invalid UTF8 and JSON errors do not echo credential text", async () => {
  for (const chunks of [[Buffer.from('{"key":"synthetic-secret",')],
    [Buffer.from('{"key":"synthetic-secret'), Buffer.from([0xf0]), Buffer.from('"}')]]) {
    await assert.rejects(readJsonStdin(Readable.from(chunks)), (error) => {
      assert.equal(error.message, "Invalid JSON stdin");
      assert.ok(!String(error).includes("synthetic-secret"));
      return true;
    });
  }
});
