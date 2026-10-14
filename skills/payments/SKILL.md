---
name: payments
description: >
  Choose payment providers, design one-off checkout, webhooks, refunds,
  subscriptions, and PCI-safe payment handling. Use when picking Stripe vs
  Paddle vs LemonSqueezy vs PayPal or Gumroad; building hosted/embedded checkout;
  verifying webhook-first fulfillment; handling trials, proration, dunning, or
  cancellation; or reviewing fraud, 3DS, chargebacks, and card-data boundaries.
  Prefer `billing` for PSP subscription state machines and ASC 606,
  `stripe-api-integration` for Stripe call-level debugging, `paypal` for PayPal
  REST, `paddle` for Paddle MoR APIs, `subscriptions` for offer-shape design
  without PSP wiring, and `webhook` for generic receiver security.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💳"}'
  related-skills: '{"billing":"Subscription lifecycle, proration, dunning, tax/invoice fields, and revenue recognition once PSP rules dominate.","stripe-api-integration":"Stripe API objects, Checkout Sessions, Connect, and webhook signature debugging.","paypal":"PayPal REST checkout, OAuth tokens, and PayPal disputes.","paddle":"Paddle merchant-of-record catalog, checkout, and tax handling.","subscriptions":"Offer tiers, trials, and packaging when the ask is product design not PSP state.","webhook":"Generic webhook receivers, signatures, retries, and idempotency beyond payment providers.","crm":"Contact and pipeline hygiene after a paid lead becomes a CRM record.","saas":"SaaS packaging and go-to-market when payments are only the monetization layer."}'
---

# Payments

Ship **money-safe checkout**: pick the right processor, keep card data off your
servers, treat **webhooks as truth**, store amounts in smallest currency units,
and design refunds, disputes, and subscription edges before go-live.

This skill is **stateless by default** for one-shot provider selection and
checkout design. Optional local notes may live under a resolved `<state_root>`
only when the user wants continuity. Never store PAN/CVV, live secrets,
customer PII dumps, or webhook signing secrets in the skill package.

## State location

Optional payment design notes may exist in `<workspace>/payments/`,
`<workspace>/memory/payments/`, or `~/payments/`. Before reading or writing
state, resolve `<state_root>`:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/payments/`, `<workspace>/memory/payments/`, `~/payments/`.
3. If several candidate directories exist, use only the highest-precedence one and
   report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create
   `<workspace>/payments/` by default.
5. If the host cannot supply `<workspace>`, read an existing `~/payments/` only;
   otherwise ask for a state root before creating data.
6. If older data exists only under `~/clawic/payments/` or
   `~/Clawic/data/payments/`, move it into the resolved `<state_root>/` after the
   user confirms, and say in one line that you moved it and from where.

Use the selected `<state_root>` for every state operation in this skill.
Typical layout (create children only when needed):

- `<state_root>/notes/` — provider choice memos (no secrets)
- `<state_root>/checklists/` — go-live checklists without live keys

## When to use

- Choose Stripe, Paddle, LemonSqueezy, PayPal, Gumroad, or a specialized high-risk processor
- Design hosted checkout, embedded elements, or (rarely) custom tokenized forms
- Wire webhook-first fulfillment, idempotency keys, refunds, and dispute intake
- Plan subscription trials, upgrades, dunning, and cancellation UX
- Review PCI SAQ posture, 3DS, fraud signals, and chargeback prevention

Prefer adjacent skills when the remaining work is Stripe API debugging
(`stripe-api-integration`), PayPal REST (`paypal`), Paddle MoR APIs (`paddle`),
subscription *product* packaging without PSP state (`subscriptions`), deep
billing state machines / recognition (`billing`), or generic webhook receivers
(`webhook`).

## Safety order (always)

1. Keep raw card data completely off application servers; use hosted checkout or
   provider tokenization so PCI stays at SAQ-A / SAQ-A-EP when possible.
2. Treat client-side success callbacks as untrusted. Fulfill only after a
   verified webhook (or equivalent server confirmation).
3. Put an idempotency key on every charge-creating request; design webhook
   handlers to be idempotent on provider event IDs.
4. Store money as integers in the currency's smallest unit; never float dollars
   into PSP APIs.
5. Examples use placeholders only (`whsec_…`, `sk_test_…`, `cus_…`); never commit
   live secrets or paste production keys into skill state.
6. Before citing live fees, tax rules, dispute windows, or API defaults, open
   `references/sources.md` and the linked official page.

## Quick workflow

1. Lock **product type** (one-off digital, physical goods, SaaS subscription,
   marketplace) and **markets** (US, EU VAT, high-risk).
2. Pick processor class: full-service (Stripe), merchant-of-record (Paddle /
   LemonSqueezy), simple hosted (Gumroad), or specialized high-risk.
3. Choose checkout surface: hosted redirect/overlay first; embedded elements when
   brand control matters; custom forms only with explicit UX need.
4. Design webhook events, signature verify, async fulfillment, and refund path
   before UI polish.
5. For subscriptions, define trial, proration, dunning, and cancel-at-period-end
   behavior up front.
6. Load the smallest reference for the active topic; re-open sources before
   quoting prices or limits.

## Progressive disclosure

| Situation | Load |
|-----------|------|
| Core rules, red flags, go-live checklist | `references/domain.md` |
| Stripe / Paddle / LemonSqueezy / PayPal / Gumroad choice | `references/providers.md` |
| Checkout surfaces, webhooks, amounts, errors | `references/integration.md` |
| Trials, tiers, dunning, proration, cancel UX | `references/subscriptions.md` |
| PCI, fraud, 3DS, chargebacks, refunds | `references/security.md` |
| Verified official URLs before citing fees/APIs | `references/sources.md` |

## Non-negotiable invariants

1. **No raw card data on your servers** — hosted checkout or tokenization only.
2. **Webhooks are truth** — client callbacks never grant paid access alone.
3. **Idempotency everywhere** — charges and webhook handlers must tolerate retries.
4. **Integer minor units** — store and send amounts as cents/pence (or zero-decimal rules).
5. **Cancel is easy** — dark-pattern cancel flows create chargebacks and bad reviews.
6. **Verify before quote** — fees, tax, and dispute windows come from `references/sources.md`, not memory.
