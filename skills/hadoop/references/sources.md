# Research sources — Hadoop (Gate 6)

Primary documentation consulted during the 2026-10-10 refactor. Prefer the
`current` docs tree live on hadoop.apache.org; pin a release (`rX.Y.Z`) when a
cluster is version-locked.

## Agent Skills format

- [Agent Skills document index](https://agentskills.io/llms.txt) — entry point for specification and creator guides
- [Agent Skills specification](https://agentskills.io/specification) — frontmatter, progressive disclosure, resource directories
- [Best practices for skill creators](https://agentskills.io/skill-creation/best-practices.md) — concise entry points and calibration
- [Optimizing skill descriptions](https://agentskills.io/skill-creation/optimizing-descriptions.md) — trigger-focused descriptions

## HDFS and common shell

- [HDFS Architecture / design](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html) — NameNode/DataNode roles, replication concept, heartbeats
- [FileSystemShell](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/FileSystemShell.html) — `dfs`/`fs` subcommands: `ls`, `df`, `du`, `rm -skipTrash`, `expunge`, `setrep`, `getmerge`, `appendToFile`, snapshots helpers
- [HDFSCommands](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HDFSCommands.html) — `fsck` options (`-list-corruptfileblocks`, `-files -blocks -locations|replicaDetails`, `-delete`), `dfsadmin` safemode/report/quota/snapshot admin, `balancer`
- [Cluster Setup](https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/ClusterSetup.html) — deployment orientation for multi-node clusters

## YARN and MapReduce defaults

- [YarnCommands](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YarnCommands.html) — `application` (`-list`, `-appStates`, `-status`, `-kill`, `-changeQueue` with deprecated `movetoqueue` note), `logs -applicationId`, `node`, `queue -status`, `rmadmin`
- [yarn-default.xml (current)](https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-common/yarn-default.xml) — scheduler allocation floors/ceilings; NM resource sentinels (`-1`)
- [mapred-default.xml (current)](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/mapred-default.xml) — map/reduce memory sentinels, speculative defaults (`true`), `mapreduce.task.timeout=600000`

## Operational takeaways applied

1. Treat replication and block health as first-class diagnostics via `fsck` + `dfsadmin`, not folklore alone.
2. Prefer `yarn application -changeQueue` in new instructions; mention `movetoqueue` only as deprecated equivalent.
3. Read live site XML for map/reduce MB numbers — current defaults frequently use `-1` / empty opts rather than fixed folklore values.
4. Keep safemode leave and `fsck -delete` behind explicit confirmation because they change availability or destroy data.
5. Trash + expunge behavior matters on full clusters; `-skipTrash` is permanent.
