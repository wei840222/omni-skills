---
name: timescaledb
description: Use when designing or operating TimescaleDB hypertables, time-bucket queries, continuous aggregates, retention, compression, or time-series performance tuning.
metadata:
  openclaw: '{"emoji":"⏱️","requires":{"anyBins":["psql"]}}'
---

## Workflow

1. Identify the workload: target table, time column, ingest pattern, query time range, retention need, and whether old rows still change.
2. Load the reference for the requested operation, verify version-sensitive syntax in `references/sources.md`, and prepare SQL for the intended database context.
3. For data-removal or storage-policy changes, confirm the hypertable, threshold, and recovery plan before executing; then verify the resulting object, policy, or query plan.

## Quick reference

| Resource | Load when |
| --- | --- |
| `references/architecture.md` | Creating hypertables, choosing chunk intervals, or assessing distributed hypertables. |
| `references/querying.md` | Writing `time_bucket` queries or setting up continuous and real-time aggregate views. |
| `references/data-lifecycle.md` | Managing data retention policies or enabling compression policies for historical data. |
| `references/performance.md` | Optimizing write throughput or tuning read latency with indexes. |
| `references/sources.md` | Verifying installed-version syntax or current behavior against official Timescale documentation. |
