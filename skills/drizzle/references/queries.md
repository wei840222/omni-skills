# Drizzle queries, writes, and transactions

Official anchors: [Select](https://orm.drizzle.team/docs/select), [Insert](https://orm.drizzle.team/docs/insert), [Update](https://orm.drizzle.team/docs/update), [Delete](https://orm.drizzle.team/docs/delete), [Operators](https://orm.drizzle.team/docs/operators), [Joins](https://orm.drizzle.team/docs/joins), [Transactions](https://orm.drizzle.team/docs/transactions), [Query performance](https://orm.drizzle.team/docs/perf-queries), [RQB entry](https://orm.drizzle.team/docs/rqb).

## Two query styles

| Style | API | Use for |
|-------|-----|---------|
| SQL-like builder | `db.select().from(users).where(...)` | Joins, partial column sets, aggregates, set ops |
| Relational query | `db.query.users.findMany({ with: { posts: true } })` | Graph reads declared via `relations()` |

Do not assume Prisma Client method names. Do not pass object-map `where: { id: 5 }`—use `eq(users.id, 5)`.

## Filters

```ts
import { and, eq, gt } from "drizzle-orm";

await db
  .select()
  .from(users)
  .where(and(eq(users.active, true), gt(users.age, 18)))
  .limit(50);
```

- Compose with `and` / `or` / `not` and comparison helpers from `drizzle-orm`.
- Always `await` the query.
- Add `.limit()` (and ordering when paginating). No implicit row cap.

## Inserts / updates / deletes

- Chain `.returning()` when you need the inserted/updated row payload and the dialect supports it (PostgreSQL is the common case; confirm on MySQL/SQLite docs for the installed version).
- Without `returning`, many drivers only give metadata such as row counts—not full row objects.
- Updates and deletes should carry an explicit `where` unless a deliberate full-table operation is requested and confirmed.

## Transactions

```ts
await db.transaction(async (tx) => {
  await tx.insert(users).values({ name: "Ada" });
  await tx.insert(profiles).values({ userId: /* ... */ });
});
```

- Multi-query writes that must commit together use `db.transaction`.
- Use the `tx` handle inside the callback—not the outer `db`—for statements that belong to the unit of work.
- Keep external HTTP/user waits outside the transaction body to avoid holding connections.

## Prepared statements

- After the builder is complete, `.prepare()` can reuse a query plan for hot paths (see performance docs).
- Prepare stable shapes; do not rebuild wildly dynamic SQL when a bound parameter would do.

## Failure modes

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| Type/runtime filter errors after Prisma-like code | Object `where` | Switch to `eq`/`and`/… |
| Promise printed / empty UI data | Missing `await` | Await the builder |
| Full table scan latency | No `limit`/index | Bound rows; verify indexes in SQL skill/engine skill |
| Partial multi-write | No transaction | Wrap in `db.transaction` |
| Insert result missing fields | No `returning` | Add `.returning()` when supported |
