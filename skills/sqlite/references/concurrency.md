# Concurrency & Transactions

## Single-writer model

- Only one writer at a time — concurrent writes queue or fail with `SQLITE_BUSY`.
- Prefer a server engine (`pg` / `mysql`) when many writers must proceed in parallel.

## WAL and busy timeout

- Enable WAL: `PRAGMA journal_mode=WAL` — readers continue during a write.
- Set a wait: `PRAGMA busy_timeout=5000` (milliseconds) so SQLite waits before returning `SQLITE_BUSY`.
- WAL creates `-wal` and `-shm` sidecar files; include them whenever you copy a live WAL database as raw files.
- Grab the write lock early with `BEGIN IMMEDIATE` for read-then-write flows to reduce deadlocks.

Official detail: https://www.sqlite.org/wal.html and https://www.sqlite.org/pragma.html#pragma_busy_timeout

## Transactions

- Autocommit is the default — each statement is its own transaction; bulk inserts are slow that way.
- Batch: `BEGIN; INSERT…; INSERT…; COMMIT` (often 10–100× faster).
- `BEGIN EXCLUSIVE` takes an exclusive lock and blocks other connections.
- Nested work uses `SAVEPOINT name` / `RELEASE name` / `ROLLBACK TO name`.
