---
name: models
description: >
  Choose AI models for coding, reasoning, agents, and high-volume work with
  cost-aware, task-matched recommendations. Use when deciding which LLM class
  to run for a job based on difficulty, context window, latency, and spend.
  Prefer `ai` for live price/rank/outage facts, `ollama` for local runtime ops,
  `prompting` for prompt failure loops, and `rag`/`fine-tuning` when those paths
  are already chosen.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🤖"}'
  related-skills: '{"agi":"Deliberation quality and uncertainty calibration once the model class is chosen.","ai":"Live prices, rankings, outages, and hardware sizing instead of stale catalog memory.","embeddings":"Embedding-model and vector-index choices when retrieval quality is the bottleneck.","fine-tuning":"Training adapters when style or domain fit needs more than prompt routing.","langchain":"Multi-step chain and agent wiring after the model portfolio is set.","ollama":"Local install, Modelfile, and runtime ops after API-vs-local routing.","prompting":"Prompt failure diagnosis when the blocker is instruction design, not model tier.","rag":"Retrieval architecture when grounding needs documents rather than a stronger base model."}'
---

This skill is **stateless knowledge**: it routes work to a model *class* and cost tier. It does not store local configuration or durable user state. For live numbers (price, rank, context window, status), load `ai` and re-open the pages in `references/sources.md`.

## When to load

Load for **portfolio / task-to-model decisions**:

- which model tier for architecture, day-to-day coding, parallel scaffolding, or review
- cost vs quality tradeoffs for high-volume simple queries vs hard reasoning
- Claude Code vs Codex-class tooling fit, or plan → execute → review orchestration
- open-weight / self-host viability as a cost or privacy lever

Route away when the task is mainly:

- live price, LMSYS/OpenRouter rank, or outage facts → `ai`
- Ollama install and local runtime → `ollama`
- prompt regression / failure diagnosis → `prompting`
- full RAG system design → `rag`
- training runs / adapters → `fine-tuning`
- pure deliberation style without portfolio choice → `agi`

## When to load references

Load the smallest reference that matches the current decision; keep SKILL.md as the entry point.

| Need | File |
|------|------|
| Coding and non-coding task matching | `references/task-routing.md` |
| Cost math, context windows, batching, caching | `references/cost-and-context.md` |
| Tooling fit and plan/execute/review pattern | `references/tooling-and-orchestration.md` |
| Verified primary URLs (Gate 6) | `references/sources.md` |

Load `references/sources.md` before restating a price, context size, arena rank, or provider capability as a current fact.

## Core rules

1. **Match model to task, not brand loyalty.** No single model is best for every job.
2. **Default mid-tier; escalate only when quality fails.** Cheap tiers often match premium ones on simple work.
3. **Treat advertised input prices as incomplete.** Output tokens usually cost several times more; compute with the real input/output mix.
4. **Verify mutable facts live** via `ai` + `references/sources.md`. Do not invent current $/M, context windows, or leaderboard ranks from memory.
5. **Build verification into the pipeline.** Do not trust any model blindly; prefer plan → execute → review with stronger models on the ends when spend allows.
6. **Reassess quarterly.** Pricing, context windows, and quality drift; last month's default may already be wrong.
7. **Prefer concrete class language** (frontier / mid-tier / fast-cheap / open-weight) over unreferenced product codenames when the user did not lock a vendor.

## Decision checklist

Before recommending a tier, collect or infer:

| Input | Why it matters |
|-------|----------------|
| Task hardness | Architecture and subtle bugs need frontier; scaffolding does not |
| Context size | Long docs need large windows or a retrieval path (`rag`) |
| Volume | High-volume simple queries → cheapest viable class |
| Latency vs batch | Interactive loops vs async/batch discount paths |
| Privacy / lock-in | Self-host or open-weight when data cannot leave the boundary |
| Verification budget | Who reviews output, and with which stronger model |

Return: recommended class, cheaper fallback, escalation trigger, and what must be re-checked live.

## Completion check

- Recommendation names a **class + why**, not only a brand slogan
- Cost or context claims either cite a live source path or are marked unverified
- Related deep work is routed (`ai` / `ollama` / `prompting` / `rag` / `fine-tuning`)
- User knows the cheaper alternative and when to escalate
