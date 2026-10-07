# Inventory storage

Canonical inventory file: `<state_root>/inventory.md`.

## First use

After `<state_root>` is resolved and the user consents to create state:

```bash
mkdir -p <state_root>
```

Create `inventory.md` with empty sections if missing:

```markdown
# Skill Manager Inventory

## Installed

## Declined
```

## Format

```markdown
# Skill Manager Inventory

## Installed
- github@1.2.0 — "PR workflows" — 2026-01-15
- stripe@1.0.0 — "payment integration" — 2026-02-01

## Declined
- jira — "prefer an alternative tool"
```

Rules:

- Installed rows: `slug@version — "purpose" — YYYY-MM-DD`
- Declined rows: `slug — "user's stated reason"` (omit version)
- One row per slug per section; update in place on version changes
- Purpose stays in the user's words when possible

## What is tracked

- Skills installed through this lifecycle flow (purpose + date + version)
- Skills the user explicitly declined (stated reason only)

## What is not tracked

- Implicit "maybe later" silence
- Behavioral telemetry or task-repetition counts
- Secrets, tokens, or full skill package contents

## Why declined exists

So contextual suggestions skip skills the user already refused, unless they
reopen the topic. Only store explicit statements.
