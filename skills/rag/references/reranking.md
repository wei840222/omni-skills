# Reranking — precision stage

**Load when** recall is fine but precision is bad.

- Bi-encoder = recall; cross-encoder / dedicated reranker = precision.
- Retrieve wide (`retrieve_k`), rerank to `context_k`. Default 30 → 5.
- A reranker over a top-5 list can only reorder five items—documents never retrieved stay missing.
- Past roughly 100 candidates, recall gains flatten while rerank latency rises linearly; cap by `latency_budget_ms`.
- Change the reranker as a single variable and measure with a paired golden-set run (`references/evaluation.md`).
