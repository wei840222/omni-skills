# Setup — Buenos Aires continuity

Use only when the user wants context kept across sessions.

## Consent first

1. Explain that continuity would live under the resolved `<state_root>/` (not inside this skill package).
2. Scope is trip/move preferences, barrio shortlist, budget band, and open tasks—not passport scans or passwords.
3. Proceed only after clear consent to create or update files.

## Initialize

1. Resolve `<state_root>` per `SKILL.md` State location (lookup before create).
2. If creating new state, copy structure from `assets/memory-template.md` into `<state_root>/memory.md`.
3. Fill only fields the user supplied; leave unknowns blank.
4. Do not pre-create empty plant-style trees of unused files.

## Update rules

- Update `<state_root>/memory.md` when barrio choice, dates, budget band, or open paperwork tasks change.
- Prefer short durable facts over chat transcripts.
- On conflict between memory and a fresh user statement, trust the fresh statement and rewrite the field.
