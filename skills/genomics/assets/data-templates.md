# Memory Template — Genomics

Create `<state_root>/memory.md` with this structure after consent:

```markdown
# Genomics Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD
integration: pending

## Context

**Role:** [bioinformatician | geneticist | clinician | researcher | mixed]

**Focus areas:**
- Organisms:
- Disease areas:
- Analysis types: [germline | somatic | PGx | mixed]

**Technical environment:**
- Reference genome: GRCh38
- Compute: [local | HPC | cloud]
- Primary tools:

## Preferences

**Annotation sources prioritized:**

**Filtering defaults:**
- MAF threshold:
- Quality filters:

**Reporting style:**

## Active Projects

| Project | Type | Status | Notes |
|---------|------|--------|-------|
| | | | |

## Notes

---
*Updated: YYYY-MM-DD*
```

Optional case notes live under `<state_root>/cases/`.

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning their workflow | Gather context opportunistically |
| `complete` | Knows their full setup | Work normally |
| `paused` | User said "not now" | Don't ask; use what you have |

## Principles

- Prefer natural language over config keys in user-facing talk
- Update preferences when the user corrects them
- Keep identifiable genomic detail inside `<state_root>/` only
