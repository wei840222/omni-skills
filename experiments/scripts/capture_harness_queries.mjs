/** Run public retrieval and host Decision with explicit, budgeted transports.
 * Settings/credentials arrive on stdin. Raw results contain public data only.
 */
import { readFile, writeFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { createHash } from "node:crypto";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createHarnessRetrievalAdapter } from "./harness_retrieval_adapter.mjs";
import { createHostDecisionAdapter } from "./host_decision_adapter.mjs";
import { createControlledFetch } from "./controlled_model_fetch.mjs";
import { validateEmbeddings } from "./embed_public_gaps.mjs";

const root = fileURLToPath(new URL("../../", import.meta.url));
const sha = (value) => createHash("sha256").update(value).digest("hex");

async function main() {
  const nativeFetch = globalThis.fetch;
  let stdin = "";
  for await (const part of process.stdin) stdin += part;
  const settings = JSON.parse(stdin);
  const runDir = path.resolve(settings.runDir);
  const relative = path.relative(path.join(root, "experiments/datasets"), runDir);
  if (!relative || relative.startsWith("..") || path.isAbsolute(relative)) throw new Error("Invalid run directory");
  const hostProbes = JSON.parse(await readFile(path.join(runDir, "m0-host-probes.json"), "utf8"));
  if (hostProbes.status !== "complete" || hostProbes.inputs.length !== 5) throw new Error("Five completed public host probes are required");
  const artifactPath = path.join(runDir, "m0-query-probes.json");
  const identity = sha(JSON.stringify({ inputs: hostProbes.inputs, policy: settings.policy, models: settings.models }));
  try {
    const old = JSON.parse(await readFile(artifactPath, "utf8"));
    if (old.status === "complete" && old.input_sha256 === identity) {
      console.log(JSON.stringify({ status: "cached-artifact", cases: old.results.length })); return;
    }
    throw new Error("An unfinished/different query capture exists; inspect it before resuming");
  } catch (error) { if (error.code !== "ENOENT") throw error; }
  const artifact = { schema_version: 1, status: "running", input_sha256: identity, results: [],
    scope: "Public 963 corpus, actual managed retrieval and host Decision; controlled experience/graph fixtures; not resident Gateway or a quality evaluation." };
  await writeFile(artifactPath, JSON.stringify(artifact, null, 2) + "\n", { flag: "wx" });
  const harnessRoot = path.join(process.env.HOME, ".openclaw/extensions/skill-harness");
  const typeSafeRoot = path.join(process.env.HOME, ".openclaw/extensions/typesafe");
  globalThis.fetch = async () => { throw new Error("Query imports have no transport authority"); };
  const { resolveConfig } = await import(pathToFileURL(path.join(harnessRoot, "dist/src/config.js")).href);
  const { parseInput, parseResult } = await import(pathToFileURL(path.join(typeSafeRoot, "dist/src/schema.js")).href);
  const logical = "https://qmd-reuse.invalid/v1";
  const endpoint = (model) => ({ model, baseUrl: logical, apiKey: "offline-controlled-transport-placeholder" });
  const resolvedConfig = resolveConfig({ qmd: { timeoutMs: settings.policy.qmdTimeoutMs,
    embedding: { ...endpoint("text-embedding-3-small"), dimension: 1536 },
    expansion: endpoint(settings.models.expansion), jev: endpoint(settings.models.jev) },
    skills: { search: { collectionWeights: settings.policy.collectionWeights } }, routing: settings.policy.routing },
  { env: {}, openClawConfig: {} });
  const rules = [
    { url: settings.endpoints.embedding.url, provider: "embedding", model: "text-embedding-3-small", resolvedModel: "text-embedding-3-small", validate: validateEmbeddings },
    { url: settings.endpoints.jev.url, provider: "jev", model: settings.models.jev, resolvedModel: settings.models.jevResolved, validate: (payload, body) => parseResult(payload, parseInput(body)) },
    { url: settings.endpoints.expansion.url, provider: "expansion", model: settings.models.expansion, resolvedModel: settings.models.expansionResolved,
      maxOutputTokens: 65536, outputBoundSource: "https://ai.google.dev/gemini-api/docs/models/gemini-3.5-flash-lite",
      validate: (payload) => { if (!Array.isArray(payload.choices) || typeof payload.choices[0]?.message?.content !== "string") throw new Error("Invalid expansion response"); } },
  ];
  const transport = createControlledFetch({ runDir, endpoints: rules, nativeFetch, python: path.join(root, "experiments/.venv/bin/python"), probe: true });
  const logicalRoutes = new Map([
    [`${logical}/embeddings`, settings.endpoints.embedding],
    [`${logical}/chat/completions`, settings.endpoints.expansion],
    [`${logical}/systemone`, settings.endpoints.jev],
  ]);
  const mappedFetch = (url, init) => {
    const destination = logicalRoutes.get(String(url));
    if (!destination) throw new Error("Unexpected logical model endpoint");
    const headers = new Headers(init.headers);
    headers.delete("authorization");
    if (destination.apiKey) headers.set("authorization", `Bearer ${destination.apiKey}`);
    return transport(destination.url, { ...init, headers });
  };
  let retrieval, decision;
  try {
    retrieval = await createHarnessRetrievalAdapter({ root, profileDir: path.join(runDir, "qmd-public"), dataRoot: path.join(runDir, "replay-runtime"), resolvedConfig,
      fetchImpl: mappedFetch, offline: false });
    const decisionRoot = path.join(runDir, "m0-integrated-host-runtime");
    await mkdir(decisionRoot, { recursive: true });
    decision = await createHostDecisionAdapter({ fixtureRoot: decisionRoot, model: settings.models.jev, offline: false,
      providerConfig: { apiBaseUrl: settings.endpoints.jev.url.replace(/\/systemone$/, ""), apiKey: settings.endpoints.jev.apiKey, timeoutMs: 30000 }, fetchImpl: transport });
    for (const probe of hostProbes.inputs) {
      const source = probe.metadata;
      const graph = new Map();
      for (const relation of source.relationEvidence ?? []) {
        const edges = graph.get(relation.from) ?? [];
        edges.push({ name: relation.to, direction: "current-to-related", relation_type: relation.relation_type, reason: relation.reason });
        graph.set(relation.from, edges);
      }
      const observation = await retrieval.retrieve({ query: source.latest, conversation: source.conversation,
        controlledExperiences: source.candidateExperiences ?? [], controlledGraph: graph });
      if (observation.status !== "completed") throw new Error("Managed retrieval did not complete");
      const selected = await decision.evaluateSelection({ latest: source.latest, conversation: source.conversation,
        candidateSkills: observation.candidateSkills, candidateSources: observation.candidateSources,
        candidateExperiences: source.candidateExperiences ?? [], relationEvidence: observation.relationEvidence },
      { timeoutMs: resolvedConfig.routing.timeoutMs, routing: resolvedConfig.routing });
      const empty = !observation.candidateSkills.length && !(source.candidateExperiences ?? []).length;
      if (!empty && selected.outcome?.status !== "ok") throw new Error("Host selection did not complete");
      artifact.results.push({ id: probe.id, observation, selection: selected.selection ?? null, outcome: selected.outcome ?? null, trace: selected.trace });
      await writeFile(artifactPath, JSON.stringify(artifact, null, 2) + "\n");
    }
    artifact.raw_hitlists = retrieval.rawHitlistManifest();
    artifact.transport = transport.stats;
    artifact.status = "complete";
    await writeFile(artifactPath, JSON.stringify(artifact, null, 2) + "\n");
    console.log(JSON.stringify({ status: artifact.status, cases: artifact.results.length, transport: transport.stats }));
  } catch {
    artifact.status = "failed"; artifact.failure = "integration-or-budget-failure"; artifact.transport = transport.stats;
    if (retrieval) artifact.raw_hitlists = retrieval.rawHitlistManifest();
    await writeFile(artifactPath, JSON.stringify(artifact, null, 2) + "\n");
    throw new Error("Public query capture stopped; inspect artifacts and ledger before resuming");
  } finally { await retrieval?.close(); await decision?.close(); }
}

main().catch(() => { console.error("Public query capture stopped; credentials and provider details omitted."); process.exitCode = 1; });
