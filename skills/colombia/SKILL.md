---
name: colombia
description: Plan Colombia trips with region-specific routing, verified entry rules,
  weather-aware logistics, and practical tourist safety.
metadata:
  openclaw: '{"emoji": "🇨🇴"}'
  related-skills: '{"travel":"General multi-destination trip framing outside Colombia-specific routing.","travel-planning":"Cross-country itinerary structure when Colombia is only one segment.","booking":"Availability and reservation workflows after a Colombia route is chosen.","flight":"Flight search and connection logic feeding Colombia arrival/departure choices.","mexico":"Mexico trip planning when the user compares or chains Latin America destinations.","brazil":"Brazil trip planning for multi-country South America routes.","argentina":"Argentina trip planning for multi-country South America routes.","spain":"Spain trip planning when the user is comparing Iberian vs Andean/Caribbean options."}'
---

## Setup

If `<state_root>/` does not exist or is empty, read `scripts/setup.md` and start naturally.

## When to load

Load this skill when the user is planning a Colombia trip and needs practical guidance on entry requirements, region choice, route design, altitude and climate fit, transport tradeoffs, or on-the-ground execution.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for structure.

```
<state_root>/
└── memory.md     # Trip context and evolving constraints
```

## Quick Reference

| Topic | File |
|-------|------|
| **Entry and Border** | |
| Visa, Check-Mig, stay limits, health docs | `references/entry-and-documents.md` |
| Customs, cash declarations, island and border notes | `references/customs-and-border.md` |
| **Planning Backbone** | |
| Regions and route strategy | `references/regions.md` |
| Sample itineraries (7-21 days) | `references/itineraries.md` |
| Accommodation strategy | `references/accommodation.md` |
| Budget and cost planning | `references/budget-and-costs.md` |
| **Regions** | |
| Bogota | `references/bogota.md` |
| Medellin & Antioquia | `references/medellin-and-antioquia.md` |
| Cartagena & Caribbean | `references/cartagena-and-caribbean.md` |
| Coffee Region | `references/coffee-region.md` |
| Cali & Pacific | `references/cali-and-pacific.md` |
| Santander & Eastern Andes | `references/santander-and-eastern-andes.md` |
| Amazon & Llanos | `references/amazon-and-llanos.md` |
| San Andres & Providencia | `references/san-andres-and-providencia.md` |
| Colonial Cities & Boyaca | `references/colonial-cities-and-boyaca.md` |
| **Logistics** | |
| Domestic transport | `references/transport-domestic.md` |
| Road trips and driving | `references/road-trips-and-driving.md` |
| Weather and seasonality | `references/weather-and-seasonality.md` |
| Safety and emergencies | `references/safety-and-emergencies.md` |
| Health and accessibility | `references/accessibility.md` |
| **Culture** | |
| Food guide | `references/food-guide.md` |
| Nightlife | `references/nightlife.md` |
| Family travel | `references/family-travel.md` |
| National parks | `references/national-parks.md` |
| **Practical** | |
| Telecoms and apps | `references/telecoms-and-apps.md` |
| Tipping and payments | `references/tipping-and-payments.md` |
