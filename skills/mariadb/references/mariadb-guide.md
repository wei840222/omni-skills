# MariaDB Engineering Guide

Operational depth for `skills/mariadb`. Load when designing schema, writing queries, tuning, clustering, or recovering MariaDB.

## Character set

- Always use `utf8mb4` for tables and connections—full Unicode including emoji.
- `utf8mb4_unicode_ci` for proper linguistic sorting; `utf8mb4_bin` for byte comparison.
- Set connection charset: `SET NAMES utf8mb4` or equivalent in the connection string/DSN.
- Collation mismatch in JOINs forces conversion and can disable index use—align joined columns.

## Indexing

- TEXT/BLOB columns need prefix length: `INDEX (description(100))` (tune length to selectivity and key limits).
- Composite index order matters—`(a, b)` serves `WHERE a=?` and `WHERE a=? AND b=?`, but not `WHERE b=?` alone.
- Foreign keys typically auto-create an index on the child table—verify with `SHOW INDEX FROM t`.
- Covering indexes: include all SELECT columns needed for the hot path to avoid table lookup.
- Confirm plans with `EXPLAIN` / `EXPLAIN ANALYZE` rather than assuming the optimizer picked the intended index.

## Sequences

- `CREATE SEQUENCE seq_name` for guaranteed unique IDs across tables or pre-insert allocation.
- `NEXT VALUE FOR seq_name` to fetch the next value—sequence advancement survives transaction rollback differently from failed auto-increment assumptions; design IDs with that in mind.
- Prefer sequences when the application must know the ID before insert or share a counter across tables.
- `SETVAL(seq_name, n)` (or documented equivalents) to reset during controlled migrations only.

## System versioning (temporal tables)

- `ALTER TABLE t ADD SYSTEM VERSIONING` tracks historical row versions.
- Query past state: `FOR SYSTEM_TIME AS OF '2024-01-01 00:00:00'`.
- Change windows: `FOR SYSTEM_TIME BETWEEN start AND end`.
- Invisible `row_start` / `row_end` (implementation names may vary by version) store validity; do not treat them as ordinary app columns without reading current docs.
- Plan retention/purging explicitly—unbounded history grows storage and backup size.

## JSON handling

- `JSON_VALUE(col, '$.key')` extracts a scalar (NULL when missing, depending on path/options).
- `JSON_QUERY(col, '$.obj')` extracts object/array fragments.
- `JSON_TABLE()` converts JSON arrays to relational rows for unnesting.
- `JSON_VALID()` before insert when the column is not a strict JSON type or input is untrusted.
- Prefer relational columns for hot filters; keep JSON for flexible attributes.

## Galera cluster

- Multi-primary: all nodes may accept writes, but same-row conflicts cause certification failure/rollback.
- `wsrep_sync_wait = 1` (or appropriate bitmask) before critical reads when the session must see its own/causal writes.
- Keep transactions small—large multi-row transactions raise conflict probability and replication lag risk.
- Prefer odd `wsrep_cluster_size` for clearer quorum; understand split-brain avoidance is about quorum and fencing, not magic.
- Monitor flow control and queue sizes before blaming application SQL alone.

## Window functions

- `ROW_NUMBER() OVER (PARTITION BY x ORDER BY y)` for ranking within groups.
- `LAG(col, 1) OVER (ORDER BY date)` for previous-row comparisons.
- `SUM(amount) OVER (ORDER BY date ROWS UNBOUNDED PRECEDING)` for running totals.
- Prefer readable CTEs (`WITH cte AS (...)`) for multi-step analytical queries; verify memory/temp usage on large sets.

## Thread pool

- Enable with `thread_handling=pool-of-threads` when high connection counts thrash under one-thread-per-connection.
- Size `thread_pool_size` around CPU cores for CPU-bound work; raise carefully for I/O-bound mixes.
- Reduces context switching with many concurrent connections; measure before/after with `SHOW STATUS LIKE 'Threadpool%'` (and server-specific status).
- Client-side pooling still matters—server thread pool is not a substitute for bounded app pools.

## Storage engines

- **InnoDB** (default for most app data): ACID transactions, row locking, crash recovery.
- **Aria**: crash-safe option often used for internal/temporary workloads as a MyISAM replacement path—confirm fit before using for durable app tables.
- **MEMORY**: fast, volatile caches; data lost on restart.
- Inspect with `SHOW TABLE STATUS WHERE Name='table'` and `SHOW ENGINES`.

## Locking

- `SELECT ... FOR UPDATE` locks qualifying rows until commit—keep transactions short.
- `LOCK TABLES t WRITE` is coarse and blocks other sessions; prefer InnoDB row locks for app paths.
- Deadlock detection rolls back one transaction—application must retry safely.
- `innodb_lock_wait_timeout` defaults are often ~50s; lower for interactive APIs that should fail fast.

## Query optimization

- `EXPLAIN` for plan shape; `EXPLAIN ANALYZE` (when supported on the running version) for actual timings.
- `optimizer_trace` (`SET optimizer_trace='enabled=on'`) for deep optimizer dumps on stubborn plans.
- `FORCE INDEX (idx)` only after measuring a real mischoice—last-mile override, not default style.
- `STRAIGHT_JOIN` forces join order as a last resort; document why and re-test after upgrades.

## Backup and recovery

- `mariadb-dump --single-transaction` for consistent logical backups of InnoDB without long table locks (still watch DDL and non-InnoDB tables).
- `mariadb-backup` (MariaBackup) for hot physical InnoDB backup; incremental flows are supported—practice restore.
- Binary logs enable point-in-time recovery: apply with `mysqlbinlog` / `mariadb-binlog` into the server per current tooling.
- A backup is incomplete until a restore has been tested on a non-production target.

## Common errors

- **Too many connections** — raise carefully, fix leaks, use pooling; inspect `max_connections` and processlist.
- **Lock wait timeout exceeded** — find blockers via `SHOW ENGINE INNODB STATUS` / performance_schema; shorten critical sections.
- **Row size too large** — wide rows, many VARCHAR, or off-page pointer limits; normalize or use TEXT/BLOB/JSON appropriately.
- **Duplicate entry for key** — unique constraint conflict; use deliberate `ON DUPLICATE KEY UPDATE` / retry logic only when upsert semantics are intended.
