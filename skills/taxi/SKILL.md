---
name: taxi
description: >
  Handle ground transportation for taxis, rideshares, and car services: live
  price comparison, surge handling, scheduled vs on-demand booking assistance,
  airport pickup rules, trip logging, dispute drafts, and lost-item recovery.
  Use when the user needs a ride now or later, wants Uber/Lyft/local-taxi
  options compared, is dealing with surge, airport transfers, accessibility or
  pet needs, receipt/expense capture, or a fare/safety/lost-item problem. Prefer
  `travel-planning` for whole-trip itineraries, `flight` for air legs and
  disruption rights, `car-rental` for multi-day self-drive, `expenses` for
  ledgering trip costs, and `travel` for standing travel documents and boxes.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🚕"}'
  related-skills: '{"travel-planning":"Whole-trip itineraries and budgets beyond a single ground leg.","flight":"Air segments, delay tracking inputs, and passenger-rights questions.","car-rental":"Multi-day or multi-stop self-drive instead of repeated rides.","expenses":"Ledger taxi costs into categories, reimbursements, and monthly totals.","travel":"Standing travel system, documents, and long-lived trip boxes."}'
---

# Taxi

Assist with ground transportation decisions and follow-through. Compare live
options, help prepare booking steps the user must confirm, log durable trip
state under `<state_root>/`, and guide disputes or lost-item recovery through
the correct in-app channels.

## State location

Taxi preferences and trip logs may exist in `<workspace>/taxi/`,
`<workspace>/memory/taxi/`, or `~/taxi/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/taxi/`, `<workspace>/memory/taxi/`, `~/taxi/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable state must be created, default to
   `<workspace>/taxi/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. If older
notes exist only at `~/Clawic/data/taxi/`, propose a copy/validation/cutover plan
and wait for user confirmation before any migration. Never write the literal
string `<state_root>` to disk.

## When to use

- Compare current Uber, Lyft, Bolt, taxi, shuttle, or car-service options
- Decide whether to wait out surge, walk away from a venue, or schedule ahead
- Airport transfers with terminal, pickup-zone, and flight-delay awareness
- Accessibility, pet, child-seat, group, late-night, or VIP vehicle constraints
- Draft fare disputes, lost-item contacts, or safety reports after a ride
- Log business/personal trips and hand totals to `expenses` when asked

## Quick reference

Load only what the current ask needs:

| Need | Load |
|------|------|
| Preferences / first setup | `references/memory.md` + `assets/taxi-data-templates.md` |
| City and app coverage | `references/cities.md` |
| Price, surge, promo checks | `references/fares.md` |
| Booking workflow | `references/booking.md` |
| Disputes, lost items, safety | `references/problems.md` |
| Official source pins | `references/sources.md` |

## Core rules

### 1. Know user context first

Before recommending a ride, read `<state_root>/memory.md` when it exists for:

- Preferred apps and why
- Saved addresses (home, work, airport/terminal)
- Payment preferences (card nickname, cash, business profile)
- Special needs (wheelchair, car seat, pet-friendly)
- Budget sensitivity and max acceptable surge

If memory is missing, ask only the fields required for this trip and offer to
persist them under `<state_root>/` after the user agrees.

### 2. Compare before booking

| Task | Agent action |
|------|----------------|
| User needs a ride | Compare 3+ options with current estimates when available |
| Surge detected | Show multipliers, suggest wait/walk/schedule/transit alternatives |
| Airport transfer | Compare rideshare vs taxi vs shuttle vs car service and pickup rules |
| Group ride | Check whether XL/van or multiple cars is cheaper |
| Regular route | Note historical windows when prices were lower |

### 3. Maximize savings without hiding trade-offs

- Search active promos and referral credits before non-urgent bookings
- Compare scheduled vs on-demand pricing
- Suggest shared/pool only when time and luggage allow
- Monitor surge and notify when it drops below the user's threshold
- Prefer airport flat rates or taxi stands when they beat metered/surge options

### 4. Assist booking; user confirms payment

Agent can:

- Open booking sites/apps
- Prefill pickup, destination, vehicle type, promo, and schedule
- Stop at the payment-confirmation step

User must:

- Confirm final payment
- Enter new payment methods
- Complete phone verification

### 5. Special scenarios

| Scenario | Handle |
|----------|--------|
| Airport pickup | Terminal, designated zone, flight tracking, meet-and-greet |
| Business travel | Receipts, corporate profile, expense category |
| Late night | Safety features, ratings, shared trip tracking |
| Foreign city | Local apps, cash/card norms, language tips |
| Accessibility | WAV / wheelchair filter and company confirmation when needed |
| Pets / kids | Pet policy, carrier rules, car-seat availability |
| Events | Exit-point planning and surge avoidance |

### 6. Track trips

When the user asks to record a trip, append to `<state_root>/trips.md`:

- Date, route, app, price, promo, category, notes

Offer monthly category totals and hand business rows to `expenses` when asked.

### 7. Resolve problems

1. Classify: overcharge, route, driver, safety, lost item, cancellation
2. Use the in-app help path first (`references/problems.md`)
3. Draft a factual complaint with trip IDs, times, screenshots needed
4. Track status; escalate only after the platform path is exhausted

### 8. Stay current and multi-modal

- Prefer live app estimates over memorized regional price bands in
  `references/fares.md`
- Re-check city coverage in `references/cities.md` before assuming Uber/Lyft
- Compare public transit, hotel shuttle, rental car, or walk + rideshare when
  they beat door-to-door cost or wait time

### 9. Privacy and safety

- Store only masked payment references (last four / nickname), never full card
  numbers, CVVs, or PINs
- Mask home addresses in shared logs when the user prefers
- Share live trip tracking with emergency contacts when requested
- Verify plate, photo, and pin before the user enters the vehicle
- For immediate danger, use the in-app emergency control and local emergency
  services; keep distance and report through the app afterward

Prefer concrete next actions over warning lists when guiding safety or
dispute flows.

## Common traps

- Booking during surge without showing the multiplier → always surface it
- Assuming one app works everywhere → check local alternatives first
- Ignoring scheduled rides → often cheaper for early airport runs
- Delaying business trip logging → harder to categorize later
- Applying the first promo found → check stacking and expiry terms
- Recommending cheapest alone → safety and reliability matter at night
- Skipping airport pickup rules → wrong curb, terminal fee, or wait charges
- Ignoring flight delays → ride arrives, user is still airborne
- Skipping saved preferences → re-ask what memory already knows

## Out of scope

- Full multi-city itineraries → `travel-planning`
- Flight search, fare rules, or aviation passenger rights → `flight`
- Multi-day self-drive → `car-rental`
- Lodging booking → `booking`
- Standing passport/visa boxes → `travel`
- General bookkeeping beyond trip evidence → `expenses` / `accountant`
