# Multiplayer and Live Operations

Use this file only when single-player loop quality is already validated.

## Multiplayer escalation path

1. Local multiplayer or async ghost data first
2. Lightweight online sync for non-critical interactions
3. Authoritative server for competitive or economy-sensitive games

Gather product evidence before adopting full authoritative architecture.

## Netcode decision heuristics

- Turn-based or low-frequency interactions: lockstep or command sync
- Action gameplay with precision demands: client prediction plus reconciliation
- Social/co-op relaxed gameplay: state replication with smoothing

## Session reliability basics

- Explicit reconnect states
- Clear host/server authority rules
- Deterministic timeout and retry policy
- Duplicate message handling via idempotent message IDs

## Live ops baseline

Before live events or seasonal content:

- telemetry for retention and drop-off points
- remote-config or data-driven tunables
- rollback plan for faulty content updates
- support playbook for incident communication

## Scope warning

Multiplayer and live ops multiply cost across code, QA, hosting, and support.
Enable them only when business goals require it.
