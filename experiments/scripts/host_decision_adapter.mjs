/** Installed host Decision V1 adapter. Run in a dedicated Node process.
 * No config, credentials, model, transport, or legacy endpoint is inferred.
 * Imports and idle periods use a rejecting fetch; the supplied callback owns
 * every admitted transport request. This module never retains native fetch.
 */
import { createHash } from "node:crypto";
import { mkdir, readFile, readdir, writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import net from "node:net";
import dgram from "node:dgram";
import dns from "node:dns";
import { fileURLToPath, pathToFileURL } from "node:url";

const workspace = fileURLToPath(new URL("../../", import.meta.url));
let processOwned = false;
const denyFetch = async () => { throw new Error("Fetch requires a controlled host decision evaluation"); };

function inside(root, target) {
  const relative = path.relative(root, target);
  return relative !== "" && !relative.startsWith("..") && !path.isAbsolute(relative);
}

async function findInternal(dist, prefix, declaration) {
  const matches = [];
  for (const name of await readdir(dist)) {
    if (name.startsWith(prefix) && name.endsWith(".mjs")) {
      const filename = path.join(dist, name);
      const source = await readFile(filename, "utf8");
      if (source.includes(declaration)) matches.push({ filename, source });
    }
  }
  if (matches.length !== 1) throw new Error(`Expected one installed host module for ${declaration}; found ${matches.length}`);
  return matches[0];
}

async function loadInternal(module, symbol) {
  // Resolve the actual export alias; compiled chunk names and aliases are unstable.
  const exports = module.source.match(/export \{([^}]+)\};?\s*$/s)?.[1];
  const item = exports?.split(",").map((value) => value.trim()).find((value) => value.split(/\s+as\s+/)[0] === symbol);
  if (!item) throw new Error(`Installed host does not export ${symbol}`);
  const alias = item.split(/\s+as\s+/)[1] ?? symbol;
  return (await import(pathToFileURL(module.filename).href))[alias];
}

export async function createHostDecisionAdapter({
  fixtureRoot,
  providerConfig,
  model,
  fetchImpl,
  offline = true,
  skillHarnessRoot = path.join(os.homedir(), ".openclaw/extensions/skill-harness"),
  typeSafeRoot = path.join(os.homedir(), ".openclaw/extensions/typesafe"),
}) {
  if (processOwned) throw new Error("Host Decision adapter requires a dedicated process and one owner");
  if (typeof fetchImpl !== "function") throw new Error("Explicit controlled fetch callback is required");
  if (typeof model !== "string" || !model.trim() || model.includes("typesafe/")) throw new Error("Explicit provider-local model is required");
  if (!providerConfig || typeof providerConfig !== "object" || (!providerConfig.apiBaseUrl && !providerConfig.baseUrl)) {
    throw new Error("Explicit TypeSafe runtime endpoint configuration is required");
  }
  fixtureRoot = path.resolve(fixtureRoot);
  if (!inside(path.join(workspace, "experiments/datasets"), fixtureRoot)) throw new Error("Fixture root must be inside workspace experiments/datasets");
  processOwned = true;
  // Install before importing any OpenClaw or plugin module. Never fall back.
  globalThis.fetch = denyFetch;
  const network = { socketAttempts: 0, dnsAttempts: 0 };
  if (offline) {
    // Guarded fetch may select Undici instead of ambient fetch. Block beneath
    // both before loading it, so a future SDK change cannot contact even loopback.
    const denySocket = () => { network.socketAttempts++; throw new Error("Offline host Decision forbids socket access"); };
    net.Socket.prototype.connect = denySocket;
    dgram.Socket.prototype.send = denySocket;
    const denyDns = () => { network.dnsAttempts++; throw new Error("Offline host Decision forbids DNS access"); };
    for (const target of [dns, dns.promises, dns.Resolver.prototype, dns.promises.Resolver.prototype]) {
      for (const key of Object.getOwnPropertyNames(target)) {
        if (/^(lookup|resolve|reverse)/.test(key) && typeof target[key] === "function") target[key] = denyDns;
      }
    }
  }
  const isolation = {
    stateDir: path.join(fixtureRoot, "state"),
    configPath: path.join(fixtureRoot, "openclaw.json"),
    logFile: path.join(fixtureRoot, "logs/host-decision.log"),
  };
  process.env.OPENCLAW_STATE_DIR = isolation.stateDir;
  process.env.OPENCLAW_CONFIG_PATH = isolation.configPath;
  process.env.OPENCLAW_LOG_LEVEL = "silent";
  const syntheticConfig = {
    agents: { defaults: { decisionModel: `typesafe/${model}` }, entries: [{ id: "offline-eval" }] },
    plugins: { enabled: true, entries: { typesafe: { enabled: true }, "skill-harness": { enabled: true } } },
    logging: { level: "silent", consoleLevel: "silent", file: isolation.logFile },
  };
  await mkdir(isolation.stateDir, { recursive: true });
  // Exclusive creation protects previous artifacts and makes all config reads synthetic.
  await writeFile(isolation.configPath, `${JSON.stringify(syntheticConfig, null, 2)}\n`, { flag: "wx", mode: 0o600 });
  const dist = path.join(skillHarnessRoot, "node_modules/openclaw/dist");
  const registryModule = await findInternal(dist, "registry-", "function createPluginRegistry(registryParams)");
  const snapshotModule = await findInternal(dist, "runtime-snapshot-", "function setRuntimeConfigSnapshot(config, sourceConfig)");
  const loggerModule = await findInternal(dist, "logger-", "function setLoggerOverride(settings)");
  const runtimeModule = await findInternal(dist, "runtime-", "async function evaluateDecisionInRegistry(batch,");
  const typeSafeDist = path.join(typeSafeRoot, "node_modules/openclaw/dist");
  const transportModules = [];
  for (const [prefix, declaration] of [
    ["fetch-guard-", "async function fetchWithSsrFGuardInternal(params)"],
    ["runtime-fetch-", "function isMockedFetch(fetchImpl)"],
    ["ssrf-", "function resolveSsrFPolicyForUrl(url, policy)"],
  ]) transportModules.push(await findInternal(typeSafeDist, prefix, declaration));
  const facadeEdge = registryModule.source.match(/const \{ evaluateDecisionInRegistry \} = await import\("(\.\/[^\"]+)"\)/)?.[1];
  const validationEdge = runtimeModule.source.match(/from "(\.\/validation-[^\"]+)"/)?.[1];
  if (!facadeEdge || !validationEdge) throw new Error("Installed host source layout changed; review facade and validation imports");
  const setRuntimeConfigSnapshot = await loadInternal(snapshotModule, "setRuntimeConfigSnapshot");
  setRuntimeConfigSnapshot(syntheticConfig);
  const setLoggerOverride = await loadInternal(loggerModule, "setLoggerOverride");
  setLoggerOverride(syntheticConfig.logging);
  const createPluginRegistry = await loadInternal(registryModule, "createPluginRegistry");
  const importPlugin = (root, filename) => import(pathToFileURL(path.join(root, filename)).href);
  const { createDecisionProvider } = await importPlugin(typeSafeRoot, "dist/src/decisions.js");
  const { parseInput, parseResult } = await importPlugin(typeSafeRoot, "dist/src/schema.js");
  const { buildSelectionBatch, parseSelectionResult } = await importPlugin(skillHarnessRoot, "dist/src/classification/selection-batch.js");
  const { evaluateSelection } = await importPlugin(skillHarnessRoot, "dist/src/classification/selection-runtime.js");
  const { resolveConfig } = await importPlugin(skillHarnessRoot, "dist/src/config.js");
  const { setApiLogger } = await importPlugin(skillHarnessRoot, "dist/api.js");
  const diagnostics = [];
  const logger = Object.fromEntries(["debug", "trace", "info", "warn", "error"].map((level) => [level, (message) => diagnostics.push({ level, message })]));
  setApiLogger(logger);
  const defaults = resolveConfig({}, { env: {}, openClawConfig: syntheticConfig });
  const registration = createPluginRegistry({
    runtime: { config: { current: () => syntheticConfig } },
    logger, coreGatewayMethodNames: [], activateGlobalSideEffects: false,
    allowProcessHomeSessionCatalogs: false,
  });
  const record = {
    id: "typesafe", name: "offline-eval", version: "2026.10.7",
    source: path.join(typeSafeRoot, "dist/index.js"), rootDir: typeSafeRoot,
    origin: "global", enabled: true, status: "loaded",
    contracts: { decisionProviders: ["typesafe"] }, services: [],
  };
  registration.registry.plugins.push(record);
  const api = registration.createApi(record, { config: syntheticConfig, pluginConfig: {}, registrationMode: "full" });
  // This is the installed TypeSafe provider; no provider/host logic is reimplemented.
  api.registerDecisionProvider(createDecisionProvider(() => ({ ...providerConfig })));
  if (registration.registry.decisionProviders.length !== 1 || registration.registry.diagnostics.length) {
    throw new Error("Installed TypeSafe provider registration failed");
  }
  const consumerRecord = {
    ...record, id: "skill-harness", name: "offline-skill-harness",
    source: path.join(skillHarnessRoot, "dist/index.js"), rootDir: skillHarnessRoot,
    contracts: {}, services: [],
  };
  registration.registry.plugins.push(consumerRecord);
  const consumerApi = registration.createApi(consumerRecord, { config: syntheticConfig, pluginConfig: {}, registrationMode: "full" });
  const sourcePaths = [
    registryModule.filename, snapshotModule.filename, loggerModule.filename, runtimeModule.filename,
    path.resolve(dist, facadeEdge), path.resolve(dist, validationEdge),
    ...transportModules.map((module) => module.filename),
    ...["dist/src/decisions.js", "dist/src/client.js", "dist/src/transport.js", "dist/src/schema.js", "dist/src/config.js"].map((name) => path.join(typeSafeRoot, name)),
    ...["dist/src/classification/selection-batch.js", "dist/src/classification/selection-runtime.js", "dist/src/config.js", "dist/src/constants.js", "dist/api.js"].map((name) => path.join(skillHarnessRoot, name)),
  ];
  const sources = [];
  for (const filename of sourcePaths) sources.push({ path: filename, sha256: createHash("sha256").update(await readFile(filename)).digest("hex") });
  const versions = {};
  for (const [name, root] of [["openclaw", path.dirname(dist)], ["skillHarness", skillHarnessRoot], ["typeSafe", typeSafeRoot]]) {
    versions[name] = JSON.parse(await readFile(path.join(root, "package.json"), "utf8")).version;
  }
  const provenance = {
    mode: "host-public-facade", consumerPluginId: "skill-harness", runtimeVersions: versions, sources, isolation, offline, network,
    defaults: { routing: defaults.routing },
    networkPolicy: "deny during imports/idle; explicit callback only during admitted evaluation; no native fetch fallback",
    transportBoundary: "SDK mock-fetch seam preserves request/response validation but skips DNS and dispatcher creation; callback owns transport",
  };
  let active = false;
  let closed = false;
  return {
    provenance,
    validateWireResponse(payload, body) {
      // Use the exact installed consumer schemas for pre-cache validation too.
      return parseResult(payload, parseInput(body));
    },
    async evaluateSelection(params, { timeoutMs = defaults.routing.timeoutMs, signal = new AbortController().signal, batch, providerAvailable = true, routing } = {}) {
      if (closed || active) throw new Error("Adapter is closed or an evaluation is already active");
      const trace = { fetchCalls: 0, hostCalls: 0, legacyCalls: 0, hostOptionKeys: [] };
      batch ??= buildSelectionBatch(params);
      if (Object.keys(batch.questions).length === 0) return { skipped: "empty-pool", trace };
      active = true;
      const entries = registration.registry.decisionProviders;
      const previousEntries = entries.splice(0);
      if (providerAvailable) entries.push(...previousEntries);
      const diagnosticStart = diagnostics.length;
      let outcome;
      globalThis.fetch = async (...args) => {
        if (!active) return denyFetch();
        trace.fetchCalls++;
        return fetchImpl(...args);
      };
      // The installed SSRF helper documents this mock seam. Without it a
      // dispatcher can bypass global fetch and therefore bypass the budget owner.
      globalThis.fetch.mock = {};
      try {
        const result = await evaluateSelection({
          batch, agentId: "offline-eval", timeoutMs, signal,
          api: {
            config: syntheticConfig,
            runtime: { decisions: { evaluate: async (input, options) => {
              trace.hostCalls++;
              trace.hostOptionKeys = Object.keys(options).sort();
              outcome = await consumerApi.runtime.decisions.evaluate(input, options);
              return outcome;
            } } },
          },
          legacy: async () => { trace.legacyCalls++; throw new Error("Legacy endpoint is forbidden"); },
        });
        const config = routing ? { ...defaults, routing: { ...defaults.routing, ...routing } } : defaults;
        return {
          selection: result ? parseSelectionResult(params, config, result) : undefined,
          outcome, trace, diagnostics: diagnostics.slice(diagnosticStart),
        };
      } finally {
        active = false;
        globalThis.fetch = denyFetch;
        entries.splice(0, entries.length, ...previousEntries);
      }
    },
    async close() {
      if (active) throw new Error("Cannot close an active evaluation");
      closed = true;
      for (const entry of registration.registry.decisionProviders) await entry.host.stop();
      globalThis.fetch = denyFetch;
    },
  };
}
