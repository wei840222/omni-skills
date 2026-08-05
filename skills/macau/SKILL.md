---
name: macau
description: "Navigate Macau as visitor, resident, worker, student, or founder — districts, transport, costs, borders, culture, and practical local context. Use when the user asks about visiting, relocating to, working in, studying in, or setting up cross-border plans involving Macau, Taipa, Cotai, Coloane, or the Greater Bay Area."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇲🇴"}'
  related-skills: '{"dubai":"Another compact tourism-heavy city with relocation depth, useful as a benchmark.","money":"Budgeting, exchange-rate thinking, and cost trade-offs relevant to Macau trip or relocation planning.","taiwan":"Another Chinese-language destination with practical travel depth, shares cultural context.","traditional-chinese":"Traditional Chinese context useful across Macau and nearby regions.","travel":"General trip planning and itinerary structure that complements Macau-specific guidance."}'
---

# Macau

Navigate Macau for visiting, relocating, working, studying, or cross-border planning with Hong Kong and Zhuhai.

## State location

Macau state may exist in `<workspace>/macau/`, `<workspace>/memory/macau/`, or `~/macau/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/macau/`, `<workspace>/memory/macau/`, `~/macau/`.
3. If none exists and state must be created, default to `<workspace>/macau/`.

Use the selected `<state_root>` for every state operation in this skill.

```text
<state_root>/
└── memory.md     # User context for trip, relocation, work, and border logistics
```

If `<state_root>/memory.md` is missing or empty, initialize it from `references/memory-template.md`.

## When to Use

User asks about Macau for any purpose: visiting, relocating, working in hospitality or gaming-adjacent roles, studying, or setting up cross-border plans with Hong Kong or Zhuhai.

## Resource routing

Load the matching reference file for each topic area. Read only the files relevant to the user's question.

| Topic | Reference |
|-------|-----------|
| First-use setup and memory initialization | `references/setup.md` |
| Memory template and status values | `references/memory-template.md` |
| **Visitors** | |
| Attractions and what matters | `references/visitor-attractions.md` |
| 1, 2, and 3 day routes | `references/visitor-itineraries.md` |
| Where to stay by trip style | `references/visitor-lodging.md` |
| Border, money, and practical tips | `references/visitor-tips.md` |
| **Districts** | |
| Quick comparison | `references/neighborhoods-index.md` |
| Historic peninsula districts | `references/neighborhoods-historic.md` |
| NAPE, Outer Harbour, east peninsula | `references/neighborhoods-central.md` |
| Taipa village and central Taipa | `references/neighborhoods-taipa.md` |
| Cotai and integrated resorts | `references/neighborhoods-cotai.md` |
| Coloane village and south side | `references/neighborhoods-coloane.md` |
| Choosing guide | `references/neighborhoods-choosing.md` |
| **Food** | |
| Dining scene overview | `references/food-overview.md` |
| Macanese, Cantonese, and local staples | `references/food-local.md` |
| International and hotel dining | `references/food-international.md` |
| Best food areas | `references/food-areas.md` |
| Reservations, tipping, and practical rules | `references/food-practical.md` |
| **Practical** | |
| Moving and settling | `references/resident.md` |
| Buses, LRT, ferries, walking, taxis | `references/transport.md` |
| Cost of living | `references/cost.md` |
| Safety and legal realities | `references/safety.md` |
| Weather and typhoon planning | `references/climate.md` |
| Banking, SIM, payments, and utilities | `references/local.md` |
| **Career** | |
| Tech and digital work reality | `references/tech.md` |
| Company setup and taxes | `references/business.md` |
| Entry and residency paths | `references/visas.md` |
| Startup and diversification landscape | `references/startup.md` |
| **Lifestyle** | |
| Culture and etiquette | `references/culture.md` |
| Healthcare and hospitals | `references/healthcare.md` |
| Schools and universities | `references/education.md` |
| Expat and local lifestyle | `references/lifestyle.md` |
| Driving, parking, and scooter logic | `references/driving.md` |

## Core Rules

### 1. Identify the User's Macau First
- Clarify whether the user means old-town sightseeing, casino resort time, family relocation, cross-border commuting, or a Greater Bay Area business base.
- Macau is tiny, but user needs differ sharply between Peninsula, Taipa, Cotai, and Coloane.

### 2. Treat Borders as a Core Planning Layer
- Most friction comes from entry rules, ferry or bridge timing, and day-trip or commute assumptions.
- Always ask where the person is arriving from: Hong Kong, Zhuhai, mainland China, or direct flight.
- Re-check current entry rules in `references/visas.md` before claiming certainty.

### 3. Macau Is Not Just Casinos
- Gaming and tourism dominate the economy, but useful guidance also means heritage streets, Portuguese legacy, food, family logistics, universities, and GBA positioning.
- Provide casino-only itineraries only when the user explicitly wants that.

### 4. Small Geography Does Not Mean Zero Logistics
- The peninsula is walkable in parts, but heat, humidity, crowds, and bridge bottlenecks change the real experience.
- Cotai resorts look close on the map yet still require planned walking or shuttles.
- Load `references/transport.md` and the relevant district file before estimating travel times.

### 5. Current Data Snapshot (March 2026)

| Item | Range |
|------|-------|
| 1BR rent, peninsula | MOP 8,000–14,000/month |
| 1BR rent, Taipa/Cotai | MOP 12,000–20,000/month |
| Median monthly employment earnings | Around MOP 17,000 |
| Bus fare | MOP 6 per ride |
| LRT fare | MOP 6–12 |
| Taxi flag drop | MOP 21 |
| Casual meal | MOP 60–120 |

### 6. Cash, Currency, and Payment Reality
- Macau pataca (MOP) is the official currency.
- Hong Kong dollars are widely accepted in tourist areas, often at 1:1, which is convenient but not favorable.
- Smaller shops, bakeries, taxis, and some old-town spots work better with cash or local e-wallets than with foreign cards.

### 7. Match the District to the User

| Profile | Best Areas |
|---------|------------|
| First-time tourist | Senado / St. Paul's / Barra or Taipa |
| Resort-focused weekend | Cotai |
| Heritage + food traveler | Historic peninsula + Taipa Village |
| Family relocation | Taipa or selected south peninsula pockets |
| Budget-conscious stay | Inner peninsula and simple Taipa hotels |
| Quiet escape | Coloane |

## Macau-Specific Traps

- Assuming Macau and Hong Kong share the same entry rules or money behavior.
- Staying only in Cotai, then claiming "Macau has no local character."
- Treating a casino resort as a normal urban neighborhood.
- Assuming all vendors take cards and all prices are quoted in HKD.
- Underestimating weekend or holiday queues at ports and the bridge.
- Planning heavy outdoor walking in July or August afternoons.
- Forgetting that many good local restaurants close between lunch and dinner.
- Thinking Portuguese heritage means Portugal-style pace; Macau often runs faster and denser.

## Legal Awareness

- Gambling is legal only in licensed venues.
- Drugs are a serious offense.
- Photography is generally fine in streets, but gaming floors and some museums or temples restrict it.
- Public order, smoking, and customs rules tighten around ports, casinos, and transport areas.
- Verify immigration and visa details against the latest official notices in `references/visas.md`.

## Greater Bay Area Context

Macau works best when framed correctly inside the Greater Bay Area:
- Tourism and hospitality hub with deep China-facing visitor flows
- Strong links to Hong Kong for flights and finance
- Practical land connection to Zhuhai for cost relief and mainland access
- Much weaker as a pure tech base than Shenzhen or Hong Kong
