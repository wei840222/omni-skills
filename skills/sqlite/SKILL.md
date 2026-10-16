---
name: sqlite
description: >
  Write correct SQLite queries, schemas, and pragmas for embedded or local
  databases. Use when enabling WAL and busy_timeout, diagnosing SQLITE_BUSY,
  turning on foreign keys per connection, choosing type affinity or STRICT
  tables, planning ALTER TABLE / DROP COLUMN, reading EXPLAIN QUERY PLAN, batching inserts, vacuuming,
  safely backing up a live database, or sharing an in-memory DB via a shared-cache URI. Prefer `sql` for cross-engine SQL craft,
  `pg` / `mysql` for server engines, and `backups` for policy-level backup
  design beyond SQLite file/API mechanics.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🪶","requires":{"bins":["sqlite3"]}}'
  related-skills: '{"sql":"Cross-engine SQL craft, EXPLAIN patterns, and migrations when the ask is not SQLite-specific.","pg":"PostgreSQL server internals once the workload outgrows single-writer SQLite.","mysql":"MySQL/InnoDB production patterns when the target engine is MySQL rather than SQLite.","backups":"Backup policy, retention, and restore drills beyond SQLite .backup / VACUUM INTO mechanics."}'
---

# SQLite

SQLite-specific concurrency, pragmas, types, schema changes, and maintenance for
embedded or local databases. This skill is knowledge-only: it does not store
local configuration or persistent user state.

## Core path

1. Confirm you need **embedded / single-writer** storage; hand high-write multi-user apps to a server engine via `pg` / `mysql`.
2. On every connection that writes under concurrency: set `PRAGMA journal_mode=WAL` and `PRAGMA busy_timeout=…`.
3. On every connection that relies on FKs: `PRAGMA foreign_keys=ON` (not persisted).
4. Prefer explicit `INTEGER PRIMARY KEY` over unstable ROWIDs; use `STRICT` only on SQLite ≥ 3.37.
5. Load only the one reference file needed for the current job.

## Depth on demand

| Need | Load |
| --- | --- |
| WAL, busy_timeout, BEGIN IMMEDIATE, batch inserts, SAVEPOINT | `references/concurrency.md` |
| Type affinity, STRICT, FK pragma, ALTER / DROP COLUMN limits | `references/schema.md` |
| cache_size, indexes, VACUUM, `.backup`, VACUUM INTO | `references/maintenance.md` |
| Official docs for version-sensitive claims | `references/sources.md` |

Server-engine vacuum/work_mem tuning and ORM schema modeling stay out of scope (`pg`, `mysql`, and `prisma` via `sql`).

## Common traps

- High-write web app on SQLite — one writer blocks; route to `pg` / `mysql`.
- Relying on ROWID after `VACUUM` — use an explicit `INTEGER PRIMARY KEY`.
- Skipping `busy_timeout` — intermittent `SQLITE_BUSY` under light concurrency.
- `':memory:'` per connection — each handle gets a different DB; use `file::memory:?cache=shared` when sharing is required.
- Copying DB files while a writer is active — use `.backup` / backup API instead.
