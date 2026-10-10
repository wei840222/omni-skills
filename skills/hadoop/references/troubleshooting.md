# Troubleshooting — Hadoop

## Quick flow

```text
Symptom
├── Job failed / killed
│   ├── yarn application -status <app_id>
│   ├── yarn logs -applicationId <app_id>
│   └── Branch on: memory | space | connection | permission
├── HDFS read-only / missing paths
│   ├── hdfs dfsadmin -safemode get
│   └── hdfs fsck … -list-corruptfileblocks
└── Cluster looks "up" but work stalls
    ├── yarn node -list
    └── yarn queue -status <queue>
```

## HDFS

### NameNode will not start

```bash
tail -n 500 /var/log/hadoop-hdfs/hadoop-hdfs-namenode-*.log
df -h /var/lib/hadoop-hdfs 2>/dev/null || df -h
ss -lptn | rg '8020|9870|9000'   # ports vary by config
```

Common causes: disk full on NN storage directories, port conflict, corrupted
edits/fsimage, HA fencing misconfig. Prefer distribution recovery runbooks before
reformatting.

### Safe mode stuck

```bash
hdfs dfsadmin -safemode get
hdfs fsck / -list-corruptfileblocks
hdfs dfsadmin -report
```

| Condition | Action |
|-----------|--------|
| Blocks healthy, still in safemode | `hdfs dfsadmin -safemode leave` after operator confirm |
| Missing/corrupt blocks | Repair replicas / restore from snapshot; avoid blind leave |
| Need controlled wait | `hdfs dfsadmin -safemode wait` |

`forceExit` is a last resort with explicit acknowledgment of risk.

### DataNode not registering

```bash
tail -n 200 /var/log/hadoop-hdfs/hadoop-hdfs-datanode-*.log
# Look for incompatible clusterID, NN unreachable, disk failures
```

Network check from DN toward NN RPC port. Wiping DN `current/` directories is a
**data-loss** path for that node—only on empty/replaceable disks with backups and
explicit approval.

### HDFS full / "No space left on device"

```bash
hdfs dfs -df -h
hdfs dfs -du -s -h / /tmp /user 2>/dev/null
hdfs dfs -expunge
hdfs dfs -du -h /tmp /user/*/.staging 2>/dev/null | sort -h | tail -n 30
```

Then, with confirmation: remove known scratch, lower replication on disposable
paths, or add DN capacity. Run `hdfs balancer` only after free space exists and
during an agreed window.

## YARN

### Application stuck in ACCEPTED

```bash
yarn application -status <app_id>
yarn queue -status <queue_name>
yarn node -list
```

Causes: queue at capacity, cluster memory/vcore exhaustion, AM resource ask above
max allocation, label/partition mismatch, ACLs.

Mitigations: free or kill lower-priority apps (confirm),
`yarn application -changeQueue <app_id> -queue <other>`, raise max allocation, or
add NodeManagers.

### Container killed / OOM

```bash
yarn logs -applicationId <app_id> | rg -i "memory|killed|exceeded|oom|heap"
```

Fix order: measure → raise container MB → set `-Xmx` below container → canary →
fleet default. For Spark, adjust executor/driver memory within YARN max.

### ResourceManager HA confusion

```bash
yarn rmadmin -getServiceState rm1
yarn rmadmin -getServiceState rm2
```

Manual failover flags are forceful; use distribution UI/runbooks when available
and confirm which RM should be active.

## MapReduce / batch jobs

### Map tasks failing

```bash
yarn logs -applicationId <app_id> | rg -i "Error|Exception|OutOfMemory"
```

| Pattern | Likely cause | Fix direction |
|---------|--------------|---------------|
| `OutOfMemoryError` | Heap/container too small | Memory math in `references/yarn.md` |
| Split/format errors | Bad input or codec | Validate input path/format |
| Task timeout | No progress | Raise `mapreduce.task.timeout` only after root-cause |

### Reduce slow / shuffle heavy

Check counters: shuffle bytes, spilled records, GC time, task duration variance.
Mitigate skew (combiner, custom partitioner, more reducers when appropriate),
network bottlenecks, and undersized reduce containers.

### Locality and stragglers

- Low data-local maps → rack awareness, block placement, or NN/DN topology issues
- One task 10× slower → skew or bad node; speculative execution may help cheap tasks

## Security

### Kerberos failures

```bash
klist
kinit -kt /path/to/keytab principal@REALM
```

| Symptom | Check |
|---------|-------|
| Clock skew | NTP across hosts |
| Ticket expired | Renew/`kinit` |
| Keytab unreadable | path + mode `600` + correct principal |

### HDFS permission denied

```bash
hdfs dfs -ls /path
hdfs dfs -getfacl /path
```

Fix with authorized `chmod` / `chown` / `setfacl`. Prefer the owning principal
or documented admin path over uncontrolled superuser impersonation.

## Emergency actions (explicit confirm required)

```bash
# Kill one application
yarn application -kill <app_id>

# Permanent data delete
hdfs dfs -rm -r -skipTrash /path

# Delete corrupted files reported by fsck (data loss)
hdfs fsck /path -delete

# Leave safemode
hdfs dfsadmin -safemode leave
```

State the affected queue, path, or NN role and wait for a clear yes before running.
