# Memory template — bar-exam

Use only after a session produces something durable. All paths are under the selected `<state_root>`.

## Files

### `<state_root>/bar-exam/profile.md`

Jurisdiction, test date, law school / admission path, baseline MBE estimate, prep course, and user type. Create on first durable intake; update in place.

```markdown
# Profile

- jurisdiction:
- exam_date:
- weeks_remaining:
- format: UBE | state-specific
- target_score:
- baseline_mbe_pct:
- prep_course:
- user_type: first-timer | retaker | attorney-transfer | international
- notes:
```

### `<state_root>/bar-exam/subjects/`

One file per MBE subject (or a single `subjects.md` log). Track question counts, accuracy, and traps.

### `<state_root>/bar-exam/essays/`

MEE drafts with IRAC scores, missed issues, and timing. One file per essay or dated log.

### `<state_root>/bar-exam/practice/`

Full or sectional practice results and analysis.

### `<state_root>/bar-exam/outlines/`

Subject outlines and mnemonics the user wants retained.

### `<state_root>/bar-exam/feedback.md`

What study methods worked or failed for this user.

```markdown
## What works
- …

## What failed
- …

## Next experiment
- …
```

## Migration

If legacy paths under `~/Clawic/data/bar-exam/` or bare `~/bar-exam/` contain user data, copy forward into the selected `<state_root>/bar-exam/` only with explicit user confirmation. Do not silently merge duplicate roots.
