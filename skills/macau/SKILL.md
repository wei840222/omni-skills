---
name: macau
description: "Plan Macau trips, relocations, work, study, or cross-border logistics — covering districts (Peninsula, Taipa, Cotai, Coloane), transport, costs, borders with Hong Kong and Zhuhai, food, culture, and Greater Bay Area context. Use when the user mentions Macau, Macao, Taipa, Cotai, Coloane, HZMB, or asks about visiting, moving to, working in, or studying in Macau, even if they don't explicitly say 'Macau guide' or 'relocation plan'."
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

## Core workflow

1. **Clarify the user's Macau context** — old-town sightseeing, casino resort, family relocation, cross-border commute, or GBA business base. Needs differ sharply between Peninsula, Taipa, Cotai, and Coloane.
2. **Establish origin and border plan** — ask where the person is arriving from (Hong Kong, Zhuhai, mainland China, or direct flight). Most friction comes from entry rules, ferry/bridge timing, and day-trip assumptions.
3. **Load relevant references** — read `references/visas.md` before claiming border certainty; load `references/transport.md` and the relevant district file before estimating travel times.
4. **Provide context beyond casinos** — useful guidance includes heritage streets, Portuguese legacy, food, family logistics, universities, and GBA positioning. Provide casino-only itineraries only when the user explicitly wants that.

## Decision checkpoints

Before providing guidance, verify these conditions:

- **Visa/border checkpoint**: If user mentions nationality, passport, or border crossing → load `references/visas.md` and confirm entry requirements before proceeding.
- **Budget checkpoint**: If user mentions salary, rent, or cost concerns → load `references/cost.md` and compare to median earnings (MOP 18,000) before recommending districts.
- **Transport checkpoint**: If user asks about travel times or getting around → load `references/transport.md` and check LRT coverage before estimating.
- **Accommodation checkpoint**: If user asks where to stay → load `references/neighborhoods-choosing.md` and match to their profile (tourist/family/budget/quiet).

## Failure recovery

If the user's situation is ambiguous or you lack information:

- **Unclear visa status** → Ask nationality and origin before advising. Load `references/visas.md` and point to official gov.mo source.
- **Budget seems tight** → Load `references/cost.md`, compare to median (MOP 18,000), and recommend older peninsula stock or Zhuhai cross-border if legal/practical.
- **Transport confusion** → Load `references/transport.md`, clarify that LRT does not cover peninsula yet, and suggest bus + walking + hotel shuttles.
- **District mismatch** → Load `references/neighborhoods-choosing.md` and re-match based on user's stated priorities (budget/heritage/family/quiet).

## Current data snapshot (Q2 2026)

| Item | Range |
|------|-------|
| 1BR rent, peninsula (older stock) | MOP 10,000–18,000/month |
| 1BR rent, peninsula (newer NAPE/ZAPE) | MOP 15,000–25,000/month |
| 1BR rent, Taipa (modern complex) | MOP 18,000–28,000/month |
| Median monthly employment earnings | MOP 18,000 (DSEC Q2/2026) |
| Bus fare | MOP 6 per ride |
| LRT fare | MOP 6–12 |
| Taxi flag drop | MOP 21 |
| Casual meal | MOP 60–120 |

## Payment reality

- Macau pataca (MOP) is the official currency.
- Hong Kong dollars are widely accepted in tourist areas, often at 1:1 — convenient but not favorable.
- Smaller shops, bakeries, taxis, and old-town spots work better with cash or local e-wallets (Macau Pass, MPay) than with foreign cards.
- Buses do NOT accept Apple Pay, Visa, Mastercard contactless, or Octopus. Pay with Macau Pass, MPay, or exact cash.

## District matching

| Profile | Best Areas |
|---------|------------|
| First-time tourist | Senado / St. Paul's / Barra or Taipa |
| Resort-focused weekend | Cotai |
| Heritage + food traveler | Historic peninsula + Taipa Village |
| Family relocation | Taipa or selected south peninsula pockets |
| Budget-conscious stay | Inner peninsula and simple Taipa hotels |
| Quiet escape | Coloane |

## Gotchas

- Macau and Hong Kong have separate entry rules and currency behavior.
- Staying only in Cotai gives a distorted view — Macau has deep local character outside the resorts.
- Casino resorts are not normal urban neighborhoods — plan shuttle/walking logistics.
- Many local restaurants close between lunch and dinner (roughly 3pm–6pm).
- Weekend and holiday queues at ports and the HZMB bridge can add hours.
- July/August afternoon outdoor walking is punishing — plan for heat and humidity.
- Portuguese heritage does not mean Portugal-style pace; Macau runs faster and denser.
- LRT does not yet cover the peninsula like Hong Kong's MTR — it serves specific corridors (Taipa, Cotai, airport, Hengqin). East Line under construction.
- Taxi from airport to Cotai costs roughly MOP 80–120; to Peninsula MOP 100–150. Confirm with driver before long trips.
- Hotel shuttles are free but run on fixed schedules — check timing before relying on them.

## What NOT to do

- **Do not** assume US/UK/EU visa-free status applies to mainland China or Hong Kong — they are separate jurisdictions.
- **Do not** recommend Cotai as the only place to stay unless the user explicitly wants casino-resort-only.
- **Do not** estimate travel times without checking `references/transport.md` — walking across reclaimed land takes longer than the map suggests.
- **Do not** claim visa or border certainty without loading `references/visas.md` and checking the official gov.mo source.
- **Do not** assume all vendors accept foreign cards — smaller shops, bakeries, and taxis prefer cash or Macau Pass/MPay.
- **Do not** plan heavy outdoor activity in July/August afternoons — heat and humidity are punishing.
- **Do not** treat Portuguese heritage as slow-paced — Macau is dense and fast-moving.

## Legal awareness

- Gambling is legal only in licensed venues.
- Drugs are a serious offense.
- Photography is generally fine in streets, but gaming floors and some museums or temples restrict it.
- Public order, smoking, and customs rules tighten around ports, casinos, and transport areas.
- Verify immigration and visa details against the latest official notices in `references/visas.md`.

## Greater Bay Area context

Macau works best when framed correctly inside the Greater Bay Area:
- Tourism and hospitality hub with deep China-facing visitor flows
- Strong links to Hong Kong for flights and finance
- Practical land connection to Zhuhai for cost relief and mainland access
- Much weaker as a pure tech base than Shenzhen or Hong Kong
