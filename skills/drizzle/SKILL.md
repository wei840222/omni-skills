---
name: drizzle
description: >
  Design Drizzle ORM schemas, type-safe queries, relations, and drizzle-kit
  migrations for PostgreSQL, MySQL, and SQLite. Use when editing Drizzle table
  definitions, choosing pgTable/mysqlTable/sqliteTable imports, writing
  db.select/insert/update/delete or relational db.query APIs, wiring relations(),
  preparing repeated statements, wrapping multi-step writes in transactions, or
  choosing drizzle-kit push vs generate+migrate. Not for Prisma schema.prisma
  workflows (`prisma`), raw cross-engine SQL without Drizzle (`sql`), or pure
  server admin for MySQL/SQLite engines (`mysql`/`sqlite`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💧","requires":{"bins":["npx"]}}'
  related-skills: '{"backend":"Service architecture around the DB tier beyond Drizzle client usage.","database-manager":"Production migration governance, backups, and incident response outside ORM syntax.","mysql":"MySQL server/engine quirks when the problem is not Drizzle API shape.","nodejs":"Process lifecycle, pools, and shutdown around the Node driver Drizzle wraps.","prisma":"Prisma schema/client workflows when the stack is Prisma-first instead of Drizzle.","sql":"Hand-written SQL, EXPLAIN, and cross-engine query design beneath or beside Drizzle.","sqlite":"SQLite concurrency/pragmas when the issue is the embedded engine, not Drizzle.","typescript":"Type-system depth beyond Drizzle inferred select/insert types."}'
---

# Drizzle

Headless, SQL-shaped TypeScript ORM. Keep driver-specific table helpers, query builders, and kit migration commands aligned with the target engine.

This skill is **stateless**: it does not store local configuration or persistent user state.

## When to load

Load for **Drizzle-first** application data work (schema, query builders, relations, kit):

- schema files using `pgTable` / `mysqlTable` / `sqliteTable`
- `db.select().from(...)`, inserts/updates/deletes, filters with `eq`/`and`/`or`
- relational queries via `db.query.<table>.findMany({ with: ... })`
- `relations()` maps used by the relational query API
- `drizzle-kit generate` / `migrate` / `push` / `pull` / `check` / `studio`
- `$inferSelect` / `$inferInsert`, `.returning()`, `.prepare()`, `db.transaction`

Prefer other skills when the ask is mainly:

- `schema.prisma` / Prisma Client → `prisma`
- dialect-agnostic SQL or EXPLAIN without Drizzle builders → `sql`
- MySQL/SQLite server mechanics → `mysql` / `sqlite`
- production change control / backups → `database-manager`

## Quick reference

| Situation | Play |
|-----------|------|
| Wrong table helper or column import | Match engine: `pg-core` / `mysql-core` / `sqlite-core` only (`references/schema.md`) |
| Prisma-style `where: { id: 5 }` | Use operators: `where: eq(users.id, 5)` (`references/queries.md`) |
| Need nested `with:` relations | Define `relations()` separately; query via `db.query` (`references/relations.md`) |
| Need SQL-like joins/aggregations | Prefer `db.select().from(...)` builders, not RQB (`references/queries.md`) |
| Local prototype schema only | `drizzle-kit push` — no migration history (`references/migrations.md`) |
| Shared/prod schema change | `drizzle-kit generate` then `drizzle-kit migrate` (`references/migrations.md`) |
| Insert/update returns empty shape | Add `.returning()` where the dialect supports it (`references/queries.md`) |
| Multi-statement write integrity | `db.transaction(async (tx) => { ... })` (`references/queries.md`) |
| Hot path reuses same SQL | `.prepare()` after the builder is complete (`references/queries.md`) |
| PG JSON document column | `jsonb()` (not MySQL `json()`) (`references/schema.md`) |
| Unbounded `findMany`/`select` | Always add `.limit()` / pagination (`references/queries.md`) |

## Progressive disclosure

| File | Load when |
|------|-----------|
| `references/schema.md` | Declaring tables, columns, drivers, inferred types |
| `references/queries.md` | Select/insert/update/delete, filters, transactions, prepare |
| `references/relations.md` | `relations()` maps and relational query API |
| `references/migrations.md` | drizzle-kit push/generate/migrate/pull/check |
| `references/sources.md` | Verifying claims against official Drizzle docs |

## Core rules

1. **One driver core per schema file set.** Mixing `pgTable` with `mysql-core` columns type-checks poorly and fails at runtime—pick PostgreSQL, MySQL, or SQLite helpers consistently.
2. **Export tables the relational API must see.** RQB and many tooling paths require tables (and relations) to be exported from the schema module graph.
3. **Operators are functions, not object bags.** `eq`, `and`, `or`, `gt`, … live in `drizzle-orm`; Prisma/object filters are invalid.
4. **Keep `relations()` out of the table callback.** Table schemas declare columns/constraints; relations are a separate `relations(table, callback)` declaration.
5. **Push is not a migration history.** Production and shared databases use `generate` + `migrate`. Treat `push` as disposable convergence for local/dev only.
6. **Do not hand-edit applied migration hashes lightly.** Prefer regenerate or intentional custom SQL under kit’s migration workflow; broken journal/hash state blocks deploys.
7. **Await every query.** Builders return promises—forgetting `await` yields a Promise, not rows.
8. **Bound reads.** Add `.limit()` (and stable order keys when paginating); Drizzle does not default a row cap.
9. **Credentials stay out of the skill and git.** Use env/runtime secrets for database URLs; examples use placeholders only.

## Default answer shape

1. Confirm engine (Postgres / MySQL / SQLite) and whether the task is schema, query, or migration.
2. Show the minimal Drizzle-typed snippet with correct imports.
3. Call out the matching failure mode (wrong driver import, object `where`, push-in-prod, missing `returning`, missing `limit`).
4. Point to one reference file above for depth—do not dump all references.

## Anti-patterns to avoid

- Do not restate long negative catalogs; route with positive engine/query/migration plays above.
- Do not dump every reference file on simple asks—load one matching file.
- Do not invent drizzle-kit flags or dialect types; open `references/sources.md` links.
