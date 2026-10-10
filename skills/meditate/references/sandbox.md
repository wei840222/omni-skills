# Sandbox rules — Meditate

## Absolute output constraints

Treat each item below as a hard output gate. Prefer omission over a borderline insight.

### Disallowed generations

- Shell commands (`rm`, `mv`, `curl`, package installs, and similar)
- Code blocks presented as ready-to-run scripts
- API calls, webhooks, or network requests
- File modifications outside `<state_root>/`
- Outbound messages, emails, or notifications to send
- Scheduled tasks, crons, or automation installs
- Credential handling or secret material

### Restricted access during meditation

- Network resources and external APIs (unless the user explicitly authorized external research for this turn)
- Files outside `<state_root>/`
- System configurations
- Credentials or secrets
- Other users’ private data

### Suggestion framing

| Prefer | Avoid |
|--------|-------|
| “Have you considered refactoring X?” | “I’ll refactor this code” |
| “Might be worth sending that email” | “Let me send that email” |
| “The config might benefit from Y” | “I should update the config” |

## Output validation checklist

Before presenting any insight, verify:

```text
[ ] Contains no executable code
[ ] Contains no shell commands
[ ] Contains no file paths outside <state_root>/
[ ] Framed purely as a question or observation
[ ] Maintains a reflective stance without promising action
[ ] Relies on in-session shared context and/or <state_root>/ data
```

If any box fails, rewrite or omit.

## If uncertain

1. Default to omitting the insight.
2. If the topic seems to require action, skip it for meditation and, only if the user asked for execution, suggest the appropriate task skill.
3. Generate pure observations and questions only.

## Monitoring

Track in `<state_root>/feedback.md` when an insight led to:

- User choosing to act themselves → allowed; they initiated
- Agent attempting action from meditation output → sandbox violation; review and correct
- Confusion about agent capabilities → restate reflection-only boundary in one line
