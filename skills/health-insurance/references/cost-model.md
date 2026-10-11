# Cost Model — Annual Health Insurance Decision

Use three scenarios: low use, expected use, and high use.

## Formula

`annual_total = annual_premium + deductible_paid + copays + coinsurance + non_covered_costs`

## Inputs

- `annual_premium = monthly_premium * 12`
- `deductible_paid` depends on expected utilization
- `copays` by visit count and service category
- `coinsurance` for services billed after deductible
- `non_covered_costs` for out-of-network or excluded items


## Health Savings Account (HSA) Adjustments

If the plan is an HSA-eligible High Deductible Health Plan (HDHP):
- Subtract estimated employer HSA contributions from the annual total.
- Factor in the tax savings on employee HSA contributions.
- Note that for 2024, the IRS contribution limits are $4,150 for individuals and $8,300 for families, with a $1,000 catch-up for those 55+.
- Note that for 2024, the maximum out-of-pocket limits for HDHPs are $8,050 for individuals and $16,100 for families.

## Scenario Definitions

## Low Use

- Preventive and occasional routine visits only
- Minimal specialist use
- No major procedures

## Expected Use

- Routine visits + some specialist care
- Regular prescriptions
- At least one moderate diagnostic or procedure event

## High Use

- Multiple specialist events or chronic care intensity
- Potential emergency or hospital encounter
- Likely approach to out-of-pocket maximum

## Decision Rule

- Base choices on total expected cost rather than premium alone.
- Compare expected scenario first.
- Use high-use scenario to assess downside protection.
- If expected savings are small but downside risk is much lower, favor the safer plan.
