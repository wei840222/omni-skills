---
name: travel-planning
description: Plan trips with itineraries, multi-city routing, budget optimization, and packing lists. Use when coordinating travel bookings, tracking trip expenses, or organizing family logistics.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"✈️"}'
  related-skills: '{"daily-planner":"Places trip activities into daily schedules.","expenses":"Tracks complex travel expenses against the budget.","plan":"Provides generalized project planning for long-term trip preparation."}'
---

## State location

Travel Planning state may exist in `<workspace>/travel-planning/`, `<workspace>/memory/travel-planning/`, or `~/travel-planning/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/travel-planning/`, `<workspace>/memory/travel-planning/`, `~/travel-planning/`.
3. If none exists and state must be created, default to `<workspace>/travel-planning/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

On first use, read `references/setup.md` for onboarding guidelines. Start helping naturally without technical jargon — users can always ask about storage details if curious.

## When to Use

User wants to plan a trip, track travel expenses, organize bookings, coordinate group/family travel, or build packing lists. Agent handles the full travel lifecycle: dreaming, planning, booking, traveling, and documenting.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure.

```
<state_root>/
├── memory.md              # Preferences + travel history summary
├── wishlist/              # Dream destinations
│   └── {destination}.md
├── trips/                 # Active and upcoming trips
│   └── {trip-name}/
│       ├── overview.md
│       ├── itinerary.md
│       ├── bookings.md
│       ├── packing.md
│       ├── budget.md
│       └── travelers.md     # For group/family trips
├── completed/             # Past trips with notes
├── templates/             # Reusable packing lists
└── documents/             # Passport, visa info, insurance
```

## Quick Reference

| Topic | File | Load Instruction |
|-------|------|------------------|
| Setup process | `references/setup.md` | Read on first use or setup |
| Memory template | `assets/memory-template.md` | Read when establishing user history/preferences |
| Booking timing | `references/booking-guide.md` | Read when advising on when to book |
| Packing templates | `assets/packing-templates.md` | Read when creating a packing list |
| Multi-city planning | `references/multi-city.md` | Read when the trip spans multiple destinations |

## Core Rules

### 1. Check Existing Memory First
When `<state_root>/memory.md` exists, read it before trip planning for:
- Travel style preferences (budget, pace, accommodation type)
- Past trip patterns (average daily spend, packing habits)
- Document status (passport expiry, frequent flyer numbers)
- Family/group composition if applicable

When the state root or memory file is absent, read `references/setup.md` before creating the initial trip records.

### 2. Trip Lifecycle
| Phase | Action |
|-------|--------|
| Dream | Add to `wishlist/` with why, when, budget estimate |
| Plan | Create trip folder in `trips/` when dates confirmed |
| Book | Track confirmations in trip's bookings.md, update budget |
| Travel | Reference itinerary, log actual expenses |
| Return | Move to `completed/`, document highlights and lessons |

### 3. Booking Timeline
When dates are known, build a trip-specific timeline from verified current requirements:
- Check the destination's official immigration authority for entry and passport rules before booking non-refundable travel.
- Check the relevant airline, rail, accommodation, activity, and insurance providers for availability, cancellation terms, and check-in deadlines.
- Record the applicable deadlines and source URLs in the trip folder; do not apply a generic booking window as a guarantee.
- Read `references/booking-guide.md` when comparing booking options or maintaining the booking record.

### 4. Budget Tracking & Optimization
For each trip, track in its budget.md:
```markdown
## Budget — {Trip Name}

### Per-Person Breakdown (for groups)
| Traveler | Share | Notes |
|----------|-------|-------|
| Adult 1 | $X | Organizer |
| Adult 2 | $X | |
| Child | $X | Child-rate activities, when applicable |

### Planned
| Category | Estimate | Optimization Applied |
|----------|----------|---------------------|
| Flights | $X | Shoulder season ✓ |
| Hotels | $X | Kitchen saves meals |
| Transport | $X | Off-airport rental |
| Food | $X | ~$Y/day/person |
| Activities | $X | City passes ✓ |
| **Total** | **$X** | **Saved: $Y** |

### Actual (update during/after)
| Category | Spent | vs Planned |
|----------|-------|------------|
```

### 5. Multi-City & Complex Itineraries
For trips with 2+ cities:
- Start with enough nights to cover the traveller's priorities and transfer time; validate the cadence against the itinerary.
- Group geographically close destinations
- Compare open-jaw flights (fly into A, out of B) with the round-trip alternative
- Set connection buffers from the carrier, airport, immigration, baggage, and transfer constraints for that itinerary.
- Track different currencies and exchange rates per leg

### 6. Family & Group Travel
When traveling with kids or groups:
- Create travelers.md in trip folder with each person's details (dietary, medical, seat prefs)
- Plan kid-friendly activities with energy breaks
- Compare accommodations with kitchen access against realistic meal costs for the group.
- Check child visa and consent requirements through the destination's official authority.
- Pack shared items list to avoid duplication
- Assign roles: navigator, budget tracker, activity planner

### 7. Document Safety (with user consent)
Store only the minimum document information the user explicitly asks to track:
- Passport expiry dates (for validity warnings)
- Visa requirements per destination
- Travel-insurance coverage notes
- Emergency contact details supplied for that trip
- Keep full document images, payment data, and unnecessary reference numbers out of the trip record.

## Booking Optimization

### Timing
See `references/booking-guide.md` for timing guidance.

### Cost Comparison Tactics
| Strategy | Compare | When to Use |
|----------|---------|-------------|
| Shoulder season | Dates, weather, closures, and total price | Flexible dates |
| Off-airport car rental | Transfer cost, operating hours, and total rental price | Car rental is needed |
| Kitchen accommodation | Total accommodation cost against realistic meal costs | Family trips or longer stays |
| City passes | Included attractions against the itinerary | Several covered attractions are planned |
| Open-jaw flights | Fare plus the cost and time of backtracking | Multi-city trip with different endpoints |
| Flight dates | Total fare across flexible dates | Dates are flexible |
| Flight and hotel bundle | Package total, cancellation terms, and loyalty benefits | Comparable package is available |

### Group Booking Tips
- Compare separate and shared flight bookings on price, fare conditions, connection protection, and disruption handling.
- Hotels: request adjoining rooms at booking, confirm before arrival
- Activities: ask the provider whether a group rate applies
- Car rentals: compare 2 cars with 1 large van on total price, capacity, and flexibility

## Itinerary Structure

```markdown
# Day X — {Date} — {Location}

## Morning
- [ ] {Activity} @ {Time}
  - Address: {address}
  - Kid-friendly: ✓/✗
  - Notes: {hours, tickets, tips}

## Afternoon
- [ ] {Activity}

## Evening
- [ ] Dinner @ {Restaurant}
  - Reservation: {time}
  - Confirmation: {number}
  - High chairs available: ✓/✗

## Logistics
- Transport: {how to get there}
- Accommodation: {check-in time if applicable}
- Backup plan: {if weather/energy fails}
```

Reserve a daily buffer that fits the itinerary's transfer effort and the traveller's pace. Mark must-dos vs nice-to-haves.

## Multi-City Connection Planning

```markdown
## City Connections — {Trip Name}

| From | To | Transport | Duration | Cost | Booked |
|------|-----|-----------|----------|------|--------|
| Paris | Amsterdam | Train | 3h20m | €80 | ✓ |
| Amsterdam | Berlin | Flight | 1h15m | €65 | ✓ |

### Connection Risks
- Paris→Amsterdam: Low (frequent trains, no checkin)
- Amsterdam→Berlin: Medium (need 2h+ at airport)

### Luggage Strategy
- Full luggage: check at origin, pick at final destination
- Day bags: carry essentials for city transitions
```

## Common Traps

- Over-scheduling → use the traveller's pace and transfer effort to leave discovery room
- Forgetting to document after trip → capture highlights and lessons while the experience is fresh
- Booking without checking visa requirements → confirm the destination's current rule first
- Ignoring passport validity → confirm the destination-specific entry rule first
- Not saving confirmation numbers → create bookings.md immediately
- One-night stays in cities → show the transfer and recovery trade-off before keeping the stop
- Ignoring jet lag recovery → plan light first day after long-haul
- Group booking strategy → compare shared and separate reservations against the provider's disruption terms

## Scope

This skill ONLY:
- Manages travel planning in `<state_root>/`
- Reads/writes markdown files for trips, budgets, packing
- Reminds about deadlines based on trip dates

This skill provides planning information and trip records; the user completes bookings directly.
Use booking or calendar details the user provides or explicitly authorizes for the current task.
Keep payment information out of travel-planning records.
Read and write trip state only within `<state_root>/`; skill resources are read from this package.
