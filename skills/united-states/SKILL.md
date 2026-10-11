---
name: united-states
description: Plan United States itineraries. Use when users need entry requirement checks, route design, transport strategies, seasonal weather planning, and on-the-ground execution tips for U.S. travel.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "\ud83c\uddfa\ud83c\uddf8"}'
  related-skills: '{"booking": "Reservation workflows and confirmation hygiene.",
    "car-rental": "Better rental strategy and handoff logistics.", "english": "Language
    support for calls, bookings, and service interactions.", "food": "Deeper culinary
    planning for each destination.", "travel": "General trip planning and itinerary
    structure."}'
---


## State location

United States trip state may exist in `<workspace>/united-states/`, `<workspace>/memory/united-states/`, or `~/united-states/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/united-states/`, `<workspace>/memory/united-states/`, `~/united-states/`.
3. If none exists and state must be created, default to `<workspace>/united-states/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

If `<state_root>/` doesn't exist or is empty, read `references/setup.md` and start naturally.

## Reference Router

Load references on-demand based on the user's focus:

- **Entry & Admin:** `references/entry-and-documents.md` (visa/ESTA/IDs), `references/customs-and-border.md` (cash/restricted items).
- **Core Strategy:** `references/regions.md` (route strategy), `references/itineraries.md` (sample routes), `references/domain.md` (core rules and common traps).
- **Logistics:** `references/transport-domestic.md` (flights/rail), `references/road-trips-and-driving.md` (driving), `references/budget-and-costs.md` (pricing/math), `references/accommodation.md`.
- **Destinations:** `references/national-parks.md`, `references/new-york-city.md`, `references/washington-dc.md`, `references/california.md`, `references/florida.md`, `references/southwest-and-rockies.md`, `references/pacific-northwest.md`, `references/great-lakes-and-midwest.md`, `references/deep-south-and-louisiana.md`, `references/hawaii-and-alaska.md`.
- **Execution & Conditions:** `references/weather-and-seasonality.md`, `references/safety-and-emergencies.md`, `references/food-guide.md`, `references/nightlife.md`, `references/family-travel.md`, `references/accessibility.md`.

## Security & Privacy

**Data that stays local:** Trip preferences in `<state_root>/`

**This skill does NOT:** Access files outside `<state_root>/` or make network requests.
