# Seville Skill — Setup Guide

## First-time setup

This skill helps navigate Seville for visiting, moving, working, studying, or starting a business.

### Step 1: Initialize your profile

Create your Seville knowledge base under the resolved `<state_root>/`:

```text
<state_root>/
├── memory.md           # Profile + priorities (from assets/memory-template.md)
├── progress.md         # Checklist of completed admin steps
├── bookmarks.md        # Saved places and resources
└── notes.md            # Personal observations
```

### Step 2: Define your context

Copy `assets/memory-template.md` into `<state_root>/memory.md` and fill in:

1. **Your role**: Visitor, potential resident, new resident, established resident
2. **Your timeline**: When arriving, how long staying
3. **Your situation**: EU/non-EU, visa status, employment type
4. **Your priorities**: What matters most (cost, location, lifestyle, heat tolerance)

### Step 3: Choose your path

Based on your role, start with the most relevant files:

| Role | Start with |
| --- | --- |
| Tourist | `visitor-attractions.md`, `visitor-itineraries.md`, `climate.md` |
| Planning to move | `cost.md`, `neighborhoods-choosing.md`, `resident.md`, `sources.md` |
| Recently arrived | `resident.md`, `local.md`, `neighborhoods-index.md` |
| Working remotely | `tech.md`, `startup.md`, `cost.md`, `sources.md` |
| Starting business | `startup.md`, `local.md`, `resident.md` |
| Student | `student.md`, `cost.md`, `neighborhoods-macarena.md` |
| Festival visitor | `fiestas.md`, `visitor-lodging.md`, `transport.md` |

## Using this skill

**Quick reference**: Start with `SKILL.md` — it has the file index organized by topic.

**Deep dive**: Each reference file covers its topic with tables, practical tips, and cost orientation where relevant.

**Asking questions**: Be specific about role, month, budget currency, passport, and quiet vs nightlife priority.

## Tracking progress

Update `<state_root>/progress.md` as steps complete:

```markdown
## Completed
- [x] Got NIE orientation checklist (YYYY-MM-DD)
- [x] Shortlisted Triana / Alameda flats (YYYY-MM-DD)

## In Progress
- [ ] Empadronamiento appointment
- [ ] Confirm summer AC before lease

## Next Steps
- [ ] Open Spanish bank account
- [ ] Register for healthcare orientation
```

Do not store passport numbers, full NIE/TIE values, bank credentials, or card numbers.
