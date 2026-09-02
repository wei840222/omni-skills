# Memory Template — ASI

Use these templates only after resolving `<state_root>` and obtaining explicit consent for the corresponding write.

Create `<state_root>/memory.md`:

```markdown
# ASI Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | done | declined

## User Model
reasoning_style: analytical | intuitive | pragmatic
depth_preference: compressed | balanced | exhaustive
anticipation_tolerance: do_it | ask_first | explain_first

## Active Domains
- domain 1

## Calibration Notes

## Open Loops

---
*Updated: YYYY-MM-DD*
```

Create `<state_root>/synthesis-log.md`:

```markdown
# Synthesis Log

## Connections

### [Date] Source → Target
- Problem: ...
- Source domain: ...
- Pattern extracted: ...
- Application: ...
- Outcome: ...

---
*Updated: YYYY-MM-DD*
```

Create `<state_root>/improvements.md`:

```markdown
# Self-Improvement Log

## Patterns Identified

### [Date] Pattern Name
- Situation: ...
- What I missed: ...
- What I should do next time: ...
- Applied: yes | pending

## Knowledge Gaps

### [Date] Gap Description
- How exposed: ...
- Priority: high | medium | low
- Addressed: yes | pending

---
*Updated: YYYY-MM-DD*
```

## Status values

| Value | Meaning | Behavior |
| --- | --- | --- |
| `ongoing` | Still calibrating | Observe and adapt. |
| `complete` | Fully calibrated | Apply the confirmed preferences. |
| `paused` | User prefers minimal persistence | Apply patterns without new state writes. |
