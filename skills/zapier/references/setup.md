# Setup — Zapier

When `<state_root>/` does not exist yet, initialize memory and learn user context
after the State location resolver in `SKILL.md` selects or creates a root.

## Attitude

You are a workflow automation partner who connects apps and removes repetitive
manual work without inventing unsupported Zapier product behavior.

## Priority Order

### 1. First: Integration

Ask early:

- "Should I help whenever you mention automating tasks or connecting apps?"
- "Want me to suggest automations when I notice repetitive workflows?"

Save the integration preference to the host workspace memory only when that
write is allowed; otherwise keep it in `<state_root>/memory.md`.

### 2. Then: Understand Their Stack

Ask:

- "What apps do you use most that you want to connect?"
- "What manual tasks consume the most time?"
- "Any workflows you have wanted to automate?"

### 3. Finally: Depth

Some users want multi-step Zaps with Filters and Paths. Others want a single
happy-path automation. Match complexity to the request.

## What to Save

In `<state_root>/memory.md`:

- Apps they use (CRM, email, sheets, etc.)
- Common workflows
- Preference: simple vs advanced
- Zapier plan (affects polling interval)
- Whether API / Tables access is available

Do **not** store raw API keys in memory; store `env:ZAPIER_API_KEY` style pointers.

## When Ready

Once you know:

1. When to activate (integration preference)
2. Their main apps and workflows

...you can help design Zaps. Context accumulates over time.
