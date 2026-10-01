# MariaDB Domain Knowledge

Version-sensitive notes and MariaDB-vs-MySQL deltas. Prefer `references/sources.md` URLs over memory when refreshing claims.

## Identity first

- Always read `SELECT VERSION()` / `SHOW VARIABLES LIKE 'version%'` before asserting syntax.
- MariaDB and MySQL diverged; do not paste MySQL-only features into MariaDB runbooks without checking MariaDB KB.
- Client binary may be `mariadb` even when talking to mixed estates—confirm server, not only CLI name.

## Charset and collation

- `utf8mb4` is the correct default for full Unicode.
- Collation mismatches on JOINs remain a top silent performance bug.
- Connection charset must match table defaults or comparisons surprise you at runtime.

## Sequences vs AUTO_INCREMENT

- MariaDB sequences are first-class when you need portable counters or pre-insert IDs.
- Do not assume sequence rollback semantics match every auto-increment mental model—verify for the version in use.
- Resetting sequences (`SETVAL` and peers) is a migration operation, not an app hot path.

## System versioning

- System-versioned tables add history storage and query syntax (`FOR SYSTEM_TIME ...`).
- History retention and purge policy are product decisions; unbounded versioning is a disk incident waiting to happen.
- Application code should not invent ad-hoc history tables when system versioning already matches the requirement—and vice versa when auditing needs differ.

## Galera

- Certification-based replication: write conflicts abort one transaction.
- Causal reads may need `wsrep_sync_wait` (or equivalent) around critical sessions.
- Odd node counts help quorum clarity; ops still need fencing and backup strategy outside the cluster.

## Thread pool and engines

- Thread pool helps high-churn connection workloads; measure with status counters.
- InnoDB remains the default durable engine for app data.
- Aria/MEMORY have specific roles; do not switch engines for fashion.

## Backup truth

- Logical dump ≠ physical backup ≠ binlog PITR. Choose deliberately.
- MariaBackup is the hot physical path for InnoDB estates when dump windows are too large.
- Untested restores are not backups.

## Common false friends with MySQL

- JSON function names and availability differ by version—check KB before teaching a function as universal.
- Optimizer hints and `EXPLAIN ANALYZE` availability differ; gate advice on the running version.
- Replication topology vocabulary (async primary/replica vs Galera) must stay explicit in runbooks.
