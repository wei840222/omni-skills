# Money-Path Failures

Decode rule: the system that first *disagrees* names the layer. Processor vs store = integration; store vs warehouse = inventory; store vs bank = fees and timing.

| Symptom | Most likely cause | First move |
|---|---|---|
| Customer charged twice, one order | Retry with a new idempotency key, or a webhook handler with no dedupe | Reconcile by intent id; refund the duplicate before replying (Rule 2) |
| Paid in the processor, no order in the store | Webhook delivery failed, or the handler 500'd and the provider gave up | Backfill from the processor's charge list for the window, then fix the handler and replay |
| Order in the store, no payment | Authorization never captured, or captured after the auth expired (card auths hold days, not weeks) | Capture window audit; auto-cancel unpaid orders on a timer (`orders.md`) |
| Stock goes negative | Read-then-write decrement, or two channels selling the same unit | Conditional atomic update (Rule 3), then reconcile counts before reopening the SKU |
| Refund issued twice | Manual refund in the processor dashboard plus an automated one in the store | Refunds originate in one system only; the other one listens (`returns.md`) |
| Payout smaller than expected, no obvious reason | Reserve, chargebacks, FX conversion, or a monthly platform fee netted out | Rebuild it: gross − refunds − disputes − fees − reserve ± FX (`payments.md`) |
| Dispute lost without a fight | The response deadline passed inside an unread email | Every new dispute becomes a `## Due` row the day it opens (Rule 8, `fraud.md`) |
| Tax charged wrong, or not charged | Threshold crossed without registration, or a B2B VAT id accepted unvalidated | Registration triggers and validation in `tax.md`; a missed threshold is retroactive |
| Discount stacks below cost | Codes combinable with automatic promos and free shipping, no floor | Stacking rules and a CM floor per cart (Rule 4, `pricing.md`) |
| Conversion drops with no deploy | Payment method down, a shipping rate returning an error, or tracking broken | Place a real test order before reading any dashboard (`checkout.md`) |
| Store credit or gift card spent twice | Balance checked then decremented in two steps | Same conditional atomic write as stock (Rule 3) |
| Anything else | Follow one real order end to end — cart, charge, order, fulfillment, payout — and stop where the two systems first disagree | `orders.md` |
