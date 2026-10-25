/** Controlled M0 host-core probe. Supply explicit public fixtures and credentials
 * as one JSON document on stdin. Never put credentials in command arguments.
 */
import { createHash } from "node:crypto";
import { lstat, mkdir, readFile, realpath, rename, writeFile } from "node:fs/promises";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createHostDecisionAdapter } from "./host_decision_adapter.mjs";
import { createControlledFetch } from "./controlled_model_fetch.mjs";

const workspace = fileURLToPath(new URL("../../", import.meta.url));
const fixtureKind = "controlled candidate/experience/relation fixtures";
const sha = (value) => createHash("sha256").update(value).digest("hex");
const record = (value) => value && typeof value === "object" && !Array.isArray(value);
const fail = () => { throw new Error("M0 host probe validation failed"); };
const inside = (root, filename) => {
  const relative = path.relative(root, filename);
  return relative !== "" && !relative.startsWith("..") && !path.isAbsolute(relative);
};
const text = (value, max = 16000) => {
  if (typeof value !== "string" || !value.trim() || value.length > max) fail();
  return value;
};
const list = (value, max = 256) => {
  if (!Array.isArray(value) || value.length > max) fail();
  return value;
};
const strings = (value) => list(value).map((entry) => text(entry, 256));
const finite = (value, min, max, integer = false) => {
  if (!Number.isFinite(value) || value < min || value > max || integer && !Number.isInteger(value)) fail();
  return value;
};

function relation(value, related = false) {
  if (!record(value)) fail();
  const result = Object.fromEntries((related
    ? ["name", "from", "relation_type", "reason"]
    : ["skill", "from", "to", "from_description", "to_description", "relation_type", "reason"]
  ).map((key) => [key, text(value[key])]));
  if (!["related", "depends_on", "composes_with", "similar_to", "conflicts_with", "specializes"].includes(result.relation_type)) fail();
  if (value.verification_status !== undefined && value.verification_status !== "unverified") fail();
  return { ...result, verification_status: "unverified" };
}

function publicProbe(raw) {
  if (!record(raw) || !/^[a-zA-Z0-9_.-]{1,80}$/.test(raw.id ?? "")) fail();
  // Project every nested object: expected/labels and other supervision fields
  // have no route into either the host request or its persisted public artifact.
  const params = {
    latest: text(raw.latest, 100000),
    candidateSkills: list(raw.candidateSkills ?? []).map((skill) => ({
      name: text(skill.name, 256), description: text(skill.description),
    })),
    candidateExperiences: list(raw.candidateExperiences ?? []).map((entry) => ({
      id: text(entry.id, 256), summary: text(entry.summary), skills: strings(entry.skills ?? []),
    })),
    relationEvidence: list(raw.relationEvidence ?? []).map((entry) => relation(entry)),
    relatedEvidence: list(raw.relatedEvidence ?? []).map((entry) => relation(entry, true)),
  };
  if (raw.conversation !== undefined) params.conversation = list(raw.conversation, 20).map((turn) => {
    if (!["user", "assistant"].includes(turn.role)) fail();
    return { role: turn.role, text: text(turn.text, 20000) };
  });
  if (raw.visibleSkillNames !== undefined) params.visibleSkillNames = strings(raw.visibleSkillNames);
  for (const [entries, key] of [[params.candidateSkills, "name"], [params.candidateExperiences, "id"]]) {
    if (new Set(entries.map((entry) => entry[key])).size !== entries.length) fail();
  }
  const questions = params.candidateSkills.length + params.candidateExperiences.length + params.relationEvidence.length;
  if (questions < 1 || questions > 256 || Buffer.byteLength(JSON.stringify(params)) > 900000) fail();
  return { id: raw.id, params, inputSha256: sha(JSON.stringify(params)) };
}

function routingProfile(raw = {}) {
  if (!record(raw)) fail();
  const skills = raw.skills ?? {};
  const experiences = raw.experiences ?? {};
  if (!record(skills) || !record(experiences)) fail();
  return {
    timeoutMs: finite(raw.timeoutMs ?? 8000, 1000, 30000, true),
    skills: {
      maxInjectedSkills: finite(skills.maxInjectedSkills ?? 6, 0, 8, true),
      relevanceThreshold: finite(skills.relevanceThreshold ?? 0.4, 0, 1),
    },
    experiences: {
      maxInjectedExperiences: finite(experiences.maxInjectedExperiences ?? 4, 0, 4, true),
      relevanceThreshold: finite(experiences.relevanceThreshold ?? 0.4, 0, 1),
    },
  };
}

function provider(raw) {
  if (!record(raw)) fail();
  const base = text(raw.apiBaseUrl, 2048);
  if (/\s|\\/.test(base)) fail();
  const url = new URL(base);
  if (!["https:", "http:"].includes(url.protocol) || url.username || url.password || url.search || url.hash) fail();
  if (url.protocol !== "https:" && !["localhost", "127.0.0.1", "[::1]"].includes(url.hostname)) fail();
  url.pathname = url.pathname.replace(/\/+$/, "") || "/v1";
  const apiBaseUrl = url.toString().replace(/\/+$/, "");
  const timeoutMs = finite(raw.timeoutMs ?? 30000, 1000, 60000, true);
  const apiKey = raw.apiKey === undefined ? undefined : text(raw.apiKey, 16384);
  return { config: { apiBaseUrl, timeoutMs, ...(apiKey ? { apiKey } : {}) }, endpoint: `${apiBaseUrl}/systemone` };
}

function summaries(runDir) {
  const result = {};
  for (const [key, ledger, limits] of [["global", "model-budget.sqlite", "budget-limits.json"], ["probe", "probe-budget.sqlite", "probe-budget-limits.json"]]) {
    const child = spawnSync(path.join(workspace, "experiments/.venv/bin/python"), [
      path.join(workspace, "experiments/scripts/model_budget.py"),
      "--ledger", path.join(runDir, ledger), "--limits", path.join(runDir, limits), "summary",
    ], { encoding: "utf8", timeout: 30000, maxBuffer: 1000000 });
    if (child.status !== 0) throw new Error("M0 budget summary unavailable");
    result[key] = JSON.parse(child.stdout);
  }
  return result;
}

export async function runHostProbe(input, { nativeFetch = globalThis.fetch.bind(globalThis) } = {}) {
  // Capture transport before adapter creation replaces ambient fetch. It is
  // passed only to the budget owner, never called from another path here.
  if (!record(input) || input.model !== "jev-latest" || input.resolvedModel !== "jev-1.14.0") fail();
  const configured = provider(input.providerConfig);
  const probes = list(input.probes, 5).map(publicProbe);
  if (!probes.length || new Set(probes.map((probe) => probe.id)).size !== probes.length) fail();
  const profile = routingProfile(input.routingProfile);
  const datasets = await realpath(path.join(workspace, "experiments/datasets"));
  const runDir = await realpath(text(input.runDir, 4096));
  if (!inside(datasets, runDir)) fail();
  const artifactPath = path.join(runDir, "m0-host-probes.json");
  for (const name of ["m0-host-probes.json", "m0-host-probes.json.next", "m0-host-runtime", "budget-limits.json", "probe-budget-limits.json", "model-budget.sqlite", "probe-budget.sqlite", "model-cache", "model-requests.jsonl"]) {
    try { if ((await lstat(path.join(runDir, name))).isSymbolicLink()) fail(); }
    catch (error) { if (error.code !== "ENOENT") throw error; }
  }
  const identity = {
    fixtureKind, model: input.model, resolvedModel: input.resolvedModel,
    endpointIdentitySha256: sha(configured.endpoint), providerTimeoutMs: configured.config.timeoutMs,
    routingProfile: profile, probes,
  };
  const inputSha256 = sha(JSON.stringify(identity));
  try {
    const existing = JSON.parse(await readFile(artifactPath, "utf8"));
    if (existing.schemaVersion !== 1 || existing.status !== "complete" || existing.inputSha256 !== inputSha256 ||
        !Array.isArray(existing.results) || existing.results.length !== probes.length ||
        existing.results.some((entry, index) => entry.status !== "ok" || entry.probeId !== probes[index].id || entry.inputSha256 !== probes[index].inputSha256) ||
        !Number.isInteger(existing.transport?.physicalAttempts)) {
      throw new Error("M0 existing artifact blocks automatic rerun");
    }
    return { status: "cached", completedProbes: existing.results.length, physicalAttempts: existing.transport.physicalAttempts, artifactPath };
  } catch (error) {
    if (error.code !== "ENOENT") throw error;
  }
  // Exclusive creation is also the restart/concurrency fence. A crash leaves a
  // running/partial artifact that must be reviewed before any further attempt.
  const artifact = {
    schemaVersion: 1, status: "running", inputSha256, fixtureKind,
    requestedModel: input.model, resolvedModel: input.resolvedModel,
    routingProfile: profile, startedAt: new Date().toISOString(),
    interpretation: "Controlled host logic via installed SDK transport seam; no accuracy, live Gateway, QMD retrieval, production experience or production graph faithfulness claim.",
    inputs: probes.map(({ id, params, inputSha256: hash }) => ({ id, inputSha256: hash, metadata: params })),
    results: [], transport: { physicalAttempts: 0, cacheHits: 0 },
  };
  await writeFile(artifactPath, `${JSON.stringify(artifact, null, 2)}\n`, { flag: "wx", mode: 0o600 });
  const persist = async () => {
    const temporary = `${artifactPath}.next`;
    await writeFile(temporary, `${JSON.stringify(artifact, null, 2)}\n`, { flag: "wx", mode: 0o600 });
    await rename(temporary, artifactPath);
  };
  let adapter;
  let transport;
  try {
    artifact.usageBefore = summaries(runDir);
    transport = createControlledFetch({
      runDir, probe: true, python: path.join(workspace, "experiments/.venv/bin/python"), nativeFetch,
      endpoints: [{ url: configured.endpoint, provider: "jev", model: input.model, resolvedModel: input.resolvedModel,
        validate: (payload, body) => adapter.validateWireResponse(payload, body) }],
    });
    const fixtureRoot = path.join(runDir, "m0-host-runtime");
    await mkdir(fixtureRoot, { recursive: true });
    let wireHash;
    adapter = await createHostDecisionAdapter({
      fixtureRoot, providerConfig: configured.config, model: input.model, offline: false,
      fetchImpl: (url, init) => { wireHash = sha(init.body); return transport(url, init); },
    });
    const provenance = adapter.provenance;
    artifact.provenance = {
      mode: provenance.mode, consumerPluginId: provenance.consumerPluginId,
      runtimeVersions: provenance.runtimeVersions, sources: provenance.sources,
      transportBoundary: provenance.transportBoundary, fixtureKind,
      runnerSources: await Promise.all(["probe_host_decision.mjs", "host_decision_adapter.mjs", "controlled_model_fetch.mjs", "model_budget.py"].map(async (name) => {
        const filename = path.join(workspace, "experiments/scripts", name);
        return { path: filename, sha256: sha(await readFile(filename)) };
      })),
    };
    for (const [index, probe] of probes.entries()) {
      wireHash = undefined;
      const started = performance.now();
      artifact.currentRequest = { requestId: `m0-host-${index + 1}-${probe.id}-${probe.inputSha256.slice(0, 12)}`,
        probeId: probe.id, inputSha256: probe.inputSha256 };
      await persist();
      const result = await adapter.evaluateSelection(probe.params, { timeoutMs: profile.timeoutMs, routing: profile });
      const ok = result.outcome?.status === "ok" && result.selection && result.outcome.result.model === input.resolvedModel;
      artifact.results.push({
        requestId: artifact.currentRequest.requestId,
        probeId: probe.id, inputSha256: probe.inputSha256, wireRequestSha256: wireHash ?? null,
        status: ok ? "ok" : "unavailable", outcome: result.outcome ?? { status: "unavailable", reason: "operation-failed" },
        selection: result.selection ?? null, trace: result.trace, durationMs: performance.now() - started,
      });
      delete artifact.currentRequest;
      artifact.transport = { ...transport.stats };
      artifact.usageAfter = summaries(runDir);
      if (!ok) {
        artifact.status = "failed";
        artifact.failure = "host-unavailable-or-model-identity";
        artifact.finishedAt = new Date().toISOString();
        await persist();
        return { status: "failed", completedProbes: artifact.results.filter((entry) => entry.status === "ok").length,
          physicalAttempts: transport.stats.physicalAttempts, artifactPath };
      }
      await persist();
    }
    artifact.status = "complete";
    artifact.finishedAt = new Date().toISOString();
    await persist();
    return { status: "complete", completedProbes: probes.length, physicalAttempts: transport.stats.physicalAttempts, artifactPath };
  } catch {
    if (artifact.currentRequest) {
      artifact.results.push({ ...artifact.currentRequest, status: "error", wireRequestSha256: null,
        outcome: { status: "unavailable", reason: "operation-failed" } });
      delete artifact.currentRequest;
    }
    artifact.status = "failed";
    artifact.failure = "probe-operation-failed";
    artifact.finishedAt = new Date().toISOString();
    artifact.transport = { ...transport?.stats ?? artifact.transport };
    try { artifact.usageAfter = summaries(runDir); } catch { artifact.usageSummaryUnavailable = true; }
    await persist();
    return { status: "failed", completedProbes: artifact.results.filter((entry) => entry.status === "ok").length,
      physicalAttempts: artifact.transport.physicalAttempts, artifactPath };
  } finally {
    await adapter?.close();
  }
}

async function main() {
  const chunks = [];
  let bytes = 0;
  for await (const chunk of process.stdin) {
    bytes += chunk.length;
    if (bytes > 1048576) fail();
    chunks.push(chunk);
  }
  const input = JSON.parse(Buffer.concat(chunks).toString("utf8"));
  const result = await runHostProbe(input);
  process.stdout.write(`${JSON.stringify(result)}\n`);
  if (result.status === "failed") process.exitCode = 1;
}

if (process.argv[1] && import.meta.url === pathToFileURL(path.resolve(process.argv[1])).href) {
  main().catch(() => { process.stderr.write("M0 host probe failed; details omitted\n"); process.exitCode = 1; });
}
