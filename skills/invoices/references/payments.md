# Payments

Decode terms before scheduling payment.

## Terms
- Parse net days and early-discount windows (for example `2/10 net 30`)
- Compute discount APR before choosing speed: `APR = (d / (1 - d)) × (365 / (net days - discount days))`
- Take the discount only when APR exceeds the cost of capital

## Payment run
- Prefer unpaid, non-disputed, approved invoices
- Partial payments and credit notes update the ledger remaining balance
- Mark paid only after a real bank/card movement is confirmed; a payment is not a VAT deduction
