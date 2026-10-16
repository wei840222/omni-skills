# Sources — Taxi / rideshare

Re-check the live page before asserting current pickup rules, promo terms, or
airport fees. Vendor marketing pages and third-party aggregators are not
substitutes for in-app estimates or official help articles.

## Agent Skills format

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt

## Rideshare product and safety pages (verified HTTP 200 on 2026-10-16)

- Lyft rider overview — https://www.lyft.com/rider
- Lyft how to request a ride — https://help.lyft.com/hc/en-us/articles/115013078708-How-to-request-a-ride
- Lyft Help Center — https://help.lyft.com/hc/en-us
- Lyft terms — https://www.lyft.com/terms
- Lyft rider safety — https://www.lyft.com/safety/rider
- Lyft safety hub — https://www.lyft.com/safety
- Lyft driver overview — https://www.lyft.com/driver
- Uber investor home (public company filings entry) — https://investor.uber.com/

## Airport ground transportation (example: SFO)

Airport pickup zones, taxi stands, and third-party lot rules change by terminal.
Confirm the operating airport page before directing a rider to a curb.

- SFO ground transportation — https://www.flysfo.com/passengers/ground-transportation
- SFO home — https://www.flysfo.com/

## Accessibility and expense evidence

- ADA.gov — https://www.ada.gov/
- ADA service animals topic — https://www.ada.gov/topics/service-animals/
- IRS Topic 511 — Business travel expenses — https://www.irs.gov/taxtopics/tc511
- IRS Publication 463 — Travel, gift, and car expenses — https://www.irs.gov/publications/p463

## Evidence notes

- Uber consumer marketing/help hosts frequently return bot-mitigation HTTP 4xx
  to plain `curl`; treat in-app Help → Trip → Report issue as the operational
  path when a public URL cannot be revalidated.
- Regional fare bands in `fares.md` are planning heuristics only. Prefer live
  app estimates for any booking decision.
