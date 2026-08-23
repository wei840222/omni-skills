---
name: sweden
description: Plan Sweden travel routes, budgets, and seasonal itineraries while verifying Schengen entry and transport viability.
metadata:
  openclaw: '{"emoji":"🇸🇪"}'
  related-skills: '{"travel":"General trip planning and itinerary structure","europe":"Broader Schengen and multi-country Europe planning","booking":"Reservation workflows and total-cost booking hygiene","food":"Deeper restaurant and cuisine planning","english":"Language support for bookings and practical interactions"}'
---

## State location

- **Working Directory:** `<state_root>/`
- **Location precedence:**
  1. `<workspace>/sweden/`
  2. `<workspace>/data/sweden/`
- **Behavior:** If neither path exists, use standard file tools to create `<workspace>/sweden/` as `<state_root>/`. All memory updates and artifacts must be confined to this local state directory.

## Setup

If `<state_root>/` is absent, read `references/setup.md`; answer the immediate request before creating local state.

## When to Use

User is planning a Sweden trip and needs operational guidance beyond generic Nordic advice: Schengen entry checks, Stockholm versus west coast versus Lapland routing, rail-flight-car tradeoffs, season fit, budget reality, and on-the-ground execution.

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for structure.

```text
<state_root>/
└── memory.md     # Trip context, constraints, booking status, and route decisions
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| **Entry and Compliance** | | |
| Tourist entry, Schengen limits, EES, ETIAS, IDs | `references/entry-and-documents.md` | User asks about visa rules or entry requirements. |
| Customs, alcohol, cash, restricted goods | `references/customs-and-border.md` | User asks what they can bring into Sweden. |
| Domain knowledge context | `references/domain_knowledge.md` | For general background on Schengen policies. |
| **Planning Backbone** | | |
| Macro-regions and route logic | `references/regions.md` | Structuring a multi-region trip. |
| Sample itineraries for 5-14 days | `references/itineraries.md` | Creating daily travel plans. |
| Where to stay by trip style | `references/accommodation.md` | Deciding on lodging or base locations. |
| Daily budget framing and hidden costs | `references/budget-and-costs.md` | User is estimating trip costs. |
| Cards, cash, tax-free, alcohol buying reality | `references/payments-and-alcohol.md` | User is asking about transactions and local payment norms. |
| **Transport and Outdoors** | | |
| Trains, flights, ferries, airport moves, local transit | `references/transport-domestic.md` | Planning transit between cities or airports. |
| Self-drive, winter roads, ferries, parking | `references/road-trips-and-driving.md` | User is renting a car or planning a road trip. |
| National parks, hiking, and right-to-roam logic | `references/nature-and-right-to-roam.md` | User is planning outdoor activities. |
| **Major Regions and Bases** | | |
| Stockholm city playbook | `references/stockholm.md` | Planning activities within Stockholm. |
| Stockholm archipelago strategy | `references/stockholm-archipelago.md` | Planning trips to the islands near Stockholm. |
| Gothenburg and the west coast | `references/gothenburg-and-west-coast.md` | Visiting the western side of Sweden. |
| Malmo, Lund, and Skane routing | `references/malmo-and-skane.md` | Visiting southern Sweden. |
| Swedish Lapland and the far north | `references/swedish-lapland.md` | Planning trips involving the Arctic, aurora, or northern nature. |
| Dalarna and central Sweden | `references/dalarna-and-central-sweden.md` | Planning a trip to the lakes and cultural heartland. |
| Gotland and island planning | `references/gotland.md` | Visiting Gotland or planning Baltic island trips. |
| **Lifestyle and Execution** | | |
| Food, fika, supermarkets, and dining rhythm | `references/food-guide.md` | User asks about Swedish dining or groceries. |
| Nightlife, festivals, alcohol, and late hours | `references/nightlife.md` | User is asking about evening activities. |
| Traveling with children | `references/family-travel.md` | User mentions traveling with kids. |
| Accessibility and low-mobility planning | `references/accessibility.md` | User mentions mobility constraints. |
| Emergencies, alerts, and practical safety | `references/safety-and-emergencies.md` | Reviewing travel safety and risks. |
| Climate, daylight, snow, and shoulder seasons | `references/weather-and-seasonality.md` | Deciding when to visit or what to pack based on weather. |
| Connectivity, apps, and payment tools | `references/telecoms-and-apps.md` | Setting up data, phones, and digital payments. |
| Official source map | `references/sources.md` | Seeking primary reference links. |

## Core Rules

### 1. Route by Corridor, Not by Flag Count
For short trips, choose one main Sweden corridor: Stockholm and archipelago, west coast, south via Skane, central lake country, or Lapland. Sweden looks simple on a map but quality drops fast when every region becomes a stop.

### 2. Ask for Month Before Naming a Route
The correct Sweden plan changes radically by month. Daylight, snow cover, ferry frequency, archipelago service, aurora chances, swimming weather, and road safety all depend on season.

### 3. Confirm Schengen Math Before Locking Plans
Use `references/entry-and-documents.md` first for passport validity, Schengen day counting, EES rollout context, and whether the user is mixing Sweden with Denmark, Norway, Finland, or the Baltics.

### 4. Always Offer Two Transport Models
For any multi-stop trip, provide at least two viable patterns:
- Rail and ferry heavy: lower winter driving risk, more timetable dependence
- Flight or self-drive heavy: more reach, higher transfer or weather friction

### 5. Budget with Sweden Reality
Calculate full costs including hotel headlines, airport transfer costs, rail supplements, island ferries, car parking, winter gear, restaurant alcohol, and shoulder-season opening patterns.

### 6. Protect the User from Nordic Overreach
Flag bad combinations early:
- Stockholm, Gothenburg, Gotland, and Lapland in one week
- Lapland winter trips without darkness or cold tolerance
- Summer archipelago or Midsummer travel booked too late
- Cross-border south-Sweden plans that ignore passport or ID checks

### 7. Deliver Operational Plans
Output should include:
- Best base or base pair
- Day-by-day flow with realistic transfer windows
- Booking deadlines or low-inventory warnings
- Weather backup and downgrade options
- Safety notes for cold, ferries, and remote areas

## Common Traps

- Treat Sweden as a compact city-break country where south, center, and far north fit naturally into one short itinerary.
- Assume Schengen administration is trivial because the first arrival point is outside Sweden.
- Choose a rental car before checking whether rail plus one strategic base solves the trip better.
- Plan Lapland around aurora certainty instead of darkness, forecasts, and backup activities.
- Ignore ferry or island timetables in the archipelago and on Gotland.
- Underestimate how much alcohol, dining, and airport transfers move the real budget.
- Book scenic summer trips before confirming sharply seasonal services.
