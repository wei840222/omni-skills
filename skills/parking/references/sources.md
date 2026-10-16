# Official Source Pins — Parking

Verified during the 2026-10-16 handoff. Prefer these live URLs over remembered
hostnames. Bot-mitigated or 4xx/403 hosts remain discovery clues only until an
authenticated session confirms them.

## Specification and format

| Source | Verified | Notes |
|--------|----------|-------|
| https://agentskills.io/specification | HTTP 200 | Agent Skills normative format used for Gate 1 |

## Discovery and maps

| Source | Verified | Notes |
|--------|----------|-------|
| https://maps.google.com/ | HTTP 200 → Google Maps | Discovery / navigation handoff |
| https://maps.apple.com/ | HTTP 200 | Discovery / navigation handoff |
| https://business.parkopedia.com/ | HTTP 200 → `/home` | Commercial Parkopedia surface; consumer `parkopedia.com` returned 403 to plain curl |
| https://www.bestparking.com/ | HTTP 200 | Bookable-inventory comparison layer in supported markets |

## North America reservation / payment

| Source | Verified | Notes |
|--------|----------|-------|
| https://spothero.com/ | HTTP 200 | Reservation-first US marketplace |
| https://www.parkwhiz.com/ | HTTP 200 | Reservation marketplace |
| https://developer.parkwhiz.com/ | HTTP 200 | Public developer docs; `api.parkwhiz.com` redirects here. Older `parking.dev` hostname did not resolve |
| https://www.parkmobile.io/ | HTTP 200 | Municipal payment + some reservation flows |

## UK / Europe

| Source | Verified | Notes |
|--------|----------|-------|
| https://www.justpark.com/ | HTTP 200 | UK driveway / venue marketplace |
| https://ringgo.co.uk/ | HTTP 200 | UK payment-first city parking |
| https://www.q-park.co.uk/ | HTTP 200 | Operator pre-book / native flows |
| https://www.apcoaconnect.com/ | HTTP 200 | Operator payment / booking |
| https://www.paybyphone.com/ | HTTP 200 | Multi-country payment app |
| https://www.easypark.com/ | HTTP 200 → country site | Europe-heavy payment coverage |
| https://parclick.com/ | HTTP 200 | Southern Europe reservations |
| https://www.onepark.co/ | HTTP 200 | France-centered reservations |

## APAC / Middle East / India

| Source | Verified | Notes |
|--------|----------|-------|
| https://www.parking.sg/ | HTTP 200 | Singapore public-space payment |
| https://www.secureparking.com.au/ | HTTP 200 | ANZ operator booking |
| https://www.wilsonparking.com.au/ | HTTP 200 | ANZ operator booking |
| https://www.rta.ae/ | HTTP 200 | Dubai / UAE city parking authority surface |
| https://parkplus.io/ | HTTP 200 | India-focused parking / car services |
| https://data.gov.hk/en/ | HTTP 200 | Hong Kong government data portal entry; specific vacancy dataset slugs 404'd under the older `hk-td-tis_12-*` paths — re-search the portal before claiming a live occupancy API |

## Maintenance

When a host returns bot-mitigation 403/4xx to automation, keep the brand as a
discovery clue, record the failure mode here, and require a user-visible browser
or authenticated check before treating inventory as confirmed.
