# Hypertables

- Convert a table to a hypertable: `SELECT create_hypertable('metrics', 'time')`.
- A hypertable needs a time column; use `TIMESTAMPTZ` when timestamps include time zones.
- Select a chunk interval based on workload volume and query patterns: `SELECT set_chunk_time_interval('metrics', INTERVAL '1 day')`.
- Inspect chunk sizes with `SELECT * FROM chunks_detailed_size('metrics')`.

# Distributed hypertables

- Multi-node deployments shard data across nodes and add operational complexity.
- Start on a single node unless measured capacity requires distribution.
