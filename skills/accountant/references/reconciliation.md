# Reconciliation — bank, card, processor

Load when bank, card, loan, or processor balances must match the ledger before reporting.

## Definition of done

Reconciled means both adjusted balances equal to the cent:

```text
bank statement ending balance
+ deposits in transit
− outstanding payments
± bank errors
= ledger cash balance
+ collections and interest not yet in ledger
− fees and returned items not yet in ledger
± ledger errors
```

A leftover difference is a finding, not a rounding plug.

## Procedure

1. Pull the statement ending balance and date for the exact account.
2. Build the bank-side adjusted balance (outstanding items, deposits in transit).
3. Build the ledger-side adjusted balance (unrecorded fees, interest, chargebacks).
4. Compare. If unequal, classify the difference before hunting single lines.
5. Clear matched items; leave unmatched items as open reconciling items with owners.
6. Record completion in `<state_root>/memory.md` (account nickname, statement date, difference = 0, open items if any).

## Difference diagnostics

| Test | If true | Likely cause |
|---|---|---|
| Difference ÷ 9 has no remainder | Transposition (e.g. 540 vs 450) | Digits swapped on entry |
| Difference ÷ 2 equals a known amount | One side posted twice or reversed | Duplicate or sign error |
| Difference equals a single deposit/payment | Timing or omitted item | In transit or missing entry |
| Difference equals processor fee total | Net deposit booked as revenue | Gross-up missing |

Then bisect by date range: half the period, then the half that still breaks, until the batch is isolated.

## Processor deposits (Stripe / PayPal / Shopify style)

The deposit is **net** of fees, refunds, and chargebacks.

Correct pattern:

1. Book **gross** sales (and tax collected) to revenue / liability.
2. Book fees to fee expense (or contra-revenue if policy says so — pick one and stay consistent).
3. Book refunds and chargebacks to their accounts.
4. The net cash hit matches the deposit.

Booking the deposit as revenue understates revenue and expenses and permanently distorts margin.

## Failure recovery

| Trigger | First fix | Still failing |
|---|---|---|
| Difference persists after ÷9/÷2 | Date-range bisect; check beginning balance carry-forward | Rebuild from last known-good recon |
| Beginning balance ≠ prior ending | Prior period was edited after close | Open prior-period correction path (reverse + re-post in open period) |
| Difference grows across months | Systematic miscoding or conversion break | Mark reporting provisional; load `audit-cleanup.md` and `escalate.md` |
| Multiple currencies in one account | Separate functional cash books or clear FX each period | Isolate FX gain/loss before recon |
