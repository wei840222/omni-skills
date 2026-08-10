# Risk Playbook — Stock Market

Apply this before validating any trade candidate.

## Position Risk Formula

Use:

`maximum_units = max_risk_amount / abs(entry_price - invalidation_price)`

Before applying the formula, confirm that `entry_price` and `invalidation_price` are finite, positive, and different. For a long candidate, require `invalidation_price < entry_price`; for a short candidate, require `invalidation_price > entry_price`. If any condition fails, keep the candidate un-sized and state the failed condition.

Where:
- `max_risk_amount` is the user's approved loss limit for one idea; for a percentage limit, calculate it as `account_value × approved_risk_percentage`
- `abs(entry_price - invalidation_price)` is the per-share risk for either a long or short setup

The formula returns a maximum unit count, not an order. Use fractional units only after confirming that the user's broker supports them for the instrument. Otherwise calculate `whole_units = floor(maximum_units)`, then recompute `planned_loss = whole_units × abs(entry_price - invalidation_price)` and confirm it does not exceed `max_risk_amount`. If the supported unit count is zero or cannot be established, keep the candidate un-sized. If the size is too large for liquidity or the approved exposure limit, reduce the unit count or exclude the candidate; preserve the thesis-derived invalidation rather than widening it to fit a larger position.

## User-Approved Limits

| Control | Record before sizing |
|---------|----------------------|
| Max risk per trade | User-approved monetary amount or account percentage |
| Max daily loss | User-approved monetary amount or account percentage |
| Correlated exposure | User-defined aggregation method and limit |
| Total open risk | User-approved monetary amount or account percentage |

Risk tolerance and time horizon are personal; record the user's limit rather than presenting a universal percentage as a standard.

## Volatility Adjustment

During high-volatility sessions:
- Recalculate per-share risk from the updated invalidation and current price data.
- Compare the resulting exposure with the user's approved limits.
- Model gap scenarios separately for earnings and major events.

During low-volatility sessions, keep targets and liquidity assumptions explicit; a tighter invalidation does not by itself justify a larger position.

## Conditions for an Un-sized Candidate

Keep the candidate un-sized when any condition is true:
- No invalidation condition can be defined.
- Entry or invalidation is non-finite, non-positive, or equal to the other price.
- The invalidation is not below entry for a long candidate or above entry for a short candidate.
- The supported unit format is unknown, or whole-unit rounding produces zero units.
- Catalyst timing or current data source is unclear.
- Bid/ask spread or liquidity makes exits unreliable.
- The written plan is being overridden by emotion.
- The user-approved daily loss limit is already reached.

## Post-Trade Risk Review

After close, present the review in the response. Record it in persistent state only when persistent state is enabled and the user approves that review update:
- Planned risk vs realized loss/gain
- Whether rules were followed
- Which limit prevented larger damage, if any

The objective is a documented, repeatable planning process rather than a short-term win-rate target.
