---
name: ibiza
description: Provide practical Ibiza guidance for holidays, relocation, remote work, seasonal work, or business setup, including zones, transport, costs, visas, and legal rules. Use when the user asks about Ibiza travel, lodging, nightlife, beaches, residency, or island operations.
metadata:
  openclaw: '{"emoji":"🏝️"}'
  related-skills: '{"travel":"Multi-destination trip planning and logistics beyond one island.","expat":"Relocation and adaptation workflows for longer stays.","food":"Dining research and personalization for food-first trips.","startup":"Founder operations when setting up or running a business from Ibiza.","spain":"Spain-wide travel and regional context beyond the Balearics.","europe":"EU/Schengen mobility and cross-border framing."}'
---

## When to Use

Use when the user asks about Ibiza for holidays, relocation, seasonal work, remote work, or business setup. Give practical, current guidance with zone-level detail and legal context. For live fares, visa eligibility, tax status, lodging availability, traffic restrictions, or weather-dependent plans, load the matching reference and verify the official source before treating a figure as current.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| **Visitors** | | |
| Beaches and coves strategy | `references/visitor-beaches.md` | User asks about beaches and coves strategy |
| Nightlife planning and club logistics | `references/visitor-nightlife.md` | User asks about nightlife planning and club logistics |
| Itineraries (3, 5, 7 days) | `references/visitor-itineraries.md` | User asks about itineraries (3, 5, 7 days) |
| Where to stay by profile | `references/visitor-lodging.md` | User asks about where to stay by profile |
| Day activities and alternatives | `references/visitor-activities.md` | User asks about day activities and alternatives |
| **Zones** | | |
| Island quick comparison | `references/zones-index.md` | User asks about island quick comparison |
| Ibiza Town and Marina zones | `references/zones-ibiza-town.md` | User asks about Ibiza Town and Marina zones |
| Sant Antoni and west coast | `references/zones-san-antonio.md` | User asks about Sant Antoni and west coast |
| Santa Eularia and east coast | `references/zones-santa-eulalia.md` | User asks about Santa Eularia and east coast |
| North and quieter areas | `references/zones-north.md` | User asks about north and quieter areas |
| Zone selection framework | `references/zones-choosing.md` | User asks about zone selection framework |
| **Food and Going Out** | | |
| Dining scene overview | `references/food-overview.md` | User asks about dining scene overview |
| Local Ibizan food | `references/food-local.md` | User asks about local Ibizan food |
| Fine dining and premium tables | `references/food-fine-dining.md` | User asks about fine dining and premium tables |
| Beach clubs and day parties | `references/food-beach-clubs.md` | User asks about beach clubs and day parties |
| Budget food strategy | `references/food-budget.md` | User asks about budget food strategy |
| **Practical** | | |
| Arrival by air and sea | `references/transport-arrival.md` | User asks about arrival by air and sea |
| Local mobility and day movement | `references/transport-local.md` | User asks about local mobility and day movement |
| Cost of living and trip budgets | `references/cost.md` | User asks about cost of living and trip budgets |
| Housing and rental risks | `references/housing.md` | User asks about housing and rental risks |
| Safety and legal basics | `references/safety.md` | User asks about safety and legal basics |
| Seasons and weather decisions | `references/seasons.md` | User asks about seasons and weather decisions |
| Local admin and services | `references/local.md` | User asks about local admin and services |
| Legal awareness | `references/legal.md` | User asks about legal or compliance basics |
| **Residency and Work** | | |
| Short and long stay visa logic | `references/visas.md` | User asks about short and long stay visa logic |
| Remote work and nomad setup | `references/nomad.md` | User asks about remote work and nomad setup |
| Seasonal jobs and contracts | `references/seasonal-work.md` | User asks about seasonal jobs and contracts |
| **Lifestyle** | | |
| Culture, etiquette, and local rhythm | `references/culture.md` | User asks about culture, etiquette, and local rhythm |
| Healthcare and coverage | `references/healthcare.md` | User asks about healthcare and coverage |
| Wellness and recovery lifestyle | `references/wellness.md` | User asks about wellness and recovery lifestyle |
| **Research** | | |
| Source map and official links | `references/sources.md` | User asks about source map and official links |
| Gate 6 research notes | `references/knowledge-sources.md` | User asks about research freshness or source updates |

## State location

This skill is stateless and does not store local configuration or persistent data.

## Core Rules

Load `references/rules.md` before making schedule, lodging, budget, visa, or safety recommendations.

## Common Traps

Load `references/traps.md` when planning peak-season trips, nightlife logistics, rentals, or seasonal work.

## Security & Privacy

- Prefer licensed transport and legal accommodation channels.
- Treat visa, tax, residency, and traffic-restriction answers as time-sensitive; verify official sources before the user spends money or commits travel.
- Do not present dated rent, fare, or passenger figures as live facts without a freshness check.
