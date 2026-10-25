---
name: home
description: >
  Practical living-space guidance for renters and owners: safety boundaries,
  maintenance priorities, layout and energy basics, organization, starter plants,
  and budget sequencing. Use when the user asks how to improve, maintain, or
  organize a home or apartment day-to-day. Prefer `house` for buy/sell/landlord
  decisions, `smart-home` or `iot` for hubs and protocols, `home-renovation` for
  remodel scope, `plants` for ongoing plant care, and `buy` for purchase research.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🏠"}'
---

# Home

Advise-only living-space guidance for people who already occupy a home or
apartment. This skill does not store durable user state, publish external
content, or give licensed electrical, gas, structural, legal, or tax advice.

Load `references/sources.md` before repeating detector intervals, MERV guidance,
cleaning-chemical rules, Matter claims, or energy claims. Prefer official pages
over memory.

## When to use

Use this skill when the user wants:

- day-to-day home or apartment improvement advice
- safety-first boundaries for DIY vs licensed work
- maintenance priorities and leak/HVAC urgency
- furniture layout, lighting layers, energy basics
- organization and clutter rules of thumb
- starter indoor plants and budget sequencing

Route away when the ask is mainly:

- buy, sell, landlord, permit, or financing decisions → `house` / `home-buying`
- hubs, Matter/Thread commissioning, VLAN hardening → `smart-home` / `iot`
- remodel scope, contractors, change orders → `home-renovation`
- ongoing plant tracking or diagnosis → `plants`
- deep purchase comps and negotiation scripts → `buy`

## Operating sequence

1. **Clarify constraints** — rent vs own, who lives there (kids, pets, mobility), room photos/dimensions when layout advice matters, landlord limits for renters.
2. **Safety first** — load `references/safety.md` for gas, panel, structural, chemical, detector, and heater boundaries before any DIY steps.
3. **Prioritize** — load `references/maintenance.md` for water damage, HVAC filters, gutters, and caulk urgency.
4. **Improve living quality** — load `references/layout-energy.md` for furniture fit, lighting layers, energy habits, organization, plants, and budget order.
5. **Hand off** — send connected-device, remodel, purchase, or plant-tracking work to the related skill instead of duplicating it here.

## Universal rules

- Renters need reversible changes; owners may invest in permanent work after checking permits via `house` / `home-renovation`.
- Water damage and active leaks are urgent; aesthetics wait.
- Licensed pros handle gas, main electrical panel, and structural work — do not provide DIY tutorials for those domains.
- Never mix bleach with ammonia or acids.
- Start smart-home changes in one room; prefer Matter-capable devices and local control for critical paths, then hand off deep setup to `smart-home`.
- Storage systems must be easier than the mess, or they will be abandoned.

## Resource map

| Need | Load |
|------|------|
| Citations and fragile facts | `references/sources.md` |
| DIY vs pro, chemicals, detectors, heaters | `references/safety.md` |
| Leaks, HVAC filters, gutters, caulk | `references/maintenance.md` |
| Layout, energy, organization, plants, budget | `references/layout-energy.md` |
