---
name: cat
description: Manage real cat care with triage, litter and behavior workflows, routines,
  travel prep, vet logistics, and portable household records. Use when the user cares
  for a live cat or kitten; skip memes, trivia, and fictional pets.
metadata:
  version: 1.0.0
  openclaw: '{"emoji":"🐈","requires":{"bins":[]},"os":["linux","darwin","win32"],"configPaths":["<state_root>/cat/"],"displayName":"Cat"}'
  related-skills: '{"memory":"Durable household facts when the user wants long-term retention beyond the cat state tree.","photos":"Photo albums and keepsakes after care milestones or memorable moments.","remind":"Medication, appointment, and recurring care nudges once the user already knows the commitment.","shopping":"Food, litter, and supply purchase decisions when restock thresholds are reached.","travel":"Human trip structure when a cat is moving with the user or needs boarding coordination."}'
---

## When to load

Load this skill for real cat or kitten care: symptom triage, litter tracking, routines, behavior, home setup, travel or sitter prep, vet logistics, shopping thresholds, and durable household records.
Prefer this skill over generic pet tracking when cat-specific red flags, litter signals, territory stress, or carrier handling change the plan.
Do not load for memes, animal trivia, fictional cats, or non-cat species as the primary subject.

## State location

Cat state may exist in `<workspace>/cat/`, `<workspace>/memory/cat/`, or `~/cat/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/cat/`, `<workspace>/memory/cat/`, `~/cat/`.
3. If none exists and state must be created, default to `<workspace>/cat/` after the user approves persistence.

Use the selected `<state_root>` for every state operation in this skill. Keep the root fixed for the rest of the invocation.

```text
<state_root>/
├── memory.md           # Household summary, activation, shared red flags
├── cats/
│   └── {name}/
│       ├── profile.md
│       ├── timeline.md
│       ├── health.md
│       ├── routines.md
│       ├── behavior.md
│       └── logistics.md
├── shopping.md         # Shared supplies and reorder thresholds
└── sitter-packs/       # Exportable care instructions for trips or absences
```

This skill can answer one-off questions without writing files. Before creating or changing files under `<state_root>/`, explain the planned write and ask for confirmation.

## Quick Reference

| Topic | File |
|-------|------|
| Core rules, scope, traps | `references/core-rules.md` |
| First activation and roster | `references/setup.md` |
| Memory templates | `assets/memory-template.md` |
| Emergency triage and intake | `references/triage.md` |
| Daily, weekly, monthly care | `references/routines.md` |
| Behavior patterns | `references/behavior.md` |
| Home and multi-cat setup | `references/household.md` |
| Travel, moving, sitter prep | `references/travel.md` |
| Records, meds, shopping | `references/records.md` |
| Official sources map | `references/sources.md` |

Load the matching relative path before topic-specific guidance.

## Core loop

1. For symptoms or sudden change, open `references/triage.md` first and escalate red flags immediately.
2. Keep one living record per cat under `<state_root>/cats/{name}/` after user approval.
3. Treat litter, appetite, and hiding as primary health or stress signals before attitude labels.
4. Fix behavior through environment, routine, and gradual exposure using `references/behavior.md` and `references/household.md`.
5. Plan travel, visitors, and moves around territory and predictability with `references/travel.md`.
6. Coordinate vet prep, meds, shopping, and sitter packs with `references/records.md` using only user- or vet-provided doses.
7. Store durable facts and milestones; keep hot memory small.

## Security and privacy

**Data that leaves the machine**
- None by default. This skill makes no network calls.

**Local data when the user approves storage**
- household summary and activation preference in `<state_root>/memory.md`
- per-cat profile, health, routines, behavior, logistics, and timeline files
- supply thresholds and sitter notes

**Operating limits**
- stay inside `<state_root>/` for skill-owned storage
- do not invent diagnoses or medication doses
- escalate active red flags instead of waiting them out
- require explicit approval before writing memory or creating directories
