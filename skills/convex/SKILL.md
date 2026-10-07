---
name: convex
description: >
  Design, debug, and operate Convex backends. Use when the task is a Convex
  project or deployment: schema/index design from real read paths, query vs
  mutation vs action boundaries, tenant authorization at every entry point,
  webhook signature and retry-safe writes, or staged migrations. Route generic
  SQL/ORM/database work with no Convex project to `backend`. Skip pure
  mathematics uses of the word "convex" and non-Convex app scaffolding.
metadata:
  version: "1.1.0"
  related-skills: '{"backend":"Extends Convex service architecture and operational reliability decisions.","javascript":"Supports JavaScript runtime behavior in Convex functions.","typescript":"Supports type-safe Convex schema and function implementations."}'
---

## State location

Before any state read or write, choose one actual directory as `<state_root>`:

1. Use a user- or host-configured state directory when specified.
2. Otherwise select the first existing directory: `<workspace>/convex/`, `<workspace>/memory/convex/`, then `~/convex/`. An existing `~/convex/` remains readable when the host has not supplied `<workspace>`. If multiple candidates exist, select the first and disclose the untouched copies.
3. If no candidate exists, inspect legacy `~/Clawic/data/convex/` as a migration source; ask the user to select a root if it exists. With no legacy copy, obtain persistence consent before creating `<workspace>/convex/`; when the workspace is unavailable, request an explicit root before creation.
4. Disclose an existing legacy copy before using a selected candidate. Migrate only with explicit authorization; keep the selected root fixed for this invocation.

Resolve the real path before substituting for `<state_root>` in any operation. Obtain user consent and follow host policy before each state write; read access alone grants no write authority. The optional `<state_root>/memory.md` holds consented cross-topic context; create it when a durable summary is first needed using `assets/memory-template.md`. The optional `<state_root>/schema-notes.md` holds table/index rationale, `<state_root>/rollout-notes.md` holds migrations/incidents, and `<state_root>/auth-notes.md` holds permission boundaries; create each only when that topic must persist and consent is given. Preserve existing notes and seek explicit authorization before consolidation or deletion.

**If state-root resolution fails** (no candidate, conflicting copies, or missing consent for a write): keep helping with an in-response draft, name the blocker, and request the missing root or consent before any file write.

## Execution

1. **Input:** active Convex task text plus any named project path, schema, or deployment target. For a new project or missing state, read `references/setup.md`. Resolve the state root and read only relevant existing notes. Deliver an answer to the active task even if onboarding details are unavailable.
2. **Route:** load only the topic reference needed next (`references/schema-and-indexes.md`, `references/operations-playbook.md`, or `references/setup.md`). Inspect the project's schema, function entry points, authentication, deployment target, and installed Convex version. If the project is unavailable, label design advice conditional and request the exact missing artifact before proposing executable changes.
3. **Decide:** name the selected index/query path or function boundary, actor/tenant check, compatibility constraint, and smallest verification. **Authorization checkpoint:** for a persistent state write, production deployment, or publication, identify the exact target and change, then obtain approval for that action before execution. If the target or approval is missing, provide a draft and request the missing decision.
4. **Complete when:** the authorized change is implemented or the draft plus missing decision is returned; the specific query path, replay behavior, or client compatibility check is reported with observed result, remaining risk, and checks not run.

**If a required artifact is missing** (schema file, auth model, deployment target, or Convex version): stop executable changes, return a conditional plan, and list the exact artifact needed.

**If verification fails** after an authorized change: report the failing check, keep the change reversible, and propose the smallest fix or rollback step without widening scope.

## Core rules

### 1. Model access patterns before writing schema

Define tables and indexes from observed read paths: filter fields, sort order, tenant scope, and uniqueness invariants. For a bounded scan, record expected table size, observed scanned documents, and latency limits. Read `references/schema-and-indexes.md` for index design and the transactional uniqueness check; verify with the installed Convex version.

### 2. Keep function boundaries strict

Use queries for deterministic reads, mutations for validated transactional writes, and actions or HTTP actions for external network effects. Persist results through internal mutations. Read `references/operations-playbook.md` for function and webhook boundaries; verify external calls remain outside the transaction.

### 3. Enforce authorization at every entry point

At each query, mutation, action, and HTTP entry point, resolve the actor or verify the webhook provider signature, check tenant scope, and validate record ownership before reading or writing. Treat client-provided IDs as input, then verify access server-side. Test unauthenticated and cross-tenant requests.

### 4. Design indexes for stable product workflows

Map user-facing lookups, admin/backoffice reads, and background queues to the same indexes used by their query paths. Record each index's purpose and maintenance cost; inspect coverage after product expansion. Read `references/schema-and-indexes.md` for field-order examples and measured index decisions.

### 5. Make writes replay-safe

For retried callbacks use a stable provider event key. In one internal mutation, check the key, apply the data change, and record processing status; an applied replay is a no-op. Reconcile partial external effects with an outbox or equivalent status and a provider idempotency key where supported. Read `references/operations-playbook.md` for signature, retry, and acknowledgement behavior; test duplicate and interrupted delivery.

### 6. Ship staged and reversible rollouts

Before schema or logic deployment, verify active-client compatibility, stage additive changes and backfill, and rehearse rollback for the exact change. **Authorization checkpoint:** obtain approval for the named project and environment before production execution; if absent, provide the plan as a draft. Read `references/operations-playbook.md` for the pre-deploy and recovery checks.

### 7. Preserve production debuggability

For incidents, capture a minimal reproduction and structured actor, function, and record IDs without secrets; identify the root cause and a prevention test. After persistence consent, put the detailed incident in `<state_root>/rollout-notes.md` and an optional cross-topic summary in `<state_root>/memory.md`. Read `references/operations-playbook.md` for triage and mitigation verification.

## Risk-action blacklist

| Risk action | Do this instead | Verify |
|---|---|---|
| Design schema from entities only | Map observed query paths and actor/tenant scope first | Name each index's leading equality fields and product path. |
| Add indexes during an outage | Measure the failing query, then ship a reviewed index change | Record scanned docs or latency before and after. |
| Network call inside a query/mutation | Move external I/O to an action; persist via internal mutation | Confirm the transaction stays deterministic. |
| UI-only auth / trust client IDs | Resolve actor and ownership server-side at every entry point | Test unauthenticated and cross-tenant requests. |
| Remove a live field in one deploy | Additive dual-write, backfill, then remove after client proof | Confirm old and new clients against the named environment. |
| Deploy without owner approval | Draft the plan; request named project + environment approval | No production mutate until approval is explicit. |
| Webhook without stable event key | Atomic check-key / apply / record-status in one mutation | Replay the same event; one applied state change. |
| Early 2xx before durable apply | Acknowledge only after apply or recognized duplicate | Interrupted delivery still recovers via provider retry. |
| Claim a Convex unique index exists | Enforce uniqueness with indexed lookup + write in one mutation | Fail a duplicate insert in the same transaction path. |
| Write state notes without consent | Keep guidance in the reply until root and consent exist | No `<state_root>` create/update without authorization. |

## Privacy and boundaries

The skill needs no credentials itself. For third-party integrations, keep credentials in the host's secret store and refer to them by name, not value. Record only necessary, non-sensitive project decisions under the resolved `<state_root>` after authorization. Use sanitized stand-ins in examples and test artifacts; keep private records within the authorized context.

## References

| Topic | File | Load when |
|-------|------|-----------|
| Setup & Integration | `references/setup.md` | State missing, first integration, or onboarding preference |
| Schema & Indexes | `references/schema-and-indexes.md` | Table design, indexes, uniqueness, migrations |
| Operations & Deploy | `references/operations-playbook.md` | Webhooks, function boundaries, rollout, incidents |
| Memory Template | `assets/memory-template.md` | Creating `<state_root>/memory.md` after consent |
| Official source checks | `references/sources.md` | Verifying version-sensitive API claims |
| Baseline behavior disposition | `references/semantic-inventory.md` | Audit of pre-refactor behavior retention |
| Prompt and rubric evidence (audit-only) | `references/evaluation.md` | Gate 8 evidence review only; not normal execution |
