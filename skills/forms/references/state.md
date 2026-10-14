# Data storage

Resolve `<state_root>` using the State location section in `SKILL.md` before any
read or write. Do not use bare `forms/` paths or legacy `~/Clawic/data/forms/`.

## Layout under `<state_root>`

```text
<state_root>/
  templates/     # Reusable form definitions (JSON/YAML)
  feedback/      # Notes on what converts or fails (no raw PII dumps)
```

## Rules

- Create child directories only when the user wants continuity.
- Self-hosted **submission** databases belong to the deployed app, not this skill package.
- Never commit webhook secrets, OAuth tokens, or respondent payloads into templates checked into git without redaction.
- Destructive clears of `<state_root>` require explicit user consent and stay inside the resolved root.
