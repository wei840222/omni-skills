# Sources — clickhouse

Gate 6 research anchors for ClickHouse OLAP operations. Prefer primary ClickHouse docs over secondary blogs. Re-verify engine, settings, and syntax against the target server version before quoting exact DDL.

Last checked: 2026-09-15

## Engines, MergeTree, and table design

- [MergeTree family](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family) — primary storage engines, ORDER BY layout, and part merges.
- [Creating tables](https://clickhouse.com/docs/en/sql-reference/statements/create/table) — ENGINE, ORDER BY, PARTITION BY, and INDEX clauses.
- [Data skipping indexes](https://clickhouse.com/docs/en/optimize/skipping-indexes) — minmax, set, bloom_filter / tokenbf secondary indexes.
- [Data types](https://clickhouse.com/docs/en/sql-reference/data-types) — DateTime/DateTime64, LowCardinality, Enum, IPv4/IPv6, Nullable trade-offs.

## Query performance and diagnostics

- [EXPLAIN](https://clickhouse.com/docs/en/sql-reference/statements/explain) — plan inspection before expensive analytics.
- [PREWHERE](https://clickhouse.com/docs/en/sql-reference/statements/select/prewhere) — early column filters for wide tables.
- [system.query_log](https://clickhouse.com/docs/en/operations/system-tables/query_log) — finished query latency, rows read, memory.
- [system.parts](https://clickhouse.com/docs/en/operations/system-tables/parts) — part count, bytes on disk, active parts.
- [system.processes](https://clickhouse.com/docs/en/operations/system-tables/processes) — currently running queries.

## Ingestion and writes

- [INSERT](https://clickhouse.com/docs/en/sql-reference/statements/insert-into) — batch-oriented writes and formats.
- [Async inserts](https://clickhouse.com/docs/en/optimize/asynchronous-inserts) — server-side buffering for smaller client batches.
- [S3 table function](https://clickhouse.com/docs/en/sql-reference/table-functions/s3) — object-storage reads (Parquet/Arrow and related formats).
- [Kafka table engine](https://clickhouse.com/docs/en/engines/table-engines/integrations/kafka) — streaming ingest patterns.

## TTL, FINAL, and materialized views

- [TTL](https://clickhouse.com/docs/en/engines/table-engines/mergetree-family/mergetree#table_engine-mergetree-ttl) — retention and volume moves.
- [FINAL modifier](https://clickhouse.com/docs/en/sql-reference/statements/select/from#final-modifier) — latest-version reads on collapsing/replacing engines and cost caveats.
- [Materialized views](https://clickhouse.com/docs/en/materialized-view) — pre-aggregation for dashboards.

## Interfaces and client setup

- [clickhouse-client](https://clickhouse.com/docs/en/interfaces/cli) — native CLI workflows used by this skill.
- [HTTP interface](https://clickhouse.com/docs/en/interfaces/http) — default HTTP endpoint expectations (8123).
- [Native interface](https://clickhouse.com/docs/en/interfaces/tcp) — native TCP endpoint expectations (9000).
