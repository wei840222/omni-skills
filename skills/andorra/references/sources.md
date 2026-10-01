# Sources — Andorra

Gate 6 research anchors. Prefer these official pages over memory when facts may drift (lift status, spa hours, road rules, telecom products).

## Official tourism and government

| Source | Use for | URL |
|--------|---------|-----|
| Visit Andorra (tourism board) | Parish overviews, events, seasonal ideas | https://visitandorra.com/en/ |
| Govern d'Andorra | Official government entry point | https://www.govern.ad/ |

## Mountain resorts

| Source | Use for | URL |
|--------|---------|-----|
| Grandvalira | Ski domain, summer mountain, Canillo/Encamp side | https://www.grandvalira.com/en |
| Pal Arinsal | Ski + bike, La Massana side | https://palarinsal.com/en |

## Transport, connectivity, wellness

| Source | Use for | URL |
|--------|---------|-----|
| Mobilitat Andorra | Traffic and road conditions | https://www.mobilitat.ad/ |
| Andorra Telecom | Local connectivity / roaming context | https://www.andorratelecom.ad/ |
| Caldea | Flagship spa planning in Escaldes | https://www.caldea.com/en/ |

## Verification notes (handoff 2026-10-02)

- Confirmed HTTP 200: Visit Andorra, Grandvalira, Pal Arinsal, Mobilitat, Govern, Caldea (Caldea via GET).
- Andorra Telecom HEAD timed out from this runner; keep URL as the canonical operator homepage and treat product details as user-verified at booking time.
- Live weather, live queue length, and live lift openings are **not** embedded in this skill—point users at the sources above plus their apps.

## Domain corrections applied in this refactor

- Replaced hard-coded `~/Clawic/data/andorra/` with portable `<state_root>` resolution.
- Removed clawic.com homepage / star / feedback CTAs.
- Restated roaming as “often excluded from EU packages,” not a guarantee of any single carrier policy.
- Kept parish guidance qualitative; no invented lift-pass prices or unverifiable 2026 tariffs.
