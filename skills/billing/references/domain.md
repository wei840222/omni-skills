## Core Rules

### 1. Money in Smallest Units, Always
- Stripe/most PSPs use cents: `amount: 1000` = $10.00
- Store amounts as integers exclusively (floating-point math fails)
- Always clarify currency in variable names: `amount_cents_usd`
- Different currencies have different decimal places (JPY has 0, KWD has 3)

### 2. Webhook Security is Non-Negotiable
- Verify the `Stripe-Signature` header against the raw body before processing
- Store `event_id` and check idempotency — webhooks duplicate
- Events arrive out of order — design state machines rather than sequential flows
- Use raw request body for signature verification instead of parsed JSON
- See `references/webhooks.md` for implementation patterns

### 3. Subscription State Machine
Critical states and transitions:
| State | Meaning | Access |
|-------|---------|--------|
| `trialing` | Free trial period | Full |
| `active` | Paid and current | Full |
| `past_due` | Payment failed, retrying | Grace period |
| `canceled` | Will end at period end | Until period_end |
| `unpaid` | Exhausted retries | None |

Grant paid access only when status is `trialing` or `active` and the current period has not ended. Treat `past_due` as grace-period policy, not full paid certainty; `unpaid` and post-period `canceled` revoke access.

### 4. Cancel vs Delete: Revenue at Stake
- `cancel_at_period_end: true` → Access continues until period ends, then halts renewal
- `subscription.delete()` → Immediate termination, possible refund
- Confusing these loses revenue OR creates angry customers
- Default to cancel-at-period-end; immediate delete only when requested

### 5. Proration Requires Explicit Choice
When changing plans mid-cycle:
| Mode | Behavior | Use When |
|------|----------|----------|
| `create_prorations` | Credit unused, charge new | Standard upgrades |
| `none` | Change at renewal only | Downgrades |
| `always_invoice` | Immediate charge/credit | Enterprise billing |

Specify proration mode on every plan change. Treat an omitted PSP default as unspecified.

### 6. Race Conditions Are Guaranteed
`customer.subscription.updated` fires BEFORE `invoice.paid` frequently.
- Design for eventual consistency
- Use database transactions for access changes
- Idempotent handlers that can safely reprocess
- Status checks before granting/revoking access

### 7. Tax Compliance Is Mandatory
| Scenario | Action |
|----------|--------|
| Same country | Charge local VAT/sales tax |
| EU B2B + valid VAT | 0% reverse charge (verify via VIES) |
| EU B2C | MOSS — charge buyer's country VAT |
| US | Sales tax varies by 11,000+ jurisdictions |
| Export (non-EU) | 0% typically |

Missing required invoice fields = legally invalid invoice. See `references/tax.md`.

### 8. PCI-DSS: Keep Card Data Off-Server
- Keep PAN, CVV, and magnetic stripe data off your servers
- Only store PSP tokens (`pm_*`, `cus_*`)
- Tokenization happens client-side (Stripe.js, Elements)
- Even "last 4 digits + expiry" is PCI scope if stored together
- See `references/disputes.md` for compliance patterns

### 9. Chargebacks Have Deadlines
| Stage | Timeline | Action |
|-------|----------|--------|
| Inquiry | 1-3 days | Provide evidence proactively |
| Dispute opened | 7-21 days | Submit compelling evidence |
| Deadline missed | Automatic loss | Set alerts |

Three or more consecutive failed charge attempts can trigger fraud monitoring — cap retries and alert.

### 10. Revenue Recognition ≠ Cash Collected
For SaaS under ASC 606/IFRS 15:
- Annual payment ≠ annual revenue (recognized monthly)
- Deferred revenue is a liability rather than an asset
- Multi-element contracts require allocation to performance obligations
- See `references/revenue-recognition.md` for accounting patterns


## Billing Traps

### Security & Compliance
- Webhook without signature verification → attackers fake `invoice.paid`
- Storing tokens in frontend JS → extractable by attackers
- CVV in logs → PCI violation, massive fines
- Retry loops without limits → fraud monitoring triggers

### Integration Errors
- Omitting `subscription_id` storage → impossible to reconcile refunds
- Assuming charge success = payment complete (3D Secure exists)
- Ignoring `payment_intent.requires_action` → stuck payments
- Using `mode: 'subscription'` without handling `customer.subscription.deleted`

### Financial Errors
- Hardcoding tax rates → wrong when rates change
- Amounts in dollars when PSP expects cents → 100x overcharge
- Recognizing 100% revenue upfront on annual plans → audit findings
- Confusing bookings vs billings vs revenue → material discrepancies

### Operational Errors
- Sending payment reminders during contractual grace period
- Dunning without checking for open disputes → double loss
- Proration without specifying mode → unexpected customer charges
- Refunding without checking for existing chargeback → paying twice
