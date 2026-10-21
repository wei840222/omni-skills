# Sources — PostgreSQL

Last checked: 2026-10-21

Reachability was checked during the 2026-10-21 takeover handoff. Prefer the live PostgreSQL documentation over package summaries for version-gated planner, DDL, vacuum, replication, and security claims.

## Core documentation

- PostgreSQL documentation index (reachable 200): https://www.postgresql.org/docs/current/index.html
- Using EXPLAIN (reachable 200): https://www.postgresql.org/docs/current/using-explain.html
- Indexes overview (reachable 200): https://www.postgresql.org/docs/current/indexes.html
- CREATE INDEX (reachable 200): https://www.postgresql.org/docs/current/sql-createindex.html
- ALTER TABLE (reachable 200): https://www.postgresql.org/docs/current/sql-altertable.html
- Routine vacuuming (reachable 200): https://www.postgresql.org/docs/current/routine-vacuuming.html
- Runtime configuration (reachable 200): https://www.postgresql.org/docs/current/runtime-config.html
- Explicit locking (reachable 200): https://www.postgresql.org/docs/current/explicit-locking.html
- MVCC / concurrency (reachable 200): https://www.postgresql.org/docs/current/mvcc.html

## Schema, JSON, search, and load

- Table partitioning (reachable 200): https://www.postgresql.org/docs/current/ddl-partitioning.html
- JSON Types (reachable 200): https://www.postgresql.org/docs/current/datatype-json.html
- Full text search (reachable 200): https://www.postgresql.org/docs/current/textsearch.html
- pg_trgm (reachable 200): https://www.postgresql.org/docs/current/pgtrgm.html
- Populating a database (reachable 200): https://www.postgresql.org/docs/current/populate.html
- SELECT (reachable 200): https://www.postgresql.org/docs/current/sql-select.html
- INSERT (reachable 200): https://www.postgresql.org/docs/current/sql-insert.html

## Availability, backup, security, client

- High availability / warm standby (reachable 200): https://www.postgresql.org/docs/current/warm-standby.html
- High availability overview (reachable 200): https://www.postgresql.org/docs/current/high-availability.html
- Backup and restore (reachable 200): https://www.postgresql.org/docs/current/backup.html
- Row security policies (reachable 200): https://www.postgresql.org/docs/current/ddl-rowsecurity.html
- CREATE POLICY (reachable 200): https://www.postgresql.org/docs/current/sql-createpolicy.html
- Client authentication (pg_hba.conf) (reachable 200): https://www.postgresql.org/docs/current/auth-pg-hba-conf.html
- Authentication methods (reachable 200): https://www.postgresql.org/docs/current/auth-methods.html
- pgcrypto (reachable 200): https://www.postgresql.org/docs/current/pgcrypto.html
- psql (reachable 200): https://www.postgresql.org/docs/current/app-psql.html
- pgbench (reachable 200): https://www.postgresql.org/docs/current/pgbench.html

## Adjacent tools and vectors

- PgBouncer usage (reachable 200): https://www.pgbouncer.org/usage.html
- pgvector repository (reachable 200): https://github.com/pgvector/pgvector

## Skill format

- Agent Skills specification (reachable 200): https://agentskills.io/specification

## Notes

- `https://www.postgresql.org/docs/current/row-security.html` returned 404 from this runner; use `ddl-rowsecurity.html` and `sql-createpolicy.html` instead.
- Managed-provider consoles (RDS, Aurora, Cloud SQL, Neon, Supabase) change often; treat provider-specific limits as live facts and re-check the vendor page before locking a migration or parameter-group claim.
