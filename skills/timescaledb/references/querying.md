# Querying and aggregates

## `time_bucket`

- Use `time_bucket('1 hour', time)` to group by arbitrary intervals.
- Include a time predicate so PostgreSQL can exclude irrelevant chunks.

## Continuous aggregates

- Define a materialized view with `WITH (timescaledb.continuous)` to precompute an aggregate.
- Add a refresh policy and query the aggregate view for recurring analytical queries.
- Real-time aggregate behavior combines materialized and recent data when enabled for the installed configuration.
