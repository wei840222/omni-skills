---
name: search-engine
description: >
  Plan engine-agnostic search architectures, indexing pipelines, retrieval
  contracts, relevance policy, offline evaluation, and safe rollout when the
  user is designing or tuning search for apps, docs, products, or knowledge
  bases. Prefer `elasticsearch` for Elasticsearch/OpenSearch cluster and Query
  DSL work, `meilisearch` for lightweight site/product search, and `rag` when
  the ask is LLM retrieval pipelines rather than general search-system design.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔎"}'
  related-skills: '{"elasticsearch":"Elasticsearch/OpenSearch mappings, Query DSL, cluster ops, and ES-specific vector fields.","meilisearch":"Lightweight site and product search when a full search cluster is more than the job needs.","rag":"LLM retrieval pipelines built on top of an index once the retrieval contract is set.","engineering":"Structure multi-week search delivery workstreams and decision logs.","software-engineer":"Testable rollout discipline, CI gates, and incident-ready delivery practices."}'
---

# Search Engine

Engine-agnostic guidance for designing, evaluating, and rolling out search
systems. This skill advises architecture and relevance workflow; it does not
mutate production indexes or call vendor APIs without explicit user approval.

Optional persistent notes live under a resolved `<state_root>/search-engine/`
tree outside this package. Never write runtime state into the skill tree.

## State location

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/search-engine/`, `<workspace>/memory/search-engine/`,
   `~/search-engine/`.
3. If several candidates exist, use only the highest-precedence directory,
   report the split copies, and do not merge or cross-write.
4. If none exists and the user wants durable notes, create
   `<workspace>/search-engine/` when `<workspace>` is available; otherwise ask
   for a state root instead of guessing from the shell cwd.
5. Prefer portable `<state_root>` paths; never hard-code host-specific absolute
   roots. Skill resources stay under `references/` and `assets/`; never treat
   the literal string `<state_root>` as a filesystem path.

Persistent state is enabled only when the user explicitly requests retention or
approves a named persistent write.

```text
<state_root>/
|-- memory.md          # Persistent context, constraints, and active priorities
|-- requirements.md    # Retrieval goals, latency targets, relevance expectations
|-- experiments.md     # Offline experiments and tuning decisions
`-- incidents.md       # Production issues, root cause, and remediation notes
```

## Setup

On first use, read `references/setup.md` and establish activation behavior,
system scope, and data constraints before proposing implementation steps.

## When to Use

Use this skill when the user needs to create, redesign, or scale a search
engine for applications, documentation, products, or internal knowledge bases.
Cover architecture planning, indexing strategy, retrieval design, relevance
controls, evaluation loops, and rollout safety.

Hand off when the work becomes product-specific:

- Elasticsearch / OpenSearch cluster, mappings, Query DSL → `elasticsearch`
- Meilisearch index settings / typo tolerance → `meilisearch`
- LLM chunking, embeddings orchestration, answer grounding → `rag`

## When to load what

| Need | Load |
|------|------|
| First-run activation + constraints | `references/setup.md` |
| Memory / status template shapes | `assets/data-templates.md` |
| Architecture options by scale | `references/architecture-blueprint.md` |
| Lexical / semantic / hybrid patterns | `references/retrieval-patterns.md` |
| Offline metrics and release gates | `references/evaluation-metrics.md` |
| Build → validate → rollout checklist | `references/implementation-checklist.md` |
| Official URLs and claim checklist | `references/sources.md` |

## Core Rules

### 1. Start with a Retrieval Contract, Not with Tools
Before selecting engines, define the contract:

- query types to support (keyword, phrase, semantic, hybrid)
- response format, latency budget, and freshness target
- error tolerance and fallback behavior

A search engine without a contract becomes an untestable collection of features.

### 2. Design Ingestion and Indexing as a Deterministic Pipeline
Every document should pass explicit stages:

- ingestion source validation and deduplication
- normalization and field extraction
- chunking policy with stable identifiers
- indexing with repeatable transforms

Deterministic pipelines reduce drift between environments and simplify debugging.

### 3. Separate Recall Layers from Precision Layers
Treat retrieval as a staged system:

- broad candidate retrieval first (lexical, vector, or hybrid)
- reranking and business rules second
- formatting and explanation last

Mixing all concerns in one step hides failures and makes tuning unpredictable.

### 4. Define Relevance Features as Versioned Policy
Relevance changes must be tracked as policy versions:

- feature weights and boosts
- typo tolerance and synonym policy
- filtering, faceting, and tie-break rules

Never ship relevance changes without versioned notes and measured deltas.

### 5. Evaluate Offline Before Production Writes
For each relevance or indexing change:

- run benchmark queries with labeled expectations
- measure hit quality, ordering quality, and coverage
- compare against current baseline and note regressions

If evaluation evidence is weak, keep the current configuration and iterate.

### 6. Build Idempotent Index Operations and Safe Rollback
Index updates must be replay-safe:

- stable document ids and version checks
- resumable batch jobs with checkpoints
- alias-based or dual-index rollback plan

Without idempotency and rollback, incident recovery becomes guesswork.

### 7. Match Complexity to Workload Reality
Use the minimum architecture that meets requirements:

- use simple localized architectures for small datasets
- select robust models for multilingual or high-noise corpora
- revisit design as scale and usage patterns change

Over-engineering and under-engineering both create expensive rework.

## Common Traps

When a search redesign starts drifting, recover with the positive next action first:

- Missing retrieval contract → write the contract before vendor selection.
- Weak filters / noisy matches → normalize fields before indexing.
- Brittle relevance → tune across head, long-tail, multilingual, and negative queries.
- Business boosts crowding useful hits → add explicit boost guardrails and re-measure.
- Unverified ranking change → load `references/evaluation-metrics.md` and compare offline before shipping.
- Reindex risk → make full reindex jobs resumable with checkpoints.
- Multilingual precision claims → verify tokenization per language before asserting parity.

## Security & Privacy

Data that leaves your machine:

- none by default in this instruction set
- only user-approved integration traffic when the user explicitly connects external services

Data that stays local:

- planning notes and experiment logs under `<state_root>/`
- constraints, relevance decisions, and rollback records

This skill does NOT:

- collect unrelated files or credentials
- require hidden network calls
- bypass user-confirmed environment boundaries
