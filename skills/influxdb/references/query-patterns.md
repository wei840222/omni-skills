# Query Patterns

## Flux Query Patterns (2.x)

- Always start with `from(bucket:)` then `|> range(start:)`. A time range is required.
- Use `|> filter(fn: (r) => r._measurement == "cpu")` for filtering.
- Use `|> aggregateWindow(every: 1h, fn: mean)` for time-based aggregation.
- Chain transforms with the `|>` pipe operator. Order matters for performance.

## InfluxQL Patterns (1.x)

- Syntax: `SELECT mean("value") FROM "measurement" WHERE time > now() - 1h GROUP BY time(5m)`
- Double quotes are for identifiers (measurements, tags, fields), single quotes for string literals.
- `GROUP BY time()` is required for time-based aggregation (needed for most dashboards).
- Use `FILL(none)` to skip empty intervals, and `FILL(previous)` to carry values forward.

## Query Performance Optimization

- Always include a time range. Unbounded queries scan all data.
- Filter on tags before fields. Tags use indexes while fields scan raw data.
- Limit results with `LIMIT` or `|> limit()`. Dashboards perform better with aggregated datasets.
- Use `GROUP BY` or `aggregateWindow` to reduce data before returning it.
