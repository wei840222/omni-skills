# Violin Progress Tracking

Read this reference when the user wants to save or review practice data. Resolve `<state_root>` before any read or write.

## State tree

```text
<state_root>/
├── repertoire.md      # Pieces learned, in progress, and planned
├── sessions/          # Optional monthly practice logs: YYYY-MM.md
├── technique.md       # Scales, shifts, études, and left/bow status
└── goals.md           # Short- and long-term goals
```

Create a file or directory only when the user wants that category tracked. Do not pre-create empty trees.

## Repertoire entry

```markdown
## Currently Learning
- Bach Partita No. 2 Allemande
  - Focus: string crossings in measures 8–12
  - Next: memorize the first half
```

## Technique entry

```markdown
## Scales & Arpeggios (3 octaves)
| Key | Scale | Arpeggio | Notes |
| --- | --- | --- | --- |
| G major | clean | clean | foundation |
| A major | working | clean | high 3rd-position shift |

## Shifting
- 1st to 3rd: comfortable
- 3rd to 5th: needs work on A string
```

## Session entry

```markdown
## 2026-10-03 (45 min)
- Scales: G, D, A major with drone.
- Bach: measures 8–12 slow, string crossings.
- Result: A-string shifts still tense; next session isolates release-before-shift.
```

## Goals entry

```markdown
## This Month
- A major scale clean at quarter = 80
- Memorize Bach Allemande first page
- Daily drone practice
```

## Logging triggers

Offer a log when the user reports a practice session, a newly stable scale or position, a recurring difficulty, or a milestone. Keep the log to the user's stated facts and confirm the destination before creating persistent data.
