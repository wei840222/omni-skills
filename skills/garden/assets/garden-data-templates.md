# Garden Data Templates

This file contains copyable templates for garden state files. The agent reads this when creating new state files.

## `<state_root>/memory.md` Template

```markdown
# Garden Memory

## Status
status: ongoing
version: 1.1.6
last: YYYY-MM-DD
integration: pending

## Context

### Location & Climate
<!-- What you've learned about their growing conditions -->

### Plants
<!-- What they're growing, natural language -->

### Goals
<!-- What matters to them: survival? yields? beauty? -->

## Notes
<!-- User-stated preferences -->
<!-- Example: wants weekly reminders, prefers quick answers -->
<!-- Things to remember for next time -->

---
*Updated: YYYY-MM-DD*
```

## `<state_root>/climate.md` Template

```markdown
# Climate

Zone: [USDA zone]
Last frost: [date]
First frost: [date]
```

## `<state_root>/harvests.md` Template

```markdown
# Harvests

| Date | Plant | Yield | Notes |
|------|-------|-------|-------|
```

## `<state_root>/plants/{name}.md` Template

```markdown
# [Plant Name]

Planted: YYYY-MM-DD
Location: [where]
Notes: [care observations]
```

## `<state_root>/zones/{name}.md` Template

```markdown
# [Zone Name]

## Conditions
- **Size:** [dimensions]
- **Sun:** [full sun / partial shade / shade]
- **Soil:** [soil type, pH if known]
- **Irrigation:** [drip / hand-water / etc.]
- **Microclimate:** [wind shelter, frost pocket, etc.]

## Current Plantings
| Position | Plant | Planted | Status |
|----------|-------|---------|--------|

## Rotation History
| Year | Spring | Summer | Fall |
|------|--------|--------|------|
```

## `<state_root>/log/YYYY-MM.md` Template

```markdown
# YYYY-MM

## Week 1 (Day 1-7)
- 🌱 [planting]
- 💧 [watering]
- 🐛 [pest]
- 🍅 [harvest]
- ✂️ [pruning]
- 🌡️ [weather event]
```

## Log Icons Reference

- 🌱 Planting/seeding
- 💧 Watering/irrigation
- 🐛 Pest activity
- 🍅 Harvest
- ✂️ Pruning/maintenance
- 🌡️ Weather event
- 💀 Plant death/loss
- 📸 Documentation
- 📝 Testing/analysis
