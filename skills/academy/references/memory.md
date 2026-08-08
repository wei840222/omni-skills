# Memory lifecycle — Academy

## Initial setup

After the state-location procedure in `SKILL.md` selects `<state_root>`, create that actual directory and write `<state_root>/memory.md` on first use. Create only the selected path; leave other candidates untouched, and treat `<state_root>` as a placeholder rather than a folder name.

Create companion files only when the corresponding feature is in use. Copyable templates live in `assets/academy-data-templates.md`.

## Status values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Still learning the academy | Keep gathering context during normal work |
| `complete` | Strong enough operating picture | Work normally and update only on changes |
| `paused` | User does not want more setup now | Use current context without pushing |
| `never_ask` | User wants no setup-style follow-up | Skip setup prompts unless required for the task |

## Integration values

| Value | Meaning |
|-------|---------|
| `pending` | Persistent activation preference not offered yet |
| `done` | User accepted a minimal activation preference |
| `declined` | User declined persistent activation behavior |

## Companion files

Create these only when useful:

- `<state_root>/admissions.md` — pipeline rules and objection patterns
- `<state_root>/cohorts.md` — calendars, groups, and capacity plans
- `<state_root>/students.md` — attendance risks and intervention notes
- `<state_root>/staff.md` — staffing load, substitutes, and hiring gaps
- `<state_root>/finance.md` — pricing, collection rules, and refund boundaries
- `<state_root>/dashboard.md` — weekly KPI summaries
- `<state_root>/archive/` — closed terms and historical reviews

## Principles

- Keep notes operational and short.
- Store patterns and constraints, not full student dossiers.
- Update `last` on every meaningful use.
- Prefer bullets that change a later decision.
- Keep secrets, card data, health data, and sensitive student information out of these files.
