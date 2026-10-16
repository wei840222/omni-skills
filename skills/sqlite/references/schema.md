# Schema & Types

## Type system

- Columns use **type affinity**, not rigid types — an `INTEGER` column can store the text `"hello"` without error unless the table is `STRICT`.
- `STRICT` tables enforce declared types — requires SQLite **3.37+** (2021).
- No native `DATE` / `TIME` — store `TEXT` as ISO-8601 or `INTEGER` Unix time.
- No native `BOOLEAN` — use `INTEGER` 0/1; `TRUE` / `FALSE` are aliases for 1/0.
- `REAL` is an 8-byte float with the usual floating-point precision limits.

Official detail: https://www.sqlite.org/datatype3.html and https://www.sqlite.org/stricttables.html

## Foreign keys (off by default)

- `PRAGMA foreign_keys=ON` must be set **per connection** — it is not stored in the database file.
- Without it, FK constraints are silently ignored.
- Check with `PRAGMA foreign_keys` (returns 0 or 1).
- `ON DELETE CASCADE` only runs when foreign keys are enabled for that connection.

Official detail: https://www.sqlite.org/foreignkeys.html

## ALTER TABLE limits

- Supported forms include `ADD COLUMN`, `RENAME TABLE`, `RENAME COLUMN`, and (since 3.35.0) `DROP COLUMN`.
- `ADD COLUMN` may **not** add a `PRIMARY KEY` or `UNIQUE` constraint.
- `ADD COLUMN … NOT NULL` requires a `DEFAULT` value so existing rows can be filled.
- `DROP COLUMN` fails if the column is a `PRIMARY KEY`, has a `UNIQUE` constraint, or is referenced elsewhere in the schema.
- Changing column type or adding many constraints still usually means: create new table → copy → drop old → rename, wrapped in a transaction.

Official detail: https://www.sqlite.org/lang_altertable.html
