# Stripe Domain Knowledge

Source-backed facts that keep Stripe guidance current. Prefer official docs over secondary summaries when they conflict.

## Platform facts

- Stripe is a financial infrastructure and software company that provides payment processing, billing, Connect marketplaces, tax, fraud, and related APIs. Dual headquarters: South San Francisco, California and Dublin, Ireland. Overview: https://en.wikipedia.org/wiki/Stripe,_Inc.
- Official product docs and API reference are the primary operational sources: https://docs.stripe.com/ and https://docs.stripe.com/api
- API versioning is explicit; integrations should pin an API version and treat upgrades as a project: https://docs.stripe.com/api/versioning
- Webhook signatures must be verified against the raw request body with the endpoint signing secret: https://docs.stripe.com/webhooks/signatures
- PaymentIntents are the recommended online card payment flow object; fulfill from events, not only the create/confirm response: https://docs.stripe.com/payments/payment-intents
- Amounts are integers in the currency minor unit; currency exponents differ (for example JPY is zero-decimal): https://docs.stripe.com/currencies
- Idempotency keys prevent duplicate side effects on retries and are honored for about 24 hours: https://docs.stripe.com/api/idempotent_requests
- Connect charge type (direct, destination, separate charges and transfers) decides fees, liability, and customer ownership: https://docs.stripe.com/connect/charges
- Test clocks advance subscription and billing time in test mode; they do not prove live Radar, payout timing, or enabled payment methods: https://docs.stripe.com/billing/testing/test-clocks
- Strong Customer Authentication / 3D Secure guidance for European and similar regimes: https://docs.stripe.com/payments/3d-secure

## Research notes for this refactor

- Confirmed that several historical companion filenames referenced by the pre-refactor package were never present as files on `main`; control-plane and reference links now point only at existing `references/` files.
- Retained operational rules from the original package (webhook-as-truth, minor-unit amounts, idempotency, metadata, PCI boundary, mode disclosure) while moving Configuration / Traps / Experts into `references/`.
