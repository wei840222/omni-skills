# Cost reality and context windows

## Incomplete sticker prices

- Output tokens commonly cost several times input tokens; advertised **input** $/M is not the full story.
- Compute unit cost from the **actual** input/output ratio of the workflow, not a marketing mix.
- Batch / async APIs often discount non-interactive work—use them when latency allows.
- Prompt caching reduces repeated system/context cost when the host and provider support it; confirm on the live docs page before promising savings.

## Context window as a product constraint

- If the working set does not fit, quality collapses or you pay for naive chunking.
- Prefer a large-context class when the user must keep a whole long document in one shot.
- Prefer `rag` when the corpus is large, multi-doc, or needs citations—not a bigger window alone.
- Never invent a current context size; open the provider catalog or OpenRouter model card first (`sources.md`).

## Practical spend rules

1. Default mid-tier for most tasks.
2. Run a cheaper pilot on a sample before locking an expensive default.
3. Track **workflow** cost (plan + tools + retries + review), not only per-token list price.
4. Escalate to frontier only when quality, safety, or review load clearly suffers.
5. Reassess defaults when provider pricing or quality notices land (see `ai` status/pricing sources).

## What not to claim without a live source

- Exact $/M input or output for any named model
- Exact context window or rate limit
- Arena rank or "best model" absolute statements
- Guaranteed batch-discount percentages for a specific account tier
