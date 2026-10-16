# Sources — travel skill

Last checked: 2026-10-17 (repair Gate 6; booking-critical claims still require a
live page check for the traveller's passport and dates).

## Schengen / EU short stay

- European Commission — Schengen border crossing:
  https://home-affairs.ec.europa.eu/policies/schengen/border-crossing_en (HTTP 200)
- European Commission — Visa policy:
  https://home-affairs.ec.europa.eu/policies/schengen/visa-policy_en (HTTP 200)
- EC short-stay calculator:
  https://ec.europa.eu/assets/home/visa-calculator/calculator.htm (HTTP 200)
- Travel Europe — ETIAS:
  https://travel-europe.europa.eu/etias_en (HTTP 200)
- Travel Europe — EES:
  https://travel-europe.europa.eu/ees_en (HTTP 200)

## Cash controls

- EUR-Lex — Regulation (EU) 2018/1672 (cash controls):
  https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32018R1672 (HTTP 202/200)
- FinCEN — history of AML / CTR framing (USD 10,000 context):
  https://www.fincen.gov/resources/history-anti-money-laundering-laws (HTTP 200)
- CBP — Travel hub (re-open traveler money pages in a browser before quoting forms):
  https://www.cbp.gov/travel (HTTP 200)

## Health

- WHO — Yellow fever Q&A:
  https://www.who.int/news-room/questions-and-answers/item/yellow-fever (HTTP 200)
- WHO — Yellow fever health topic:
  https://www.who.int/health-topics/yellow-fever (HTTP 200)

## Passport / general travel advice portals

- UK Government — Renew adult passport:
  https://www.gov.uk/renew-adult-passport/renew (HTTP 200)
- UK Government — Foreign travel advice hub:
  https://www.gov.uk/foreign-travel-advice (HTTP 200)
- IATA Timatic overview (carrier entry data products):
  https://www.iata.org/en/services/compliance/timatic/ (HTTP 200)

## Fetch gaps

- Several CBP deep links, Travel Europe `/en` home, some WHO news permalinks, and
  travel.state.gov URLs returned 403/404 to this automation UA. Keep the official
  hubs above and re-open destination MFA / CBP / WHO pages in a browser before
  stating nationality-specific visa outcomes, exact declaration forms, or
  vaccine certificate lifetimes for a given itinerary.
- Connection buffers and airport arrival times are operational heuristics, not
  statutes—prefer carrier MCT and airport guidance for the actual tickets.
