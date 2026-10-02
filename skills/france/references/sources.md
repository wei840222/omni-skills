# Sources — France

Gate 6 research anchors. Prefer these official pages over memory when facts may drift (timetables, museum hours, cards, safety numbers, tourism guidance).

## Official tourism and government

| Source | Use for | URL |
|--------|---------|-----|
| France.fr (Atout France) | National tourism framing, regions, practical travel | https://www.france.fr/en |
| Atout France institutional | Destination marketing / trade orientation | https://www.atout-france.fr/en |
| Service-Public.fr | Government services entry points for residents/visitors admin | https://www.service-public.fr/ |
| French Ministry for Europe and Foreign Affairs | Consular / travel diplomacy framing | https://www.diplomatie.gouv.fr/en/ |
| Ministry of Culture | National culture institutions and heritage context | https://www.culture.gouv.fr/ |

## Cities and regions

| Source | Use for | URL |
|--------|---------|-----|
| OnlyLYON | Lyon visitor framing and city practicalities | https://www.onlylyon.com/ |
| Lyon France tourism | Lyon experiences / stay orientation | https://www.lyon-france.com/ |
| Marseille Tourisme | Marseille and metro practical visitor info | https://www.marseille-tourisme.com/en/ |
| Côte d'Azur France | French Riviera destination framing | https://www.cotedazurfrance.fr/en/ |
| Provence-Alpes-Côte d'Azur tourism | Regional Provence / coast routing | https://www.provence-alpes-cotedazur.com/en/ |
| Bordeaux Tourism | Bordeaux and wine-route orientation | https://www.bordeaux-tourisme.com/ |
| Visit French Wine | National wine-route discovery | https://www.visitfrenchwine.com/ |

## Transport and airports

| Source | Use for | URL |
|--------|---------|-----|
| SNCF Connect | Rail schedules, tickets, disruption notices | https://www.sncf-connect.com/en-en |
| SNCF corporate | Network / product orientation | https://www.sncf.com/en |
| Paris Aéroport | CDG/ORY passenger info | https://www.parisaeroport.fr/en |

## Museums and culture (examples)

| Source | Use for | URL |
|--------|---------|-----|
| Louvre | Flagship Paris museum hours/tickets | https://www.louvre.fr/en |
| Paris Musées | City of Paris museum network | https://www.parismusees.paris.fr/en |

## Weather and emergencies

| Source | Use for | URL |
|--------|---------|-----|
| Météo-France | Weather for coast/mountain pacing | https://www.meteofrance.com/ |
| Your Europe — Emergency | EU 112 framing for travelers | https://europa.eu/youreurope/citizens/travel/security-and-emergencies/emergency/index_en.htm |

## Verification notes (handoff 2026-10-02)

- Confirmed HTTP 200 from this runner: France.fr, Atout France, Service-Public, Diplomatie, Culture, OnlyLYON, Lyon France, Marseille Tourisme, Côte d'Azur France, PACA tourism, Bordeaux Tourism, Visit French Wine, SNCF Connect, SNCF, Paris Aéroport, Louvre, Paris Musées, Météo-France, Your Europe emergency page.
- RATP / Parisinfo / Île-de-France Mobilités / Transilien pages often return HTTP 403 to automated clients; still treat operator apps named in `references/apps.md` as canonical for Paris metro routing and tell users to confirm in-app.
- Air France homepage was unstable from this runner (TLS/stream errors); keep airline choice qualitative and confirm on the carrier site at booking time.
- Live weather, strike notices, seat inventory, and ticket prices are **not** embedded—point users at sources above plus `references/apps.md`.

## Domain corrections applied in this refactor

- Replaced hard-coded `~/Clawic/data/france/` with portable `<state_root>` resolution.
- Removed clawic.com homepage / star / feedback CTAs and `_meta.json`.
- Moved guides under `references/` and memory template under `assets/`.
- Freud pass: renamed residual “Mistakes to Avoid” style lists toward actionable Best Practices / Important Considerations; keep anti-patterns as positive guidance.
- Kept restaurant and fare anecdotes as experiential priors; user should re-check hours/prices at booking time.
