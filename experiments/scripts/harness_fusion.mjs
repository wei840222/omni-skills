/** Local ablation of frozen public QMD hitlists. No model or quality scoring.
 * The baseline runs installed createSkillQmdIndex against a frozen FakeStore.
 * The alternative changes fusion identity only, retaining document ranks.
 */
import { createHash } from "node:crypto";
import { mkdir, readFile, readdir, writeFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { createHarnessRetrievalAdapter, loadInstalledRetrievalSources } from "./harness_retrieval_adapter.mjs";

const workspace = fileURLToPath(new URL("../../", import.meta.url));
const runRoot = path.join(workspace, "experiments/datasets/harness-quality-20261025");
const weights = { "skill-meta": 3, "skill-body": 2, "skill-references": 1 };
const hash = (value) => createHash("sha256").update(value).digest("hex");
const inside = (root, filename) => { const relative = path.relative(root, filename); return relative && !relative.startsWith("..") && !path.isAbsolute(relative); };

async function isolatedParsers(sources) {
  const sourcePath = sources.sources.find((entry) => entry.path.endsWith("/qmd/skill-index.js"))?.path;
  if (!sourcePath) throw new Error("Installed skill index source identity is missing");
  const text = await readFile(sourcePath, "utf8");
  const names = ["parseFrontmatterIdentity", "hitId", "deriveEvidenceScore", "parseStoreHits", "decodeSkillSegment"];
  const fragments = names.map((name) => {
    const fragment = text.match(new RegExp(`function ${name}\\([^\\n]*\\) \\{[\\s\\S]*?\\n\\}`))?.[0];
    if (!fragment) throw new Error(`Installed private pure helper not found: ${name}`);
    return { name, fragment, sha256: hash(fragment) };
  });
  // Every body is the installed pure function verbatim. The only external
  // bindings are its actual gray-matter and public path-identity decoder.
  const parser = new Function("matter", "skillIdentityFromDocsPath", `${fragments.map((entry) => entry.fragment).join("\n")}\nreturn {parseStoreHits,hitId,deriveEvidenceScore,decodeSkillSegment};`)(sources.matter, sources.skillIdentityFromDocsPath);
  return { ...parser, provenance: { sourcePath, sourceSha256: hash(text), mode: "source-isolated-verbatim-private-pure-functions", fragments: fragments.map(({ name, sha256 }) => ({ name, sha256 })) } };
}

function frozenInput(observation) {
  if (typeof observation?.query !== "string" || !Array.isArray(observation.rawHitlists) || (observation.expansionContext !== undefined && typeof observation.expansionContext !== "string")) throw new Error("Frozen observation requires query/context strings and rawHitlists");
  const hitlists = new Map();
  for (const entry of observation.rawHitlists) {
    const collection = entry.options?.collection;
    if (!Object.hasOwn(weights, collection) || hitlists.has(collection) || !Array.isArray(entry.hits) || entry.hits.length > 40 || entry.options.limit !== 40 || entry.options.candidateLimit !== 40 || entry.options.rerank !== false || entry.options.explain !== true) throw new Error("Expected unique frozen three-collection top40 hitlists");
    hitlists.set(collection, structuredClone(entry.hits));
  }
  if (hitlists.size !== 3) throw new Error("All three frozen hitlists are required, including empty collections");
  return { query: observation.query, ...(observation.expansionContext === undefined ? {} : { expansionContext: observation.expansionContext }), hitlists };
}

function identitySum(input, parser, sources, publicNames, docsRoot) {
  const visible = new Set(publicNames.map((name) => name.toLowerCase()));
  const segments = new Map();
  for (const name of publicNames) {
    const segment = parser.decodeSkillSegment(sources.safePathSegment(name)).toLowerCase();
    segments.set(segment, segments.has(segment) ? undefined : name);
  }
  const skills = new Map();
  for (const [collection, weight] of Object.entries(weights)) {
    const ranked = parser.parseStoreHits({ results: input.hitlists.get(collection), collection, docsRoot, namesBySegment: segments })
      .filter((hit) => visible.has(hit.skillName.toLowerCase()))
      .sort((left, right) => right.score - left.score || parser.hitId(left).localeCompare(parser.hitId(right)));
    const contributed = new Set();
    for (let index = 0; index < ranked.length; index++) {
      const hit = ranked[index];
      const rank = index + 1; // Keep original document position, before skill dedup.
      const contribution = weight / (60 + rank);
      const skill = skills.get(hit.skillName) ?? { name: hit.skillName, score: 0, evidenceById: new Map(), contributions: [] };
      if (!contributed.has(hit.skillName)) {
        skill.score += contribution;
        skill.contributions.push({ collection, documentRank: rank, weight, contribution });
        contributed.add(hit.skillName);
      }
      const semanticScore = parser.deriveEvidenceScore(hit.explain);
      if (semanticScore !== undefined && (skill.semanticScore === undefined || semanticScore > skill.semanticScore)) skill.semanticScore = semanticScore;
      const id = parser.hitId(hit);
      if (!skill.evidenceById.has(id)) skill.evidenceById.set(id, { collection: hit.collection, path: hit.path, score: contribution, ...(hit.snippet ? { snippet: hit.snippet } : {}), ...(hit.explain === undefined ? {} : { explain: hit.explain }) });
      skills.set(hit.skillName, skill);
    }
  }
  return [...skills.values()].map((skill) => ({
    name: skill.name, score: skill.score,
    ...(skill.semanticScore === undefined ? {} : { semanticScore: skill.semanticScore }),
    evidence: [...skill.evidenceById.values()].sort((left, right) => right.score - left.score || `${left.collection}\0${left.path}`.localeCompare(`${right.collection}\0${right.path}`)).slice(0, 3),
    contributions: skill.contributions,
  })).sort((left, right) => right.score - left.score || left.name.localeCompare(right.name));
}

export async function createFrozenFusionReplay({ config, fixtureRoot, root = workspace, profileDir = path.join(runRoot, "qmd-public") } = {}) {
  config = structuredClone(config);
  if (config?.routing?.skills?.maxInjectedSkills !== 6 || config?.skills?.search?.collectionWeights?.meta !== 3 || config.skills.search.collectionWeights.body !== 2 || config.skills.search.collectionWeights.references !== 1) throw new Error("This ablation fixes injection cap6 and collection weights3/2/1");
  fixtureRoot = path.resolve(fixtureRoot ?? "");
  if (!inside(path.join(runRoot, "replay-runtime"), fixtureRoot)) throw new Error("Frozen replay needs its own ignored fixture under replay-runtime");
  const sources = await loadInstalledRetrievalSources({ offline: true });
  const parser = await isolatedParsers(sources);
  const implementation = { fusion: { path: fileURLToPath(import.meta.url), sha256: hash(await readFile(fileURLToPath(import.meta.url))) }, downstream: { path: fileURLToPath(new URL("./harness_retrieval_adapter.mjs", import.meta.url)), sha256: hash(await readFile(new URL("./harness_retrieval_adapter.mjs", import.meta.url))) } };
  const publicNames = [];
  for (const entry of (await readdir(path.join(root, "skills"))).sort()) {
    try { const parsed = sources.matter(await readFile(path.join(root, "skills", entry, "SKILL.md"), "utf8")); if (parsed.data.name === entry) publicNames.push(entry); }
    catch (error) { if (!["ENOENT", "ENOTDIR"].includes(error.code)) throw error; }
  }
  if (publicNames.length !== 963) throw new Error("Frozen fusion replay must retain all 963 public skills");
  const downstream = await createHarnessRetrievalAdapter({ root, profileDir, dataRoot: path.join(fixtureRoot, "downstream"), resolvedConfig: config, offline: true, fetchImpl: async () => { throw new Error("Frozen fusion replay forbids model transport"); } });
  const fakeRoot = path.join(fixtureRoot, "frozen");
  const fingerprint = hash(JSON.stringify({ publicNames, mode: "frozen-fakestore-only" }));
  const indexRoot = path.join(fakeRoot, "qmd/skills/indexes", fingerprint);
  const docsRoot = path.join(indexRoot, "docs");
  await mkdir(docsRoot, { recursive: true });
  await writeFile(path.join(indexRoot, "skill-search.sqlite"), "Frozen FakeStore fixture; no SQLite connection is opened.\n", { flag: "wx" });
  await mkdir(path.join(fakeRoot, "qmd/skills/agents"), { recursive: true });
  await writeFile(path.join(fakeRoot, "qmd/skills/agents/offline-eval.json"), JSON.stringify({ schemaVersion: 1, fingerprint, allowedSkillNames: publicNames }), { flag: "wx" });
  const frozenConfig = { qmd: { timeoutMs: config.qmd.timeoutMs, embedding: { model: "text-embedding-3-small", dimension: 1536, baseUrl: "https://qmd-reuse.invalid/v1" }, expansion: { model: config.qmd.expansion.model, baseUrl: "https://qmd-reuse.invalid/v1" } }, skills: config.skills };
  let active;
  let pending = Promise.resolve();
  let closed = false;
  const index = sources.createSkillQmdIndex({ dataRoot: fakeRoot, config: () => frozenConfig, readOnly: true,
    createStore: async (options) => {
      if (!options.readOnly || options.dbPath !== path.join(indexRoot, "skill-search.sqlite")) throw new Error("Frozen replay attempted a writable/unexpected store");
      return { close: async () => {}, search: async (options) => {
        if (!active || options.query !== active.query || options.limit !== 40 || options.candidateLimit !== 40 || options.rerank !== false) throw new Error("Frozen replay attempted a new or altered retrieval");
        return structuredClone(active.hitlists.get(options.collection));
      } };
    },
  });
  async function rank({ observation, fusion = "current-max", poolLimit = 6, controlledExperiences = [], controlledGraph = new Map() }) {
    if (closed) throw new Error("Frozen fusion replay is closed");
    if (!["current-max", "skill-identity-sum"].includes(fusion)) throw new Error("Unsupported frozen fusion strategy");
    if (![6, 10, 20].includes(poolLimit)) throw new Error("poolLimit must be one of6/10/20 independently of injection cap6");
    const input = frozenInput(observation);
    const sourceInput = { query: input.query, ...(input.expansionContext === undefined ? {} : { expansionContext: input.expansionContext }), rawHitlists: [...input.hitlists].map(([collection, hits]) => ({ collection, hits })) };
    let skillHits, contributions;
    if (fusion === "current-max") {
      active = input;
      try { skillHits = await index.search({ agentId: "offline-eval", query: input.query, limit: poolLimit, includeEvidence: true, ...(input.expansionContext === undefined ? {} : { expansionContext: input.expansionContext }) }); }
      finally { active = undefined; }
      if (!skillHits) throw new Error("Installed frozen baseline replay was unavailable");
    } else {
      const ranked = identitySum(input, parser, sources, publicNames, docsRoot).slice(0, poolLimit);
      contributions = Object.fromEntries(ranked.map((hit) => [hit.name, hit.contributions]));
      skillHits = ranked.map(({ contributions, ...hit }) => hit);
    }
    const candidates = downstream.candidatesFromHits({ query: input.query, skillHits, controlledExperiences, controlledGraph });
    return { skillHits, ...candidates,
      metadata: { schema_version: 1, fusion, poolLimit, injectionCap: 6, publicSkillCount: publicNames.length, rrfK: 60, weights: { ...weights }, rawInputSha256: hash(JSON.stringify(sourceInput)), sourceCallsAreFrozen: true,
        explicitControlledSourcesSha256: hash(JSON.stringify({ experiences: controlledExperiences, graph: [...controlledGraph.entries()].sort(([left], [right]) => left.localeCompare(right)) })),
        algorithm: fusion === "current-max" ? "Installed document-identity RRF, maximum fused document score per skill, then direct pool cap." : "For each collection use the best original parsed document rank per skill; sum weight/(60+rank) across collections only. No per-skill rank compression or same-collection file-volume summation.",
        rankBasis: "Installed visible parseStoreHits order: score descending, hitId tie-break; rank before any skill deduplication.",
        semanticScore: "Maximum finite installed deriveEvidenceScore over matching raw hit explanations; distinct from fusion score.",
        ...(contributions ? { contributions } : {}),
        provenance: { installedSources: structuredClone(sources.sources), parser: structuredClone(parser.provenance), implementation, downstreamMode: "actual candidatesFromHits method; fixed gate/name/union/superset policies" },
        scope: "Local ranking replay only; no model requests, labels, Decision or quality scores.",
      },
    };
  }
  return { publicNames: [...publicNames], rankFrozenCandidates(input) { const work = pending.then(() => rank(input)); pending = work.catch(() => {}); return work; }, async close() { await pending; closed = true; await index.close(); await downstream.close(); } };
}
