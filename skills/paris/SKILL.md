---
name: paris
description: Provide practical, current guidance for Paris including transit, safety, living costs, itineraries, and area comparisons. Trigger this skill when the user asks about visiting, moving to, studying, or working in Paris.
metadata:
  openclaw: '{"emoji":"🇫🇷"}'
---

## When to Use

User asks about Paris for any purpose: visiting, moving, working, studying, or starting a business. Agent provides practical guidance with current data.

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| **Visitors** | | |
| Attractions (must-see vs skip) | `references/visitor-attractions.md` | When user asks about attractions (must-see vs skip). |
| Itineraries (1/3/7 days) | `references/visitor-itineraries.md` | When user asks about itineraries (1/3/7 days). |
| Where to stay | `references/visitor-lodging.md` | When user asks about where to stay. |
| Tips & day trips | `references/visitor-tips.md` | When user asks about tips & day trips. |
| **Arrondissements** | | |
| Quick comparison | `references/arrondissements-index.md` | When user asks about quick comparison. |
| Central (1-4) | `references/arrondissements-central.md` | When user asks about central (1-4). |
| Left Bank (5-7) | `references/arrondissements-left-bank.md` | When user asks about left bank (5-7). |
| Right Bank (8-11) | `references/arrondissements-right-bank.md` | When user asks about right bank (8-11). |
| Outer (12-20) | `references/arrondissements-outer.md` | When user asks about outer (12-20). |
| Choosing guide | `references/arrondissements-choosing.md` | When user asks about choosing guide. |
| **Food** | | |
| Overview & restaurants | `references/food-overview.md` | When user asks about overview & restaurants. |
| French classics | `references/food-traditional.md` | When user asks about french classics. |
| Markets | `references/food-markets.md` | When user asks about markets. |
| Best areas | `references/food-areas.md` | When user asks about best areas. |
| Wine bars & cafes | `references/food-wine-cafes.md` | When user asks about wine bars & cafes. |
| Dietary & tips | `references/food-practical.md` | When user asks about dietary & tips. |
| **Practical** | | |
| Moving & settling | `references/resident.md` | When user asks about moving & settling. |
| Transport | `references/transport.md` | When user asks about transport. |
| Cost of living | `references/cost.md` | When user asks about cost of living. |
| Safety | `references/safety.md` | When user asks about safety. |
| Weather | `references/climate.md` | When user asks about weather. |
| Local services | `references/local.md` | When user asks about local services. |
| **Career** | | |
| Tech industry | `references/tech.md` | When user asks about tech industry. |
| Students | `references/student.md` | When user asks about students. |
| Startups | `references/startup.md` | When user asks about startups. |

## Plan the Answer

1. Identify the traveller's purpose, dates, budget, party, and access needs.
2. Load the relevant topical reference from the table above.
3. Use `references/core-rules.md` for cross-cutting safety, weather, transit, and arrondissement guidance.
4. For fares, prices, availability, visa/residence, admissions, or any other mutable fact, first load `references/current-information.md` and verify the official source it names. State when a figure is only an estimate.


## Paris-Specific Traps

For scam-prevention or tourist-trap questions, load `references/traps.md` and pair it with current official guidance when an immediate safety decision depends on it.
