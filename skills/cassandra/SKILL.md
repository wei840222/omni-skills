---
name: cassandra
description: >
  Design Apache Cassandra tables and CQL for query patterns, partition keys,
  clustering order, consistency levels, tombstones, batches, compaction, and
  nodetool/cqlsh ops. Use when modeling Cassandra keyspaces, fixing ALLOW
  FILTERING or wide-partition pain, choosing QUORUM vs LOCAL_QUORUM, diagnosing
  high tombstones, or running repair. Prefer `db` for generic relational traps,
  `sql` for dialect-agnostic SQL craft, `dynamodb` for AWS single-table design,
  and `observability` for metrics around the data plane.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"👁️","requires":{"anyBins":["cqlsh","nodetool"]}}'
  related-skills: '{"backups":"Retention, immutability, and restore drills beyond Cassandra snapshots and incremental backups.","db":"Cross-engine relational ops traps when the workload is not Cassandra-specific.","dynamodb":"AWS DynamoDB single-table design and capacity modes instead of Cassandra CQL.","mongodb":"Document-store modeling outside Cassandra wide-column tables.","observability":"Metrics, logs, and traces for latency, tombstones, and repair progress.","sql":"Dialect-agnostic SQL and EXPLAIN craft when the engine is relational, not CQL."}'
---

# Cassandra

Query-first **Apache Cassandra** skill for table design, CQL correctness, tunable consistency, and cluster ops with `cqlsh` / `nodetool`. Keep credentials, JMX passwords, and production host lists out of the package; inject connection targets at runtime.

## When to load

Load for Cassandra-specific work:

- Query-driven data modeling, partition/clustering keys, denormalized tables per access path
- CQL SELECT/INSERT/UPDATE/DELETE constraints, `ALLOW FILTERING`, secondary indexes / SAI trade-offs
- Consistency levels, lightweight transactions (LWT), batches, TTL and tombstone pressure
- Compaction strategy choice, repair, hints, rolling restart, `nodetool` health checks

Prefer other skills when the ask is mainly:

- Generic multi-engine DB traps → `db`
- Relational SQL craft → `sql`
- DynamoDB single-table design → `dynamodb`
- Document MongoDB modeling → `mongodb`
- Backup policy design beyond engine snapshots → `backups`
- RED/USE metrics and tracing → `observability`

## State location

Optional operator notes (non-secret cluster inventory, keyspace map, repair windows) may live under `<workspace>/cassandra/`, `<workspace>/memory/cassandra/`, or `~/cassandra/`. Resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when available.
2. Otherwise the first existing directory in that order.
3. If multiple exist, use only the highest-precedence path and report duplicates.
4. Create `<workspace>/cassandra/` only with user consent when no candidate exists and notes must persist.

Keep live `data/`, commitlog, hints, snapshots, and credentials **out of the skill package and out of git**. Examples use placeholders such as `<KEYSPACE>`, `<TABLE>`, and `<NODE_HOST>`.

## Routing

Keep `SKILL.md` as the progressive-disclosure router; load supporting references only when needed:

- **Data modeling, keys, CQL traps, consistency, batches, LWT, collections** → `references/cassandra-best-practices.md`
- **Compaction, repair, nodetool/cqlsh ops, failure recovery** → `references/ops-and-recovery.md`
- **Gate 6 primary sources** → `references/sources.md`
- **Darwin score evidence** → `references/darwin-evaluation.md`

## Core rules

Execute in order; load references only when a rule points deeper.

1. **Model from queries, not entities.** List the concrete SELECT shapes first; create one table (or deliberate denormalized copy) per access path. Cassandra has no runtime joins for application queries.
2. **Partition key owns placement.** Every equality filter that must hit one node set belongs in the partition key. Keep partitions bounded (target well under ~100MB / tens of millions of cells); add a time bucket or other splitter when a key grows without bound.
3. **Clustering columns own on-disk order.** Range and `ORDER BY` must follow the declared clustering prefix. Fetching “latest N rows for X” needs `(partition, clustering…)` plus `CLUSTERING ORDER`, not partition-only PK.
4. **Full partition key in `WHERE`.** Partial partition predicates need a redesign or a justified secondary/SAI index path. Treat `ALLOW FILTERING` as a redesign signal, not a production default.
5. **Pick consistency for the failure domain.** Prefer `LOCAL_QUORUM` inside a multi-DC deployment to avoid cross-DC round trips; use `QUORUM` when the client must span DCs. Strong read-your-writes needs overlapping write+read levels (for example both `QUORUM`).
6. **Treat deletes and short TTLs as tombstone generators.** Mass `DELETE`, overwrites, and aggressive TTL create read amplification until compaction purges. Inspect tombstone metrics before raising timeouts.
7. **Batch only same-partition atomic groups.** Logged multi-partition batches add coordinator coordination; oversized or unrelated batches hurt latency. Prefer async single-partition writes when atomicity across partitions is not required.
8. **LWT is Paxos, not a general transaction system.** Use `IF NOT EXISTS` / conditional updates for rare linearizable slots; expect higher latency and contention under hot keys.
9. **Repair is how missed writes converge.** Hints are best-effort. Schedule repair so replica sets stay consistent before tombstones expire or nodes are replaced.
10. **Verify with tools, not memory.** Use `cqlsh` for schema/query checks and `nodetool status|cfstats|tablestats|compactionstats|netstats|describecluster` for health; re-check after version upgrades.

## Quick triage

| Symptom | First move |
|---|---|
| Query needs `ALLOW FILTERING` | Redesign table/index for the access path → `references/cassandra-best-practices.md` |
| Timeout on reads after heavy deletes | Tombstones + compaction strategy → best-practices + ops |
| “Latest N events for user” slow/wrong order | Add clustering timestamp + `CLUSTERING ORDER` |
| Multi-DC latency spikes on every read | Prefer `LOCAL_*` consistency when safe |
| Batch timeouts / coordinator CPU | Split to same-partition batches or single writes |
| Node missing data after outage | `nodetool repair` / auto-repair status → `references/ops-and-recovery.md` |
| Schema disagreement | Wait for `nodetool describecluster` agreement before more DDL |
| Hot partition / huge partition | Time-bucket or split partition key |

## Safety

- Never commit cluster passwords, TLS keys, JMX credentials, or production dumps into the skill package.
- Confirm operator intent before `nodetool assassinate`, decommission, bulk deletes, or RF changes.
- Treat snapshot/backup success as restore-tested only; document the restore path outside git secrets.
