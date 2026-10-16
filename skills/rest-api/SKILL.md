---
name: rest-api
description: >
  Design and ship framework-independent REST APIs: OpenAPI-first contracts,
  resource/URL conventions, authz at the resource boundary, additive migrations,
  contract/integration tests, and release observability. Use when defining or
  reviewing endpoints, error envelopes, pagination, versioning, idempotency,
  BOLA/auth bypass risks, or expand/migrate/contract rollouts. Prefer `fastapi`,
  `flask`, or `django` for framework wiring; `http` for protocol-only status/
  headers/caching; `auth` for OAuth/OIDC/MFA design; `api` for consuming third-
  party APIs; `backend` for broader service resilience beyond the HTTP surface.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🌐"}'
  related-skills: '{"fastapi":"Async FastAPI routers, Depends, and Pydantic wiring for a concrete Python stack.","flask":"WSGI Flask blueprints and app-factory wiring instead of generic REST contracts.","django":"Django ORM/admin/DRF stack beyond contract-first REST design.","http":"Protocol-level methods, status codes, headers, and caching independent of API product design.","auth":"Session/JWT/OAuth/MFA identity design beyond attaching schemes to OpenAPI operations.","api":"Consuming third-party REST/GraphQL APIs rather than building your own.","backend":"Service resilience, pools, caching, and observability below the public HTTP contract."}'
---

# REST API

Ship **contract-first REST APIs** that stay compatible under change: OpenAPI before
handlers, predictable resource semantics, authz at the object boundary, additive
schema evolution, and release gates that prove error paths as well as happy paths.

This skill is **stateless by default** for one-shot design and review. Optional
project memory may live under a resolved `<state_root>` only when the user wants
continuity. Never store secrets, live tokens, or customer payloads in the skill
package.

## State location

Optional notes may exist in `<workspace>/rest-api/`,
`<workspace>/memory/rest-api/`, or `~/rest-api/`. Before reading or writing state,
resolve `<state_root>`:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/rest-api/`, `<workspace>/memory/rest-api/`, `~/rest-api/`.
3. If several candidate directories exist, use only the highest-precedence one and
   report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create
   `<workspace>/rest-api/` by default.
5. If the host cannot supply `<workspace>`, read an existing `~/rest-api/` only;
   otherwise ask for a state root before creating data.
6. If older data exists only under `~/clawic/rest-api/` or
   `~/Clawic/data/rest-api/`, move it into the resolved `<state_root>/` after the
   user confirms, and say in one line that you moved it and from where.

Use the selected `<state_root>` for every state operation in this skill.
Typical layout (create children only when needed):

- `<state_root>/memory.md` — active API context (status, resources, risks)
- `<state_root>/contracts/` — OpenAPI drafts and compatibility notes
- `<state_root>/decisions/` — short ADRs
- `<state_root>/operations/` — runbooks and release check evidence

## When to use

- Designing or reviewing resource models, OpenAPI operations, and error envelopes
- Choosing methods, status codes, pagination, filtering, and idempotency keys
- Attaching authn/authz to operations and checking object-level authorization
- Planning additive migrations and expand → migrate → contract rollouts
- Defining contract/integration/e2e gates and observability for an API release

Prefer `fastapi` / `flask` / `django` once the question is framework wiring.
Prefer `http` for pure protocol mechanics. Prefer `auth` for identity protocols.
Prefer `api` when the user is **calling** someone else's API. Prefer `backend`
for pools, retries, and service internals below the public contract.

Load deeper notes on demand from the Quick reference table only; do not preload
every `references/` file.

## Quick reference

| Situation | Play |
| --- | --- |
| Start a new API or reshape resources | OpenAPI first → `references/domain.md` Contract workflow |
| URL / method / status / pagination debate | Resource conventions → `references/domain.md` Endpoint rules |
| Auth scheme vs object permission gaps | AuthN then AuthZ at resource → `references/domain.md` Security |
| Schema or response field change | Additive first; version or sunset for breaks → `references/domain.md` Compatibility |
| Release readiness | Contract + error-path tests + metrics → `references/domain.md` Release gate |
| Where to store project memory | Resolver above → `references/state.md` |
| Cite standards / live sources | `references/sources.md` |

## Workflow

1. **Name the consumer job** and the resources it owns; list identifiers and
   immutable fields before routes.
2. **Write or update the OpenAPI contract** (schemas, status map, security
   requirements, examples) before handlers.
3. **Enforce security on the server**: authenticate, then authorize at the
   resource/object boundary; validate inputs; never trust client-supplied roles.
4. **Plan change safely**: additive migrations and response fields first;
   breaking changes need versioned routes or an explicit sunset window.
5. **Prove release readiness**: contract tests, integration coverage of error
   paths, metrics/alerts with `request_id`, and a rollback path.

## Output shape

When helping with an API task, produce the smallest useful artifact first:

- OpenAPI fragment or endpoint/error matrix for the resources in scope
- Authz notes for each mutating operation (who may act on which object)
- Migration / compatibility plan when fields or routes change
- Test and observability checklist tied to the same operations

Point to `references/domain.md` for rules and traps; keep secrets as pointers
only under `<state_root>/`.
