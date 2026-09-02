# MySQL Domain Knowledge

MySQL is a widely used open-source relational database management system.

## Best Practices
- **Storage Engine**: InnoDB should always be preferred over MyISAM for features like transactions, row-level locking, foreign keys, and crash recovery.
- **Character Sets**: Utilize `utf8mb4` to support 4-byte characters like emojis; `utf8` in MySQL defaults to a maximum of 3 bytes per character.
- **Security**: Prevent SQL injection by using prepared statements rather than dynamically assembling SQL queries in code.
