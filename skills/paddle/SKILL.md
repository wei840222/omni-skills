---
name: paddle
description: >
  Integrate Paddle Billing as merchant of record: sandbox-first API keys,
  Paddle.js checkout, webhook signature verification, subscription status and
  access provisioning, proration, Retain dunning, and tax-inclusive pricing.
  Use when building or debugging Paddle subscriptions, checkouts, webhooks,
  past_due access, cancel/pause, or sandbox→live go-live. Not for Stripe-first
  PSP wiring (`stripe-api-integration`), provider selection before committing
  to Paddle (`payments`), generic billing architecture without Paddle IDs
  (`billing`), or personal consumer subscription trackers (`subscriptions`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏓"}'
  related-skills: '{"billing":"Provider-agnostic subscription architecture once Paddle-specific IDs and events are settled.","payments":"PSP selection and one-off checkout when Paddle is not yet chosen.","subscriptions":"Personal consumer subscription inventory, not merchant Paddle product billing.","stripe-api-integration":"Direct Stripe API patterns when the merchant is not using Paddle MoR."}'
---

# Paddle

Paddle Billing is a **merchant of record**: Paddle collects payment, calculates
and remits sales tax/VAT, and exposes products, prices, customers, transactions,
and subscriptions over a versioned REST API plus Paddle.js checkout.

## State location

Paddle integration notes may exist in `<workspace>/paddle/`,
`<workspace>/memory/paddle/`, or `~/paddle/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/paddle/`, `<workspace>/memory/paddle/`, `~/paddle/`.
3. If more than one candidate exists, use only the highest-precedence directory,
   report the conflict, and leave other copies unchanged.
4. If none exists and durable state must be created, default to
   `<workspace>/paddle/` only with user consent. If `<workspace>` is unavailable,
   an existing `~/paddle/` may be read; otherwise ask before creating data.
5. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.
Never treat the literal string `<state_root>` as a filesystem path.

```text
<state_root>/
├── memory.md      # environment, product shape, price ID pointers (no secrets)
└── webhooks.md    # destination URLs, subscribed events, handler notes
```

**No credential is ever written under `<state_root>/`.** Store pointers only:
`env:PADDLE_API_KEY`, `env:PADDLE_WEBHOOK_SECRET`, `env:PADDLE_CLIENT_TOKEN`,
`1password:Work/Paddle/sandbox`. Publishable client-side tokens and entity IDs
(`pri_…`, `pro_…`, `ctm_…`) are not secrets; API keys, endpoint secret keys, and
raw PANs are.

**Legacy paths.** Notes under `~/Clawic/data/paddle/` or similar vendor roots are
not in active lookup order. Migrate only when the user asks; say in one line what
moved and from where.

## When to load

Load when the user needs:

- Paddle sandbox or live API setup, key rotation, or `Paddle-Version` pinning
- Paddle.js overlay/inline checkout, client-side tokens, or `customData` mapping
- Webhook destinations, `Paddle-Signature` verification, retries, or IP allowlists
- Subscription access from `trialing` / `active` / `past_due` / `paused` / `canceled`
- Cancel, pause, resume, proration, or Retain dunning behavior
- Correcting wrong price IDs, mode mixups, or tax-inclusive MoR assumptions

Hand off when a sibling owns the job:

| Job | Skill |
| --- | --- |
| Choose Stripe vs Paddle vs other PSP | `payments` |
| Provider-agnostic billing architecture | `billing` |
| Direct Stripe API / Connect | `stripe-api-integration` |
| Personal consumer subscription list | `subscriptions` |

## Progressive disclosure

Load a reference only when that topic is in scope:

| Topic | Load |
| --- | --- |
| First-use questions and sandbox path | `references/setup.md` |
| Auth, base URLs, IDs, rate limits, checkout, common calls | `references/api.md` |
| Signature verify, events, retries, idempotency | `references/webhooks.md` |
| Status→access, proration, Retain, traps | `references/domain.md` |
| What leaves the machine; secret handling | `references/security.md` |
| Optional memory file shape | `references/memory-template.md` |
| Canonical URLs before citing a limit | `references/sources.md` |

## Core rules

1. **Sandbox first.** Server base URLs are `https://sandbox-api.paddle.com` and
   `https://api.paddle.com`. Price IDs, API keys, client tokens, and webhook
   secrets differ per environment — never reuse sandbox IDs against live keys.
2. **Bearer API keys stay server-side.** `Authorization: Bearer <api_key>` plus
   optional `Paddle-Version: 1`. Client-side tokens (`ctkn_…`) open checkouts
   only; they must not call privileged API routes.
3. **Webhooks are the source of truth for access.** Verify `Paddle-Signature` on
   the **raw body** before parse. Prefer official SDK helpers. Respond `200`
   within five seconds, then process asynchronously. Deduplicate on `event_id`;
   order with `occurred_at`.
4. **Gate access from `subscription.status` (and scheduled changes).**
   | Status | Access |
   | --- | --- |
   | `trialing` | Full (same as active) |
   | `active` | Full |
   | `past_due` | Keep access; warn + portal/update payment; Retain retries auto-collected |
   | `paused` | Restrict or stop per product policy |
   | `canceled` | Revoke when status is `canceled` (scheduled cancel stays prior status until effective) |
5. **Lean cache, not a full mirror.** Store `customer.id`, `subscription.id`,
   `status`, item `price.id` / `product_id`, and `scheduled_change` timing.
   Prefer `subscription.created` + `subscription.updated` over polling.
6. **Proration is explicit.** Item changes need `proration_billing_mode`:
   `prorated_immediately`, `full_immediately`, `prorated_next_billing_period`,
   `full_next_billing_period`, or `do_not_bill`.
7. **Cancel/pause timing.** `effective_from`: `next_billing_period` (default) or
   `immediately`. Paused subscriptions cancel only immediately. Avoid cancel or
   pause within ~30 minutes of the next billing date.
8. **MoR tax is Paddle's job.** Do not invent a parallel tax engine for standard
   catalog sales; pass location signals Paddle needs and show Paddle-calculated
   totals.
9. **No card data on your servers.** Checkout and payment methods stay in Paddle.js
   / Paddle-hosted flows. Log object IDs and statuses only.

## Failure signatures

| Signature | Likely cause | First move |
| --- | --- | --- |
| Signature mismatch | Body parsed/rewritten before HMAC; wrong destination secret | Verify raw bytes; one secret per notification destination |
| 401 / auth errors | Live key on sandbox host (or reverse); missing `Bearer` | Match key environment to base URL |
| `resource` not found on known Dashboard ID | Sandbox ID against live (or reverse) | Compare `pri_`/`sub_` environment |
| Access revoked on `past_due` | Treated like canceled | Keep access; warn; wait for Retain / `canceled` |
| Duplicate grants or double side effects | Retries without `event_id` idempotency | Store processed `event_id` before side effects |
| Checkout opens, app never provisions | Relied on browser callback only | Provision from webhooks (`subscription.*` / `transaction.completed`) |
| `429` / `too_many_requests` | >240 req/min (or 1000 on preview endpoints) | Honor `Retry-After`; cache; prefer webhooks |
| Immediate upgrade charge blocked | Per-subscription immediate-charge caps | Space chargeable updates; use next-period proration when possible |

## Quick checkout sketch

```html
<script src="https://cdn.paddle.com/paddle/v2/paddle.js"></script>
<script>
  Paddle.Environment.set("sandbox"); // omit for live
  Paddle.Initialize({
    token: "ctkn_…", // client-side token, not API key
    eventCallback: (event) => {
      if (event.name === "checkout.completed") {
        // UX only — access still waits on webhooks
      }
    },
  });
  Paddle.Checkout.open({
    items: [{ priceId: "pri_…", quantity: 1 }],
    customData: { user_id: "internal-user-id" },
  });
</script>
```

Depth: `references/api.md` (checkout + REST), `references/webhooks.md` (verify +
events), `references/domain.md` (status, proration, Retain).
