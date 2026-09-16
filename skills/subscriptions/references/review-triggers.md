# Review triggers — subscriptions

Operational defaults for keep/cancel and renewal hygiene. Replace thresholds when the user states stricter policy.

## Unused 30+ days

- Detection: `Last used` older than 30 days, or user says they have not opened the service
- Action: propose cancel; state monthly savings if cancelled
- Exceptions: seasonal tools (tax software, vacation apps) marked by the user; keep with next expected-use note

## Price increase

- Detection: merchant email, bank descriptor, or user-reported new price differs from stored Cost
- Action: show `old → new` and annualized delta; offer keep / downgrade / cancel
- Do not silently overwrite Cost until the user confirms the new baseline

## Annual renewal window

- Default lead time: **7 days before** charge date
- Surface: service name, amount, payment method pointer, cancel-or-keep decision
- After charge posts without prior reminder: log miss in notes and restore the 7-day cadence

## Quarterly value review

- Cadence: about every 90 days per paid inventory
- Prompt: "Still getting value from X at $Y/period?"
- Outcome states: keep, downgrade, pause/seasonal, cancel
- Write the decision and date so the next review is not amnesia

## Billing-this-week scan

- List every active row with billing day inside the next 7 days
- Useful opener: "3 subscriptions bill this week — want a keep/cancel pass?"

## Severity ladder (optional)

| Signal | Suggested urgency |
|--------|-------------------|
| Annual charge ≤7 days, amount ≥ user high-threshold | High — ask now |
| Unused 30+ days, medium/low value | Medium — cancel candidate |
| Price up <10% on essential service | Low — note and monitor |
| Duplicate family plans | Medium — consolidate |

## Handoffs

- Full cashflow or CSV statement work → `personal-finance-tracker`
- Debt/save sequencing after cut list is known → `money`
- Calendar-only nudge after decision is made → `remind`
