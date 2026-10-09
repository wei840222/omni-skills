---
name: dominican-republic
description: >
  Plan Dominican Republic trips with beach-region routing, verified entry
  steps, off-resort logistics, and practical local safety. Use when choosing a coast
  or base, deciding resort vs independent travel, handling e-ticket and entry steps,
  or answering transport, weather, and safety questions for Dominican Republic travel.
  Not for general multi-country trip systems (`travel`), day-by-day multi-destination
  itineraries (`travel-planning`), or Spanish-language writing (`spanish`).
metadata:
  version: "1.2.0"
  openclaw: '{"emoji":"🇩🇴"}'
  related-skills: '{"travel":"Standing traveler system for passports, visas, bookings, and trip memory across destinations.","travel-planning":"Multi-city itineraries, packing lists, and budget tracking beyond one-country DR routing.","spanish":"Write or edit Spanish-language text rather than plan Dominican Republic travel.","mexico":"Plan Mexico travel instead of Dominican Republic destinations.","spain":"Plan Spain travel instead of Dominican Republic destinations.","flight":"Search or compare flights once the DR route and airports are decided.","booking":"Search lodging after the coast and stay style are chosen.","car-rental":"Arrange rental cars after DR road and transfer decisions are set."}'
---

## State location

Optional Dominican Republic trip context may exist in
`<workspace>/dominican-republic/`, `<workspace>/memory/dominican-republic/`, or
`~/dominican-republic/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/dominican-republic/`, `<workspace>/memory/dominican-republic/`,
   `~/dominican-republic/`.
3. If none exists and durable trip context must be created, default to
   `<workspace>/dominican-republic/` only with user consent.
4. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/dominican-republic/` may be read; otherwise ask before creating
   data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

**Data.** Durable notes live in `<state_root>/memory.md` when the user wants
trip context kept across sessions (see `references/memory-template.md` and
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

- Planning a Dominican Republic trip beyond generic resort marketing
- Choosing which coast or base fits calm water, surf, city depth, or independent travel
- Confirming e-ticket, entry, passport, and visa-check paths before non-refundable bookings
- Handling domestic transport, night-driving risk, weather timing, and practical safety
- Not for standing multi-destination travel systems (`travel`), multi-country itineraries (`travel-planning`), or Spanish composition (`spanish`)

## Core path

1. Load `references/setup.md` on first use or if state is empty and the user wants notes kept.
2. Resolve `<state_root>` before any state read/write.
3. Load `references/domain.md` for coast-fit traps and execution rules; open only the leaf `references/` files needed for the current decision.
4. Open `references/sources.md` before treating e-ticket, visa, safety, or other official claims as current fact; re-check the live page when money or legal consequences are involved.
5. Maintain `<state_root>/memory.md` only when durable context should persist, using `references/memory-template.md`.

## Quick Reference

| Topic | File | Load when |
|-------|------|-----------|
| Domain rules and traps | `references/domain.md` | Non-trivial DR planning |
| Regions and coast fit | `references/regions.md` | Choosing base coast or multi-base route |
| Beaches and water fit | `references/beaches.md` | Calm swim, surf, snorkel, or boat days |
| Entry and documents | `references/entry-and-documents.md` | E-ticket, visa path, passport checks |
| Domestic transport | `references/transport-domestic.md` | Airports, transfers, buses, domestic hops |
| Road trips and driving | `references/road-trips-and-driving.md` | Rental car, night driving, toll roads |
| Safety and emergencies | `references/safety-and-emergencies.md` | 911, beach flags, theft, storm buffer |
| Weather and seasonality | `references/weather-and-seasonality.md` | Hurricane season, heat, rain timing |
| Budget and costs | `references/budget-and-costs.md` | Stay style and daily spend bands |
| Payments and money | `references/payments-and-money.md` | Cards, cash, tips, ATMs |
| Accommodation styles | `references/accommodation.md` | Resort, boutique, apartment, villa |
| Punta Cana / Bavaro | `references/punta-cana-and-bavaro.md` | East-coast resort ease |
| Bayahibe / La Romana | `references/bayahibe-and-la-romana.md` | Calm Caribbean water, lighter AI density |
| Samana / Las Terrenas | `references/samana-and-las-terrenas.md` | Independent beach-town base |
| Puerto Plata / Cabarete / Sosua | `references/puerto-plata-cabarete-and-sosua.md` | North-coast wind and surf |
| Santo Domingo | `references/santo-domingo.md` | City culture overnight, not beach filler |
| Jarabacoa / Constanza | `references/jarabacoa-and-constanza.md` | Highlands and cooler climate |
| Itineraries | `references/itineraries.md` | Sample day patterns and base changes |
| Experiences | `references/experiences.md` | Tours, boats, nature days |
| Food guide | `references/food-guide.md` | Local dining beyond resort buffet |
| Nightlife | `references/nightlife.md` | Evening plans by region |
| Family travel | `references/family-travel.md` | Kids, mobility, beach safety |
| Culture | `references/culture.md` | Local norms and etiquette |
| Telecoms and apps | `references/telecoms-and-apps.md` | SIM, rideshare, delivery apps |
| Setup | `references/setup.md` | First use or empty state |
| Memory template | `references/memory-template.md` | Creating or reshaping memory.md |
| Sources | `references/sources.md` | Official URLs to re-check |

## Progressive Disclosure

- Start from this file plus `references/domain.md` and either `references/regions.md` or the single topic the user asked about.
- Open destination files only after the coast or trip style is in play.
- Open `references/sources.md` when quoting entry, safety, or official destination claims that may change.

## Failure Modes

- Overselling Punta Cana all-inclusives when the user wants calm independent beaches or city depth
- Treating Santo Domingo as a same-day beach side trip from far east-coast resorts
- Ignoring night-driving, transfer time, and hurricane-season buffer
- Inventing visa or e-ticket rules without checking official sources for the traveler's nationality
- Writing skill state without resolving `<state_root>` or without user consent for new durable files
