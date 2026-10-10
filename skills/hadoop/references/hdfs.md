# HDFS operations — Hadoop

Commands below use the `hdfs` / `hadoop fs` CLIs documented in Apache Hadoop
FileSystemShell and HDFSCommands. Equivalent `hadoop fs …` forms are valid.

## Architecture snapshot

```text
NameNode
├── Namespace (paths → inode metadata)
├── Block map (file → block IDs + locations)
└── Replication decisions

DataNode
├── Stores block bytes
├── Heartbeats + block reports to NameNode
└── Serves read/write/replication pipelines
```

## File and directory operations

```bash
# List / read
hdfs dfs -ls /path
hdfs dfs -ls -R /path
hdfs dfs -cat /path/file
hdfs dfs -head /path/file
hdfs dfs -tail /path/file
hdfs dfs -get /hdfs/path local/path
hdfs dfs -getmerge /hdfs/dir local/file.txt

# Write / namespace
hdfs dfs -mkdir -p /path/to/dir
hdfs dfs -put local/file.txt /hdfs/path
hdfs dfs -put -f local/file.txt /hdfs/path
hdfs dfs -mv /src /dst
hdfs dfs -cp /src /dst
hdfs dfs -appendToFile local.txt /hdfs/existing.txt   # when append enabled

# Delete
hdfs dfs -rm /path/file
hdfs dfs -rm -r /path/dir
hdfs dfs -rm -skipTrash /path/file          # permanent; confirm first
hdfs dfs -rm -r -skipTrash /path/dir
hdfs dfs -expunge                           # empty trash
```

## Capacity, quotas, replication

```bash
hdfs dfs -df -h
hdfs dfs -du -h /path
hdfs dfs -du -s -h /path
hdfs dfs -count /path
hdfs dfs -count -q /path                    # includes quota columns

# Admin quotas (bytes / namespace object counts)
hdfs dfsadmin -setSpaceQuota 107374182400 /path    # bytes; confirm unit with ops policy
hdfs dfsadmin -setQuota 10000 /path
hdfs dfsadmin -clrSpaceQuota /path
hdfs dfsadmin -clrQuota /path

# Replication (EC files ignored by setrep)
hdfs dfs -setrep 2 /path/file
hdfs dfs -setrep -R 2 /path/dir
hdfs dfs -setrep -w 3 /path                 # wait for completion (can be slow)
hdfs dfs -stat %r /path/file
```

Replication factor is a per-file property stored in metadata; site default is
commonly 3 via `dfs.replication` but must be read from live config.

## fsck and block health

```bash
hdfs fsck /path
hdfs fsck /path -files -blocks
hdfs fsck /path -files -blocks -locations
hdfs fsck /path -files -blocks -replicaDetails
hdfs fsck / -list-corruptfileblocks
hdfs fsck /path -delete                     # deletes corrupted files; data loss
```

Prefer path-scoped fsck. Full-filesystem checks on large busy clusters belong in
maintenance windows (`-showprogress` optional).

## Snapshots

```bash
hdfs dfsadmin -allowSnapshot /path
hdfs dfsadmin -disallowSnapshot /path
hdfs dfs -createSnapshot /path snapshot_name
hdfs dfs -ls /path/.snapshot
hdfs dfs -renameSnapshot /path old_name new_name
hdfs dfs -deleteSnapshot /path snapshot_name
hdfs dfs -cp /path/.snapshot/snapshot_name/file /path/restored_file
```

## Permissions and ACLs

```bash
hdfs dfs -chown user:group /path
hdfs dfs -chown -R user:group /path
hdfs dfs -chmod 755 /path
hdfs dfs -getfacl /path
hdfs dfs -setfacl -m user:alice:rwx /path
hdfs dfs -setfacl -m group:analysts:r-x /path
```

## Admin: safemode, report, refresh, balancer

```bash
hdfs dfsadmin -safemode get
hdfs dfsadmin -safemode enter
hdfs dfsadmin -safemode leave                # only when block health is acceptable
hdfs dfsadmin -safemode wait
hdfs dfsadmin -safemode forceExit           # last resort; understand impact first

hdfs dfsadmin -report
hdfs dfsadmin -report -live -dead
hdfs dfsadmin -printTopology
hdfs dfsadmin -refreshNodes

# Balancer (HDFSCommands)
hdfs balancer
hdfs balancer -threshold 10
```

Bandwidth caps are cluster-specific (`dfs.datanode.balance.bandwidthPerSec` and
balancer tool options). Raise carefully on shared networks.

## Small files and locality

- Many tiny files stress NameNode memory — consider HAR, sequence/container
  formats, or Combine-style inputs for batch jobs.
- Default block size is distribution-specific (often 128MB+); match layout to
  typical object size rather than copying folklore.
- Favor data-local reads; rack-awareness misconfig shows up as low data-local map
  percentages and extra network shuffle.
