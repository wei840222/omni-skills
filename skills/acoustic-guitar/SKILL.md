---
name: acoustic-guitar
description: Build acoustic guitar practice plans, troubleshoot fingerpicking and strumming technique, maintain an acoustic guitar, and track practice progress. Use when the user wants help learning, practicing, diagnosing, caring for, or logging work on an acoustic guitar.
metadata:
  version: "1.0.0"
  category: "music"
  openclaw: '{"emoji":"🎸"}'
---

## State location

Practice state may exist in `<workspace>/acoustic-guitar/`, `<workspace>/memory/acoustic-guitar/`, or `~/acoustic-guitar/`. Before reading or writing practice data, resolve `<state_root>` as follows:

1. Use an explicitly configured state root when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/acoustic-guitar/`, `<workspace>/memory/acoustic-guitar/`, then `~/acoustic-guitar/`.
3. If no candidate exists and the user asks to save practice data, create `<workspace>/acoustic-guitar/`.

Use the selected `<state_root>` for every practice-state operation in this invocation. If several candidate directories exist, use only the highest-precedence one and tell the user that separate copies were detected.

## Workflow

1. Establish the player's immediate goal: accompaniment or solo playing; fingerpicking, strumming, or both; genre; and the next concrete outcome.
2. Give one focused exercise with a tempo or repetition target, then name the observable cue for clean execution.
3. When a technique, care, or logging detail is needed, load the matching reference below.
4. When the user wants persistent tracking, confirm the state root and update only the requested records.

| Resource | Load when |
| --- | --- |
| `references/technique-and-care.md` | Explaining fingerstyle, strumming mechanics, barre chords, nail care, humidity, or a symptom-based technique fix. |
| `references/progress.md` | Creating or updating repertoire, session, technique, or goal records in `<state_root>`. |
| `references/sources.md` | Verifying maintenance guidance or Agent Skills packaging facts. |

## Practice guidance

### Before advising

Ask the smallest set of questions that changes the advice: playing style, genre, current ability, and the user's next goal. Begin with the technique they can practice today.

### Build clean fundamentals

- Let the wrist lead strumming and use the arm for broader dynamics.
- Use relaxed minimum fretting pressure; keep non-fretting fingers clear of neighboring strings.
- Establish thumb independence with a repeating bass pattern before adding melody notes.
- Shape dynamics deliberately: relaxed strokes for soft passages and a controlled accent for stronger beats.
- For a barre chord, place the thumb behind the neck near the middle finger and roll the index finger slightly toward its bony edge.

### Diagnose the symptom

| Symptom | First correction | Check the result |
| --- | --- | --- |
| Chords sound muted | Place each fretting finger close behind its fret and clear adjacent strings. | Pick each string individually, then play the full chord. |
| Strumming feels stiff or lifeless | Loosen the grip and move from the wrist. | Record four bars with quiet and accented beats. |
| Fingerpicking is uneven | Loop thumb plus one finger before adding another finger. | Keep the bass pulse even for one minute at a comfortable tempo. |
| Barre chords sound muddy | Adjust the index-finger angle and thumb position, then reduce pressure. | Test each string before returning to the progression. |

### Care and progress

Keep the instrument in a stable environment; a common target is 45–55% relative humidity. Use a hygrometer and follow the guitar maker's care guidance for the specific instrument and case. When a user finishes practice or reaches a milestone, offer a concise log using `references/progress.md`.
