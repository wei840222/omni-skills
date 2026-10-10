# Domain rules — Hadoop

## Operating principles

1. **Health before mutate.** Read-only `dfsadmin -report`, `dfs -df`, `node -list`,
   and application status come before kill, delete, balancer, or safemode leave.
2. **Storage before compute.** "No space left", missing blocks, and NN safemode
   present as job failures. Clear HDFS pressure before rewriting application code.
3. **Read live site config.** Apache `yarn-default.xml` / `mapred-default.xml`
   often use `-1` or empty sentinels for memory; cluster `yarn-site.xml` and
   `mapred-site.xml` are authoritative.
4. **Memory math.** Keep JVM heap strictly below the YARN container size. A
   common starting heuristic is heap ≈ 0.8 × container MB with overhead for
   non-heap native memory; validate against the distribution's guidance.
5. **Replication is policy, not magic.** Default replication is commonly 3 and
   configurable. Temp scratch can use lower replication; critical datasets need
   verified replica counts via `fsck … -replicaDetails` or `dfs -stat %r`.
6. **Scheduler shapes waits.** Capacity vs Fair (or distribution-specific)
   schedulers change why an app stays `ACCEPTED`. Inspect queue status and node
   capacity before blaming the job.
7. **Destructive ops need a blast radius.** `-skipTrash`, `fsck -delete`, forced
   safemode leave, RM `--forcemanual` failover, and bulk kills require explicit
   user confirmation.

## HDFS semantics (stable domain)

- Namespace and block map live on the NameNode; block bytes live on DataNodes.
- Files are write-once / append-oriented when append is enabled — not POSIX
  random-write files.
- Deletes usually move to trash when trash is enabled; trash still consumes
  capacity until `expunge`.
- `fsck` reports corrupt / missing blocks; `-delete` removes corrupted files and
  loses their data.
- Snapshots require `dfsadmin -allowSnapshot` on the directory first.

## YARN semantics (stable domain)

- ResourceManager schedules; NodeManagers launch containers; each app has an AM.
- Application states include `NEW`, `NEW_SAVING`, `SUBMITTED`, `ACCEPTED`,
  `RUNNING`, `FINISHED`, `FAILED`, `KILLED` (filter with `-appStates`).
- `yarn application -movetoqueue` is deprecated in current docs in favor of
  `-changeQueue` with the same purpose.
- `yarn logs -applicationId` is the post-completion log aggregation entry point.
- Exit code **137** usually means SIGKILL (often host OOM); YARN may also surface
  container killed-by-RM style failures when allocation limits are exceeded.

## Security defaults

- Prefer Kerberos (`kinit` / keytab) on secured clusters; check `klist` before
  long admin sequences.
- HDFS ACL and POSIX permission fixes run as an authorized principal; do not
  invent superuser access.
- Keep keytabs mode `600`, principals explicit, and clocks NTP-synced (skew breaks
  Kerberos).
- No secret material in `<state_root>/` — pointers only.

## Anti-patterns

| Trap | Better move |
|------|-------------|
| Delete with trash on a full cluster and stop | `df` → largest paths → `expunge` / targeted `-skipTrash` after confirm |
| Set container MB below JVM `-Xmx` | Raise container first, then set heap < container |
| Enable speculative exec on costly GPU/licensed tasks | Keep speculative on cheap stragglers only |
| Cluster-wide `fsck /` during peak | Path-scoped fsck in a maintenance window |
| Assume HDFS ≈ local POSIX FS | Design for immutability, rename commit, append policy |
| Orchestrator cron in mixed timezones | Pin TZ and document cluster-local time |
| Force safemode leave with missing blocks | Repair/replicate or accept data loss path first |
| Store keytabs inside skill memory files | Host secret store + pointer |

## Log locations (common packages)

| Component | Typical log glob |
|-----------|------------------|
| NameNode | `/var/log/hadoop-hdfs/hadoop-hdfs-namenode-*.log` |
| DataNode | `/var/log/hadoop-hdfs/hadoop-hdfs-datanode-*.log` |
| ResourceManager | `/var/log/hadoop-yarn/yarn-yarn-resourcemanager-*.log` |
| NodeManager | `/var/log/hadoop-yarn/yarn-yarn-nodemanager-*.log` |
| JobHistory | `/var/log/hadoop-mapreduce/mapred-mapred-historyserver-*.log` |
| Application | `yarn logs -applicationId <app_id>` |

Distribution packages may relocate logs; confirm on the host when paths differ.
