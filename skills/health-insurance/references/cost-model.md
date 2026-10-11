# Cost Model — Annual Health Insurance Decision

Use three scenarios: low use, expected use, and high use.

## Formula

`annual_total = annual_premium + deductible_paid + copays + coinsurance + non_covered_costs`

When the plan is HSA-eligible, adjust after the base total:

`adjusted_total = annual_total - employer_hsa_contribution - estimated_tax_savings_on_employee_hsa`

## Inputs

- `annual_premium = monthly_premium * 12`
- `deductible_paid` depends on expected utilization (cannot exceed the plan deductible)
- `copays` by visit count and service category
- `coinsurance` for services billed after deductible
- `non_covered_costs` for out-of-network or excluded items
- HSA inputs only when the plan is an HSA-eligible HDHP for that plan year

## Health Savings Account (HSA) and HDHP Limits

If the plan is an HSA-eligible High Deductible Health Plan (HDHP):

1. Confirm the **plan year / calendar year** before citing any dollar figure.
2. Subtract estimated employer HSA contributions from the annual total.
3. Factor estimated tax savings on employee HSA contributions (jurisdiction-dependent; label assumptions).
4. Apply the IRS annual contribution limitation and HDHP out-of-pocket ceiling for that year.
5. Catch-up contributions for age 55+ remain **$1,000** under IRC §223 unless a later statute changes them; verify before advising.

### Verified IRS inflation-adjusted amounts (orientation baselines)

| Calendar year | HSA contribution limit (self-only) | HSA contribution limit (family) | HDHP minimum deductible (self / family) | HDHP maximum OOP (self / family) | Primary source |
| --- | --- | --- | --- | --- | --- |
| 2024 | $4,150 | $8,300 | $1,600 / $3,200 | $8,050 / $16,100 | IRS Rev. Proc. 2023-23 |
| 2025 | $4,300 | $8,550 | $1,650 / $3,300 | $8,300 / $16,600 | IRS Rev. Proc. 2024-25 |
| 2026 | $4,400 | $8,750 | $1,700 / $3,400 | $8,500 / $17,000 | IRS Rev. Proc. 2025-19 |

Full URLs live in `references/sources.md`. If the user is modeling a later year than this table covers, stop and fetch the current IRS revenue procedure before quoting limits.

## Scenario Definitions

### Low Use

- Preventive and occasional routine visits only
- Minimal specialist use
- No major procedures

### Expected Use

- Routine visits + some specialist care
- Regular prescriptions
- At least one moderate diagnostic or procedure event

### High Use

- Multiple specialist events or chronic care intensity
- Potential emergency or hospital encounter
- Likely approach to out-of-pocket maximum

## Decision Rule

- Base choices on total expected cost rather than premium alone.
- Compare expected scenario first.
- Use high-use scenario to assess downside protection.
- If expected savings are small but downside risk is much lower, favor the safer plan.
- For HDHP vs copay-plan debates, show the HSA tax/employer offset **and** the high-use OOP path side by side.
