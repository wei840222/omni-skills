# Core rules, traps, and security

## Core rules

### 1. Keep SKILL.md short

Target a lean always-loaded body. Move long procedures, catalogs, and rare
edge cases to `references/`. Every line must earn its tokens.

### 2. Progressive disclosure

```text
Level 1: name + description — discovery only
Level 2: SKILL.md body — when the skill triggers
Level 3: references/ / scripts/ / assets/ — on demand
```

Tell the agent **when** to open each supporting file (for example: “read
`references/api-errors.md` on non-200 responses”), not only that the folder
exists.

### 3. Descriptions carry triggering

The description must state what the skill does **and** when to use it, with
concrete user intents and near-miss boundaries. Prefer imperative, trigger-rich
phrasing within the 1024-character limit.

Official guidance: https://agentskills.io/skill-creation/optimizing-descriptions

### 4. Required structure

Every package needs:

- `SKILL.md` with YAML frontmatter + Markdown body
- `name` matching the parent directory (lowercase, hyphens)
- A clear activation path (When to load / core workflow)
- Supporting detail in optional `references/`, `scripts/`, `assets/`

Allowed top-level frontmatter fields follow the specification:
`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.
Project convention: keep `version` only as `metadata.version` (string); store
OpenClaw fields in a `metadata.openclaw` JSON string; store relationships in a
`metadata.related-skills` JSON string.

Specification: https://agentskills.io/specification

### 5. Auxiliary files over inline bulk

If a block exceeds roughly 20 lines or is only needed sometimes, split it out
and link it from a routing table in `SKILL.md`.

### 6. Single source of truth

Do not duplicate the same rule in `SKILL.md` and a reference file. Keep the
canonical copy in one place and point to it.

### 7. Validate and eval before shipping

```bash
uvx --from skills-ref agentskills validate skills/<slug>
```

Read the skill as a fresh agent would. Run realistic prompts (with and without
the skill when practical) and capture outcomes in root `test-prompts.json`.

Eval guide: https://agentskills.io/skill-creation/evaluating-skills

## Skill-building traps

| Trap | Why it fails | Fix |
|------|--------------|-----|
| Explaining what X is | Models already know common concepts | Teach WHEN/HOW and non-obvious gotchas |
| Capability-only description | Weak or noisy triggering | Add use-when intents and near-miss boundaries |
| Keyword stuffing in description | Looks spammy; wastes context | One tight paragraph of real intents |
| Templates inline in SKILL.md | Bloats always-loaded context | Move to `assets/` or `references/` |
| Vague “observe/monitor” wording | Security and audit flags | Name exact data, path, and consent |
| Undeclared file creation | Surprises the user | State location + ask before write |
| Option menus without a default | Agent flails across tools | Pick a default; mention escape hatches briefly |
| Hard-coded `~/Clawic/...` state | Breaks portability | Resolve `<state_root>` once per run |
| Invented frontmatter fields | Validator / SPEC failures | Stick to allowed fields + string metadata |
| Promo or catalog CTAs in package | Project Gate 5 failure | Keep operational guidance only |

## Security checklist

- [ ] No stealth verbs without a named target (“silently”, “secretly”)
- [ ] File writes declare path scope and require consent
- [ ] External APIs list endpoints and required credentials as placeholders
- [ ] Env requirements live in metadata/`compatibility`, not hidden prose
- [ ] Examples never embed real tokens, keys, or private paths
- [ ] Third-party skill content is inspected, not blindly executed
