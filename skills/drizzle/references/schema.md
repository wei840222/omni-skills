# Drizzle schema and drivers

Official anchors: [SQL schema declaration](https://orm.drizzle.team/docs/sql-schema-declaration), [PostgreSQL column types](https://orm.drizzle.team/docs/column-types/pg), [MySQL column types](https://orm.drizzle.team/docs/column-types/mysql), [SQLite column types](https://orm.drizzle.team/docs/column-types/sqlite), [Get started PostgreSQL](https://orm.drizzle.team/docs/get-started/postgresql-new), [Get started MySQL](https://orm.drizzle.team/docs/get-started/mysql-new), [Get started SQLite](https://orm.drizzle.team/docs/get-started/sqlite-new).

## Driver table helpers

| Engine | Table helper | Column import package |
|--------|--------------|------------------------|
| PostgreSQL | `pgTable` | `drizzle-orm/pg-core` |
| MySQL | `mysqlTable` | `drizzle-orm/mysql-core` |
| SQLite | `sqliteTable` | `drizzle-orm/sqlite-core` |

Rules:

- Do not mix helpers across engines in one logical schema aimed at a single database.
- Shared “generic” column imports across drivers are a defect even when TypeScript appears quiet.
- Connection setup is driver-specific (node-postgres, postgres.js, mysql2, better-sqlite3, libsql, D1, etc.)—follow the matching get-started guide for the runtime.

## Table definition habits

- Export every table that queries, relations, or kit must see.
- Prefer explicit column helpers (`serial`, `text`, `boolean`, `integer`, …) from the **same** core package as the table helper.
- Keep constraints/indexes with the schema API documented for that dialect (`primaryKey`, `unique`, index helpers).
- Infer types from the table:
  - `type User = typeof users.$inferSelect`
  - `type NewUser = typeof users.$inferInsert`
- `$inferSelect` includes defaults/generated shapes suitable for reads; `$inferInsert` keeps insert-time optionality—do not treat them as identical.

## JSON and dialect-sensitive columns

- PostgreSQL document JSON: prefer `jsonb()` from `pg-core` unless you have a deliberate `json()` reason.
- MySQL JSON: `json()` from `mysql-core`.
- SQLite: JSON is typically text affinity with application-level JSON—do not copy PG `jsonb()` APIs into sqlite-core.

Verify uncommon types (uuid, numeric, enums, arrays) on the dialect column-types page for the installed drizzle-orm major.

## Config surface

Application runtime uses a DB client + `drizzle(client, { schema })` pattern from the get-started guides. Schema path and dialect for migrations belong in `drizzle.config.ts` (see `references/migrations.md`), not hard-coded secrets.
