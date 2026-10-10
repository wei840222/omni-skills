---
name: hadoop
description: >
  Operate Apache Hadoop clusters with HDFS storage checks, YARN application
  lifecycle, MapReduce memory tuning, safe-mode recovery, and distributed-job
  diagnostics. Use when the user mentions HDFS, YARN, MapReduce, NameNode,
  DataNode, ResourceManager, NodeManager, Hive-on-YARN, Spark-on-YARN, dfsadmin,
  fsck, balancer, container OOM, ACCEPTED-not-RUNNING jobs, safe mode, under-
  replicated or corrupt blocks, queue capacity, or Kerberos access to a Hadoop
  cluster. Not for pure Kubernetes scheduling (`k8s`), single-host Docker only
  (`docker`), or generic Linux host administration outside the Hadoop stack
  (`linux` / `bash`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🐘","requires":{"bins":["hdfs","yarn","hadoop"]},"os":["linux","darwin"]}'
  related-skills: '{"bash":"Shell quoting, pipelines, and script hardening around hdfs/yarn one-liners.","docker":"Containerized edge clients or single-host daemons that still talk to HDFS/YARN.","linux":"Host disks, NTP, firewall, systemd, and OS limits underneath NameNode/DataNode/NodeManager."}'
---

# Hadoop

Diagnose and operate **HDFS + YARN** with concrete commands, recovery branches,
and portable cluster notes. Prefer the smallest check that names the failing
subsystem: storage, scheduler/queue, container memory, auth, or node health.

## State location

Hadoop notes may exist in `<workspace>/hadoop/`,
`<workspace>/memory/hadoop/`, or `~/hadoop/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/hadoop/`, `<workspace>/memory/hadoop/`, `~/hadoop/`.
3. If none exists and durable state must be created, default to
   `<workspace>/hadoop/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, leave the workspace root unset and
   avoid treating the shell cwd as a substitute. An existing `~/hadoop/` may be
   read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

**Data.** Read `<state_root>/memory.md` and any cluster file it indexes under
`<state_root>/clusters/{name}.md` when they exist. Load
`references/memory-template.md` for formats. Create optional cluster files only
when the user needs durable per-cluster context.

**Credentials stay out of state.** Record pointers only
(`env:HADOOP_USER`, `keytab:~/.keytabs/hive.service.keytab`,
`cmd:kinit -kt …`). Keep passwords, keytab bytes, and tokens outside
`<state_root>/` — store only non-secret pointers.

**Legacy paths.** Historical notes under `~/Clawic/data/hadoop/` or other
non-candidate roots are **not** in active lookup order and must **not** be
moved, merged, or deleted during ordinary sessions. Migration is a separate
user decision with copy, validation, cutover, and rollback.

## When to load

- HDFS capacity, quotas, trash, replication, fsck, snapshots, or balancer work
- YARN list/status/kill/changeQueue, queue pressure, node health, RM HA
- MapReduce/Spark-on-YARN container memory, OOM exit codes, speculative tasks
- Safe mode, missing blocks, Kerberos/`Permission denied`, stuck ACCEPTED apps
- First-use setup of durable cluster notes → `references/setup.md`

## Routing

Load supporting resources only on demand:

| Need | File |
| --- | --- |
| First-use integration questions | `references/setup.md` |
| Memory and cluster note templates | `references/memory-template.md` |
| Core rules, traps, security defaults | `references/domain.md` |
| HDFS shell, fsck, dfsadmin, snapshots | `references/hdfs.md` |
| YARN apps, queues, nodes, memory knobs | `references/yarn.md` |
| Symptom → fix playbooks | `references/troubleshooting.md` |
| Gate 6 research URLs | `references/sources.md` |

## Quick diagnosis

```text
Job or cluster symptom?
├── Storage / "No space left" / missing blocks → hdfs dfs -df -h, fsck, expunge
├── App ACCEPTED only → yarn application -status, yarn queue -status, yarn node -list
├── Container killed / exit 137 / -100 → memory math in references/yarn.md
├── Safe mode / read-only HDFS → hdfs dfsadmin -safemode get + fsck corrupt list
└── Auth / Permission denied → klist, hdfs dfs -getfacl, then fix ACLs as admin
```

## Core workflow

1. **Resolve context.** Read `<state_root>/memory.md` when present; confirm
   distribution (Apache / CDP / EMR / Dataproc), cluster name, and auth mode.
2. **Health before mutate.** Run read-only cluster checks before delete, kill,
   safemode leave, balancer, or replication changes:
   ```bash
   hdfs dfsadmin -report
   hdfs dfs -df -h
   yarn node -list
   yarn application -list
   ```
3. **Name the subsystem.** Storage issues cascade into compute failures. Check
   HDFS capacity and block health before rewriting job code.
4. **Apply the smallest fix.** Prefer expunge/trash cleanup, queue move, or
   container memory correction over cluster-wide restarts.
5. **Confirm destructive intent.** Permanent delete (`-skipTrash`),
   `fsck -delete`, forced safemode leave, RM failover, and mass kill require an
   explicit user confirmation and a stated blast radius.
6. **Write durable notes** only after consent: update
   `<state_root>/memory.md` / `<state_root>/clusters/{name}.md` with non-secret
   facts (versions, pain points, successful knobs).

## Essential commands

```bash
# HDFS capacity and namespace
hdfs dfs -df -h
hdfs dfs -du -h /path
hdfs dfs -count -q /path
hdfs fsck /path -files -blocks
hdfs fsck / -list-corruptfileblocks
hdfs dfsadmin -safemode get
hdfs dfsadmin -report

# YARN applications and nodes
yarn application -list
yarn application -list -appStates ACCEPTED,RUNNING,FAILED
yarn application -status <app_id>
yarn application -kill <app_id>
yarn application -changeQueue <app_id> -queue <queue>
yarn logs -applicationId <app_id>
yarn node -list
yarn queue -status <queue_name>
yarn rmadmin -getServiceState rm1
```

Default HDFS replication is commonly **3** and is configurable per file; treat
site `dfs.replication` as source of truth rather than hard-coding. YARN and
MapReduce memory properties often default to sentinel/`-1` (resource calculator
derived) in current Apache defaults—read live `yarn-site.xml` /
`mapred-site.xml` before prescribing numbers.

## Security boundaries

- Cluster notes and preferences stay under `<state_root>/`.
- `hdfs` / `yarn` / `hadoop` commands use the user's configured cluster endpoints
  and may read host paths such as `/etc/hadoop/conf` and `/var/log/hadoop-*`.
- Destructive or irreversible operations proceed only after explicit confirmation.
- Kerberos keytabs and tokens stay outside skill state; use `kinit` / host secret
  stores and record pointers only.

## Common traps

- Trash still consumes HDFS space after `rm` without `-skipTrash` + `expunge`
- JVM heap ≥ container size → instant kill with confusing YARN messages
- Speculative execution duplicates expensive tasks on already-slow jobs
- Full-cluster `fsck` on a busy NN hurts latency — scope path + maintenance window
- HDFS is not POSIX: no in-place random write; append only when enabled
- Scheduler timezone / DST mistakes for Oozie or external orchestrators

Details, recovery tables, and verified sources live in `references/`.
