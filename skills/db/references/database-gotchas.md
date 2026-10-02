# Database Gotchas

Cross-engine operational traps. Re-check version-specific DDL behavior against `references/sources.md` before treating any bullet as absolute.

## Connection Traps

- Connection pools exhausted = app hangs or queues silently — size `max_connections` and app pool together; monitor in-use/wait.
- Each Lambda/serverless invocation may open a new connection — put a pooling proxy in front (RDS Proxy, PgBouncer, ProxySQL).
- Connections left open block schema changes — `ALTER TABLE` waits on lingering sessions/transactions.
- Idle connections consume memory and slots — set idle session/client timeouts; kill abandoned `idle in transaction`.

## Transaction Gotchas

- Long transactions hold locks and bloat MVCC (Postgres) — keep transactions short and split batch work.
- Read-only transactions still take snapshots — can delay vacuum/cleanup while open.
- Implicit autocommit varies by driver/database — prefer explicit `BEGIN`/`COMMIT` for multi-statement safety.
- Deadlocks from inconsistent lock ordering — always lock tables/rows in the same global order.
- Lost updates from read-modify-write without locking — use `SELECT … FOR UPDATE`, serializable conflicts, or optimistic version columns.

## Schema Changes

- Adding a column with a volatile/non-constant default rewrote whole tables on older engines — prefer nullable add → backfill → set default/constraint (Postgres 11+ fast default for constant defaults still needs version confirmation).
- Index creation can block writes — use `CREATE INDEX CONCURRENTLY` (Postgres) or online/inplace DDL where the engine supports it; monitor invalid indexes after failed concurrent builds.
- Renaming/dropping columns breaks running binaries — expand-migrate-contract: add new path, dual-read/write, remove old after rollout.
- Dropping a column while old code still selects it causes errors — deploy tolerant code first, then DDL.
- Foreign key checks slow bulk loads — load into staging, validate, then attach constraints; do not leave production without FKs permanently.

## Backup and Recovery

- Logical dumps (`pg_dump`, `mysqldump`) can miss concurrent writes or lock hot tables — prefer consistent snapshots or dump options that guarantee a single snapshot.
- Point-in-time recovery needs WAL/binlog retention configured **before** the incident.
- Backups that were never restored are unproven — schedule restore drills and record RTO/RPO evidence.
- Taking backups only from a lagging replica can encode inconsistency — measure lag; prefer snapshot fencing or primary-consistent methods.

## Replication Traps

- Replication lag means stale reads — check lag before serving read-your-writes from replicas.
- Writes to a replica corrupt or diverge replication — keep replicas read-only at role and network policy layers.
- Schema changes applied unevenly break replication — ship DDL through the same replication/orderly migration path.
- Split-brain after failover loses or forks writes — use fencing/STONITH/lease mechanisms so the old primary cannot accept writes.
- Promoting a replica does not move clients by itself — update service discovery/DSN and drain old connections.

## Query Patterns

- N+1 queries from ORM lazy loading — eager-load, join, or batch by key lists.
- Missing indexes on foreign keys slow joins and cascading deletes — index FK columns used in joins/filters.
- Large `IN` lists become slow planner/memory problems — batch keys or use a temp table/VALUES join.
- `COUNT(*)` on huge heaps is expensive — use estimates, counters, or constrained counts.
- `SELECT` without a bound on unbounded data risks OOM and long locks — always `LIMIT`/keyset paginate large reads.

## Data Integrity

- Application-level unique checks race under concurrency — enforce uniqueness in the database.
- Disabling check constraints for “flexibility” invites silent corruption — keep constraints; batch-validate before enable.
- Orphan rows from missing foreign keys — add FKs after cleanup; prefer restrict/cascade policies that match product semantics.
- Timezone confusion — store UTC instants (or `timestamptz`); convert at the edge for display.
- Floating point for money causes rounding errors — use `DECIMAL`/numeric or integer minor units.

## Scaling Limits

- Single hot table past ~100M rows often needs partitioning/sharding strategy — design before the emergency.
- Autovacuum falling behind causes bloat and bad plans — monitor dead tuple ratio and long transactions blocking cleanup.
- Planner statistics go stale after bulk load — `ANALYZE` (or equivalent) after large imports.
- Connection count does not scale linearly — more sessions increase memory and lock contention; prefer poolers.
- Disk IOPS often bottleneck before CPU — watch I/O wait, checkpoint spikes, and vacuum I/O.

## Positive operator defaults

- Dry-run or expand-only migrations on production-shaped staging first.
- Pair every destructive DDL with a documented rollback window.
- Prefer engine metrics (pool wait, lock waits, lag, bloat) over guesswork after incidents.
