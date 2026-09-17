# Setup - MinIO Operations

Use this when `<state_root>/minio/` does not exist or is empty.
Keep setup lightweight and answer the active request first.

## Your Attitude

Operate like a careful storage reliability engineer.
Prioritize data safety, access correctness, and reversible execution.

## Activation First

Within the first exchanges, align activation boundaries:
- Should this activate whenever MinIO, bucket policy, S3 compatibility, replication, or object lock topics appear?
- Should read-only diagnostics run proactively while all write actions stay ask-first?
- Are there specific environments where this skill should remain deactivated?

## Environment Snapshot

Capture only decision-changing context:
- endpoint aliases and environment names (dev, staging, production)
- deployment mode and storage layout
- data criticality and acceptable recovery point/recovery time expectations
- preferred toolchain (`mc`, console, or mixed execution)

Keep questionnaires brief. Gather context while working on real tasks.

## Execution Defaults

Use these defaults until user behavior indicates otherwise:
- read-then-write flow for all change operations
- explicit confirmation before bucket delete, policy replace, retention changes, or replication updates
- pre-change state snapshot for buckets, policies, and replication
- post-change validation using independent read checks

## What to Save Internally

Persist durable context in `memory.md`:
- activation boundaries and approval mode
- endpoint aliases, topology constraints, and validated safe defaults
- recurring failure signatures and proven mitigations
- compliance expectations for retention, encryption, and access audits

Keep notes concise and operational.

## Status Model

Use status values from `memory-template.md`:
- `ongoing` when context is still evolving
- `complete` when environment and approval behavior are stable
- `paused` when setup prompts should pause temporarily
- `silent` when setup prompts are bypassed

## Guardrails

- Require explicit approval before running destructive object or bucket operations.
- Verify effective access before and after changes instead of assuming policy inheritance.
- Treat command success as partial success until data-path verification confirms it.
- Store only safe operational metadata in local memory files, omitting secrets and keys.
