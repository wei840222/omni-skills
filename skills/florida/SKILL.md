---
name: florida
description: >
  Navigate Florida for living, moving, working, seasonal stays, and road
  trips with region fit, storm/insurance reality, licensing, housing, and
  dual-state logistics. Use when choosing a Florida region, relocating,
  settling as a resident, planning snowbird/seasonal living, or designing
  statewide trips that generic U.S. advice gets wrong. Prefer `travel` for
  multi-destination traveler systems, `car-rental` for rental/airport logistics,
  `booking` for reservation workflows, `business` for non-Florida business ops,
  and `health-insurance` for deeper plan comparison beyond Florida access.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🌴"}'
  related-skills: '{"booking":"Reservation workflows for flights, cruises, resorts, and schedule holds after Florida bases or dates are chosen.","business":"Broader business operations guidance beyond Florida-specific rules and Sunbiz workflows.","car-rental":"Rental car, airport pickup, and highway planning for Florida trips.","health-insurance":"Deeper plan-comparison support beyond Florida-specific access questions.","travel":"General itinerary design and standing multi-destination traveler systems outside Florida-specific logistics."}'
---

## State location

Optional Florida continuity notes may exist in
`<workspace>/florida/`, `<workspace>/memory/florida/`, or `~/florida/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/florida/`, `<workspace>/memory/florida/`, `~/florida/`.
3. If none exists and durable context must be created, default to
   `<workspace>/florida/` only with user consent.
4. If more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell cwd.
   An existing `~/florida/` may be read; otherwise ask before creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.
Treat legacy `~/Clawic/data/florida/` only as a migration source—ask before
copying or deleting it.

**Data.** Durable notes live in `<state_root>/memory.md` when the user wants
continuity (see `references/memory-template.md` and `references/setup.md`).
This skill answers one-off Florida questions without state. Avoid storing
credentials, SSNs, Medicare numbers, payment details, or full street addresses
unless the user explicitly asks for that continuity. Host-shared memory such as
workspace `MEMORY.md` is outside `<state_root>` and needs separate consent.

```text
<state_root>/
└── memory.md     # User context, regions, timelines, insurance concerns, and open loops
```

## When to Use

User needs Florida-specific guidance that generic U.S. advice usually gets wrong: choosing a region, moving, licensing, insurance, hurricane prep, HOA or condo reality, healthcare access, seasonal living, or statewide trip planning.

Activate for five modes: visiting, moving to Florida, living in Florida, operating a Florida-based business, and managing a seasonal or snowbird setup.

## Progressive disclosure

Keep this file as the always-on contract. Load **at most one** reference for
the current ask; do not preload every deep dive or the whole Quick Reference matrix. Verify unstable rules from
`references/sources.md` before locking compliance steps or money decisions.

| Topic | File | When to load |
|-------|------|--------------|
| Setup guide | `references/setup.md` | No `<state_root>` yet, or user asks what would be stored |
| Memory template | `references/memory-template.md` | Creating or reshaping `<state_root>/memory.md` |
| Region fit and metro tradeoffs | `references/regions.md` | Choosing among South Florida, Central, Tampa Bay, SWFL, Panhandle, First Coast, Keys |
| Move-in sequence and resident checklist | `references/moving-and-settling.md` | Relocation deadlines, homestead, settling tasks |
| License, registration, tolls, and vehicles | `references/florida-dmv-and-vehicles.md` | DL/ID, plates, tolls, title/registration |
| Renting, buying, condo rules, and insurance pressure | `references/housing-and-insurance.md` | Housing search, HOA/condo, wind/flood coverage |
| Utilities, internet, storm outages, and recurring bills | `references/utilities-and-bills.md` | Move-in utilities and outage planning |
| Taxes, wages, insurance costs, and total budget reality | `references/costs-and-taxes.md` | Total cost of living beyond "no state income tax" |
| Hurricanes, flooding, heat, and preparedness | `references/storms-and-preparedness.md` | Storm timing, surge/flood, evacuation readiness |
| Laws, scams, and practical safety | `references/laws-and-safety.md` | Practical legal/safety traps and scam patterns |
| Schools, childcare, and family planning | `references/family-and-schools.md` | Districts, childcare, family logistics |
| Health insurance, providers, Medicare, and care access | `references/healthcare-and-coverage.md` | Marketplace, Medicare, provider networks |
| Jobs, LLC setup, tourism exposure, and business tradeoffs | `references/work-and-business.md` | Employment or Florida entity setup |
| Driving, airports, transit, and corridor planning | `references/transit-and-driving.md` | Car-first mobility, airports, corridors |
| Part-time residency, snowbirds, and dual-state logistics | `references/seasonal-living-and-snowbirds.md` | Split-year / second-home logistics |
| Beaches, parks, theme parks, and road-trip strategy | `references/road-trips-and-visiting.md` | Visitor pacing and statewide trip design |
| Official sources map | `references/sources.md` | Before precise compliance, insurance, school, or portal steps |

## Core Rules

### 1. Classify the User Before Giving Advice
- Decide which Florida mode applies first: visitor, future resident, current resident, business operator, or seasonal resident.
- Then anchor the answer to the user's region, metro, county, ZIP, flood zone, and school district when those variables change the recommendation.
- If that context is missing, ask for it before treating Florida as one market.

### 2. Separate State Rules from Local Execution
- Florida-level rules are only the first layer. County tax collectors, cities, flood zones, evacuation zones, condo associations, school districts, and utility territories often change the real answer.
- Always label which parts are statewide and which parts must be verified locally.
- For address-specific questions, prefer official portals over generic summaries.

### 3. Florida Is Multiple Operating Environments
- South Florida, Central Florida, Tampa Bay, Southwest Florida, the Panhandle, the First Coast, and the Keys address distinct problems.
- Compare regions using multiple factors beyond beach access or rent.
- Fit usually depends on storm exposure, insurance availability, commute style, age mix, healthcare access, and how seasonal the area feels.

### 4. No State Income Tax Does Not Mean Low Cost
- Include homeowners or condo insurance, flood insurance, car insurance, tolls, HOA dues, utility spikes, and storm-prep costs.
- For condo or coastal housing, mention reserves, assessments, wind mitigation, and coverage exclusions when relevant.
- Use `references/costs-and-taxes.md` before calling a place affordable.

### 5. Storm and Heat Planning Change Good Advice
- Hurricanes, storm surge, inland flooding, lightning, heat, humidity, algae events, and outage risk belong in the primary plan.
- Adjust home choice, seasonal timing, trip design, and evacuation guidance around actual exposure.
- When weather is part of the problem, lead with readiness and fallback plans.

### 6. Seasonal Residents Need Different Guidance
- Snowbirds, second-home owners, and split-year residents care about mail, insurance, vehicles, healthcare continuity, taxes, and storm readiness when away.
- Verify stay duration, voting location, insurance, and medical care setup before advising part-time households.
- Use `references/seasonal-living-and-snowbirds.md` whenever the user splits time across states.

### 7. Deliver Sequence, Not Vacation Copy
- Florida users often need deadlines, documents, portals, and tradeoffs.
- For administrative topics, answer in the form "do this today / this week / later" whenever possible.
- For relocation or seasonal topics, show why one base region fits better than another.
- Before creating or changing local files in `<state_root>/`, explain the planned write and ask for confirmation.

### 8. Use Official Sources for Unstable Rules
- Licensing, registration, homestead, evacuation, school boundaries, insurance programs, Medicare options, and park rules can change.
- Verify current information from the official state or local source before giving precise compliance steps.
- State clearly if current verification is blocked and provide only general guidance.

## Common Traps

- Treating Florida like one market instead of a mix of metros, retiree corridors, inland towns, and high-risk coastal zones.
- Recommending a home or condo without checking flood zone, evacuation zone, reserves, assessments, and insurance fit.
- Calling Florida affordable because there is no state income tax while ignoring property insurance, HOA dues, tolls, and car costs.
- Giving resident advice without asking whether the user is full-time, seasonal, retired, or theme-park or hospitality adjacent.
- Planning trips by map distance instead of I-4 traffic, heat, afternoon storms, cruise timing, and airport spread.
- Mixing up FLHSMV, county tax collectors, property appraisers, insurance offices, and local emergency management.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://www.myflorida.gov | Page requests only unless user explicitly wants form guidance | State service portal and resident tasks |
| https://www.flhsmv.gov | Page requests only unless user explicitly provides personal case details | Driver license, ID, registration, and vehicle workflow guidance |
| https://floridarevenue.com | Page requests only unless user explicitly wants tax-specific guidance | Tax, reemployment tax, and business references |
| https://www.myfloridacfo.com/division/consumers | ZIP, county, or region references if the user asks for insurance help | Insurance consumer help, claims, and insurer complaints |
| https://www.floridadisaster.org | County, ZIP, or evacuation context if the user asks for hazard-specific help | Emergency readiness, hurricanes, shelters, and evacuation guidance |
| https://www.fldoe.org | ZIP, city, district, or school references if the user asks for school matching | Education and district framework |
| https://www.floridahealth.gov | County references if the user asks for public-health or local-care guidance | Health department and care navigation |
| https://www.visitflorida.com | Page requests only | Official trip-planning and regional travel references |

Only the endpoints above are used for external lookups in this skill.

## Security & Privacy

**Data that may leave your machine:**
- Public page requests to official Florida agencies and official service portals
- ZIP, county, flood-zone, or district data only when the user asks for location-specific guidance

**Data that stays local:**
- Region preference, move timeline, seasonal-living setup, insurance concerns, and open tasks in `<state_root>/`

**Boundaries:**
- Government forms are submitted only with explicit user instruction for that action
- Credentials, SSNs, Medicare numbers, and payment information stay out of local memory by default
- County, municipality, condo association, and flood-zone answers require local verification instead of statewide assumptions

## Trust

By using this skill, location details such as ZIP, county, district, or flood-zone context may be checked against official Florida or local-government websites when the user asks for precise guidance.

Install only when those public services are acceptable for that lookup context.
