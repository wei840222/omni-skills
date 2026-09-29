---
name: california
description: Navigate California living, moving, and travel logistics including housing,
  taxes, hazards, DMV, and regional trade-offs. Use when the user asks about California
  regions, relocation, resident tasks, or state-specific trip planning.
metadata:
  openclaw: '{"emoji":"🌊","requires":{"config":["<state_root>/california/"]}}'
  related-skills: '{"travel":"General itinerary design and multi-stop trip structure beyond California-specific logistics.","car-rental":"Rental car pickup, return, and handoff decisions for California trips.","housing":"Deeper buy/rent/invest workflow after California region and housing fit are narrowed.","home-buying":"Purchase and mortgage workflow support once a California market is selected.","health-insurance":"Plan comparison terminology after Covered California or employer coverage is in scope.","business":"Broader operations guidance beyond California formation, tax, and local compliance layers.","legal":"General legal framing when a California question escalates past practical resident guidance."}'
---

## When to load

Load this skill for California regions, moving logistics, DMV rules, housing, taxes, hazard planning, utilities, schools, health coverage, business setup, transit, and trip preparation. Prefer this skill over generic travel or housing skills when California state or local layers change the answer.

## State location

Resolve `<state_root>` once per invocation before any persistent read or write:

1. Prefer an explicit host- or user-configured state root when provided.
2. Otherwise use the first existing candidate among host defaults for skill state.
3. If none exist and the user confirms continuity, create `<state_root>/california/` after explaining what will be stored.
4. Keep the selected root fixed for the rest of the invocation.

- State root: `<state_root>/california/`
- Memory file: `<state_root>/california/memory.md`
- Memory schema: `assets/memory-template.md`
- First-use setup: `references/setup.md`

This skill works statelessly for one-off questions. Before creating or changing files under `<state_root>/california/`, explain the planned write and ask for confirmation.

```text
<state_root>/california/
└── memory.md     # mode, region, timelines, constraints, open loops
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup guide | `references/setup.md` |
| Security and trust | `references/security-and-trust.md` |
| Memory template | `assets/memory-template.md` |
| Regions, metros, and base-city tradeoffs | `references/regions.md` |
| Move-in sequence and relocation checklist | `references/moving-and-settling.md` |
| Driver license, registration, smog, and DMV flow | `references/california-dmv-and-vehicles.md` |
| Renting, buying, insurance pressure, and property fit | `references/housing-and-insurance.md` |
| Electricity, water, gas, internet, and recurring bills | `references/utilities-and-bills.md` |
| Taxes, salary reality, and total cost of life | `references/costs-and-taxes.md` |
| Wildfire, earthquake, flood, and outage readiness | `references/hazards-and-preparedness.md` |
| Laws, scams, and practical safety | `references/laws-and-safety.md` |
| Schools, childcare, and family-location logic | `references/family-and-schools.md` |
| Health insurance, care access, and plan selection | `references/healthcare-and-coverage.md` |
| Work, startups, LLCs, and statewide business tradeoffs | `references/work-and-business.md` |
| Transit, driving, and commute design | `references/transit-and-commutes.md` |
| Road trips, parks, and visiting strategy | `references/road-trips-and-visiting.md` |
| Official sources map | `references/sources.md` |

Read the matching relative path before giving topic-specific guidance.

## Core Rules

### 1. Classify the user before giving advice
- Decide which California mode applies first: visitor, future resident, current resident, or business operator.
- Anchor the answer to region, metro, county, ZIP, and school district when those variables change the recommendation.
- If that context is missing, ask for it before treating California as one market.

### 2. Separate state rules from local California reality
- California-level rules are only the first layer. City, county, utility territory, school district, coastal or inland climate, and insurance exposure often change the real answer.
- Label which parts are statewide and which parts must be verified locally.
- For address-specific questions, prefer official portals over generic summaries.

### 3. Treat California as distinct operating environments
- Bay Area, Los Angeles, Orange County, Inland Empire, San Diego, Sacramento, Central Coast, and mountain or desert regions each solve different problems.
- Compare housing cost, commute shape, hazard exposure, and job geography together.
- The right base usually depends on that combined fit, not a single headline metric.

### 4. Total cost beats headline rent or salary
- Include state income tax, sales-tax variation, car or transit cost, parking, utilities, insurance, and hazard-driven costs.
- For homeowners and renters, mention wildfire or earthquake readiness, deductible pressure, and availability problems when relevant.
- Use `references/costs-and-taxes.md` before calling a place "worth it."

### 5. Hazard planning changes good advice
- Wildfire, smoke, earthquake, flood, mudslide, drought, heat, and outage risk are not side notes.
- Adjust home choice, commute, trip design, and insurance guidance around actual exposure.
- When hazard risk matters, lead with readiness and fallback plans.

### 6. Deliver sequence, not brochure copy
- California users often need deadlines, documents, portals, and tradeoffs.
- For administrative topics, answer as "do this today / this week / later" when possible.
- For destination or relocation topics, show why one base region fits better than another.

### 7. Use official sources for unstable rules
- DMV steps, smog rules, tax rates, wildfire insurance issues, district boundaries, and health-coverage details can change.
- Verify current information from the official state or local source before giving precise compliance steps.
- If current verification is blocked, say so plainly and state the uncertainty.

## Common Traps

- Treating California like one state experience instead of multiple markets and risk zones.
- Recommending a neighborhood without checking commute shape, insurance stress, and district fit.
- Comparing salaries without subtracting state tax, parking, transit, utilities, and local cost pressure.
- Ignoring wildfire, smoke, earthquake, or flood exposure until after housing is narrowed.
- Mixing up DMV, CDTFA, FTB, Covered California, CPUC-regulated utilities, and local school or county systems.
- Planning California travel by map distance instead of traffic, mountain timing, permits, and seasonal hazard conditions.

## External Endpoints

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| https://www.ca.gov | Page requests only unless the user explicitly wants form guidance | State services and resident tasks |
| https://www.dmv.ca.gov | Page requests only unless the user explicitly provides case details | Driver license, REAL ID, registration, and smog workflows |
| https://www.cdtfa.ca.gov | Page requests only unless the user wants tax-specific guidance | Sales tax and local district tax guidance |
| https://www.ftb.ca.gov | Page requests only unless the user wants income-tax guidance | State income tax references and resident tax workflows |
| https://www.fire.ca.gov | ZIP, county, or region only if the user asks for wildfire-specific guidance | Official CAL FIRE portal for wildfire context |
| https://www.listoscalifornia.org | Page requests; region only if the user asks for preparedness help | California preparedness playbooks including wildfire |
| https://www.ready.gov/wildfires | Page requests only | Federal wildfire readiness checklist cross-check |
| https://www.earthquake.ca.gov | Page requests only | Earthquake alerts and preparedness guidance |
| https://www.insurance.ca.gov | ZIP, county, or region only if the user asks for insurance or wildfire-loss guidance | Insurance help, wildfire consumer protections, and claims guidance |
| https://www.coveredca.com | County or ZIP only if the user asks for marketplace coverage help | Health insurance marketplace and plan lookup |
| https://www.ca.gov/departments/140/ | Page requests only | California Department of Education entry via CA.gov directory |
| https://www.cde.ca.gov | ZIP, city, district, or school only if the user asks for school matching | Education department site when reachable; verify live pages before citing district details |

No other data is sent externally. Do not submit government forms, store credentials, SSNs, or payment details unless the user explicitly requests that behavior and provides the data for the current task.
