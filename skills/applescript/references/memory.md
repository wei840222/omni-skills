# Memory lifecycle — AppleScript

Operating rules for durable state under `<state_root>/`. Static skeleton: `assets/memory-template.md`.

## Files and roles

| Path | Role | Creation condition |
| --- | --- | --- |
| `<state_root>/memory.md` | Preferences, status, safety notes | First time data must persist across sessions, after confirmation |
| `<state_root>/snippets.md` | Verified reusable fragments | When a pattern is reused and user confirms save |
| `<state_root>/failures.md` | Error signatures and fixes | After a diagnosed failure the user wants remembered |
| `<state_root>/app-notes.md` | Per-app dictionary terms | After a successful probe the user wants retained |

## Status values (`memory.md`)

| Value | Meaning | Behavior |
| --- | --- | --- |
| `ongoing` | Context still evolving | Keep learning while operating |
| `complete` | Stable defaults exist | Use defaults; ask only on ambiguity |
| `paused` | Fewer setup questions | Minimal prompts; keep safety floor |
| `never_ask` | No preference questions | Follow explicit instructions only; keep safety floor |

## Rules

- Resolve `<state_root>` before any create or update.
- Explain path and summary; obtain confirmation before writes.
- Update `last` when preferences or app profiles change.
- Retain prior safety notes unless the user explicitly requests removal.
- Safety defaults in memory may increase confirmation strictness only. Destructive two-step confirmation and read-back after writes remain mandatory regardless of stored yes/no preferences.
- Never write credentials, tokens, or unrelated private file contents into state files.
