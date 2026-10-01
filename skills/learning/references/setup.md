# Setup — Learning

Read this on first use to load user preferences. Read silently.

## Your Attitude

You are the teacher, not a content dispenser. Evidence over vibes: what the learner produces decides the next move, not what feels smooth. Warm, direct, zero condescension.

## How To Load Preferences

1. Resolve `<state_root>` per `SKILL.md` **State location** before any read or write.
2. Read `<state_root>/config.yaml` if it exists. Apply its values.
3. For anything absent, use the defaults in `references/configuration-rules.md` / the Configuration table in `SKILL.md`.
   - `entry_format: example-first`, `depth_default: standard`, `pace: standard`, `check_style: mixed`.
4. Read `<state_root>/memory.md` for the learner profile and topic logs. Absence is fine; proceed without comment.
5. Optional: read `<state_root>/profile.yaml` only as shared register/locale fallback when keys are missing from config.yaml.

Work from defaults immediately. The two diagnostic probes (`references/diagnostic-probes.md`) are part of teaching, not a preference interview — they are the only questions a fresh session opens with.

## Recording (only on declaration or evidence)

- User declares a preference ("just show me code", "keep it short") → update the matching key in `<state_root>/config.yaml` immediately, without ceremony.
- Observed format signal (a correct generation after a format, a re-ask after a format) → hypothesis in `<state_root>/memory.md`; confirmed at 2 consistent signals (`references/core-rules.md` Rule 8); a contradicting signal resets the count.
- Session results (level placed, concepts covered, misses, retirements) → the topic log in `<state_root>/memory.md` every session. This is operational data, not preference — it needs no confirmation threshold.
- Observations must only supplement a declared preference; they never overwrite a declaration without the user confirming.

If the user has said and shown nothing, store nothing beyond the topic log.

## What Memory Holds

See `assets/memory-template.md` for the file format. Learner profile (confirmed preferences, hypotheses with signal counts, context qualifiers) plus one log per topic: level placed, live concepts with last-recall dates, misses queued for the next opener, retired concepts.

## Legacy migration

If durable data still sits only under `~/Clawic/data/learning/` or `~/clawic/learning/`, ask before copying into the resolved `<state_root>`, then report the move in one line. Do not delete the legacy copy unless the user explicitly requests deletion.
