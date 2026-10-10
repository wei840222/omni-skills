---
name: billing
description: >
  Design and debug subscription billing, invoices, PSP webhooks, proration,
  dunning, tax handling, and revenue recognition. Use when configuring Stripe
  or another PSP, diagnosing webhook/access bugs, mid-cycle plan changes,
  cancel-at-period-end vs immediate delete, or ASC 606 deferred revenue.
  Not for one-off checkout-only flows owned by payments, stripe-api-integration,
  or paypal, and not for bookkeeping close owned by accounting.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💳"}'
  related-skills: '{"stripe-api-integration":"Stripe API call patterns once billing rules are chosen.","payments":"One-off checkout and payment capture outside subscription lifecycle.","subscriptions":"Subscription product design when the question is offer shape rather than PSP state.","paddle":"Paddle merchant-of-record billing instead of direct Stripe.","paypal":"PayPal-specific capture and dispute flows.","accounting":"Books, close, and ledger treatment after revenue events are recognized."}'
---

# Billing

Own **subscription billing correctness**: money in smallest units, webhook verification and idempotency, subscription access state, explicit proration, tax/invoice validity, PCI token boundaries, chargeback deadlines, usage metering, marketplace splits, and ASC 606 / IFRS 15 recognition. This package is stateless; do not persist card data, live secrets, or customer PII in the skill tree.

## When to load

Load for PSP subscription lifecycle work, webhook/access bugs, mid-cycle plan changes, invoice/tax field checks, dispute windows, Connect fee splits, or revenue-recognition questions tied to billed periods. Prefer adjacent skills when the ask is pure one-off checkout (`payments` / `stripe-api-integration` / `paypal`), offer-shape design without PSP state (`subscriptions`), Paddle MoR (`paddle`), or post-recognition bookkeeping (`accounting`).

## Progressive disclosure

Load a reference only when that topic is in scope:

| Topic | Load |
|-------|------|
| Core rules and billing traps | `references/domain.md` |
| Stripe objects and calls | `references/stripe.md` |
| Webhook verification and ordering | `references/webhooks.md` |
| Subscription lifecycle | `references/subscriptions.md` |
| Invoice generation | `references/invoicing.md` |
| Tax and invoice fields | `references/tax.md` |
| Usage-based billing | `references/usage-billing.md` |
| Chargebacks and PCI | `references/disputes.md` |
| Marketplace splits | `references/marketplace.md` |
| Revenue recognition | `references/revenue-recognition.md` |
| Source URLs before citing a limit or API default | `references/sources.md` |

## Non-negotiable invariants

1. Amounts are integers in the currency's smallest unit; never float dollars into PSP APIs.
2. Verify webhook signatures on the **raw** body before parse; store `event_id` for idempotency; design for out-of-order delivery.
3. Gate product access on subscription `status` **and** period bounds (`trialing`/`active` with valid period; do not treat `past_due`/`unpaid`/`canceled` after period end as paid access).
4. Default churn path is `cancel_at_period_end`; use immediate `subscription.delete()` only when the customer requests immediate termination.
5. Every mid-cycle plan change sets `proration_behavior` explicitly (`create_prorations`, `none`, or `always_invoice`).
6. Keep PAN/CVV/track data off servers; store only PSP tokens (`pm_*`, `cus_*`).
7. Before citing a PSP default, tax rule, dispute window, or recognition treatment, open `references/sources.md` and the linked official page.

## Safety

- Examples use placeholders only (`whsec_…`, `cus_…`, `sub_…`); never commit live secrets.
- Do not invent jurisdiction tax rates, dispute deadlines, or accounting treatments from memory when sources.md lists a canonical URL.
- Refund and chargeback paths must check open disputes before issuing a second credit.
