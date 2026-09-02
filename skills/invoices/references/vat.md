# VAT

Separate deduction logic from payment status.

## Extraction
- Capture gross, net, and VAT amounts
- Split VAT by rate band when multiple rates appear
- Note reverse charge / cross-border cases where the buyer accounts for VAT

## Deduction readiness
- A payment record alone does not prove deductibility
- The invoice must identify the recipient and, where required, the recipient tax ID
- Non-deductible or mixed-use amounts stay annotated on the ledger row for period close
