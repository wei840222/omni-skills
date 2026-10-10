# API and checkout — Paddle Billing

Facts below track Paddle Billing API **version 1** docs. Confirm live pages via
`references/sources.md` before asserting a new limit.

## Base URLs and auth

| Environment | API base |
| --- | --- |
| Sandbox | `https://sandbox-api.paddle.com` |
| Live | `https://api.paddle.com` |

```http
Authorization: Bearer pdl_…   # server API key — never ship to browsers
Paddle-Version: 1             # optional but recommended; cannot go below account default
Content-Type: application/json
```

- **API keys** — full server access per assigned permissions; secret.
- **Client-side tokens** (`ctkn_…`) — Paddle.js checkout and client previews only.
- Smoke-test auth with `GET /event-types` (no catalog required).

## ID prefixes (selection)

| Prefix | Entity |
| --- | --- |
| `ctm_` | Customer |
| `sub_` | Subscription |
| `txn_` | Transaction |
| `pri_` | Price |
| `pro_` | Product |
| `evt_` | Event |
| `ntf_` | Notification (delivery attempt) |
| `ntfset_` | Notification destination |
| `ctkn_` | Client-side token |
| `apikey_` | API key id |
| `dsc_` | Discount |
| `add_` | Address |
| `biz_` | Business |

IDs are lexicographically sortable (creation order). Always store the full ID
string; never strip prefixes.

## Rate limits

| Scope | Limit (docs) | On exceed |
| --- | --- | --- |
| Most API operations | 240 requests / minute / IP | `429` `too_many_requests`; wait `Retry-After` (commonly 60s) |
| Transaction/price **preview** endpoints | 1000 / minute / IP | same |
| Chargeable subscription updates (`prorated_immediately` / `full_immediately` with no credit) | 20 / hour and 100 / 24h **per subscription** | subscription immediate-charge errors |

Mitigations: `include=` related entities, cache, webhooks instead of poll loops,
client-side `Paddle.PricePreview` / `Paddle.TransactionPreview` when appropriate.

## Common server calls

Replace host with sandbox or live. Placeholders only — no real secrets.

```bash
# Create customer
curl -sS -X POST "$PADDLE_API/customers" \
  -H "Authorization: Bearer $PADDLE_API_KEY" \
  -H "Paddle-Version: 1" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","name":"Ada Lovelace"}'

# List subscriptions for a customer
curl -sS "$PADDLE_API/subscriptions?customer_id=ctm_…" \
  -H "Authorization: Bearer $PADDLE_API_KEY" \
  -H "Paddle-Version: 1"

# Cancel (default: end of billing period)
curl -sS -X POST "$PADDLE_API/subscriptions/sub_…/cancel" \
  -H "Authorization: Bearer $PADDLE_API_KEY" \
  -H "Paddle-Version: 1" \
  -H "Content-Type: application/json" \
  -d '{"effective_from":"next_billing_period"}'

# Pause
curl -sS -X POST "$PADDLE_API/subscriptions/sub_…/pause" \
  -H "Authorization: Bearer $PADDLE_API_KEY" \
  -H "Paddle-Version: 1" \
  -H "Content-Type: application/json" \
  -d '{"effective_from":"next_billing_period"}'

# Resume
curl -sS -X POST "$PADDLE_API/subscriptions/sub_…/resume" \
  -H "Authorization: Bearer $PADDLE_API_KEY" \
  -H "Paddle-Version: 1" \
  -H "Content-Type: application/json" \
  -d '{"effective_from":"immediately"}'
```

When changing items on a subscription, send `proration_billing_mode` (see
`references/domain.md`). Inspect transaction `details.line_items.proration` when
debugging mid-cycle charges.

## Paddle.js checkout

```html
<script src="https://cdn.paddle.com/paddle/v2/paddle.js"></script>
<script>
  Paddle.Environment.set("sandbox"); // remove or set live for production
  Paddle.Initialize({
    token: "ctkn_…",
    eventCallback: (e) => {
      // e.name === "checkout.completed" → success UX only
    },
  });

  Paddle.Checkout.open({
    items: [{ priceId: "pri_…", quantity: 1 }],
    customer: { email: "user@example.com" }, // optional prefill
    customData: { user_id: "internal-user-id" },
    // settings.successUrl optional; or handle checkout.completed
  });
</script>
```

Rules:

- `Paddle.Initialize` once per page; later updates use `Paddle.Update`.
- Recurring items in one checkout share the same billing interval.
- `customData` must be JSON with ≥1 key; copied to the transaction and, for
  recurring items, onto the created subscription.
- Prefer opening with `items` **or** an existing `transactionId`, not conflicting
  both without intent.
- Browser success is **not** provisioning — wait for webhooks.

## Errors (shape)

```json
{
  "error": {
    "type": "request_error",
    "code": "not_found",
    "detail": "…",
    "documentation_url": "https://developer.paddle.com/errors/…"
  }
}
```

Treat `too_many_requests` as load control, not a permanent business failure.
Auth failures usually mean wrong environment or missing Bearer key.
