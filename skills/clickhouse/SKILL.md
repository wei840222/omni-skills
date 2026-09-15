---
name: clickhouse
description: Query, optimize, and administer ClickHouse OLAP databases. Use for schema design, ORDER BY/primary-key layout, data skipping indexes, batch ingestion, slow-query tuning, system table diagnostics, TTL/retention, and MergeTree family operations with clickhouse-client.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji": "🏠","requires": {"bins": ["clickhouse-client"]},"install": [{"id": "brew","kind": "brew","formula": "clickhouse","bins": ["clickhouse-client"],"label": "Install ClickHouse (Homebrew)"}],"os": ["linux","darwin"]}'
  related-skills: '{"sql": "General SQL query patterns.","analytics": "Data analysis workflows using ClickHouse.","data-analysis": "Structured data exploration."}'
---

# ClickHouse 🏠

Real-time analytics on billions of rows. Sub-second queries. No indexes needed.


## State location

ClickHouse state may exist in `<workspace>/clickhouse/`, `<workspace>/memory/clickhouse/`, or `~/clickhouse/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/clickhouse/`, `<workspace>/memory/clickhouse/`, `~/clickhouse/`.
3. If none exists and state must be created, default to `<workspace>/clickhouse/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

On first use, read `references/setup.md` for connection configuration.

## Trigger conditions

Load this skill for OLAP analytics, log analysis, time-series data, or real-time dashboards on ClickHouse. Prefer it for schema design, query optimization, batch ingestion, system-table diagnostics, and MergeTree administration rather than generic SQL-only asks.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure.

```
<state_root>/
├── memory.md        # Connection profiles + query patterns
├── schemas/         # Table definitions per database
└── queries/         # Saved analytical queries
```

## Operational files

Read these files based on the user's specific request:

- `references/setup.md` — Read when first configuring a ClickHouse connection.
- `assets/memory-template.md` — Use to format connection profiles and state.
- `references/queries.md` — Read when writing or analyzing SQL queries.
- `references/performance.md` — Read when debugging slow queries or optimizing layout.
- `references/ingestion.md` — Read when importing data or configuring inserts.
- `references/sources.md` — Gate 6 research anchors and official documentation map.

## Core Rules

### 1. Always Specify Engine
Every table needs an explicit engine. Default to MergeTree family:

```sql
-- Time-series / logs
CREATE TABLE events (
    timestamp DateTime,
    event_type String,
    data String
) ENGINE = MergeTree()
ORDER BY (timestamp, event_type);

-- Aggregated metrics
CREATE TABLE daily_stats (
    date Date,
    metric String,
    value AggregateFunction(sum, UInt64)
) ENGINE = AggregatingMergeTree()
ORDER BY (date, metric);
```

### 2. ORDER BY is Your Index
ClickHouse has no traditional indexes. The `ORDER BY` clause determines data layout:

- Put high-cardinality filter columns first
- Put range columns (dates, timestamps) early
- Match your most common WHERE patterns

```sql
-- Good: filters by user_id, then date range
ORDER BY (user_id, date, event_type)

-- Bad: date first when you filter by user_id
ORDER BY (date, user_id, event_type)
```

### 3. Use Data Skipping Indexes
For columns not in the `ORDER BY` key, use secondary data skipping indexes (`minmax`, `set`, `bloom_filter`) to prevent full column scans:

```sql
CREATE TABLE events (
    timestamp DateTime,
    event_type String,
    user_id UInt64,
    data String,
    INDEX idx_user user_id TYPE minmax GRANULARITY 3,
    INDEX idx_data data TYPE tokenbf_v1(256, 2, 0) GRANULARITY 3
) ENGINE = MergeTree()
ORDER BY (timestamp, event_type);
```

### 4. Use Appropriate Data Types

| Use Case | Type | Why |
|----------|------|-----|
| Timestamps | `DateTime` or `DateTime64` | Native time functions |
| Low-cardinality strings | `LowCardinality(String)` | 10x compression |
| Enums with few values | `Enum8` or `Enum16` | Smallest footprint |
| Nullable only if needed | `Nullable(T)` | Adds overhead |
| IPs | `IPv4` or `IPv6` | 4 bytes vs 16+ |

### 5. Batch Inserts
Use batch inserts exclusively. ClickHouse is optimized for batch writes:

```bash
# Good: batch insert
clickhouse-client --query="INSERT INTO events FORMAT JSONEachRow" < batch.json

# Bad: individual inserts in a loop
for row in data:
    INSERT INTO events VALUES (...)
```

Minimum batch: 1,000 rows. Optimal: 10,000-100,000 rows.

### 6. Prewarm Queries with FINAL
Queries on ReplacingMergeTree/CollapsingMergeTree need `FINAL` for accuracy:

```sql
-- May return duplicates/old versions
SELECT * FROM users WHERE id = 123;

-- Guaranteed latest version
SELECT * FROM users FINAL WHERE id = 123;
```

`FINAL` has performance cost. For dashboards, consider materialized views.

### 7. Materialized Views for Speed
Pre-aggregate expensive computations:

```sql
CREATE MATERIALIZED VIEW hourly_events
ENGINE = SummingMergeTree()
ORDER BY (hour, event_type)
AS SELECT
    toStartOfHour(timestamp) AS hour,
    event_type,
    count() AS events
FROM events
GROUP BY hour, event_type;
```

### 8. Check System Tables First
Before debugging, check system tables:

```sql
-- Running queries
SELECT * FROM system.processes;

-- Recent query performance
SELECT query, elapsed, read_rows, memory_usage
FROM system.query_log
WHERE type = 'QueryFinish'
ORDER BY event_time DESC
LIMIT 10;

-- Table sizes
SELECT database, table, formatReadableSize(total_bytes) as size
FROM system.tables
ORDER BY total_bytes DESC;
```

## Common Traps

- **String instead of LowCardinality** → 10x larger storage for status/type columns
- **Wrong ORDER BY** → Full table scans instead of index lookups
- **Row-by-row inserts** → Massive part fragmentation, slow writes
- **Missing TTL** → Unbounded table growth, disk full
- **SELECT *** → Reads all columns, kills columnar advantage
- **Nullable everywhere** → Overhead + NULL handling complexity
- **Forgetting FINAL** → Stale/duplicate data in merge tables

## Performance Checklist

Before running expensive queries:

1. **Check EXPLAIN**: `EXPLAIN SELECT ...` shows execution plan
2. **Sample first**: `SELECT ... FROM table SAMPLE 0.01` for 1% sample
3. **Limit columns**: Only SELECT what you need
4. **Use PREWHERE**: Filters before reading all columns
5. **Check parts**: `SELECT count() FROM system.parts WHERE table='X'`

```sql
-- PREWHERE optimization
SELECT user_id, event_type, data
FROM events
PREWHERE date = today()
WHERE event_type = 'click';
```

## Cluster Administration

### Adding TTL for Data Retention

```sql
-- Delete old data
ALTER TABLE events
MODIFY TTL timestamp + INTERVAL 90 DAY;

-- Move to cold storage
ALTER TABLE events
MODIFY TTL timestamp + INTERVAL 30 DAY TO VOLUME 'cold';
```

### Monitoring Disk Usage

```sql
SELECT
    database,
    table,
    formatReadableSize(sum(bytes_on_disk)) as disk_size,
    sum(rows) as total_rows,
    count() as parts
FROM system.parts
WHERE active
GROUP BY database, table
ORDER BY sum(bytes_on_disk) DESC;
```

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| localhost:8123 | SQL queries | HTTP interface |
| localhost:9000 | SQL queries | Native TCP interface |

No external services contacted. All queries run against user-specified ClickHouse instances.

## Security & Privacy

**Data saved locally (with user consent):**
- Connection profiles (host, port, database) in <state_root>/memory.md
- Query patterns and schema documentation
- Authentication method preferences (password vs certificate)

**Important:** If you provide database passwords, they are stored in plain text in <state_root>/. Consider using environment variables or connection profiles managed by clickhouse-client instead.

**Operating boundaries:**
- Connect only to ClickHouse instances the user explicitly configures
- Keep all queries and state local to the user-specified instance and `<state_root>`
- Ask before storing credentials; prefer env vars or clickhouse-client profiles over plaintext passwords
