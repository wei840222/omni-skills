# Domain knowledge - OpenTable

## Core rules

### 1. Anchor every change to a service goal

Before touching availability or policies, identify the target outcome:

- raise seated covers
- increase average check through better mix
- reduce no-shows and dead inventory
- protect guest experience at peak times

If the goal is unclear, propose options and get confirmation first.

### 2. Keep inventory honest across all time windows

Availability must reflect what operations can actually seat.

- Open only slots the kitchen or floor can absorb
- Separate peak, shoulder, and off-peak strategy
- Treat special events and holidays as explicit override windows

Prefer fewer accurate slots over inflated inventory that leads to walk-back.

### 3. Use pacing and table mix as primary control levers

Adjust flow with pacing first, not only with blanket block rules.

- Map party-size mix by hour
- Reserve capacity for high-value windows and turn targets
- Adjust release cadence for same-day demand spikes

Always document expected impact before applying broad slot changes.

### 4. Design guest messaging to prevent friction

Confirmations, reminders, and policy copy should reduce uncertainty.

- Keep cancellation windows explicit
- Send reminder timing based on lead-time profile
- Align special request language with what can actually be delivered

Use neutral policy explanations instead of punitive language.

### 5. Run weekly experiments with measurable hypotheses

Every optimization cycle must include:

- one hypothesis
- one controlled change
- one measurable result window
- one decision to keep, rollback, or iterate

Test one change at a time rather than stacking many changes in the same week when attribution matters.

### 6. Prepare failure paths before they are needed

For outages, overbookings, and confirmation failures:

- Detect quickly with operational signals
- Provide fallback booking or waitlist path
- Message affected guests with clear options
- Log cause, workaround, and prevention action

Reliability and trust beat short-term occupancy gains.

### 7. Protect access and guest data boundaries

Use least-privilege access for reservation operations.

- Keep account roles scoped to responsibilities
- Keep sensitive guest details out of long-lived notes
- Document only what is required for operational decisions

Ensure users supply credentials only through secure authenticated integrations rather than pasting into chat.

## Common traps

- Chasing occupancy without pacing controls → service collapses during peak turns
- Opening too much inventory early → high-value demand displaced by low-yield bookings
- Weak reminder and cancellation copy → avoidable no-shows and support load
- Editing listing content without testing impact → conversion drops without clear cause
- Ignoring incident postmortems → repeated failures and reactive firefighting

## Trust

OpenTable workflows depend on OpenTable services and configured integrations.
Only install and run this skill if you trust those services with reservation operations.

## Research notes (Gate 6)

Operational guidance below is grounded in official OpenTable help and hospitality capacity practice. Prefer live venue data over generic benchmarks when they conflict.

### Official product / help sources

- OpenTable Restaurant Center help home: https://restaurant.opentable.com/help/
- OpenTable availability and inventory management topics are documented in Restaurant Center help under availability, floor plans, and shifts (start from the help home and open the current availability articles for the venue's product tier).
- OpenTable guest communication and reservation modification guidance lives in Restaurant Center help under guest messaging / reservation management.

### Capacity and no-show practice

- Keep published inventory aligned to seatable covers and kitchen throughput; inflated slots create walk-backs and service failure.
- Use pacing, party-size mix, and release cadence before permanent hard blocks when the goal is demand shaping rather than a hard close.
- No-show reduction works best as a system: clear cancellation windows, lead-time-aware reminders, and measured policy changes—not punitive copy alone.

When OpenTable UI labels differ by product tier or region, verify against the venue's live Restaurant Center screens and the current help article rather than memorized menu names.
