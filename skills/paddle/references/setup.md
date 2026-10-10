# Setup — Paddle

Use when the user is starting a Paddle integration or `<state_root>/` is empty.

## Goal

Reach a **sandbox** path that can: create/list products and prices, open a
Paddle.js checkout with a client-side token, receive one verified webhook, and
map `customData` / customer IDs back to the app user.

## Discover (do not interrogate)

Learn only what changes the integration shape:

1. Fresh Paddle account vs migration from Stripe/another PSP
2. Catalog shape: subscription SaaS, one-time, or mixed; trials or not
3. Stack: web only vs mobile link-out; Node/Go/Python/etc. for webhooks
4. Whether they already have sandbox API key, client-side token, and a public
   webhook URL (or tunnel)

Write durable non-secret answers under `<state_root>/memory.md` using
`references/memory-template.md`. Never store API keys or endpoint secrets in
files — pointers only (`env:…`, `1password:…`).

## Sandbox path (order)

1. **Seller account** — create/open a Paddle sandbox account; complete any
   required business profile later for live.
2. **API key (server)** — Dashboard → Authentication → API keys. Permissions
   least-privilege; rotatable when the platform supports it. Test with
   `GET /event-types` (works with empty catalogs).
3. **Client-side token** — separate from API keys; safe in frontend for
   checkout/price preview only.
4. **Catalog** — create product (`pro_…`) then price (`pri_…`) for each plan and
   billing interval. Recurring items on one checkout must share the same
   interval.
5. **Notification destination** — type `url`, HTTPS endpoint, subscribe at least
   `subscription.created`, `subscription.updated`, `subscription.canceled`,
   `subscription.past_due`, and `transaction.completed` (adjust to product).
   Copy that destination's **endpoint secret key** into a secret store.
6. **Handler** — raw body → verify signature → `200` fast → queue → idempotent
   apply. Details in `references/webhooks.md`.
7. **Checkout** — `Paddle.Initialize` + `Paddle.Checkout.open` with sandbox
   price IDs and `customData` carrying the internal user id.
8. **Access mapping** — on `subscription.created` / `updated`, upsert lean cache
   fields from `references/domain.md`.

## Live cutover (separate change)

- New live API key, client-side token, price IDs, and webhook destination/secret
- Pin notification destination API version deliberately
- Domain approval for checkout / Apple Pay association file when required
- Never point live webhooks at a handler still loaded with sandbox secrets

## Consent

Creating `<state_root>/` or writing memory needs user intent for continuity.
Read-only advice can proceed without files.
