---
name: slides
description: >
  Create, edit, and automate presentation decks with programmatic tools
  (python-pptx, Google Slides API, reveal.js, Marp, Slidev), enforce visual
  consistency, and learn user style preferences. Use when the user needs slides
  created or revised, a pitch/lesson/report deck, PowerPoint or web presentation
  output, brand-aligned slide design, or validation of deck layout and density.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📊"}'
  related-skills: '{"design":"Quantified visual hierarchy, type, color, and layout judgment beyond slide-specific defaults.","figma":"Design-file and prototype handoff when the deck originates in Figma.","powerpoint":"Live PowerPoint app control on macOS when automation of an open PPT session is required.","typography":"Measure, leading, and type-scale depth when legibility is the primary problem.","writing":"Narrative structure and concise copy when slide wording needs editing beyond layout.","storytelling":"Story arc and audience framing for pitch and keynote narratives."}'
---

## State location

Slides state may exist in `<workspace>/slides/`, `<workspace>/memory/slides/`, or `~/slides/`.
`<workspace>` means the workspace root provided by the host/runtime, not the shell cwd.

Before any state read or write, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/slides/`, `<workspace>/memory/slides/`, `~/slides/`.
3. If multiple candidates exist, keep only the highest-precedence directory, leave others untouched, and tell the user which location was selected.
4. If none exists and persistent state must be created, default to `<workspace>/slides/` after brief first-write consent.

Use the selected `<state_root>` for every state path in this skill. Never write the literal string `<state_root>` to disk. Skill package files stay under `references/` and `assets/`; never write learned data into `SKILL.md`.

On first use, create:

```bash
mkdir -p <state_root>/{styles,projects,templates}
```

Load `assets/memory-template.md` for `memory.md`, style, project, and template file shapes.

## When to Use

User needs presentation slides created, edited, or automated. Agent selects the tool (python-pptx, Google Slides API, reveal.js, Marp, Slidev), applies stored style preferences, generates visually consistent decks, and validates output before delivery.

## Progressive disclosure

Load only the reference needed for the current step; keep `SKILL.md` as the routing surface.


| Need | Load |
|------|------|
| Memory / style / project layout | `assets/memory-template.md` |
| Tool APIs and code patterns | `references/tools.md` |
| Typography, color, layout, anti-patterns | `references/design.md` |
| Deck structures by type (pitch, corporate, technical) | `references/formats.md` |

## Scope

This skill handles:

- Creating and editing presentations through the declared tools
- Storing style preferences under `<state_root>/`
- Reading user templates and brand guidelines from `<state_root>/`
- Generating previews or representative slides for validation

Out of scope (route elsewhere or stop):

- Email, calendar, or contacts access
- Network calls without an explicit user-requested delivery step
- Reading files outside `<state_root>/` and the user-provided project paths
- Auto-sending decks to external services
- Live PowerPoint app session control on macOS (`powerpoint` skill)
- Pure visual taste without slide generation (`design` / `figma`)

## Core workflow

### 1. Identify context first

Before generating slides, capture:

- **Purpose**: pitch, lesson, report, demo, quarterly update
- **Audience**: investors, students, executives, clients
- **Output tool**: PowerPoint (`.pptx`), Google Slides, web (reveal.js / Slidev / Marp)
- Load matching style from `<state_root>/styles/` when present

### 2. Tool selection by output

| Need | Tool | When |
|------|------|------|
| `.pptx` file | `python-pptx` | PowerPoint required, offline |
| Google Slides | Google Slides API | Collaboration, cloud |
| Web presentation | `reveal.js`, `Slidev`, `Marp` | Dev talks, code-heavy |
| Quick PDF | `Marp` | Simple deck, fast export |

Details and code patterns: `references/tools.md`.

### 3. Visual consistency

- Load the user's style before generating
- If no style exists: ask for brand colors and fonts, or use neutral defaults
- Keep one typography hierarchy across the whole deck
- Cap the palette at 3–4 colors
- Full rules: `references/design.md`

### 4. Content density limits

- Maximum 6 bullet points per slide
- Maximum 6 words per bullet (6×6 rule)
- One idea per slide
- If content overflows, split into multiple slides

### 5. Validate before delivery

- Generate a preview or screenshot of key slides when tooling allows
- Check readable body text (24pt+), contrast, and alignment
- For important decks, show 2–3 slides for confirmation before finishing the full set

### 6. Learn user preferences

| Event | Action |
|-------|--------|
| User provides a style guide | Save to `<state_root>/styles/{name}.md` |
| User corrects a design choice | Update the style file |
| User approves a template | Save to `<state_root>/templates/` |
| New project starts | Create `<state_root>/projects/{name}/` |

### 7. Version management

- Log each significant revision in `projects/{name}/versions.md`
- Track date, changes, and audience variant
- Support quick comparison questions such as "What changed since v2?"

## Common traps

- **python-pptx units** — Use `Inches()`, `Pt()`, `Emu()` from `pptx.util`; raw numbers break layout
- **Marp frontmatter** — YAML must include `marp: true`
- **reveal.js separators** — `---` horizontal, `--` vertical
- **Slidev syntax** — Differs from reveal.js; check current docs per framework
- **Google Slides API quotas** — Batch updates to stay under rate limits
- **Image sizing** — Always set dimensions; auto-fit often fails
- **Font availability** — Prefer system fonts unless embedding is confirmed

## Safety and package integrity

- Keep learned styles under `<state_root>/styles/`; keep project context under `<state_root>/projects/`
- Leave `SKILL.md` unchanged at runtime
- Prefer positive acceptance checks over vague "never" lists when guiding generation
