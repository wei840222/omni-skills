# Subledgers — receivables and payables

Load for AR aging, bad debt, AP bills, three-way match, early-pay discounts, or duplicate payments.

## Receivables

### Aging buckets

Standard buckets: current, 1–30, 31–60, 61–90, 90+. Review 90+ weekly when cash is tight.

### Allowance method (preferred under accrual)

1. Estimate uncollectible (history %, specific ID, or hybrid).
2. Dr bad debt expense / Cr allowance for doubtful accounts.
3. When a specific invoice is written off: Dr allowance / Cr AR (or expense if direct write-off is the elected small-entity method — stay consistent).

### DSO

`DSO ≈ (AR / credit sales) × days in period`. Rising DSO with flat sales signals collection friction.

### Customer deposits

Cash before delivery: liability (deferred revenue / customer deposits), not revenue.

## Payables

### Three-way match

For goods: PO ↔ receiving ↔ invoice. Mismatch holds payment until resolved.

### Goods received not invoiced

Accrue: Dr inventory or expense / Cr accrued liabilities (or GRNI). Clear when the invoice posts against the liability.

### Early-pay discount APR (approximate)

If terms are `x/n net N`:

`APR ≈ (x / (100 − x)) × (365 / (N − n))`

Use the APR to decide whether to take the discount versus using cash elsewhere.

### Duplicate payment

1. Confirm both payments cleared.
2. Dr cash or prepaid/other receivable / Cr AP or expense correction as appropriate once refund or credit is arranged.
3. Add a control: invoice number uniqueness check.

## Failure recovery

| Trigger | First fix | Still failing |
|---|---|---|
| Aging ≠ control | Find direct control JEs | Rebuild aging from open invoices |
| Write-off without allowance | Set policy; book allowance going forward | Document one-time direct write-off if materiality allows |
| Vendor balance disputed | Freeze payment; reconcile PO/receipt/invoice | Escalate to operator with package of three docs |
