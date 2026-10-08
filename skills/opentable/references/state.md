# State and security - OpenTable

## Architecture

Memory lives in the resolved `<state_root>/`. See `references/memory-template.md` and `assets/memory-template.md` for field templates.

```text
<state_root>/
├── memory.md            # Current strategy, goals, and integration state
├── reservation-log.md   # Demand patterns, pacing changes, and outcomes
├── guest-signals.md     # No-show patterns, special requests, and friction points
└── incidents.md         # Overbooking, outage, and recovery records
```

## Data storage

Local notes stay under `<state_root>/`:

- strategy snapshot and current priorities in memory file
- reservation pacing and demand signals in reservation log
- guest behavior patterns in guest signals file
- incident timeline and mitigations in incidents file

Create or update these files only after the user opts into persistent tracking.

## Security and privacy

Data that leaves your machine by default:

- none required by this playbook itself

Data that stays local:

- operational notes and decisions stored under `<state_root>/`
- local experiment and incident logs without full guest datasets

This skill does NOT:

- configure or execute authenticated OpenTable API access by itself
- request hidden background data collection
- persist credentials in local markdown files
- run undeclared network destinations
