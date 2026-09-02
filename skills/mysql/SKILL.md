---
name: mysql
description: Write correct MySQL queries utilizing proper character sets, indexing, transactions, and production patterns. Use when modifying or querying a MySQL database.
metadata:
  openclaw: '{"emoji": "\ud83d\udc2c","requires": {"bins": ["mysql"]}}'
  related-skills: '{"sqlite": "Use when the workload fits embedded/local SQLite instead of a server MySQL instance.", "mariadb": "Use when the target is MariaDB-specific syntax or operational differences from MySQL.", "timescaledb": "Hand off time-series hypertable and continuous-aggregate work on PostgreSQL/Timescale.", "sql": "Use for dialect-agnostic SQL patterns before specializing to MySQL."}'
---
## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Index design deep dive | `references/indexes.md` | When designing schema and indexes |
| Transactions and locking | `references/transactions.md` | When dealing with concurrent writes |
| Query optimization | `references/queries.md` | When rewriting slow queries |
| Production config | `references/production.md` | When configuring database server |
| Domain knowledge | `references/domain-knowledge.md` | When verifying high-level MySQL operating rules |

## Workflow

1. Confirm engine and version (`SHOW VARIABLES LIKE 'version%'; SHOW TABLE STATUS`). Prefer InnoDB for application data.
2. Enforce `utf8mb4` at schema and connection layer before writing queries that store text.
3. Design indexes for the actual predicates; use prefix lengths for TEXT/BLOB and generated columns for expressions when needed.
4. Wrap multi-statement writes in explicit transactions; verify isolation and lock order under concurrency.
5. Validate plans with `EXPLAIN` / `EXPLAIN ANALYZE` (8.0.18+) before shipping slow-path changes.
6. Load the matching reference file only when the current task needs that depth.

## Character Set Traps

- Prefer `utf8mb4`; MySQL `utf8` is a 3-byte alias and cannot store emoji.
- Use `utf8mb4_unicode_ci` for case-insensitive sorting; `utf8mb4_bin` for exact byte comparison.
- Keep collation consistent across joined columns—mismatches force conversions and hurt index use.
- Set connection charset to match (`SET NAMES utf8mb4` or DSN parameters).
- utf8mb4 indexes are wider; use prefix indexes when key length limits appear.

## Index Differences from PostgreSQL

- No partial indexes—index definitions cannot include a `WHERE` filter.
- Expression indexes need generated columns before MySQL 8.0.13.
- TEXT/BLOB indexes require an explicit prefix length: `INDEX (description(100))`.
- Covering columns belong in the index itself (`INDEX (a, b, c)`); there is no INCLUDE clause.
- Foreign keys auto-create indexes only on InnoDB—verify the engine first.

## UPSERT Patterns

- Prefer `INSERT ... ON DUPLICATE KEY UPDATE` when a unique key conflict defines upsert semantics.
- Use `LAST_INSERT_ID()` for auto-increment values; MySQL has no `RETURNING` clause like PostgreSQL.
- Avoid `REPLACE INTO` unless delete-then-insert side effects (new auto-increment IDs, DELETE cascades) are intentional.
- Interpret affected-row counts carefully: 1 = inserted, 2 = updated.

## Locking Traps

- Default `REPEATABLE READ` can surprise with gap locks; choose isolation deliberately for write-heavy paths.
- Keep transactions short; long open transactions hold locks and inflate undo history.
- Watch deadlocks via `SHOW ENGINE INNODB STATUS` and normalize lock order across code paths.
- Prefer row-level patterns over table locks for application traffic.

## InnoDB vs MyISAM

- Use InnoDB for application tables: transactions, row locking, foreign keys, crash recovery.
- Treat MyISAM as legacy/system-table territory, not application data.
- Confirm with `SHOW TABLE STATUS` and convert via `ALTER TABLE ... ENGINE=InnoDB` when safe.
- Mixed engines in JOINs can work but lose shared transaction guarantees.

## Syntax Gotchas

- `LIMIT offset, count` ordering differs from PostgreSQL `LIMIT count OFFSET offset`.
- Both `!=` and `<>` work; prefer `<>` for SQL-standard clarity.
- DDL commits immediately—`ALTER TABLE` cannot be rolled back inside a transaction.
- Boolean is `TINYINT(1)`; `TRUE`/`FALSE` are 1/0.
- Prefer `COALESCE` for general null handling; `IFNULL(a, b)` remains fine for two-arg cases.

## Connection Management

- `wait_timeout` kills idle connections (default 8h); pools must detect/reconnect.
- Default `max_connections` is 151 and is often too low for multi-instance apps.
- Keep aggregate pool size below `max_connections`.
- Use `SHOW PROCESSLIST` and `KILL <id>` for stuck sessions.

## Replication Awareness

- Statement-based replication can break with non-deterministic functions (`UUID()`, `NOW()`).
- Row-based replication is safer and is the MySQL 8 default, at higher bandwidth cost.
- Check replica lag (`Seconds_Behind_Source` / `Seconds_Behind_Master`) before depending on replica reads.
- Write only to the primary; verify replicas are read-only.

## Performance

- `EXPLAIN ANALYZE` exists on MySQL 8.0.18+; older versions provide `EXPLAIN` without actual timings.
- Query cache is removed in MySQL 8—cache at the application layer when needed.
- `OPTIMIZE TABLE` rebuilds/fragments cleanup but locks; use online schema-change tools for large tables.
- Size `innodb_buffer_pool_size` around 70–80% of RAM on dedicated DB hosts, then validate with metrics.

## State location

This skill is knowledge-only and does not store local configuration or database data in the agent filesystem.
