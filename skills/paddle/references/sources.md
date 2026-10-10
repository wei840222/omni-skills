# Primary sources — Paddle Billing

Prefer the live document over memorized limits. Fetched for this refactor against
Paddle developer docs (Billing API v1 era).

## Platform and packaging

- [Agent Skills specification](https://agentskills.io/specification)
- [skills-ref validator](https://github.com/agentskills/agentskills/tree/main/skills-ref)
- [Paddle docs index (llms.txt)](https://developer.paddle.com/llms.txt)

## Authentication, versioning, IDs, limits

- [Authentication](https://developer.paddle.com/api-reference/about/authentication) — Bearer API keys vs client-side tokens
- [Versioning](https://developer.paddle.com/api-reference/about/versioning) — `Paddle-Version`, current v1
- [Paddle IDs](https://developer.paddle.com/api-reference/about/paddle-ids) — prefixes (`ctm_`, `sub_`, `pri_`, …)
- [Rate limiting](https://developer.paddle.com/api-reference/about/rate-limiting) — 240/min, preview 1000/min, subscription immediate-charge caps
- [API overview / quickstart](https://developer.paddle.com/api-reference/about) — `GET /event-types` smoke test

## Webhooks

- [How webhooks work](https://developer.paddle.com/webhooks/about/how-webhooks-work) — envelope, at-least-once, `event_id`
- [Handle webhook delivery](https://developer.paddle.com/webhooks/about/respond-to-webhooks) — 5s / 200, retries, sandbox vs live IPs
- [Verify webhook signatures](https://developer.paddle.com/webhooks/about/signature-verification) — `Paddle-Signature` `ts`/`h1`, HMAC-SHA256, SDK 5s skew
- [Notification destinations](https://developer.paddle.com/webhooks/about/notification-destinations)

## Subscriptions and access

- [Provision access and subscription state](https://developer.paddle.com/build/subscriptions/provision-access-webhooks) — lean cache, status table, `past_due` access
- [Get subscription](https://developer.paddle.com/api-reference/subscriptions/get-subscription) — status enum and scheduled changes
- [Cancel subscriptions](https://developer.paddle.com/build/subscriptions/cancel-subscriptions) — `effective_from`
- [Pause subscriptions](https://developer.paddle.com/build/subscriptions/pause-subscriptions) — portal gap, resume behavior
- [Proration](https://developer.paddle.com/concepts/subscriptions/proration) — `proration_billing_mode` values
- [Payment recovery / Retain dunning](https://developer.paddle.com/concepts/retain/payment-recovery-dunning)

## Checkout / Paddle.js

- [Paddle.Initialize](https://developer.paddle.com/paddle-js/methods/paddle-initialize)
- [Paddle.Checkout.open](https://developer.paddle.com/paddle-js/methods/paddle-checkout-open)
- [checkout.completed](https://developer.paddle.com/paddle-js/events/checkout-completed)
- [Include Paddle.js](https://developer.paddle.com/paddle-js/about/include-paddlejs)

## SDKs

- [paddle-node-sdk](https://github.com/PaddleHQ/paddle-node-sdk)
- [paddle-go-sdk](https://github.com/PaddleHQ/paddle-go-sdk)
