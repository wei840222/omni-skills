# Recurring Payments - Google Pay

Use this file when checkout includes recurring billing or renewals.

## Scope clarification

Google Pay improves initial payment entry, but recurring charges depend on
backend and PSP contracts that differ from one-time checkout. Prefer the
`billing` and `subscriptions` skills for renewal state machines, dunning, and
offer design; use `stripe-api-integration` or `paypal` for PSP-specific API
debugging.

## Required decisions

- Is Google Pay used for initial payment method capture only?
- Which PSP handles recurring billing lifecycle events?
- What is the renewal failure and dunning strategy?

## Recurring flow basics

1. Capture the initial payment method through the Google Pay flow.
2. Store a reusable payment method reference via the PSP.
3. Run renewals from the backend scheduler or billing engine.
4. Reconcile renewals through webhook events (`webhook` skill).

## Validation checklist

- Initial Google Pay checkout and first invoice succeed.
- Renewal charge succeeds without user interaction when expected.
- Failed renewal moves to retry and notification flow correctly.
- Cancel and reactivation behavior matches product policy.

## Common pitfalls

- Assuming one-time payload behavior matches recurring contracts.
- Missing renewal reconciliation, causing a false active state.
- Not testing expired funding sources and payment method updates.
- Inventing a Google-Pay-only renewer instead of handing off to billing/PSP.
