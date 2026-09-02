# Validation

Run before payment preparation.

## Identity and duplicates
- Primary key: supplier tax ID + invoice number
- Weak key: canonical supplier + invoice number when tax ID is missing
- Same total/date under a new number may be a re-issue — inspect before paying twice

## Math and fraud checks
- Per rate band: line sums, tax, and total must reconcile within ±0.02
- Bank-detail changes halt the payment path until out-of-band verification
- Flag totals far above supplier norms for review rather than auto-filing as normal
