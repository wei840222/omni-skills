---
name: pets
description: Track and care for pets with profiles, routines, behavior logging, training progress, and creative projects.
metadata:
  openclaw: '{"emoji": "🐾", "requires": {"bins": []}, "os": ["linux", "darwin", "win32"],
    "displayName": "Pets"}'
---

## When to load

Load this skill when the user mentions their pets, asks about pet care, wants to log pet activities, track training progress, or generate pet-related reports and creative content.

## State location

Memory lives in `<state_root>/pets/`.

```
<state_root>/pets/
├── index.md                    # List of all pets with quick stats
└── {pet-name}/
    ├── profile.md              # Species, breed, age, personality, quirks
    ├── routines.md             # Feeding, walks, grooming schedule
    ├── log.jsonl               # ALL events: incidents, wins, moments, anything
    ├── training.md             # Commands learned, in progress, methods that work
    └── photos/                 # Saved photos and created images
```

## Quick Reference

| Topic | File |
|-------|------|
| Core operations | `references/core-operations.md` |
| Storage structure | `references/storage.md` |
| Behavior tracking | `references/behavior.md` |
| Training methods | `references/training.md` |
| Routines and reminders | `references/routines.md` |
| Creative projects | `references/creative.md` |
| Report generation | `references/reports.md` |

## Core Execution

1. Read `<state_root>/pets/{pet}/profile.md` to understand the pet's personality, needs, and history.
2. Log everything — incidents, wins, funny moments, milestones, observations.
3. Track training progress and spot behavioral patterns.
4. Generate reports on request with trend analysis.
5. Manage routines and creative projects.

See `references/core-operations.md` for detailed workflows.

## Boundaries

- Medical inquiries go to a vet — log symptoms but do not diagnose or recommend treatments.
- Breed decisions are outside scope — too personal, depends on lifestyle.
- Behavior logging is encouraged; diagnosing behavioral disorders is outside scope.
