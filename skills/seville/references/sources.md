# Sources — Seville skill

Last bulk-checked: 2026-10-16 (handoff). Booking-critical fare, visa, fee, and listing claims still require a live page check at answer time.

## Tourism and city orientation

- Visitasevilla (EN): https://www.visitasevilla.es/en (HTTP 200)
- Spain.info — Seville destination: https://www.spain.info/en/destination/seville/ (HTTP 200)
- AENA — Sevilla Airport: https://www.aena.es/en/sevilla.html (HTTP 200)

## Weather

- AEMET Sevilla forecast: https://www.aemet.es/en/eltiempo/prediccion/municipios/sevilla-id41091 (HTTP 200)

## Housing search surfaces (not escrow)

- Fotocasa Sevilla rentals: https://www.fotocasa.es/es/alquiler/viviendas/sevilla-capital/todas-las-zonas/l (HTTP 200)
- Idealista often blocks automated fetches (HTTP 403 from this runner); still a common human search surface — verify live in a browser when quoting rents.

## Transit operators (automation often blocked)

- TUSSAM / municipal bus surfaces frequently return HTTP 403 or timeout from this runner — treat packaged euro fares as orientation and re-open operator sites before trip-critical budgets.
- Seville Metro overview (secondary orientation): https://en.wikipedia.org/wiki/Seville_Metro (HTTP 200)
- Renfe pages frequently return HTTP 403 from this runner; confirm rail fares in a browser before booking.

## Immigration / residency orientation (Spain)

- BOE — international telework / Digital Nomad framework text: https://www.boe.es/buscar/doc.php?id=BOE-A-2022-21739 (HTTP 200)
- Sede — public administrations directory / NIE entry: https://sede.administracionespublicas.gob.es/ (HTTP 200)
- Some sevilla.org / policia.es / renfe.com paths timed out or returned 403 from this runner; mark those claims unverified until a browser session opens the live product page for the user's passport.

## Agent Skills specification

- Document index: https://agentskills.io/llms.txt (HTTP 200)
- Specification: https://agentskills.io/specification (HTTP 200)
- Reference validator package: https://github.com/agentskills/agentskills/tree/main/skills-ref

## Notes for agents

- Treat rent, salary, fare, and fee tables in this skill as orientation ranges, not live quotes.
- For immigration, licensing, or tax filings, point to the official agency page and licensed professionals; do not act as counsel.
- Prefer Visitasevilla / Spain.info / AEMET / BOE / sede pages over secondary listicles when schedules, residency, or weather matter.
