# Sources — Italy Skill

Last checked: 2026-10-16 (handoff Gate 6 pass; booking-critical claims still require live page check)

## Entry, Visa, and Borders

- Italian MFA home (English): https://www.esteri.it/en/ (HTTP 200; may hit bot challenge—open in a browser before quoting visa products)
- Visa for Italy portal: https://vistoperitalia.esteri.it/ (HTTP 200)
- EU Travel to Europe — ETIAS: https://travel-europe.europa.eu/en/etias (HTTP 200)
- EU Travel to Europe — EES: https://travel-europe.europa.eu/en/ees (HTTP 200)
- European Commission Schengen border-crossing policy: https://home-affairs.ec.europa.eu/policies/schengen/border-crossing_en (HTTP 200)
- Polizia di Stato home: https://www.poliziadistato.it/ (HTTP 200)

## ZTL / Urban Access

- Polizia di Stato — ZTL article: https://www.poliziadistato.it/articolo/10930-ztl (HTTP 200)
- Polizia di Stato related article: https://www.poliziadistato.it/articolo/10930 (HTTP 200)
- Comune di Roma home: https://www.comune.roma.it/web/it/home.page (HTTP 200)
- Roma mobility agency (automation SSL failure): https://www.agenziamobilita.roma.it/ — open in a browser before quoting Area C / ZTL hours

## Rail and National Transport

- Trenitalia English: https://www.trenitalia.com/en.html (HTTP 200)
- Italo Treno English: https://www.italotreno.com/en (HTTP 200)
- ViaggiaTreno infomobility: https://www.viaggiatreno.it/infomobilita/index.jsp (HTTP 200; may redirect to http)
- FS Italiane English hub: https://www.fsitaliane.it/en.html (HTTP 200)

## City Transit

- ATAC Rome: https://www.atac.roma.it/ (HTTP 200)
- ATM Milan English: https://www.atm.it/en/Pages/default.aspx (HTTP 200)
- ACTV / AVM Venice English: https://www.actv.it/en (HTTP 200; redirects to https://actv.avmspa.it/en)
- Venezia Unica tourist tickets: https://www.veneziaunica.it/en (HTTP 200)

## Museums and Tickets

- Italia.it national tourism portal: https://www.italia.it/en (HTTP 200)
- Musei Italiani portal: https://www.museiitaliani.it/ (HTTP 200)
- Uffizi Galleries English: https://www.uffizi.it/en (HTTP 200)
- CoopCulture English (Colosseum / Roman sites ticketing partner): https://www.coopculture.it/en/ (HTTP 200)
- Vatican Museums home: https://www.museivaticani.va/ (HTTP 200; redirects under `/content/museivaticani.html`)
- Vatican Museums tickets: https://tickets.museivaticani.va/ (HTTP 200)

## Safety, Health, Civil Protection

- Ministero della Salute home: https://www.salute.gov.it/portale/home.html (HTTP 200)
- Protezione Civile English: https://www.protezionecivile.gov.it/en/ (HTTP 200)
- European emergency number orientation: use **112** as the EU single number; confirm local secondary numbers (118 ambulance historically) on Protezione Civile / local pages before quoting procedures

## Fetch gaps / obsolete handling

- `www.interno.gov.it/en`, some Prefettura hosts, and Agenzia delle Entrate English pages returned HTTP 403 to this automation UA. Keep official destinations, but re-open in a browser before quoting entry thresholds or tax rules.
- `www.agenziamobilita.roma.it` and some Vatican ticket aliases failed TLS/DNS from this runner—use Comune di Roma + `tickets.museivaticani.va` until alternate paths verify.
- `112.gov.it` failed certificate verification here; treat **112** as the standard EU emergency number and confirm operational guidance via Protezione Civile or Polizia pages in a browser.
- Schengen day counts, ETIAS/EES applicability, and nationality-specific visa outcomes are orientation only until re-checked for the traveler’s passport and travel date.
- Train fares, ZTL hours, and museum ticket windows change frequently—re-open Trenitalia/Italo, local Comune ZTL pages, and official ticket partners before non-refundable bookings.
