# Memory template — optional project tracker

**Optional.** Only when the user wants to track skill drafts across sessions,
resolve `<state_root>` using `SKILL.md` State location, then create
`<state_root>/projects.md` after explicit consent for that path.

Do not create a literal directory named `<state_root>`. Do not write under the
skill package for runtime project notes.

## Template

```markdown
# Skill Projects

## Active

### [skill-name]
- status: drafting | reviewing | ready
- goal: [one sentence]
- files: SKILL.md, references/..., test-prompts.json
- notes: [decisions, open questions]
- last: YYYY-MM-DD

## Completed

### [skill-name]
- published-or-merged: YYYY-MM-DD
- version: X.Y.Z
- lessons: [what worked, what to improve]

---
*Updated: YYYY-MM-DD*
```

## Status values

| Value | Meaning |
|-------|---------|
| `drafting` | Writing initial content |
| `reviewing` | Structure, validator, and eval checks |
| `ready` | Ready to hand off to trial/publish flows |

## Usage

- Add a row when the user starts a skill
- Update status as work progresses
- Move to Completed after ship/merge
- Capture lessons for the next package
- Keep all paths under the resolved `<state_root>/`
