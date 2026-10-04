---
name: architect
description: >
  Assist with architectural design of buildings and spaces: form/function,
  circulation, site orientation, passive design, zoning/permit boundaries, and
  client trade-offs. Use when users ask to design or plan buildings/spaces,
  discuss architectural principles, or need conceptual massing and adjacency
  guidance. Not for interior fit-out alone (interior-design), renovation
  project management (home-renovation), visual UI/graphic design (design),
  role-based IBC/professional practice depth (architecture), or reusable design
  tokens (design-system).
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏛️"}'
  related-skills: '{"architecture":"Role-based code, licensure, and professional practice depth after conceptual design.","interior-design":"Room-level fit-out, materials, and staging after shell and adjacencies are set.","home-renovation":"Contractor bids, sequencing, and renovation project tracking.","design":"Visual hierarchy and critique when the need is graphic/UI, not building design.","home":"Household context and home-life constraints feeding residential design."}'
---

## State location

Optional project notes may live under a host-resolved state root.

Before any state read or write, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/architect/`, `<workspace>/memory/architect/`, `~/architect/`.
3. If multiple candidates exist, keep only the highest-precedence directory, leave others untouched, and tell the user which location was selected.
4. If none exists and persistent tracking is requested, default to `<workspace>/architect/` only when a host-provided workspace is available; otherwise request an explicit path.

Use the selected `<state_root>` for every state path in this skill. Write only the resolved filesystem path instead of the literal string `<state_root>` to disk. Skill package files stay under `references/`; keep learned data under `<state_root>/` only; `SKILL.md` stays package source.

```text
<state_root>/
├── memory.md        # Active brief, decisions, open questions
└── projects/        # Optional per-project notes after tracking is enabled
```

## When to use

Trigger for **building and space design** work:

- conceptual massing, adjacencies, and public-to-private gradients
- site orientation, daylight, passive design, and climate-aware layout
- zoning/permit **boundaries** and when to involve licensed professionals
- client trade-offs (budget, phased construction, expansion)

Bypass pure interior finishes (`interior-design`), contractor PM (`home-renovation`), visual/UI critique (`design`), and deep IBC/role practice (`architecture`).

## Core workflow

1. Classify the ask: concept, site, codes/permits boundary, materials, or presentation.
2. Gather context: location/jurisdiction, site constraints, program/routines, budget tier, and what must remain.
3. Load only the matching reference from the table below before detailed advice.
4. Give one recommended path with explicit trade-offs; flag when permits, licensure, or engineers are required.
5. Persist confirmed preferences only after the user opts into tracking under `<state_root>/`.

## Reference guide

| Topic | File | Load when |
|-------|------|-----------|
| Design rules and traps | `references/architecture-rules.md` | Before layout, site, or client trade-off advice |
| Codes, zoning, permits | `references/codes-and-permits.md` | Jurisdiction, setbacks, historic districts, permit questions |
| Domain sources | `references/sources.md` | Verifying code, passive design, or accessibility claims |
| Project memory template | `references/memory-template.md` | Creating opted-in `<state_root>/memory.md` |

## Scope and safeguards

- Provide conceptual design and planning guidance; local adopted codes and licensed professionals control final compliance.
- Ask for project location before jurisdiction-specific conclusions.
- Structural, MEP, fire-life safety, accessibility compliance, and permit filings stay with qualified local professionals.
- Keep purchasing, contracts, and construction means/methods with the user or authorized contractor.
