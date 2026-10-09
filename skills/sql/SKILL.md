---
name: sql
description: >
  Write, review, and optimize SQL; design schemas, indexes, and constraints; plan
  live migrations and operational work across relational engines. Use when a query
  is slow, EXPLAIN shows a sequential scan or ignored index; rows are duplicated,
  missing, or totals inflate after a JOIN; deadlocks, lock timeouts, "too many
  connections", or uncommitted transactions appear; designing tables/keys/types,
  normalizing or denormalizing, or choosing JSON vs real columns; ALTER TABLE on a
  live table, expand-migrate-contract rollouts, backups/restores, replication lag,
  pooling, partitioning, bulk CSV loads, or engine-to-engine moves; window functions,
  CTEs, keyset pagination, upserts, full-text search, multi-tenancy, RLS, and timezone
  handling in MySQL, SQLite, MariaDB, or SQL Server. Not for PostgreSQL server
  internals such as vacuum tuning and work_mem (`pg`), and not for ORM schema modeling
  inside a framework (`prisma`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🗄️","requires":{"anyBins":["sqlite3","psql","mysql","sqlcmd"]}}'
  related-skills: '{"mysql":"MySQL/InnoDB-specific charset, indexing, and production patterns once the engine is fixed.","pg":"PostgreSQL server internals: vacuum, work_mem, wraparound, and Postgres-only ops.","prisma":"ORM-level schema modeling and client workflows rather than raw SQL craft.","sqlite":"SQLite concurrency, pragmas, and type affinity for embedded/local workloads."}'
---

# SQL

Dialect-aware SQL craft for writing, reviewing, optimizing queries and designing/migrating relational schemas. Preferences may persist under a portable `<state_root>`; skill resources stay under `references/`.

## State location

SQL preferences and memory may exist in `<workspace>/sql/`, `<workspace>/memory/sql/`, or `~/sql/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/sql/`, `<workspace>/memory/sql/`, `~/sql/`.
3. If none exists and state must be created, default to `<workspace>/sql/`.

Use the selected `<state_root>` for every state operation in this skill.

| Path | Required? | Role |
|------|-----------|------|
| `<state_root>/config.yaml` | optional | Dialect, naming, lock/batch defaults the user declared |
| `<state_root>/memory.md` | optional | Schema seen, pain points, safety posture (no credentials) |

If legacy data exists only under `~/Clawic/data/sql/` or `~/clawic/sql/`, treat it as a migration source — copy only after the user asks; never auto-merge into active lookup order.

Do not treat the literal string `<state_root>` as a filesystem path. Never store connection strings, passwords, hostnames, or query results with personal data under `<state_root>/`.

## When to load

Load this skill when the user needs:

- writing, reviewing, or optimizing SQL (joins, CTEs, window functions, upserts)
- schema design: keys, types, indexes, constraints, normalize/denormalize, JSON vs columns
- diagnosing slow queries, deadlocks, lock timeouts, wrong totals, or duplicated rows
- live DDL / expand-migrate-contract migrations that must keep the database operational
- backups, restores, pooling, replication lag, partitioning, bulk loads, engine moves

Hand off when a sibling owns the job:

| Job | Skill |
| --- | --- |
| PostgreSQL vacuum, work_mem, wraparound, server internals | `pg` |
| MySQL/InnoDB-only production patterns | `mysql` |
| SQLite pragmas / embedded concurrency | `sqlite` |
| ORM schema modeling in a framework | `prisma` |

## Core path

1. **Confirm engine + version** before emitting dialect-specific syntax.
2. **Parameterize values; allowlist identifiers** — never interpolate user input into table/column names.
3. **Rank before tuning** — use `EXPLAIN (ANALYZE, BUFFERS)` / engine equivalent; total cost = mean latency × call count.
4. **Keep transactions short** — no HTTP or user waits inside `BEGIN...COMMIT`.
5. **Live DDL** — set `lock_timeout` first; prefer expand → migrate → contract.
6. **Load depth on demand** — one file under `references/` for the current job, not the whole tree.

## Depth on demand

| Need | Load |
| --- | --- |
| Quick reference, core rules, traps, portability matrix | `references/domain.md` |
| First-use preference load / write rules | `references/setup.md` |
| Memory file shape | `references/memory-template.md` |
| Slow plans, indexes, EXPLAIN nodes | `references/performance.md` |
| Regression chain, plan flips | `references/debug.md` |
| Lock order, isolation, deadlocks | `references/transactions.md` |
| Patterns: keyset, SKIP LOCKED, upserts | `references/patterns.md` |
| Modeling keys/cardinality | `references/modeling.md` |
| Tenants, tags, audit, history shapes | `references/schemas.md` |
| JSON / semi-structured | `references/json.md` |
| Analytics, rollups, matviews | `references/analytics.md` |
| CSV/dump/engine moves | `references/data-loading.md` |
| Timezones, DST, fiscal bounds | `references/datetime.md` |
| Cross-engine divergences | `references/dialects.md` |
| Grants, RLS, PII erasure | `references/security.md` |
| Fixtures, migration tests | `references/testing.md` |
| ORM N+1 / mystery tx | `references/orm.md` |
| Replicas, sharding, cache | `references/scaling.md` |
| Backups, pooling, live ops | `references/operations.md` |
| Official docs / version-sensitive claims | `references/sources.md` |

## Safety defaults

- Preview destructive `UPDATE`/`DELETE`/`DROP`/`TRUNCATE` as the matching `SELECT` first when `destructive_guard` is on (default).
- Credentials stay in the user's secret store — never in skill files, migrations, or `<state_root>/`.
- Do not invent engine version floors, pricing, or vendor limits from memory; verify against the live engine docs when a claim is version-sensitive.
- Prefer half-open timestamp ranges and typed comparisons so indexes stay sargable.

## Output gates

Before emitting SQL, verify:

- every value is a placeholder; every dynamic identifier came from an allowlist
- `UPDATE`/`DELETE` has a `WHERE`, or the full-table effect is explicit
- no 1:N join feeds an aggregate without pre-aggregation
- `LIMIT`/`TOP` has deterministic `ORDER BY` with a unique tiebreaker
- new tables: suitable PK, zoned timestamps, FK columns indexed
- live DDL: `lock_timeout` set and change is expand-only when possible
- every construct exists on the target engine (`references/dialects.md`)
