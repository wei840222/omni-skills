# MySQL Research Sources

Official documentation used to verify Gate 6 claims. Prefer these over blog summaries.

## Character sets and collations
- **MySQL 8.0 Reference Manual — utf8mb4 Character Set** — 4-byte UTF-8 guidance via https://dev.mysql.com/doc/refman/8.0/en/charset-unicode-utf8mb4.html
- **MySQL 8.0 Reference Manual — Character Sets and Collations** — connection/schema charset behavior via https://dev.mysql.com/doc/refman/8.0/en/charset.html

## Indexes and generated columns
- **CREATE INDEX** — prefix lengths and index limits via https://dev.mysql.com/doc/refman/8.0/en/create-index.html
- **Generated Columns** — expression-index substitute via https://dev.mysql.com/doc/refman/8.0/en/create-table-generated-columns.html

## Transactions, locking, upsert
- **InnoDB Transaction Isolation Levels** — REPEATABLE READ / gap locks via https://dev.mysql.com/doc/refman/8.0/en/innodb-transaction-isolation-levels.html
- **INSERT ... ON DUPLICATE KEY UPDATE** — upsert semantics via https://dev.mysql.com/doc/refman/8.0/en/insert-on-duplicate.html
- **REPLACE Statement** — delete-then-insert side effects via https://dev.mysql.com/doc/refman/8.0/en/replace.html

## Engines, explain, replication
- **InnoDB and MyISAM** — engine capabilities via https://dev.mysql.com/doc/refman/8.0/en/innodb-introduction.html and https://dev.mysql.com/doc/refman/8.0/en/myisam-storage-engine.html
- **EXPLAIN / EXPLAIN ANALYZE** — plan inspection via https://dev.mysql.com/doc/refman/8.0/en/explain.html
- **Replication Formats** — statement vs row-based via https://dev.mysql.com/doc/refman/8.0/en/replication-formats.html
- **Server System Variables** — `max_connections`, `wait_timeout`, buffer pool via https://dev.mysql.com/doc/refman/8.0/en/server-system-variables.html
