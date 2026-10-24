---
name: colombia
description: "Plan travel across Colombia. Use when creating region-specific itineraries (Bogotá, Medellín, Cartagena, Coffee Triangle), checking entry/visa rules, understanding weather logistics, or tourist safety tips."
metadata:
  openclaw: '{"emoji": "🇨🇴"}'
  related-skills: '{"argentina": "Argentina trip planning for multi-country South America routes.", "booking": "Availability and reservation workflows after a Colombia route is chosen.", "brazil": "Brazil trip planning for multi-country South America routes.", "flight": "Flight search and connection logic feeding Colombia arrival/departure choices.", "mexico": "Mexico trip planning when the user compares or chains Latin America destinations.", "spain": "Spain trip planning when the user is comparing Iberian vs Andean/Caribbean options.", "travel": "General multi-destination trip framing outside Colombia-specific routing.", "travel-planning": "Cross-country itinerary structure when Colombia is only one segment."}'
---

## Setup

If `<state_root>/` does not exist or is empty, read `scripts/setup.md` and start naturally.

## When to load

Load this skill when the user is planning a Colombia trip and needs practical guidance on entry requirements, region choice, route design, altitude and climate fit, transport tradeoffs, or on-the-ground execution.

## State location

Colombia state may exist in `<workspace>/colombia/`, `<workspace>/memory/colombia/`, or `~/colombia/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/colombia/`, `<workspace>/memory/colombia/`, `~/colombia/`.
3. If none exists and state must be created, default to `<workspace>/colombia/`.

Use the selected `<state_root>` for every state operation in this skill.

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
| Primary sources & Gate 6 anchors | `references/sources.md` |
