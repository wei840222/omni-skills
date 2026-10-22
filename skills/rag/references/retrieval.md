# Retrieval — hybrid by default

**Load when** exact identifiers miss, hybrid fusion needs tuning, or near-duplicates dominate.

- Dense + sparse (BM25) by default. Cosine and BM25 live on different scales—fuse by **rank**, not raw score.
- Reciprocal rank fusion: `score(d) = Σ_i 1 / (60 + rank_i(d))` (rank constant 60 is the published default; see `references/sources.md`).
- Move to a tuned weighted sum only once a labeled set exists to fit the weight.
- Pure dense loses part numbers, error codes, and surnames users paste.
- Query rewrite before embedding for multi-turn (pronouns, ellipsis)—see `references/conversation.md`.
- Optional MMR after retrieval to reduce near-duplicate crowding.
