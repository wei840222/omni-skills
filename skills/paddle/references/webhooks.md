# Webhooks — Paddle Billing

## Destination setup

1. Create a notification destination with type `url` (webhook).
2. HTTPS endpoint that accepts `POST` + JSON.
3. Subscribe to the events the app needs (see below).
4. Store that destination's **endpoint secret key** as a secret pointer — each
   destination has its own secret.
5. Set the destination API version deliberately (independent of account default).

Local dev: public URL required. Docs recommend tunnels such as Hookdeck CLI
(`hookdeck listen <port> paddle --path <path>`). Dashboard simulation and replay
APIs exist for fixtures.

## Delivery contract

| Rule | Detail |
| --- | --- |
| Success | HTTP `200` within **5 seconds** |
| Body | Do not parse/rewrite before signature check |
| Order | **Not** guaranteed — use `occurred_at` |
| Delivery | **At-least-once** — dedupe on `event_id` |
| Retries (sandbox) | 3 attempts within ~15 minutes |
| Retries (live) | Up to 60 attempts over ~3 days (backoff) |
| Exhausted | Notification `failed`; replay via API if needed |

Respond `200` **before** slow work (CRM writes, email, provisioning). Queue
internally.

### Optional IP allowlist

Allowlisting helps network policy; it is **not** authenticity. Always verify
signatures.

**Sandbox:** `34.194.127.46`, `54.234.237.108`, `3.208.120.145`,
`44.226.236.210`, `44.241.183.62`, `100.20.172.113`

**Live:** `34.232.58.13`, `34.195.105.136`, `34.237.3.244`, `35.155.119.135`,
`52.11.166.252`, `34.212.5.7`

User-Agent commonly includes `Paddle`. Bypass WAF bot challenges on the webhook
path.

## Payload envelope

| Field | Role |
| --- | --- |
| `event_id` (`evt_…`) | Idempotency key for the fact that happened |
| `event_type` | Routing key (`entity.action`) |
| `occurred_at` | Event time (RFC 3339) — ordering |
| `notification_id` (`ntf_…`) | This delivery attempt |
| `data` | Entity snapshot at event time |

One event can fan out to many notifications (one per destination).

## Recommended subscriptions for SaaS access

| Event | Typical action |
| --- | --- |
| `subscription.created` | Link customer/subscription IDs; grant access |
| `subscription.updated` | Refresh status, items, scheduled_change, period |
| `subscription.past_due` | Warn user; keep access; link portal / update payment |
| `subscription.paused` / `subscription.resumed` | Restrict / restore per policy |
| `subscription.canceled` | Revoke access |
| `transaction.completed` | Record payment / one-off fulfillment |
| `transaction.payment_failed` | Log; rely on Retain for auto-collection |

`subscription.updated` covers many renewals and plan changes; still handle
explicit status events your product cares about. Use the webhook simulator for
scenario traces.

## Signature verification

Header: `Paddle-Signature`, e.g. `ts=1671552777;h1=<hex>`.

1. Read header; require both `ts` and `h1`.
2. Optionally reject old `ts` (official SDKs default **5 second** tolerance —
   tighten only with clock-sync awareness; never skip HMAC).
3. Build signed payload: `ts` + `:` + **raw body string** (no re-serialization).
4. HMAC-SHA256 with the destination endpoint secret; hex digest.
5. Compare to `h1` with a constant-time equality check.

**Prefer official SDKs** (`@paddle/paddle-node-sdk` `paddle.webhooks.unmarshal`,
Go `WebhookVerifier`, PHP `Verifier`, etc.). Manual verify only when SDKs cannot
run.

### Manual sketch (Node.js)

```javascript
import { createHmac, timingSafeEqual } from "crypto";

function verifyPaddleSignature(rawBody, signatureHeader, secret) {
  if (!signatureHeader || rawBody == null) return false;
  const parts = Object.fromEntries(
    signatureHeader.split(";").map((p) => {
      const i = p.indexOf("=");
      return [p.slice(0, i), p.slice(i + 1)];
    }),
  );
  const ts = parts.ts;
  const h1 = parts.h1;
  if (!ts || !h1) return false;

  const body = Buffer.isBuffer(rawBody) ? rawBody.toString("utf8") : String(rawBody);
  const expected = createHmac("sha256", secret)
    .update(`${ts}:${body}`, "utf8")
    .digest("hex");

  const a = Buffer.from(h1, "utf8");
  const b = Buffer.from(expected, "utf8");
  return a.length === b.length && timingSafeEqual(a, b);
}

// express: app.post(path, express.raw({ type: "application/json" }), ...)
// On failure → 401. On success → parse JSON, enqueue, res.sendStatus(200).
```

### Manual sketch (Python)

```python
import hmac
import hashlib

def verify_paddle_signature(raw_body: bytes, signature: str, secret: str) -> bool:
    parts = dict(p.split("=", 1) for p in signature.split(";") if "=" in p)
    ts, h1 = parts.get("ts"), parts.get("h1")
    if not ts or not h1:
        return False
    signed = f"{ts}:{raw_body.decode('utf-8')}".encode("utf-8")
    expected = hmac.new(secret.encode("utf-8"), signed, hashlib.sha256).hexdigest()
    return hmac.compare_digest(h1, expected)
```

## Idempotent handler pattern

```text
receive → verify → parse → if event_id seen: 200 and stop
         → record event_id (pending/processed) → 200
         → apply business logic using occurred_at vs stored timestamps
```

Never key idempotency only on `notification_id` (retries of the same event share
`event_id` but not necessarily the same notification id across destinations).
