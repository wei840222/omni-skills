---
name: germany
description: "Plan Germany trips with region-specific routing, rail-vs-car strategy, verified entry rules, and practical travel logistics. Note: For complex multi-city trips, read references in sequence, focusing on core planning before execution details."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇩🇪","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"travel": "General trip planning and itinerary structure", "booking": "Reservation workflows and confirmation hygiene", "car-rental": "Better rental strategy and handoff logistics", "food": "Deeper restaurant and cuisine recommendations", "german": "Language support for bookings, transport, and service interactions"}'
---

## State location
Stateful skill. Files are managed in `<state_root>/` following workspace-first convention.

## Setup

If `<state_root>/` is missing or empty, read `references/setup.md` and start naturally.

## When to Use

User is planning a Germany trip and needs practical guidance beyond generic inspiration: Schengen entry checks, rail versus car decisions, region choice, seasonal tradeoffs, budgeting, and on-the-ground execution.

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for structure.

```
<state_root>/
└── memory.md     # Trip context and evolving constraints
```

## Quick Reference

Use this map to jump into the right decision module before building the route.

| Topic | File | When to load |
|-------|------|--------------|
| **Core Guidance and Rules** | | |
| Essential rules for planning | `references/core-rules.md` | Always load first |
| Common planning mistakes to avoid | `references/common-traps.md` | During review of plans |
| Recent facts and domain updates | `references/domain-knowledge.md` | Before making final recommendations |
| **Entry, Border, and Core Planning** | | |
| Schengen, passport, visas, current border systems | `references/entry-and-documents.md` | Start of planning |
| Customs, allowances, restricted items, cash rules | `references/customs-and-border.md` | Pre-departure |
| Region selection and route architecture | `references/regions.md` | Before setting itinerary |
| Sample itineraries for 5-21 days | `references/itineraries.md` | After region selection |
| Accommodation strategy by trip style | `references/accommodation.md` | While booking hotels |
| Budget framing and cost traps | `references/budget-and-costs.md` | Before finalizing budget |
| Cards, cash, tips, and payment friction | `references/payments-and-tipping.md` | General advice |
| **Transport and Movement** | | |
| ICE, regional rail, airports, local transit | `references/transport-domestic.md` | When discussing transit |
| Scenic driving, rental cars, low-emission zones | `references/road-trips-and-driving.md` | If driving is preferred |
| **Major Regions and Cities** | | |
| Berlin playbook | `references/berlin.md` | If visiting Berlin |
| Munich and Upper Bavaria playbook | `references/munich-and-upper-bavaria.md` | If visiting Munich/Bavaria |
| Franconia and Romantic Road playbook | `references/franconia-and-romantic-road.md` | If visiting Franconia |
| Rhine, Moselle, Cologne, and west playbook | `references/rhine-moselle-and-west.md` | If visiting the West |
| Hamburg and the north playbook | `references/hamburg-and-north.md` | If visiting the North |
| Black Forest and southwest playbook | `references/black-forest-and-southwest.md` | If visiting Southwest |
| Saxony and east playbook | `references/saxony-and-east.md` | If visiting East Germany |
| **Lifestyle and Execution** | | |
| Food strategy by region and timing | `references/food-guide.md` | When discussing food |
| Beer halls, wine regions, and drinking context | `references/beer-and-wine-regions.md` | For drink highlights |
| Nightlife by city type | `references/nightlife.md` | For nightlife planning |
| Culture, etiquette, Sundays, and quiet hours | `references/culture-and-etiquette.md` | General advice |
| Traveling with children or mixed ages | `references/family-travel.md` | For family trips |
| Accessibility and low-mobility planning | `references/accessibility.md` | For mobility issues |
| Christmas markets and major festival logic | `references/christmas-markets-and-festivals.md` | For winter/festival trips |
| **Conditions and Tools** | | |
| Emergencies, protests, weather alerts, disruptions | `references/safety-and-emergencies.md` | Emergency prep |
| Climate and seasonality planning | `references/weather-and-seasonality.md` | Before fixing dates |
| Connectivity, rail apps, transport cards, useful tools | `references/telecoms-and-apps.md` | Pre-departure prep |
| Research source map | `references/sources.md` | For additional sources |

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/`

**This skill does NOT:** Access files outside `<state_root>/` or make network requests.
