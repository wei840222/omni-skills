---
name: uk
description: >
  Plan United Kingdom trips with nation-specific routing, ETA-aware entry checks,
  rail-versus-car tradeoffs, and practical local logistics. Use when choosing England,
  Scotland, Wales, or Northern Ireland bases, confirming ETA or visitor-visa paths,
  comparing rail and road options, or answering London transit, seasonality, budget,
  and on-the-ground logistics questions. Not for standing multi-destination traveler
  systems (`travel`), multi-country day-by-day itineraries (`travel-planning`),
  Spanish composition (`spanish`), or restaurant booking workflows once the route is set
  (`booking`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇬🇧","requires":{"config":["<state_root>/uk/"]}}'
  related-skills: '{"travel":"Standing traveler system for passports, visas, bookings, and trip memory across destinations.","travel-planning":"Multi-city itineraries, packing lists, and budget tracking beyond one-country UK routing.","booking":"Search lodging or timed tickets after UK bases and dates are chosen.","car-rental":"Arrange rental cars after UK road and rural-route decisions are set.","food":"Deeper restaurant and cuisine planning once the UK route is fixed.","english":"Language help for bookings, menus, and service interactions.","flight":"Search or compare flights once UK airports and dates are decided."}'
---

## State location

Optional United Kingdom trip context may exist in
`<workspace>/uk/`, `<workspace>/memory/uk/`, or `~/uk/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/uk/`, `<workspace>/memory/uk/`, `~/uk/`.
3. If none exists and durable trip context must be created, default to
   `<workspace>/uk/` only with user consent.
4. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/uk/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

Legacy `~/Clawic/data/uk/` copies are migration sources only — move them into
the resolved `<state_root>/` when the user asks, and say in one line that you
moved them and from where.

**Data.** Durable notes live in `<state_root>/memory.md` when the user wants
trip context kept across sessions (see `references/memory-template.md` and
`references/setup.md`). This skill is primarily routing knowledge; durable notes
are optional. Avoid storing credentials, full passport numbers, payment details,
or third-party private data in skill state. Host-shared memory such as workspace
`MEMORY.md` is outside `<state_root>` and needs separate user consent.

```text
<state_root>/
└── memory.md     # Trip context, route logic, and evolving constraints
```

## When to Use

- Planning a United Kingdom trip beyond generic London tips
- Choosing England / Scotland / Wales / Northern Ireland bases and corridors
- Confirming ETA, visitor-visa, passport, and Common Travel Area logic before non-refundables
- Comparing rail-first versus car-first movement models
- Answering seasonality, budget, London transit, heritage, food, family, or safety logistics
- Not for standing multi-destination travel systems (`travel`), multi-country itineraries
  (`travel-planning`), Spanish composition (`spanish`), or lodging search once bases are chosen (`booking`)

## Core path

1. Load `references/setup.md` on first use or if state is empty and the user wants notes kept.
2. Resolve `<state_root>` before any state read/write.
3. Confirm entry logic with `references/entry-and-documents.md` before locking flights or non-refundable lodging.
4. Choose one macro-cluster with `references/regions.md` or `references/itineraries.md`; open only the leaf nation/city files needed.
5. Match transport to geography with `references/transport-domestic.md` and `references/road-trips-and-driving.md`.
6. Open `references/sources.md` before treating ETA, visa, customs, rail-fare, or other official claims as current fact; re-check the live page when money or legal consequences are involved.
7. Maintain `<state_root>/memory.md` only when durable context should persist, using `references/memory-template.md`.

## Quick Reference

| Topic | File | Load when |
|-------|------|-----------|
| Setup flow | `references/setup.md` | First use or empty state |
| Memory schema | `references/memory-template.md` | Creating or reshaping memory.md |
| ETA, visa, passport, border | `references/entry-and-documents.md` | Before non-refundable bookings |
| Customs, food, cash, duty | `references/customs-and-border.md` | Arrival goods or cash questions |
| Regions and route selection | `references/regions.md` | Choosing nation or corridor |
| Sample itineraries | `references/itineraries.md` | Duration and base-change patterns |
| Accommodation strategy | `references/accommodation.md` | Base and lodging style |
| Budget planning | `references/budget-and-costs.md` | Full-trip cost realism |
| Cards, cash, tipping | `references/payments-and-tipping.md` | Money norms |
| Rail, flights, ferries, transit | `references/transport-domestic.md` | Mode choice and city links |
| Driving and road-trip strategy | `references/road-trips-and-driving.md` | Rural or multi-stop car plans |
| London playbook | `references/london.md` | London-centred stays |
| South England and Cotswolds | `references/south-england-and-cotswolds.md` | Bath, Cotswolds, south coast |
| North England and Lake District | `references/north-england-and-lake-district.md` | York, Lakes, north corridors |
| Scotland | `references/scotland.md` | Edinburgh, Glasgow, Highlands |
| Wales | `references/wales.md` | Cardiff, Snowdonia/Eryri, coast |
| Northern Ireland | `references/northern-ireland.md` | Belfast and NI routing |
| Heritage and castles | `references/heritage-and-castles.md` | Timed heritage days |
| Food by region | `references/food-guide.md` | Meal planning beyond generics |
| Nightlife | `references/nightlife.md` | Evening plans by destination type |
| Family travel | `references/family-travel.md` | Kids, pace, access |
| Accessibility | `references/accessibility.md` | Step-free and assistance planning |
| Safety and emergencies | `references/safety-and-emergencies.md` | 999/111, disruption, health |
| Weather and seasonality | `references/weather-and-seasonality.md` | Rain, daylight, bank holidays |
| Telecoms and apps | `references/telecoms-and-apps.md` | SIM, payments, journey apps |
| Official source map | `references/sources.md` | Re-checking mutable official facts |

## Progressive Disclosure

- Start from this file plus entry logic and either `references/regions.md` or the single topic the user asked about.
- Open nation or city files only after the macro-cluster is in play.
- Open `references/sources.md` when quoting ETA, visa, customs, TfL, or other official claims that may change.

## Core Rules

### 1. Route by nation and corridor
Keep one macro-cluster per week: London plus South England, North England plus Scotland, or one nation-focused loop. Strong rail and roads do not make four-nation packing high quality on a short trip.

### 2. Confirm entry before non-refundables
Use `references/entry-and-documents.md` first: ETA versus visa, passport validity for the whole stay, border flow, and any Ireland or Northern Ireland crossover complexity. ETA is permission to travel, not a guarantee of admission.

### 3. Match transport to geography
Offer at least two movement models:
- Rail-first for London, major English cities, and Edinburgh/Glasgow corridors
- Car-first for Cotswolds, Cornwall, Highlands, Snowdonia/Eryri, or coastal-rural loops

### 4. Keep Great Britain and Northern Ireland distinct
Payments, transport, geography, and cross-border considerations change when Northern Ireland or the Republic of Ireland enters the plan. Confirm both UK and Ireland entry logic before spending money on combined routes.

### 5. Budget the real total
Price more than the room headline: rail yield pricing, hotel breakfast or parking, London transit and airport transfers, heritage day spend, and rural car costs.

### 6. Make every plan season-aware
Use `references/weather-and-seasonality.md` before promising island hops, Highlands driving, coastal hikes, or festival-heavy weekends. Rain, wind, short winter daylight, and bank-holiday crowding reshape good routes.

### 7. Deliver actionable plans
Every final output should include base strategy, day-by-day flow with realistic transfer windows, reservation deadlines, rain or disruption backups, and safety quick notes.

## Failure Modes

- Treating the UK as London plus a few easy day trips and missing nation-level tradeoffs
- Combining London, Edinburgh, Highlands, Wales, and Belfast into one short trip
- Renting a car for London-centred itineraries where rail and transit are stronger
- Inventing ETA, visa, or Ireland-crossover rules without checking official sources for the traveler's nationality
- Quoting stale TfL, rail, or heritage prices instead of routing through `references/sources.md`
- Writing skill state without resolving `<state_root>` or without user consent for new durable files
- Copying U.S. tipping or tax assumptions into UK plans

## Security & Privacy

**Data that stays local:** Trip preferences and optional notes under `<state_root>/`.

**Out of scope for silent network use:** This skill does not require outbound API calls for core routing. When mutable official facts are needed, open the live pages listed in `references/sources.md` rather than inventing prices, fees, or eligibility.
