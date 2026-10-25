# Routing experiments

This directory benchmarks the current `skills/*/SKILL.md` catalog. Keep generated
data under the ignored `datasets/` directory and the uv environment under `.venv/`.
Use `uv sync --locked` before running the scripts. See `README.md` for commands.

## Experimental contract

- Select all current skill packages, independently of historical CHANGELOG rows.
- Compare three representations: `name-description`, `full`, `full-references`.
- Use the same original natural-language task for lexical, dense, hybrid and
  rerank stages. Ground-truth labels and legacy `bm25_prompt` keywords must never
  be supplied to query rewriting or retrieval.
- Treat each test prompt's owning skill as the author-provided single label.
  These are skill-authored cases, not an independent held-out routing dataset.
  Do not infer real-world accuracy or multi-label correctness from these alone.
- Use stable pipeline identifiers. RRF must combine lexical and dense rankings;
  rerank must call the configured model, not simulate one with rank weights.
- Read endpoint, authentication and model defaults from the user's QMD YAML at
  runtime. Model overrides belong to run arguments. Never save credentials in
  artifacts, logs, examples or version control.
- Record corpus/query fingerprints, source revision, model/dimension settings,
  chunking, candidate limits and collection counts. Cache by actual input and
  model configuration; preserve response ordering and validate vector dimensions.
- Measure timings. Distinguish remote API service time, cached local retrieval,
  throughput and notebook load time. Never label static numbers as observations.
- Do not modify `skills/` when generating benchmarks. Generated datasets may be
  regenerated; user runtime QMD indexes and configuration are outside this task.

## Notebooks

The router notebook reads benchmark results and the vector notebook reads the
embedding artifacts. Counts, metrics, transitions and charts must derive from
those artifacts. Missing data should produce actionable UI, not fake results.

- Prefix cell-local names with `_`; give shared variables one defining cell.
- Compute semantic distances in the original embedding space. PCA is a visual
  projection, not evidence that distances or groups are preserved.
- Use ASCII matplotlib titles and labels to avoid missing-font warnings.
- Render plots in notebook cells; do not dump PNG/JPG files.
- Inspect running Marimo sessions before editing. Use the `marimo-pair` skill
  and live code-mode API for any notebook already open in a live kernel.
- Run `uv run marimo check notebooks` and execute both apps after changes.

## Validation

Run focused tests for ranking dispatch, query leakage, response ordering, cache
invalidation and metrics. Verify small real requests before a full remote run.
Do not silently convert service/schema failures into retrieval misses, invent
ablation results, or carry conclusions forward after the corpus/model changes.
