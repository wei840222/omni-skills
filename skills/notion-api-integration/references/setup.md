# Setup — First Run and State Boxes

Load silently on first use or when `<state_root>/` is empty. Answer the user's Notion task first; then offer to initialize local state.

## Resolve state first

Follow the State location section in `SKILL.md`. Never write the literal string `<state_root>` to disk.

## Suggested layout

```text
<state_root>/
├── config.yaml          # declared preferences
├── memory.md            # observations, ## Boxes index, ## Due
├── schemas/             # per data-source schema boxes
├── artifacts/           # durable filter payloads / runbooks
├── runs/YYYY.md         # bulk run logs
├── mappings/            # external id ↔ Notion page id
└── integrations.md      # optional split when memory grows
```

Shared (not under this skill's state root by default):

- `<workspace>/projects/<project>.md`
- `<workspace>/contacts/contacts.md`

## Templates

When creating a file, copy structure from `assets/data-templates.md`. Announce each write in one line naming the path. Secrets stay pointer-only.

## First questions to avoid

Do not interrogate the user about their token or expertise. Work from defaults. Exception: if `api_version` is unset, **state** which `Notion-Version` you are assuming before acting.
