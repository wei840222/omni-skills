---
name: dubai
description: Provide practical guidance on Dubai for visitors, residents, tech workers, and entrepreneurs. Use this skill when asked about Dubai neighborhoods, transport, costs, visas, or local insights.
metadata:
  openclaw: '{"emoji": "\ud83c\udfd9\ufe0f", "requires": {"bins": null}, "os": ["linux", "darwin", "win32"], "displayName": "Dubai"}'
---

## State location

This skill is stateless and does not store local configuration or state.

## When to Use

User asks about Dubai for any purpose: visiting, moving, working, studying, or starting a business. Agent provides practical guidance with current data.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| **Visitors** | | |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` | User wants to know what to see in Dubai |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` | User wants a planned trip schedule |
| Where to stay | `references/visitor-lodging.md` | User needs hotel or accommodation advice for a visit |
| Tips & day trips | `references/visitor-tips.md` | User needs general tips for visiting Dubai |
| **Neighborhoods** | | |
| Quick comparison | `references/neighborhoods-index.md` | User wants a high-level comparison of areas |
| Downtown, DIFC, Business Bay | `references/neighborhoods-downtown.md` | User asks about Downtown, DIFC, or Business Bay |
| Dubai Marina, JBR, JLT | `references/neighborhoods-marina.md` | User asks about Dubai Marina, JBR, or JLT |
| Jumeirah, Palm, Al Sufouh | `references/neighborhoods-beach.md` | User asks about Jumeirah, Palm, or beach areas |
| Arabian Ranches, Springs, DSO | `references/neighborhoods-suburban.md` | User asks about suburban communities or villas |
| Choosing guide | `references/neighborhoods-choosing.md` | User needs help deciding where to live |
| **Food** | | |
| Overview & dining scene | `references/food-overview.md` | User wants a general understanding of Dubai's food scene |
| Local & Middle Eastern | `references/food-local.md` | User wants to find local or Middle Eastern cuisine |
| International & fine dining | `references/food-international.md` | User wants international or fine dining recommendations |
| Best areas for dining | `references/food-areas.md` | User wants to know the best neighborhoods for dining |
| Dietary, alcohol, Ramadan | `references/food-practical.md` | User asks about alcohol rules, dietary needs, or Ramadan dining |
| **Practical** | | |
| Moving & settling | `references/resident.md` | User is moving to Dubai or newly settled |
| Transport (metro, taxis, Salik) | `references/transport.md` | User needs info on getting around (metro, taxi, driving) |
| Cost of living | `references/cost.md` | User asks about cost of living, expenses, or budgeting |
| Safety & laws | `references/safety.md` | User asks about safety, emergency contacts, or basic laws |
| Weather & survival tips | `references/climate.md` | User asks about weather, summer heat, or when to visit |
| Local services (banking, SIM) | `references/local.md` | User asks about banking, SIM cards, or local services |
| **Career** | | |
| Tech industry & salaries | `references/tech.md` | User is a tech worker or asks about tech industry salaries |
| Business setup & free zones | `references/business.md` | User wants to set up a business or asks about free zones |
| Visas (employment, golden, freelance) | `references/visas.md` | User asks about visa types, golden visa, or freelance permits |
| Startups & funding | `references/startup.md` | User asks about startups, incubators, or funding |
| **Lifestyle** | | |
| Culture & customs | `references/culture.md` | User asks about local culture, customs, or etiquette |
| Healthcare & insurance | `references/healthcare.md` | User asks about medical facilities, insurance, or finding a doctor |
| Schools & education | `references/education.md` | User asks about schools, curriculums, or education costs |
| Expat lifestyle & social | `references/lifestyle.md` | User asks about expat lifestyle, socializing, or daily life |
| Driving & car ownership | `references/driving.md` | User asks about driving licenses, buying a car, or road rules |
| **General Rules** | | |
| Core Rules | `references/core-rules.md` | Mandatory context for any broad request about living or working in Dubai |
| Free Zones | `references/free-zones.md` | User asks about starting a company, freelance visa, or tech zones |
| Traps | `references/traps.md` | Always load when advising tourists or new expats to prevent major issues |
| Legal Awareness | `references/legal.md` | Always load when discussing safety, alcohol, cohabitation, or online behavior |
| Domain Research | `references/domain-research.md` | User asks for general facts, population, or economic status of Dubai |
