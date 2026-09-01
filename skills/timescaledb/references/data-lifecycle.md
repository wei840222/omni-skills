# Data lifecycle

## Compression

- Enable compression on historical chunks using the syntax supported by the installed TimescaleDB version.
- Add a compression policy only after confirming that historical data no longer needs row-level changes.

## Retention

- Use `SELECT add_retention_policy('metrics', INTERVAL '90 days')` to drop chunks older than the retention interval.
- Confirm the hypertable, retention period, and recovery plan before adding a retention policy.
