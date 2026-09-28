---
name: convex
description: Design, debug, and operate Convex backends. Use for Convex schema/index design, query/mutation/action boundaries, tenant authorization, webhook retries, and safe migrations; route generic database work without a Convex project to the backend skill.
metadata:
  related-skills: '{"backend":"Extends Convex service architecture and operational reliability decisions.","javascript":"Supports JavaScript runtime behavior in Convex functions.","typescript":"Supports type-safe Convex schema and function implementations."}'
---

## State location

Before any state read or write, choose one actual directory as `<state_root>`:

1. Use a user- or host-configured state directory when specified.
2. Otherwise select the first existing directory: `<workspace>/convex/`, `<workspace>/memory/convex/`, then `~/convex/`. An existing `~/convex/` remains readable when the host has not supplied `<workspace>`. If multiple candidates exist, select the first and disclose the untouched copies.
3. If no candidate exists, inspect legacy `~/Clawic/data/convex/` as a migration source; ask the user to select a root if it exists. With no legacy copy, obtain persistence consent before creating `<workspace>/convex/`; when the workspace is unavailable, request an explicit root before creation.
4. Disclose an existing legacy copy before using a selected candidate. Migrate only with explicit authorization; keep the selected root fixed for this invocation.

Resolve the real path before replacing `<state_root>` in any operation. It is a placeholder; substitute only the resolved directory. Obtain user consent and follow host policy before each state write; read access alone grants no write authority. The optional `<state_root>/memory.md` holds consented cross-topic context; create it when a durable summary is first needed using `assets/memory-template.md`. The optional `<state_root>/schema-notes.md` holds table/index rationale, `<state_root>/rollout-notes.md` holds migrations/incidents, and `<state_root>/auth-notes.md` holds permission boundaries; create each only when that topic must persist and consent is given. Preserve existing notes and seek explicit authorization before consolidation or deletion.

## Execution

1. For a new project or missing state, read `references/setup.md`. Resolve the state root and read only relevant existing notes. Deliver an answer to the active task even if onboarding details are unavailable.
2. Read the topic reference below; inspect the project's schema, function entry points, authentication, deployment target, and installed Convex version. If the project is unavailable, label design advice conditional and request the exact missing artifact before proposing executable changes.
3. Name the selected index/query path or function boundary, actor/tenant check, compatibility constraint, and smallest verification. **Authorization checkpoint:** for a persistent state write, production deployment, or publication, identify the exact target and change, then obtain approval for that action before execution. If the target or approval is missing, provide a draft and request the missing decision.
4. Implement only the authorized change. Verify the specific query path, replay behavior, or client compatibility affected; report the observed result, remaining risk, and checks not run.

## Decision boundaries

- For schema and index changes, map real access paths and tenant scope first; read `references/schema-and-indexes.md` and validate index order and query behavior against the installed Convex version.
- For queries and mutations, validate input and actor access on the server; use an action or HTTP action for external network calls, then an internal mutation for persistent writes. For retried webhooks, use a stable event key, transactional replay-safe update, and processing-status record; distinguish partially completed external side effects from an already-applied database mutation. Read `references/operations-playbook.md` for webhooks and incident recovery.
- For deployments, read `references/operations-playbook.md` before changing schema or functions. Compare current clients and schema, stage additive changes and backfill, then rehearse rollback for the exact change. Request deployment authorization with the named project and environment before production execution. For dangerous shortcuts and a safer recovery, use its "Risk action → safe recovery" table.

## Privacy and boundaries

The skill needs no credentials itself. For third-party integrations, keep credentials in the host's secret store and refer to them by name, not value. Record only necessary, non-sensitive project decisions under the resolved `<state_root>` after authorization. Use sanitized placeholders in examples and test artifacts; keep private records within the authorized context.

## References

| Topic | File |
|-------|------|
| Setup & Integration | `references/setup.md` |
| Schema & Indexes | `references/schema-and-indexes.md` |
| Operations & Deploy | `references/operations-playbook.md` |
| Memory Template | `assets/memory-template.md` |
| Official source checks | `references/sources.md` |
| Baseline behavior disposition | `references/semantic-inventory.md` |
