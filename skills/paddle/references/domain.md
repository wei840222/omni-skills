# Domain rules — Paddle Billing

## Subscription status → access

Official status values include: `trialing`, `active`, `past_due`, `paused`,
`canceled`.

| Status | Access guidance |
| --- | --- |
| `trialing` | Full access (treat like active) |
| `active` | Full access |
| `past_due` | **Keep access**; show banner; deep-link customer portal / update payment. Automatically collected subs: Paddle Retain retries. Manually collected invoices: customer must pay; Retain does not drive those the same way. |
| `paused` | Restrict or read-only per product; make resume obvious |
| `canceled` | No access once status is `canceled` |

Scheduled cancel/pause: status often stays `active` / `past_due` until
`scheduled_change.effective_at`. Store that timestamp so UX can say when access
ends.

Lean fields to cache (from provision guidance):

- `customer.id`, `subscription.id`, `subscription.status`
- `items[].price.id`, `items[].price.product_id` (feature mapping)
- `scheduled_change` (action + `effective_at`)
- billing period bounds when showing renewal dates

Primary events: `subscription.created`, `subscription.updated`. Add
`transaction.completed` for one-off charges.

## Proration (`proration_billing_mode`)

When replacing items or quantities mid-cycle:

| Mode | Behavior |
| --- | --- |
| `prorated_immediately` | Bill prorated delta now |
| `full_immediately` | Bill full amount now (no proration math) |
| `prorated_next_billing_period` | Proration calculated now; charge next renewal |
| `full_next_billing_period` | Full amount next renewal |
| `do_not_bill` | No charge for the change |

Engine is minute-level. Immediate chargeable updates face per-subscription rate
caps (`references/api.md`). Preview customer impact before applying upgrades.

## Cancel and pause

**Cancel** `POST /subscriptions/{id}/cancel` with `effective_from`:
`next_billing_period` (default) or `immediately`.

- Next period: scheduled change; status becomes `canceled` when it fires.
- Immediate: status `canceled` now (required path for already-paused subs).
- `past_due` may stay past_due until period end if cancel is scheduled; Retain may
  still collect unless canceled immediately.

**Pause** `POST /subscriptions/{id}/pause` with `effective_from` and optional
`resume_at`. Customer portal does **not** self-serve pause — build app workflow
or use Dashboard. On pause of auto-collected renewals, Paddle may cancel open
past-due recurring transactions to avoid overlap. Resume may start a new billing
period (charge) depending on `on_resume` / timing.

Avoid cancel/pause within about **30 minutes** of the next billing date.

## Paddle Retain (dunning)

For **automatically collected** subscriptions, Payment Recovery retries failed
payments over a multi-day window (docs describe a default ~30-day recovery
effort), with email / optional in-app / SMS. Success moves `past_due` → `active`
when no other past-due transactions remain; next billing date stays on schedule.

Do **not** implement a competing retry mailer that fights Retain. Product job on
`past_due`: warn, collect updated method, keep access until `canceled` or policy
says otherwise after Retain exhausts (pause vs cancel is a Retain/dashboard
setting).

## Merchant of record

Paddle is MoR for supported catalog sales: tax calculation and remittance are
Paddle's responsibility. Pass accurate customer location/address data Paddle
requests; display Paddle-calculated totals rather than a second tax engine for
the same charge.

## Common traps

| Trap | Corrective |
| --- | --- |
| Hard-coded `pri_…` across sandbox/live | Env-specific config; never mix |
| Trust checkout.js success alone | Provision on webhooks |
| Revoke on first `past_due` | Keep access; warn; wait for cancel/Retain outcome |
| Parse body before HMAC | Raw body only |
| One shared webhook secret for all destinations | Secret per `ntfset_…` |
| Poll subscriptions in a tight loop | Webhooks + cache; respect 240 rpm |
| Ignore `scheduled_change` | Users still entitled until effective time |
| Assume portal supports pause | Pause is API/Dashboard only |
| Cardless trial assumptions without price flags | Check trial `requires_payment_method` on price |
