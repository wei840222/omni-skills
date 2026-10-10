# Electric Guitar Progress Tracking

Read this reference when the user wants to save or review practice data. Resolve `<state_root>` before any read or write.

## State tree

```text
<state_root>/
├── repertoire.md      # Songs learned, in progress, and planned
├── sessions/          # Optional monthly practice logs: YYYY-MM.md
├── technique.md       # Scales, techniques, and exercise status
└── goals.md           # Short- and long-term goals
```

Create a file or directory only when the user wants that category tracked. Do not pre-create empty trees.

## Repertoire entry

```markdown
## Currently Learning
- Comfortably Numb intro solo — Pink Floyd
  - Focus: whole-step bend intonation in the intro
  - Next: second-solo phrasing at practice tempo
```

## Technique entry

```markdown
## Technique Snapshot
| Technique | Status | Notes |
| --- | --- | --- |
| Alternate picking | developing | 16ths clean at 100 BPM |
| Bending | developing | half step reliable; whole step needs work |
| Vibrato | inconsistent | rate wanders under sustain |
| Sweep picking | not started | — |
```

## Session entry

```markdown
## 2026-10-10 (35 min)
- Comfortably Numb intro: bend-to-pitch drills with fretted reference.
- Exercise: alternate picking 16ths at 80 BPM, then 100 BPM only while clean.
- Result: half-step bends stable; whole-step still sharp/flat; next session holds 80 BPM longer.
```

## Logging triggers

Offer a log when the user reports a practice session, a newly stable technique, a recurring difficulty, or a milestone. Keep the log to the user's stated facts and confirm the destination before creating persistent data. Never write practice state into the skill package.
