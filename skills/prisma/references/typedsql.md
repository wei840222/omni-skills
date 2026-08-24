# Prisma TypedSQL

TypedSQL is a feature in Prisma that allows developers to write raw SQL while retaining Prisma Client's type safety.

## Using TypedSQL

TypedSQL shifts the pattern from writing raw SQL strings in TypeScript to writing `.sql` files in a dedicated directory, which Prisma then types and exposes as methods on the client.

1. **Enable the feature**: Add `typedSql` to the `previewFeatures` array in the generator block of `schema.prisma`.
2. **Write SQL**: Create a `.sql` file in the `prisma/sql` directory (e.g., `prisma/sql/getUsersWithPosts.sql`).
3. **Generate**: Run `prisma generate`. Prisma will generate a TypedSQL method on the Prisma Client.
4. **Call the query**: The query can be called via `$queryRawTyped` (e.g., `prisma.$queryRawTyped(getUsersWithPosts(userId))`).

## Benefits

- Full type safety for raw SQL queries.
- Prevents SQL injection by default since variables are parameterized.
- Easier to read and maintain complex SQL queries compared to inline string templates.
- Works natively with Prisma Client extensions.

## Constraints

- Requires Prisma version 5.19.0 or newer.
- Only works for PostgreSQL and MySQL (SQLite and SQL Server not fully supported for all advanced TypedSQL features in early access).
