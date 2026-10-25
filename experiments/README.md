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
```

The router notebook shows measured metrics, per-query failures, transitions and
service timing. The vector notebook shows projections and distances from the
current embedding artifacts. Missing artifacts produce instructions to run the
commands above. No QMD index or global collection changes are required.

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
