# Sources — Portugal

Gate 6 research anchors. Prefer these official pages over memory when facts may drift (timetables, cards, safety numbers, tourism guidance).

## Official tourism and government

| Source | Use for | URL |
|--------|---------|-----|
| Visit Portugal (Turismo de Portugal) | National tourism framing, regions, practical travel | https://www.visitportugal.com/en |
| República Portuguesa — government portal | Government services entry points | https://www.portugal.gov.pt/en/gc25 |
| Lisboa Official Tourism | Neighborhoods, cards, events framing | https://www.visitlisboa.com/en |
| Porto Official Tourism | City tips, experiences | https://visitporto.travel/en-GB |

## Transport

| Source | Use for | URL |
|--------|---------|-----|
| CP — Comboios de Portugal | Train products, Alfa Pendular / Intercidades | https://www.cp.pt/passageiros/en |
| Metropolitano de Lisboa | Lisbon metro | https://www.metrolisboa.pt/en/ |
| CARRIS | Lisbon buses/trams | https://www.carris.pt/en/ |
| Rede Expressos | Long-distance coaches (site may bot-block some clients; still canonical operator) | https://www.rede-expressos.pt/ |
| Oceanário de Lisboa | Flagship family attraction hours/tickets | https://www.oceanario.pt/en/ |
| ANA Aeroportos | Airport operator orientation | https://www.ana.pt/ |
| Aeroporto de Lisboa | Lisbon airport traveler info | https://www.aeroportolisboa.pt/en |

## Safety and emergencies

| Source | Use for | URL |
|--------|---------|-----|
| Your Europe — Emergency | EU 112 framing for travelers | https://europa.eu/youreurope/citizens/travel/security-and-emergencies/emergency/index_en.htm |

## Verification notes (handoff 2026-10-02)

- Confirmed HTTP 200 from this runner: Visit Portugal, Portugal.gov, Visit Lisboa, Visit Porto, CP, Metro Lisboa, CARRIS, Oceanário, ANA, Aeroporto de Lisboa, Your Europe emergency page, Segurança Social homepage.
- Rede Expressos homepage is the canonical coach operator URL; some automated clients receive HTTP 403—treat product details as user-verified at booking time.
- Metro do Porto hostname was TLS-unstable from this runner; keep qualitative Porto metro guidance and tell users to confirm on the operator site when booking. ANA / Aeroporto de Lisboa verified 200.
- Navegante / former Viva Viagem naming can drift—direct users to current Lisbon operator pages before purchase advice solidifies.
- Live weather, ferry disruptions, and ticket inventory are **not** embedded—point users at sources above plus `references/apps.md`.

## Domain corrections applied in this refactor

- Replaced hard-coded `~/Clawic/data/portugal/` with portable `<state_root>` resolution.
- Removed clawic.com homepage / star / feedback CTAs and `_meta.json`.
- Moved guides under `references/` and memory template under `assets/`.
- Kept restaurant and fare anecdotes as experiential priors; user should re-check hours/prices at booking time.
