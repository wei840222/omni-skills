# Setup — coaching a first skill

Use this script when the user is starting a skill from scratch.

## Role

Help the user capture a reusable agent procedure. Prefer real task traces over
generic “best practices” essays.

## Priority order

### 1. Understand the goal

Ask:

- What outcome should the agent produce?
- Which tasks should trigger this skill?
- What should stay out of scope (sibling skills)?

Listen for domain nouns, fragile steps, and audience (human-guided vs
agent-to-agent).

### 2. Identify the structure

Decide:

- Does it need durable state under `<state_root>/`?
- Does it call external APIs or local binaries?
- How much detail belongs in `references/` vs always-on `SKILL.md`?
- Are there scripts that must stay deterministic?

### 3. Guide the build

Walk through:

1. Directory name = `name` (lowercase hyphens)
2. Trigger-rich description (capability + when to use + boundaries)
3. Core workflow with defaults and recovery branches
4. Gotchas the model will otherwise miss
5. Routing table to supporting files
6. Optional `<state_root>` project tracker only with consent

## Principles to convey

**Add what the agent lacks.** Project conventions, exact commands, and
non-obvious failure modes beat textbook definitions.

**Progressive disclosure.** Details load when the branch needs them.

**Description is the trigger surface.** Agents often see only name +
description until the skill activates.

**Defaults over menus.** Choose one primary tool path; mention alternatives
briefly.

Official best practices: https://agentskills.io/skill-creation/best-practices

## Done when

- Goal and non-goals are explicit
- Draft tree is agreed (`SKILL.md`, optional `references/`, `scripts/`, `assets/`)
- User knows the next validation command:
  `uvx --from skills-ref agentskills validate skills/<slug>`
- Any file creation under `<state_root>/` has named consent
