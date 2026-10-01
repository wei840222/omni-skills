# Drizzle relations and relational queries

Official anchors: [Drizzle Relations](https://orm.drizzle.team/docs/relations), [Relations schema declaration](https://orm.drizzle.team/docs/relations-schema-declaration), [RQB](https://orm.drizzle.team/docs/rqb).

## Separate relations from table columns

Declare tables with `pgTable` / `mysqlTable` / `sqliteTable`, then declare relations with `relations(table, ({ one, many }) => ({ ... }))` in a separate call. Do not embed relation graphs inside the table column callback.

```ts
import { relations } from "drizzle-orm";
import { pgTable, serial, text, integer } from "drizzle-orm/pg-core";

export const users = pgTable("users", {
  id: serial("id").primaryKey(),
  name: text("name").notNull(),
});

export const posts = pgTable("posts", {
  id: serial("id").primaryKey(),
  ownerId: integer("owner_id").notNull(),
  title: text("title").notNull(),
});

export const usersRelations = relations(users, ({ many }) => ({
  posts: many(posts),
}));

export const postsRelations = relations(posts, ({ one }) => ({
  author: one(users, {
    fields: [posts.ownerId],
    references: [users.id],
  }),
}));
```

## Wiring for `db.query`

- Pass the schema object that includes **tables and relations** into `drizzle(client, { schema })`.
- Relational queries look like `db.query.users.findMany({ with: { posts: true }, limit: 20 })`.
- SQL-like `db.select().from(users).leftJoin(...)` remains available when you need explicit join control; RQB does not replace every join shape.

## Rules of thumb

- Export relation maps the same way you export tables—private non-exported relations are a common “`with` does nothing / types miss relation” cause.
- Keep foreign-key columns on the table schema; relations describe how RQB navigates them.
- Disambiguate multiple relations between the same pair of tables using the documented relation naming fields on the official relations page.
- When upgrading across major relational-query generations, read the project’s upgrade notes (`v0 → v1`, RQB v1→v2) before rewriting call sites.
