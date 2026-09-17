---
name: minio
description: Deploy MinIO clusters, manage bucket lifecycles, and configure IAM policies using mc.
metadata:
  openclaw: '{"emoji": "🗂️","requires": {"bins": ["mc","curl","openssl"],"config": ["<state_root>/minio/"]},"configPaths": ["<state_root>/minio/"]}'
  related-skills: '{"s3": "S3-compatible object storage workflows across providers when MinIO is one backend among several.","cloud-storage": "Broader storage architecture for mixed cloud and local environments beyond MinIO operations.","backups": "Backup verification and restore-first practices that complement MinIO durability controls.","infrastructure": "Infrastructure planning baselines when MinIO is part of a wider platform footprint.","docker": "Containerized deployment and service lifecycle when MinIO runs as containers."}'
---

## Setup

On first use, read `references/setup.md` to align activation boundaries, environment defaults, and write-approval rules before mutating buckets, policies, or replication.

## When to load

Load this skill when the user asks to install MinIO, configure MinIO buckets, write IAM policies for MinIO, or execute `mc` commands against an object storage cluster.

## Architecture

Memory lives in `<state_root>/minio/`. See `references/memory-template.md` for structure and status values.

```text
<state_root>/minio/
|-- memory.md              # Activation preferences and approval model
|-- environments.md        # Endpoint map, topology, and region notes
|-- buckets.md             # Bucket inventory, versioning, lifecycle, lock mode
|-- identities.md          # Users, groups, policies, and credential rotation state
`-- incidents.md           # Outages, corruption events, and validated recovery steps
```

## Quick Reference

Use the smallest file needed for the current task.

| Topic | File |
|-------|------|
| Setup and activation behavior | `references/setup.md` |
| Memory structure and status model | `references/memory-template.md` |
| Deployment and topology choices | `references/deployment-patterns.md` |
| Bucket, IAM, and mc execution flow | `references/mc-operations.md` |
| Hardening, backup, and disaster recovery | `references/hardening-dr.md` |
| Official sources and version anchors | `references/sources.md` |

## Core Rules

### 1. Classify Topology Before Any Command
- Identify single-node, distributed, or tenant-style deployment before writing a plan.
- Validate endpoint, region, and storage layout so commands target the correct environment.

### 2. Gate Write Operations with Explicit Confirmation
- Bucket deletion, lifecycle rewrite, policy replacement, and replication changes need explicit user confirmation.
- Confirm scope, expected impact, and rollback path before applying mutating actions.

### 3. Use Read-Then-Write mc Workflows
- Start with read commands (`mc admin info`, `mc ls`, `mc policy get` / listing) before write commands.
- Keep command output snapshots so post-change verification can compare expected versus observed state.

### 4. Enforce Identity and Policy Least Privilege
- Default to scoped policies by bucket and prefix rather than broad wildcard access.
- Rotate access keys and verify policy bindings after every security-sensitive change.

### 5. Protect Durability Features During Maintenance
- Check versioning, object lock, retention mode, and replication health before major updates.
- Maintain durability controls unless there is a documented user-approved exception.

### 6. Verify by API Behavior, Not Only Command Exit Codes
- Confirm changes with independent checks: listing, object test writes (if approved), and policy simulation.
- Treat partial success as failure until data path and auth path both validate.

### 7. Record Durable Context for Next Sessions
- Update `<state_root>/minio/` notes with environment constraints, safe defaults, and incident learnings.
- Keep only reusable operational context, omitting secrets or raw credentials.

## Key Success Factors

- Match commands to the real topology (single-node vs distributed) before mutating state.
- Read effective policy bindings before replacing policies; keep a rollback snapshot.
- Enable versioning and clock/time sync checks before replication.
- Dry-check lifecycle expiration on active prefixes before applying.
- Capture pre-change snapshots so outage response has a reliable rollback path.
- Validate TLS trust chains independently of bare endpoint reachability.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://<minio-endpoint> | S3 API object and metadata requests | Bucket and object operations against user-managed MinIO |
| https://<minio-endpoint>/minio/admin | Admin API requests for cluster and identity operations | Health, IAM, and operational control |
| https://min.io/docs | Documentation lookups only | Reference for command behavior and configuration details |

No other data is sent externally.

## Security & Privacy

Data that leaves your machine:
- Requests to user-managed MinIO endpoints for object, bucket, and IAM operations.
- Optional documentation fetches from official MinIO docs.

Data that stays local:
- Operational context stored in `<state_root>/minio/`.
- Command planning notes, incident logs, and approved runbooks.

This skill does NOT:
- Execute undeclared endpoints.
- Store raw credentials in memory files.
- Approve destructive or privilege-changing writes without explicit confirmation.
- Modify SKILL.md or auxiliary files automatically.

## Trust

This skill can send data to MinIO endpoints and optional documentation endpoints when executing approved operations.
Only install if you trust the configured MinIO infrastructure and its credential handling model.
