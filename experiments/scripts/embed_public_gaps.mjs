/** Fill only preflight-proven public vector gaps through both spending guards.
 * Credentials arrive over stdin and are never saved or printed.
 */
import { createHash } from "node:crypto";
import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createControlledFetch } from "./controlled_model_fetch.mjs";

const root = fileURLToPath(new URL("../../", import.meta.url));
const hash = (value) => createHash("sha256").update(value).digest("hex");

export function validateEmbeddings(payload, body) {
  if (!Array.isArray(payload.data) || payload.data.length !== body.input.length) throw new Error("Embedding count mismatch");
  const indices = new Set();
  for (const row of payload.data) {
    if (!Number.isInteger(row.index) || row.index < 0 || row.index >= body.input.length || indices.has(row.index)) throw new Error("Embedding indices are invalid");
    indices.add(row.index);
    if (!Array.isArray(row.embedding) || row.embedding.length !== 1536 || row.embedding.some((value) => typeof value !== "number" || !Number.isFinite(value)) || !row.embedding.some((value) => value !== 0)) throw new Error("Invalid embedding vector");
  }
}

async function main() {
  let stdin = "";
  for await (const chunk of process.stdin) stdin += chunk;
  const config = JSON.parse(stdin);
  const runDir = path.resolve(config.runDir);
  const relative = path.relative(path.join(root, "experiments/datasets"), runDir);
  if (!relative || relative.startsWith("..") || path.isAbsolute(relative)) throw new Error("Run path is outside the experiment root");
  const requestFile = path.join(runDir, "missing-embedding-inputs.json");
  const raw = await readFile(requestFile, "utf8");
  const manifest = JSON.parse(raw);
  const rows = manifest.entries ?? manifest.inputs;
  if (!Array.isArray(rows) || rows.length < 1 || rows.length > 32) throw new Error("Gap input manifest must contain 1-32 public rows");
  const preflight = JSON.parse(await readFile(path.join(runDir, "qmd-preflight.json"), "utf8"));
  const expected = new Set(preflight.missing_inputs.map((row) => row.input_sha256));
  const actual = new Set(rows.map((row) => row.input_sha256));
  if (actual.size !== expected.size || [...actual].some((item) => !expected.has(item)) || rows.some((row) => typeof row.input !== "string" || hash(row.input) !== row.input_sha256)) throw new Error("Public gap identities differ from preflight");
  const output = path.join(runDir, "public-embedding-supplement.json");
  try {
    const prior = JSON.parse(await readFile(output, "utf8"));
    if (prior.input_manifest_sha256 !== hash(raw)) throw new Error("Existing supplement belongs to a different input manifest");
    console.log(JSON.stringify({ status: "cached-artifact", count: prior.entries.length, new_physical_requests: 0 }));
    return;
  } catch (error) { if (error.code !== "ENOENT") throw error; }
  const controlled = createControlledFetch({ runDir, python: path.join(root, "experiments/.venv/bin/python"), probe: true,
    endpoints: [{ url: config.endpoint, provider: "embedding", model: "text-embedding-3-small", resolvedModel: "text-embedding-3-small", validate: validateEmbeddings }], nativeFetch: globalThis.fetch });
  const response = await controlled(config.endpoint, { method: "POST", headers: { "content-type": "application/json", ...(config.apiKey ? { authorization: `Bearer ${config.apiKey}` } : {}) },
    body: JSON.stringify({ model: "text-embedding-3-small", dimensions: 1536, input: rows.map((row) => row.input) }) });
  if (!response.ok) throw new Error("Embedding provider did not return success");
  const payload = await response.json();
  const byIndex = new Map(payload.data.map((row) => [row.index, row.embedding]));
  await writeFile(output, JSON.stringify({ schema_version: 1, created_at: new Date().toISOString(), model: "text-embedding-3-small", dimension: 1536,
    input_manifest_sha256: hash(raw), physical_transport: controlled.stats, provider_usage: payload.usage,
    entries: rows.map((row, index) => ({ input_sha256: row.input_sha256, input: row.input, vector: byIndex.get(index) })) }) + "\n", { flag: "wx" });
  console.log(JSON.stringify({ status: "complete", count: rows.length, transport: controlled.stats, billed_input_tokens: payload.usage.total_tokens }));
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  main().catch(() => { console.error("Public-gap embedding stopped; credentials and provider details omitted. Inspect the budget ledger before resuming."); process.exitCode = 1; });
}
