---
name: instacart
description: >
  Build Instacart Marketplace recipe pages, shopping-list pages, and nearby
  retailer lookups with Developer Platform REST or MCP, including auth, payload
  shaping, launch approval, and Connect boundary checks. Use when the user needs
  Instacart Developer Platform integration, shoppable recipe or list links,
  MCP create-recipe/create-shopping-list handoff, retailer discovery by postal
  code, or production launch readiness. Prefer `grocery` for generic shopping
  planning without Instacart APIs, `api` for generic REST patterns, `auth` for
  credential hygiene outside Instacart keys, `webhook` for Connect callbacks,
  and `workflow` for non-Instacart runbook design.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🛒","requires":{"env":["INSTACART_API_KEY"],"bins":["jq"]},"primaryEnv":"INSTACART_API_KEY"}'
  related-skills: '{"api":"Generic REST request and error-handling patterns beyond Instacart endpoints.","auth":"Credential and environment hygiene when the problem is not Instacart-key specific.","grocery":"Grocery planning and item taxonomy without Instacart Developer Platform calls.","webhook":"Callback verification when Connect post-checkout events are in scope.","workflow":"General operating runbooks outside Instacart surface routing."}'
---

## State location

Instacart operating state may exist in `<workspace>/instacart/`, `<workspace>/memory/instacart/`, or `~/instacart/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/instacart/`, `<workspace>/memory/instacart/`, `~/instacart/`.
3. If none exists and state must be created, default to `<workspace>/instacart/`.

Use the selected `<state_root>` for every state operation in this skill.
If more than one candidate exists, keep the highest-precedence directory only,
report the conflict, and do not merge or cross-write the copies.

```text
<state_root>/
|-- memory.md          # Activation rules, surface defaults, launch boundary
|-- url-cache.md       # Normalized payload hashes → products_link URLs
|-- retailer-notes.md  # Geo defaults and preferred retailer_key values
|-- launch-notes.md    # Production approval and messaging constraints
`-- incidents.md       # Failed requests, root causes, fixes
```

This skill writes only inside the resolved `<state_root>`. Never store raw API
keys in state files; keep secrets in the environment or secret manager.

## Setup

If `<state_root>/` does not exist or is empty, read `references/setup.md` and start naturally.

## When to load

Load this skill when the user needs Instacart-specific execution: Developer Platform recipe or shopping-list pages, nearby retailer lookup, MCP agent handoff, launch approval checks, or API troubleshooting. Skip generic meal planning that has no Instacart link or API work.

## Decision gates

1. **Surface first.** Choose Developer Platform MCP, Developer Platform REST, or Instacart Connect before assembling any request. Read
   `references/connect-boundaries.md` when fulfillment, delivery windows, order
   lifecycle, or post-checkout callbacks appear.
2. **Environment and auth.** Confirm development vs production host, key scope
   (read-only / read-write / admin), and that production keys are approved before
   write traffic. Read `references/auth-playbook.md`.
3. **Payload quality.** Keep product `name` generic; put brand and health intent in
   filters; use supported units; never send both `product_ids` and `upcs` on one
   item. Read `references/request-patterns.md` and `references/units.md`.
4. **Idempotency.** Cache `products_link_url` by normalized payload + environment in
   `<state_root>/url-cache.md` before recreating equivalent pages.
5. **Launch messaging.** Public claims about an Instacart integration require full
   production approval. Read `references/launch-and-messaging.md`.

## When to load map

| Topic | File |
|-------|------|
| First-use setup and activation | `references/setup.md` |
| Auth, hosts, key scopes, smoke tests | `references/auth-playbook.md` |
| REST endpoints and response shape | `references/endpoint-map.md` |
| Recipe / shopping-list request patterns | `references/request-patterns.md` |
| Units of measurement | `references/units.md` |
| MCP tools and when to prefer REST | `references/mcp-integration.md` |
| Developer Platform vs Connect | `references/connect-boundaries.md` |
| Core operating rules | `references/core-rules.md` |
| Common traps | `references/common-traps.md` |
| Errors, retries, weak matches | `references/troubleshooting.md` |
| Launch approval and public messaging | `references/launch-and-messaging.md` |
| Security and data boundaries | `references/security-and-privacy.md` |
| Memory schema | `references/memory-template.md` |
| Research sources | `references/sources.md` |

| Evaluation harness only | `test-prompts.json` |

## Requirements

- Required secret: `INSTACART_API_KEY` (Bearer token for Developer Platform REST/MCP)
- Required tool for documented smoke tests: `jq`
- Optional: MCP Inspector (`npx`) for MCP connectivity checks

Keep API keys out of chat. Use environment variables or the user's secret manager.

## Related Skills

Consider these skills when the request leaves Instacart Developer Platform scope:

- `api` — generic REST patterns
- `auth` — non-Instacart credential hygiene
- `grocery` — shopping planning without Instacart APIs
- `webhook` — Connect callback verification
- `workflow` — general runbook design
