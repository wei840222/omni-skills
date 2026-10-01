# Task routing by model class

Use class language unless the user already locked a vendor and product line. Re-check live catalogs in `sources.md` before naming a specific snapshot SKU or price.

## Coding

| Job | Prefer | Avoid |
|-----|--------|-------|
| Architecture and design decisions | Frontier / highest-reasoning class | Fast-cheap alone for irreversible design |
| Day-to-day implementation | Mid-tier (strong quality/cost balance) | Always-on frontier for routine edits |
| Parallel subtasks, scaffolding, boilerplate | Fast-cheap class | Paying frontier rates for bulk generation |
| Code review and subtle concurrency/edge bugs | Thorough / high-accuracy class | Latency-optimized models as sole reviewer |

Heuristic retained from the pre-refactor skill: mid-tier often delivers most of frontier capability at a fraction of the spend for ordinary implementation; escalate when tests, review, or user quality bar fail.

## Non-coding

| Job | Prefer | Notes |
|-----|--------|-------|
| Hard reasoning and multi-step math | Extended-thinking / frontier class | Cost is justified when mistakes are expensive |
| General assistance | User preference + mid-tier default | Public preference ranks often diverge from synthetic benchmarks |
| High-volume simple queries | Cheapest class that meets quality bar | Do not overpay; cheap and expensive can perform the same on easy asks |
| Long documents | Large-context class **or** `rag` | Context window is a hard viability constraint; chunking is not free |

## Benchmark skepticism

- Scaffolding and eval method can swing scores dramatically; do not treat a single leaderboard as truth.
- User preference rankings frequently disagree with static benchmark leaders.
- Coding-bench scores are weak predictors of messy real-world maintainability.
- Models drift; re-validate defaults on a short internal eval set, not last quarter's blog post.

## Open-weight and self-host lever

Consider open-weight / self-host when:

- data must stay on-prem or in a private VPC
- spend is dominated by steady high volume rather than rare hard jobs
- you need custom fine-tunes (hand off training detail to `fine-tuning`)

Still verify license, VRAM order-of-magnitude (`ai` guidelines), and ops cost via `ollama` or the host runtime skill—not from memory.
