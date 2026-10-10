# Security and privacy — Paddle

## Trust boundary

| Direction | Data | Notes |
| --- | --- | --- |
| App → `sandbox-api.paddle.com` / `api.paddle.com` | Customer email/name, addresses, subscription and price IDs, amounts Paddle already owns | Server API key in `Authorization` |
| Browser → Paddle.js / checkout | Payment method entry, client-side token | PCI scope stays with Paddle when you never touch PAN |
| Paddle → your webhook URL | Event snapshots (`evt_…`), subscription/transaction payloads | Verify every delivery |

No other third party should receive Paddle secrets or raw webhook bodies from
this skill's guidance.

## Required controls

1. **API keys and endpoint secrets** — environment variables or a secret manager
   only. Under `<state_root>/` store pointers (`env:PADDLE_API_KEY`), never values.
2. **Client-side tokens only in frontend** — never embed server API keys in JS,
   mobile binaries, or public repos.
3. **Webhook authenticity** — `Paddle-Signature` HMAC on raw body; optional IP
   allowlist is additive only (`references/webhooks.md`).
4. **No PAN/CVC storage** — if card data would touch your server, stop and move
   the flow back to Paddle.js / hosted checkout.
5. **Log hygiene** — log `event_id`, `subscription_id`, status codes; never log
   full `Authorization` headers, endpoint secrets, or raw payment methods.
6. **Environment isolation** — separate secrets, price IDs, and destinations for
   sandbox vs live; prevent cross-env webhook acceptance when practical
   (secret mismatch should fail closed).

## This skill must not

- Write credentials into the skill package or git
- Invent tax filing advice beyond "Paddle MoR calculates/remits for supported sales"
- Exfiltrate customer billing data to non-Paddle systems without explicit user direction
