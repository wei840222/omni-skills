---
name: texas
description: "Navigate Texas for living, relocation, and travel. Use when comparing Texas metros (Austin, Dallas, Houston, San Antonio), managing DPS/TxDMV requirements, planning for property taxes and severe weather, or planning road trips."
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🤠","requires":{"config":["<state_root>/texas/"]}}'
---

## When to Use

User needs Texas-specific guidance that generic U.S. advice usually gets wrong: choosing a metro, moving, driving, taxes, weather prep, family logistics, small business setup, or road trip execution.

Activate for four modes: visiting, moving to Texas, living in Texas, and operating a Texas-based business.

## State location

Texas state may exist in `<workspace>/texas/`, `<workspace>/memory/texas/`, or `~/texas/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/texas/`, `<workspace>/memory/texas/`, `~/texas/`.
3. If none exists and state must be created, default to `<workspace>/texas/`.

Use the selected `<state_root>` for every state operation in this skill.

Optional continuity lives in portable `<state_root>/texas/`. One-off Texas questions stay stateless.

```text
<state_root>/texas/
└── memory.md     # User context, region, timelines, constraints, and open loops
```

- Resolve `<state_root>` from the active agent/workspace convention; do not hard-code a machine-specific home path in instructions.
- Preferred path: `<state_root>/texas/`.
- If the directory does not exist and the user wants continuity, read `references/setup.md`, explain the planned local storage in plain language, and ask for confirmation before creating files. Use `references/memory-template.md` for structure.
- Before creating or changing local files under `<state_root>/texas/`, explain the planned write and ask for confirmation.

## When to Load References

| Topic | When to load | File |
|-------|--------------|------|
| Setup guide | First persistent-memory use | `references/setup.md` |
| Memory template | Updating user context | `references/memory-template.md` |
| Region fit and metro tradeoffs | Choosing a city or base | `references/regions.md` |
| Move-in sequence and admin checklist | Moving planning | `references/moving-and-settling.md` |
| License, registration, tolls, and vehicles | Driving / vehicle admin | `references/texas-dmv-and-vehicles.md` |
| Renting, buying, property tax, and flood risk | Housing | `references/housing-and-property.md` |
| Power, water, internet, and recurring bills | Utilities | `references/utilities-and-bills.md` |
| Taxes, insurance pressure, and cost reality | Budget / cost claims | `references/costs-and-taxes.md` |
| Heat, storms, freezes, outages, and prep | Weather risks | `references/weather-and-emergencies.md` |
| Laws, scams, and practical safety | Safety / laws | `references/laws-and-safety.md` |
| Schools, childcare, and family planning | Family context | `references/family-and-schools.md` |
| Health insurance, urgent care, and care access | Healthcare | `references/healthcare-and-insurance.md` |
| Jobs, LLC setup, sales tax, and compliance | Business | `references/work-and-business.md` |
| Road trips, visiting, and city-hopping | Travel | `references/road-trips-and-visiting.md` |
| Official sources map | Verifying unstable rules | `references/sources.md` |

## Core Rules

### 1. Classify the User Before Giving Advice
- Decide which Texas mode applies first: visitor, future resident, current resident, or business operator.
- Anchor the answer to region, metro, county, ZIP, and school district when those variables change the recommendation.
- If that context is missing, ask for it before treating Texas as uniform.

### 2. Separate State Rules from Local Reality
- Texas-level rules are only the first layer. City, county, appraisal district, utility territory, school district, and flood zone often change the real answer.
- Label which parts are statewide and which parts must be verified locally.
- For address-specific questions, prefer official portals over memory or generic summaries.

### 3. Distances and Drive Time Beat Map Intuition
- Texas plans fail when users underestimate distance, tolls, fatigue, weather, and event traffic.
- For relocation and travel, convert geography into realistic drive-time, airport, and corridor tradeoffs.
- Prefer multi-day plans when destinations are far instead of packing everything into one day.

### 4. Texas Cost Reality Is Broader Than "No State Income Tax"
- Include housing, property tax pressure, insurance, toll roads, summer power bills, car dependence, and weather-driven costs.
- For homeowners and businesses, mention appraisal, deductible, flood, hail, and outage exposure when relevant.
- Load `references/costs-and-taxes.md` before calling a place "cheap."

### 5. Weather and Grid Risk Change Good Advice
- Heat, flood, hail, hurricanes, tornadoes, wildfire smoke, and winter freezes are normal planning inputs.
- Adjust moving plans, road trips, home choice, and seasonal recommendations around actual hazard exposure.
- When weather is part of the problem, lead with readiness and fallback plans.

### 6. Deliver Checklists, Not Tourism Copy
- Texas users usually need deadlines, documents, portals, sequence, and tradeoffs.
- For administrative questions, answer as "do this today / this week / later" when possible.
- For destination questions, show why one base city or region fits better than another.

### 7. Use Official Sources for Unstable Rules
- License rules, registration steps, sales tax, homestead details, district lookups, and emergency guidance can change.
- Verify current information from the official state or local source before giving precise compliance steps.
- If current verification is blocked, say so plainly and give only verified ranges or next lookup steps.

## Common Traps

- Treating Texas like one market instead of multiple metros and risk zones.
- Recommending a neighborhood or suburb without commute shape, flood exposure, and school district.
- Saying "no state income tax" while ignoring property tax, insurance, tolls, and electricity spikes.
- Mixing up Texas DPS, TxDMV, county tax offices, appraisal districts, and city utilities.
- Planning a road trip by miles instead of daylight, heat, event traffic, and fuel gaps.
- Giving housing advice without HOA, wind/hail exposure, and renter or owner insurance gaps.
- Using U.S.-generic legal guidance for cannabis, DWI, landlord-tenant, or permit questions.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://www.texas.gov | Page requests only unless user explicitly wants form guidance | State service portal and resident tasks |
| https://www.dps.texas.gov | Page requests only unless user explicitly provides personal case details | Driver license and ID rules |
| https://www.txdmv.gov | Page requests only unless user explicitly wants vehicle workflow help | Vehicle title, registration, and county office guidance |
| https://comptroller.texas.gov | Page requests only unless user explicitly wants tax-specific guidance | Sales tax, franchise tax, property tax resources |
| https://tea.texas.gov | ZIP, city, district, or school references if the user asks for school matching | School district and education framework |
| https://www.texasready.gov | Page requests only | Emergency preparedness and hazard planning |
| https://powertochoose.org | ZIP if the user asks to compare electric plans in deregulated areas | Electricity market lookup |

No other data is sent externally.

## Security & Privacy

**Data that may leave your machine:**
- Public page requests to official Texas or utility-choice sites
- ZIP, city, county, or district data only when the user asks for location-specific guidance

**Data that stays local:**
- Region preference, move timeline, family constraints, vehicle notes, and open tasks in `<state_root>/texas/`

**This skill does NOT:**
- Submit government forms on the user's behalf without explicit instruction
- Store credentials, SSNs, or payment information in local memory
- Assume local rules when the answer depends on a city, county, or district

## Trust

By using this skill, location details such as ZIP, county, or district may be checked against official Texas or local-government websites when the user asks for precise guidance.

Only install if you trust those public services with that lookup context.
