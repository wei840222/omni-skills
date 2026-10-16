# Performance & Maintenance

## Performance pragmas

- `PRAGMA optimize` before closing long-lived connections — refreshes query-planner stats.
- `PRAGMA cache_size=-64000` ≈ 64 MB cache (negative values are KiB); the default is small.
- With WAL, `PRAGMA synchronous=NORMAL` is a common durability/speed balance.
- `PRAGMA temp_store=MEMORY` keeps temp tables in RAM for faster sorts.

Official detail: https://www.sqlite.org/pragma.html

## Indexing

- Covering indexes can avoid table lookups by including needed columns.
- Partial indexes (3.8+): `CREATE INDEX … WHERE condition`.
- Expression indexes (3.9+): `CREATE INDEX ON t(lower(name))`.
- Inspect plans with `EXPLAIN QUERY PLAN`.

Official detail: https://www.sqlite.org/eqp.html

## Vacuum & space reclaim

- Deletes do not shrink the file; `VACUUM` rewrites the whole database.
- `VACUUM` temporarily needs roughly **2×** free disk space.
- Incremental reclaim: `PRAGMA auto_vacuum=INCREMENTAL` then `PRAGMA incremental_vacuum`.
- After bulk deletes, vacuum (or incremental vacuum) or the file stays bloated.

Official detail: https://www.sqlite.org/lang_vacuum.html

## Backup safety

- Prefer online backup: sqlite3 `.backup` or the `sqlite3_backup_*` C API while the DB is open.
- Copying the main file (and `-wal` / `-shm`) as ordinary files while a writer is active can corrupt the copy.
- `VACUUM INTO 'backup.db'` (3.27+) writes a standalone consistent copy.

Official detail: https://www.sqlite.org/backup.html
