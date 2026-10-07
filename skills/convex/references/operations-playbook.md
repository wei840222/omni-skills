# Convex Operations Playbook

Use this file for release readiness and incident response.

## Pre-Deploy Gate

1. Confirm schema and function compatibility with active clients.
2. Verify auth checks on all new entry points.
3. Rehearse rollback for the exact change set.
4. Confirm observability for high-risk paths.

## Rollout Strategy

- Roll out additive schema changes before behavior switches.
- Gate risky logic behind explicit flags where possible.
- Prefer staged traffic or staged feature activation over big-bang flips.

## Incident Triage

When production breaks:
1. Capture failing function and affected records (actor, function, record IDs; no secrets).
2. Classify: data integrity, auth leak, performance, or external dependency.
3. Pause harmful writes first.
4. Select a reversible mitigation matched to the failure class (pause a faulty writer, restrict a leaking read path, or isolate a failing external dependency), then verify the affected path recovers and unaffected paths remain healthy.
5. Draft a user-impact summary and next authorization checkpoint; publish only with the service owner's authorization.

### Failure recovery matrix

| Failure | Immediate action | Recovery check |
|---|---|---|
| Mutation OCC conflict / repeated retry | Keep the mutation idempotent; reduce read-set or serialize the hot key | Same write succeeds once; no duplicate side effects. |
| Action external call timeout | Leave DB consistent via outbox/`failed` status; retry action with provider idempotency key | Status progresses to `applied` or stays safely `failed` for replay. |
| Webhook signature mismatch | Reject with non-2xx without writing business data | No row created; valid signed replay still applies once. |
| Auth/tenant miss on a live path | Deny the entry point; patch server-side checks before re-enabling | Unauthenticated and cross-tenant tests fail closed. |
| Migration leaves clients broken | Roll back to the rehearsed prior revision or re-enable dual-read | Named clients read/write successfully again. |

## Post-Incident Learning

- With persistence consent, log the detailed root cause in `<state_root>/rollout-notes.md` and add only a concise cross-topic summary to `<state_root>/memory.md` when that summary is useful; otherwise report it in the current task.
- Add a prevention rule to test or review checklists.
- Remove temporary mitigations once durable fix is live.

## Webhook and Action Safety

- For an inbound webhook use an HTTP action. Read the raw request body once, verify its provider-specific signature and timestamp with the configured secret according to the provider's current contract, then validate event type and identifiers before processing.
- Run an internal mutation to atomically check a stable event ID, update data, and record a processing status (`received`/`applied`/`failed` as appropriate). A separate preflight read races with retries; return success for an already-applied event. For external side effects, use an outbox or equivalent reconciled status and an external idempotency key if the provider supports one; a Convex transaction cannot atomically commit a network call.
- Route external service calls through actions, outside database transactions. Convex does not automatically retry failed HTTP actions: return a success response only after the event is durably applied or recognized as an already-applied duplicate; return a provider-retryable failure when processing remains incomplete, using the provider's actual delivery contract.

## Function and authorization boundaries

### Function Boundaries
Use each function type for its intended purpose:
- Query: read-only, reactive, and deterministic
- Mutation: validated transactional state changes
- Action/HTTP action: network requests or external side effects; call an internal mutation for database writes

Keep deterministic data paths separate from external calls.

### Auth & Authorization
Treat every query, mutation, action, and HTTP entrypoint as untrusted input:
- Resolve identity explicitly
- Check workspace or tenant boundaries
- Validate ownership before returning or mutating records

Validate all client-provided identifiers with explicit server checks.

### Safe Rollout Discipline
Before deploying schema or logic changes:
- Verify backward compatibility for current clients
- Prepare migration steps for renamed fields or tables
- Confirm failure mode and rollback path

Deploy a breaking data change only after recording client compatibility checks, a tested backfill plan, the exact-change rollback rehearsal, and owner authorization from the Pre-Deploy Gate.

### Debuggability
When fixing incidents:
- Capture a minimal reproduction query
- Keep structured logs around actor, function, and record ids
- Record the detailed root cause and preventive rule in `<state_root>/rollout-notes.md` after persistence consent

### Risk action → safe recovery

| Risk action | Safer next step | Check |
|---|---|---|
| Network call in a query or mutation | Move the external call to an action and persist through an internal mutation | Verify the transaction remains deterministic. |
| Missing actor identity or mismatched tenant | Deny access at the entry point | Test unauthenticated and cross-tenant requests. |
| Removing a schema field while active clients still read it | Stage additive compatibility and backfill first | Confirm both old and new clients before removal. |
| Replaying a callback after partial processing | Deduplicate by stable event key within the internal mutation and reconcile any external side effect | Replay the same event and confirm one applied state change. |
| Early provider 2xx before durable apply | Return success only after apply or recognized duplicate; otherwise provider-retryable failure | Interrupted delivery recovers on redelivery. |
| Treating a schema index as SQL UNIQUE | Enforce uniqueness with indexed lookup + write in one mutation | Duplicate insert fails in the same path. |
| Deploy or state write without named approval | Return a draft plan and request project/environment or persistence consent | No production mutate or `<state_root>` write until approved. |
