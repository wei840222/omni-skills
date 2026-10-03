---
name: violin
description: >
  Plan violin practice, diagnose left-hand and bow-arm problems, guide basic
  instrument care, and track progress. Use when the user asks to learn,
  practice, troubleshoot, maintain, or log work on a violin. Prefer
  `acoustic-guitar` or `electric-guitar` for guitar, `piano` or `drums` for
  those instruments, `music` for listening history, and `song` for original
  writing.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎻"}'
  related-skills: '{"acoustic-guitar":"Acoustic guitar practice and care instead of violin technique.","drums":"Drum-kit practice and rudiments instead of violin work.","electric-guitar":"Amplified guitar tone and gear instead of violin practice.","habits":"Design the recurring practice habit once the violin routine itself is clear.","music":"Track listening history, playlists, and concerts rather than violin technique.","piano":"Keyboard practice plans and technique instead of violin.","song":"Original songwriting, lyrics, and harmony when composition is the goal."}'
---

## State location

Practice state may exist in `<workspace>/violin/`, `<workspace>/memory/violin/`, or `~/violin/`. Before reading or writing practice data, resolve `<state_root>` as follows:

1. Use an explicitly configured state root when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/violin/`, `<workspace>/memory/violin/`, then `~/violin/`.
3. If no candidate exists and the user asks to save practice data, create `<workspace>/violin/` only after confirming the destination.
4. If several candidate directories exist, use only the highest-precedence one, tell the user that separate copies were detected, and leave the others unchanged.

Use the selected `<state_root>` for every practice-state operation in this invocation. Do not hardcode absolute host paths. Do not write runtime practice data into the skill package.

## Workflow

1. Establish the player's immediate goal: classical, fiddle, or orchestral focus; years playing; teacher status; current repertoire; and the next concrete outcome.
2. Give one focused exercise with a tempo, duration, or repetition target, then name the observable cue for clean execution.
3. When a technique, care, or logging detail is needed, load the matching reference below rather than loading every reference at once.
4. When the user wants persistent tracking, confirm the state root and update only the requested records.

| Resource | Load when |
| --- | --- |
| `references/technique-and-care.md` | Explaining left hand, bow arm, intonation, vibrato, tone, diagnosing symptoms, string or bow care, or a symptom-based technique fix. |
| `references/progress.md` | Creating or updating repertoire, session, technique, or goal records in `<state_root>`. |
| `references/sources.md` | Verifying technique terminology, instrument structure, or Agent Skills packaging facts. |

## Practice defaults

- Apply one correction at a time and verify it with a short, observable check before adding another change.
- Ask only the questions that change the advice: years playing, repertoire, classical vs fiddle vs orchestral goals, and teacher status.
- Start with a technique the player can practice in the current session.
- Prefer maker-specific care guidance over generic defaults when the two conflict.
- If pain is sharp, radiating, or persists after rest, pause technical drills and recommend a qualified teacher or clinician rather than forcing more pressure or repetition.
- After pain settles, return to lighter open-string and first-position drills before retrying shifts or extended techniques.
