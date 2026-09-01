# Performance

## Indexes and query plans

Hypertables create an index on the time partitioning column by default. Add indexes only for observed filter and ordering patterns, for example:

```sql
CREATE INDEX ON metrics (device_id, time DESC);
```

Use bounded-time predicates and select only necessary columns. Validate the effect of an index or chunk-interval change with a representative query:

```sql
EXPLAIN (ANALYZE, BUFFERS)
SELECT time, value
FROM metrics
WHERE device_id = 42
  AND time >= now() - INTERVAL '1 day'
ORDER BY time DESC
LIMIT 100;
```

## Ingest

Use multi-row `INSERT` or PostgreSQL `COPY` for bulk ingest. Measure write throughput and query latency under representative concurrency before finalizing a tuning change.
