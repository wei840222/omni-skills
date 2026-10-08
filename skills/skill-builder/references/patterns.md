# Patterns — package shapes and descriptions

## Pattern 1: Memory-based skills

Skills that learn preferences or accumulate durable records.

```text
skill/
├── SKILL.md                 # Workflow + State location
├── references/
│   ├── setup.md
│   └── memory-template.md   # or domain schemas
└── test-prompts.json
```

Key elements:

- Resolve `<state_root>` once; every later path uses `<state_root>/...`
- Consent before first create
- Rules for when memory updates vs stays read-only

## Pattern 2: Tool integration skills

Skills wrapping CLIs or HTTP APIs.

```text
skill/
├── SKILL.md
├── references/
│   ├── commands.md
│   └── errors.md
├── scripts/                 # optional helpers
└── test-prompts.json
```

Key elements:

- Default tool path with a short escape hatch
- External endpoints / required bins declared clearly
- Error recovery for non-zero exits and auth failures

## Pattern 3: Domain expert skills

Skills that teach specialized judgment more than file I/O.

```text
skill/
├── SKILL.md                 # core rules + routing
├── references/
│   ├── topic-a.md
│   └── topic-b.md
└── test-prompts.json
```

Key elements:

- Load references only for the active subtopic
- Gotchas beat encyclopedia chapters
- Clear not-for boundaries vs sibling skills

## Pattern 4: Multi-phase workflow skills

Skills that gate irreversible steps.

```text
skill/
├── SKILL.md                 # phase overview + checkpoints
├── references/
│   ├── phase-1.md
│   └── phase-2.md
├── assets/                  # output templates
└── test-prompts.json
```

Key elements:

- Explicit checkpoints before destructive actions
- Progress notes only under `<state_root>/` when needed
- Templates in `assets/` loaded on demand

## Description patterns

### Strong shapes

| Domain | Description sketch |
|--------|--------------------|
| PDF | Extract, merge, and fill PDFs; use when handling forms, page ops, or document extraction. |
| Git | Manage branches, conflicts, and automation; use when repo history or PR hygiene is the task. |
| Docker | Build, run, and debug containers/compose; use when image, network, or volume failures block work. |

### Weak shapes

| Weak text | Why |
|-----------|-----|
| “Helper for PDFs” | No capability depth or triggers |
| “Use when you need Docker” | Starts with filler; no job story |
| “Git stuff and more” | Vague; no boundaries |

### Practical formula

```text
[Do X, Y, and Z]. Use when [intent A], [intent B], or [intent C]. Prefer
[sibling] for [near miss]. Not for [out of scope].
```

Keep the whole description ≤ 1024 characters. Frontmatter may use `>` folded
scalars for readability.

Official guide: https://agentskills.io/skill-creation/optimizing-descriptions

## Frontmatter checklist (project)

```yaml
---
name: clear-name
description: >
  Capability sentence(s). Use when triggers… Prefer sibling for near-miss.
  Not for out-of-scope.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📎"}'
  related-skills: '{"other-skill":"Why hand off or bound scope."}'
---
```

Omit unused optional fields. Do not keep top-level `slug`, `homepage`, or
`changelog`. Do not keep `_meta.json`.

## Quality checklist

- [ ] `SKILL.md` stays scannable; deep material is routed
- [ ] Description includes triggers and boundaries
- [ ] State paths use `<state_root>/...` after the resolver
- [ ] `related-skills` targets exist in-repo when listed
- [ ] `uvx --from skills-ref agentskills validate skills/<slug>` exits 0
- [ ] `test-prompts.json` has realistic prompts with expected outcomes
