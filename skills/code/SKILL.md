---
name: code
description: >
  Guides coding work through plan → execute → verify → deliver with explicit
  user approval between steps, preference memory, and screenshot/API evidence
  before handoff. Use when the user asks to implement a feature, break work into
  testable steps, track a multi-request queue, or verify UI/API changes before
  delivery. Prefer `coding` for durable style/stack preference capture,
  `agentic-coding` for PACT contract loops, `developer` for ticket-to-merge /
  CI/CD / on-call loops, `review-code` for PR risk review, and language skills
  (`go`, `javascript`, …) once implementation is language-specific. Not for
  autonomous unattended coding or inventing production architecture alone.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💻","os":["linux","darwin","win32"],"displayName":"Code"}'
  related-skills: '{"coding":"Capture and apply durable coding style, stack, and architecture preferences across sessions.","agentic-coding":"Contract-driven PACT loops when merge-ready agentic delivery is the primary ask.","developer":"Full ticket-to-merge, CI parity, migration, and on-call loop beyond stepwise coding guidance.","review-code":"Risk-first PR review and merge-readiness once a diff already exists.","software-engineer":"Architecture and production trade-off coaching beyond stepwise implementation guidance.","setup":"OpenClaw install, channel, and gateway configuration outside this coding workflow."}'
---

## State location

Optional coding preference state may exist in `<workspace>/code/`,
`<workspace>/memory/code/`, or `~/code-skill/`. Before reading or writing state,
resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/code/`, `<workspace>/memory/code/`, `~/code-skill/`.
3. If several candidate directories exist, use only the highest-precedence one and
   report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create
   `<workspace>/code/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. Store
preferences only in `<state_root>/memory.md` (see `assets/data-templates.md` and
`references/setup.md`). Create or update that file only when the user explicitly
asks to remember a preference.

Legacy `~/Clawic/data/code/` and `~/clawic/code/` are migration sources only—
keep them out of the active lookup order, and move them into the resolved
`<state_root>` only when the user asks; say in one line that you moved the data
and from where.

Scripts and shell examples must receive the resolved filesystem path; never
write the literal string `<state_root>` to disk.

## When to use

- User asks to implement, build, or fix code and wants a stepwise plan first
- Multi-file work that needs testable chunks and approval between steps
- UI or API changes that need screenshot or payload evidence before delivery
- Multiple concurrent coding requests that need a visible queue
- Preference memory for coding workflow habits the user explicitly asks to store

Prefer other skills when:

- Durable style/stack preference systems → `coding`
- PACT / acceptance-contract agentic delivery → `agentic-coding`
- Ticket sizing, CI/CD parity, migrations, on-call mitigation → `developer`
- Reviewing an existing PR/diff for risk → `review-code`
- Language-specific panics, modules, or idioms → the matching language skill

## Quick reference

| Topic | File |
|-------|------|
| Memory setup | `references/setup.md` + `assets/data-templates.md` |
| Task breakdown | `references/planning.md` |
| Execution flow | `references/execution.md` |
| Verification | `references/verification.md` |
| Multi-task state | `references/state.md` |
| Preference criteria | `references/criteria.md` |
| Research sources | `references/sources.md` |

## Scope

This skill provides:

- Coding workflow guidance (plan → execute → verify → deliver)
- Preference storage the user explicitly requests under `<state_root>/memory.md`
- Progressive disclosure into the reference files above

Operational boundaries:

- Wait for explicit user instruction before executing a step
- Do not open network connections from this skill itself
- Limit durable preference files to the resolved `<state_root>` plus the user's project checkout
- Keep `SKILL.md` and packaged references immutable
- Require user awareness before autonomous or sub-agent actions

## Core rules

### 1. Check memory first

If `<state_root>/memory.md` exists after State location resolution, read it for
stated preferences before planning.

### 2. User controls execution

- Provide guidance and wait for manual approval between steps
- The user decides when to proceed
- Sub-agent delegation requires an explicit user request

### 3. Plan before code

- Break requests into independently testable steps
- Each step names an output and a verification check
- See `references/planning.md`

### 4. Verify everything

| After | Do |
|-------|-----|
| Each function / unit | Suggest the narrowest relevant tests |
| UI changes | Capture and review screenshots before sending |
| API changes | Show the actual response payload |
| Before delivery | Suggest the full suite the change warrants |

### 5. Store preferences only on request

| User says | Action |
|-----------|--------|
| "Remember I prefer X" | Add to `<state_root>/memory.md` Preferences |
| "Exclude Y from future tasks" | Add to `<state_root>/memory.md` Excluded |

Only store what the user explicitly asks to save. See `references/criteria.md`.

## Workflow

```
Request → Plan → Execute → Verify → Deliver
```

Show progress after each approved step. Pause on errors, credential needs, or
A/B decisions. Details: `references/execution.md`, `references/state.md`.

## Planning upgrades

Prefer these positive defaults over vague delivery:

- Verify with tests or screenshots before claiming done
- Split large changes into independently reviewable chunks
- Re-read `<state_root>/memory.md` before choosing style or tooling
- Ask for the failing log before guessing a build fix
- Route language-deep or PR-review asks to the related skill above

## External endpoints

This skill makes no network requests of its own.

| Endpoint | Data sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

## Security and privacy

**Stays local**

- Preferences the user explicitly asks to save in `<state_root>/memory.md`

**Leaves the machine**

- None from this skill

Do not commit secrets into preference memory. Prefer placeholders in examples.
