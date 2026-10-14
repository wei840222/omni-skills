# Sources (Gate 6)

Full URLs checked while refactoring this skill (2026-10-14). Re-open before
restating live fees, tax rules, dispute windows, SAQ eligibility, or API defaults.

## Agent skill format

- Agent Skills specification: https://agentskills.io/specification
- Agent Skills llms.txt: https://agentskills.io/llms.txt
- skills-ref validator: https://github.com/agentskills/agentskills/tree/main/skills-ref

## Stripe (official)

- Checkout: https://docs.stripe.com/payments/checkout
- Webhooks: https://docs.stripe.com/webhooks
- API keys: https://docs.stripe.com/keys
- Idempotent requests: https://docs.stripe.com/api/idempotent_requests
- Payment methods overview: https://docs.stripe.com/payments/payment-methods/overview
- Security guide: https://docs.stripe.com/security/guide
- Radar: https://docs.stripe.com/radar
- Disputes: https://docs.stripe.com/disputes
- 3D Secure: https://docs.stripe.com/payments/3d-secure
- Billing subscriptions overview: https://docs.stripe.com/billing/subscriptions/overview
- Subscription pending updates reference: https://docs.stripe.com/billing/subscriptions/pending-updates-reference
- Connect: https://docs.stripe.com/connect
- Pricing (verify live fees): https://stripe.com/pricing

## Paddle / Lemon Squeezy / PayPal

- Paddle developer portal: https://developer.paddle.com/
- Paddle Billing product: https://www.paddle.com/billing
- Paddle pricing (verify live fees): https://www.paddle.com/pricing
- Lemon Squeezy getting started: https://docs.lemonsqueezy.com/guides/getting-started
- Lemon Squeezy pricing (verify live fees): https://www.lemonsqueezy.com/pricing
- PayPal Checkout docs: https://developer.paypal.com/docs/checkout/

## PCI

- PCI SSC document library: https://www.pcisecuritystandards.org/document_library/
- PCI SSC standards overview: https://www.pcisecuritystandards.org/standards/

## Claim handling notes

| Claim class | Handling in this skill |
|-------------|------------------------|
| Card data off servers / webhook-first | Retained as hard invariants; aligned with Stripe security + webhooks docs |
| Fee tables | Orientation only; always re-open vendor pricing URLs |
| SAQ letter names | Orientation; confirm eligibility with current PCI docs / QSA |
| Dunning day ladder | Product pattern, not a guaranteed Stripe calendar — confirm Billing retries |
| Local payment methods | Coverage varies; check provider country matrices before promising |
