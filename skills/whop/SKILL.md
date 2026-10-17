---
name: whop
description: >
  Run and grow a Whop business with offer design, checkout links, promo and
  affiliate strategy, ads/tracking, member operations, and advanced API or
  webhook automation when the dashboard is not enough. Use when shaping Whop
  products/pricing, creating checkout links, configuring affiliates or promo
  codes, debugging membership/payment ops, verifying webhooks, choosing
  bearer vs `x-whop-user-token` auth, or testing in sandbox. Prefer `ads` for
  paid-media testing discipline, `api` for generic REST debugging, `oauth` for
  delegated sign-in flows, `payments` for provider-agnostic payment design, and
  `webhook` for generic receiver security outside Whop-specific envelopes.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🟠","requires":{"env":[]},"configPaths":["<state_root>/"]}'
  related-skills: '{"ads":"Paid acquisition strategy, testing discipline, and media-buying tradeoffs beyond Whop Ads specifics.","api":"Generic REST auth, pagination, and HTTP debugging outside Whop endpoint families.","oauth":"OAuth token lifecycles and delegated access when the path is Sign in with Whop rather than iframe auth.","payments":"Provider selection, checkout design, and PCI-safe payment handling beyond Whop dashboard/API specifics.","webhook":"Generic webhook receiver security, replay handling, and idempotency outside Whop Standard Webhooks envelopes."}'
---

# Whop

Operate a **Whop business end-to-end**: sharpen the offer and checkout path first,
keep growth attribution clean, treat ops/refunds/disputes as funnel work, and only
reach for API / webhooks / local proxy when the native dashboard is too slow or
too manual.

## State location

Whop business notes, IDs, and environment metadata may exist in
`<workspace>/whop/`, `<workspace>/memory/whop/`, or `~/whop/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/whop/`, `<workspace>/memory/whop/`, `~/whop/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable state must be created, default to
   `<workspace>/whop/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. If older
notes exist only at `~/Clawic/data/whop/`, propose a copy/validation/cutover plan
and wait for user confirmation before any migration. Never write the literal
string `<state_root>` to disk. Never store API key literals, webhook secrets,
OAuth tokens, or raw payment payloads in state files.

Optional durable notes under the resolved `<state_root>/`:

```text
<state_root>/
├── memory.md       # Current business model, priorities, and blockers
├── offers.md       # Products, pricing, trials, waitlists, and checkout notes
├── growth.md       # Promo codes, affiliates, ads, tracking, and channel notes
├── ops.md          # Support, refunds, disputes, retention, and analytics habits
└── tech.md         # Non-secret key presence, webhooks, app IDs, permissions
```

## When to use

- Product, pricing, free-trial, waitlist, or checkout-link work on Whop
- Promo codes, global/custom affiliates, rev share, ads, or attribution
- Member ops: analytics, refunds, disputes, retention, team workflows
- Advanced automation: REST, webhooks, sandbox, permissions, local proxy
- Auth mode selection: Account/App API key, iframe `x-whop-user-token`, OAuth,
  or short-lived access tokens

## Quick reference

Load only the smallest file needed. Keep this `SKILL.md` as the router:

| Need | Load |
|------|------|
| First-use setup / consent | `references/setup.md` + `assets/data-templates.md` |
| Offers, pricing, trials, waitlists, checkout links | `references/offers-and-checkouts.md` |
| Promo codes, affiliates, ads, attribution | `references/growth-and-marketing.md` |
| Analytics, users, refunds, disputes, support | `references/operations-and-retention.md` |
| Auth modes, access checks, permissions | `references/auth-permissions.md` |
| Advanced API automation and stats | `references/api-workflows.md` |
| Local app development with the proxy | `references/proxy-and-local-dev.md` |
| Webhooks, sandbox, go-live checks | `references/webhooks-and-sandbox.md` |
| Verified source pins (Gate 6) | `references/sources.md` |

## Requirements

- No API key is required for dashboard-only guidance around offers, affiliates,
  analytics, or operations
- Optional env: `WHOP_API_KEY` for advanced REST, stats, webhook management,
  promo-code automation, or access-token creation
- Optional env: `WHOP_WEBHOOK_SECRET` for verifying webhook deliveries
- Optional local proxy CLI: `@whop-apps/dev-proxy` exposes `whop-proxy`
- Optional official packages: `@whop/sdk`, `@whop/embedded-components-react-js`,
  `@whop/embedded-components-vanilla-js`, `whop-sdk`, `whop_sdk`

Keep secret literals outside chat and local notes; record only whether a key
exists and which environment it belongs to.

## Core rules

### 1. Start from the business goal, not the API surface
- Decide first whether the user is trying to sell more, launch faster, improve
  conversion, retain members, or automate a repetitive workflow.
- Default to the native Whop dashboard flow when it already solves the problem.
- Reach for API, webhooks, or local app tooling only when the user needs scale,
  repeatability, or custom behavior.

### 2. Optimize the offer before optimizing acquisition
- Use products, pricing, free trials, waitlists, and checkout links first.
- Whop checkout links cover free, one-time, and recurring payment paths.
- Use waitlists when qualification matters more than raw volume.

### 3. Keep attribution clean across every channel
- Use tracking links to compare email, X, Instagram, YouTube, communities, and
  paid traffic sources.
- Add external tracking integrations before scaling spend.
- Keep affiliate, ad, and direct traffic paths separate in notes.

### 4. Use the right growth lever for the right traffic source
- Promo codes are for controlled price incentives at checkout.
- Global affiliates expose the business to Whop's affiliate network with a
  default **30%** commission (changeable per product).
- Custom affiliates and rev share are better for closers, creators, partners,
  and negotiated deals.
- Whop Ads exists as a native paid-growth surface; treat access and availability
  as live facts and verify before promising scale.

### 5. Read operations and retention as part of the funnel
- Analytics, support chats, user management, refunds, disputes, and payment
  operations change retention and reputation.
- Line up acquisition source, product, checkout path, payment outcome, and
  member lifecycle before changing strategy.
- Use built-in analytics first, then Whop stats or webhooks when the dashboard
  view is not enough.

### 6. Treat advanced automation as a separate trust boundary
- Server-to-server work uses `Authorization: Bearer ***` against
  `https://api.whop.com/api/v1` (sandbox API:
  `https://sandbox-api.whop.com/api/v1`).
- Embedded app requests inside a Whop iframe identify the current user through
  `x-whop-user-token`; verify before trusting claims.
- Embedded components use short-lived access tokens, not raw iframe headers or
  long-lived API keys in the browser.
- Webhooks follow Standard Webhooks headers; verify before side effects, and
  keep sandbox and production assets fully separate.

### 7. Keep Whop IDs and environments explicit
- Preserve prefixes such as `biz_`, `app_`, `prod_`, `plan_`, `user_`, `hook_`,
  and `file_`.
- Record whether a fact came from dashboard work, sandbox testing, or production
  automation.
- Handle 403s and weird data mismatches as scope or approval problems before
  blaming payloads.

## Workflow

1. Read `references/setup.md` and resolve `<state_root>` before writing notes.
2. Classify the ask: offer, growth, operations, or technical automation.
3. Load one matching reference file; do not ingest the whole package.
4. For money movement, webhooks, or auth, prefer sandbox evidence first.
5. Prefer-other when the ask is generic ads / REST / OAuth / payments / webhook
   security rather than Whop-specific product guidance.
6. Save only non-secret metadata the user consents to keep.

## Whop traps

| Trap | Consequence | Better move |
|------|-------------|-------------|
| Scaling traffic before the offer is clear | Clicks into a weak checkout | Tighten product, pricing, trial, and checkout first |
| Mixing promo codes, affiliates, and direct traffic | Muddy attribution | Keep one tracking path per channel |
| Using global affiliates when you need negotiated terms | Margin drift | Use custom affiliates or rev share |
| Treating analytics as a last step | Revenue drops surprise you | Review user/payment/support signals weekly |
| Testing payment or webhook automation in production | Real money / noisy data | Start in sandbox with separate keys and webhooks |
| Using a company API key where iframe user context is required | Wrong identity | Choose bearer vs `x-whop-user-token` vs access token first |
| Pointing production SDK clients at sandbox hosts (or reverse) | Silent wrong-env writes | Pin environment/`sandbox-api` vs `api.whop.com` explicitly |

## External endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| `https://api.whop.com/api/v1/*` | Bearer token, query params, JSON bodies, resource IDs | Production REST |
| `https://sandbox-api.whop.com/api/v1/*` | Sandbox bearer token and test payloads | Sandbox REST |
| `https://sandbox.whop.com/*` | Sandbox dashboard / developer actions | Sandbox UI and key creation |
| `https://docs.whop.com/*` | No runtime secrets required | Official docs |
| `https://whop.com/apps/*/install` | App and company selection in browser | Install and re-approve permissions |

No other data is sent externally by this skill.

## Security and privacy

**Leaves the machine when the user runs Whop integrations:**
- Bearer credentials for authenticated API requests
- Business metadata, membership/payment filters, promo-code changes, stats queries
- Webhook acknowledgements from the user's app back to Whop

**Stays local under `<state_root>/`:**
- Offer, growth, operations, and environment notes
- Local proxy configuration and development URLs
- Secret *presence* metadata only (never secret values)

**This skill does NOT:**
- Store secret literals in repository files or chat
- Skip token or webhook verification
- Push the user into API work when the dashboard path is better
- Assume sandbox parity for apps, messaging, or every payment method
- Make undeclared requests outside Whop

## Trust

By using this skill for live integrations, data is sent to Whop.
Only continue if you trust Whop with customer, growth, payout, membership, and
business metadata.

## Related skills

- `ads` — Paid acquisition strategy beyond Whop Ads specifics
- `api` — Generic REST debugging outside Whop endpoint families
- `oauth` — Delegated Sign in with Whop / OAuth lifecycles
- `payments` — Provider-agnostic payment design beyond Whop
- `webhook` — Generic receiver security outside Whop envelopes
