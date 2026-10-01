# MariaDB Research Sources

Official documentation used to verify Gate 6 claims. Prefer these over blog summaries.

## Character sets and collations

- **Character Sets** — table/connection charset and collation guidance via https://mariadb.com/kb/en/character-sets/
- **SET statement** — session variables including charset-related settings via https://mariadb.com/kb/en/set-statement/

## Indexes and query plans

- **Getting Started with Indexes** — index kinds and design basics via https://mariadb.com/kb/en/getting-started-with-indexes/
- **EXPLAIN** — plan inspection via https://mariadb.com/kb/en/explain/

## Sequences and temporal tables

- **Sequence Overview** — `CREATE SEQUENCE` / `NEXT VALUE FOR` via https://mariadb.com/kb/en/sequence-overview/
- **System-Versioned Tables** — system versioning and `FOR SYSTEM_TIME` via https://mariadb.com/kb/en/system-versioned-tables/

## JSON

- **JSON Functions** — `JSON_VALUE`, `JSON_QUERY`, `JSON_TABLE`, validation helpers via https://mariadb.com/kb/en/json-functions/

## Clustering and concurrency

- **About Galera Replication** — multi-primary certification basics via https://mariadb.com/kb/en/about-galera-replication/
- **Thread Pool in MariaDB** — `thread_handling=pool-of-threads` via https://mariadb.com/kb/en/thread-pool-in-mariadb/
- **LOCK TABLES** — coarse table locks via https://mariadb.com/kb/en/lock-tables-and-unlock-tables/
- **Server System Variables** — timeouts, connections, engine tunables via https://mariadb.com/kb/en/server-system-variables/

## Engines

- **Storage Engines** — engine catalog via https://mariadb.com/kb/en/storage-engines/
- **InnoDB** — default transactional engine via https://mariadb.com/kb/en/innodb/
- **Aria** — crash-safe MyISAM-oriented alternative path via https://mariadb.com/kb/en/aria/

## Window functions

- **Window Functions** — ranking, analytic frames, related syntax via https://mariadb.com/kb/en/window-functions/

## Backup and recovery

- **mariadb-dump** — logical dumps via https://mariadb.com/kb/en/mariadb-dump/
- **MariaBackup Overview** — hot physical backup via https://mariadb.com/kb/en/mariabackup-overview/

## Specification (format gates)

- **Agent Skills specification** — package format via https://agentskills.io/specification
- **skills-ref / agentskills validator** — reference validation tooling via https://github.com/agentskills/agentskills/tree/main/skills-ref
