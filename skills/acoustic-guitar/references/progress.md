# Acoustic Guitar Progress Tracking

Read this reference when the user wants to save or review practice data. Resolve `<state_root>` before any read or write.

## State tree

```text
<state_root>/
├── repertoire.md      # Songs learned, in progress, and planned
├── sessions/          # Optional monthly practice logs: YYYY-MM.md
├── technique.md       # Patterns, strumming, and fingerpicking status
└── goals.md           # Short- and long-term goals
```

Create a file or directory only when the user wants that category tracked.

## Repertoire entry

```markdown
## Currently Learning
- Blackbird — Beatles
  - Focus: thumb independence in the verse
  - Next: add vocals while playing
```

## Technique entry

```markdown
## Fingerpicking Patterns
| Pattern | Status | Notes |
| --- | --- | --- |
| Basic arpeggio | comfortable | p-i-m-a is even |
| Travis picking | developing | bass is steady; melody needs work |
```

## Session entry

```markdown
## 2026-09-01 (40 min)
- Blackbird: practiced the verse and alternating bass.
- Exercise: thumb-only bass for 10 minutes.
- Result: smoother pulse; next session adds one melody finger.
```

## Logging triggers

Offer a log when the user reports a practice session, a newly stable technique, a recurring difficulty, or a milestone. Keep the log to the user's stated facts and ask before creating persistent data.
