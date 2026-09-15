---
name: brazil
description: Structure Brazil travel itineraries. Load this skill to route between macro-regions, verify visa/entry rules, plan payment strategies (PIX/CPF), and resolve city-level logistics.
metadata:
  openclaw: '{"emoji": "🇧🇷", "requires": {"config": ["<state_root>/brazil/"]}, "configPaths": ["<state_root>/brazil/"]}'
  related-skills:
    travel: skills/travel
    booking: skills/booking
    car-rental: skills/car-rental
    food: skills/food
    portuguese: skills/portuguese
---

## When to load

Load this skill when the user is planning travel to Brazil. Use it for nationality-specific entry checks, realistic routing across long distances, neighborhood-aware stays, money and payment strategies (including PIX/CPF friction), and on-the-ground execution rules.

## Architecture

Memory lives in `<state_root>/brazil/`. If `<state_root>/brazil/` does not exist, run `references/setup.md`. See `assets/memory-template.md` for structure.

```text
<state_root>/brazil/
└── memory.md     # Trip context and evolving constraints
```

## Quick Reference

Use this map to enter the right decision module before building the route.

| Topic | File |
|-------|------|
| **Entry, Border, and Money** | |
| Tourist entry, visas, passport checks, vaccines | `references/entry-and-documents.md` |
| Customs, declarations, restricted goods, cash | `references/customs-and-border.md` |
| Cards, cash, PIX, exchange, CPF friction | `references/money-payments-and-exchange.md` |
| **Planning Backbone** | |
| Macro-regions and route architecture | `references/regions.md` |
| Sample itineraries for 7-21 days | `references/itineraries.md` |
| Accommodation and neighborhood logic | `references/accommodation.md` |
| Budget framing and hidden-cost traps | `references/budget-and-costs.md` |
| Flights, buses, ferries, airport buffers | `references/transport-domestic.md` |
| Self-drive loops, tolls, night-driving rules | `references/road-trips-and-driving.md` |
| Parks, islands, lodges, permits, nature logistics | `references/national-parks-and-nature.md` |
| Cross-border side trips and re-entry risk | `references/border-hops-and-neighbor-countries.md` |
| **Major Regions and Cities** | |
| Rio de Janeiro playbook | `references/rio-de-janeiro.md` |
| Sao Paulo playbook | `references/sao-paulo.md` |
| Salvador and Bahia coast playbook | `references/salvador-and-bahia-coast.md` |
| Foz do Iguacu playbook | `references/foz-do-iguacu.md` |
| Manaus and Amazon playbook | `references/manaus-and-amazon.md` |
| Pantanal and Bonito playbook | `references/pantanal-and-bonito.md` |
| Florianopolis and Santa Catarina coast playbook | `references/florianopolis-and-santa-catarina.md` |
| Fernando de Noronha and Recife playbook | `references/fernando-de-noronha-and-recife.md` |
| Minas Gerais and colonial cities playbook | `references/minas-gerais-and-colonial-cities.md` |
| Brasilia and Chapada dos Veadeiros playbook | `references/brasilia-and-chapada-dos-veadeiros.md` |
| **Lifestyle and Execution** | |
| Food strategy by region and city type | `references/food-guide.md` |
| Nightlife and late-return logic | `references/nightlife.md` |
| Families, mixed ages, and calmer routes | `references/family-travel.md` |
| Accessibility and low-mobility planning | `references/accessibility.md` |
| Safety, theft prevention, beach and heat risk | `references/safety-and-emergencies.md` |
| Climate, rain, heat, smoke, and events | `references/weather-and-seasonality.md` |
| Connectivity, eSIM, transport, and useful apps | `references/telecoms-and-apps.md` |
| Research sources map | `references/sources.md` |

## Core Rules

### 1. Build Brazil by Macro-Blocks, Not by Wish List
For short and medium trips, keep to one anchor block and one contrast block at most. Brazil punishes fantasy routing more than most countries because flights, ferries, and road transfers consume real daylight.

### 2. Lock Entry, Health, and Money Before Non-Refundables
Before buying flights, confirm the correct entry path in `references/entry-and-documents.md`, check vaccine recommendations for the planned ecosystems, and decide the payment model from `references/money-payments-and-exchange.md`.

### 3. Choose Cities by Profile, Not by Fame
Rio, Sao Paulo, Salvador, Florianopolis, Recife, and Brasilia solve different trips. Recommend the city and neighborhood that fits the user's pace, beach needs, food goals, and risk tolerance.

### 4. Always State the Transfer Cost of Every Dream Add-On
Each extra region must include the true price of adding it:
- Door-to-door travel time
- New baggage or transfer costs
- Lost beach, park, or city time
- New weather or logistics risk

### 5. Treat PIX and CPF as Friction, Not Assumptions
Cards work widely in major corridors, but local operators, event tickets, and some websites may prefer PIX or ask for CPF. Offer foreigner-safe booking channels and clarify which local deals require PIX/CPF.

### 6. Give Safer Arrival and Return Plans
When users land late, move between neighborhoods, or return after nightlife, recommend the transport model explicitly and tell them which transport models require advance booking.

### 7. Deliver Actionable Plans
Output should include:
- Best-fit base city and neighborhood
- Day-by-day flow with realistic transfer buffers
- What must be booked early
- Payment and connectivity setup
- Safety and weather fallback notes

## Common Traps

- Treating Brazil like one compact destination instead of several different trip products.
- Adding Amazon, Rio, Iguacu, and beach islands into one short holiday.
- Assuming "best time for Brazil" exists as one answer for all regions.
- Choosing accommodation by nightly rate only and losing hours in traffic or unsafe arrival patterns.
- Assuming every app, ticket site, or small operator will accept foreign cards without friction.
- Underestimating New Year, Carnival, and school-holiday price spikes.
- Treating security as a generic warning instead of a context-specific operating rule.

## Security & Privacy

Data that stays local:
- trip preferences and working plans under `<state_root>/brazil/` if the user approves persistence

This skill does NOT:
- access files outside `<state_root>/brazil/`
- make network requests by default
- store passport numbers, payment credentials, or booking confirmation secrets in memory files
- book tickets or submit visa applications on the user's behalf

## Scope

This skill ONLY:
- structures Brazil trip planning into entry, money, routing, city, and logistics modules
- keeps durable trip-context notes under `<state_root>/brazil/` when approved
- points to official sources for entry, customs, transport, health, and destination facts

Required restrictions:
- invent one universal "best time for Brazil" for all regions
- pack Amazon, Rio, Iguacu, and remote islands into one short trip without stating transfer cost
- assume every local operator accepts foreign cards without PIX/CPF friction
- give generic safety warnings without neighborhood or arrival context

## Related Skills
- `travel` - General trip planning and itinerary structure.
- `booking` - Reservation workflows and confirmation hygiene.
- `car-rental` - Self-drive strategy and handoff logistics.
- `food` - Deeper restaurant and cuisine recommendations.
- `portuguese` - Language support for bookings, transport, and service interactions.
