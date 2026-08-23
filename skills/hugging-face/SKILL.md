---
name: hugging-face
description: "Discover, evaluate, and run Hugging Face models and datasets. Triggers when the user asks to find a model, compare models, run inference via HF API, or search datasets."
compatibility: "linux, darwin, win32"
metadata:
  openclaw: '{"emoji":"HF","requires":{"bins":["curl","jq"],"env":["HF_TOKEN"]}}'
  related-skills: '{"ai": "general AI strategy and model-selection framing", "api": "API-first integration patterns and HTTP debugging", "data-analysis": "dataset inspection and quality interpretation", "data": "structured data workflows and extraction patterns", "code": "implementation support for scripts and adapters"}'
---

## State location

Memory and reusable artifacts live in `<state_root>/`.
- Candidate locations: `.hugging-face/`, `~/.hugging-face/`
- Lookup order: workspace-first, then global fallback.
- Creation: Create the directory if it does not exist upon first setup.

## Setup

On first use, read `scripts/setup.md` for integration guidelines and local memory initialization.

## When to Use

User needs to find the right Hugging Face model, dataset, or Space for a concrete task and move from browsing to reliable execution.
Agent handles discovery, filtering, license checks, quick benchmarking, and integration-ready inference plans.

## Architecture

Memory and reusable artifacts live in `<state_root>/`. See `references/memory-template.md` for structure and status fields.

```text
<state_root>/
|- memory.md          # Stable context, priorities, and defaults
|- shortlists.md      # Candidate models and datasets by use case
|- evaluations.md     # Benchmark runs, winners, and caveats
|- endpoints.md       # Approved endpoints and auth notes
`- exports/           # Saved outputs and comparison snapshots
```

## Quick Reference

Load only one focused file at a time to keep context small and decisions explicit.

| Topic | File | When to load | How to load |
|-------|------|--------------|-------------|
| Setup process | `scripts/setup.md` | User explicitly asks to initialize memory or set up the skill. | `cat scripts/setup.md` |
| Memory template | `references/memory-template.md` | Creating or updating the state files. | `cat references/memory-template.md` |
| Model and dataset discovery | `references/discovery.md` | Searching for models or datasets via HF Hub. | `cat references/discovery.md` |
| Inference execution patterns | `references/inference.md` | Running models via Inference API or local code. | `cat references/inference.md` |
| Evaluation rubric and scoring | `references/evaluation.md` | Comparing candidates or running benchmarks. | `cat references/evaluation.md` |
| Common failures and recovery | `references/troubleshooting.md` | When encountering errors like 401, 403, or rate limits. | `cat references/troubleshooting.md` |
| Domain knowledge | `references/hugging-face-domain.md` | When needing facts about HF API structure or tools. | `cat references/hugging-face-domain.md` |

## Core Rules

### 1. Lock Objective and Constraints First
Before selecting any artifact, confirm task type, latency budget, cost boundary, and deployment target.

Use this minimum scope packet:
- Task type: chat, generation, embedding, classification, vision, or speech
- Quality priority: best quality, best speed, or balanced
- Runtime constraints: CPU only, specific GPU class, or hosted endpoint
- Compliance constraints: license, region, or private data limits

### 2. Separate Discovery from Execution
Create a shortlist of at least three candidates, then execute only on finalists that pass compatibility and license checks.

### 3. Validate License and Access Before Recommendation
For every candidate, verify license, gated access status, model size, and framework compatibility.

If any of these are unknown, mark the candidate as provisional and seek an alternative for production recommendation.

### 4. Benchmark with a Deterministic Mini Suite
Use the same prompt set and output checks across candidates so results are comparable.

Minimum benchmark set:
- One typical request
- One edge-case request
- One failure-prone request

### 5. Minimize External Data
Send only what is required for the selected endpoint.

Only send the minimal text necessary for the task in request payloads. Keep credentials and local paths out of payloads.

### 6. Use a Fallback Ladder
If the preferred model fails, apply ordered fallback:
1. Retry same endpoint with smaller payload
2. Switch to a compatible backup model
3. Switch to local-only workflow if available

### 7. Keep Runs Reproducible
Log selected model id, endpoint, key parameters, and evaluation result in local memory so future runs are consistent and auditable.

## Common Traps

- Picking the highest download count as the only criterion -> often misses license, latency, or domain fit.
- Ignoring gated model requirements -> integration fails at runtime due to access restrictions.
- Comparing models with different prompts -> quality conclusions become unreliable.
- Sending full user context to inference endpoints -> unnecessary privacy exposure.
- Skipping fallback design -> workflows fail hard on transient endpoint errors.

## External Endpoints

Use discovery endpoints before inference so candidate selection remains explainable and reproducible.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| `https://huggingface.co/api/models` | Search terms, filter parameters | Discover model candidates |
| `https://huggingface.co/api/datasets` | Search terms, filter parameters | Discover dataset candidates |
| `https://huggingface.co/api/spaces` | Search terms, filter parameters | Discover runnable Spaces |
| `https://api-inference.huggingface.co/models/{model_id}` | Prompt or task input payload, selected model id, auth token | Run hosted inference |

Only the exact query parameters and payloads specified above are sent externally.

## Security & Privacy

**Data that leaves your machine:**
- Search terms and filter inputs sent to Hugging Face discovery APIs.
- Inference payloads sent to Hugging Face Inference API when execution is requested.

**Data that stays local:**
- Preferences, shortlists, evaluation notes, and endpoint decisions in `<state_root>/`.

**This skill does NOT:**
- Exfiltrate local files by default.
- Send undeclared network requests.
- Store raw secrets in local notes.
- Modify its own skill definition file.

## Trust

By using this skill, selected request data is sent to Hugging Face services. Only install if you trust Hugging Face with the inputs you choose to process.
