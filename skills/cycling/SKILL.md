---
name: cycling
description: Trigger this skill when the user asks about cycling training, bike fit, power zones, on-bike nutrition, or bicycle safety and maintenance.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🚴","displayName":"Cycling"}'
  related-skills: '{"fitness":"Broader fitness programming, cardio progression, and training plans beyond cycling-specific guidance"}'
---

## State location

This skill is stateless and does not store local configuration or state.

## Quick Reference

Load these references to provide domain knowledge about cycling:

| Reference | When to load |
|---|---|
| `references/bike-fit.md` | When the user asks about saddle height, handlebar reach, cleat position, or general bicycle fit setup. |
| `references/training.md` | When the user asks about FTP, power zones, interval training, cadence, indoor training, or climbing. |
| `references/nutrition.md` | When the user asks about hydration, fueling, gels, carbs, or caffeine before/during a ride. |
| `references/safety-and-maintenance.md` | When the user asks about helmet usage, road safety, maintenance schedule, tire pressure, or chain lubrication. |
