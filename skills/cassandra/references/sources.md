# Gate 6 sources (verified at handoff)

Primary documentation used to check data-modeling, CQL, consistency, compaction, repair, and tooling claims. Re-open the live page before restating version-specific defaults.

Handoff verification date: **2026-10-03** (local takeover of Jules session `17536671515668707378`).

## Agent Skills format

| Topic | Source | URL | Takeaway used in skill |
| --- | --- | --- | --- |
| Spec | Agent Skills specification | https://agentskills.io/specification | Frontmatter shape, progressive disclosure, package layout |
| Index | Agent Skills llms.txt | https://agentskills.io/llms.txt | Document discovery entrypoint |
| Validator | agentskills / skills-ref | https://github.com/agentskills/agentskills/tree/main/skills-ref | `uvx --from skills-ref agentskills validate skills/cassandra` |

## Apache Cassandra — modeling and CQL

| Topic | Source | URL | Takeaway used in skill |
| --- | --- | --- | --- |
| Basics | Cassandra Basics | https://cassandra.apache.org/_/cassandra-basics.html | Product orientation |
| Data modeling intro | Data Modeling Introduction | https://cassandra.apache.org/doc/latest/cassandra/developing/data-modeling/intro.html | Query-driven modeling; not RDBMS normalization |
| Application queries | Defining application queries | https://cassandra.apache.org/doc/latest/cassandra/developing/data-modeling/data-modeling_queries.html | List concrete queries before schema |
| Data modeling index | Data Modeling | https://cassandra.apache.org/doc/latest/cassandra/developing/data-modeling/index.html | Conceptual → logical → physical path |
| CQL index | Cassandra Query Language | https://cassandra.apache.org/doc/latest/cassandra/developing/cql/index.html | CQL surface area map |
| DDL | Data definition (DDL) | https://cassandra.apache.org/doc/latest/cassandra/developing/cql/ddl.html | Keyspaces, tables, primary key grammar |
| DML | Data manipulation (DML) | https://cassandra.apache.org/doc/latest/cassandra/developing/cql/dml.html | SELECT/WHERE, ALLOW FILTERING, writes/deletes |
| Architecture overview | Architecture Overview | https://cassandra.apache.org/doc/latest/cassandra/architecture/overview.html | Distributed storage context |
| Dynamo heritage | Dynamo | https://cassandra.apache.org/doc/latest/cassandra/architecture/dynamo.html | Partitioning / replication heritage |
| Guarantees / CAP | Guarantees | https://cassandra.apache.org/doc/latest/cassandra/architecture/guarantees.html | Availability vs consistency framing |

## Operations

| Topic | Source | URL | Takeaway used in skill |
| --- | --- | --- | --- |
| Compaction | Compaction | https://cassandra.apache.org/doc/latest/cassandra/managing/operating/compaction/index.html | STCS, LCS, TWCS, UCS, tombstones |
| Repair | Repair | https://cassandra.apache.org/doc/latest/cassandra/managing/operating/repair.html | Hints are best-effort; merkle repair converges replicas |
| Hints | Hints | https://cassandra.apache.org/doc/latest/cassandra/managing/operating/hints.html | Missed-write delivery limits |
| Backups | Backups | https://cassandra.apache.org/doc/latest/cassandra/managing/operating/backups.html | Snapshot semantics |
| cqlsh | cqlsh | https://cassandra.apache.org/doc/latest/cassandra/managing/tools/cqlsh.html | Shell usage |
| nodetool | nodetool | https://cassandra.apache.org/doc/latest/cassandra/managing/tools/nodetool/nodetool.html | status, repair-related, snapshot commands |
| cassandra.yaml | cassandra.yaml | https://cassandra.apache.org/doc/latest/cassandra/managing/configuration/cass_yaml_file.html | Cluster configuration surface |

## Supplementary consistency / batch references

| Topic | Source | URL | Takeaway used in skill |
| --- | --- | --- | --- |
| Tunable consistency intro | DataStax OSS consistency overview | https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/dml/dmlAboutDataConsistency.html | QUORUM/LOCAL_QUORUM mental model (verify against running major) |
| BATCH usage | DataStax CQL batching | https://docs.datastax.com/en/cql-oss/3.x/cql/cql_using/useBatch.html | Single- vs multi-partition batch atomicity and misuse |

## Operational notes retained (not live measurements)

- Official docs host multiple majors (`latest` tree may label prerelease); prefer the version matching the target cluster when advising UCS availability or exact nodetool subcommand names (`tablestats` vs `cfstats`).
- Tombstone size guidance “keep partitions practical (often cited ~100MB class)” is an operational heuristic—validate with table metrics on the live cluster rather than treating it as a hard spec limit.
- Batch “~50KB” class guidance is a coordinator-safety heuristic from common ops practice; enforce cluster-configured limits when present.
