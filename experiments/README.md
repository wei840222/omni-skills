# Full-catalog skill routing experiments

Benchmark the current `skills/*/SKILL.md` packages with their author-provided
`test-prompts.json` cases. Results, embeddings and caches stay in `datasets/`;
the notebooks read these local artifacts without calling a model.

## Set up and run

From this directory:

```bash
uv sync --locked
uv run python scripts/prepare_experiment_datasets.py
uv run python scripts/generate_embeddings.py --embed-model text-embedding-3-small --dimension 1536
uv run python scripts/run_routing_evaluation.py --embed-model text-embedding-3-small --dimension 1536
```

The default remote endpoints, dimensions and authentication are read from
`~/.config/qmd/index.yml`. The embedding model argument overrides the model for
this run. The reranker uses the configured `models.rerank_api_model` and endpoint.
Credentials remain in the user's configuration and are never written to results.
Remote embedding and rerank calls incur the provider's normal usage charges.
Content and model fingerprints allow interrupted remote work to resume from
local caches; changing the corpus, query or model invalidates affected entries.

## Open the notebooks

```bash
uv run marimo edit notebooks/skill_router_mo.py --host 127.0.0.1 --port 2718 --no-token
uv run marimo edit notebooks/vector_visualization_mo.py --host 127.0.0.1 --port 2719 --no-token
uv run marimo edit notebooks/harness_quality_mo.py --host 127.0.0.1 --port 2720 --no-token
uv run marimo edit notebooks/ontology_graph_mo.py --host 127.0.0.1 --port 2721 --no-token
```

The router notebook shows measured metrics, per-query failures, transitions and
service timing. The vector notebook shows projections and distances from the
current embedding artifacts. Missing artifacts produce instructions to run the
commands above. No QMD index or global collection changes are required.

The ontology notebook replays `../ontology/graph.jsonl` and shows the current
directed graph, degree distributions, reciprocal declarations, connected
components and isolated skills. Search for a skill and choose incoming,
outgoing or both to inspect its one-hop arrows and original relation reasons.
It uses local data only. Force-layout distances are visual, and relation counts
are not skill-quality scores or evidence of routing accuracy.

## What is compared

| Representation | Content |
| --- | --- |
| `name-description` | Skill name and frontmatter description |
| `full` | Chunked complete `SKILL.md` |
| `full-references` | Chunked `SKILL.md` and recursive Markdown references |

All four pipelines receive the same original natural-language query:

1. SQLite FTS5 BM25 lexical retrieval.
2. Dense cosine retrieval with maximum chunk similarity per skill.
3. Reciprocal rank fusion of lexical and dense candidate lists.
4. The configured remote model reranking hybrid candidates.

The old answer-conditioned `bm25_prompt` fields are ignored. The historical
`generate_bm25_prompts.py` command now only compiles original query records and
never calls a generator or modifies skill packages. Pipeline selection uses
stable identifiers; reranking performs real model requests.

## Interpretation and provenance

Hit@1/3/5 and MRR@10 use the prompt's owning skill as a single ground-truth
label. These are skill-authored scenarios, not an independent held-out routing
benchmark. Overlapping skills can both be useful while the metric accepts only
one label. BM25 uses FTS5 lexical tokenization; this is not a reproduction of
QMD's complete production query expansion and ranking pipeline.

`manifest.json`, `embedding_manifest.json` and `routing_benchmark_results.json`
record corpus/query hashes, source revision, model settings, chunk sizes and
actual counts. Timings distinguish local cached retrieval from remote model
service calls. They do not establish end-to-end cold-start production latency.
A cached rerank retains the original request timing; it is not a new timing run.
PCA plots are projections; semantic distances use the original vector space.

## Validate

```bash
uv run python -m unittest discover -s tests -v
uv run marimo check notebooks
```

Run both notebook apps after generating data. Generated datasets, service
caches and virtual environments are ignored by Git.

## Harness-aligned evaluation

The 2026-10-25 harness run retained the current baseline. See the
[results and limitations](reports/harness-quality-20261025.md),
[compact data and task sources](reports/harness-quality-20261025.json), and
`../plan/active/2026-10-25-skill-library-harness-quality.md`. Its M0 artifacts
freeze the public corpus and installed plugin/host source hashes. They do not
turn the historical `rerank-3` results into production Decision accuracy.

The Node adapters use the locally installed skill-harness, QMD, OpenClaw and
TypeSafe implementations. Host tests exercise the actual public Decision
facade with synthetic configuration and a controlled HTTP callback. The SDK
mock-fetch seam bypasses DNS/dispatcher creation; the tests do not validate the
production network guard. No Gateway is started or changed.

Public QMD document vectors are reused only when normalized content, path,
title, model, chunk positions and dimensions match. Changed public content stays
in the corpus and is reported as a gap. The current run reused 10,433 inputs and
embedded ten public `triage` inputs; the resulting isolated profile has 10,443
vector rows. This is corpus readiness, not a measured routing improvement.

Every physical paid request and retry passes a persisted reservation ledger.
The M0 attempt cap also consumes the full-run ledger. Missing usage retains its
reservation; two consecutive provider failures stop new requests. Cache keys
include exact payload and frozen response model, and only consumer-validated
responses enter the cache. Budget files and credentials are never committed;
credentials reach the paid runners through stdin rather than command arguments.

From this directory, the offline checks are:

```bash
uv run python -m unittest discover -s tests -v
node --test tests/*.mjs
```

The host and QMD tests require the installed local plugins. Five successful
public M0 host probes validate integration only. The independent pilot labels,
development comparisons and single held-out comparison were completed. No tested
change passed the frozen adoption rules; this run does not establish a causal
benefit over using no harness.

The pilot has 180 public cases in 36 intent families, with 120 development cases
and 60 held-out cases. The committed primary annotations are an immutable first
review, not final gold labels. Final source-adjudicated silver labels and their
hash manifest live in the ignored run directory as `m1-silver-labels.json` and
`m1-freeze.json`. Uncertain cases remain visible and are excluded from the main
quality denominator. A launcher refuses paid stages before that freeze exists.
A versioned copy of the final silver annotations is also committed as
`fixtures/harness_silver_annotations.json`; it has the same bytes as the run copy.

The ablation protocol is fixed in `fixtures/harness_ablation_protocol.json`.
It first compares fusion rules, then candidate pools of 6/10/20 with injection
cap 6, then bounded matched passages. Every variant reuses the same captured raw
hitlists. The selector uses the installed host facade, the frozen 0.4 skill
threshold and 8,000 ms timeout. It does not substitute a generic reranker.

After the M1 freeze, the explicit development-stage commands are:

```bash
uv run python scripts/run_harness_stage.py --stage capture --phase development --run-dir datasets/harness-quality-20261025
uv run python scripts/run_harness_stage.py --stage prepare --phase development --run-dir datasets/harness-quality-20261025 --fusion current-max --pool-limit 6 --snippet none
uv run python scripts/run_harness_stage.py --stage select --phase development --run-dir datasets/harness-quality-20261025 --variant current-max-pool6-none
```

Capture and selection read only the allowed model fields from QMD settings and
pass credentials in memory through stdin. Preparation runs without model access.
Completed artifacts must match their original hashes; an incomplete paid attempt
requires inspection rather than an automatic rerun. Holdout capture and selection
also require the single frozen `challenger-config.json`.

Cached model observations retain their original service time and billed input
tokens. Cache lookup time is never reported as selector service latency. Query
time, reconstructed pipeline time and actual new spending are separate measures.
The 12 task validators in `harness_task_checks.py` check generated artifacts; their
authored positive/negative controls are not counted as actual paired task results.
They cover a small public task subset and do not establish whole-library quality.

The harness notebook reads the local run when present and otherwise uses the
committed compact export. It shows family-macro set F1, single/multi-turn case
groups, uncertainty exclusions, paired comparisons, original service timings,
and actual task results without issuing model requests.

M4 task routing uses three fresh Node processes through this launcher:

```bash
uv run python scripts/run_harness_tasks.py --stage raw --run-dir datasets/harness-quality-20261025
uv run python scripts/run_harness_tasks.py --stage prepare --run-dir datasets/harness-quality-20261025
uv run python scripts/run_harness_tasks.py --stage select --run-dir datasets/harness-quality-20261025
```

Routing does not generate task answers. `prepare_harness_task_packets.py` prepares
opaque public-only packets for fresh native workers; `collect_harness_tasks.py`
requires primary-agent source inspection before executing the frozen graders.
The completed run has 24 single-attempt native artifacts. Primary scores remain
10/12 per arm. Four guard-rejected artifacts passed a separately reviewed API
compatibility supplement; `supplement_harness_task_checks.py` preserves the
original grader, cases, artifacts and primary scores. This supplement is not
adoption evidence. The JSON export includes the actual artifact sources.
