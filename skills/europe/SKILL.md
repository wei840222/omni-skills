---
name: europe
description: "Expertly manage cross-border trip planning, mobility rights, choosing a base, moving, studying, and working remotely across Europe by understanding how the EU, Schengen, eurozone, and national systems intersect."
license: MIT
compatibility: "*"
metadata:
  openclaw: '{"emoji":"🇪🇺"}'
  related-skills: '{"travel":"skills/travel","booking":"skills/booking","car-rental":"skills/car-rental","health-insurance":"skills/health-insurance","english":"skills/english"}'
---
## When to Use

User needs Europe-specific guidance that generic travel or relocation advice usually gets wrong: choosing the right country or city, understanding EU vs Schengen vs eurozone rules, planning multi-country trips, moving, studying, working remotely, handling healthcare, or operating across borders.

This skill should activate for seven modes: visiting Europe, choosing a base in Europe, moving to Europe, living in Europe, studying in Europe, working remotely across Europe, and operating a Europe-facing business or freelance setup.

## State location

This skill works statelessly for one-off Europe questions. If the user wants continuity across sessions, memory lives in `<state_root>/`. If `<state_root>/` does not exist, read `references/setup.md`, explain planned local storage in plain language, and ask for confirmation before creating files. See `references/memory-template.md` for structure.

```text
<state_root>/
└── memory.md     # Nationality, mobility rights, target countries, timelines, constraints, and open loops
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup guide | `references/setup.md` |
| Memory template | `references/memory-template.md` |
| Europe blocs, rights layers, and country-group logic | `references/europe-basics-and-blocs.md` |
| Macroregions, corridors, and cluster tradeoffs | `references/regional-corridors-and-country-clusters.md` |
| Choosing countries, cities, and base strategy | `references/choosing-countries-and-cities.md` |
| Entry, visas, residence pathways, and right-to-stay logic | `references/entry-visas-and-right-to-stay.md` |
| Schengen math, borders, and 90/180 traps | `references/schengen-border-and-90-180.md` |
| Move-in sequence and settling checklist | `references/moving-and-settling.md` |
| Housing, banking, SIMs, utilities, and local admin | `references/housing-banking-phone-and-admin.md` |
| Jobs, universities, qualifications, and business setup | `references/work-study-and-qualifications.md` |
| Tax residence, social security, and cross-border paperwork | `references/taxes-social-security-and-residency.md` |
| Public healthcare, EHIC/GHIC logic, and private cover | `references/healthcare-and-insurance.md` |
| Rail, flights, ferries, buses, and passenger rights | `references/transport-and-passenger-rights.md` |
| Multi-country routing, road trips, and Europe pace design | `references/rail-flights-and-road-trips.md` |
| Eurozone reality, cards, cash, and everyday payments | `references/money-payments-and-eurozone.md` |
| Remote work, digital nomads, and split-country life | `references/remote-work-and-digital-nomads.md` |
| Seasonal stays, second homes, and part-year Europe life | `references/seasonal-living-and-second-homes.md` |
| Families, children, schools, and student tradeoffs | `references/family-students-and-children.md` |
| Scams, emergencies, 112, and consumer protection | `references/safety-scams-and-consumer-rights.md` |
| Climate, shoulder seasons, and event timing | `references/weather-seasons-and-trip-timing.md` |
| Weekend trips, interrail-style loops, and short-break logic | `references/weekend-trips-and-multicountry-routes.md` |
| Official sources map | `references/sources.md` |
| Gate 6 research sources | `references/research.md` |

## Core Rules
Load `references/core-rules.md` to learn about the core rules for this skill.

## Common Traps
Load `references/common-traps.md` to learn about the common traps to avoid for this skill.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://europa.eu/youreurope/ | Page requests only unless user explicitly wants country-specific rights guidance | EU citizen rights, travel, residence, work, health, consumer protection |
| https://immigration-portal.ec.europa.eu/ | Nationality and target-country context only if user asks for non-EU residence or work guidance | Non-EU migration pathways by country |
| https://eures.europa.eu/ | Country, language, and profession context only if user asks for job-market guidance | Jobs, living and working conditions |
| https://europass.europa.eu/ | Qualification or CV context only if user asks for recognition or study/work prep | Skills, qualifications, and CV framework |
| https://eur-lex.europa.eu/ | Page requests only | EU law and regulation reference |
| https://ec.europa.eu/eurostat | Page requests only unless user asks for comparative data pulls | Europe-wide comparative statistics |
| https://europa.eu/112 | Country or location only if user asks for emergency readiness | Europe emergency-number framework |
| https://www.eccnet.eu/ | Country and consumer-case context only if user asks for purchase or travel-rights help | Consumer protection and dispute support |
| https://europa.eu/solvit/ | Country and rights-problem context only if user asks for EU-rights problem solving | Cross-border rights assistance |

No other data is sent externally.

## Security & Privacy

**Data that may leave your machine:**
- Public page requests to official EU and national portals
- Country, nationality, residency, profession, or route context only when the user asks for location-specific guidance

**Data that stays local:**
- Mobility goals, target countries, trip or move timelines, family constraints, and open tasks in `<state_root>/`

**This skill does NOT:**
- Submit visa, tax, residency, or university forms on the user's behalf without explicit instruction
- Store passport numbers, tax IDs, bank credentials, or payment information in local memory by default
- Assume country-specific rules when the answer depends on nationality, right-to-stay, or local registration

## Trust

By using this skill, details such as nationality, target country, and cross-border route context may be checked against official European or national-government websites when the user asks for precise guidance.

Only install if you trust those public services with that lookup context.
