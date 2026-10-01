# Memory Template — Stock Images

Create `<state_root>/memory.md` only when the user wants saved preferences:

```markdown
# Stock Images Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD

## Context
<!-- What you've learned about their image needs -->
<!-- E.g., "SaaS marketing site; needs clean product hero photos" -->

## Preferences
<!-- Observed preferences -->
<!-- E.g., "Prefers minimal light backgrounds" -->
<!-- E.g., "Default size 1200x630 for OG images" -->
<!-- E.g., "Primary provider: Picsum for mocks, Unsplash API for production" -->

## Saved Images
<!-- Public URLs they reused and liked -->

---
*Updated: YYYY-MM-DD*
```

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning preferences | Note sizes, providers, styles they accept |
| `complete` | Stable style known | Apply saved defaults automatically |
| `declined` | Prefers fully stateless turns | Return URLs only; skip memory file |

## Default path

Most users only need immediate URLs. Create `<state_root>/memory.md` after they ask for saved preferences or consistent multi-session style guidance.
