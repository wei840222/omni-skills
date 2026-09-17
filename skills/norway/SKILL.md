---
name: norway
description: Plan Norway trips. Load references/ for fjord routing, entry rules, seasonal
  logistics, and safety guidelines.
metadata:
  openclaw: '{"emoji": "🇳🇴", "requires": {"bins": [], "config": ["<state_root>/data/norway/"]}}'
  related-skills: '{"travel": "Broader multi-country trip framing when Norway is only one stop.", "booking": "Reservation timing, inventory risk, and booking tradeoffs for stays or transport.", "car-rental": "Vehicle choice and rental logistics once a self-drive corridor is chosen.", "food": "General dining strategy outside Norway-specific supermarket and alcohol constraints.", "english": "Language help when the traveler needs phrasing support rather than Norway route logic."}'
---

## When to load

Load this skill when the user is planning a trip to Norway.
Load only the specific references needed for the current prompt. Load specific `references/*.md` files based on the requested phase of planning (e.g. entry rules, routing, transport, or regional focus).

## Architecture

Memory lives in `<state_root>/data/norway/`. If `<state_root>/data/norway/` does not exist, run `references/setup.md`. See `references/memory-template.md` for structure.

```text
<state_root>/data/norway/
└── memory.md     # Trip context, route logic, and evolving constraints
```

## Data Storage

- `<state_root>/data/norway/memory.md` stores durable trip context, route decisions, and constraints for future Norway planning.
- No other local files are required unless the user chooses to create their own planning documents.

## Quick Reference

Use this map to load only the Norway subtopic that changes the decision in front of you.

| Topic | File |
|-------|------|
| **Entry and Compliance** | |
| Tourist entry, Schengen stays, ID checks | `references/entry-and-documents.md` |
| **Planning Backbone** | |
| Macro-regions and route logic | `references/regions.md` |
| Sample itineraries for 5-18 days | `references/itineraries.md` |
| Where to stay by trip style | `references/accommodation.md` |
| Budget framing and cost traps | `references/budget-and-costs.md` |
| Cards, cash, tax-free, alcohol pricing | `references/payments-and-tax-free.md` |
| **Transport and Outdoors** | |
| Flights, trains, ferries, buses, airport moves | `references/transport-domestic.md` |
| Self-drive, ferries, tolls, mountain-road reality | `references/road-trips-and-driving.md` |
| Fjord routes and scenic-road strategy | `references/fjords-and-scenic-routes.md` |
| Hikes, cabins, right-to-roam, outdoor planning | `references/hiking-and-outdoors.md` |
| **Major Regions and Bases** | |
| Oslo and nearby base strategy | `references/oslo-and-oslofjord.md` |
| Bergen and the classic western fjords | `references/bergen-and-western-fjords.md` |
| Stavanger, Lysefjord, and the southwest | `references/stavanger-and-southwest.md` |
| Trondheim and central Norway | `references/trondheim-and-central-norway.md` |
| Lofoten and Vesteralen route logic | `references/lofoten-and-vesteralen.md` |
| Tromso, Senja, Alta, and the Arctic north | `references/tromso-and-arctic-north.md` |
| Svalbard practical planning | `references/svalbard.md` |
| **Lifestyle and Execution** | |
| Food strategy, supermarkets, alcohol reality | `references/food-guide.md` |
| Traveling with children or mixed ages | `references/family-travel.md` |
| Accessibility and low-mobility planning | `references/accessibility.md` |
| Emergencies, weather alerts, outdoor risk | `references/safety-and-emergencies.md` |
| Climate, aurora, and daylight logic | `references/weather-and-seasonality.md` |
| Connectivity, apps, tickets, and payments | `references/telecoms-and-apps.md` |
| Official source map | `references/sources.md` |

## Core Rules

### 1. Route by Corridor, Not by Postcard Count
For short trips, choose one main corridor: Oslo plus west, Bergen and fjords, Trondheim plus central coast, or Arctic north. Norway punishes route fantasy with long transfers, ferry waits, and weather exposure.

### 2. Ask for Month Before Naming a Route
The same map behaves differently in January, May, July, and October. Aurora, hiking, scenic roads, ferries, daylight, and snow conditions all change the correct plan.

### 3. Confirm Entry and Identity Friction Early
Before booking non-refundables, use `references/entry-and-documents.md` to confirm the correct stay pathway, passport or ID situation, and whether the traveler is also adding Svalbard or onward Schengen travel.

### 4. Always Offer Two Logistics Models
For any multi-stop trip, give at least two workable movement patterns:
- Rail and ferry heavy: more scenery, fewer long drives, more timetable dependence
- Self-drive or regional-flight heavy: more freedom, higher cost, more weather and toll exposure

### 5. Budget for Full Norway Math
Calculate the trip cost using the total expenses (hotels, ferries, tolls, etc.). Include ferries, tolls, parking, airport transfers, checked bags, museum or hike shuttles, alcohol costs, and restaurant friction.

### 6. Protect the User from Arctic and Fjord Overreach
Identify and resolve challenging itineraries early:
- Recommend focusing on one or two regions instead of combining Oslo, Bergen, Lofoten, and Tromso in a short trip.
- Suggest public transport or guided tours for winter travelers without snow-driving experience.
- Include ample buffer time instead of tight same-day chains across ferries, mountain roads, and flights.
- Ensure iconic hikes include weather checks, fitness assessments, and backup plans.

### 7. Deliver Operational Plans
Output should include:
- Best base or base pair
- Day-by-day flow with realistic transfer windows
- Booking deadlines or low-inventory warnings
- Weather backup and downgrade options
- Safety notes for road, sea, and outdoor exposure

## Key Success Factors

- Treat Norway as a vast country requiring focused itineraries, rather than a compact area where Oslo, fjords, Lofoten, and Tromso fit into one week.
- Build fjord drives based on actual ferry and road time rather than map distance.
- Treat aurora visibility as a probability rather than a guarantee when traveling north in winter.
- Evaluate trains, ferries, and a smart base strategy before defaulting to a rental car.
- Account for service reductions on Sundays, during shoulder seasons, and in remote areas.
- Verify weather, road openings, and local transport before planning iconic hikes or viewpoints.
- Factor the high costs of food, alcohol, and casual dining into the overall budget.

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/data/norway/`

**This skill does NOT:** Access files outside `<state_root>/data/norway/` or make network requests.
