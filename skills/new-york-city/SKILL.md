---
name: new-york-city
description: Navigate New York City visits, relocation, neighborhood selection, transit, housing, food, work, and daily logistics. Use when a user needs borough-specific NYC guidance, an itinerary, a move or commute decision, or local practical advice.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🗽"}'
  related-skills: '{"booking":"Handles accommodation comparisons, cancellation terms, and reservation completion after an NYC stay has been selected.","business":"Extends NYC work, startup, and business-location choices into broader business strategy.","car-rental":"Covers rental-car decisions when an airport pickup or trip beyond NYC makes a car appropriate.","health-insurance":"Provides detailed coverage comparisons when a move or job change raises insurance questions.","travel":"Provides cross-destination travel planning and standing travel records beyond NYC-specific routing."}'
---

## State location

NYC continuity state may exist in `<workspace>/new-york-city/`, `<workspace>/memory/new-york-city/`, or `~/new-york-city/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/new-york-city/`, `<workspace>/memory/new-york-city/`, `~/new-york-city/`.
3. If several candidate directories exist, use only the highest-precedence one and tell the user that separate copies were found.
4. If none exists and the user explicitly wants continuity, create `<workspace>/new-york-city/` by default. If the host cannot provide `<workspace>`, ask for a state root before creating state.

Use the selected `<state_root>` for every state operation in this invocation. Resolve existing locations before creating one; do not merge, migrate, or cross-write copies automatically.

## When to use

Use this skill for NYC-specific decisions that generic travel or relocation advice misses: selecting a borough or neighborhood, planning a visit, moving into the city, designing a commute, using transit or airports, avoiding low-value tourist routing, and choosing a practical work or study base.

Classify the user's current mode—visitor, future resident, current resident, or work/study—then anchor advice to borough, neighborhood, budget, schedule, and commute. Ask only for the next missing detail that materially changes the recommendation.

## Reference routing

| Topic | Read | When to load |
|---|---|---|
| Continuity setup and consent | `references/setup.md` | The user wants persistent NYC context or `<state_root>/` needs initialization |
| Memory structure | `references/memory-template.md` | Creating or updating `<state_root>/memory.md` after consent |
| Boroughs and bases | `references/neighborhoods-and-bases.md` | Recommending a neighborhood, hotel base, or borough |
| Moving and housing | `references/moving-and-housing.md` | Evaluating rentals, a move, buildings, or settling in |
| Transit and airports | `references/transit-and-airports.md` | Designing a commute, subway/bus/ferry route, or airport transfer |
| Food and dining | `references/food-and-dining.md` | Recommending where or how to eat |
| Safety and weather | `references/safety-and-weather.md` | Discussing street awareness, weather, or late-night routing |
| Work and study | `references/work-study-and-startups.md` | Choosing an office, campus, startup, or professional base |
| Visits and itineraries | `references/visiting-and-itineraries.md` | Designing trip days, attraction routing, or bookings |
| Official sources | `references/sources.md` | A current rule, fare, policy, or operational detail needs verification |
| Current transit facts | `references/domain-knowledge.md` | Checking congestion pricing, OMNY, or airport-transfer facts |

## Core workflow

1. **Map the repeat journey.** Identify where the user must be at peak times, their transfer and walking tolerance, luggage or accessibility needs, and late-night return path. In NYC, time, transfers, stairs, and reliability usually matter more than straight-line distance.
2. **Compare concrete tradeoffs.** Contrast routine fit rather than hype: quieter but slower, cheaper but farther, convenient but small, or exciting but exhausting. Treat Manhattan, Brooklyn, Queens, the Bronx, and Staten Island as distinct choices.
3. **Verify mutable details.** For fares, service changes, reservations, airport access, housing rules, or city workflows, read `references/sources.md` and confirm current details with the responsible official source. If verification is unavailable, provide the durable decision framework and mark the mutable fact as unverified.
4. **Persist only with consent.** For a user who wants continuity, read `references/setup.md`, resolve `<state_root>`, explain the intended scope, and then use `references/memory-template.md`. Keep `<state_root>/memory.md` focused on details that improve future NYC advice.

## Practical guardrails

- Base neighborhood recommendations on the actual commute and late-night return path, not a borough label or landmark list.
- Give current prices, fares, and hotel costs as verified figures or clearly labeled ranges; avoid false precision.
- Treat borough-level guidance as general. Verify a particular block, building, route, or venue when the user needs a decision at that level.
- Use official city, transit, airport, venue, and agency sources for unstable operational details. Send borough, ZIP, station, or airport context only when the user requests location-specific help.
- Complete bookings or submissions only after explicit user instruction. Keep credentials, payment details, passport details, and other sensitive identifiers out of `<state_root>/`.
