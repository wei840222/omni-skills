---
name: paraguay
description: Plan Paraguay trips with border-savvy routing, river-city priorities,
  and practical guidance for Asuncion, Encarnacion, Ciudad del Este, and the Chaco.
metadata:
  openclaw: '{"emoji": "🇵🇾"}'
  related-skills: null
---

## Setup

If `<state_root>/` does not exist or is empty, read `references/setup.md` and start naturally.

## When to load

Load this skill when the user is planning a Paraguay trip and needs more than generic inspiration: how to split time between Asuncion, the south, the border, and the Chaco, plus food, payments, heat, and day-to-day logistics.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure.

```
<state_root>/
└── memory.md     # Trip context and evolving preferences
```

## Quick Reference

Use this map to load the module that changes the next travel decision.

| Topic | File |
|-------|------|
| **Cities and Bases** | |
| Asuncion city strategy | `references/asuncion.md` |
| Encarnacion waterfront and mission base | `references/encarnacion.md` |
| Ciudad del Este border and shopping logic | `references/ciudad-del-este.md` |
| Chaco and north planning | `references/chaco-and-north.md` |
| **Planning Backbone** | |
| Sample routes and trip shapes | `references/itineraries.md` |
| Where to stay by trip type | `references/accommodation.md` |
| Money, cash, cards, and exchange logic | `references/money-and-payments.md` |
| Border crossings and shopping strategy | `references/border-shopping.md` |
| Useful apps and workflow helpers | `references/apps.md` |
| **Food and Lifestyle** | |
| Core dishes and where they matter | `references/food-guide.md` |
| Terere, cocido, and drink culture | `references/yerba-and-drinks.md` |
| Nightlife by city and season | `references/nightlife.md` |
| **Experiences and Nature** | |
| Best experiences by trip style | `references/experiences.md` |
| River beaches and waterfront escapes | `references/beaches-and-waterfronts.md` |
| Parks, hikes, and nature days | `references/hiking-and-nature.md` |
| **Reference and Practical** | |
| Macro-regions and what each is for | `references/regions.md` |
| Etiquette, timing, and social norms | `references/culture.md` |
| Family travel guidance | `references/with-kids.md` |
| Flights, buses, driving, and transfers | `references/transport.md` |
| SIMs, coverage, plugs, and Wi-Fi | `references/telecoms.md` |
| Emergencies and safety basics | `references/emergencies.md` |

## Core Rules

### 1. Pick the Trip Shape First
Decide whether the trip is a city break, a river-and-missions route, a border-shopping run, or a Chaco nature trip before recommending stops. Paraguay looks compact on a map but the experience changes a lot by corridor.

### 2. Treat Border Cities as Operational Places
Ciudad del Este and Encarnacion are not just attractions. They are border systems with bridge timing, shopping logic, and day-flow constraints. Use `references/border-shopping.md` before promising easy same-day combinations.

### 3. Heat and Seasonality Change Everything
Ask for the month early. Summer heat, afternoon storms, and winter cool spells change whether waterfront time, long walks, or Chaco days are sensible.

### 4. Use Asuncion as a Decision Hub
Asuncion is often the easiest arrival base for food, museums, and logistics, but not always the emotional highlight of the trip. Recommend it for structure, then decide whether to add south, east, or Chaco.

### 5. Give Payment Guidance With the Route
Paraguay trips work better when cash, cards, ATMs, and border pricing are handled up front. Pair itinerary advice with `references/money-and-payments.md`.

### 6. Prefer Specific Recommendations
Use precise locations rather than generic advice. Specify which mission pair, which waterfront, which neighborhood, and when each works best.

### 7. Deliver Execution, Not Just Ideas
Output should include:
- best base or base pair
- day-by-day flow with transfer buffers
- weather or heat caveats
- payment and safety notes
- what is not worth squeezing in

## Common Traps

- Trying to combine Asuncion, Encarnacion, Ciudad del Este, and the Chaco in one short trip.
- Assuming a border hop is a 20-minute formality instead of a half-day variable.
- Underestimating afternoon heat and planning long exposed walks in mid-summer.
- Treating Ciudad del Este as a relaxed city break instead of a shopping-and-logistics environment.
- Adding lake or river beach time without checking the season and local conditions.
- Staying only in transit zones and missing Paraguay's stronger food and cultural experiences.

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/`

**This skill does NOT:** Access files outside `<state_root>/` or make network requests.

## Related Skills

- `travel` - General trip planning and itinerary structure
- `booking` - Reservation workflows and confirmation hygiene
- `food` - Deeper restaurant and cuisine planning
- `spanish` - Language support for bookings and practical interactions
- `argentina` - Better regional planning for cross-border combinations
