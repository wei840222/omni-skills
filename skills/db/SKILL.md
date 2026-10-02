---
name: db
description: >
  Design and operate relational databases safely: connection pools, short
  transactions, lock ordering, SELECT FOR UPDATE, expand-migrate-contract schema
  changes, CONCURRENTLY/ONLINE indexes, backup/PITR, replica lag, N+1 and unbounded
  SELECT, constraints over app checks, UTC timestamps, DECIMAL money, vacuum and
  IOPS limits. Use for generic DB gotchas across Postgres/MySQL-class systems.
  Prefer `sql` for dialect-agnostic query craft, `mysql`/`mariadb`/`sqlite`/
  `mongodb`/`timescaledb`/`dynamodb`/`influxdb`/`oracle-db` for engine-specific work,
  and `observability` for metrics/traces around the data plane.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🗃️"}'
  related-skills: '{"sql":"Dialect-agnostic SQL craft, EXPLAIN patterns, and schema design when the ask is query/model shape rather than ops traps.","mysql":"MySQL-server-specific syntax, InnoDB quirks, and ops.","mariadb":"MariaDB-only features (sequences, temporal tables, Galera, thread pool).","sqlite":"Embedded/local SQLite instead of a server database.","mongodb":"Document store modeling and ops outside relational gotchas.","timescaledb":"Postgres time-series hypertables and continuous aggregates.","dynamodb":"AWS DynamoDB single-table design and capacity modes.","influxdb":"Influx time-series write/query paths.","oracle-db":"Oracle-specific SQL and administration.","observability":"Metrics, logs, and traces for pool saturation, lag, and lock waits.","backups":"Retention, immutability, and restore drills beyond engine-native dump/PITR."}'
---

# db

Cross-engine **database operational gotchas** skill. Keep credentials and connection strings out of the package; inject DSNs and admin access at runtime.

## When to load

Load when the work is about **shared failure modes** of server databases:

- pool exhaustion, serverless connection storms, idle session bloat
- long transactions, deadlocks, lost updates, lock ordering
- online schema changes, default-value rewrites, index builds, expand-migrate-contract
- backup consistency, WAL/binlog retention, restore drills, replica lag / split-brain
- N+1 queries, missing FK indexes, huge `IN` lists, unbounded `SELECT`/`COUNT(*)`
- app-level uniqueness races, orphan rows, timezone storage, floating-point money
- single-table growth, autovacuum/bloat, stale planner stats, connection vs lock contention, IOPS ceilings

Prefer other skills when the ask is mainly:

- dialect-agnostic SQL/EXPLAIN craft → `sql`
- MySQL / MariaDB / SQLite / MongoDB / Timescale / DynamoDB / Influx / Oracle specifics → matching engine skill
- retention policy and immutable backup design → `backups`
- RED/USE metrics and tracing around the data plane → `observability`

## State location

Optional audit notes, migration runbooks, and restore drill logs may live under `<workspace>/db/`, `<workspace>/memory/db/`, or `~/db/`. Resolve `<workspace>` as the host/runtime workspace root, never the shell cwd. Do not store production credentials in the skill tree.

## Progressive disclosure

Load only `SKILL.md` first. Open `references/database-gotchas.md` for trap depth and `references/sources.md` when citing or refreshing facts.

## Quick reference

| Topic | File | When to load |
|-------|------|--------------|
| Operational traps (connections → scaling) | `references/database-gotchas.md` | Default depth for reviews and incident triage |
| Research sources | `references/sources.md` | Citing or refreshing Gate 6 claims |

## Workflow

1. Identify engine + major version before asserting DDL/lock behavior (Postgres 11+ default-add differs from older rewrites; MySQL online DDL variants differ by version).
2. Separate **schema change**, **query shape**, and **capacity** problems; do not fix pool exhaustion with a bigger instance alone.
3. Prefer expandable migrations: add nullable column → backfill in batches → set default/constraints → drop old path after readers/writers move.
4. Keep transactions short; take locks in a stable global order; use `SELECT … FOR UPDATE` or optimistic versioning for read-modify-write.
5. Treat replicas as eventually consistent; check lag before critical reads; never write to a replica.
6. Load `references/database-gotchas.md` for trap depth; load `references/sources.md` when refreshing citations.
7. Verify with engine tools (`pg_stat_activity`, `pg_locks`, `EXPLAIN`, pool metrics) rather than memorized absolutes after major upgrades.

## Core ops checklist

1. **Connections** — size pools to real `max_connections`; put serverless workers behind RDS Proxy / PgBouncer-class pooling; set idle timeouts.
2. **Transactions** — short critical sections; consistent lock order; explicit `BEGIN`/`COMMIT` when autocommit semantics differ.
3. **Schema** — avoid full-table rewrites on hot tables; use `CREATE INDEX CONCURRENTLY` (Postgres) or online DDL where supported; deploy code that tolerates dual columns before drops.
4. **Backup** — consistent snapshots or verified logical dumps; retain WAL/binlog for PITR **before** you need it; restore-test on a schedule.
5. **Replication** — lag-aware reads; fencing on failover; app reconnect after promote.
6. **Queries** — kill N+1; index FKs; batch large `IN` lists; approximate or cache huge counts; always bound unbounded scans.
7. **Integrity** — DB unique/check/FK constraints beat app-only checks; store UTC instants; money as `DECIMAL`/integer minor units.
8. **Scale** — plan partitioning/sharding before 100M+ hot rows; watch vacuum/dead tuples, planner stats after bulk load, I/O wait vs CPU.

## Failure recovery (quick)

| Symptom | First checks | Safe next step |
|---------|--------------|----------------|
| App hangs under load | pool in-use vs max; DB `max_connections`; idle sessions | shed load; raise pool only with evidence; add pooler |
| Migration blocked | long tx / open locks holding relation | kill idle-in-transaction; reschedule DDL off peak |
| Deadlocks | lock graphs / error detail | reorder lock acquisition; shorten tx |
| Stale reads after write | replica lag metrics | read-after-write on primary or sync wait |
| Restore uncertainty | last successful restore drill date | restore to scratch and compare checksums before trusting backup |
| Bloat / slow seq scans | dead tuple ratio; last `ANALYZE` | vacuum/analyze; fix long tx preventing cleanup |

## Positive defaults

- Store secrets in the host secret flow; pass DSNs via env at runtime.
- Add `--dry-run` / expand-only steps before destructive DDL or mass deletes.
- Prefer constraints and typed columns over application-only validation.
- Document rollback (dual-write window, feature flag) beside every production migration.

## Out of scope

- Implementing a full ORM or generating entire application schemas from scratch without an engine target
- Vendor pricing, managed-SKU recommendations without current official docs
- Replacing engine-specific skills listed in `related-skills`
