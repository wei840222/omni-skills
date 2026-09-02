# MySQL Domain Knowledge

MySQL is an open-source relational database commonly deployed with the InnoDB storage engine for transactional workloads.

## Verified operating rules
- Prefer InnoDB for application data needing transactions, row-level locking, foreign keys, and crash recovery.
- Use `utf8mb4` (not legacy `utf8`) whenever text may include emoji or other 4-byte Unicode.
- Prefer prepared statements / parameterized queries; do not assemble SQL by string concatenation with untrusted input.
- Treat version-sensitive syntax (`EXPLAIN ANALYZE`, expression indexes, replication status column names) as release-dependent and verify on the target server.

## Freshness boundary
Confirm exact syntax against the installed MySQL major/minor version before applying production DDL or replication assumptions.
