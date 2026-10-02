# Cassandra data modeling and CQL practices

Load this file for table design, query restrictions, consistency, tombstones, batches, LWT, collections, and anti-patterns. Operational repair/compaction commands live in `ops-and-recovery.md`. Source URLs live in `sources.md`.

## Query-first modeling

- Design tables around **application queries**, not normalized entities. Cassandra does not perform relational joins for app access paths.
- Prefer **one table per query pattern**; duplicate attributes across tables when different filters or sort orders are required.
- Start from concrete SELECT shapes (and UI wireflows when available), then derive partition and clustering keys.
- Keep a keyspace per application as the common default; set replication strategy and factor at keyspace level.

## Primary keys

- `PRIMARY KEY (a, b, c)`: `a` is the partition key; `b` and `c` are clustering columns.
- `PRIMARY KEY ((a, b), c)`: compound partition key `(a, b)` with clustering `c`.
- Clustering columns define on-disk order inside a partition. Range queries and `ORDER BY` must respect that prefix order.
- Filtering by clustering columns still requires the full partition key (unless an approved index path exists).

### Example: latest logs per user

```cql
CREATE TABLE user_logs (
  user_id uuid,
  log_timestamp timestamp,
  body text,
  PRIMARY KEY (user_id, log_timestamp)
) WITH CLUSTERING ORDER BY (log_timestamp DESC);
```

`PRIMARY KEY (user_id)` alone cannot efficiently return the last N events in time order.

## Partition size and placement

- The partition key decides which replicas own the row set.
- Bound partition growth: very wide partitions degrade compaction, repair, and reads. Split with time buckets or additional partition components when a single key accumulates unbounded history.
- Avoid pure random UUID partition keys for bulk-load heavy time series without a deliberate distribution plan; prefer keys aligned to access patterns.

## Query restrictions

- `WHERE` should include the full partition key for targeted reads.
- `ALLOW FILTERING` forces broader scans and is a redesign signal for production paths.
- Range predicates apply to the last clustering column used in an unbroken prefix (`a=? AND b>?` can work; skipping clustering columns does not).
- `IN` on partition keys fans out to multiple partitions—use sparingly.

## Consistency levels

- Tunable consistency balances latency and how many replicas must acknowledge.
- Common defaults: `QUORUM` for single-DC strong-enough paths; `LOCAL_QUORUM` for multi-DC to keep coordination inside one DC.
- `ONE` / `LOCAL_ONE` favor availability and may return stale data—acceptable for caches, risky for critical reads.
- For stronger read-your-writes, choose write and read levels whose replica sets overlap (for example write `QUORUM` + read `QUORUM`).
- LWT uses serial consistency (`SERIAL` / `LOCAL_SERIAL`) in addition to regular CL.

## Tombstones

- `DELETE` writes a tombstone; data remains until compaction can purge it.
- Mass deletes and short TTLs under high write volume create read amplification (queries must scan tombstones).
- Prefer TTL designs that match real expiry, bounded partitions, and compaction strategies suited to the write/delete pattern.
- Inspect table tombstone metrics (historically via `nodetool` table/cf stats) before raising client timeouts.

## Batches

- Single-partition batches can apply as one mutation and provide atomicity for that partition when kept small.
- Multi-partition logged batches use a batchlog for atomicity and add coordinator overhead—reserve for true multi-partition atomic needs.
- Keep batch payloads small (on the order of tens of KB, not multi-MB blobs of unrelated writes).
- Unrelated multi-partition “performance batches” usually hurt; send independent async writes instead.

## Lightweight transactions

- `IF NOT EXISTS` / `IF col = ?` use Paxos and cost roughly several times a normal write.
- Use for rare linearizable operations (unique claim, conditional status flip), not counters or hot high-frequency updates.
- Always inspect the `[applied]` result (or driver equivalent); a failed condition is not a successful write.

## Collections and counters

- Sets/lists/maps live with the row; keep collection cell sizes bounded and avoid multi-megabyte collections without pagination strategy.
- List prepend patterns generate tombstones; prefer append-friendly or set semantics when possible.
- Counters belong in dedicated counter tables; do not mix counter and regular columns in one table.
- Counter increments are not idempotent—retries can double-count; design client retry accordingly.

## Secondary indexes and SAI

- Legacy secondary indexes (2i) on high-cardinality or frequently updated columns often cause scatter-gather or tombstone pain.
- Prefer query-driven tables. When indexes are required, read current SAI vs 2i guidance for the running major version and validate cardinality.
- `SELECT *` is brittle across schema evolution—project needed columns explicitly in application queries.

## Compaction strategy (selection)

Match strategy to workload (details and commands in `ops-and-recovery.md`):

| Strategy | Typical fit |
|---|---|
| STCS (Size-Tiered) | Write-heavy default-like profiles; watch space amplification |
| LCS (Leveled) | Read-latency sensitive, update-heavy; higher write amplification |
| TWCS (Time-Window) | Time-series with TTL; reduces tombstone burden when windows fit expiry |
| UCS (Unified) | Newer unified strategy—confirm support on the cluster version before adopting |

Wrong strategy for the workload shows up as rising read latency, disk pressure, or compaction backlog—not as a single error string.
