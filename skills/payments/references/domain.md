# Payments domain rules

## Universal rules

**Card data must remain strictly off your servers.** Use provider-hosted checkout
or tokenization. PCI compliance burden explodes the moment raw card numbers touch
your application servers.

**Webhooks are truth.** Client-side success callbacks lie. A payment succeeded
only when your verified webhook (or equivalent server confirmation) says so.
Design fulfillment webhook-first.

**Test mode exists for a reason.** Use test cards, simulate declines and disputes,
and verify webhook handling before live keys. Production surprises cost real money
and real customers.

**Pricing psychology vs retention.** `$9.99/mo` can feel cheaper than `$120/yr`,
but annual plans often retain better. Prefer offering both; default presentation
depends on product, not a fixed slogan.

## Provider quick compare

| Need | Starting recommendation |
|------|-------------------------|
| US/global B2C, developer control | Stripe |
| SaaS selling into EU with VAT burden | Paddle or Lemon Squeezy (merchant of record) |
| Simple digital product, minimal eng | Gumroad or Lemon Squeezy hosted |
| Marketplace splits | Stripe Connect |
| High-risk / adult / gambling niches | Specialized processors (e.g. CCBill, Epoch) — expect higher fees and reserves |

See `references/providers.md` for decision detail. Re-open
`references/sources.md` before quoting live percentage fees.

## Integration checklist (before go-live)

- [ ] Webhook endpoint HTTPS + signature verification on the **raw** body
- [ ] Idempotency keys on charge-creating API calls
- [ ] Webhook handlers idempotent on provider event IDs
- [ ] Declined / expired / insufficient-funds paths tested
- [ ] Receipts and invoices configured for the chosen provider model
- [ ] Refund and partial-refund flows tested
- [ ] Subscription lifecycle events handled (if recurring): activate, fail, cancel
- [ ] Amounts stored in minor units; zero-decimal currencies documented
- [ ] No PAN/CVV/logging of full card numbers anywhere

## Red flags (block ship)

- Storing CVV anywhere, ever → immediate PCI violation
- Trusting only client-side payment confirmation → fraud vector
- No retry / dead-letter path for failed webhooks → lost fulfillment
- Hardcoding prices only in the frontend → easy manipulation
- Missing `cancel_at_period_end` (or provider equivalent) handling → angry subscribers
- Inventing live fee tables from memory instead of opening sources

## Adjacent handoff

| If the remaining work is… | Prefer |
|---------------------------|--------|
| Stripe object/API debugging | `stripe-api-integration` |
| PayPal REST / disputes | `paypal` |
| Paddle MoR APIs | `paddle` |
| Deep subscription state + recognition | `billing` |
| Offer packaging without PSP wiring | `subscriptions` |
| Generic webhook receiver design | `webhook` |
