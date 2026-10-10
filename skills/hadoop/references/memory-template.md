# Memory templates — Hadoop

Create files only after `<state_root>` is resolved and the user wants durable notes.

## `<state_root>/memory.md`

```markdown
# Hadoop Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD
integration: pending | done | declined

## Environment
<!-- Distribution, version floor, auth mode (simple/kerberos) -->

## Clusters
| Name | Purpose | Notes File |
|------|---------|------------|
| prod | Production ETL | clusters/prod.md |

## Common Workflows
<!-- Frequent jobs, queues, orchestrators -->

## Preferences
<!-- How they like checks ordered; change windows -->

## Notes
<!-- Non-secret facts learned in conversation -->

---
*Updated: YYYY-MM-DD*
```

### Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning their setup | Gather context opportunistically |
| `complete` | Environment well known | Work from notes first |
| `paused` | User deferred deeper setup | Use currently available information |
| `halt_asking` | User asked to stop probing | Proceed without new context requests |

## `<state_root>/clusters/{name}.md`

```markdown
# Cluster: {Name}

## Overview
- Distribution:
- Version:
- Nodes: X NameNode roles, Y DataNodes / NodeManagers
- Purpose:

## Key Settings
| Parameter | Value | Notes |
|-----------|-------|-------|
| dfs.replication | 3 | site default unless per-path override |
| yarn.nodemanager.resource.memory-mb | (read live) | |

## Known Issues
<!-- Recurring problems and fixes that worked -->

## Access
<!-- Principal names, edge host, UI URLs — no secrets -->

---
*Updated: YYYY-MM-DD*
```

## Principles

- Prefer natural-language descriptions of settings when sharing with non-admins
- Learn from conversation; avoid interrogation loops
- Most environments stay `ongoing` because clusters evolve
- Update `last` on each durable write
- Credentials: store `env:`, `keytab:path`, or secret-manager pointers only
