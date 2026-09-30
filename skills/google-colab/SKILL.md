---
name: google-colab
description: >
  Run Google Colab notebooks for Python and machine learning with reproducible
  runtimes, data pipelines, debugging workflows, and experiment discipline. Use
  when the user needs Colab setup, GPU/TPU runtime pinning, Drive/GCS data IO,
  notebook cell contracts, disconnect recovery, or reproducible experiment logs;
  not for pure local Jupyter without Colab, or generic non-notebook ML theory.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📓","requires":{"bins":["curl","jq"]}}'
  related-skills: '{"api":"Design resilient API contracts for notebook data and model integrations.","automate":"Convert proven notebook steps into reliable automation after Colab reproducibility is locked.","gcp":"Plan GCS, IAM, and Google Cloud service boundaries used by Colab workloads.","numpy":"Improve numerical computation patterns inside Colab cells.","pandas":"Build tabular transforms and schema validation used before Colab training runs."}'
---

## State location

Google Colab operational state may exist in `<workspace>/google-colab/`, `<workspace>/memory/google-colab/`, or `~/google-colab/`.
Before reading or writing state, resolve `<state_root>` once for this invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/google-colab/`, `<workspace>/memory/google-colab/`, `~/google-colab/`.
3. If none exists and persistent state must be created, default to `<workspace>/google-colab/`.

Use only the selected `<state_root>` for every state operation in this skill. When more than one candidate exists, choose the highest-precedence path, report the conflict, and leave other copies unchanged until the user chooses a migration path. Never invent `<workspace>` from the shell cwd.

## Setup

On first use, load `references/setup.md` and align activation behavior, cost boundaries, and data-access rules before proposing notebook changes.

## When to load

Load this skill when the user needs Google Colab notebook work that must be reproducible rather than one-off trial and error. Handle runtime setup, package hygiene, Drive/GCS data flows, debugging failures, and experiment tracking.

Do not load as the primary skill for pure local Jupyter without Colab, generic non-notebook ML theory, or full GCP platform architecture (`gcp`).

## Architecture

Memory lives in `<state_root>/`. Load `assets/memory-template.md` when initializing or updating durable status values.

```text
<state_root>/
|-- memory.md                   # Activation preferences, constraints, and current goals
|-- notebooks.md                # Notebook registry with owners and objective per notebook
|-- runtimes.md                 # Runtime choices, dependency pins, and restart history
|-- datasets.md                 # Data source map, mount paths, and validation notes
|-- incidents.md                # Error timelines, root causes, and fixes
`-- experiments.md              # Hypotheses, metrics, and reproducibility evidence
```

## Quick Reference

Load the smallest relevant file for the active task:

| Topic | File | Load when |
|-------|------|-----------|
| Setup and activation behavior | `references/setup.md` | First use, consent, or missing state |
| Memory and local templates | `assets/memory-template.md` | Initializing or updating durable notes |
| Notebook structure and cell contracts | `references/notebook-architecture.md` | Designing or restructuring notebooks |
| Runtime setup, pinning, and restart recovery | `references/runtime-playbook.md` | Choosing GPU/TPU tier or recovering disconnects |
| Data import, export, and schema checks | `references/data-io-patterns.md` | Mounting Drive/GCS or validating datasets |
| Debugging triage and failure recovery | `references/debugging-runbook.md` | Runtime, data, model, or eval failures |
| Experiment log format and promotion rules | `assets/experiment-log-template.md` | Recording or comparing significant runs |
| Official sources and Gate 6 notes | `references/sources.md` | Verifying Colab facts, runtimes, or IO docs |

## Requirements

- For diagnostics and lightweight API checks: `curl`, `jq`
- For notebook execution: Google account with Colab access
- For dataset mounting: explicit permission for Drive, GCS, or external endpoints

Never ask users to paste API keys, OAuth refresh tokens, or private dataset credentials into chat. Prefer Colab secrets, secure mounts, or environment variables the host already controls.

## Data Storage

Local operational notes stay in `<state_root>/`:

- notebook inventory with objective, owner, and current status
- runtime and dependency decisions with pinned versions
- dataset and schema validation history
- experiment outcomes and unresolved risks

Optional state files are created only when the matching feature is needed. Do not pre-create empty trees.

## Core Rules

### 1. Start with Objective, Constraints, and Exit Criteria

Before writing notebook steps, identify:

- objective: prototype, benchmark, fine-tuning, teaching, or production prep
- constraints: runtime tier, budget, execution time, and data availability
- exit criteria: metric threshold, artifact output, or decision checkpoint

Without explicit exit criteria, notebook sessions drift and become hard to evaluate.

### 2. Design Notebook Cells as Contracts

Each cell should have a contract:

- inputs required and where they come from
- deterministic output shape and validation check
- failure mode and fallback behavior

Treat hidden state between cells as technical debt and document every state dependency.

### 3. Pin Runtime and Dependency State

Any runnable plan must define:

- Python version and runtime class (CPU, T4, L4, A100, or TPU when relevant and available)
- pinned package versions for non-standard libraries
- rehydration steps after runtime disconnect or restart

Never assume a fresh runtime matches previous package state. Re-run a validation cell after reconnect.

### 4. Validate Data Paths and Schema Before Training or Evaluation

Before expensive operations:

- verify mount success and path existence
- sample and validate schema and null patterns
- block execution when split boundaries or label columns are ambiguous

Fast schema checks prevent long failed runs and invalid metrics.

### 5. Make Cost and Time Guardrails Explicit

For any medium or high-cost run:

- estimate runtime duration and checkpoint intervals
- define early-stop conditions and budget cutoff
- recommend a smaller dry-run dataset before full execution

No full-scale run should start without budget and cutoff rules.

### 6. Triage Failures by Layer, Not by Guessing

Debug in layers:

1. runtime health and package import layer
2. data loading and preprocessing layer
3. model logic and training loop layer
4. evaluation and artifact export layer

Layered triage shortens incident resolution and avoids random patching.

### 7. Log Reproducibility Evidence in Every Significant Run

For each meaningful run, capture:

- notebook id or link, runtime class, seed, and dependency snapshot
- dataset version or timestamp and split method
- primary metric result and whether exit criteria passed

If reproducibility evidence is missing, treat conclusions as provisional.

## Common Traps

Prefer the recovery path next to each failure mode instead of only naming the anti-pattern.

- Installing packages ad hoc across cells without pins → results differ after runtime reconnect
- Using absolute local paths copied from old sessions → file not found during replay
- Training before schema and null validation → wasted GPU time and misleading metrics
- Mixing exploratory and production cells in one notebook → brittle execution order
- Treating cached outputs as fresh ground truth → stale evaluation and wrong decisions
- Ignoring random seeds and data splits → impossible to compare experiment outcomes
- Exporting artifacts without metadata → model files cannot be audited later

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://colab.research.google.com | Notebook execution metadata and selected runtime actions | Interactive notebook execution and runtime control |
| https://www.googleapis.com | File identifiers and requested object payloads | Google Drive and related API interactions |
| https://storage.googleapis.com | Dataset or artifact object requests | Read or write objects in Google Cloud Storage |
| https://pypi.org | Package names and version requests | Python dependency installation and version resolution |

No other data should be sent externally unless the user explicitly configures additional systems.

## Security & Privacy

Data that leaves your machine:

- notebook payloads and runtime metadata required by Colab services
- selected file and object metadata required for Drive or GCS operations
- package lookup requests for dependency installation

Data that stays local:

- workflow memory and decision logs under `<state_root>/`
- incident notes, experiment summaries, and validation evidence

This skill does NOT:

- request or store raw secrets in conversation text
- execute high-cost runs without explicit guardrails
- bypass user-defined data boundaries or compliance rules

## Trust

This skill relies on Google Colab, Google APIs, and package repositories used during notebook setup. Only install and run it if you trust those systems with your code and data.
