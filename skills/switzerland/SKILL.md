---
name: switzerland
description: Plan Switzerland trips handling Alpine rail, mountain logistics, Schengen rules, scenic routing, and practical local execution. Use when the user needs actionable operational guidance, rail vs car choices, or region selection based on seasons and altitude for a Switzerland visit.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji": "🇨🇭"}'
  related-skills: '{"booking": "Reservation workflows and confirmation hygiene", "car-rental": "Better self-drive strategy and handoff logistics", "europe": "Better wider-Europe context when Switzerland is part of a longer route", "food": "Deeper restaurant and cuisine planning", "travel": "General trip planning and itinerary structure"}'
---

## State location

Switzerland state may exist in `<workspace>/switzerland/`, `<workspace>/memory/switzerland/`, or `~/switzerland/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/switzerland/`, `<workspace>/memory/switzerland/`, `~/switzerland/`.
3. If none exists and state must be created, default to `<workspace>/switzerland/`.

Use the selected `<state_root>` for every state operation in this skill. Data stored: Trip preferences, route decisions, and deadlines.

## Setup

If `<state_root>/` does not exist or is empty, read `references/setup.md` and start naturally.

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for structure.

```text
<state_root>/
└── memory.md     # Trip context, routing logic, and evolving constraints
```

## Quick Reference

Use this map to load only the Switzerland subtopic that changes the decision in front of you.

| Topic | File |
|-------|------|
| **Entry and Compliance** | |
| Tourist entry, Schengen logic, passport checks | `references/entry-and-documents.md` |
| Customs, duty-free limits, border habits | `references/customs-and-border.md` |
| **Planning Backbone** | |
| Macro-regions and route logic | `references/regions.md` |
| Sample itineraries for 4-14 days | `references/itineraries.md` |
| Where to stay by trip style | `references/accommodation.md` |
| Budget framing and hidden costs | `references/budget-and-costs.md` |
| Cards, cash, tax-free, tipping | `references/payments-and-tax-free.md` |
| **Transport and Outdoors** | |
| Trains, boats, buses, airport links, passes | `references/transport-domestic.md` |
| Driving, vignette, passes, parking, winter roads | `references/road-trips-and-driving.md` |
| Scenic trains, lifts, lakes, hiking, panoramas | `references/alps-lakes-and-scenic-trains.md` |
| Ski, snow, festive season, winter routing | `references/winter-ski-and-snow.md` |
| **Major Regions and Bases** | |
| Zurich and easy first-trip routing | `references/zurich.md` |
| Lucerne and Central Switzerland | `references/lucerne-and-central-switzerland.md` |
| Bern city, Gruyeres, and slower culture routes | `references/bern-and-fribourg.md` |
| Interlaken, Jungfrau, Lauterbrunnen, Grindelwald | `references/bernese-oberland.md` |
| Geneva, Lausanne, Montreux, and Lavaux | `references/geneva-lausanne-and-lake-geneva.md` |
| Zermatt, Valais, Matterhorn, and high Alps | `references/valais-and-zermatt.md` |
| Graubunden, Engadin, Davos, and scenic rail | `references/graubunden-and-engadin.md` |
| Ticino and Italian-speaking lake routes | `references/ticino.md` |
| Basel, Jura, and tri-border positioning | `references/basel-and-northwest.md` |
| **Lifestyle and Execution** | |
| Food strategy and regional specialties | `references/food-guide.md` |
| Traveling with children or mixed ages | `references/family-travel.md` |
| Accessibility and low-mobility planning | `references/accessibility.md` |
| Emergencies, weather, mountain risk, disruptions | `references/safety-and-emergencies.md` |
| Climate, altitude, and seasonality logic | `references/weather-and-seasonality.md` |
| Connectivity, apps, roaming, ticketing tools | `references/telecoms-and-apps.md` |
| Official source map | `references/sources.md` |

## Core Rules

### 1. Route by Corridor, Not by Pin Count
For short trips, choose one dominant Switzerland shape: Zurich and Central Switzerland, Bernese Oberland, Lake Geneva, Valais, Graubunden, Ticino, or Basel and Jura. Scenic density is high, but hotel changes, lifts, and transfer friction still punish over-routing.

### 2. Ask for Month and Altitude Tolerance Before Naming the Best Region
The same Switzerland plan changes meaning in February, June, September, and December. Snow line, lake appeal, hiking access, daylight, and school-holiday demand can make a famous route smart or wasteful.

### 3. Default to Rail, Add a Car Only When It Clearly Improves Execution
Classic visitor routes are usually better by train and boat. Car value appears when the trip is built around rural lakes, remote valleys, low-frequency villages, or border-heavy driving loops.

### 4. Treat Mountains as Logistics, Not Background
Use `references/alps-lakes-and-scenic-trains.md`, `references/winter-ski-and-snow.md`, and `references/weather-and-seasonality.md` before promising panoramic days. Cloud, wind, snow, avalanche controls, and pass closures can change the whole plan.

### 5. Budget With Real Swiss Friction
Price using comprehensive costs instead of hotel headlines alone. Include CHF reality, resort taxes, lift tickets, seat reservations where relevant, parking, tunnel or pass detours, luggage handling, and mountain food premiums.

### 6. Protect the User From Border and Sunday Mistakes
Switzerland sits inside Schengen but outside the EU customs and roaming default that many travelers assume. Border shopping, tax-free steps, Sunday closures, and cross-border train or car choices need explicit handling.

### 7. Deliver Operational Plans
Output should include:
- Best base or base pair
- Day-by-day flow with realistic transfer windows
- Booking deadlines or low-availability warnings
- Weather downgrade options
- Safety, payment, and emergency notes

## Best Practices for Routing

- Ensure reasonable pacing, as Switzerland has high transfer friction.
- Focus on one or two dominant regions for short trips to avoid excessive transit.
- Verify if SBB (trains/buses/boats) solves the route better before booking a car.
- Verify current weather and season conditions, as mountain visibility varies heavily.
- Schedule scenic trains as full-day experiences rather than quick transfers.
- Account for severe peak summer and ski-season hotel pricing in famous alpine bases.
- Apply specific Swiss rules for roaming, customs, and CHF pricing instead of EU defaults.

## Security & Privacy

**Data that stays local:** Trip preferences, route decisions, and deadlines in `<state_root>/`

**This skill does NOT:** Access files outside `<state_root>/` or make network requests.

**Memory rule:** Keep local trip notes only when the user is doing ongoing Switzerland planning or clearly wants continuity across sessions. For one-off answers, help without creating extra trip memory.
