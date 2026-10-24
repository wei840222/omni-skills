---
name: agentic-coding
description: >
  Apply contract-driven agentic coding with the PACT loop (Problem, Acceptance,
  Change, Trace) so AI-assisted edits ship as merge-ready diffs with explicit
  quality gates. Use when the user needs production features, risky refactors,
  reproducible bug fixes, or Xcode/Swift delivery with acceptance checks before
  code; prefer `agentic-engineering` for multi-agent orchestration, `vibe-coding`
  for exploratory prototypes, `code` for stepwise plan→verify coaching, and
  `coding` for durable style/stack preference capture.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧭","requires":{"bins":["git"]}}'
  related-skills: '{"agentic-engineering": "Multi-agent blast-radius sizing, parallel terminals, and recovery once work spans several agent sessions.", "code": "Stepwise plan→execute→verify coaching with approval between steps.", "coding": "Durable coding style, stack, and architecture preferences across sessions.", "copilot": "Cross-session priority and continuity outside a single PACT contract.", "delegate": "Bounded sub-agent fan-out when parallel cost beats serial execution.", "vibe-coding": "Prompt-led exploration and MVP shipping when deep review is deferred."}'
---

## State location

Agentic-coding state may exist in `<workspace>/agentic-coding/`,
`<workspace>/memory/agentic-coding/`, or `~/agentic-coding/`. `<workspace>` is
the host/runtime workspace root, never the shell cwd.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/agentic-coding/`, `<workspace>/memory/agentic-coding/`,
   `~/agentic-coding/`.
3. If multiple candidates exist, keep only the highest-precedence directory,
   report the duplicates, and leave every other copy untouched.
4. If none exists and durable notes must be created, describe the write, obtain
   consent, then default to `<workspace>/agentic-coding/`. If `<workspace>` is
   unavailable, ask for a state root instead of guessing from the current
   directory.
5. Keep the resolved `<state_root>` fixed for the invocation. Write only real
   filesystem paths; the literal token `<state_root>` is documentation-only.

Use the selected `<state_root>` for every state operation in this skill. Seed
new memory from `assets/memory-template.md`. Domain research anchors live in
`references/sources.md`.

## Positioning

This skill is intentionally different from adjacent coding skills:

- `agentic-engineering` — multi-agent operating patterns and team throughput
- `vibe-coding` — prompt-led exploration and fast idea shipping
- `code` — stepwise plan→execute→verify with approval between steps
- `agentic-coding` — contract-first implementation, proof of fix, reviewer-ready
  handoff

## When to load

Load when the user wants merge-ready code from an AI agent with explicit quality
gates. Typical triggers: production features, risky refactors, bugs with a
reproducible failure, and Xcode-centered work such as Swift feature delivery,
iOS/macOS regressions, and release-branch hotfixes.

Prefer other skills when:

- Multi-agent blast radius / parallel terminals → `agentic-engineering`
- Exploratory MVP without deep review → `vibe-coding`
- Durable style/stack preference systems → `coding`
- Ticket-to-merge / CI/CD / on-call loops → `developer`
- Existing PR risk review → `review-code`

## Architecture

After State location resolution, memory lives under `<state_root>/`:

```text
<state_root>/
├── memory.md       # Persistent preferences and operating mode
├── contracts.md    # Accepted task contracts and non-goals
├── evidence.md     # Test evidence and verification snapshots
└── handoffs.md     # Delivery notes and rollback hints
```

Create optional files only when that feature is needed. Keep unused optional
trees uncreated until a feature needs them.

## Quick Reference

Load these files on demand to keep context focused.

| Topic | File |
|-------|------|
| Setup process | `references/setup.md` |
| Memory template | `assets/memory-template.md` |
| PACT loop | `references/protocol.md` |
| Contract prompts | `references/prompt-contracts.md` |
| Merge handoff checklist | `references/handoff.md` |
| Research sources | `references/sources.md` |

## Core Rules

### 1. Lock a Contract Before Writing Code

Start every task with a compact contract:

- Objective: exact outcome in one sentence
- Acceptance: checks that prove success
- Non-goals: what must stay untouched
- Constraints: stack, style, limits, deadlines

A written contract unlocks coding.

### 2. Run the PACT Loop

Use the same execution loop every time:

1. **P**roblem framing: restate objective and assumptions
2. **A**cceptance design: define checks before edits
3. **C**hange set: produce the smallest useful diff
4. **T**race and test: show evidence and residual risk

This skill is execution discipline, not brainstorming. For Xcode workflows, tie
acceptance to a concrete target, simulator/device, and test command before
editing.

### 3. Keep Diffs Surgical

One user objective maps to one focused change set:

- Prefer file-local edits over broad rewrites
- Separate behavior change from style cleanup
- Keep side effects inside the declared scope

If scope grows, split into a second contract.

### 4. Prove Failure Then Prove Fix

For bugs and regressions:

- Capture the failing condition first (test, log, or reproduction)
- Apply a minimal fix
- Re-run the same check to prove resolution

Every fix claim needs explicit before-and-after evidence.

### 5. Deliver Handoff-Grade Output

End each cycle with a delivery packet:

- What changed and why
- Files touched and blast radius
- Validation run and results
- Known risks and rollback path

Finish only when the handoff answers what changed, why it is trusted, and how to revert.

### 6. Escalate With a Structured Fallback

When blocked after two failed attempts:

- Pause editing
- State what was tried
- Propose two grounded alternatives
- Request a decision with tradeoffs

Prefer explicit options over unguided iteration.

## Execution Guidelines

- Define acceptance checks before implementation so "done" is measurable.
- Prefer surgical diffs that keep review and rollback tractable.
- Separate feature work from architecture overhauls.
- Report success only with reproducible evidence (command + outcome).
- Treat AI output as a draft that still needs review and verification.

## Security & Privacy

**Data that leaves your machine:**

- None from this skill itself

**Data that stays local:**

- Contracts, evidence notes, and handoff summaries under `<state_root>/`

**Operational boundaries:**

- Keep network requests declared and explicit
- Restrict durable skill state to the resolved `<state_root>`
- Keep skill package files immutable at runtime
- Require explicit evidence before claiming risky code is safe to merge
- Defer high-risk security review to the project's designated reviewers
- Follow project contribution rules rather than inventing a parallel process

## Scope

This skill provides:

- Execution quality for AI-assisted coding
- Contract-driven implementation and verification
- Clear handoff packets for reviewers

It does not replace project security review, language-specific skills, or
ticket/CI ownership covered by `developer`.
