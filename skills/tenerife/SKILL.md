---
name: tenerife
description: >
  Guide Tenerife visits, moves, and remote-work stays with north/south zone fit,
  transport, cost bands, residency orientation, and Canary tax context. Use for
  visitor itineraries, digital-nomad bases, NIE/empadronamiento orientation, or
  Teide/microclimate planning. Not for filing a visa, booking non-refundable
  travel, or quoting live income floors without re-checking official pages.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🌋"}'
  related-skills: '{"travel":"Multi-country or multi-island itineraries when Tenerife is only one stop.","booking":"Reservation hygiene after the Tenerife base and dates are chosen.","food":"Deeper cuisine workflows beyond Canarian dining pointers.","spanish":"Spanish production for forms, menus, and local bookings.","housing":"Cross-market housing search when Tenerife is one candidate island.","europe":"Schengen / multi-city Europe framing beyond Tenerife-only logistics.","flight":"Flight shopping and buffer planning into TFN/TFS.","expat":"General expat settling patterns that are not Tenerife-specific."}'
---

# Tenerife

Island routing for **Tenerife**: north/south character, zone fit, visitor pacing,
remote-work bases, and Canary practicalities. Prefer live official pages before
any booking-critical visa, tax, fare, or income number.

## State location

Tenerife planning or move context may exist in `<workspace>/tenerife/`,
`<workspace>/memory/tenerife/`, or `~/tenerife/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/tenerife/`, `<workspace>/memory/tenerife/`, `~/tenerife/`.
3. If none exists and the user wants planning context kept, create
   `<workspace>/tenerife/`.
4. If more than one candidate exists, use the highest-precedence directory and
   tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/tenerife/` only.
   Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Create
or update `<state_root>/memory.md` only when the user wants trip or move context
kept across sessions. Legacy `~/Clawic/data/tenerife/` is a migration source
only. Keep it out of the active lookup order, and move it only when the user asks.

This skill is primarily **routing knowledge**. Durable notes are optional.

```text
<state_root>/
└── memory.md     # role, zone preference, timeline, open decisions
```

Template: `assets/memory-template.md`. First-run intake: `references/setup.md`.

## When to load

Load for Tenerife **visitor**, **relocation**, **remote work**, or **local-life**
questions:

- 1/3/7-day itineraries, attractions, lodging zones, day trips
- north vs south fit (Santa Cruz, La Laguna, Puerto de la Cruz, Costa Adeje,
  El Médano, Los Cristianos / Las Américas)
- bus/tram vs car, mountain-road timing, TFN/TFS choice
- cost bands, settling checklist (NIE, empadronamiento, healthcare orientation)
- Spain Digital Nomad Visa / Canary IGIC / ZEC **orientation** (not filing)
- climate microzones and Teide day planning

Route away when the task is mainly:

- multi-country or multi-island trip systems → `travel` / `europe`
- hotel/flight booking ops → `booking` / `flight`
- Spanish language production → `spanish`
- generic housing search outside Tenerife → `housing`
- live visa filing for a specific passport → open current official pages and
  tell the user to confirm; do not invent thresholds from memory

Read `references/sources.md` before repeating rent bands, IGIC/ZEC rates, Digital
Nomad Visa income floors, bus fares, or emergency procedures as hard fact.
Re-check the official page before the user books non-refundable travel or relies
on a visa number.

## When to load references

Keep `SKILL.md` as the progressive-disclosure router. Load the smallest matching
file; skill package paths use `references/` (not `<state_root>`).

| Need | File |
|------|------|
| Verified source URLs (Gate 6) | `references/sources.md` |
| First-run preference intake | `references/setup.md` |
| Attractions | `references/visitor-attractions.md` |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` |
| Where to stay | `references/visitor-lodging.md` |
| Tips & day trips | `references/visitor-tips.md` |
| Zone comparison | `references/zones-index.md` |
| Santa Cruz & La Laguna | `references/zones-capital.md` |
| Puerto de la Cruz & North | `references/zones-north.md` |
| Los Cristianos & Las Américas | `references/zones-south-tourist.md` |
| Costa Adeje & La Caleta | `references/zones-south-upscale.md` |
| El Médano & Granadilla | `references/zones-southeast.md` |
| Choosing a zone | `references/zones-choosing.md` |
| Food overview | `references/food-overview.md` |
| Canarian cuisine | `references/food-local.md` |
| International dining | `references/food-international.md` |
| Dining areas | `references/food-areas.md` |
| Markets, wine, practical food | `references/food-practical.md` |
| Moving & settling | `references/resident.md` |
| Transport | `references/transport.md` |
| Cost of living | `references/cost.md` |
| Safety | `references/safety.md` |
| Climate & microclimates | `references/climate.md` |
| Local services (banking, NIE) | `references/local.md` |
| Digital nomad guide | `references/nomad.md` |
| Coworking & tech scene | `references/coworking.md` |
| ZEC & tax orientation | `references/tax.md` |
| Visas & residency orientation | `references/visas.md` |
| Culture | `references/culture.md` |
| Healthcare | `references/healthcare.md` |
| Schools & education | `references/education.md` |
| Expat & local lifestyle | `references/lifestyle.md` |
| Driving & car ownership | `references/driving.md` |
| Nature & outdoor | `references/nature.md` |
| Persisted context shape | `assets/memory-template.md` |

## Core rules

### 1. Identify user context first
- **Role**: tourist, digital nomad, retiree, family relocating, investor
- **Timeline**: short visit, planning to move, already there
- Load the matching reference only after role + timeline are clear

### 2. North vs south split
Tenerife has two distinct characters divided by Mount Teide:
- **South**: tourist-focused, sunnier year-round, beaches, resorts, nightlife
- **North**: greener, more local character, cultural centers, more cloud days
See zone files for neighborhood-level guidance.

### 3. EU / Schengen context (orientation only)
Tenerife is part of Spain and the EU, with Canary customs nuances:
- **EU/EEA citizens**: free movement; long stays still need local registration
  (empadronamiento + NIE orientation in `references/visas.md` / `references/local.md`)
- **Non-EU citizens**: visa path depends on passport and purpose; Spain Digital
  Nomad Visa is a common remote-work route — confirm live requirements
- **UK post-Brexit**: short-stay Schengen limits apply without a residence path
- Re-open official pages before stating stay windows or income floors

### 4. Canary special zone (ZEC / IGIC) — orientation
Business and consumer tax treatment differs from mainland Spain (ZEC corporate
regime; IGIC instead of mainland IVA). Treat package numbers as orientation and
confirm via `references/sources.md` + a qualified advisor before company setup.

### 5. Cost bands (directional, re-check before budgeting)
Published package bands (approx., mid-2020s orientation):

| Item | Band |
|------|------|
| 1BR rent (Santa Cruz) | €600–900/month |
| 1BR rent (Costa Adeje) | €800–1,200/month |
| Local salary orientation | €1,400–2,000/month |
| Remote worker spend (typical) | €2,500–6,000/month |
| Monthly groceries | €200–350/person |
| Coworking desk | €100–250/month |
| Private healthcare | €50–150/month |
| International school fees | €5,000–12,000/year |

Label these as **directional**. Listing sites and season move the real number.

### 6. Cost reality
Often lower than mainland Spain and much of Northern Europe for remote workers:
- **Housing**: main swing factor; nomad demand lifts El Médano / Costa Adeje
- **Groceries / dining**: local produce and menú del día keep food affordable
- **Transport**: fuel and buses relatively cheap; mountain time ≠ map distance
- **Healthcare**: public access via social security when eligible; private is common
- **Outdoors**: beach and many hikes are low-cost high-ROI

### 7. Climate zones
Microclimates matter more than the island average:
- **South coast**: dry, warm, reliable sun
- **North coast**: milder, greener, more humidity/cloud
- **High altitude**: alpine; Teide can have snow in winter
- **East / southeast**: windier; strong for water sports
See `references/climate.md` before packing or locking outdoor days.

### 8. Zone matching

| Profile | Strong starting areas |
|---------|------------------------|
| Digital nomads (social) | Costa Adeje, El Médano, La Laguna |
| Retirees | Puerto de la Cruz, Los Cristianos, Costa Adeje |
| Families | La Laguna, Santa Cruz, Adeje village |
| Budget-conscious | Santa Cruz, La Laguna, Granadilla |
| Beach lifestyle | El Médano, Los Cristianos, Playa de las Américas |
| Surf / kite | El Médano, La Tejita |
| Culture / authenticity | La Laguna (UNESCO), Puerto de la Cruz |
| Luxury | Costa Adeje, Abama, La Caleta |

## Digital nomad hub (summary)

Tenerife is a frequent remote-work base: mild winters, fiber in main towns, active
meetup scene, and Spain remote-work visa options. Load `references/nomad.md` and
`references/coworking.md` for base choice; load `references/visas.md` +
`references/sources.md` before any visa claim.

## Tenerife-specific traps

- **North weather assumptions** — cloud in the north with sun in the south is normal; drive 20 minutes before cancelling a day.
- **Generic south strips** — Las Américas / Los Cristianos can feel interchangeable; step inland or to local streets for character.
- **Driving time** — mountain roads are fine but slow; 30 km can take an hour.
- **Spanish bureaucracy pace** — NIE / empadronamiento / bank onboarding needs buffer (often weeks, not days).
- **August closures** — local businesses may pause while mainland Spain holidays.
- **Siesta hours** — many shops close mid-afternoon; plan errands around it.
- **Island time** — appointments drift; build slack.
- **Car dependency** — TITSA buses exist but outside main corridors a car wins.
- **Rent pressure** — popular nomad zones rose with demand; verify live listings.
- **Work status** — remote work still has tax/residency implications; autónomo and visa rules are not optional flavor text.

## Essential local knowledge

- **Language**: Spanish (Canarian accent). English common in tourist south; thinner in the north.
- **Tipping**: not mandatory; rounding up or ~5–10% for strong service is fine.
- **Meal times**: lunch often 14:00–16:00, dinner 21:00–23:00 (earlier in tourist zones).
- **Pharmacies**: green cross; rotating 24h duty.
- **Emergency**: 112 EU-wide; confirm local non-emergency numbers in `references/safety.md`.
- **Water**: tap is generally safe; many locals prefer bottled for taste (minerals).
- **Power**: 230V, Type C/F.

See `references/local.md` for settling detail.

## Failure modes

| Situation | Do this |
|-----------|---------|
| No role / timeline | Ask before locking a zone or multi-day plan |
| Visa / income floor question | Open live official source; do not paste stale package numbers as law |
| Booking-critical fare or ticket | Confirm operator site the same day |
| Multiple `<state_root>` candidates | Use highest precedence; report duplicates; do not merge silently |
| User wants multi-island hop | Hand off framing to `travel` / `europe` after Tenerife segment is clear |
