---
name: austria
description: >
  Plan Austria trips with rail-first routing, Schengen entry checks, alpine
  season timing, region sequencing, and on-the-ground execution for cities,
  lakes, mountains, ski weeks, and Christmas markets. Use when the user needs
  practical Austria itineraries, transport tradeoffs, vignette/driving rules,
  hut and lift timing, or crowd-sensitive destinations like Hallstatt. Prefer
  `travel` for generic multi-country structure, `car-rental` for rental
  handoff details, `booking` for reservation workflows, `food` for deep dining
  research, and `german` for language support at counters and stations.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🇦🇹","displayName":"Austria","requires":{"bins":[],"config":["<state_root>/"]}}'
  related-skills: '{"travel":"General multi-country trip structure when Austria is only one segment.","car-rental":"Rental pickup/drop and cross-border permission after the route needs a car.","booking":"Reservation and confirmation hygiene for trains, hotels, and lifts.","food":"Deeper restaurant and cuisine research beyond Austria meal-rhythm basics.","german":"Language support for bookings, transport desks, and service interactions."}'
---

## Setup

If `<state_root>/` doesn't exist or is empty, read `references/setup.md` and start naturally.

## When to load

Load this skill when the user is planning an Austria trip and needs practical guidance beyond generic inspiration: entry rules, region choice, rail vs car tradeoffs, mountain timing, city sequencing, food and culture context, and on-the-ground execution.

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for structure. Keep trip preferences out of the skill package.

```
<state_root>/
└── memory.md     # Trip context and evolving constraints
```

## When to load map

Use this map to choose the right decision module before building the route.

| Topic | File |
|-------|------|
| **Entry, Border, and Money** | |
| Tourist entry, visa, Schengen logic, IDs | `references/entry-and-documents.md` |
| Customs, cash, food restrictions, border habits | `references/customs-and-border.md` |
| Budget framing and hidden costs | `references/budget-and-costs.md` |
| Cards, cash, tipping, tax-free basics | `references/tipping-and-payments.md` |
| **Planning Backbone** | |
| Region selection and route architecture | `references/regions.md` |
| Sample itineraries for 4-14 days | `references/itineraries.md` |
| Accommodation strategy by trip style | `references/accommodation.md` |
| **Transport and Outdoors** | |
| Rail, buses, airport links, route timing | `references/transport-domestic.md` |
| Driving, vignette, winter equipment, mountain roads | `references/road-trips-and-driving.md` |
| Alpine, lake, hiking, hut, and cable-car logic | `references/alps-lakes-and-outdoors.md` |
| Winter sports, Christmas markets, thermal rhythm | `references/winter-ski-and-christmas.md` |
| Border hops and nearby add-ons | `references/border-hops-and-day-trips.md` |
| **Regions and Cities** | |
| Vienna playbook | `references/vienna.md` |
| Salzburg and Salzkammergut playbook | `references/salzburg-and-salzburgerland.md` |
| Innsbruck and Tyrol playbook | `references/innsbruck-and-tyrol.md` |
| Graz and Styria playbook | `references/graz-and-styria.md` |
| Carinthia and lake districts playbook | `references/carinthia-and-lakes.md` |
| Danube, Linz, and Wachau playbook | `references/danube-linz-and-wachau.md` |
| **Lifestyle and Execution** | |
| Food, coffeehouse, Heuriger, and meal rhythm | `references/food-guide.md` |
| Family pacing and mixed-age planning | `references/family-travel.md` |
| Accessibility and low-mobility planning | `references/accessibility.md` |
| Emergencies, mountain risk, and disruption logic | `references/safety-and-emergencies.md` |
| Climate and seasonality planning | `references/weather-and-seasonality.md` |
| Connectivity, apps, roaming, and tickets | `references/telecoms-and-apps.md` |
| Research sources map | `references/sources.md` |
| Core Rules, Traps, & Security | `references/core-rules.md` |

| Evaluation harness only | `test-prompts.json` |

## Related Skills
Consider using these skills if the user needs them:
- `travel` — General trip planning and itinerary structure
- `car-rental` — Better rental strategy and handoff logistics
- `booking` — Reservation workflows and confirmation hygiene
- `food` — Deeper restaurant and cuisine recommendations
- `german` — Language support for bookings, transport, and service interactions
