# Doctor visit prep

Build this file only from entries in `<state_root>/log/` for the window the user names. Default window: the last 30 days. Save it as `<state_root>/for-doctor/appointment-YYYY-MM-DD.md`.

```markdown
# Appointment YYYY-MM-DD

## Window
<start> to <end>, from <state_root>/log/

## Counts
- <symptom>: <n> entries, severity <min>-<max>/10

## Repeated context the user reported
- <factor>: noted in <n> of <n> entries

## What the user said changed it
- Helped: <their words, or "not recorded">
- Worsened: <their words, or "not recorded">

## Medicines or measures already tried
- <name or measure>: <their reported effect>

## Questions to raise
- <one question grounded in the log, not a suspected diagnosis>
```

Example:

```markdown
# Appointment 2026-02-15

## Window
2026-01-16 to 2026-02-15, from <state_root>/log/

## Counts
- Headache: 4 entries, severity 4-7/10

## Repeated context the user reported
- Short sleep: noted in 3 of 4 entries
- Morning onset: noted in 4 of 4 entries

## What the user said changed it
- Helped: caffeine, dark room
- Worsened: bright lights

## Medicines or measures already tried
- Nothing recorded beyond rest and caffeine

## Questions to raise
- The log shows 4 morning headaches after short sleep. What should be tracked before the next visit?
```

Do not add a disease name that the user or a clinician has not already used.
