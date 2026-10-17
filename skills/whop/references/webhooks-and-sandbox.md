# Webhooks and Sandbox — Whop

## Webhook basics

Whop sends a signed `POST` to your public URL when subscribed events occur
(payment succeeded, membership activated, dispute opened, and related families).
Use webhooks to react to state changes, not to replace normal data validation.

High-signal event examples from the docs:
- `payment.succeeded`
- `membership.activated`
- `membership.deactivated`
- `entry.created`

Whop webhooks follow the
[Standard Webhooks](https://github.com/standard-webhooks/standard-webhooks)
specification. Prefer the official SDK verify helper when it exists.

Frozen request headers across API pins:
- `webhook-id`
- `webhook-signature`
- `webhook-timestamp`
- `content-type`

Envelope field note (retrieved 2026-10-18): webhooks pinned on/after
`2026-08-14` use `account_id`; older or unpinned webhooks may still emit
`company_id` for the same account field.

## Verification rules

- Copy the webhook secret and store it in `WHOP_WEBHOOK_SECRET`
- Verify every delivery before side effects
- Make handlers idempotent so retries or replays do not double-apply state
- Keep the HTTP response fast and push heavy work to a queue or background task

## Managing webhook endpoints

Use the REST API to audit current webhook endpoints:

```bash
curl -s "https://api.whop.com/api/v1/webhooks?company_id=$WHOP_COMPANY_ID&first=25" \
  -H "Authorization: Bearer ***"
```

Track at least:
- Company / account owning the webhook
- URL
- Environment: sandbox or production
- Events consumed by downstream code
- `api_version_date` pin when present

## Sandbox first

Whop provides a separate sandbox environment for safe testing:

| Environment | URL |
|-------------|-----|
| Frontend / dashboard | `https://sandbox.whop.com` |
| REST API | `https://sandbox-api.whop.com/api/v1` |
| Developer keys | `https://sandbox.whop.com/dashboard/developer` |

Auth header format matches production: `Authorization: Bearer ***`.
Configure sandbox webhooks separately from production.

Use sandbox when testing:
- Payins
- Membership activation and cancellation flows
- Webhook delivery handling
- Stats and permission wiring around payment data

SDK note: prefer the SDK `Sandbox` / environment switch (SDK 2.0+) so every host
moves together. On older clients, point the base URL at
`https://sandbox-api.whop.com/api/v1` explicitly.

## Official sandbox test cards

| Card | Result |
|------|--------|
| `4242 4242 4242 4242` | Successful payment |
| `4000 0000 0000 0002` | Declined payment |
| `4000 0000 0000 0341` | Card setup succeeds; later charges decline |
| `5385 3083 6013 5181` | Requires 3D Secure; docs say enter `Checkout1!` |

For sandbox cards:
- Use any future expiration date
- Use any 3-digit CVC
- Use any billing address

## Sandbox limitations

Live docs (retrieved 2026-10-18) warn:
- Do not rely on apps or messaging features in sandbox
- Alternative payment methods are limited; sandbox is oriented around card
  payments (no Apple Pay / Google Pay style alternatives in the sandbox guide)
- Treat Whop Elements sandbox availability as a live fact; do not promise it
  without checking current docs

That means sandbox is strong for payins and webhook plumbing, not full product
parity for every Whop surface.

## Go-live checklist

Before moving from sandbox to production:

1. Confirm production keys are separate from sandbox keys
2. Recreate webhook endpoints for production
3. Re-check required permissions and approvals on the production install
4. Re-run access checks against production IDs
5. Remove sandbox-specific URLs, cards, and assumptions from notes
6. Confirm production REST host is `https://api.whop.com/api/v1`

## Common failure patterns

- Sandbox works, production fails: wrong install, wrong permissions, or wrong IDs
- Webhook arrives but nothing updates: missing verification, duplicate
  suppression bug, or slow handler timeout
- Payment succeeded but entitlements did not change: webhook, product, plan, and
  access check are out of sync
- Envelope field mismatch (`account_id` vs `company_id`): check the webhook
  `api_version_date` pin
