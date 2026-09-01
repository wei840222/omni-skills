# Performance

## Indexing

- Hypertables create an index on the time partitioning column by default.
- Add a composite index for observed filter patterns, for example `CREATE INDEX ON metrics (device_id, time DESC)`.

## Ingest and query patterns

- Use multi-row `INSERT` or `COPY` for bulk ingest.
- Add bounded time ranges to queries and select only needed columns.
- Use `EXPLAIN (ANALYZE, BUFFERS)` to measure the effect of an index or chunk-interval change.
