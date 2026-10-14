# Payment integration patterns

## Checkout flow options

### Hosted checkout (default recommendation)

Provider hosts the payment UI; your app redirects or opens an overlay.

- **Stripe:** Checkout Sessions
- **Paddle:** overlay or redirect checkout
- **Lemon Squeezy:** hosted checkout links
- **PayPal:** hosted / JS SDK checkout (see `paypal`)

**Pros:** PCI-friendliest path, less custom UI risk
**Cons:** Less brand control; redirect can drop some conversions

### Embedded elements

Provider components render inside your page (tokenized fields).

- **Stripe:** Payment Element / Card Element patterns
- **Paddle:** inline JS patterns

**Pros:** On-site UX
**Cons:** More state handling; still never touch raw PAN in your backend

### Custom form (only with explicit UX need)

You build the form and tokenize via provider SDK.

- Increases integration surface and PCI questionnaire scope
- Prefer hosted/elements unless product requirements force custom UI

## Webhook architecture

**Webhooks are the source of truth.** Client-side callbacks are untrusted hints.

### Essential event classes (names vary by provider)

| Business outcome | Typical event family (Stripe-oriented examples) |
|------------------|--------------------------------------------------|
| Payment succeeded | `payment_intent.succeeded` / checkout completed |
| Payment failed | `payment_intent.payment_failed` |
| Invoice paid (subs) | `invoice.paid` |
| Subscription changed | `customer.subscription.updated` |
| Subscription ended | `customer.subscription.deleted` |
| Refund | `charge.refunded` |
| Dispute opened | `charge.dispute.created` |

Map equivalents when on Paddle / Lemon Squeezy / PayPal — do not invent event
names; open provider docs via `references/sources.md`.

### Webhook security checklist

1. Verify signature against the **raw** request body (not a re-serialized JSON object)
2. HTTPS only; reject unsigned or skew-expired events per provider tolerance
3. Return success quickly; queue slow fulfillment
4. Idempotent processing keyed by provider event ID
5. Log enough to debug without storing PAN or full payment method secrets

### Failure handling

Providers retry. Handlers must tolerate duplicates and out-of-order delivery.
Missing events need reconciliation jobs (list recent successful payments vs
granted access), not silent hope.

## Currency and amount handling

**Store and transmit amounts in the currency's smallest unit** (cents, pence).

```text
✅ $10.00 → 1000
✅ €25.50 → 2550
❌ 10.00 as float into charge APIs
```

Also account for **zero-decimal** currencies (e.g. JPY) and any three-decimal
special cases per provider docs. Display formatting is separate from storage.

## Idempotency

Every charge-creating request needs an idempotency key scoped to the **business
action** (order id + attempt semantics), not a random retry stamp alone.

Without idempotency:

- Timeout leaves charge state unknown
- Blind retry can double-charge

With idempotency:

- Same key returns the original result
- Safe to retry transport failures

Stripe documents idempotent request behavior; other PSPs have equivalents —
confirm in sources before coding.

## Error handling

| Error class | User-facing | System |
|-------------|-------------|--------|
| Declined | Try another card / contact bank | Log decline code; no retry spam on hard declines |
| Insufficient funds | Same | Soft decline may allow later retry |
| Expired card | Update payment method | Portal / update flow |
| Fraud suspected | Contact bank / support path | Block + manual review |
| Processor outage | Retry later | Backoff + status page |

Never expose raw processor codes as the only UX string. Map to plain language.

## Testing checklist

- [ ] Happy-path payment + fulfillment
- [ ] Decline path
- [ ] Webhook signature success and failure
- [ ] Duplicate webhook delivery
- [ ] Refund full and partial
- [ ] 3DS / SCA path when required for market
- [ ] Zero-decimal currency if you sell into those markets
- [ ] Cancel / proration paths for subscriptions
