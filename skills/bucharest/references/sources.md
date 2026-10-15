# Sources — Bucharest skill

Last bulk-checked: 2026-10-16 (handoff). Booking-critical fare, visa, fee, and listing claims still require a live page check at answer time.

## Tourism and city orientation

- Romania Tourism — Bucharest: https://romaniatourism.com/bucharest.html (HTTP 200)
- Romania Tourism home: https://romaniatourism.com/ (HTTP 200)
- bucharest.ro city portal: https://www.bucharest.ro/ (HTTP 200)
- In Your Pocket — Bucharest: https://www.inyourpocket.com/bucharest (HTTP 200; redirects to romania/bucharest)
- Lonely Planet — Bucharest destination: https://www.lonelyplanet.com/romania/bucharest (HTTP 200)

## Transit operators

- STB (surface transit; formerly RATB branding still redirects): https://www.stb.ro/ (HTTP 200)
- STB English: https://www.stb.ro/en/ (HTTP 200)
- Legacy RATB redirect: https://ratb.ro/ (HTTP 200 → stb)
- Metrorex pages frequently timed out from this runner — treat packaged metro fares as orientation and re-open the operator site in a browser before trip-critical budgets. Background context only: https://en.wikipedia.org/wiki/Bucharest_Metro (HTTP 200)

## Immigration / residency orientation

- Inspectoratul General pentru Imigrări (IGI) EN: https://igi.mai.gov.ro/en/ (HTTP 200)
- Ministry of Internal Affairs EN: https://www.mai.gov.ro/en/ (HTTP 200)
- MAI press category (policy signals): https://www.mai.gov.ro/en/category/comunicate-de-presa/ (HTTP 200)
- EU Home Affairs — Schengen visa policy: https://home-affairs.ec.europa.eu/policies/schengen/visa-policy_en (HTTP 200)
- UK FCDO Romania travel advice: https://www.gov.uk/foreign-travel-advice/romania (HTTP 200)
- EURAXESS Romania (researcher mobility): https://www.euraxess.gov.ro/ (HTTP 200)
- MAE / eVisa paths often returned HTTP 503 or connection resets from this runner — mark entry-product claims unverified until a browser session opens the live MAE page for the user's passport.

## Tax / banking / money

- ANAF (tax authority): https://www.anaf.ro/ (HTTP 200)
- Banca Națională a României: https://www.bnr.ro/ (HTTP 200; `/Home.aspx` redirects)
- BCR: https://www.bcr.ro/ (HTTP 200)
- BRD: https://www.brd.ro/ (HTTP 200)

## Housing search surfaces (not escrow)

- Storia Bucharest rentals / sales surface: https://www.storia.ro/ (HTTP 200)
- Imobiliare.ro and OLX housing paths returned HTTP 403 from this runner; still common human search surfaces — verify live in a browser when quoting rents.

## Tech / startups

- StartupCafe: https://startupcafe.ro/ (HTTP 200)
- Start-Up Nation: https://start-upnation.ro/ (HTTP 200)
- eMAG: https://www.emag.ro/ (HTTP 200)
- Bitdefender: https://www.bitdefender.com/ (HTTP 200; may geo-redirect)

## Notes for agents

- Treat rent, salary, fare, and fee tables in this skill as orientation ranges, not live quotes.
- For immigration, licensing, or tax filings, point to IGI / MAE / ANAF pages and licensed professionals; do not act as counsel.
- Prefer IGI / MAI / STB / ANAF / BNR pages over secondary listicles when entry, residency, transit, tax, or FX matter.
- Metrorex and some MAE endpoints were unreachable from this automation host; disclose that gap instead of inventing live fares or visa fees.
