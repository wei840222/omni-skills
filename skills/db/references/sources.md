# db Research Sources

Official documentation used to verify Gate 6 claims. Prefer these over blog summaries. MySQL Reference Manual URLs may block unattended fetchers; claims that need MySQL-specific confirmation should be re-checked in a browser session against the current RefMan.

## PostgreSQL — schema, locks, vacuum

- **ALTER TABLE** — table rewrites, defaults, constraints via https://www.postgresql.org/docs/current/sql-altertable.html
- **DDL altering** — general alter guidance via https://www.postgresql.org/docs/current/ddl-alter.html
- **CREATE INDEX** — including `CONCURRENTLY` via https://www.postgresql.org/docs/current/sql-createindex.html
- **Explicit locking** — lock modes and deadlocks via https://www.postgresql.org/docs/current/explicit-locking.html
- **Transaction isolation** — MVCC isolation levels via https://www.postgresql.org/docs/current/transaction-iso.html
- **MVCC** — snapshot and visibility basics via https://www.postgresql.org/docs/current/mvcc.html
- **Routine vacuuming** — bloat, autovacuum, freezing via https://www.postgresql.org/docs/current/routine-vacuuming.html
- **Populating a database** — bulk load and analyze guidance via https://www.postgresql.org/docs/current/populate.html

## PostgreSQL — connections, types, backup, HA

- **Connection settings** — `max_connections` and related GUCs via https://www.postgresql.org/docs/current/runtime-config-connection.html
- **Resource runtime config** — memory/I/O related settings via https://www.postgresql.org/docs/current/runtime-config-resource.html
- **SELECT** — limiting and query shape via https://www.postgresql.org/docs/current/sql-select.html
- **Numeric types** — exact vs inexact numerics via https://www.postgresql.org/docs/current/datatype-numeric.html
- **Date/time types** — `timestamptz` guidance via https://www.postgresql.org/docs/current/datatype-datetime.html
- **Backup and restore** — dump/PITR overview via https://www.postgresql.org/docs/current/backup.html
- **High availability** — replication/failover concepts via https://www.postgresql.org/docs/current/high-availability.html
- **Don't Do This (wiki)** — common operator foot-guns via https://wiki.postgresql.org/wiki/Don't_Do_This

## Connection pooling

- **PgBouncer usage** — pool modes and server connections via https://www.pgbouncer.org/usage.html
- **Amazon RDS Proxy** — managed pooling for RDS/Aurora via https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy.html

## Format (package gates)

- **Agent Skills specification** — package format via https://agentskills.io/specification
- **skills-ref / agentskills validator** — reference validation tooling via https://github.com/agentskills/agentskills/tree/main/skills-ref

## Engine-specific handoff

When claims are MySQL/MariaDB/SQLite-only, switch to the matching skill and that engine's official manual rather than stretching this generic gotchas pack:

- MariaDB sources pattern: see `skills/mariadb/references/sources.md` after that package is loaded
- Prefer browser-verified MySQL RefMan pages when automation receives HTTP 403 from `dev.mysql.com`
