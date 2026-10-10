---
name: electric-guitar
description: >
  Plan electric guitar practice, diagnose picking and fretting problems, shape
  amp/pedal tone, and track progress. Use when the user asks to learn, practice,
  troubleshoot, tone-shape, or log work on an electric guitar. Prefer
  `acoustic-guitar` for unplugged fingerstyle and humidity care, `piano` or
  `drums` for those instruments, `music` for listening history, and `song` for
  original writing.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🎸"}'
  related-skills: '{"acoustic-guitar":"Unplugged fingerstyle, strumming, and acoustic care instead of amplified tone work.","drums":"Drum-kit practice and rudiments instead of electric guitar work.","habits":"Design the recurring practice habit once the electric routine itself is clear.","music":"Track listening history, playlists, and concerts rather than guitar technique.","piano":"Keyboard practice plans and technique instead of electric guitar.","song":"Original songwriting, lyrics, and harmony when composition is the goal."}'
---

## State location

Practice state may exist in `<workspace>/electric-guitar/`, `<workspace>/memory/electric-guitar/`, or `~/electric-guitar/`. Before reading or writing practice data, resolve `<state_root>` as follows:

1. Use an explicitly configured state root when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/electric-guitar/`, `<workspace>/memory/electric-guitar/`, then `~/electric-guitar/`.
3. If no candidate exists and the user asks to save practice data, create `<workspace>/electric-guitar/` only after confirming the destination.
4. If several candidate directories exist, use only the highest-precedence one, tell the user that separate copies were detected, and leave the others unchanged.

Use the selected `<state_root>` for every practice-state operation in this invocation. Do not hardcode absolute host paths. Do not write runtime practice data into the skill package. Never treat the literal string `<state_root>` as a filesystem path.

## Workflow

1. Establish the player's immediate goal: rhythm or lead; style (rock, blues, metal, jazz, other); gear context (amp, pedals, pickup position); and the next concrete outcome.
2. Give one focused exercise with a tempo or repetition target, then name the observable cue for clean execution.
3. When a technique, tone, troubleshooting, or logging detail is needed, load the matching reference below rather than loading every reference at once.
4. When the user wants persistent tracking, confirm the state root and update only the requested records.

| Resource | Load when |
| --- | --- |
| `references/domain.md` | Explaining alternate picking, bending, vibrato, palm muting, CAGED/triads, level-based traps, tone defaults, or symptom-based fixes. |
| `references/state.md` | Creating or updating repertoire, session, technique, or goal records in `<state_root>`. |
| `references/sources.md` | Verifying technique terminology, tone basics, or Agent Skills packaging facts. |

## Practice defaults

- Apply one correction at a time and verify it with a short, observable check before adding another change.
- Ask only the questions that change the advice: style, gear, current ability, and the next goal.
- Clean beats speed: drop tempo until the motion is even, then rebuild.
- Prefer rhythm stability before lead ornamentation when both are weak.
- Keep gain low enough that note starts and stops remain audible during practice.
- If pain is sharp, radiating, or persists after rest, pause technical drills and recommend a qualified teacher or clinician rather than forcing more pressure, stretch, or repetition.
- After pain settles, return to lighter fretting and open-position drills before retrying high-tension techniques.

## Quick defaults before deep references

- Bends off pitch → fretted target note first, then bend to match; check reference fretted pitch.
- Solos feel random → land chord tones on harmony changes; escape pure pentatonic boxes with triads.
- Rhythm sloppy → muted downstrokes or palm-muted 16ths to a click before adding fretted notes.
- Can't play clean at tempo → practice at about 60% speed until alternate picking stays even.
