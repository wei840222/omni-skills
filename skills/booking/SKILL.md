---
name: booking
description: Search, compare, and book accommodation across platforms with real pricing and calculated fees. Use when the user wants to manage, search, plan, or review a booking.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏨"}'
---

## State location

Booking state may exist in `<workspace>/booking/`, `<workspace>/memory/booking/`, or `~/booking/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/booking/`, `<workspace>/memory/booking/`, `~/booking/`.
3. If none exists and state must be created, default to `<workspace>/booking/`.

Use the selected `<state_root>` for every state operation in this skill.

## Instructions

Load the following references when needed:
- Load `references/search.md` when the user wants to search, compare, or shortlist accommodations.
- Load `references/platforms.md` when you need information on platforms, data sources, and API choices.
- Load `references/pricing.md` to accurately calculate total costs and fees.

## User Preferences

Store preferences in `<state_root>/memory.md`. Load on activation.

```
<state_root>/
├── memory.md       # Traveler type, budget, preferences
├── history.md      # Past bookings, liked properties
└── alerts.md       # Active price tracking
```

## Critical Rules

1. **Calculate TOTAL cost always** — base price + cleaning fee + service fee + tourist tax + any extras. Always quote total cost including all fees.
2. **Compare 3+ platforms** before recommending — Booking.com, Airbnb, direct hotel, local platforms (Hostelworld, HousingAnywhere, etc.)
3. **Verify real-time data** — Check live availability and current prices via active searches.
4. **Ask about purpose** — tourist, business, family, remote work, budget. Needs differ completely.
5. **Surface deal-breakers early** — non-refundable, no A/C, far from center, negative review patterns, wifi issues for workers.
6. **Shortlist concisely** — Present 3-5 curated options with trade-offs.
7. **Execute when asked** — "book this" means book, execute the booking process.
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
