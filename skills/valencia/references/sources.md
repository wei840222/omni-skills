# Sources — Valencia skill

Last bulk-checked: 2026-10-16 (handoff). Booking-critical fare, visa, fee, and listing claims still require a live page check at answer time.

## Tourism and city orientation

- Visit Valencia: https://www.visitvalencia.com/en
- Visit Valencia — what to do: https://www.visitvalencia.com/en/what-to-do-valencia
- Spain.info — Valencia destination: https://www.spain.info/en/destination/valencia/
- Fallas / festival orientation: https://www.fallas.com/

## Weather

- AEMET Valencia forecast: https://www.aemet.es/en/eltiempo/prediccion/municipios/valencia-id46250
- AEMET Valencia (ES): https://www.aemet.es/es/eltiempo/prediccion/municipios/valencia-id46250

## Housing search surfaces (not escrow)

- Fotocasa Valencia rentals: https://www.fotocasa.es/es/alquiler/viviendas/valencia-capital/todas-las-zonas/l
- Idealista often blocks automated fetches (HTTP 403 from this runner); still a common human search surface — verify live in a browser when quoting rents.

## Transit operators (automation often times out)

- Valenbisi home: https://www.valenbisi.es/ (HTTP 200 intermittently; retry in browser if timeout)
- Metrovalencia / FGV / EMT pages frequently timed out or blocked from this runner — treat packaged euro fares as orientation and re-open operator sites before trip-critical budgets.

## Immigration / residency orientation (Spain)

- BOE — international telework / Digital Nomad framework text: https://www.boe.es/buscar/doc.php?id=BOE-A-2022-21739
- BOE plain text mirror: https://www.boe.es/diario_boe/txt.php?id=BOE-A-2022-21739
- Sede — public administrations directory / NIE entry: https://sede.administracionespublicas.gob.es/
- Social Security portal: https://www.seg-social.es/
- Ministerio de Asuntos Exteriores home: https://www.exteriores.gob.es/es/Paginas/index.aspx
- Some inclusion.gob.es / policia.es / renfe.com paths returned HTTP 403/404 from this runner; mark those claims unverified until a browser session opens the live product page for the user's passport.

## Notes for agents

- Treat rent, salary, fare, and fee tables in this skill as orientation ranges, not live quotes.
- For immigration, licensing, or tax filings, point to the official agency page and licensed professionals; do not act as counsel.
- Prefer Visit Valencia / BOE / sede / AEMET pages over secondary listicles when schedules, residency, or weather matter.
- Record fetch gaps plainly (timeout/403) instead of inventing current metro or DN fee numbers.
