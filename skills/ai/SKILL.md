---
name: ai
description: >
  Answer AI product, pricing, ranking, hardware, and engineering questions with
  live verification instead of stale training data. Use when the user asks about
  current model prices, LMSYS/OpenRouter standings, outages, hallucination
  controls, RAG vs fine-tuning, local VRAM order-of-magnitude, API vs local fit,
  or token counting; prefer `models` for multi-model task routing, `ollama` for
  local runtime ops, `rag`/`fine-tuning` for deep retrieval or training work,
  and `prompting` for prompt failure diagnosis.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🤖"}'
  related-skills: '{"models":"Task-to-model and cost-tier selection beyond generic AI Q&A.","ollama":"Local Ollama install, Modelfile, and runtime ops after API-vs-local choice.","rag":"Retrieval architecture, chunking, and evaluation when RAG is the chosen path.","fine-tuning":"Training data, adapters, and eval loops when style/domain fit needs fine-tuning.","prompting":"Prompt failure diagnosis and iteration when the blocker is instruction design.","agi":"Deliberation and uncertainty calibration when the need is reasoning quality, not AI product facts.","embeddings":"Embedding model and vector-index choices supporting RAG stacks.","langchain":"Multi-step chain/agent wiring after the AI approach is chosen."}'
---

## When to load

Load this skill for **AI product and engineering Q&A** that must not trust stale training data: live pricing, public rankings, provider outages, hallucination controls, RAG-vs-fine-tune triage, rough local hardware sizing, API vs local fit, and token counting.

Do **not** load as the primary skill for multi-model portfolio routing (`models`), Ollama install/runtime (`ollama`), full RAG system design (`rag`), training runs (`fine-tuning`), prompt regression loops (`prompting`), or pure deliberation style (`agi`).

## State location

Optional AI Q&A notes (preferred live URLs, verified snapshots, hardware inventory) may live under `<workspace>/ai/`, `<workspace>/memory/ai/`, or `~/ai/`. Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/ai/`, `<workspace>/memory/ai/`, `~/ai/`.
3. If none exists and persistent state must be created, default to `<workspace>/ai/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path, report the conflict, and leave other copies unchanged.

Use only the selected `<state_root>` for every state operation in this skill. Never invent `<workspace>` from the shell cwd. Keep API keys, account tokens, and private eval corpora **out of the skill package and out of git**.

```text
<state_root>/
|-- verified-facts.md   # Dated snapshots of prices/rankings the user asked to keep
|-- hardware.md         # Local GPU/RAM notes the user supplied
`-- links.md            # Preferred status and docs URLs for this workspace
```

One-off answers may stay conversational. Before creating or changing files under `<state_root>/`, explain the planned write and ask for confirmation.

## Routing

| Need | Load |
|------|------|
| Live price / rank / outage checks and source map | `references/sources.md` |
| Hallucination, RAG vs FT, hardware, API vs local, tokens | `references/guidelines.md` |

## Core rules

1. **Verify before quoting mutable facts.** Prices, context windows, rate limits, arena ranks, and status change often. Open the live page (or ask the user to) before stating a number.
2. **Prefer primary aggregators and status pages** listed in `references/sources.md` over memory.
3. **Give operational advice, not slogans.** Hallucination, RAG/FT, and hardware answers must include concrete controls or order-of-magnitude ranges with caveats (see `references/guidelines.md`).
4. **Count tokens with a tokenizer**, not character heuristics, when the user needs a real budget.
5. **Route deep work** to related skills once the triage answer is clear.

## Completion check

Before answering, confirm: mutable claims were verified or explicitly marked unverified; guidance matches `references/guidelines.md`; related deep work is routed; no secrets were written into the skill tree.