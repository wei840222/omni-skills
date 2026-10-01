---
name: argentina
description: Load this skill to structure Argentina itineraries, validate regional
  logic, and plan practical logistics including money strategy and domestic transport.
metadata:
  openclaw: '{"emoji": "🇦🇷", "requires": {"bins": [], "config": ["<state_root>"]},
    "os": ["linux", "darwin", "win32"], "displayName": "Argentina"}'
  related-skills:
  - travel
  - car-rental
  - booking
  - food
  - spanish
---

## When to load

Load this skill when the user is planning a trip to Argentina and needs practical guidance on entry rules, money and payments, region choice, flight and road logic, park access, safety, and day-to-day execution.

## Setup

If `<state_root>` doesn't exist or is empty, read `references/setup.md` and start naturally.
Memory lives in `<state_root>`. See `assets/memory-template.md` for structure.

## Reference Routing

Always read the relevant references from `references/` before answering:

| Topic | File |
|-------|------|
| **Entry, Border, and Money** | |
| Tourist entry, visa, stays, paperwork | `references/entry-and-documents.md` |
| Customs, cash limits, food, tax-free notes | `references/customs-and-border.md` |
| Cash, cards, exchange logic, VAT, tips | `references/money-payments-and-exchange.md` |
| **Planning Backbone** | |
| Region selection and route architecture | `references/regions.md` |
| Sample itineraries for 7-21 days | `references/itineraries.md` |
| Accommodation strategy by trip style | `references/accommodation.md` |
| Budget framing and cost traps | `references/budget-and-costs.md` |
| **Transport and Nature** | |
| Flights, buses, trains, airport buffers | `references/transport-domestic.md` |
| Self-drive, mountain roads, border paperwork | `references/road-trips-and-driving.md` |
| Parks, permits, tickets, outdoor logistics | `references/national-parks-and-nature.md` |
| Neighbor-country side trips and border hops | `references/border-hops-and-neighbor-countries.md` |
| **Major Regions and Cities** | |
| Buenos Aires playbook | `references/buenos-aires.md` |
| Mendoza and wine country playbook | `references/mendoza-and-wine-country.md` |
| Iguazu and Misiones playbook | `references/iguazu-and-misiones.md` |
| Patagonia Lakes playbook | `references/patagonia-lakes.md` |
| South Patagonia playbook | `references/patagonia-south.md` |
| Ushuaia and Tierra del Fuego playbook | `references/ushuaia-and-tierra-del-fuego.md` |
| Salta and Jujuy playbook | `references/salta-and-jujuy.md` |
| Peninsula Valdes and Puerto Madryn playbook | `references/peninsula-valdes-and-puerto-madryn.md` |
| Cordoba and central Argentina playbook | `references/cordoba-and-central-argentina.md` |
| Atlantic coast and Mar del Plata playbook | `references/atlantic-coast-and-mar-del-plata.md` |
| **Lifestyle and Execution** | |
| Food strategy by region and timing | `references/food-guide.md` |
| Nightlife by city type | `references/nightlife.md` |
| Traveling with children or mixed ages | `references/family-travel.md` |
| Accessibility and low-mobility planning | `references/accessibility.md` |
| Emergencies, theft, weather alerts, disruptions | `references/safety-and-emergencies.md` |
| Climate and seasonality planning | `references/weather-and-seasonality.md` |
| Connectivity, transport cards, helpful apps | `references/telecoms-and-apps.md` |
| Research sources map | `references/sources.md` |

## Core Rules

1. **Route by Macro-Region, Not by Map Fantasy:** For short trips, pick one anchor cluster and one contrast region at most.
2. **Lock Entry and Money Before Non-Refundables:** Confirm the correct entry path, length of stay, border-hop implications, and payment strategy before buying flights.
3. **Ask for Month First:** Argentina changes dramatically by season; plan with region-specific weather knowledge.
4. **Treat Patagonia as Multiple Trips:** Lake District, South Patagonia, and Ushuaia are different products. Plan each segment intentionally.
5. **Always Offer Two Transport Models:** For each route, give at least two practical options with tradeoffs (flight-heavy vs. road/bus-heavy).
6. **Budget with Friction, Not Headlines:** Account for transfer costs, excursion timing, and card/cash execution.
7. **Deliver Action Plans:** Output should include base-city strategy, day-by-day flow, booking deadlines, weather fallbacks, and safety notes.
