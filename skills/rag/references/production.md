# Production & cost — operate without folklore

**Load when** latency, drift, reindex, or spend is the question.

## Operations

- Stage-by-stage latency budget (embed query, retrieve, rerank, generate).
- Drift alarms: score-distribution shift, citation-verification failure rate, empty-result rate, refusal-rate jump.
- Reindex as a migration with a rollback index—never in place when the fingerprint changes.
- Semantic cache only for near-identical queries, keyed by tenant and filter.

## Cost levers (cheapest first)

1. Shrink `retrieve_k` / `context_k` after measuring recall.
2. Shorter embeddings / lower dimension when the model supports it.
3. Cache repeated identical queries.
4. Route easy queries away from agentic loops and hosted rerankers.
5. Change providers only after a paired eval—not from list price alone.

Absolute vendor prices move; record the figure you verified and the date in `<state_root>/artifacts/` rather than hard-coding dollars into this skill.
