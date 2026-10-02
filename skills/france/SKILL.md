---
name: france
description: Plan and organize travel across France. Use when the user wants to coordinate French city itineraries, manage train routes, or find local dining and cultural experiences.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji": "🇫🇷"}'
  related-skills: '{"travel": "General trip planning and itinerary structuring", "food": "Deeper restaurant and cuisine recommendations", "french": "Language support for local communication and bookings", "english": "Backup communication support for multilingual travel"}'
---
## State location

France travel state may exist in `<workspace>/france/`, `<workspace>/memory/france/`, or `~/france/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/france/`, `<workspace>/memory/france/`, `~/france/`.
3. If none exists and state must be created, default to `<workspace>/france/`.

Use the selected `<state_root>` for every state operation in this skill.



## Using References

Load `references/` files on demand based on the user's specific region or topic interest (for example `references/paris.md` for Paris questions). Keep `SKILL.md` as the router; do not load every city guide up front.

- Live fares, strike notices, museum hours, and ticket inventory drift — confirm via `references/sources.md` and operator apps in `references/apps.md` before the user pays.
- Do not treat the literal string `<state_root>` as a filesystem path.

## When to Use

User planning a trip to France or asking for local insights: what to prioritize, where to base, what to skip, and how to handle transport, timing, and budgeting.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure.

```
<state_root>/
└── memory.md     # Trip context
```

## Quick Reference

| Topic | File |
|-------|------|
| **Cities and Regions** | |
| Paris complete guide | `references/paris.md` |
| Lyon complete guide | `references/lyon.md` |
| Marseille and Provence complete guide | `references/marseille-provence.md` |
| French Riviera complete guide | `references/french-riviera.md` |
| **Planning** | |
| Sample itineraries | `references/itineraries.md` |
| Where to stay by style | `references/accommodation.md` |
| Useful apps | `references/apps.md` |
| **Food and Drink** | |
| Regional dishes and restaurant strategy | `references/food-guide.md` |
| Wine regions and tastings | `references/wine.md` |
| **Experiences** | |
| Signature experiences | `references/experiences.md` |
| Beaches and coastal strategy | `references/beaches.md` |
| Hikes and mountain safety | `references/hiking.md` |
| Nightlife by city and coast | `references/nightlife.md` |
| **Reference** | |
| Regions and route differences | `references/regions.md` |
| Culture, etiquette, expectations | `references/culture.md` |
| Traveling with children | `references/with-kids.md` |
| **Practical** | |
| Intercity transport and transfers | `references/transport.md` |
| Phone and internet | `references/telecoms.md` |
| Emergencies and safety | `references/emergencies.md` |
| Official sources (Gate 6) | `references/sources.md` |

## Core Rules

### 1. Specific Over Generic
Provide specific advice like "start museums early, shift to neighborhood lunch away from the biggest landmarks, then move to evening river-side or local bistro zones with a reservation."

### 2. Local Perspective
What locals and repeat travelers actually do, not brochure advice:
- Hyper-tourist blocks near landmark clusters often have weaker value for food
- One-night city hopping looks efficient on paper but burns time in station transfers
- Southern summer heat changes pacing for outdoor sightseeing and day trips
- Sundays and Mondays can change restaurant and shop availability by area

### 3. Regional Differences

| Region | Key difference |
|--------|----------------|
| Paris and Ile-de-France | Museum density, strongest rail access, reservation pressure |
| Lyon and Rhone corridor | Food-first city rhythm and easier urban pace |
| Provence and Marseille | Market culture, coast plus inland villages, heat-aware planning |
| French Riviera | Scenic coast with high seasonal pricing and congestion |
| Bordeaux and Atlantic | Wine routes, ocean towns, strong shoulder-season value |
| Alps and east routes | Mountain logistics, weather variability, activity-first trips |

### 4. Timing is Everything
- Shoulder months often deliver best value and crowd balance
- Peak summer requires earlier booking in coast and famous small towns
- Winter city breaks are great for museums and food with shorter daylight
- Rail strikes or disruptions can reshape route timing quickly
- Meal windows and reservation timing are major quality levers in France

### 5. Flag Tourist Traps
Direct users away from common pitfalls by explicitly stating alternatives:
- Eating every meal in landmark-adjacent restaurant rows
- Attempting Paris, Provence, and Riviera in a short trip with no transfer buffer
- Booking no-reservation weekends in high-demand dining zones
- Treating all Cote d'Azur beach towns as same-cost and same-crowd patterns

### 6. Match Trip Style

| Traveler | Focus on |
|----------|----------|
| Foodie | `references/food-guide.md`, `references/lyon.md`, `references/paris.md` |
| Culture and museums | `references/paris.md`, `references/regions.md`, `references/culture.md` |
| Coast and scenery | `references/french-riviera.md`, `references/beaches.md`, `references/experiences.md` |
| Family | `references/with-kids.md`, `references/accommodation.md`, `references/itineraries.md` |
| Nightlife | `references/nightlife.md`, `references/paris.md`, `references/marseille-provence.md` |
| Mixed route trip | `references/itineraries.md`, `references/transport.md`, `references/regions.md` |

## Important Considerations

- Budget transfer time: France is not one compact destination; same-day multi-region hops often fail.
- Prefer fewer bases on short trips instead of nightly city hopping.
- Reserve high-demand restaurants and timed museum entries early, especially weekends.
- Keep summer outdoor blocks shorter with heat and crowd buffers.
- Default to rail for major city pairs; use cars for village, wine, or mountain loops.
- Re-check local Sunday/Monday opening patterns per town rather than assuming a national rhythm.
- Confirm live rail disruptions, fares, and hours on official sources before locking the plan.
