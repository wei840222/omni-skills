# Research Sources — Stripe API Integration

Primary developer documentation, API specifications, and operational references for Stripe payment workflows.

## Official Documentation & API Reference

- **Stripe Documentation** — https://docs.stripe.com/
  - Core guides for online payments, checkout sessions, billing, and fraud prevention.
- **Stripe API Reference** — https://docs.stripe.com/api
  - Endpoint definitions, parameters, request objects, and error types.
- **Stripe API Versioning** — https://docs.stripe.com/api/versioning
  - API version pinning, backwards compatibility guidelines, and breaking change changelogs.
- **Webhook Signatures** — https://docs.stripe.com/webhooks/signatures
  - Verifying webhook signatures via `Stripe-Signature` header, timestamp tolerance, and HMAC-SHA256 secret validation.

## Product-Specific Guides

- **PaymentIntents Lifecycle** — https://docs.stripe.com/payments/payment-intents
  - PaymentIntent status flow (`requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `succeeded`).
- **Stripe Connect & Payouts** — https://docs.stripe.com/connect
  - Standard, Express, and Custom accounts, transfer schedules, and KYC compliance.
