# Setup — Whop

Read this when `<state_root>/` does not exist or is empty, or on first
activation. Answer the user's immediate Whop question first, then start
integrating naturally.

## Operating priorities

- Treat Whop work like live business operations with technical edges.
- Prefer the safest path that still answers the need when money, memberships,
  disputes, or webhooks are involved.
- Sandbox-first applies to technical payment and webhook tests; dashboard
  strategy work can proceed without sandbox.

## First activation flow

1. Confirm what surface is in scope now:
   - Product, pricing, waitlist, or free-trial setup
   - Checkout links, promo codes, payment operations, or payouts
   - Affiliates, ads, tracking links, or attribution
   - Analytics, support, refunds, disputes, or team workflows
   - Embedded app, REST API, webhooks, or local proxy work

2. Confirm environment and role:
   - Dashboard-only, sandbox, or production for technical work
   - Operator, seller, marketer, or developer primary mode
   - Which company / product is in scope

3. Resolve `<state_root>` using the State location rules in `SKILL.md` before
   creating any files. Never mkdir the literal string `<state_root>`.

4. If the user consents to durable notes and no state root exists yet, create
   the default resolved directory (`<workspace>/whop/` when `<workspace>` is
   available). Then create only the files needed for the current work:

```bash
# After resolving STATE_ROOT to a real absolute path:
mkdir -p "$STATE_ROOT"
chmod 700 "$STATE_ROOT"
touch "$STATE_ROOT/memory.md"
chmod 600 "$STATE_ROOT/memory.md"
# Optional when those workflows start:
# touch "$STATE_ROOT/offers.md" "$STATE_ROOT/growth.md" "$STATE_ROOT/ops.md" "$STATE_ROOT/tech.md"
# chmod 600 "$STATE_ROOT"/offers.md "$STATE_ROOT"/growth.md "$STATE_ROOT"/ops.md "$STATE_ROOT"/tech.md
```

5. If `memory.md` is empty, initialize it from `assets/data-templates.md`.

## Integration questions (lightweight)

- Should this activate automatically whenever Whop, products, plans,
  memberships, payouts, or app installs come up?
- Should it activate for both API work and embedded app work, or only one?
- Are there cases where it should stay quiet unless explicitly asked?

## Details that remove friction

If they want depth, gather and save:
- Stable IDs they reuse often (`biz_`, `app_`, `prod_`, `plan_`, …)
- Current offer, price points, trial length, and waitlist rules
- Channels in use: direct, affiliates, ads, content, communities
- Promo-code logic, attribution setup, and analytics questions
- Permission decisions, webhook events, and local proxy use when advanced
- Known blockers, missing scopes, churn reasons, or confusing edge cases

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning the user's Whop setup | Keep collecting context opportunistically |
| `complete` | Enough Whop context is stable | Use saved context by default |
| `paused` | User does not want more setup questions right now | Work with existing context and avoid digging deeper |
| `never_ask` | User explicitly does not want proactive Whop setup questions | Never prompt for more context unless they ask |

## Guardrails

- Keep secrets out of memory. Store only safe metadata such as which key
  exists, not the value.
- Preserve Whop ID prefixes exactly.
- Record whether facts came from dashboard-only work, sandbox, or production.
- Prefer short natural-language notes over config-like blobs.
- Legacy `~/Clawic/data/whop/` is migration-only; do not put it in the active
  lookup order or move it without user confirmation.
- If the user reveals a secret value directly, do not repeat it back. Move them
  toward environment variables or their normal secret manager.
