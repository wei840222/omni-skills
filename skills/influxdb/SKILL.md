---
name: influxdb
description: >
  Query and write InfluxDB time-series data with schema design, line protocol,
  Flux/InfluxQL patterns, cardinality control, and retention guidance. Load when
  designing measurements/tags/fields, generating Flux or InfluxQL, diagnosing
  high-cardinality or write errors, or planning downsampling. Prefer for InfluxDB
  1.x/2.x workloads rather than general metrics definitions or full-text search.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji": "📈", "requires": {"anyBins": ["influx", "curl"]}, "os": ["linux", "darwin", "win32"], "displayName": "InfluxDB"}'
  related-skills: '{"metrics": "Define standardized metric contracts and formulas before storing series in InfluxDB.", "elasticsearch": "Full-text/search workloads; not a substitute for time-series ingestion and continuous queries.", "minio": "Object storage for long-term exports or backup artifacts adjacent to InfluxDB retention.", "docker": "Containerized InfluxDB deployment and local stack lifecycle outside query design."}'
---

# InfluxDB 📈

Design schemas, write line protocol, and query InfluxDB 1.x (InfluxQL) or 2.x (Flux) without mixing version concepts.

## When to load

Load this skill when generating Flux or InfluxQL, designing a new time-series schema, troubleshooting high cardinality or write/query failures, or planning retention and downsampling for InfluxDB.

Do not load it for generic KPI definitions (`metrics`), full-text search indexes (`elasticsearch`), or non-Influx object storage operations (`minio`).

## References

Load only the file needed for the current task:

| Topic | File |
|-------|------|
| Tags vs fields, line protocol, cardinality, schema layout | `references/schema-design.md` |
| Flux (2.x) and InfluxQL (1.x) query patterns | `references/query-patterns.md` |
| Write/read performance, retention, common errors | `references/performance.md` |

## Version differences

- **InfluxDB 2.x / Cloud**: Flux (or InfluxQL compatibility where enabled), buckets, organizations, API tokens.
- **InfluxDB 1.x**: InfluxQL, databases, retention policies, users/privileges.
- Confirm the active major version before copying queries, auth, or admin commands. Do not mix 1.x database names with 2.x bucket APIs.

## Core rules

1. **Filter on tags; aggregate on fields.** Tags are indexed; fields are not. Wrong tag/field choice cannot be changed after write without rewrite.
2. **Bound cardinality.** High-cardinality tags (unique user IDs, request IDs, unbounded free text) explode series count and memory. Prefer fields or redesign.
3. **Always bound time.** Unbounded Flux/InfluxQL scans are a common outage mode; require `range` / `WHERE time`.
4. **State precision on write.** Default timestamp precision is nanoseconds; sending epoch seconds without `precision=s|ms|us|ns` lands data in the wrong century.
5. **Separate versions in instructions.** Never present a single example that mixes Flux pipes with InfluxQL `GROUP BY time()` as if interchangeable.

## Quick checks

| Symptom | First check |
|---------|-------------|
| Writes land in year 1970/2000 | Timestamp unit vs declared `precision` |
| Series explosion / OOM on index | Tag cardinality; move unique IDs to fields |
| `field type conflict` | Same field name written as different types |
| `database not found` on 2.x | Using 1.x database API against buckets |
| Slow dashboard query | Missing time bound; filter fields before tags; missing aggregateWindow/GROUP BY time |
