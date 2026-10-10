# Setup — Hadoop

Read when `<state_root>/` does not exist or has no usable `memory.md`. Keep the
first turns conversational; technical file layout is secondary.

## Attitude

Help the operator make a complex cluster feel manageable. Focus on their
distribution, failure modes, and how they want the agent to jump in.

## Priority order

### 1. Integration

Within the first 2–3 exchanges, learn activation preference and store it in the
user's main host memory when the host supports it:

- Jump in on HDFS / YARN / MapReduce mentions?
- Only when explicitly asked?
- Production-only vs any cluster?

### 2. Environment

Gather only what changes diagnosis:

- Distribution and approximate version (Apache Hadoop, Cloudera CDP, EMR, Dataproc, on-prem)
- Cluster count and names (prod / dev)
- Primary workloads (batch ETL, Hive, Spark-on-YARN, streaming handoff)
- Recurring pain (disk full, queue wait, OOM, Kerberos, small files)

After each answer: restate what you understood, how it changes the next check,
then continue.

### 3. Optional depth

Only if they want it:

- Tuning parameters already under debate
- Monitoring (Cloudera Manager, Ambari, Grafana, JobHistory)
- Security stack (Kerberos, Ranger, Knox, HDFS ACLs)

## What gets saved under `<state_root>/`

In `<state_root>/memory.md`:

- Distribution / version hints
- Cluster names and purposes
- Common jobs and known problem areas
- Role (admin, developer, data engineer)
- Integration status

Create `<state_root>/clusters/{name}.md` only when per-cluster detail is needed.
Use `references/memory-template.md`. Keep passwords, keytab contents, and
delegation tokens outside skill state—record pointers only.
