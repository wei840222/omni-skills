---
name: garden
description: Track plants, zones, tasks, harvests, and climate-aware rotations across seasons. Use when managing gardens, diagnosing plant issues, planning rotations, or reviewing yields. Also use for plant care questions, seasonal planning, or when the user mentions their garden, plants, or growing conditions.
metadata:
  version: "1.1.6"
  openclaw: '{"emoji":"🌱"}'
  related-skills: '{"daily-planner":"Places garden work into daily priorities and time blocks.","habits":"Turns recurring garden care into trackable routines.","journal":"Captures free-form garden observations outside structured records.","plants":"Extends garden with plant-specific care and identification.","remind":"Schedules watering and seasonal task reminders."}'
---

## State Location

Garden state may exist in `<workspace>/garden/`, `<workspace>/memory/garden/`, or `~/garden/`. `<workspace>` means the workspace root provided by the host/runtime, not the shell's current working directory.

Before any state read, query, create, update, or delete, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/garden/`, `<workspace>/memory/garden/`, `~/garden/`.
3. If none exists and state must be created, default to `<workspace>/garden/`.

If multiple candidate directories exist, use only the first one, tell the user that multiple state directories were found, and do not merge or modify the others. Use the selected `<state_root>` for every state operation during the run. Never create a directory whose literal name is `<state_root>`.

## Setup

After resolving `<state_root>`, if `<state_root>/memory.md` doesn't exist or is empty, read `references/setup.md` and follow it.

## Core Workflows

### First-Time Setup
1. Resolve `<state_root>` using State Location procedure
2. If `<state_root>/memory.md` missing → read `references/setup.md`, gather user context
3. Before creating files, confirm with user: "I'll create garden tracking files at `<state_root>`. OK?"
4. Create `<state_root>/memory.md` using template from `references/memory.md`
5. Ask: "Do you want detailed tracking for plants, zones, and harvests?" → if yes, create additional files

### Adding a Plant
1. User says "I planted tomatoes" or similar
2. If plant name already exists in `<state_root>/plants/`, ask: "This plant already exists. Update existing or create new variety?"
3. Create `<state_root>/plants/{name}.md` using template from `references/tracking.md`
4. Update `<state_root>/memory.md` → add to "Current Plants" section
5. Log action in `<state_root>/log/YYYY-MM.md` with 🌱 icon

### Diagnosing a Problem
1. User reports issue (yellow leaves, pests, etc.)
2. Load `<state_root>/plants/{name}.md` → check health history
3. Load `<state_root>/zones/{zone}.md` → check conditions
4. Read `references/diagnostics.md` → follow IPM framework
5. Update plant's health log with diagnosis and treatment
6. When recommending chemical treatment, confirm with user before proceeding

### Planning Next Season
1. User asks "What should I plant?"
2. Load all `<state_root>/zones/*.md` → check rotation history
3. Load `<state_root>/climate.md` → check frost dates
4. Read `references/planning.md` → apply rotation rules
5. Suggest crops that fit rotation constraints and climate window

## Architecture

State lives under the resolved `<state_root>`. See `references/memory.md` for templates.

```text
<state_root>/
├── memory.md      # REQUIRED: context and status
├── climate.md     # Optional: zone, frost dates
├── plants/        # Optional: detailed plant files
├── zones/         # Optional: zone tracking
├── harvests.md    # Optional: yield records
└── log/           # Optional: monthly activity logs
```

Start minimal (just `<state_root>/memory.md`). Add others only if the user wants detailed tracking.

## Quick Reference

| Topic | File | When to Load |
|-------|------|--------------|
| Setup process | `references/setup.md` | First use, or when `<state_root>/memory.md` is missing |
| Memory template | `references/memory.md` | Creating or updating `<state_root>/memory.md` |
| Plant & zone templates | `references/tracking.md` | Creating new plant or zone files |
| Climate configuration | `references/climate.md` | Setting up climate, planning planting dates |
| Problem diagnosis | `references/diagnostics.md` | User reports plant health issues |
| Rotation planning | `references/planning.md` | Planning next season, checking rotation constraints |
| Data templates | `assets/garden-data-templates.md` | Need copyable templates for state files |

## Core Rules

### 1. Plant Registry
Each plant gets a file at `<state_root>/plants/{name}.md` with: variety, planting date, zone, care schedule, health history. Load on request, not by default.

### 2. Zone Management
Each garden area gets a file at `<state_root>/zones/{name}.md` with: conditions, current plants, rotation history. Enforce 3-4 year minimum before repeating same plant family (Iowa State Extension, 2025).

### 3. Activity Logging
Log actions in `<state_root>/log/YYYY-MM.md` with icons: 🌱 plant, 💧 water, 🐛 pest, 🍅 harvest, ✂️ prune, 🌡️ weather event.

### 4. Climate Awareness
The user configures `<state_root>/climate.md` with USDA zone and frost dates. Use it for planting window calculations and seasonal alerts.

### 5. Harvest Tracking
Log yields in `<state_root>/harvests.md` with date, plant, zone, and quantity. This enables season-over-season comparison and variety evaluation.

### 6. Problem Diagnosis
When user reports issue: check plant health history, zone conditions, recent weather. Apply IPM framework (identify, assess threshold, prevent, control with least-risk methods). See `references/diagnostics.md` for symptom reference.

### 7. Tiered Storage
- `<state_root>/memory.md` = current focus, always loaded first
- `<state_root>/plants/` and `<state_root>/zones/` = load on demand
- `<state_root>/log/` = historical reference only

## Common Queries

- "What needs water?" - check care schedules against `<state_root>/log/`
- "What can I plant now?" - frost dates + rotation rules
- "Why yellow leaves?" - diagnostic flow in `references/diagnostics.md`
- "Show tomato history" - load `<state_root>/plants/{name}.md`
- "Last year's harvest?" - aggregate from `<state_root>/harvests.md`

## Gotchas

- **Rotation enforcement**: Always check `<state_root>/zones/{zone}.md` rotation history before planting. Same family in same zone within 3-4 years = disease buildup.
- **Microclimate variance**: Different zones may have different frost dates. Check `<state_root>/climate.md` microclimate notes, not just USDA zone.
- **Log before you forget**: Record problems immediately in `<state_root>/plants/{name}.md` health log. Delayed diagnosis is harder.
- **Soil over schedule**: Check soil moisture first — overwatering kills more plants than underwatering.
- **Hardiness zone drift**: USDA zones shifted in 2023. Verify current zone at planthardiness.ars.usda.gov before planting zone-sensitive crops.
- **Resolve state first**: Resolve `<state_root>` before any file operation; write only to the resolved `<state_root>`.
- **Verify climate data**: Check `<state_root>/climate.md` exists before using frost dates. If missing, ask user to configure.
- **Confirm chemical treatment**: IPM chemical control step requires explicit user approval.
- **Confirm file creation**: First-time setup requires user confirmation before writing to `<state_root>`.
- **Confirm before deletion**: Deletion is irreversible. Confirm with user before removing records.
- **Request missing data**: Ask user for required fields (dates in YYYY-MM-DD, numeric quantities, non-empty names).
- **Use resolved state root**: Use resolved `<state_root>` for all state writes; the current working directory is unrelated.
- **Report write failures**: If write fails, clean up and report. Leave no incomplete records.

## Failure Modes

### State location not found
If no candidate directory exists and user hasn't specified a location:
- Ask user "Where should I store garden data?" before creating files.
- Use the resolved `<state_root>` for all file operations.

### File write errors
If file creation or update fails (disk full, permission denied, invalid path):
- Report error to user: "Cannot write to `<path>`: <error message>"
- Ask user to resolve the issue before continuing.

### Invalid input
If user provides invalid data (wrong date format, missing required fields):
- Ask user to correct: "I need <field> in <format>. Can you provide it?"
- Examples: planting date must be YYYY-MM-DD, zone name cannot be empty, quantity must be numeric.

### Missing plant/zone files
If user references a plant or zone that doesn't exist:
- Create the file first using templates from `references/tracking.md`
- Then proceed with the requested operation
- Ensure complete records for every tracked item.

### Diagnosis without history
If user asks for diagnosis but plant has no health log:
- Record "First diagnosis" in health log
- Treat this as the baseline; prior treatments or conditions are unknown.

### Chemical treatment
If IPM framework reaches chemical control step:
- Confirm with user before recommending any pesticide.
- Explain risks and alternatives first.

### Deleting records
If user asks to delete a plant, zone, or log entry:
- Confirm deletion: "Delete <record>? This cannot be undone."
- Wait for explicit "yes" before proceeding.

## Security & Privacy

- All state lives under `<state_root>`. No network calls, no telemetry.
- Writes: files under `<state_root>`, plus optionally one line in host-provided workspace `MEMORY.md` **only after explicit "yes"**.
- Confirm preferences before inferring them; access weather APIs or control hardware only with user authorization; write outside `<state_root>` only after asking.
