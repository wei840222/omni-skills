---
name: piano
description: Provide piano practice strategies, correct technique, guide repertoire selection, and track session progress. Load this when the user discusses learning piano, asks for practice advice, or mentions piano technique/repertoire.
metadata:
  version: "1.0.1"
  openclaw: "{\"emoji\": \"🎹\"}"
  related-skills:
    music: skills/music
---

## When to load references

- `references/progress.md`: Load before logging practice, updating repertoire, or structuring the piano workspace.
- `references/sources.md`: Load for pedagogy and injury-prevention source notes behind practice defaults.

## Core Behavior

- Create `<state_root>/piano/` as workspace on first interaction
- After practice sessions, offer to log progress
- Before suggesting pieces, check current repertoire
- Load `references/progress.md` to understand the workspace structure and session logging format before logging progress

## Before Advising

- Ask level AND context — "beginner" who played as child ≠ true beginner
- Ask instrument — synth vs weighted changes technique advice
- Ask time — 15 min/day ≠ 2 hours/day

## Practice Defaults

- Keep hands separate until each hand is reliable, then combine slowly
- Prioritize hard sections; use interleaved practice across sections for retention
- Prefer accuracy before speed so muscle memory stays clean
- Prefer short daily sessions (about 20 min/day) over rare marathon blocks

## Technique Defaults

- Use arm weight through the fingers; fingers transmit force rather than press from the knuckles alone
- Smooth thumb crossings for even scales
- Curve fingers on black keys to reach without twisting the hand
- Wrist or forearm pain means pause immediately and re-check posture/tension before continuing

## Mistakes by Level

**Beginners:** Eyes on hands, same volume, ignoring rests

**Intermediate:** Pedal as blur, rushing hard passages, memorizing without harmony

**Advanced:** Over-practicing through pain, perfection over expression

## Repertoire

| Level | Pieces | Timeline |
|-------|--------|----------|
| Beginner | Method books, folk songs | 0-12 months |
| Early Intermediate | Sonatinas, Bach Minuets | 1-2 years |
| Intermediate | Easy Mozart, Bach Inventions | 2-4 years |
| Advanced | Chopin Ballades, late Beethoven | 6+ years |

## Troubleshooting

- "Struggling to improve" → slow 50%, hands separate, small sections
- "Hands won't coordinate" → each hand automatic first
- "Same mistake" → isolate transition, 20x correctly
- "Sounds choppy" → legato exercises, hold until next note

## Pedaling

- Default without pedal — add when the score indicates
- Syncopated: down AFTER note, up on harmony change

## Digital Pianos

- Prefer weighted hammer action for transferable technique
- "Semi-weighted" is not full weighted; 88 keys support full repertoire range

## Progress Tracking

Log to `<state_root>/piano/`: pieces in progress, completed repertoire, recurring issues

## What to Surface

- "Working on [piece] 3 weeks — want help?"
- "Logs show recurring issue — want exercises?"
- "No practice logged this week — schedule?"
