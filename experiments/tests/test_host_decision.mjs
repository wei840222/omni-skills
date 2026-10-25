import assert from "node:assert/strict";
import { mkdtemp, mkdir, readFile, readdir, writeFile } from "node:fs/promises";
import { spawnSync } from "node:child_process";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";
import { createHostDecisionAdapter } from "../scripts/host_decision_adapter.mjs";
import { createControlledFetch } from "../scripts/controlled_model_fetch.mjs";

const workspace = fileURLToPath(new URL("../../", import.meta.url));
const fixtureParent = path.join(workspace, "experiments/datasets/host-decision-smoke");
await mkdir(fixtureParent, { recursive: true });
const fixtureRoot = await mkdtemp(path.join(fixtureParent, "run-"));
let callback = () => { throw new Error("No replay configured"); };
const adapter = await createHostDecisionAdapter({
  fixtureRoot,
  providerConfig: { apiBaseUrl: "http://127.0.0.1:9/v1", timeoutMs: 1000 },
  model: "jev-latest",
  fetchImpl: (...args) => callback(...args),
});

const candidates = (latest) => ({
  latest,
  candidateSkills: [
    { name: "synthetic-alpha", description: "Synthetic relevant capability." },
    { name: "synthetic-beta", description: "Synthetic unrelated capability." },
  ],
  candidateExperiences: [{ id: "synthetic-note", summary: "Synthetic reference.", skills: ["synthetic-alpha"] }],
});
const respond = (body, probabilities = [0.9, 0.1, 0.8]) => Response.json({
  model: body.model,
  answers: Object.fromEntries(Object.keys(body.questions).reverse().map((id) => [
    id, { type: "noul", noul: probabilities[Object.keys(body.questions).indexOf(id)] },
  ])),
  usage: { input_tokens: 12, output_tokens: 6 },
});

test("full host facade replays five synthetic cases with exact Boolean/noul alignment", async () => {
  for (const latest of ["Write a synthetic test", "Inspect a synthetic table", "Explain a synthetic diagram", "Plan a synthetic trip", "Edit a synthetic paragraph"]) {
    callback = async (url, init) => {
      assert.equal(String(url), "http://127.0.0.1:9/v1/systemone");
      assert.equal(init.method, "POST");
      assert.equal(new Headers(init.headers).has("authorization"), false);
      const body = JSON.parse(init.body);
      assert.equal(body.model, "jev-latest");
      assert.equal(body.state.latest_message, latest);
      assert.deepEqual(Object.values(body.questions).map((q) => q.type), ["noul", "noul", "noul"]);
      return respond(body);
    };
    const result = await adapter.evaluateSelection(candidates(latest));
    assert.deepEqual(result.selection.skills, ["synthetic-alpha"]);
    assert.deepEqual(result.selection.experiences, ["synthetic-note"]);
    assert.equal(result.outcome.status, "ok");
    assert.equal(result.outcome.result.answers["skill_synthetic-alpha"].probabilityTrue, 0.9);
    assert.deepEqual(result.outcome.result.usage, { inputTokens: 12, outputTokens: 6 });
    assert.equal(result.trace.fetchCalls, 1);
    assert.equal(result.trace.legacyCalls, 0);
    assert.equal(result.trace.hostCalls, 1);
    assert.deepEqual(result.trace.hostOptionKeys, ["agentId", "purpose", "rubricVersion", "signal", "timeoutMs"]);
  }
});

test("wire validator uses installed TypeSafe schema and rejects unknown fields", async () => {
  const body = { model: "jev-latest", state: {}, questions: { relevant: { type: "noul" } } };
  const payload = await respond(body, [0.9]).json();
  assert.equal(adapter.validateWireResponse(payload, body), payload);
  assert.throws(() => adapter.validateWireResponse({ ...payload, unknown: true }, body));
  assert.throws(() => adapter.validateWireResponse(payload, { ...body, unknown: true }));
  assert.throws(() => adapter.validateWireResponse({ ...payload, answers: { wrong: { type: "noul", noul: 0.9 } } }, body));
});

test("host facade, controlled transport and both ledgers agree on validated caching and billed usage", async () => {
  const runDir = path.join(fixtureRoot, "controlled-budget");
  await mkdir(runDir);
  const limits = { request_cap: 2, providers: { jev: { requests: 2, tokens: 131072, usd_per_million: "0.042" } } };
  for (const filename of ["budget-limits.json", "probe-budget-limits.json"]) {
    await writeFile(path.join(runDir, filename), JSON.stringify(limits), { flag: "wx" });
  }
  const python = path.join(workspace, "experiments/.venv/bin/python");
  const summary = (ledger, limitFile) => {
    const process = spawnSync(python, [path.join(workspace, "experiments/scripts/model_budget.py"),
      "--ledger", path.join(runDir, ledger), "--limits", path.join(runDir, limitFile), "summary"], { encoding: "utf8" });
    assert.equal(process.status, 0);
    return JSON.parse(process.stdout).jev;
  };
  let wrongAnswers = false;
  let nativeCalls = 0;
  const controlled = createControlledFetch({
    runDir, python, probe: true,
    endpoints: [{
      url: "http://127.0.0.1:9/v1/systemone", provider: "jev", model: "jev-latest", resolvedModel: "jev-1.14.0",
      validate: (payload, body) => adapter.validateWireResponse(payload, body),
    }],
    nativeFetch: async (_url, init) => {
      nativeCalls++;
      const payload = await respond(JSON.parse(init.body)).json();
      payload.model = "jev-1.14.0";
      payload.usage = { input_tokens: wrongAnswers ? 23 : 321, output_tokens: 7 };
      if (wrongAnswers) {
        payload.answers.wrong = payload.answers["skill_synthetic-alpha"];
        delete payload.answers["skill_synthetic-alpha"];
      }
      return Response.json(payload);
    },
  });
  callback = controlled;
  const params = candidates("Synthetic ledger integration");
  const first = await adapter.evaluateSelection(params);
  assert.equal(first.outcome.status, "ok");
  assert.equal(first.outcome.result.model, "jev-1.14.0");
  assert.deepEqual(first.selection.skills, ["synthetic-alpha"]);
  assert.deepEqual(first.selection.experiences, ["synthetic-note"]);
  assert.deepEqual(first.outcome.result.usage, { inputTokens: 321, outputTokens: 7 });
  const repeated = await adapter.evaluateSelection(params);
  assert.deepEqual(repeated.selection, first.selection);
  assert.deepEqual(controlled.stats, { physicalAttempts: 1, cacheHits: 1 });
  assert.equal(nativeCalls, 1);
  for (const [ledger, limitFile] of [["model-budget.sqlite", "budget-limits.json"], ["probe-budget.sqlite", "probe-budget-limits.json"]]) {
    const result = summary(ledger, limitFile);
    assert.equal(result.attempts, 1);
    assert.equal(result.observed_billed_tokens, 321);
    assert.equal(result.reserved_or_billed_tokens, 321);
    assert.equal(result.unknown_usage_attempts, 0);
  }
  wrongAnswers = true;
  const invalid = await adapter.evaluateSelection(candidates("Synthetic rejected cache entry"));
  assert.equal(invalid.selection, undefined);
  assert.equal(invalid.outcome.status, "unavailable");
  assert.equal(invalid.trace.fetchCalls, 1);
  assert.equal(invalid.trace.legacyCalls, 0);
  assert.equal(nativeCalls, 2);
  assert.deepEqual(controlled.stats, { physicalAttempts: 2, cacheHits: 1 });
  assert.equal((await readdir(path.join(runDir, "model-cache"))).length, 1);
  for (const [ledger, limitFile] of [["model-budget.sqlite", "budget-limits.json"], ["probe-budget.sqlite", "probe-budget-limits.json"]]) {
    const result = summary(ledger, limitFile);
    assert.equal(result.attempts, 2);
    assert.equal(result.observed_billed_tokens, 344);
    assert.equal(result.unknown_usage_attempts, 0);
  }
  // A rejected response must neither overwrite nor poison an existing valid cache.
  const validAgain = await adapter.evaluateSelection(params);
  assert.deepEqual(validAgain.selection, first.selection);
  assert.equal(nativeCalls, 2);
  assert.deepEqual(controlled.stats, { physicalAttempts: 2, cacheHits: 2 });
  assert.deepEqual(adapter.provenance.network, { socketAttempts: 0, dnsAttempts: 0 });
});

test("empty candidate pool skips host and fetch", async () => {
  const result = await adapter.evaluateSelection({ latest: "Synthetic empty pool" });
  assert.equal(result.skipped, "empty-pool");
  assert.equal(result.trace.hostCalls, 0);
  assert.equal(result.trace.fetchCalls, 0);
});

test("misaligned answer IDs are rejected without retry or fallback", async () => {
  callback = async (_url, init) => {
    const response = await respond(JSON.parse(init.body)).json();
    response.answers.unexpected = response.answers["skill_synthetic-alpha"];
    delete response.answers["skill_synthetic-alpha"];
    return Response.json(response);
  };
  const result = await adapter.evaluateSelection(candidates("Synthetic bad alignment"));
  assert.equal(result.selection, undefined);
  assert.equal(result.outcome.status, "unavailable");
  assert.equal(result.trace.fetchCalls, 1);
  assert.equal(result.trace.legacyCalls, 0);
});

test("HTTP rate limit fails closed without retry or plugin fallback", async () => {
  callback = async () => new Response("unconsumed synthetic error", { status: 429 });
  const result = await adapter.evaluateSelection(candidates("Synthetic HTTP error"));
  assert.equal(result.selection, undefined);
  assert.equal(result.outcome.reason, "rate-limited");
  assert.equal(result.trace.fetchCalls, 1);
  assert.equal(result.trace.legacyCalls, 0);
});

test("unsupported input never reaches transport", async () => {
  const result = await adapter.evaluateSelection(candidates("Synthetic invalid state"), {
    batch: { state: { invalid: Number.NaN }, questions: { bad: { type: "boolean" } } },
  });
  assert.equal(result.selection, undefined);
  assert.equal(result.trace.hostCalls, 0);
  assert.equal(result.trace.fetchCalls, 0);
  assert.equal(result.trace.legacyCalls, 0);
});

test("host contract rejects unsupported question types before provider dispatch", async () => {
  const result = await adapter.evaluateSelection(candidates("Synthetic host contract"), {
    batch: { state: {}, questions: { unsupported: { type: "unknown" } } },
  });
  assert.equal(result.selection, undefined);
  assert.equal(result.outcome, undefined);
  assert.ok(result.diagnostics.some(({ message }) => message.includes("operation-failed")));
  assert.equal(result.trace.hostCalls, 1);
  assert.equal(result.trace.fetchCalls, 0);
  assert.equal(result.trace.legacyCalls, 0);
});

test("host deadline aborts and drains the accepted fetch", async () => {
  let settled = false;
  callback = (_url, init) => new Promise((_resolve, reject) => {
    const abort = () => { settled = true; reject(init.signal.reason); };
    if (init.signal.aborted) abort();
    else init.signal.addEventListener("abort", abort, { once: true });
  });
  const result = await adapter.evaluateSelection(candidates("Synthetic deadline"), { timeoutMs: 100 });
  assert.equal(result.selection, undefined);
  assert.equal(result.outcome.reason, "deadline");
  assert.equal(settled, true);
  assert.equal(result.trace.fetchCalls, 1);
  assert.equal(result.trace.legacyCalls, 0);
});

test("caller cancellation is propagated and drains transport", async () => {
  const controller = new AbortController();
  let accepted = 0;
  let settled = false;
  callback = (_url, init) => new Promise((_resolve, reject) => {
    accepted++;
    init.signal.addEventListener("abort", () => { settled = true; reject(init.signal.reason); }, { once: true });
    controller.abort(new Error("Synthetic caller cancellation"));
  });
  await assert.rejects(adapter.evaluateSelection(candidates("Synthetic cancellation"), { signal: controller.signal }), /Synthetic caller cancellation/);
  assert.equal(accepted, 1);
  assert.equal(settled, true);
});

test("provider absence stays unavailable with no transport or fallback", async () => {
  const result = await adapter.evaluateSelection(candidates("Synthetic no provider"), { providerAvailable: false });
  assert.equal(result.selection, undefined);
  assert.equal(result.outcome.reason, "not-configured");
  assert.equal(result.trace.fetchCalls, 0);
  assert.equal(result.trace.legacyCalls, 0);
});

test("global fetch is blocked outside a controlled evaluation", async () => {
  await assert.rejects(fetch("http://127.0.0.1:9/unexpected"), /controlled host decision/);
});

test("provenance pins source and isolates config/state/log destinations", async () => {
  assert.equal(adapter.provenance.mode, "host-public-facade");
  assert.equal(adapter.provenance.runtimeVersions.openclaw, "2026.10.7");
  assert.equal(adapter.provenance.defaults.routing.timeoutMs, 5000);
  assert.deepEqual(adapter.provenance.network, { socketAttempts: 0, dnsAttempts: 0 });
  assert.ok(adapter.provenance.sources.length >= 10);
  for (const source of adapter.provenance.sources) assert.match(source.sha256, /^[a-f0-9]{64}$/);
  for (const value of Object.values(adapter.provenance.isolation)) assert.ok(value.startsWith(fixtureRoot + path.sep));
  const config = JSON.parse(await readFile(adapter.provenance.isolation.configPath, "utf8"));
  assert.equal(config.logging.level, "silent");
  assert.equal(JSON.stringify(config).includes("apiKey"), false);
  assert.deepEqual((await readdir(fixtureRoot)).sort(), ["controlled-budget", "openclaw.json", "state"]);
  console.log(JSON.stringify({ smoke: "host-decision-M0", replayedSyntheticCases: 5, fixtureRoot, provenance: adapter.provenance }));
});

test.after(async () => { await adapter.close(); });
