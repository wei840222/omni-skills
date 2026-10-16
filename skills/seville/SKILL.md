---
name: seville
description: >
  Navigate Seville for visitors, residents, tech workers, students, and
  entrepreneurs: neighborhoods, TUSSAM/metro/bike, costs, tapeo culture,
  flamenco authenticity, Semana Santa/Feria timing, extreme summer heat, and
  local services. Use for Seville stay, move, commute, or work-base decisions.
  Prefer `spain` for multi-city Spain routing, `travel`/`travel-planning` for
  generic trip systems, and `expat` for full cross-border move project tracking.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏛️"}'
  related-skills: '{"booking":"Lodging search and reservation completion after a Seville neighborhood base is chosen.","dubai":"Peer dense-city guide when comparing city-skill patterns.","expat":"Cross-border move project tracking beyond Seville neighborhood and settling advice.","spain":"Country-level multi-city Spain routing when Seville is only one stop.","spanish":"Everyday Spanish for menus, bookings, and on-the-ground talk.","travel":"Standing multi-destination travel records when Seville is one city among several.","travel-planning":"Day-by-day multi-city itineraries when the trip leaves Seville.","valencia":"Peer Andalusian/Spanish city guide for Valencia comparisons."}'
---

## State location

Seville continuity state may exist in `<workspace>/seville/`, `<workspace>/memory/seville/`, or `~/seville/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/seville/`, `<workspace>/memory/seville/`, `~/seville/`.
3. If several candidate directories exist, use only the highest-precedence one and report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create `<workspace>/seville/` by default.
5. If the host cannot supply `<workspace>`, read an existing `~/seville/` only; otherwise ask for a state root before creating data.

Use the selected `<state_root>` for every state operation in this invocation. Create or update `<state_root>/memory.md` only when the user wants context kept across sessions. Legacy `~/Clawic/data/seville/` is a migration source only—keep it out of active lookup; move only with explicit user consent (copy, validate, cutover).

Scripts and shell examples must receive the resolved filesystem path; never write the literal string `<state_root>` to disk.

Research notes and official source URLs live in `references/sources.md` (progressive disclosure).

## When to use

Use for **Seville (Sevilla city + metro area)** decisions: visit length and neighborhood base, relocation fit, TUSSAM/metro/bike routing, cost bands, safety street-smarts, tech/work base, visas and residency *orientation*, tapeo/food, flamenco authenticity, Semana Santa/Feria timing, climate survival, schools, healthcare orientation, and driving-in-city tradeoffs (including ZBE).

Do **not** use this skill as the sole source for a multi-city Spain itinerary (`spain`), a multi-country standing travel system (`travel`), generic day packing across cities (`travel-planning`), or a full move project board (`expat`).

Classify the user first: visitor, planning-to-move, already-resident, tech/remote worker, student, or entrepreneur. Ask only for the next missing detail that changes the recommendation (dates/month, budget currency, passport, kids, Spanish level, quiet vs nightlife priority).

## Reference routing

Load the smallest set that answers the current question. Prefer `references/sources.md` before booking-critical fare, entry, residency, or heat-risk claims.

| Topic | File | When to load |
| --- | --- | --- |
| Continuity setup | `references/setup.md` | User wants persistent Seville context or empty `<state_root>/` |
| Memory structure | `assets/memory-template.md` | Creating/updating `<state_root>/memory.md` after consent |
| Official source map | `references/sources.md` | Before booking-critical fares, entry rules, residency, or agency claims |
| Visitor attractions | `references/visitor-attractions.md` | Must-see vs skip lists |
| Visitor itineraries | `references/visitor-itineraries.md` | 1/3/7-day frames |
| Visitor lodging | `references/visitor-lodging.md` | Hotel/Airbnb neighborhood fit for short stays |
| Visitor tips | `references/visitor-tips.md` | Day trips, packing, practical visitor traps |
| Neighborhoods index | `references/neighborhoods-index.md` | Quick neighborhood comparison |
| Centro / Santa Cruz | `references/neighborhoods-centro.md` | Historic core bases |
| Triana | `references/neighborhoods-triana.md` | River / flamenco / local feel |
| La Macarena | `references/neighborhoods-macarena.md` | Value residential / northern edge |
| Nervión / Los Remedios | `references/neighborhoods-modern.md` | Modern / business / shopping bases |
| Choosing guide | `references/neighborhoods-choosing.md` | Profile → neighborhood matching |
| Food overview / tapeo | `references/food-overview.md` | Meal timing and social food culture |
| Traditional dishes | `references/food-traditional.md` | Local specialties |
| Tapas bars / areas | `references/food-tapas.md` | Bar routing |
| Markets / food halls | `references/food-markets.md` | Market shopping |
| Dietary / Ramadan notes | `references/food-practical.md` | Practical dietary constraints |
| Moving / settling | `references/resident.md` | Empadronamiento, NIE orientation, move-in |
| Transport | `references/transport.md` | Walk / bus / metro / bike / ZBE |
| Cost of living | `references/cost.md` | Rent and monthly budget orientation |
| Safety | `references/safety.md` | Petty theft + heat risk framing |
| Climate survival | `references/climate.md` | Extreme summer planning |
| Local services | `references/local.md` | Banks, SIM, admin surfaces |
| Tech / salaries | `references/tech.md` | Local tech scene orientation |
| Startups / coworking | `references/startup.md` | Coworking and startup hubs |
| Fiestas | `references/fiestas.md` | Semana Santa and Feria de Abril |
| Flamenco | `references/flamenco.md` | Authentic vs tourist tablao routing |
| Students | `references/student.md` | Universities and student life |

## Core rules

1. **Identify context first** — role, timeline, month, budget currency, passport, and Spanish level before locking a neighborhood or itinerary.
2. **Heat is a planning constraint** — June–September regularly hits 35–45°C; treat afternoon outdoor sightseeing as a heat-risk decision, not a default. Prefer morning outdoor blocks and indoor/rest windows 14:00–17:00. See `references/climate.md`.
3. **Tapeo is the social default** — many bars include a tapa with a drink; standing crowds often signal quality; lunch windows ~13:30–16:00 and dinner ~20:30–midnight. See `references/food-overview.md` and `references/food-tapas.md`.
4. **Treat money and legal tables as orientation** — rent, salary, fare, and fee ranges expire. Re-open the matching page in `references/sources.md` before non-refundable bookings or filings.
5. **Plan around civic festivals** — Semana Santa and Feria de Abril reshape lodging, noise, and access; book early and treat caseta access as invite-driven. See `references/fiestas.md`.
6. **Use Spanish schedules** — lunch often opens ~14:00; dinner commonly 21:00–23:00; nightlife later. Early openings are usually tourist-oriented.
7. **Prefer authentic flamenco routing** — Triana bars and peñas over Santa Cruz tourist tablaos when authenticity matters. See `references/flamenco.md`.
8. **Prefer transit or walking in Centro** — ZBE, tickets, and theft risk make street parking a poor default.

## Orientation ranges (verify live)

| Item | Orientation range |
| --- | --- |
| 1BR Centro rent | EUR 700–1,000 / month |
| 1BR outer rent | EUR 450–650 / month |
| Modest monthly total | EUR 1,200–1,600 |
| Comfortable monthly total | EUR 1,800–2,500 |
| Best visit months | Mar–May, Oct–Nov |
| Extreme heat months | Jul–Aug (often 40°C+) |

## Common planning upgrades

| Instead of | Prefer |
| --- | --- |
| Afternoon Alcázar / cathedral walk in July | Morning ticketed visit + indoor/rest window after lunch |
| Santa Cruz tourist tablao as “real flamenco” | Triana peña / local bar routing after asking taste and budget |
| Feria without a caseta plan | Local invite path or clear public-access expectations |
| Semana Santa weekend hotel booked late | Book 6+ months ahead or shift dates |
| Street parking in Centro | Walk, TUSSAM, metro, or park-and-walk outside ZBE |
| Assuming Seville is coastal | Plan Matalascañas (~1h+) as a separate beach trip |
| Renting a historic flat without checking AC | Confirm AC before summer leases |

## Comparing with other Spanish cities

| Axis | Seville | Madrid | Barcelona |
| --- | --- | --- | --- |
| Cost | Lower | Higher | Higher |
| Heat | Extreme summers | Hot but milder peaks | Hot + humid |
| Character | Traditional, festive | Cosmopolitan | Catalan, modern |

Seville is typically cheaper and more traditional than Madrid/Barcelona, with a strong local festival identity.

## Safety and honesty boundaries

- Do not invent nationality-specific visa outcomes; point to BOE / sede / consulate pages and licensed advisors.
- Do not treat packaged rent or salary tables as live quotes.
- Do not store passport numbers, full NIE/TIE, bank credentials, or card numbers in `<state_root>/`.
- Prefer official Visitasevilla / Spain.info / AEMET / BOE pages over secondary listicles for schedules, weather, and residency orientation.
