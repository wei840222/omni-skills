---
name: booking
description: Search, compare, and book accommodation across platforms with real pricing and calculated fees. Use when the user wants hotel, Airbnb, hostel, VRBO, or long-stay lodging options, total-cost comparisons, cancellation checks, or help completing a booking.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🏨"}'
  related-skills: '{"travel-planning":"Extends lodging choices into a full itinerary, packing list, and whole-trip budget.","flight":"Pairs accommodation dates with flight search, fare rules, and disruption handling."}'
---

## State location

Booking state may exist in `<workspace>/booking/`, `<workspace>/memory/booking/`, or `~/booking/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/booking/`, `<workspace>/memory/booking/`, `~/booking/`.
3. If none exists and the user asks to retain booking state, default to `<workspace>/booking/`.

Use the selected `<state_root>` for every state operation in this skill. If multiple candidates exist, use the highest-precedence one, report the duplicate state, and keep the other copies unchanged. Treat prior Clawic paths as migration sources only; migrate them only through a user-approved copy, validation, and cutover.

## State and privacy

When `<state_root>/memory.md` exists, read it before applying saved traveler preferences. Read `<state_root>/history.md` only for a request about past stays or liked properties. Read `<state_root>/alerts.md` only for price-tracking work.

Create or update state only when the user asks to save preferences, track a stay, or set an alert. Keep payment credentials, government ID numbers, and full card data out of state; store only non-secret pointers when needed.

```
<state_root>/
├── memory.md       # Traveler type, budget, preferences
├── history.md      # Past bookings, liked properties
└── alerts.md       # Active price tracking
```

## Instructions

Load the following references when needed:
- Load `references/search.md` when the user wants to search, compare, or shortlist accommodations.
- Load `references/platforms.md` when you need information on platforms, data sources, and API choices.
- Load `references/pricing.md` to accurately calculate total costs and fees.

## Default workflow

1. Confirm trip context: dates, party size, purpose, budget ceiling, and non-negotiables.
2. Search at least 3 platforms relevant to the stay type; verify live availability and current totals.
3. Calculate true total cost for every shortlisted option (base + cleaning + service + tax + extras).
4. Present 3-5 curated options with trade-offs, cancellation deadlines, and location context.
5. If live lookup fails for a platform, drop that platform from the comparison, state the gap, and continue with verified sources.
6. If no option meets the budget or hard constraints, report the closest verified alternatives and the blocking constraint.

Mode: **advise by default**. Present options with total cost and let the user pick. Prepare a booking draft or fill a form only when requested. The user completes payment unless they explicitly ask the agent to finish checkout with credentials they provide in-session.

## Critical Rules

1. **Calculate TOTAL cost always** — base price + cleaning fee + service fee + tourist tax + any extras. Always quote total cost including all fees.
2. **Compare 3+ platforms** before recommending — Booking.com, Airbnb, direct hotel, local platforms (Hostelworld, HousingAnywhere, etc.).
3. **Verify real-time data** — Check live availability and current prices via active searches.
4. **Ask about purpose** — tourist, business, family, remote work, budget. Needs differ completely.
5. **Surface deal-breakers early** — non-refundable, no A/C, far from center, negative review patterns, wifi issues for workers.
6. **Shortlist concisely** — Present 3-5 curated options with trade-offs.
7. **CHECKPOINT before checkout** — Before any paid booking step, restate property name, dates, guest count, total price, cancellation deadline, and payment channel; proceed only after the user confirms that exact summary.
8. **Check cancellation policy** — state deadline clearly before any booking.

## Traveler-Specific Traps

| Type | Common Model Failure |
|------|---------------------|
| Casual | Ignoring stated budget, recommending based on popularity not fit |
| Business | Missing corporate rates, not understanding loyalty program math |
| Family | Treating "2 bedrooms" as sufficient without checking bed config, missing safety issues |
| Backpacker | Recommending mid-range, not calculating fees, missing hostel direct pricing |
| Nomad | Multiplying nightly×30 instead of real monthly rate, trusting "wifi included" |

## Before Recommending Any Property

- [ ] Total price calculated with ALL fees
- [ ] Cancellation policy stated
- [ ] Location context (walking time to center/meeting/beach)
- [ ] Review patterns checked (cleanliness, noise, wifi for workers, family-friendliness)
- [ ] Deal-breakers surfaced if any
