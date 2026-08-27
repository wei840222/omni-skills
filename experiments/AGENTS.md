# AGENTS.md — SkillRouter & Embedding Experiments

## 🎯 Mission & Scope

This directory (`experiments/`) serves as the empirical research and benchmarking suite for `omni-skills`, replicating and expanding upon **[SkillRouter: Skill Routing for LLM Agents at Scale (arXiv:2603.22455)](https://arxiv.org/abs/2603.22455)**.

The objective is to evaluate, visualize, and diagnose skill routing, semantic manifolds, embedding drift, and retrieval efficiency across hundreds of modular agent skills.

---

## 🏛️ Experimental Architecture

### 1. Three-Tier Evaluation Collections
Experiments compare skill representations across three distinct corpus layers:

| Collection | Path | Content Description | Retrieval Characteristic |
|---|---|---|---|
| **`name-description` (ND)** | `datasets/name-description/` | Skill frontmatter `name` + `description` only | High-purity metadata, concise lexical matching (BM25 Hit@1 > 93%) |
| **`full`** | `datasets/full/` | Full `SKILL.md` document body | Comprehensive context, instructions, and examples |
| **`full-references`** | `datasets/full-references/` | Full `SKILL.md` + all files in `references/*.md` | Chunk-level Late Interaction (Max-Sim pooling) across 2,400+ vectors |

### 2. Model & Runtime Stack

- **Embedding Model**: Local `hf:Qwen/Qwen3-Embedding-0.6B-GGUF/Qwen3-Embedding-0.6B-Q8_0.gguf` (1024-dimensional dense vectors, executed via QMD).
- **LLM / Generation & Reranking**: `gemini-3.1-flash-lite-agy` via Bifrost OpenAI-compatible endpoint (`https://bifrost.home-infra.weii.cloud/openai/v1/chat/completions`).
- **Vector & Lexical Engine**: `QMD` (Quantum Markdown) backed by SQLite `index.sqlite` with `sqlite-vec` extension and FTS5 full-text search.
- **Interactive Environment**: [Marimo](https://marimo.io) reactive Python notebooks.
- **Python Virtualenv**: Managed via `uv` at `experiments/.venv`.

---

## 📂 Directory Layout

```
experiments/
├── AGENTS.md                               # This document (guidelines & SOPs)
├── README.md                               # User-facing experiment overview
├── pyproject.toml                          # uv package configuration & dependencies
├── .qmd/
│   ├── index.yml                           # QMD multi-collection index configuration
│   └── index.sqlite                        # Unified SQLite database (sqlite-vec + FTS5)
├── datasets/
│   ├── benchmark_queries.json              # 321 ground-truth queries extracted from test-prompts.json
│   ├── query_embeddings.json               # Cached 1024D Qwen3 embeddings for all benchmark queries
│   ├── routing_benchmark_results.json      # Full 5-pipeline evaluation metrics and case traces
│   ├── name-description/                   # Generated ND dataset (131 skills)
│   ├── full/                               # Generated Full SKILL.md dataset (131 skills)
│   └── full-references/                    # Generated Full + references/ dataset (961 files)
├── notebooks/
│   ├── vector_visualization_mo.py          # Marimo notebook: 3D PCA, KDE, Semantic Drift, Radius, Confusion
│   └── skill_router_mo.py                  # Marimo notebook: Benchmark matrix, Transitions, Pareto, Hard queries
└── scripts/
    ├── prepare_experiment_datasets.py      # Extracts skills from CHANGELOG.md into 3 dataset tiers
    ├── generate_bm25_prompts.py            # Generates keyword search prompts using Gemini
    ├── generate_qwen3_query_embeddings.js  # Precomputes 1024D vectors for all benchmark queries via QMD
    └── run_routing_evaluation.py           # Vectorized multi-collection benchmark runner
```

---

## 🔄 Standard Operating Procedures (SOPs)

### SOP 1: Re-Syncing Datasets & Updating Embeddings

When new skills are refactored or updated in `skills/`:

```bash
# 1. Activate environment
cd experiments && source .venv/bin/activate

# 2. Extract dataset tiers from CHANGELOG.md
python3 scripts/prepare_experiment_datasets.py

# 3. Generate BM25 prompts for newly added test-prompts
python3 scripts/generate_bm25_prompts.py

# 4. Update QMD database & compute document embeddings
qmd update
qmd embed

# 5. Precompute and cache query embeddings
node scripts/generate_qwen3_query_embeddings.js
```

### SOP 2: Executing Routing Evaluation Benchmark

To run the vectorized multi-collection routing benchmark across all 5 pipelines (BM25, Vector, Hybrid RRF, Hybrid No Rerank, Two-Stage Rerank):

```bash
python3 scripts/run_routing_evaluation.py
```
*Outputs are saved to `datasets/routing_benchmark_results.json` and printed as formatted tables.*

### SOP 3: Maintaining & Linting Marimo Notebooks

Marimo notebooks must remain deterministic, reactive, and warning-free:

```bash
# Lint and format notebook cells
marimo check --fix ./notebooks

# Verify execution without errors
python3 notebooks/vector_visualization_mo.py
python3 notebooks/skill_router_mo.py

# Launch interactive UI server
marimo edit --no-token --host 0.0.0.0 --port 2718
```

---

## 📐 Marimo & Code Conventions

1. **No Static Image Dumping**: Do NOT write static `.png` or `.jpg` plot files to disk. All visualizations must render dynamically inside Marimo notebook cells using `plt.subplots()` or `mo.ui` components.
2. **Namespace Hygiene**:
   - Variables internal to a cell (e.g., temporary loop variables, figures, axes, sub-dataframes) **must be prefixed with an underscore** (e.g., `_c`, `_fig`, `_ax`, `_df_sub`) to prevent cross-cell DAG definition collisions.
   - Only expose top-level datasets intended for downstream cell consumption.
3. **Clean Font Rendering**:
   - Avoid non-ASCII glyphs / emojis inside `matplotlib` axes titles (e.g., use `"Top 10 Broadest Skills"` instead of `"🌐 Top 10 Broadest Skills"`) to prevent Linux `DejaVu Sans` missing glyph warnings.
4. **Vectorized Numerical Performance**:
   - Always use vectorized NumPy matrix multiplication ($Q \cdot M^T$) and vectorized Max-Sim pooling for dense retrieval evaluations. Avoid iterative per-query loops over SQLite queries.

---

## 📊 Benchmark Metrics & Diagnostic Standards

### Core Evaluation Metrics
- **Hit@1 (%)**: Percentage of queries where the exact Ground Truth skill is ranked at Top-1.
- **Hit@3 (%)** / **Hit@5 (%)**: Recall within Top-3 / Top-5 candidate window.
- **MRR@10**: Mean Reciprocal Rank truncated at rank 10 ($\frac{1}{\text{rank}}$).

### Diagnostic Modules
- **Dual Transition Analysis**: Break down `ND ➔ Full` and `Full ➔ References` into:
  - *Unchanged Correct* (Green)
  - *Rescue* (Blue/Purple)
  - *Regression/Dilution* (Red/Orange)
  - *Unchanged Incorrect* (Gray)
- **Top Intruder Analysis**: Identify generic technical skills that steal Top-1 rankings due to keyword/chunk overlap.
- **Pareto Trade-off**: Evaluate Latency (ms) vs. Hit@1 to determine production-ready routing pipelines.
- **Hard Query Diagnostics**: Audit all-pipeline failures to prescribe actionable frontmatter and description improvements.
