---
name: buenos-aires
description: >
  Navigate Buenos Aires as a visitor, resident, tech worker, student, or
  entrepreneur: neighborhoods, transport (SUBE/subte), costs and money friction,
  safety, visas/residency paths, food, climate, and local services. Use for
  CABA-specific stay, move, commute, or work-base decisions. Prefer `argentina`
  for multi-region country routing, `travel`/`travel-planning` for generic trip
  systems, and `expat` for full cross-border move project tracking.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🇦🇷"}'
  related-skills: '{"argentina":"Country-level macro-region routing when Buenos Aires is only one stop.","booking":"Lodging search, total-cost comparison, and reservation completion after a barrio base is chosen.","expat":"Cross-border move project tracking beyond CABA neighborhood and settling advice.","spanish":"Rioplatense and everyday Spanish for menus, bookings, and on-the-ground talk.","travel":"Standing multi-destination travel records when BA is one city among several.","travel-planning":"Day-by-day multi-city itineraries when the trip leaves Buenos Aires."}'
---

## State location

Buenos Aires continuity state may exist in `<workspace>/buenos-aires/`, `<workspace>/memory/buenos-aires/`, or `~/buenos-aires/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/buenos-aires/`, `<workspace>/memory/buenos-aires/`, `~/buenos-aires/`.
3. If several candidate directories exist, use only the highest-precedence one and report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create `<workspace>/buenos-aires/` by default.
5. If the host cannot supply `<workspace>`, read an existing `~/buenos-aires/` only; otherwise ask for a state root before creating data.

Use the selected `<state_root>` for every state operation in this invocation. Create or update `<state_root>/memory.md` only when the user wants context kept across sessions. Legacy `~/Clawic/data/buenos-aires/` is a migration source only—keep it out of active lookup; move only with explicit user consent (copy, validate, cutover).

## When to use

Use for **Buenos Aires (CABA and adjacent AMBA context)** decisions: visit length and barrio base, relocation neighborhood fit, SUBE/subte/colectivo routing, cost and payment friction, safety street-smarts, tech/work base, visas and residency *orientation*, food and climate, schools, healthcare orientation, and driving-in-city tradeoffs.

Do **not** use this skill as the sole source for a multi-region Argentina itinerary (`argentina`), a multi-country standing travel system (`travel`), generic day packing across cities (`travel-planning`), or a full move project board (`expat`).

Classify the user first: visitor, planning-to-move, already-resident, tech/remote worker, student, or entrepreneur. Ask only for the next missing detail that changes the recommendation (dates/month, budget currency, passport, kids, Spanish level, work-from-home vs office).

## Reference routing

| Topic | File | When to load |
| --- | --- | --- |
| Continuity setup | `references/setup.md` | User wants persistent BA context or empty `<state_root>/` |
| Memory structure | `assets/memory-template.md` | Creating/updating `<state_root>/memory.md` after consent |
| Core rules, traps, context | `references/domain.md` | First substantive answer; always for money/season/visa framing |
| Official source map | `references/sources.md` | Before booking-critical fares, entry rules, residency, or agency claims |
| Visitor attractions | `references/visitor-attractions.md` | Must-see vs skip lists |
| Visitor itineraries | `references/visitor-itineraries.md` | 1/3/7-day frames |
| Visitor lodging | `references/visitor-lodging.md` | Hotel/Airbnb barrio fit for short stays |
| Visitor tips | `references/visitor-tips.md` | Day trips, packing, practical visitor traps |
| Neighborhoods index | `references/neighborhoods-index.md` | Quick barrio comparison |
| Norte (Palermo, Belgrano, Núñez) | `references/neighborhoods-norte.md` | Those barrios |
| Centro (Microcentro, San Nicolás, Retiro) | `references/neighborhoods-centro.md` | Centro / Retiro |
| Sur (San Telmo, La Boca, Barracas) | `references/neighborhoods-sur.md` | Southern barrios; La Boca safety nuance |
| Oeste (Caballito, Almagro, Villa Crespo) | `references/neighborhoods-oeste.md` | West / value barrios |
| Premium (Puerto Madero, Recoleta) | `references/neighborhoods-premium.md` | Premium bases |
| Choosing guide | `references/neighborhoods-choosing.md` | Profile → barrio matching |
| Food overview | `references/food-overview.md` | Dining scene map |
| Local cuisine | `references/food-local.md` | Asado, parrilla, cafés |
| International / fine dining | `references/food-international.md` | Non-Argentine options |
| Food areas | `references/food-areas.md` | Where to eat by barrio |
| Food practical | `references/food-practical.md` | Dietary, tipping, cubierto |
| Moving & settling | `references/resident.md` | Contracts, utilities, everyday resident life |
| Transport | `references/transport.md` | Subte, colectivos, taxis, SUBE |
| Cost of living | `references/cost.md` | Rent bands and monthly budgets (ranges, not live quotes) |
| Safety | `references/safety.md` | Street crime patterns and area awareness |
| Climate | `references/climate.md` | Season, heating/cooling reality |
| Local services | `references/local.md` | Banking, SIM, paperwork orientation |
| Tech industry | `references/tech.md` | Salaries, remote work, offices |
| Business setup | `references/business.md` | Company formation orientation |
| Visas & residency | `references/visas.md` | Tourist stay, DN, residency paths (verify passport) |
| Startups | `references/startup.md` | Ecosystem and funding orientation |
| Culture | `references/culture.md` | Customs, timing, social norms |
| Healthcare | `references/healthcare.md` | Prepaga / public orientation |
| Education | `references/education.md` | Schools and universities orientation |
| Lifestyle | `references/lifestyle.md` | Expat social life |
| Driving | `references/driving.md` | Car ownership vs city transit |

## Core workflow

1. **Lock context.** Role, month, length of stay, passport (for entry only), budget currency (USD vs ARS earner), Spanish comfort, and whether kids or office commute matter.
2. **Answer the immediate question first.** Then load the smallest reference set from the table—do not dump every file.
3. **Money before bookings.** Argentina payment and FX rules change. Prefer durable frameworks (card + some ARS cash friction, avoid treating old “blue dollar blog math” as current law). Re-open `references/sources.md` and official pages before non-refundable flights, multi-month leases, or residency filings.
4. **Barrio from routine, not hype.** Match late-night return path, commute, noise tolerance, and budget—not Instagram labels. For La Boca, Caminito daytime tourist pocket ≠ whole barrio at night.
5. **Entry is passport-specific.** Tourist stay windows and visa needs vary. Orient with `references/visas.md`, then verify on Migraciones for that nationality and travel date.
6. **Persist only with consent.** Follow `references/setup.md`; never store passport numbers, bank credentials, or full address dumps in chat logs meant for reuse.

## Core rules (durable)

1. Identify role and timeline before neighborhood or cost advice.
2. Separate **headline USD blog prices** from **what the user can actually pay with** (foreign card, local account, cash). Mark stale FX anecdotes.
3. January often empties the city; many locals leave—plan services around it.
4. Winter apartments are often under-heated; pack for indoor cold, not just outdoor °C.
5. Prefer SUBE + walking + ride-hail inside dense CABA; cars are usually a liability for city-only stays.
6. Phone-snatch and distraction theft are the dominant tourist risks—conceal devices, avoid flashing wealth at ATMs.
7. Spanish helps outside Palermo/tourist bubbles; do not assume English everywhere.
8. For multi-province trips, hand off routing to `argentina` after the BA city block is set.

## Prefer these patterns

- Re-check payment rails near travel; treat dual-rate blog posts as historical color only.
- Visit La Boca as a daylight Caminito pocket with a clear exit plan.
- For short culture trips, prefer walkable Recoleta/Palermo/San Telmo bases over isolated towers unless the user wants that quiet.
- For multi-province routes, finish the CABA block here then hand off to `argentina`.
- Before long rentals, map contrato type, deposit custom, and how rent adjusts with inflation.
- Verify tourist stay and residency products per passport on Migraciones.
- Quote Subte fares and agency fees only from live official pages (or mark unverified).

## Safety and privacy

- Advise; do not claim real-time crime maps or guarantee neighborhood safety block-by-block.
- No live network actions, bookings, or government filings without explicit user instruction.
- Keep credentials, passport images, CUIT/CUIL, and payment secrets out of `<state_root>/`.
- Mark unverified mutable facts clearly when official pages cannot be opened.

## Source freshness

Package orientation was bulk-aligned on 2026-10-14 against the URL map in `references/sources.md`. Before any booking-critical or legal claim, open the matching official page again for the user's passport and travel month.
