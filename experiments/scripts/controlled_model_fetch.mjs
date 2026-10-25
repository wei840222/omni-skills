/** All physical model attempts reserve the shared ledger before native fetch.
 * Cache keys include endpoint, model and exact payload; auth never enters logs.
 */
import { createHash } from "node:crypto";
import { mkdir, readFile, writeFile, appendFile } from "node:fs/promises";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const scriptRoot = path.dirname(fileURLToPath(import.meta.url));
const sha = (value) => createHash("sha256").update(value).digest("hex");

export function createControlledFetch({ runDir, endpoints, nativeFetch, python, probe = false }) {
  if (typeof nativeFetch !== "function") throw new Error("Explicit transport is required");
  if (endpoints.some((rule) => !rule.resolvedModel || typeof rule.validate !== "function")) {
    throw new Error("Every endpoint requires a frozen resolved model and consumer response validator");
  }
  const stats = { physicalAttempts: 0, cacheHits: 0, observations: [] };
  const billedUsage = (payload, provider) => provider === "jev" ? payload.usage?.input_tokens
    : payload.usage?.total_tokens ?? ((payload.usage?.prompt_tokens ?? NaN) + (payload.usage?.completion_tokens ?? 0));
  const observedResponse = (payload, observation) => {
    stats.observations.push(observation);
    const headers = { "content-type": "application/json", "x-omni-observation-source": observation.source };
    if (Number.isFinite(observation.originalServiceMs)) headers["x-omni-original-service-ms"] = String(observation.originalServiceMs);
    return new Response(JSON.stringify(payload), { status: 200, headers });
  };
  const command = (ledger, limits, args) => {
    const result = spawnSync(python, [path.join(scriptRoot, "model_budget.py"),
      "--ledger", path.join(runDir, ledger), "--limits", path.join(runDir, limits), ...args],
    { encoding: "utf8", timeout: 30000, maxBuffer: 1_000_000 });
    if (result.status !== 0) throw new Error("Model budget rejected operation; no automatic reset or retry");
    return JSON.parse(result.stdout);
  };
  const ledgers = [["model-budget.sqlite", "budget-limits.json"],
    ...(probe ? [["probe-budget.sqlite", "probe-budget-limits.json"]] : [])];
  const transport = async (input, init = {}) => {
    if (input instanceof Request || !(typeof input === "string" || input instanceof URL)) {
      throw new Error("Request objects are not accepted; pass an explicit URL and complete init");
    }
    const url = String(input);
    const rule = endpoints.find((entry) => entry.url === url);
    if (!rule || (init.method ?? "GET") !== "POST") throw new Error("Model endpoint/method is not allowlisted");
    if (typeof init.body !== "string" || Buffer.byteLength(init.body) > 1_048_576) throw new Error("Model payload must be bounded JSON text");
    const body = JSON.parse(init.body);
    if (body.model !== rule.model) throw new Error("Unapproved model change");
    if (rule.provider === "embedding" && body.dimensions !== 1536) throw new Error("Embedding dimension must remain 1536");
    const headers = new Headers(init.headers);
    if (headers.has("TypeSafe-Danger-Zone-Long-Context")) throw new Error("Long-context billing is not enabled for this run");
    let outputBound = 0;
    if (rule.provider === "expansion") {
      outputBound = body.max_tokens ?? rule.maxOutputTokens;
      if (!Number.isSafeInteger(rule.maxOutputTokens) || rule.maxOutputTokens < 1 || !Number.isSafeInteger(outputBound) || outputBound < 1 || !rule.outputBoundSource || outputBound > rule.maxOutputTokens) {
        throw new Error("Expansion needs a documented output token bound before paid execution");
      }
    }
    const upper = rule.provider === "jev" ? 65536 : Buffer.byteLength(init.body) + 4096 + outputBound;
    const key = sha(JSON.stringify(["controlled-fetch-v2", url, rule.resolvedModel, body]));
    const cachePath = path.join(runDir, "model-cache", `${key}.json`);
    try {
      const cached = JSON.parse(await readFile(cachePath, "utf8"));
      if (cached.key !== key || cached.model !== rule.model || cached.payload.model !== rule.resolvedModel) throw new Error("Corrupt model cache identity");
      await rule.validate(cached.payload, body);
      const billed = billedUsage(cached.payload, rule.provider);
      if (!Number.isSafeInteger(billed) || billed < 0 || (cached.billedTokens !== undefined && cached.billedTokens !== billed)) {
        throw new Error("Corrupt model cache usage; no automatic refetch");
      }
      stats.cacheHits++;
      return observedResponse(cached.payload, { key, provider: rule.provider, source: "cache",
        originalServiceMs: cached.originalServiceMs ?? null, billedTokens: billed });
    } catch (error) {
      if (error.code !== "ENOENT") throw error;
    }
    const reservations = [];
    for (const [ledger, limits] of ledgers) {
      const { id } = command(ledger, limits, ["reserve", "--provider", rule.provider, "--fingerprint", key, "--tokens", String(upper)]);
      reservations.push({ ledger, limits, id });
    }
    const settle = (tokens, status) => {
      for (const { ledger, limits, id } of reservations) command(ledger, limits,
        ["settle", "--id", id, "--status", status, ...(Number.isInteger(tokens) ? ["--tokens", String(tokens)] : [])]);
    };
    const started = performance.now();
    let response;
    stats.physicalAttempts++;
    try {
      response = await nativeFetch(url, { ...init, headers, redirect: "error" });
    } catch {
      settle(undefined, "transport-error");
      throw new Error("Controlled model transport failed; details omitted");
    }
    if (!response.ok) {
      await response.body?.cancel();
      settle(undefined, "http-error");
      return new Response("", { status: response.status });
    }
    let payload;
    try { payload = await response.json(); } catch {
      settle(undefined, "invalid-response");
      throw new Error("Model returned invalid JSON");
    }
    // Network plus response-body/JSON time, excluding ledger settlement and
    // cache I/O. Replaying a response must retain this original observation.
    const originalServiceMs = performance.now() - started;
    const billed = billedUsage(payload, rule.provider);
    if (!Number.isSafeInteger(billed) || billed < 0) {
      settle(undefined, "usage-unavailable");
      throw new Error("Model usage is unavailable; reservation retained and result not cached");
    }
    if (payload.model !== rule.resolvedModel) {
      settle(billed, "model-identity-mismatch");
      throw new Error("Model response differs from frozen resolved model identity");
    }
    try { await rule.validate(payload, body); } catch {
      settle(billed, "invalid-response");
      throw new Error("Model response failed consumer validation; result not cached");
    }
    settle(billed, "completed");
    await mkdir(path.dirname(cachePath), { recursive: true });
    await writeFile(cachePath, JSON.stringify({ key, model: rule.model, payload, originalServiceMs, billedTokens: billed }), { flag: "wx" });
    await appendFile(path.join(runDir, "model-requests.jsonl"), JSON.stringify({
      provider: rule.provider, requestedModel: rule.model, observedModel: payload.model ?? null,
      key, billedTokens: billed, originalServiceMs, durationMs: performance.now() - started,
    }) + "\n");
    return observedResponse(payload, { key, provider: rule.provider, source: "remote", originalServiceMs, billedTokens: billed });
  };
  transport.stats = stats;
  return transport;
}
