# Data lifecycle

## Compression

Confirm the installed TimescaleDB version before enabling historical-data compression because product terminology and supported storage syntax can differ by release. Identify late-arriving updates and deletes, test the change on representative chunks, then add an automated policy only after confirming the target hypertable and age threshold.

## Retention

A retention policy drops complete chunks older than the configured interval. Verify the target hypertable, interval, downstream consumers, and backup/recovery plan before adding one:

```sql
SELECT add_retention_policy('metrics', INTERVAL '90 days');
```

Review the policy in the TimescaleDB information views after creation. A completed drop requires restoring data from backup; changing a policy does not recreate dropped chunks.
