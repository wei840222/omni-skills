---
name: mexico
description: >
  Plan Mexico travel with neighborhood-level city routing, regional base selection,
  food timing, coastal weather buffers, and practical transport logistics. Use when
  choosing CDMX/Oaxaca/Guadalajara/Yucatan/Baja bases, pacing altitude and heat,
  avoiding multi-region transfer traps, or answering Mexico lodging, food, transit,
  and safety questions. Prefer `travel` for multi-country traveler systems,
  `travel-planning` for generic multi-city itinerary scaffolding, and `spanish`
  for Spanish writing rather than destination routing.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇲🇽"}'
---

## State location

Optional Mexico trip context may exist in
`<workspace>/mexico/`, `<workspace>/memory/mexico/`, or `~/mexico/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/mexico/`, `<workspace>/memory/mexico/`, `~/mexico/`.
3. If none exists and durable trip context must be created, default to
   `<workspace>/mexico/` only with user consent.
4. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/mexico/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

**Data.** Durable notes live in `<state_root>/memory.md` when the user wants
trip context kept across sessions (see `assets/data-templates.md` and
`references/setup.md`). This skill is primarily routing knowledge; durable notes
are optional. Do not invent a booking CRM unless the user asks to keep state.
Avoid storing credentials, full passport numbers, payment details, or third-party
private data in skill state. Host-shared memory such as workspace `MEMORY.md` is
outside `<state_root>` and needs separate user consent.

```text
<state_root>/
└── memory.md     # Trip context, route logic, and evolving constraints
```

## When to Use

- Planning a Mexico trip beyond brochure-level city lists
- Choosing a primary base among Mexico City, Oaxaca, Guadalajara/Jalisco, Yucatan/Riviera Maya, or Baja
- Pacing altitude, heat, UV, museum queues, and meal timing
- Avoiding short-trip multi-region transfer traps
- Answering lodging style, food strategy, domestic transport, weather buffers, and practical safety
- Not for standing multi-destination travel systems (`travel`), generic itinerary scaffolding (`travel-planning`), or Spanish composition (`spanish`)

## Core path

1. Load `references/setup.md` on first use or if state is empty and the user wants notes kept.
2. Resolve `<state_root>` before any state read/write.
3. Load only the leaf `references/` files needed for the current decision; start with region fit before stacking coasts and day trips.
4. Open `references/sources.md` before treating entry, visa, Tren Maya status, weather advisories, or other official claims as current fact; re-check the live page when money or legal consequences are involved.
5. Maintain `<state_root>/memory.md` only when durable context should persist, using `assets/data-templates.md`.

## Quick Reference

| Topic | File | Load when |
|-------|------|-----------|
| Mexico City | `references/cdmx.md` | CDMX neighborhoods, museums, food pacing |
| Oaxaca | `references/oaxaca.md` | Culture, cuisine, day-trip craft routes |
| Guadalajara / Jalisco | `references/guadalajara.md` | Urban culture and Tequila day routes |
| Yucatan / Riviera Maya | `references/yucatan-riviera-maya.md` | Beaches, cenotes, ruins, humidity pacing |
| Regions overview | `references/regions.md` | Choosing a primary base or multi-base feasibility |
| Sample itineraries | `references/itineraries.md` | Duration-fit route shapes |
| Accommodation style | `references/accommodation.md` | Neighborhood and stay-style fit |
| Useful apps | `references/apps.md` | Discovery tools before paying for bookings |
| Food strategy | `references/food-guide.md` | Market lunch and reservation timing |
| Wine routes | `references/wine.md` | Baja / highland tasting plans |
| Signature experiences | `references/experiences.md` | High-signal activities by region |
| Beaches | `references/beaches.md` | Caribbean vs Pacific beach fit |
| Hiking / altitude | `references/hiking.md` | Elevation and outdoor pacing |
| Nightlife | `references/nightlife.md` | City or coast evening plans |
| Culture / etiquette | `references/culture.md` | Local expectations and etiquette |
| Traveling with kids | `references/with-kids.md` | Family pacing and logistics |
| Transport | `references/transport.md` | Metro, buses, flights, Tren Maya checks |
| Phone / internet | `references/telecoms.md` | Connectivity setup |
| Emergencies / safety | `references/emergencies.md` | Practical safety and emergency routing |
| Verified sources | `references/sources.md` | Official URLs before money/legal claims |

## Core Rules

### 1. Specific Over Generic
Route by neighborhood and clock time: "start with a market lunch in Roma Norte before 13:00, reserve dinner in Condesa or Juarez, and plan around peak queue windows in central tourist corridors."

### 2. Local Perspective
Prefer what locals and repeat travelers actually do:
- One high-tourist zone usually raises costs and lowers food quality
- Same-day transfers between distant regions look easy on maps but burn most of the day
- Midday heat and sun exposure can break beach and archaeological plans without pacing
- Historic centers are useful, but neighborhood-level planning usually improves value

### 3. Regional Differences

| Region | Key difference |
|--------|----------------|
| Mexico City | Museum and food density, strongest urban transit, neighborhood-driven planning |
| Oaxaca | Culture and cuisine depth, slower rhythm, day-trip craft and mezcal routes |
| Guadalajara and Jalisco | Urban culture plus Tequila day routes, balanced city value |
| Yucatan and Riviera Maya | Beaches, cenotes, ruins, and humidity-driven pacing |
| Baja California | Wine routes, desert-coast contrast, road-trip logic |
| Central Highlands | Colonial cities, cooler climate, culture-first itineraries |

### 4. Timing is Everything
- Dry season is usually easier for long route planning in many regions
- Rain and hurricane windows need flexible coastal itineraries
- Peak holiday weeks can change pricing and transfer reliability quickly
- Urban museums and top restaurants perform better with weekday timing
- Heat index and UV intensity should shape daily plans, not only distance

### 5. Flag Tourist Traps
Call out these anti-patterns explicitly:
- Paying premium prices in high-traffic restaurant strips without a quality signal
- Attempting CDMX, Oaxaca, and Riviera Maya in a short trip with no buffer
- Overstacking ruins, beach time, and nightlife in one humid day
- Ignoring airport-to-hotel transfer strategy until arrival

### 6. Match Trip Style

| Traveler | Focus on |
|----------|----------|
| Foodie | `references/food-guide.md`, `references/cdmx.md`, `references/oaxaca.md` |
| Culture and history | `references/regions.md`, `references/cdmx.md`, `references/oaxaca.md` |
| Beach and nature | `references/yucatan-riviera-maya.md`, `references/beaches.md`, `references/hiking.md` |
| Family | `references/with-kids.md`, `references/accommodation.md`, `references/itineraries.md` |
| Nightlife | `references/nightlife.md`, `references/cdmx.md`, `references/guadalajara.md` |
| Mixed route trip | `references/itineraries.md`, `references/transport.md`, `references/regions.md` |

## Common Traps

- Treating Mexico as one compact destination with easy transfers
- Choosing too many bases for short trips
- Booking key beach and holiday stays too late
- Ignoring heat and humidity limits for outdoor-heavy days
- Using only social-media spots with long queues and weak value
- Assuming every area has the same safety profile

## Security & Privacy

**Data that stays local:** optional trip preferences in `<state_root>/`

**This skill does NOT:** access files outside `<state_root>/` or make network requests during normal guidance. Re-check live official pages from `references/sources.md` when the user needs current legal, entry, or service-status facts.
