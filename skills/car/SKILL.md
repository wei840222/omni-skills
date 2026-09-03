---
name: car
description: "Guide car buying, maintenance, roadside emergencies, and ownership cost checks. Use when the user needs negotiation help, repair triage, warning-light guidance, trip prep, or insurance/claim next steps for a personal vehicle; not for rental-car logistics (`car-rental`) or household cash-flow sequencing (`money`)."
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🚗"}'
  related-skills: '{"buy":"General purchase research, scam checks, and deal negotiation beyond vehicle-specific buying.","money":"Household affordability and cash-flow limits around ownership costs.","price":"Fair-market and deal-timing checks before locking a purchase price."}'
---
## State location

This skill is stateless. It does not store local configuration or runtime data.

## Decision Tree

| Situation | Action |
|-----------|--------|
| Buying a car | Check `references/buying.md` for price negotiation, inspection checklist, financing |
| Maintenance due or warning light | Check `references/maintenance.md` for schedules, DIY vs mechanic, symptom diagnosis |
| Breakdown or accident | Check `references/emergencies.md` for immediate steps, who to call, documentation |
| Road trip planning | Pre-trip checklist below, then `references/emergencies.md` for kit and what-ifs |

---

## Pre-Trip Checklist

Before any long drive:
- [ ] Tire pressure (including spare) at recommended PSI
- [ ] Oil level between min/max marks
- [ ] Coolant reservoir at proper level
- [ ] All lights working (headlights, brake, turn signals)
- [ ] Windshield washer fluid filled
- [ ] Wiper blades wiping cleanly
- [ ] Phone charger and emergency contact numbers accessible

---

## Warning Lights — Quick Reference

| Light | Severity | Action |
|-------|----------|--------|
| Check engine (steady) | Medium | Safe to drive, diagnose within days |
| Check engine (flashing) | Critical | Stop driving, call tow |
| Oil pressure | Critical | Stop immediately, check oil level |
| Temperature/coolant | Critical | Pull over, let engine cool, check coolant |
| Battery | Medium | Drive to shop, may have 30-60 min before stall |
| ABS | Low | Brakes work, but ABS disabled — drive carefully |
| Tire pressure | Low | Check and inflate soon |

---

## Cost Sanity Check

Before approving any repair, verify the quote:
1. Get the exact repair name (e.g., "replace water pump" instead of "fix the engine")
2. Search "[repair name] + [car model] + cost" for typical range
3. Labor: $80-150/hr is normal; over $200/hr is premium/dealer
4. If quote is 50%+ above average, get a second opinion

Common repairs (USD):
- Oil change: $30-75
- Brake pads (pair): $150-300 installed
- Battery replacement: $150-250
- Alternator: $400-600
- Timing belt: $500-1000

---

## Fuel Efficiency Tips

- Optimal highway speed: 55-65 mph (above 65, efficiency drops ~15%)
- Tire pressure: check monthly, underinflation costs 0.2% per PSI
- AC vs windows: AC more efficient above 45 mph
- Remove roof racks when not in use (5% drag penalty)
- Turn off the engine if stopped for more than 30 seconds

---

## When to Load More

| Situation | Reference | When to load |
|-----------|-----------|--------------|
| Buying new or used, financing, negotiation | `references/buying.md` | Load when the user asks for advice on buying a vehicle, negotiations, or checking car values. |
| Maintenance schedules, DIY repairs, diagnostics | `references/maintenance.md` | Load when the user asks about maintenance intervals, DIY vs mechanic advice, or cost estimates for repairs. |
| Accidents, breakdowns, insurance claims | `references/emergencies.md` | Load when the user is stuck on the road, has a breakdown, or is involved in an accident. |
