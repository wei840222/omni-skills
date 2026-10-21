---
name: pg
description: >
  Tune, design, and operate PostgreSQL: slow queries, indexes, schemas,
  migrations, vacuum, locks, replication, and backups. Use when writing
  Postgres SQL or psql, designing tables and indexes, reading an EXPLAIN plan,
  running DDL or a migration on a live table, or when a query suddenly slowed,
  a table grows while rows stay flat, autovacuum falls behind, "too many
  clients already" appears, a replica lags, deadlocks and lock waits pile up,
  pg_wal fills the disk, or an upgrade, restore, or partitioning plan is on
  the table. Covers connection pooling and PgBouncer, full-text, trigram and
  pgvector search, JSONB, roles and row-level security, PITR, extensions, and
  managed Postgres (RDS, Aurora, Cloud SQL, Neon, Supabase). Prefer `sql` for
  cross-engine SQL portability, `prisma` for ORM-level modeling, `timescaledb`
  for hypertables/compression/continuous aggregates, and `db` for
  engine-agnostic reliability patterns.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🐘"}'
  related-skills: '{"db":"Engine-agnostic database reliability, scaling, and operations patterns beyond Postgres-specific recipes.","prisma":"ORM-level schema modeling and query pitfalls when the stack sits on top of Postgres.","sql":"Cross-engine SQL portability and dialect differences outside Postgres-only work.","timescaledb":"Time-series workloads on Postgres: hypertables, compression, and continuous aggregates."}'
---

## State location

Optional PostgreSQL preferences and memory may exist in
`<workspace>/pg/`, `<workspace>/memory/pg/`, or `~/pg/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/pg/`, `<workspace>/memory/pg/`, `~/pg/`.
3. If none exists and durable preferences must be created, default to
   `<workspace>/pg/` only with user consent.
4. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/pg/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

Legacy locations `~/Clawic/data/pg/`, `~/clawic/pg/`, and bare `~/pg/` leftovers
outside the resolver are migration sources only. Copy, validate, and cut over
only after the user chooses migration; do not write there by default.

```text
<state_root>/
├── config.yaml   # Declared preferences (version, provider, timeouts, …)
└── memory.md     # Observed schema shape, incidents, and stance
```

Load `references/setup.md` on first use and `assets/data-templates.md` for blank shapes.
Open `references/sources.md` before treating version-gated behavior, planner knobs,
or extension claims as current fact.

## When To Use

- A query is slow, a plan needs interpretation, or an index is being ignored
- Designing a schema: types, keys, constraints, partitions, JSONB vs columns
- Running DDL, a migration, or a backfill against a live production table
- Operating Postgres: connections, timeouts, vacuum, bloat, locks, replication, backups, upgrades
- A production incident: disk full, wraparound warnings, connection storm, runaway query, suspected corruption
- Building queue, upsert, search, or vector patterns that Postgres solves natively
- Not for cross-engine SQL portability (`sql`), ORM modeling (`prisma`), time-series hypertables (`timescaledb`), or engine-agnostic reliability patterns (`db`)

## Quick Reference

| Situation | Play |
|---|---|
| Slow query, cause unknown | Slow-Query Triage below — start from `EXPLAIN (ANALYZE, BUFFERS)` |
| Plan shows a seq scan you did not expect | Not automatically the bug: a scan beats an index past roughly 5-15% of the table (→ `references/slow-queries.md`) |
| WHERE on a function of a column | Expression index matching the query text exactly (→ Indexing Essentials) |
| Status/flag column, minority of rows queried | Partial index `WHERE status = 'active'` |
| Substring/fuzzy search (`LIKE '%x%'`, ILIKE, typos) | pg_trgm GIN index; a B-tree cannot serve a leading wildcard (→ `references/search.md`) |
| Word/phrase search, ranking | Stored generated `tsvector` + GIN, queried via `websearch_to_tsquery` (→ `references/search.md`) |
| Job queue, retries, or an event outbox in Postgres | `SELECT ... FOR UPDATE SKIP LOCKED` — no external broker needed (→ `references/queues.md`) |
| Insert-or-update | `INSERT ... ON CONFLICT ... DO UPDATE` + `RETURNING` |
| First/top-N rows per group | `DISTINCT ON` for first-row; `LATERAL` + matching index for top-N at scale |
| Deep pagination | Keyset (`WHERE (created_at, id) < (?, ?)`) on an indexed sort key; avoid deep `OFFSET` |
| DDL on a busy table | `SET lock_timeout` first, then the online variant (→ Safe DDL on Busy Tables) |
| Query hangs with no CPU burn | It is blocked: `pg_blocking_pids()` names the holder (→ `references/locks.md`) |
| Table grows on disk while row count is flat | Bloat: find the oldest transaction or replication slot first (→ `references/vacuum-bloat.md`) |
| An error code or message to decode | Error Codes below; full catalog in `references/errors.md` |
| Slow test suite, or a migration that needs rehearsing on real volume | Transaction-per-test and template databases; rehearse on a restored copy (→ `references/test-databases.md`) |
| Anything else surprising | `EXPLAIN (ANALYZE, BUFFERS)` before and after every change; if it is live and stuck, check `pg_stat_activity` for a blocker before touching anything |

Depth on demand, by phase:

- **Diagnose** — `references/slow-queries.md` · `references/locks.md` · `references/errors.md` · `references/monitoring.md` · `references/incidents.md`
- **Design** — `references/schema-design.md` · `references/indexing.md` · `references/partitioning.md` · `references/json.md` · `references/search.md` · `references/queues.md`
- **Change** — `references/migrations.md` · `references/bulk-load.md` · `references/upgrades.md` · `references/functions-triggers.md` · `references/test-databases.md`
- **Operate** — `references/connections.md` · `references/vacuum-bloat.md` · `references/tuning.md` · `references/backup-restore.md` · `references/replication.md` · `references/security.md` · `references/managed-postgres.md` · `references/psql.md` · `references/extensions.md`

## Core Rules

1. **Tune from a plan.** Run `EXPLAIN (ANALYZE, BUFFERS)`; plain EXPLAIN prints estimates and the estimate is usually the bug. Check estimated vs actual rows per node — off by more than 10x means a statistics problem, not a missing index.
2. **Index every foreign key column you join or cascade on.** Postgres indexes primary keys and unique constraints automatically; you must explicitly index FK columns. A parent `DELETE` of 10k rows against an unindexed 50M-row child is 10k sequential scans.
3. **Composite index order: equality columns first, then one range or sort column.** `(tenant_id, created_at)` answers `WHERE tenant_id = ? ORDER BY created_at DESC LIMIT 20` from the first 20 index entries; `(created_at, tenant_id)` walks every row in date order filtering as it goes. A column is usable only while every column to its left is pinned by equality.
4. **Set the three timeouts per role before you need them, and start every live DDL with `lock_timeout`.** Defaults: `lock_timeout = '2s'` (variable `lock_timeout_default`), `statement_timeout = '30s'`, `idle_in_transaction_session_timeout = '5min'`. A blocked `ALTER TABLE` waiting for ACCESS EXCLUSIVE queues every later query on that table behind it — the outage is the queue, not the lock. An idle transaction with no timeout freezes vacuum's horizon for the whole database.
5. **`work_mem` is per sort/hash node, not per query.** Worst case = connections × nodes per query × `work_mem`: 100 × 4 × 64MB = 25.6GB. Keep it small globally (4-16MB) and raise it per session for a known heavy query.
6. **Pick the type that deletes a class of bugs.** `TIMESTAMPTZ` (stores a UTC instant, not a zone) · money as `NUMERIC(12,2)` or integer cents (never binary float; never `money`) · `TEXT` over `VARCHAR(n)` (identical performance; add length as a CHECK only if it is a business rule) · `GENERATED ALWAYS AS IDENTITY` over `SERIAL` (PostgreSQL >=10).
7. **Schema changes follow expand → backfill in batches → contract.** One `UPDATE` over 50M rows writes 50M new row versions in a single transaction: the table doubles on disk, vacuum cannot reclaim anything until commit, and a failure at minute 50 discards everything. Batch 1k-50k rows with a commit and a resume key per batch.
8. **A backup you have never restored is a hypothesis.** Schedule the restore, not just the dump: restore into a scratch instance on a fixed cadence, time it, and write the measured RTO down. `pg_dump` also omits roles and tablespaces — only `pg_dumpall --globals-only` has them.

## Slow-Query Triage

Run in this order; skipping to step 4 spends the fix on the wrong query.

1. `pg_stat_statements` ordered by `total_exec_time DESC` (needs `shared_preload_libraries`). High `mean_exec_time` = slow query; high `calls` = hot path — a 5ms query called 10k/min beats a 2s report as a target.
2. `EXPLAIN (ANALYZE, BUFFERS)` on the worst offender. Estimates are the thing that lies.
3. Compare estimated vs actual rows per node. Off by >10x → stale or insufficient statistics: run `ANALYZE`; still off → `ALTER TABLE ... ALTER COLUMN ... SET STATISTICS 1000` (default 100), or `CREATE STATISTICS` for correlated columns (city+country style).
4. Read Buffers: `read` dominant → I/O-bound (missing index, cold cache); `hit` dominant → plan or CPU bound (wrong join order, overwide scan).
5. A seq scan is not automatically the bug: it beats an index once a query touches roughly 5-15% of the table (correlation-dependent). On SSD set `random_page_cost = 1.1` (default 4.0 assumes spinning disk) or the planner will refuse good indexes.
6. Re-run step 2 after the fix and compare buffers and actual time — a prettier plan shape with the same buffer count fixed nothing.

## Indexing Essentials

- Partial index size is proportional to matching rows: `WHERE active` over a 5%-active table is ~95% smaller and stays resident in cache.
- Expression index must match the query text exactly: `ON lower(email)` serves `WHERE lower(email) = ?`, not `WHERE email ILIKE ?`.
- Covering index `INCLUDE (name)` enables index-only scans — verify "Heap Fetches" near 0 in EXPLAIN; vacuum lag leaves a stale visibility map and silently degrades them back to heap fetches.
- Updating any indexed column defeats HOT updates and writes to every index on the table. Keep counters and churning timestamps out of indexes; set `fillfactor = 90` on update-heavy tables so HOT has page room.
- Drop unused with care: `pg_stat_user_indexes` where `idx_scan = 0`, but only after a full business cycle (month-end reports) and checked on every replica — index statistics are per node.
- Defer indexing a low-cardinality column alone (boolean, three-value enum): the planner ignores it. Fold it into a composite or make the index partial.

## Postgres-Native Query Patterns

- `FOR UPDATE SKIP LOCKED`: concurrent workers each claim unlocked rows; the canonical Postgres job queue, no broker required.
- `pg_advisory_xact_lock(key)`: application mutex with no table, released automatically at commit. The session variant (`pg_advisory_lock`) survives commit and leaks when a pooled connection is recycled.
- `IS NOT DISTINCT FROM`: NULL-safe equality, replaces `(a = b OR (a IS NULL AND b IS NULL))`.
- `x NOT IN (subquery)` returns zero rows if the subquery yields a single NULL — use `NOT EXISTS`.
- `count(*) > 0` scans every match; `EXISTS (SELECT 1 ...)` returns at the first match.
- Aggregates with `FILTER (WHERE ...)` replace CASE-inside-SUM pivots, readably.
- `now()` is frozen at transaction start, so every row written in one long transaction shares a timestamp; `clock_timestamp()` gives wall time.
- CTEs: PostgreSQL >=12 inlines them like subqueries; below that every CTE is an optimization fence that blocks index pushdown. `MATERIALIZED` restores the fence deliberately.

## Safe DDL on Busy Tables

Every recipe starts with `SET lock_timeout = '2s'` and a retry loop (rule 4). Full procedures, backfill loops and expand/contract sequencing in `references/migrations.md`.

- `ADD COLUMN ... DEFAULT <constant>` is metadata-only (PostgreSQL >=11); a volatile default (`now()`, `gen_random_uuid()`) rewrites the whole table. Add nullable, backfill in batches, then set the default.
- New constraint on a big table: `ADD CONSTRAINT ... NOT VALID` (instant), then `VALIDATE CONSTRAINT` (weak lock, full scan that does not block writes).
- `SET NOT NULL`: PostgreSQL >=12 skips the full-table scan when a validated `CHECK (col IS NOT NULL)` already proves it — add the check NOT VALID, validate, set not null, drop the check.
- `CREATE INDEX CONCURRENTLY`: no write lock, but it cannot run inside a transaction block and a failure leaves an INVALID index behind — check `pg_index.indisvalid`, drop, retry. Same for `REINDEX CONCURRENTLY` (PostgreSQL >=12).
- Type changes: widening `varchar(n)` or `varchar → text` is metadata-only; `int → bigint` rewrites the table. On a hot table that means new column, dual-write, backfill, swap.

## Error Codes

SQLSTATE is stable across versions; the message text is not. Match on the code. Full catalog with fixes in `references/errors.md`.

| SQLSTATE | Name | First move |
|---|---|---|
| 23505 | unique_violation | Genuine duplicate or a race — if the insert is idempotent, `ON CONFLICT DO NOTHING/UPDATE` |
| 40001 | serialization_failure | Retry the whole transaction; on a replica it also means a recovery conflict (→ `references/replication.md`) |
| 40P01 | deadlock_detected | Two transactions took the same rows in opposite order — impose one order in the app |
| 53300 | too_many_connections | Pool before raising `max_connections` (→ `references/connections.md`) |
| 55P03 | lock_not_available | Your `lock_timeout` fired, exactly as designed — back off and retry |
| 57014 | query_canceled | `statement_timeout` or a human cancel |
| 25P02 | in_failed_sql_transaction | An earlier statement failed; everything is refused until ROLLBACK |
| 54000 | program_limit_exceeded | Usually an index row above ~2.7 kB (a third of an 8 kB page) — index a hash or a prefix instead |
| 22P02 | invalid_text_representation | A string reached a typed column or parameter (`''` into an integer, unknown enum label) |

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| server_version | number (12-18) | 16 | Which version-gated advice applies (`feature >=X` lines) when the live server version is unknown; also gates upgrade recommendations |
| deployment | self-hosted \| rds \| aurora \| cloudsql \| neon \| supabase | self-hosted | Switches configuration advice between `ALTER SYSTEM`/postgresql.conf and provider parameter groups, and suppresses superuser-only recipes |
| client | psql \| pgcli \| gui | psql | Which client meta-commands and flags appear in examples |
| pooler | none \| app-pool \| pgbouncer \| supavisor | app-pool | Whether session-state features (session advisory locks, `SET`, temp tables, LISTEN/NOTIFY) are safe to emit in generated code |
| id_style | bigint-identity \| uuidv7 \| uuidv4 | bigint-identity | Primary key type in every generated `CREATE TABLE` and migration |
| naming_convention | snake_plural \| snake_singular | snake_plural | Table and column names in generated DDL and examples |
| lock_timeout_default | duration | 2s | The `SET lock_timeout` value prefixed to every DDL recipe (Core Rules 4, Safe DDL) |
| destructive_confirm | bool | true | `DROP`, `TRUNCATE`, unqualified `DELETE`/`UPDATE`, `VACUUM FULL` and `pg_terminate_backend` are emitted for review instead of run |

Preference areas — customizable dimensions; a stated preference is recorded in `config.yaml` and applied from then on:

- **Tooling** — migration framework (plain SQL files, Flyway, Alembic, Prisma Migrate), diff tooling, bloat/repack tooling — affects the shape of emitted migrations
- **Thresholds** — per-role `statement_timeout`, backfill batch size, slow-query threshold worth reporting, index-bloat percentage that triggers a rebuild
- **Conventions** — schema layout (`public` vs per-domain schemas), enum vs lookup table, soft-delete policy, timestamp column names, index naming
- **Platform** — major version, OS and glibc/ICU provider, storage class (NVMe vs network disk), instance memory — affects `references/tuning.md` numbers
- **Risk posture** — whether to run DDL directly or hand back reviewed SQL, whether replicas may be read, how aggressive autovacuum tuning may be
- **Output format** — SQL only vs SQL plus a plan walkthrough, how much EXPLAIN detail to narrate, whether to include rollback SQL by default
- **Integrations** — monitoring stack (pg_stat_statements alone, Prometheus exporter, provider console), backup tooling (pgBackRest, WAL-G, provider snapshots)
- **Restrictions** — extensions the platform forbids, compliance regimes that mandate RLS or column encryption, tables that must never be touched online
- **Cadence** — restore-drill frequency, index-usage review cycle, statistics/vacuum maintenance windows

## Output Gates

Before emitting DDL, a migration, or a schema:

- Does every new foreign key column get an index in the same migration?
- Does every statement touching a live table set `lock_timeout` first?
- Is the destructive step (drop column, drop table, drop index) split into its own later migration, after the code that stopped using it shipped?
- Is the backfill batched, resumable, and committed per batch?
- Are new indexes `CONCURRENTLY` and outside any transaction block?
- New tables: `TIMESTAMPTZ` timestamps, key per `id_style`, NOT NULL wherever it is true, uniqueness stated as a constraint?
- Did you run `EXPLAIN (ANALYZE, BUFFERS)` before and after, and compare buffers rather than wall time alone?

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| `NOT IN` with a nullable subquery | One NULL makes the predicate unknown → 0 rows, silently | `NOT EXISTS` |
| `OFFSET 100000` pagination | Postgres computes and discards every skipped row; page 1000 costs 1000 pages | Keyset pagination on an indexed sort key |
| Adding an index because the query "feels" unindexed | Half the time the plan is fine and the statistics are wrong; the new index just adds write cost | Read the plan first (Core Rules 1) |
| `CREATE INDEX` without CONCURRENTLY on a live table | SHARE lock blocks all writes for the whole build | CONCURRENTLY + `indisvalid` check |
| DDL without `lock_timeout` | The waiting ALTER queues every later query behind it | `SET lock_timeout` + retry (→ Safe DDL) |
| `VACUUM FULL` to fix bloat on a live table | ACCESS EXCLUSIVE for the whole rewrite — a full outage on that table, plus double the disk | `pg_repack`, or fix the cause: oldest transaction, replication slot, autovacuum settings |
| `OS kill signals` on a stuck backend | The postmaster treats it as a crash and restarts the entire cluster into recovery | `pg_cancel_backend(pid)`, then `pg_terminate_backend(pid)` |
| `TIMESTAMP` (no time zone) for event times | Two servers in different zones write incomparable values; DST duplicates an hour | `TIMESTAMPTZ` (Core Rules 6) |
| CTE performance assumed on old Postgres | Below 12 every CTE materializes: no index pushdown into it | Upgrade, inline as a subquery, or accept the fence knowingly |
| Dropping an "unused" index seen on the primary only | Index statistics are per node; replicas may be serving reads from it | Check `pg_stat_user_indexes` on every node, across a full cycle |
| Trusting plain `EXPLAIN` | Costs are estimates; the misestimate IS the usual bug | `EXPLAIN (ANALYZE, BUFFERS)` |
| ENUM for fast-changing categories | Values cannot be dropped or reordered without type surgery | Lookup table + FK once the set churns |

## Where Experts Disagree

- **bigint vs UUID primary keys.** Random UUIDv4 fragments the B-tree and bloats every secondary index; bigint leaks row counts and needs coordination across writers. Boundary: external-facing or multi-writer IDs → UUID, time-ordered (v7) where available; internal high-write tables → `bigint IDENTITY`.
- **Normalize vs denormalize.** Postgres joins are cheaper than most engineers assume; denormalize only after a plan shows the join as the measured bottleneck, and prefer a materialized view over duplicated columns — it has a single refresh point.
- **App-side pool vs PgBouncer.** One or two services → the app pool suffices; many services or serverless connection churn → PgBouncer, accepting the session-state limits.
- **Scale up vs scale out.** Read replicas push lag handling into the application; a bigger box stays defensible far longer than fashion suggests. Reach for replicas when reads are heavy AND tolerant of staleness, not at the first slow query.
- **JSONB as a schema escape hatch.** One camp treats a jsonb column as pragmatic velocity; the other as a schema you failed to write. The testable boundary: any key you filter, join, or sort on regularly belongs in a real column, because jsonb keys carry no per-key statistics.
