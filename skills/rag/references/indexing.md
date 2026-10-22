# Indexing — filters inside the search

**Load when** choosing/sizing a store, or a metadata filter returns empty results while matches exist.

- Prefer stores that support pre-filtered or filtered-graph search. Post-filtering ANN→drop can return zero hits behind thousands of matches.
- If the store only post-filters, over-fetch by roughly `k / selectivity` and treat that multiplier as a cost line.
- Chunks inherit document permissions at ingestion; a field added later must be backfilled or those chunks are invisible/always-visible bugs.
- Memory/index sizing, quantization, and HNSW/IVF parameters belong with the chosen store; escalate to `qdrant` / `weaviate` / `elasticsearch` for API depth.
- Deduplicate near-duplicate documents at ingestion so overlap does not crowd the top-k.
