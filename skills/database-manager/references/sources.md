# Sources — database-manager

Gate 6 research anchors for relational database operations. Prefer primary vendor docs and standards over listicles. Re-verify engine-specific lock, backup, and restore flags before quoting exact commands.

## Migrations and zero-downtime patterns

- [expand/contract pattern overview (Prisma docs — expanding and contracting)](https://www.prisma.io/docs/orm/prisma-migrate/workflows/development-and-production) — staged schema evolution and production migration discipline.
- [PostgreSQL ALTER TABLE notes](https://www.postgresql.org/docs/current/sql-altertable.html) — lock levels and concurrent-safe operations vary by clause; check current version docs before production DDL.
- [MySQL Online DDL overview](https://dev.mysql.com/doc/refman/8.4/en/innodb-online-ddl-operations.html) — in-place vs copy algorithms and concurrent DML behavior.
- [SQLite ALTER TABLE](https://www.sqlite.org/lang_altertable.html) — limited ALTER surface; table-rebuild patterns for complex changes.

## Query safety, locks, and plans

- [PostgreSQL explicit locking](https://www.postgresql.org/docs/current/explicit-locking.html) — row/table lock modes and deadlock behavior.
- [PostgreSQL EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) — plan shape verification after index/query changes.
- [MySQL EXPLAIN output format](https://dev.mysql.com/doc/refman/8.4/en/explain-output.html) — access type and key usage checks.
- [SQL transaction isolation levels (SQL standard summary via PostgreSQL)](https://www.postgresql.org/docs/current/transaction-iso.html) — isolation trade-offs for bulk writes and verification reads.

## Backup, restore, and recovery objectives

- [PostgreSQL backup and restore](https://www.postgresql.org/docs/current/backup.html) — logical vs physical backups and PITR concepts.
- [MySQL backup and recovery](https://dev.mysql.com/doc/refman/8.4/en/backup-and-recovery.html) — dump, binary log, and recovery paths.
- [SQLite backup API](https://www.sqlite.org/backup.html) — online backup considerations for file-backed DBs.
- [NIST SP 800-34 contingency planning concepts](https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final) — RTO/RPO framing for recovery objectives (adapt to team scale).

## Incident and change control

- [Google SRE — Managing Incidents](https://sre.google/sre-book/managing-incidents/) — role clarity, communication, and follow-up discipline.
- [OWASP Database Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html) — least privilege, secrets, and destructive-op hygiene boundaries.
