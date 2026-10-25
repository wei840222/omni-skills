import test from "node:test";
import assert from "node:assert/strict";
import { mkdtemp, writeFile, readFile, rm } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createControlledFetch } from "../scripts/controlled_model_fetch.mjs";

const root = fileURLToPath(new URL("../..", import.meta.url));
const python = path.join(root, "experiments/.venv/bin/python");
const rule = { url: "https://example.invalid/v1/systemone", provider: "jev", model: "jev-latest", resolvedModel: "jev-1.14.0",
  validate(payload, body) { assert.deepEqual(Object.keys(payload.answers).sort(), Object.keys(body.questions).sort()); } };
const request = { method: "POST", body: JSON.stringify({ model: "jev-latest", state: "public", questions: {} }) };

async function fixture(t, nativeFetch) {
  const dir = await mkdtemp(path.join(os.tmpdir(), "controlled-fetch-"));
  t.after(() => rm(dir, { recursive: true, force: true }));
  const limits = { request_cap: 2, providers: { jev: { requests: 2, tokens: 131072, usd_per_million: "0.042" } } };
  await writeFile(path.join(dir, "budget-limits.json"), JSON.stringify(limits));
  return { dir, fetch: createControlledFetch({ runDir: dir, endpoints: [rule], nativeFetch, python }) };
}

test("exact payload cache reuses result without new spending; auth stays out of ledger", async (t) => {
  let calls = 0;
  const { dir, fetch } = await fixture(t, async () => {
    calls++; return Response.json({ model: "jev-1.14.0", usage: { input_tokens: 12 }, answers: {} });
  });
  await fetch(rule.url, { ...request, headers: { authorization: "Bearer synthetic-secret" } });
  await fetch(rule.url, request);
  assert.equal(calls, 1);
  assert.equal(fetch.stats.cacheHits, 1);
  const log = await readFile(path.join(dir, "model-requests.jsonl"), "utf8");
  assert.ok(!log.includes("synthetic-secret"));
  assert.ok(!log.includes('"public"'));
});

test("unapproved endpoint/model/long context never reaches transport", async (t) => {
  let calls = 0;
  const { fetch } = await fixture(t, async () => { calls++; throw new Error("unreachable"); });
  await assert.rejects(fetch("https://other.invalid", request), /allowlisted/);
  await assert.rejects(fetch(rule.url, { ...request, body: '{"model":"other"}' }), /model change/);
  await assert.rejects(fetch(rule.url, { ...request, headers: { "TypeSafe-Danger-Zone-Long-Context": "true" } }), /Long-context/);
  assert.equal(calls, 0);
});

test("cached billed tokens must match validated response usage before observation", async (t) => {
  let calls = 0;
  const { dir, fetch } = await fixture(t, async () => {
    calls++; return Response.json({ model: "jev-1.14.0", usage: { input_tokens: 1000, total_tokens: 1007 }, answers: {} });
  });
  await fetch(rule.url, request);
  const cachePath = path.join(dir, "model-cache", `${fetch.stats.observations[0].key}.json`);
  const cached = JSON.parse(await readFile(cachePath, "utf8"));
  cached.billedTokens = 1;
  await writeFile(cachePath, JSON.stringify(cached));
  await assert.rejects(fetch(rule.url, request), /cache usage/);
  assert.equal(calls, 1);
  assert.equal(fetch.stats.cacheHits, 0);
  assert.equal(fetch.stats.observations.length, 1);
  cached.billedTokens = 1000;
  delete cached.payload.usage;
  await writeFile(cachePath, JSON.stringify(cached));
  await assert.rejects(fetch(rule.url, request), /cache usage/);
  assert.equal(calls, 1);
});

test("legacy cache derives billed input from payload without inventing service time", async (t) => {
  let calls = 0;
  const { dir, fetch } = await fixture(t, async () => {
    calls++; return Response.json({ model: "jev-1.14.0", usage: { input_tokens: 1000 }, answers: {} });
  });
  await fetch(rule.url, request);
  const cachePath = path.join(dir, "model-cache", `${fetch.stats.observations[0].key}.json`);
  const cached = JSON.parse(await readFile(cachePath, "utf8"));
  delete cached.billedTokens;
  delete cached.originalServiceMs;
  await writeFile(cachePath, JSON.stringify(cached));
  await fetch(rule.url, request);
  assert.equal(fetch.stats.observations[1].billedTokens, 1000);
  assert.equal(fetch.stats.observations[1].originalServiceMs, null);
  assert.equal(calls, 1);
});

test("two unknown failures trip ledger before a third physical attempt", async (t) => {
  let calls = 0;
  const { fetch } = await fixture(t, async () => { calls++; throw new Error("synthetic"); });
  for (let i = 0; i < 2; i++) await assert.rejects(fetch(rule.url, request), /transport failed/);
  await assert.rejects(fetch(rule.url, request), /budget rejected/);
  assert.equal(calls, 2);
});

test("missing billed usage cannot be cached or treated as free", async (t) => {
  const { fetch } = await fixture(t, async () => Response.json({ answers: {} }));
  await assert.rejects(fetch(rule.url, request), /usage is unavailable/);
  assert.equal(fetch.stats.cacheHits, 0);
});

test("Request objects cannot hide long-context headers from validation", async (t) => {
  let calls = 0;
  const { fetch } = await fixture(t, async () => { calls++; return Response.json({ model: "jev-1.14.0", answers: {}, usage: { input_tokens: 1 } }); });
  const original = new Request(rule.url, { method: "POST", headers: { "TypeSafe-Danger-Zone-Long-Context": "true" }, body: request.body });
  await assert.rejects(fetch(original, request), /Request objects/);
  assert.equal(calls, 0);
});

test("resolved model shift is billed but never cached as the frozen alias", async (t) => {
  let calls = 0;
  const { fetch } = await fixture(t, async () => { calls++; return Response.json({ model: "jev-1.15.0", answers: {}, usage: { input_tokens: 1 } }); });
  await assert.rejects(fetch(rule.url, request), /model identity/);
  await assert.rejects(fetch(rule.url, request), /model identity/);
  assert.equal(calls, 2);
  assert.equal(fetch.stats.cacheHits, 0);
});

test("misaligned paid answers are failures and cannot poison the cache", async (t) => {
  let calls = 0;
  const { fetch } = await fixture(t, async () => { calls++; return Response.json({ model: "jev-1.14.0", answers: { wrong: {} }, usage: { input_tokens: 1 } }); });
  await assert.rejects(fetch(rule.url, request), /consumer validation/);
  await assert.rejects(fetch(rule.url, request), /consumer validation/);
  await assert.rejects(fetch(rule.url, request), /budget rejected/);
  assert.equal(calls, 2);
  assert.equal(fetch.stats.cacheHits, 0);
});

test("probe cap blocks transport while global reservations remain conservative", async (t) => {
  const { dir } = await fixture(t, async () => {});
  await writeFile(path.join(dir, "probe-budget-limits.json"), JSON.stringify({ request_cap: 1, providers: { jev: { requests: 1, tokens: 65536, usd_per_million: "0.042" } } }));
  let calls = 0;
  const fetch = createControlledFetch({ runDir: dir, endpoints: [rule], python, probe: true,
    nativeFetch: async () => { calls++; return Response.json({ model: "jev-1.14.0", answers: {}, usage: { input_tokens: 1 } }); } });
  await fetch(rule.url, request);
  await assert.rejects(fetch(rule.url, { ...request, body: JSON.stringify({ ...JSON.parse(request.body), state: "different" }) }), /budget rejected/);
  assert.equal(calls, 1);
});

test("documented expansion output bound reserves tokens without changing production wire payload", async (t) => {
  const { dir } = await fixture(t, async () => {});
  await writeFile(path.join(dir, "budget-limits.json"), JSON.stringify({ request_cap: 1, providers: { expansion: { requests: 1, tokens: 100000, usd_per_million: null } } }));
  const expansion = { url: "https://example.invalid/v1/chat/completions", provider: "expansion", model: "gemini-3.5-flash-lite", resolvedModel: "gemini-3.5-flash-lite",
    maxOutputTokens: 65536, outputBoundSource: "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite", validate() {} };
  const original = JSON.stringify({ model: expansion.model, messages: [{ role: "user", content: "public" }], temperature: 0.3 });
  let calls = 0;
  const fetch = createControlledFetch({ runDir: dir, endpoints: [expansion], python, nativeFetch: async (url, init) => {
    assert.equal(init.body, original); calls++;
    return Response.json({ model: expansion.resolvedModel, choices: [], usage: { total_tokens: 12 } });
  } });
  await fetch(expansion.url, { method: "POST", body: original });
  assert.equal(calls, 1);
});

test("cached selectors retain the original service observation rather than cache read time", async (t) => {
  const { fetch } = await fixture(t, async () => {
    await new Promise((resolve) => setTimeout(resolve, 5));
    return Response.json({ model: "jev-1.14.0", answers: {}, usage: { input_tokens: 12 } });
  });
  const first = await fetch(rule.url, request);
  const second = await fetch(rule.url, request);
  assert.equal(first.headers.get("x-omni-observation-source"), "remote");
  assert.equal(second.headers.get("x-omni-observation-source"), "cache");
  assert.ok(Number(first.headers.get("x-omni-original-service-ms")) > 0);
  assert.equal(first.headers.get("x-omni-original-service-ms"), second.headers.get("x-omni-original-service-ms"));
  assert.equal(fetch.stats.observations.length, 2);
  assert.equal(fetch.stats.observations[1].billedTokens, 12);
});
