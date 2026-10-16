# Setup and activation

## Directory layout

After `<state_root>` is resolved (see `SKILL.md`), use this layout:

```text
<state_root>/
├── memory.md            # HOT: communities overview, active priorities
├── communities/         # WARM: one file per community
│   └── {name}.md        # Platform, channels, voice, metrics
├── content/             # Content calendar and templates
│   ├── calendar.md
│   └── templates.md
└── archive/             # COLD: past campaigns, old metrics, incident notes
```

Templates live in `assets/data-templates.md`. Create only the files the user
consents to persist.

## Activation checklist

1. Confirm the target community name, platforms, and whether durable memory is
   allowed for this session.
2. Resolve `<state_root>` once; report duplicates if more than one candidate
   exists.
3. If only `~/Clawic/data/community-manager/` exists, follow
   `references/migration.md` before copying anything.
4. Create `memory.md` and the first `communities/{name}.md` from the templates
   when the user wants standing ops notes.
5. Load `references/platforms.md` before the first cross-platform post.

## One-off mode

If the user declines storage, keep calendars, onboarding copy, and moderation
advice in chat only. Do not create `<state_root>/` until consent is explicit.
