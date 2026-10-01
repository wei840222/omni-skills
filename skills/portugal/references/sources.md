# Sources — Portugal

Gate 6 research anchors. Prefer these official pages over memory when facts may drift (timetables, cards, safety numbers, tourism guidance).

## Official tourism and government

| Source | Use for | URL |
|--------|---------|-----|
| Visit Portugal (Turismo de Portugal) | National tourism framing, regions, practical travel | https://www.visitportugal.com/en |
| República Portuguesa — Portal do Cidadão / gov entry | Government services entry points | https://www.portugal.gov.pt/en/gc25 |
| Segurança Social / citizen services context | High-level public service orientation (not benefits advice) | https://www.seg-social.pt/ |

## Transport

| Source | Use for | URL |
|--------|---------|-----|
| CP — Comboios de Portugal | Train products, Alfa Pendular / Intercidades | https://www.cp.pt/passageiros/en |
| Rede Expressos | Long-distance coaches | https://www.rede-expressos.pt/en |
| Metropolitano de Lisboa | Lisbon metro | https://www.metrolisboa.pt/en/ |
| CARRIS | Lisbon buses/trams | https://www.carris.pt/en/ |
| Metro do Porto | Porto metro | https://www.metrodoporto.pt/ |
| ANA Aeroportos | Airport orientation | https://www.ana.pt/en |

## City / region tourism

| Source | Use for | URL |
|--------|---------|-----|
| Lisboa Official Tourism | Neighborhoods, cards, events framing | https://www.visitlisboa.com/en |
| Porto Official Tourism | City tips, experiences | https://visitporto.travel/en-GB |
| Centro de Ciência Viva / Oceanário context via city guides | Family attractions (verify hours on venue site) | https://www.oceanario.pt/en/ |

## Safety and emergencies

| Source | Use for | URL |
|--------|---------|-----|
| European emergency number context | 112 framing | https://european-union.europa.eu/live-work-study/emergency-number-112_en |
| PSP — Polícia de Segurança Pública | Public security orientation | https://www.psp.pt/ |

## Verification notes (handoff 2026-10-02)

- Prefer official operator pages for cards, fares, and hours; skill text keeps qualitative prices only as planning priors, not live quotes.
- Navegante / former Viva Viagem naming can drift—direct users to current Lisbon operator pages before purchase advice solidifies.
- Live weather, ferry disruptions, and ticket inventory are **not** embedded—point users at sources above plus `references/apps.md`.

## Domain corrections applied in this refactor

- Replaced hard-coded `<state_root>/` with portable `<state_root>` resolution.
- Removed clawic.com homepage / star / feedback CTAs and `_meta.json`.
- Moved guides under `references/` and memory template under `assets/`.
- Kept restaurant and fare anecdotes as experiential priors; user should re-check hours/prices at booking time.
