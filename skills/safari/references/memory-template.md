# Memory Template - Safari Browser Control

Create `<state_root>/memory.md` with this structure:

```markdown
# Safari Browser Control Memory

## Status
status: ongoing
version: 1.1.0
last: YYYY-MM-DD
integration: pending | complete | paused | never_ask

## Context
- Activation preference:
- Preferred control mode:
- Daily session control allowed:
- Main Safari targets:
- Risk boundaries:
- Preferred output shape:

## Notes
- Durable permission and control lessons
- Snippets and recipes worth reusing
- Recovery sequences that worked

---
*Updated: YYYY-MM-DD*
```

## Status Values

| Value | Meaning | Behavior |
|-------|---------|----------|
| `ongoing` | Context still evolving | Keep learning modes, permission state, and failure patterns |
| `complete` | Defaults are stable | Focus on execution and maintenance |
| `paused` | User wants minimal setup | Help without pushing deeper tracking |
| `never_ask` | User wants no setup prompts | Avoid asking integration questions unless requested |

## File Templates

Create `<state_root>/permissions.md`:

```markdown
# Permissions

## Control Path
- Apple Events:
- Screen Recording:
- JavaScript path:
- safaridriver enable:
- Notes:
```

Create `<state_root>/sessions.md`:

```markdown
# Sessions

## Active Notes
- Mode: AppleScript | WebDriver
- Target tabs / URL patterns:
- Isolation expectations:
- Notes:
```

Create `<state_root>/snippets.md`:

```markdown
# Snippets

## Known-good
- Title:
- Command:
- Verification:
```

Create `<state_root>/recipes.md`:

```markdown
# Recipes

## Task
- Goal:
- Mode:
- Steps:
- Verification:
```

Create `<state_root>/incidents.md`:

```markdown
# Incidents

## Entry
- Date:
- Symptom:
- Root cause:
- Fix:
- Prevent:
```

## Safety

- Never store passwords, cookies, full history dumps, or Keychain material.
- Prefer short operational notes over page-content archives.
- Keep `<state_root>` outside the skill package and version control.
