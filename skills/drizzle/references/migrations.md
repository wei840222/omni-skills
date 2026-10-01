# drizzle-kit migrations

Official anchors: [Migrations overview](https://orm.drizzle.team/docs/migrations), [Kit overview](https://orm.drizzle.team/docs/kit-overview), [`generate`](https://orm.drizzle.team/docs/drizzle-kit-generate), [`migrate`](https://orm.drizzle.team/docs/drizzle-kit-migrate), [`push`](https://orm.drizzle.team/docs/drizzle-kit-push), [drizzle.config.ts](https://orm.drizzle.team/docs/drizzle-config-file), [Team migrations](https://orm.drizzle.team/docs/kit-migrations-for-teams).

## Command roles

| Command | Role | Safe default context |
|---------|------|----------------------|
| `drizzle-kit push` | Push schema directly to the database without writing migration history | Local prototypes / disposable databases only |
| `drizzle-kit generate` | Diff schema → migration SQL files + journal metadata | Development when history is required |
| `drizzle-kit migrate` | Apply pending migration files | CI / shared / production deploys |
| `drizzle-kit pull` | Introspect DB → schema artifacts | Brownfield import |
| `drizzle-kit check` | Validate migration consistency | CI guardrail |
| `drizzle-kit studio` | Browse data via kit studio | Local debugging |

## Production posture

1. Model schema in TypeScript.
2. `drizzle-kit generate` to create SQL migrations.
3. Review SQL (renames, drops, locks) before merge.
4. `drizzle-kit migrate` in deploy pipelines—**do not** run `push` there.
5. Commit migration folders and meta journals the team relies on; do not “fix drift” by editing already-applied SQL without a deliberate team process.

## Config

Use `drizzle.config.ts` for dialect, schema paths, and migrations output. Database credentials come from environment variables / secrets managers—never from skill files or committed plaintext URLs with passwords.

Optional kit flags such as stricter schema checks belong in project config when the team wants drift caught early; confirm exact option names on the current config docs rather than memorizing flags.

## Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Prod schema changed with no files | Someone used `push` or manual DDL | Stop push-in-prod; baseline/generate deliberately |
| Hash / journal mismatch after editing SQL | Hand-edited applied migration | Restore history or follow team custom-migration process |
| Rename became drop+add | Diff matched by identity poorly | Adjust schema mapping / review generated SQL before apply |
| CI applies different SQL than dev | Uncommitted migrations or multiple configs | Single config path; commit generated assets |
