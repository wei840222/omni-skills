# Billing Skill Research Sources

Verified 2026-09-24. Use these URLs before advising a PSP default, deadline, or recognition rule.

## Money, webhooks, and idempotency

- **Stripe — Currencies** — zero-decimal currencies and smallest-unit amounts via https://docs.stripe.com/currencies
- **Stripe — Webhooks** — signature verification on the raw body, retries, and out-of-order delivery via https://docs.stripe.com/webhooks
- **Stripe — Webhook signatures** — `Stripe-Signature` and official library verification via https://docs.stripe.com/webhooks#verify-official-libraries

## Subscriptions, cancel, and proration

- **Stripe — How subscriptions work** — status lifecycle and access implications via https://docs.stripe.com/billing/subscriptions/overview
- **Stripe — Subscription object** — `status`, `current_period_end`, `cancel_at_period_end` via https://docs.stripe.com/api/subscriptions/object
- **Stripe — Cancel subscriptions** — cancel at period end versus immediate cancellation via https://docs.stripe.com/billing/subscriptions/cancel
- **Stripe — Prorations** — `create_prorations`, `none`, and `always_invoice` via https://docs.stripe.com/billing/subscriptions/prorations
- **Stripe — Update a subscription** — `proration_behavior` must be set explicitly via https://docs.stripe.com/api/subscriptions/update

## Tax, PCI, disputes, usage, Connect

- **Stripe Tax** — tax calculation is jurisdiction-specific; do not hardcode rates via https://docs.stripe.com/tax
- **Stripe — Security** — tokenization and keeping card data off your servers via https://docs.stripe.com/security
- **PCI DSS** — cardholder data scope via https://www.pcisecuritystandards.org/standards/pci-dss/
- **Stripe — Disputes** — evidence windows and automatic loss on a missed deadline via https://docs.stripe.com/disputes
- **Stripe — Usage-based billing** — metered prices and reporting usage via https://docs.stripe.com/billing/subscriptions/usage-based
- **Stripe Connect — Separate charges and transfers** — platform fees and `reverse_transfer` on refunds via https://docs.stripe.com/connect/separate-charges-and-transfers
- **Stripe — PaymentIntents** — `requires_action` and incomplete payments via https://docs.stripe.com/payments/payment-intents

## Revenue recognition

- **Stripe Revenue Recognition** — deferred revenue versus cash collected via https://docs.stripe.com/revenue-recognition
- **FASB ASU 2014-09 (ASC 606)** — revenue from contracts with customers via https://storage.fasb.org/ASU%202014-09_Section%20A.pdf
- **IFRS 15** — revenue from contracts with customers via https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/
