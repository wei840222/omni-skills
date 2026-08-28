---
name: greece
description: Plan Greece trips with island-mainland routing, ferry logistics, verified entry rules, and practical seasonal safety.
metadata:
  related-skills: '{"travel": "General trip planning and itinerary structure", "booking": "Reservation workflow and confirmation hygiene", "car-rental": "Better island and mainland rental strategy", "food": "Deeper restaurant and cuisine planning", "greek": "Language support for bookings, menus, and local interactions"}'
  openclaw: '{"emoji":"🇬🇷"}'
---

## State location
State follows a workspace-first convention. Use `<state_root>/` for configuration and active execution state.

## Setup

If `<state_root>/` does not exist or is empty, read `references/setup.md` and start naturally.

## When to Use

User is planning a Greece trip and needs practical guidance beyond generic island lists: Schengen entry checks, island vs mainland choices, ferry and driving tradeoffs, seasonality, costs, and on-the-ground execution.

## Architecture

Memory lives in `<state_root>/`. See `references/setup.md` for first activation flow and `references/memory-template.md` for the file structure.

```text
<state_root>/
└── memory.md     # Trip context and evolving constraints
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| **Entry and Compliance** | | |
| Schengen, passport, border, ferry docs | `references/entry-and-documents.md` | Load when advising on visas, border crossings, or required entry documents |
| **Planning Backbone** | | |
| Regions and route selection | `references/regions.md` | Load when first selecting which regions of Greece to visit |
| Sample itineraries | `references/itineraries.md` | Load when structuring a multi-day trip |
| Where to stay by trip style | `references/accommodation.md` | Load when recommending hotels or areas to stay |
| Budget planning | `references/budget-and-costs.md` | Load when discussing pricing, costs, or trip budgeting |
| Cards, cash, and tips | `references/payments-and-tipping.md` | Load when advising on tipping customs or payment methods |
| **Transport** | | |
| Flights, KTEL, rail, Athens transport | `references/transport-domestic.md` | Load when planning mainland or domestic flight travel |
| Ferry strategy and island hopping | `references/island-hopping-and-ferries.md` | Load when connecting islands or discussing ferry schedules |
| Driving and car rental strategy | `references/road-trips-and-driving.md` | Load when planning car rentals or mainland driving |
| **History and Place Logic** | | |
| Archaeological sites and museum planning | `references/archaeology-and-museums.md` | Load when focusing on historical sites or museum visits |
| Athens and Attica playbook | `references/athens-and-attica.md` | Load when planning time in the Athens region |
| Cyclades playbook | `references/cyclades.md` | Load when visiting Santorini, Mykonos, Naxos, Paros, etc. |
| Crete playbook | `references/crete.md` | Load when planning a trip to Crete |
| Ionian Islands playbook | `references/ionian-islands.md` | Load when visiting Corfu, Zakynthos, Kefalonia, etc. |
| Peloponnese and mainland south playbook | `references/peloponnese-and-mainland.md` | Load when exploring southern mainland Greece |
| Northern Greece and Meteora playbook | `references/northern-greece-and-meteora.md` | Load when visiting Thessaloniki or Meteora |
| **Lifestyle and Execution** | | |
| Food by region and meal style | `references/food-guide.md` | Load when giving dining recommendations or regional specialties |
| Nightlife strategy by destination type | `references/nightlife.md` | Load when the user asks about nightlife or evening activities |
| Traveling with children | `references/family-travel.md` | Load when planning a family trip with kids |
| Accessibility strategy | `references/accessibility.md` | Load when travelers have mobility constraints |
| **Safety and Conditions** | | |
| Emergencies, fire, heat, sea conditions | `references/safety-and-emergencies.md` | Load when discussing safety, wildfires, or emergency preparedness |
| Seasonality and weather planning | `references/weather-and-seasonality.md` | Load when selecting travel dates or packing for specific seasons |
| **Tools** | | |
| Connectivity and practical apps | `references/telecoms-and-apps.md` | Load when setting up mobile data or downloading travel apps |
| Official source map | `references/sources.md` | Load when verifying official links or external resources |

## Core Rules

### 1. Route by Cluster, Not by Postcard Count
Keep one macro-cluster per week: Athens plus nearby mainland, one island group, or one larger island plus one city base. Ferry time and wind risk destroy overpacked plans.

### 2. Confirm Entry and Border Friction Before Booking
Use `references/entry-and-documents.md` first: Schengen stay limits, passport validity, visa pathway when relevant, and whether the traveler may face extra border processing during current EU rollout changes.

### 3. Match Transport to Geography
Always offer at least two movement models:
- Island-first with ferries and short hops
- Mainland or big-island route with car or bus logic

### 4. Make Every Plan Season-Aware
Use `references/weather-and-seasonality.md` before promising beaches, ferries, hikes, or archaeology-heavy daytime plans. Meltemi wind, heat, wildfire risk, and winter service reductions are trip-shaping factors.

### 5. Reserve High-Friction Items Early
Lock the hard pieces first:
- Key ferries on popular dates
- Acropolis or headline archaeological slots when timing matters
- Car rental for islands or remote mainland routes
- Premium sunset or beach-club zones in peak season

### 6. Budget for Full Greece Math
Price the real trip, not the hotel headline:
- Ferry seat vs cabin vs car cost
- Port transfers and taxi exposure
- Beach setup fees in some areas
- City tax, parking, and snack-day spend on islands

### 7. Always Build a Wind or Heat Backup
Every output should include:
- Primary route
- Buffer plan if ferries are disrupted
- Midday heat adaptation for summer
- Last-night-in-departure-city protection before flight home

## Strategic Guidelines

- Treat Santorini, Mykonos, Naxos, Crete, and Athens as distinct regions requiring dedicated time rather than a short seamless loop.
- Book island hops with wind and port-transfer buffers.
- Verify rail coverage, as it primarily serves a few mainland corridors.
- Stay multiple nights per stop to minimize packing and check-in friction.
- Plan archaeology-heavy days in July or August with a clear shade and hydration strategy (e.g., early morning or late afternoon).
- Choose a compact walkable base over a car rental when appropriate.

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/`

**This skill does NOT:** Access files outside `<state_root>/` or make network requests.
