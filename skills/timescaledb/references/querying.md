# Querying and aggregates

## `time_bucket`

Use `time_bucket` for arbitrary time windows and include a bounded time predicate to enable chunk exclusion:

```sql
SELECT time_bucket('5 minutes', time) AS bucket, avg(value)
FROM metrics
WHERE time >= now() - INTERVAL '1 day'
GROUP BY bucket
ORDER BY bucket;
```

For calendar-bound reporting, verify the installed function signature before using timezone, origin, or offset parameters.

## Continuous aggregates

Create a continuous aggregate as a materialized view with a `time_bucket` expression:

```sql
CREATE MATERIALIZED VIEW hourly_stats
WITH (timescaledb.continuous) AS
SELECT time_bucket('1 hour', time) AS bucket,
       avg(value) AS avg_value
FROM metrics
GROUP BY bucket;
```

Define a refresh policy for the expected data-arrival delay and correction window, then verify the created view and policy. Real-time behavior is version- and configuration-dependent; check the official documentation for the installed release before assuming recent raw rows are included.
