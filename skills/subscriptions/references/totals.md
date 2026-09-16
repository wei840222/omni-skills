# Totals — subscriptions

How to keep `<state_root>/totals.md` honest.

## Monthly rollup

1. Read every entry under `active/`
2. Normalize each cost to a monthly figure:
   - `/month` → as stated
   - `/year` → divide by 12
   - `/week` → multiply by 52/12
   - `/quarter` → divide by 3
3. Sum by category file (streaming / software / services)
4. Write category subtotals and **Total: $X/month = $Y/year** where `Y = X * 12`

## Annual renewals coming

- List upcoming `/year` (or annualized large) charges with date and amount
- Sort ascending by next charge date
- Keep only still-active rows; remove after cancel or after the charge is acknowledged

## Rebuild rules

- Rebuild after add, cost change, category move, or cancel
- If category sum ≠ derived active sum, prefer active files as source of truth
- Round to cents when currency uses decimal subunits; say when FX conversion is approximate

## Example surface lines

- "You spend $147/month on subscriptions ($1,764/year)."
- "Streaming is $43/month — largest bucket."
- "Adobe renews Sep 15 for $660."
- "Cancelling Hulu saves $18/month."

## Currency

- Keep one primary currency per totals file when possible
- If mixed currencies appear, show per-row currency and avoid fake single-total precision unless the user provides an FX rate
