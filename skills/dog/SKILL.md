---
name: dog
description: >
  Track dog health, walks, training, routines, travel, and vet coordination with
  species-aware memory and emergency triage. Use when the user mentions a real
  dog or puppy they live with, foster, rescue, or regularly care for; reports
  symptoms, walks, training, behavior, boarding, sitter prep, medication logs, or
  supply reorders; or needs conservative non-diagnostic triage before a vet visit.
  Not for generic animal trivia, memes, fictional pets, livestock, or cats.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🐕","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"memory":"Durable household facts that outlive a single dog-care session.","remind":"Walk, medication, and appointment nudges the user already decided to schedule.","shopping":"Food, gear, and supply purchase decisions beyond simple reorder thresholds.","travel":"Human travel logistics when pet boarding or pet travel is only one part of the trip.","photos":"Photo library organization when dog photos need indexing rather than care records."}'
---

# Dog

Practical dog-care operations for real household, foster, and rescue dogs:
triage, records, walks, training, behavior context, travel handoffs, and supply
thresholds. Preserve conservative medical boundaries; this skill never replaces
a veterinarian.

## State location

Dog state may exist in `<workspace>/dog/`, `<workspace>/memory/dog/`, or
`~/dog/`. `<workspace>` is the workspace root supplied by the host/runtime.

Before any state read, query, create, update, or delete, resolve `<state_root>`
once:

1. Use an explicitly configured path supplied by the user or host when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/dog/`, `<workspace>/memory/dog/`, `~/dog/`.
3. When multiple candidates exist, use only the highest-precedence path, tell the
   user about duplicates, and leave the others unchanged — never merge silently.
4. If none exists and state must be created, default to `<workspace>/dog/` when
   the host supplied `<workspace>`; otherwise ask for an explicit path before
   creating data.
5. Create the resolved directory path itself rather than a literal directory
   named `<state_root>`.

Use the selected `<state_root>` for every state operation in this skill. Legacy
paths such as `~/Clawic/data/dog/` are migration sources only — copy with
explicit user consent after verify; do not auto-delete or auto-move.

## Setup

On first use, or when `<state_root>/memory.md` is missing or empty, read
`references/setup.md` for activation preference, local-memory consent, and the
current dog roster. Keep setup light and continue helping the live problem
immediately. Seed structure from `assets/memory-template.md` only after consent.

## When to use

- Real dog or puppy care the user lives with, fosters, rescues, or regularly manages
- Symptom triage, walks, training, behavior incidents, routines, travel/boarding
- Vet logistics, medication logs, shopping thresholds, sitter packs, milestone memory

Prefer other skills when the ask is mainly:

- Durable facts outside dog care → `memory`
- Timed nudges already decided by the user → `remind`
- Purchase research beyond reorder thresholds → `shopping`
- Broader human travel system design → `travel`
- Photo library indexing → `photos`

## Architecture

```text
<state_root>/
├── memory.md           # Household summary, activation, red flags, shared rules
├── dogs/
│   └── {name}/
│       ├── profile.md
│       ├── timeline.md
│       ├── health.md
│       ├── routines.md
│       ├── behavior.md
│       ├── training.md
│       └── logistics.md
├── shopping.md         # Shared supplies and reorder thresholds
└── sitter-packs/       # Exportable care instructions for trips or absences
```

## Routing

Keep `SKILL.md` as the progressive-disclosure router; load the smallest relevant
file before writing advice into memory.

| Situation | Load |
|---|---|
| First activation / consent / roster | `references/setup.md` |
| Memory and per-dog file shapes | `assets/memory-template.md` |
| Emergency and same-day triage | `references/triage.md` |
| Daily, weekly, monthly care load | `references/routines.md` |
| Training cues and threshold management | `references/training.md` |
| Behavior patterns and escalation | `references/behavior.md` |
| Travel, boarding, sitter packs | `references/travel.md` |
| Records, meds, shopping, reports | `references/records.md` |
| Gate 6 verified sources | `references/sources.md` |

## Scope

This skill ONLY:

- Helps manage real-world dog care, records, logistics, walks, and behavior tracking
- Uses local files under `<state_root>/` when the user approves memory
- Gives conservative triage and preparation support for veterinary conversations

This skill does NOT:

- Diagnose disease or behavior disorders with certainty from chat alone
- Recommend medication doses, human medicines, or unsafe home toxicology fixes
- Default to punishment-heavy training
- Write memory without user approval
- Replace emergency or diagnostic veterinary care

## Core rules

### 1. Start with dog-specific triage

Use `references/triage.md` before advising on symptoms or sudden changes.

Ask only for facts that change risk:

- age and life stage
- size when heat or bloat risk matters
- appetite, water, stool, urine, and energy
- vomiting, diarrhea, coughing, limping, or pain signs
- toxins, trauma, overheating, and current medication
- whether the change happened during exercise, after eating, or after a trigger

If breathing trouble, collapse, seizure, toxin exposure, heavy bleeding, major
trauma, heat injury, or a swollen abdomen with unproductive retching appears,
switch to emergency guidance immediately and stop non-urgent planning.

### 2. Keep one living record per dog

Use `references/records.md` and `assets/memory-template.md`.

Store durable facts such as:

- identity, age range, weight range, and microchip
- conditions, allergies, meds, and regular vet details
- normal walk load, feeding pattern, and elimination baseline
- training progress, triggers, and handling limits
- boarding, sitter, travel, and gear notes

Separate confirmed facts from guesses. Date symptom changes, incidents,
appointments, and medication events.

### 3. Exercise and enrichment must fit the actual dog

Use `references/routines.md` before prescribing more activity.

Match the plan to age and recovery state, breed tendencies without stereotyping,
weather and heat risk, pain or mobility limits, and the dog's real threshold
around people, dogs, bikes, or noise.

### 4. Training means clear cues and reinforcement

Use `references/training.md` and `references/behavior.md` together.

Default to:

- one cue for one behavior
- immediate, repeatable reward timing
- distance from triggers before adding difficulty
- short sessions with clean resets
- management tools when the dog cannot yet succeed

Prioritize positive reinforcement and safe on-leash work when recall is not earned.

### 5. Behavior plans need context, not labels

When the user says "reactive," "stubborn," "anxious," or "aggressive," ask what
actually happened. Track trigger, distance, intensity, duration, recovery time,
and what made it better or worse. Ensure a medical or pain review when behavior
changes quickly.

### 6. Coordinate logistics proactively but safely

Use `references/records.md` for vet prep, meds, shopping, and sitter packs.

Support walk and medication schedules, appointment prep, food and gear reorder
thresholds, and boarding/sitter/travel handoffs. Use only exact prescribed doses,
support continuing prescribed medication, and escalate heat or bloat warnings
immediately.

### 7. Preserve progress without noise

Keep shared `memory.md` small. Use each dog's timeline for dated facts worth
resurfacing later: clean recall milestones, first successful crate or car ride,
post-surgery checkpoints, major trips, and memorable moments the user wants kept.

## Common traps

- Treating a pain-driven behavior shift as obedience failure
- Adding intensity when the dog is already over threshold
- Recommending exercise during heat or illness
- Calling off-leash reliability good enough before proofing under distraction
- Saving every small walk detail into memory

## External endpoints

This skill makes no external network requests.

| Endpoint | Data sent | Purpose |
|---|---|---|
| None | None | N/A |

## Security and privacy

**Data that leaves the machine:** none.

**Data stored locally if the user approves memory:**

- household summary and activation preference in `<state_root>/memory.md`
- one per-dog record with profile, health, routines, behavior, training, logistics
- supply thresholds and sitter notes

**This skill does not:**

- access files outside `<state_root>/` for storage
- send dog data to third parties
- create automations or reminders automatically
- replace veterinary care for emergencies or diagnosis
