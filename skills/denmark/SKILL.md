---
name: denmark
description: Plan Denmark trips with concise route logic, verify entry rules, and
  access practical local execution guides.
metadata:
  openclaw: '{"emoji": "🇩🇰", "requires": {"bins": [], "config": ["<state_root>/denmark/"]}}'
---
## When to load

User is planning a Denmark trip and needs operational guidance beyond generic city lists: Schengen entry checks, Copenhagen vs Jutland vs island routing, rail and ferry choices, weather-fit timing, budget reality, and on-the-ground execution.

## Architecture

Memory lives in `<state_root>/denmark/`. If `<state_root>/denmark/` does not exist, run `scripts/setup.md`. See `assets/memory-template.md` for structure.

```text
<state_root>/denmark/
└── memory.md     # Trip context, route logic, and evolving constraints
```

## Data Storage

- `<state_root>/denmark/memory.md` stores durable trip context, route decisions, and constraints for future Denmark planning.
- No other local files are required unless the user chooses to create their own planning documents.

## Quick Reference

Use this map to load only the Denmark subtopic that changes the decision in front of you.

| Topic | File |
|-------|------|
| **Entry and Compliance** | |
| Tourist entry, Schengen stays, passport checks | `references/entry-and-documents.md` |
| Customs, cash declarations, restricted goods | `references/customs-and-border.md` |
| **Planning Backbone** | |
| Macro-regions and route logic | `references/regions.md` |
| Sample itineraries for 3-14 days | `references/itineraries.md` |
| Where to stay by trip style | `references/accommodation.md` |
| Budget framing and hidden costs | `references/budget-and-costs.md` |
| Cards, cash, tax-free, and payment habits | `references/payments-and-tax-free.md` |
| **Transport and Outdoors** | |
| Trains, buses, ferries, metro, and airport moves | `references/transport-domestic.md` |
| Driving, bridge tolls, parking, and EV logic | `references/road-trips-and-driving.md` |
| Bike-first, coast, and island travel logic | `references/cycling-coasts-and-islands.md` |
| **Major Regions and Bases** | |
| Copenhagen and capital-region base strategy | `references/copenhagen.md` |
| North Zealand, Roskilde, and Mons Klint logic | `references/north-zealand-and-south-zealand.md` |
| Funen, Odense, and archipelago pacing | `references/funen-and-odense.md` |
| Aarhus, Djursland, and east Jutland | `references/aarhus-and-east-jutland.md` |
| Aalborg, Skagen, Thy, and north Jutland | `references/north-jutland-and-skagen.md` |
| Ribe, Romo, and the Wadden Sea coast | `references/southwest-jutland-and-wadden-sea.md` |
| Bornholm planning and access strategy | `references/bornholm.md` |
| **Lifestyle and Execution** | |
| Food strategy, bakeries, and dining rhythm | `references/food-guide.md` |
| Traveling with children or mixed ages | `references/family-travel.md` |
| Accessibility and low-mobility planning | `references/accessibility.md` |
| Emergencies, warnings, coast, and weather risk | `references/safety-and-emergencies.md` |
| Climate, daylight, and seasonality logic | `references/weather-and-seasonality.md` |
| Connectivity, ticketing apps, and digital tools | `references/telecoms-and-apps.md` |
| Official source map | `references/sources.md` |

## Core Rules

### 1. Route by Corridor, Not by Municipality Count
For short trips, choose one dominant shape: Copenhagen and capital region, Funen plus east Jutland, north Jutland coast, southwest Jutland, or Bornholm. Denmark is compact, but bridges, ferries, wind, and hotel changes still punish over-routing.

### 2. Ask for Month Before Naming the Best Region
The same Denmark trip changes meaning in February, May, July, and November. Daylight, coast time, cycling comfort, ferry value, event density, and island logistics all depend on season.

### 3. Confirm Entry and Schengen Friction Early
Before non-refundable bookings, use `references/entry-and-documents.md` to confirm passport validity, Schengen day-count logic, visa or visa-free status, and whether the trip also touches Sweden, Germany, or wider Schengen routing.

### 4. Always Offer Two Movement Models
For any multi-destination trip, give at least two workable movement patterns:
- Rail and city-transit heavy: easier in Copenhagen, Odense, Aarhus, and simple intercity routes
- Car, ferry, or bike-assisted: better for coasts, west Jutland, Mons Klint, Thy, and flexible island travel

### 5. Budget With Full Denmark Math
Price using full trip math. Include bridge tolls, parking, ferry bookings, airport transfers, museum passes, car-seat or bike-rental costs, and restaurant reality in high-demand areas.

### 6. Protect the User from Island and Coast Fantasy
Flag bad combos early:
- Copenhagen, Aarhus, Skagen, Wadden Sea, and Bornholm in one short trip
- Summer-island plans with no ferry or lodging buffer
- Winter beach or bike-heavy routes when acknowledging daylight and wind impacts
- Car rental for city-only stays where parking and stress destroy value

### 7. Deliver Operational Plans
Output should include:
- Best base or base pair
- Day-by-day flow with realistic transfer windows
- Booking deadlines or low-inventory warnings
- Weather downgrade and indoor backup options
- Safety, payment, and emergency notes

## Common Traps

- Treating Denmark like a checkbox add-on instead of a route with real regional character.
- Building a "whole country" trip when the user only has 4-7 days.
- Assuming every island move is spontaneous in peak summer.
- Renting a car before checking whether rail plus one day rental solves the trip better.
- Underestimating wind, cool water, and shoulder-season daylight on coast-heavy trips.
- Forgetting that many small-town restaurants, attractions, and shops have tighter hours outside peak season.
- Planning by map distance instead of bridge, ferry, parking, and check-in friction.

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/denmark/`

**This skill does NOT:** Access files outside `<state_root>/denmark/` or make network requests.

## Related Skills
Related skills:
- `skills/travel` — General trip planning and itinerary structure
- `skills/europe` — Better wider-Europe context when Denmark is part of a longer route
- `skills/booking` — Reservation workflows and confirmation hygiene
- `skills/food` — Deeper restaurant and cuisine planning
- `skills/english` — Language support for bookings, transport, and service interactions
