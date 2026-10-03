# Dog Records and Logistics

## Per-dog files under `<state_root>/dogs/{name}/`

Maintain these files when the user approves storage:

- `profile.md` for durable identity, health baseline, and preferences
- `timeline.md` for dated symptom changes, appointments, milestones, and incidents
- `health.md` for labs, vaccines, meds, and vet follow-up questions
- `training.md` for cue reliability, trigger distance, and handling progress
- `behavior.md` for trigger logs and escalation notes
- `routines.md` for walk, feed, and enrichment load
- `logistics.md` for microchip, insurance, sitter, boarding, and travel notes

These are runtime state files under `<state_root>/`, not skill package resources.
Skill guidance for those topics lives in `references/training.md`,
`references/behavior.md`, `references/routines.md`, and `references/travel.md`.

## Medication tracking

Record:

- medication name
- purpose as given by the vet
- schedule
- start date
- refill point
- any side effect the user reports

Use only the exact dose already prescribed by the veterinarian.

## Appointment prep

Before a vet visit, prepare:

- the change timeline
- appetite, elimination, energy, and pain notes
- current medications and last doses given
- questions the user wants answered
- photos or videos only if the user already has them and they change the decision

## Shopping and supplies

Use `<state_root>/shopping.md` for shared reorder thresholds:

- food and treats
- waste bags and cleanup gear
- meds and preventatives the vet already prescribed
- leash, harness, crate, and travel gear

When the user wants purchase research beyond a threshold, hand off to `shopping`.

## Sitter packs

Export a concise care pack under `<state_root>/sitter-packs/` for trips or absences:

- feeding and medication schedule
- walk load and handling limits
- emergency clinic and vet contacts the user provided
- known triggers and management tools
- what success looks like for the absence window
