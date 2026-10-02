# Cassandra operations and recovery

Load this file for compaction ops, repair, nodetool/cqlsh checks, rolling restarts, and failure recovery. Modeling rules stay in `cassandra-best-practices.md`.

## Tooling baselines

```bash
# Interactive CQL
cqlsh <NODE_HOST> -k <KEYSPACE>

# Cluster health
nodetool status
nodetool describecluster
nodetool compactionstats
nodetool netstats
nodetool tpstats
# Table stats name varies by version: tablestats or cfstats
nodetool tablestats <KEYSPACE>.<TABLE> || nodetool cfstats -H <KEYSPACE>.<TABLE>
```

Interpret `nodetool status` letters carefully: **UN** (Up Normal) is healthy; **DN** is down; investigate **UJ**/**UM** during join/move.

## Compaction

- Compaction merges SSTables, drops eligible tombstones, and reshapes read paths.
- Watch `nodetool compactionstats` for pending tasks and throughput before blaming application timeouts alone.
- Choose STCS / LCS / TWCS / UCS from workload shape (see best-practices table); change strategy only with a capacity plan and version-confirmed support.
- After mass deletes or TTL expiry waves, expect compaction debt—throttle other heavy jobs (repair, bulk load) if disk or CPU saturates.

## Repair

- Hints try to deliver missed writes but are **not** a guarantee. Repair compares replica data (merkle trees) and streams differences for shared token ranges.
- Run repair regularly so inconsistencies do not become permanent when tombstones expire or nodes are replaced.
- Prefer incremental repair when the cluster version and prior repair history support it; use full repair when incremental state is unknown or corrupted.
- Monitor progress (`nodetool netstats`, repair sessions, auto-repair status when enabled). Avoid overlapping full repairs that stream the whole cluster at once without scheduling.
- Read-repair helps on query paths but does not replace anti-entropy repair.

## Schema changes

- Schema agreement is eventually consistent across nodes. After DDL, wait until `nodetool describecluster` shows agreement before issuing dependent DDL or assuming all coordinators see the new schema.
- Rolling configuration changes: change one node at a time when procedure requires it; confirm UN before continuing.

## Rolling restart

1. Confirm cluster has sufficient live RF coverage for the planned CL.
2. Drain or stop one node per procedure; restart; wait for **UN** and quiet compaction/stream queues.
3. Proceed node-by-node. Do not restart a second node while the first is still joining or streaming heavily unless the runbook explicitly allows it.

## Snapshots and backups

```bash
nodetool snapshot -t <SNAPSHOT_NAME> <KEYSPACE>
# clearsnapshot only after backups are copied off-node
```

- Snapshots are hard-link based on-node markers—not offsite backups until data files are copied to durable storage.
- Pair engine snapshots with retention/immutability policy (`backups` skill) and a tested restore drill.
- Keep restore runbooks and credentials outside the skill package.

## Failure recovery playbook

| Situation | Actions |
|---|---|
| One node DN | Check process/disk/network; restart; watch bootstrap/stream; repair if downtime exceeded hint window |
| Read timeouts + high tombstones | Stop mass-delete patterns; adjust TTL/compaction; consider TWCS for time-series; repair as needed |
| Coordinator batch storms | Break multi-partition batches; reduce batch size; inspect `tpstats` |
| Schema disagreement | Pause DDL; check seeds/gossip; restore agreement before more changes |
| Suspected lost writes after outage | `nodetool repair` on affected keyspaces/ranges; verify with targeted reads at appropriate CL |
| Dead node cannot decommission cleanly | Prefer documented removenode flows; `assassinate` only as last resort (no re-replication) |

## Safety gates before destructive ops

- Explicit operator approval for `assassinate`, RF reduction, mass `TRUNCATE`/`DELETE`, and bulk `cleanup` after token changes.
- Capture `nodetool status` + keyspace RF before and after topology changes.
- Never store real JMX/`cqlsh` passwords in git or skill assets; use env/secret mounts.
