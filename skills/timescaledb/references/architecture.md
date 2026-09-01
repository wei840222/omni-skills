# Hypertables

## Create and inspect

A hypertable partitions a PostgreSQL table into time-based chunks. Convert a table only after confirming its time column and the installed TimescaleDB API syntax:

```sql
SELECT create_hypertable('metrics', 'time');
```

Verify that the target became a hypertable with the TimescaleDB information view:

```sql
SELECT *
FROM timescaledb_information.hypertables
WHERE hypertable_name = 'metrics';
```

## Chunk intervals

Start with the default chunk interval unless measured ingest and query behavior needs a change. Select an interval for the expected data volume and bounded-time query pattern, then inspect resulting chunk sizes:

```sql
SELECT set_chunk_time_interval('metrics', INTERVAL '1 day');
SELECT * FROM chunks_detailed_size('metrics');
```

Compare representative query plans and ingest behavior after changing an interval. Existing chunks retain their current boundaries; check the installed-version documentation before relying on changed interval behavior.

## Distributed hypertables

Use multi-node hypertables only when measured capacity or availability requirements exceed a single-node deployment. Confirm edition and version support before planning a distributed migration because data-node placement adds operational complexity.
