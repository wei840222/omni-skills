# Memory template — AppleScript

Static skeleton only. Lifecycle and mandatory safety floor: `references/memory.md`.
Create `<state_root>/memory.md` from this template after the user confirms the path.

```markdown
# AppleScript Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending

## Context
- Main app domains automated by the user
- Preferred output format and response style
- Read-only vs write-allowed app list

## App Profiles
- App name
- Verified dictionary terms
- Known command patterns that work
- Known failures and fixes

## Safety Defaults
- Extra confirm before reversible writes: yes/no (default no)
- Extra confirm before bulk edits: always (mandatory floor)
- Destructive two-step confirm: always (mandatory floor; not optional)
- Require read-back after writes: always (mandatory floor)

## Notes
- Reusable snippet pointers (details in snippets.md)
- Common edge cases from repeated tasks

---
*Updated: YYYY-MM-DD*
```
