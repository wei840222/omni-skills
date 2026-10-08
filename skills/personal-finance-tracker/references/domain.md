# Domain Knowledge — Personal Finance Tracker

## Core Rules

### 1. Start with the Runway Review

- Answer three questions first: what cash is available now, what fixed obligations hit next, and what room is actually free to spend.
- A finance tracker that cannot tell the user whether they are safe this week is not useful.
- Use `review-rhythm.md` to frame the first snapshot in under 30 seconds.

### 2. Normalize inputs before making claims

- Clean dates, signs, merchants, categories, and duplicates before summarizing patterns, whether the input comes from CSV exports or pasted transaction lines.
- Messy exports create fake insights and broken budgets.
- Use `csv-schema.md` and `scripts/cashflow_rollup.py` before giving trend or category conclusions.

### 3. Separate recurring drag from one-off spend

- Distinguish rent, utilities, debt payments, subscriptions, and annual charges from irregular purchases.
- Users usually fail because fixed drag hides inside noisy transaction lists.
- Use `scripts/recurring_scan.py` and `debt-triage.md` to isolate what repeats and what can be cut.
- Before claiming a merchant is recurring, normalize name variants (`Netflix`, `Netflix.com`, `NETFLIX`).

### 4. Prioritize cashflow before optimization theater

- Protect essentials, taxes, minimum debt payments, and near-term obligations before discussing long-range goals.
- Fancy charts are useless if the account risks overdraft next week.
- Recommend protect, watch, cut, or defer actions instead of generic motivation.

### 5. Turn every review into a concrete next-action list

- End each session with a short list: pay, cancel, renegotiate, transfer, delay, or monitor.
- Cap next actions at three; if more exist, re-prioritize.
- Use `review-rhythm.md` to close weekly and monthly reviews with named actions.

### 6. Keep storage minimal, local, and opt-in

- Save only balances, recurring commitments, debt priorities, and review decisions the user wants remembered.
- Require explicit user consent before creating local files for sensitive finance data.
- Use `assets/memory-template.md` only after the user agrees to continuity and `<state_root>` is resolved.

### 7. Maintain separation between guidance and account control

- This skill can analyze, classify, forecast, and prepare plans.
- It must not move money, cancel services, log into banks, or present itself as regulated financial advice.
- Keep recommendations transparent, reversible, and grounded in the user-provided data.

## Operating Rhythm

### Fast snapshot

- Cash on hand now
- Payments due in the next 7 to 14 days
- Largest recurring drains
- Free-to-spend amount after essentials

### Weekly review

- Compare actual outflow vs expected outflow
- Flag duplicate charges, subscription drift, and overspend categories
- Update the cut list and next bill dates

### Monthly reset

- Rebuild recurring obligations
- Re-rank debt pressure and savings targets
- Capture what changed in income, bills, and available runway

## Common Traps

- Tracking every coffee but ignoring annual charges -> false sense of control and surprise cash hits.
- Mixing personal, business, and tax money in one mental bucket -> bad decisions and missed obligations.
- Treating subscriptions as harmless small spend -> silent monthly drag compounds quickly.
- Looking only at category charts -> hides due dates, debt penalties, and account timing risk.
- Forecasting from raw exports without cleanup -> duplicates and sign errors corrupt the plan.
- Letting the agent store full statements by default -> unnecessary privacy exposure.
- Treating positive monthly net as safety when early due dates still exceed cash on hand.

## Source Notes (Gate 6)

Household cashflow practice here is operational, not product-specific:

- Runway and free-to-spend framing follows standard personal cashflow review practice (cash now − near-term obligations).
- Recurring detection uses merchant normalization plus cadence windows (~monthly 25–35 days, ~annual 330–380 days) as heuristics, not guarantees.
- Debt triage modes (avalanche / snowball / cashflow relief) are decision biases; choose by rate variance, motivation, or monthly drag—not as investment advice.
- No bank API, fee schedule, or jurisdiction-specific tax rule is asserted without a user-supplied figure or an official source opened in-session.
