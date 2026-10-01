---
name: mariadb
description: >
  Write and operate MariaDB correctly: utf8mb4/collations, indexes, sequences,
  system-versioned (temporal) tables, JSON functions, Galera, thread pool,
  engines, locking, EXPLAIN, and backup/restore. Use when the target is MariaDB
  or MariaDB-specific syntax and ops differ from generic MySQL. Not for
  dialect-agnostic SQL (`sql`), pure MySQL server work (`mysql`), embedded
  SQLite (`sqlite`), or Timescale hypertables (`timescaledb`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🦭","requires":{"bins":["mariadb"]}}'
  related-skills: '{"mysql":"Hand off when the server is MySQL-specific rather than MariaDB syntax or Galera/temporal features.","sql":"Use for dialect-agnostic SQL patterns before specializing to MariaDB.","sqlite":"Use when the workload fits embedded/local SQLite instead of a server MariaDB instance.","timescaledb":"Hand off time-series hypertable and continuous-aggregate work on PostgreSQL/Timescale."}'
---

## When to load

Load for **MariaDB** schema, query, cluster, temporal-table, Galera, thread-pool, engine, lock, or backup work.

Do **not** load as the primary skill for generic SQL (`sql`), MySQL-only server quirks (`mysql`), embedded SQLite (`sqlite`), or Timescale/Postgres time-series (`timescaledb`).

## Quick reference

| Topic | File | When to load |
|-------|------|--------------|
| Charset, indexes, sequences, temporal, JSON, engines, locks, EXPLAIN, backup | `references/mariadb-guide.md` | Default depth for MariaDB design and ops |
| Domain knowledge & traps | `references/domain-knowledge.md` | Version-sensitive claims and MariaDB vs MySQL deltas |
| Research sources | `references/sources.md` | Citing or refreshing official docs |

## Workflow

1. Confirm server identity and version: `SELECT VERSION();` / `SHOW VARIABLES LIKE 'version%';`. Prefer InnoDB for application data unless a documented engine choice applies.
2. Enforce `utf8mb4` at schema and connection layer before storing text (`SET NAMES utf8mb4` or DSN charset).
3. Design indexes for real predicates; use prefix lengths on TEXT/BLOB; verify with `SHOW INDEX` / `EXPLAIN`.
4. Prefer MariaDB sequences when you need IDs before insert or across tables; use system versioning only when history queries are a product requirement.
5. Keep Galera transactions small; set `wsrep_sync_wait` before critical reads when causal consistency matters.
6. Validate plans with `EXPLAIN` / `EXPLAIN ANALYZE` (where available) before shipping slow-path changes.
7. Load `references/mariadb-guide.md` for depth; load `references/domain-knowledge.md` when claiming version behavior; load `references/sources.md` when refreshing citations.
8. Prefer concrete verification (`SHOW`, `EXPLAIN`, status checks) over memorized absolutes; re-check after major version upgrades.

## Character set traps

- Prefer `utf8mb4`; older 3-byte UTF-8 aliases cannot store full Unicode including emoji.
- Use `utf8mb4_unicode_ci` for linguistic case-insensitive sorting; `utf8mb4_bin` for exact byte comparison.
- Keep collation consistent across joined columns—mismatches force conversions and hurt index use.
- Set the connection charset to match schema defaults.

## Indexing traps

- TEXT/BLOB indexes need an explicit prefix length.
- Composite order matters: `(a, b)` serves `WHERE a=?` but not `WHERE b=?` alone.
- Foreign keys usually create an index on the child; still verify with `SHOW INDEX`.
- Covering indexes avoid table lookups when every selected column is in the index.

## MariaDB-specific strengths

- **Sequences**: `CREATE SEQUENCE` / `NEXT VALUE FOR` when you need pre-insert IDs that survive rollback better than ad-hoc auto-increment patterns.
- **System versioning**: `ADD SYSTEM VERSIONING` plus `FOR SYSTEM_TIME AS OF` / `BETWEEN` for row history.
- **Galera**: multi-primary cluster semantics; same-row conflicts roll back—keep writes small and plan quorum with odd `wsrep_cluster_size`.
- **Thread pool**: `thread_handling=pool-of-threads` under high concurrency instead of one thread per connection by default habit.
- **JSON**: `JSON_VALUE`, `JSON_QUERY`, `JSON_TABLE`, `JSON_VALID` for extract/unnest/guard paths.

## Failure modes

- "Too many connections" → pool clients, review `max_connections`, kill idle sessions intentionally.
- "Lock wait timeout exceeded" → `SHOW ENGINE INNODB STATUS`, shorten transactions, fix lock order.
- "Row size too large" → move wide payloads to TEXT/BLOB/JSON, normalize, or re-check row format.
- Galera certification failures → retry with smaller transactions; avoid hot-row multi-primary writes.
- Collation/join surprises → normalize charset/collation before blaming the optimizer.

## Safety

- Never commit live credentials, dumps with PII, or production connection strings into the skill package.
- Treat backup success as restore-tested only; schedule restore drills.
- Destructive DDL, mass `UPDATE`/`DELETE`, and cluster membership changes need explicit operator intent and a rollback path.
