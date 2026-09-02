# Memory Template - Video Downloader

Create `<state_root>/memory.md` with this structure:

```markdown
# Video Downloader Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | complete | paused | never_ask

## Context
- User goals for download quality, format, and local file organization.
- Any explicit boundaries about what should not be downloaded.

## Notes
- Observed preferences from repeated requests.
- Common failure causes and successful fallback patterns for this user.

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Learning preferences | Adapt gradually from usage |
| `complete` | Stable defaults known | Use remembered defaults first |
| `paused` | User paused memory updates | Read memory, preserve existing notes without modifications |
| `never_ask` | User explicitly declines setup prompts | Bypass setup prompts in all future interactions |

## Key Principles

- Keep entries short and directly actionable.
- Ensure all account credentials and private tokens are excluded from storage.
- Record only behavior that clearly repeats.
- Update `last` whenever memory is changed.
