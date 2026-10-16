# Setup — Italy Skill

## Requirements

No external binaries. This skill uses file-based knowledge plus optional local trip memory under a resolved `<state_root>`.

## Memory configuration

1. Resolve `<state_root>` using the State location rules in `SKILL.md`.
2. Only after the user wants continuity, create the directory with the **resolved path** (never the literal string `<state_root>`):

```bash
mkdir -p /resolved/path/to/italy
```

3. Copy the template into `memory.md` at that path:

```bash
cp assets/data-templates.md /resolved/path/to/italy/memory.md
```

Legacy `~/Clawic/data/italy/` is migration-only. Do not create new state there. Move it only when the user asks.

## Package layout

```text
italy/
├── SKILL.md
├── test-prompts.json
├── assets/
│   └── data-templates.md
└── references/
    ├── setup.md
    ├── sources.md
    ├── itineraries.md
    ├── accommodation.md
    ├── rome.md
    ├── florence.md
    ├── venice.md
    ├── naples.md
    ├── regions.md
    ├── food-guide.md
    ├── wine.md
    ├── experiences.md
    ├── beaches.md
    ├── hiking.md
    ├── nightlife.md
    ├── culture.md
    ├── with-kids.md
    ├── transport.md
    ├── telecoms.md
    ├── apps.md
    └── emergencies.md
```

## When to load which file

| User intent | Start with |
| --- | --- |
| General Italy trip | `SKILL.md` → `references/itineraries.md` + `references/sources.md` |
| Rome food / traps | `references/rome.md` + `references/food-guide.md` |
| Florence + driving | `references/florence.md` + `references/transport.md` (ZTL) |
| Venice day plan | `references/venice.md` + `references/transport.md` |
| Naples / Amalfi | `references/naples.md` + `references/beaches.md` |
| Entry / emergency claims | `references/sources.md` first, then `references/emergencies.md` |

## Safety notes

- Treat restaurant prices, train fares, and ZTL hours as perishable; re-check official pages before booking.
- Do not invent nationality-specific visa outcomes.
- Keep trip preferences local under `<state_root>`; do not write runtime state into this package.
