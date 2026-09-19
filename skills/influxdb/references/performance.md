# Performance & Reliability

## Write Performance

- Always batch writes. Individual points incur significant HTTP overhead.
- Use Telegraf for production ingestion. It handles batching, buffering, and retries natively.
- Write to localhost if possible to reduce network latency on high throughput.
- Use `async` writes in client libraries to prevent blocking on each write.

## Retention and Downsampling

- Set retention policies or bucket durations to auto-delete old data.
- Standard pattern: Retain raw data at 10s intervals for 7 days, downsample to 1min for 30 days, and 1h for 1 year.
- InfluxDB 2.x uses **Tasks** for downsampling; 1.x uses **Continuous Queries**.
- Without downsampling, storage grows infinitely and queries degrade in performance.

## Troubleshooting Common Errors

- `"partial write: field type conflict"`: Same field written with different data types. Fix at the source.
- `"max-values-per-tag limit exceeded"`: Cardinality is too high. Redesign schema to move high-cardinality values to fields.
- `"database not found"`: 2.x uses buckets, not databases. Verify the API endpoint version.
- **Query timeouts**: Apply a narrower time range or aggregate more aggressively to reduce payload.
