# Sources — Finland Skill

Last checked: 2026-10-16 (repair re-verify pass; booking-critical claims still require live page check)

## Entry, Visa, and Borders

- Finnish Ministry for Foreign Affairs — entering Finland: https://um.fi/entering-finland (HTTP 200)
- EU Travel to Europe portal (home): https://travel-europe.europa.eu/ (HTTP 200)
- ETIAS overview on Travel Europe: https://travel-europe.europa.eu/en/etias (HTTP 200)
- EES overview on Travel Europe: https://travel-europe.europa.eu/en/ees (HTTP 200)
- European Commission Entry/Exit System policy page: https://home-affairs.ec.europa.eu/policies/schengen/smart-borders/entry-exit-system_en (HTTP 200)
- Finland Abroad portal (embassy network home): https://finlandabroad.fi/etusivu (HTTP 200; visa deep links may 404—navigate from the country page rather than a cached path)
- Finnish Immigration Service (Migri): https://migri.fi/en/coming-to-finland (HTTP 403 to this automation runner — open in a browser before quoting visa products)
- Finnish Border Guard: https://raja.fi/en/frontpage (HTTP 403 to automation — open in a browser before quoting border status)
- Finnish Government eastern-border update (example notice): https://valtioneuvosto.fi/en/-/1410869/finland-closes-the-crossing-points-on-the-eastern-border-and-centralises-the-receipt-of-applications-for-international-protection (HTTP 403 to automation — confirm current status in a browser)

## Customs, Airport, and Consumer Basics

- Finnish Customs traveller guidance: https://tulli.fi/en/private-persons/travelling (HTTP 403 to automation)
- Finnish Customs foodstuffs guidance: https://tulli.fi/en/private-persons/travelling/foodstuffs (HTTP 403 to automation)
- Finnish Customs cash declaration: https://tulli.fi/en/private-persons/travelling/cash (HTTP 403 to automation)
- Finavia Helsinki Airport hub: https://www.finavia.fi/en/airports/helsinki-airport (HTTP 200; older `/services/security-control` path returned 404)

## Transport and Tickets

- VR trains and night trains: https://www.vr.fi/en (HTTP 200)
- Matkahuolto national bus and ticket network: https://www.matkahuolto.fi/en (HTTP 200)
- Fintraffic traffic situation and road conditions: https://www.fintraffic.fi/en (HTTP 200)
- HSL Helsinki region transport: https://www.hsl.fi/en (HTTP 403 to automation — open in a browser before quoting zones or fares)
- Visit Finland home / planning portal: https://www.visitfinland.com/en/ (HTTP 200; older `/practical-tips/getting-around-in-finland/` path returned 404)

## Weather, Alerts, and Safety

- Finnish Meteorological Institute weather: https://en.ilmatieteenlaitos.fi/ (HTTP 200)
- FMI warnings: https://en.ilmatieteenlaitos.fi/warnings (HTTP 200)
- 112 Suomi emergency services: https://112.fi/en (HTTP 403 to automation)
- Luontoon national parks guidance: https://www.luontoon.fi/en (HTTP 200)
- Luontoon destinations index: https://www.luontoon.fi/en/destinations (HTTP 200)

## Regional and Trip Planning

- MyHelsinki official city guide: https://www.myhelsinki.fi/en (HTTP 200; redirects to `/`)
- Visit Rovaniemi: https://www.visitrovaniemi.fi/ (HTTP 200)
- Visit Tampere: https://visittampere.fi/en/ (HTTP 200)
- Visit Turku (English): https://en.visitturku.fi/ (HTTP 200; `visitturku.fi/en` redirects here)

## Fetch gaps / obsolete handling

- Migri, Border Guard, Customs, HSL, 112, and some valtioneuvosto pages returned HTTP 403 to this automation UA. Keep those URLs as official destinations, but re-open them in a browser before quoting thresholds, fares, or current border status.
- Finland Abroad visa deep link `.../web/eng/visa-to-visit-finland` returned HTTP 404; start from https://finlandabroad.fi/etusivu or https://um.fi/entering-finland instead of a cached path.
- Finavia security-control deep link and Visit Finland “getting around” article returned HTTP 404; use the Helsinki Airport hub and Visit Finland home until a replacement article is confirmed.
- Schengen day counts, EES/ETIAS applicability, and nationality-specific visa outcomes are orientation only until re-checked for the traveler’s passport and travel date.
