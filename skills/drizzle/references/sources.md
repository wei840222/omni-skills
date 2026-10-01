# Sources — Drizzle

Gate 6 research anchors. Prefer these official pages over model memory when APIs, kit commands, or dialect types may have drifted.

## Primary documentation

| Source | Use for | URL |
|--------|---------|-----|
| Drizzle ORM overview | Product framing, entry points | https://orm.drizzle.team/docs/overview |
| llms.txt index | Machine-readable doc map | https://orm.drizzle.team/llms.txt |
| SQL schema declaration | Table/schema fundamentals | https://orm.drizzle.team/docs/sql-schema-declaration |
| Relations | Soft relations maps | https://orm.drizzle.team/docs/relations |
| Relations schema declaration | Relation fundamentals | https://orm.drizzle.team/docs/relations-schema-declaration |
| Relational queries (RQB) | `db.query` graph reads | https://orm.drizzle.team/docs/rqb |
| Select / Insert / Update / Delete | SQL-like builders | https://orm.drizzle.team/docs/select · https://orm.drizzle.team/docs/insert · https://orm.drizzle.team/docs/update · https://orm.drizzle.team/docs/delete |
| Operators | `eq`/`and`/comparisons | https://orm.drizzle.team/docs/operators |
| Joins | Explicit joins | https://orm.drizzle.team/docs/joins |
| Transactions | `db.transaction` | https://orm.drizzle.team/docs/transactions |
| Query performance | Limits, prepare, hot paths | https://orm.drizzle.team/docs/perf-queries |
| Migrations overview | Migration model | https://orm.drizzle.team/docs/migrations |
| Kit overview | drizzle-kit surface | https://orm.drizzle.team/docs/kit-overview |
| generate / migrate / push | Kit command roles | https://orm.drizzle.team/docs/drizzle-kit-generate · https://orm.drizzle.team/docs/drizzle-kit-migrate · https://orm.drizzle.team/docs/drizzle-kit-push |
| drizzle.config.ts | Kit configuration | https://orm.drizzle.team/docs/drizzle-config-file |
| Gotchas | Known sharp edges | https://orm.drizzle.team/docs/gotchas |

## Dialects and get-started

| Source | URL |
|--------|-----|
| PostgreSQL column types | https://orm.drizzle.team/docs/column-types/pg |
| MySQL column types | https://orm.drizzle.team/docs/column-types/mysql |
| SQLite column types | https://orm.drizzle.team/docs/column-types/sqlite |
| PostgreSQL get started | https://orm.drizzle.team/docs/get-started/postgresql-new |
| MySQL get started | https://orm.drizzle.team/docs/get-started/mysql-new |
| SQLite get started | https://orm.drizzle.team/docs/get-started/sqlite-new |
| Connect overview | https://orm.drizzle.team/docs/connect-overview |

## Verification notes (handoff 2026-10-02)

- Confirmed HTTP 200 from this runner: overview, sql-schema-declaration, rqb, select, insert, update, delete, transactions, migrations, drizzle-kit generate/migrate/push, relations, perf-queries, column-types pg/mysql/sqlite, get-started postgresql/mysql/sqlite, operators, joins, indexes-constraints, schemas, connect-overview, kit-overview, gotchas, llms.txt.
- Legacy paths `docs/connect-postgresql`, `docs/connect-mysql`, `docs/connect-sqlite`, and `docs/data-types` returned 404—use get-started + column-types + connect-overview instead.
- Kit option names and RQB major versions drift; re-open the linked pages before asserting flag-level behavior beyond push vs generate+migrate.
- No vendor pricing or third-party benchmark claims are embedded.

## Domain corrections applied in this refactor

- Removed clawic.com homepage / `_meta.json` catalog metadata.
- Replaced object-style filter guidance risk with explicit operator-function rules.
- Split push (dev) from generate+migrate (shared/prod) as a hard routing rule.
- Documented engine-specific JSON helpers (`jsonb` vs `json`) and table helper packages.
- Marked skill stateless (no Clawic data paths).
