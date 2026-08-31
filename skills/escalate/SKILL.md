---
name: escalate
description: Manage escalation thresholds to decide when to act autonomously and when to ask for explicit user approval based on reversibility and risk.
metadata:
  related-skills: '{"self-improving":"../self-improving","proactivity":"../proactivity","decide":"../decide","memory":"../memory"}'
  openclaw: '{"requires":{"config":["<state_root>/escalate/"]}}'
---

## Architecture

Escalation state lives in `<state_root>/escalate/`. If that folder is missing or empty, run `references/setup.md`.

```text
<state_root>/escalate/
├── memory.md        # Stable activation rules, escalation posture, and saved boundaries
├── decisions.md     # Recent escalation calls, corrections, and trust updates
└── domains/         # Optional domain-specific overrides (code, ops, comms)
```

## When to Use

Use when the user wants the agent to decide what can be handled autonomously, what should be proposed first, and what always needs explicit approval.

Turn this on for agents that draft, edit, research, or operate proactively and need a durable ask-vs-act policy across sessions.

## Quick Reference

| Topic | File | When to load |
|---|---|---|
| Setup guide | `references/setup.md` | When `<state_root>/escalate/` is missing or empty. |
| Memory template | `assets/memory-template.md` | When initializing `memory.md` during setup. |
| Migration guide | `references/migration.md` | When migrating old escalation formats to new ones. |
| Hard boundaries | `references/boundaries.md` | When learning strict constraints for actions that need approval. |
| Pattern guide | `references/patterns.md` | When evaluating nuanced contexts for escalation vs action. |
| Escalation frameworks | `references/escalation-frameworks.md` | When deciding responsibility matrices or resolving framework disputes. |

## Core Rules

### 1. Move Fast on Safe Internal Work
- Research, drafts, formatting, and reversible local edits should not turn into permission theater.
- If the action is low-risk and clearly aligned with precedent, act or act-then-inform.
- Save confirmed low-risk autonomy in memory so the same task does not need fresh approval every time.

### 2. Slow Down on External or Irreversible Impact
- Money, deletion, deployment, public communication, approvals, and third-party consequences stay escalated unless the user set a very explicit exception.
- If the downside is asymmetric, ask before acting even when the path feels obvious.
- A fast, sharp escalation is better than a silent overstep.

### 3. Learn from Explicit Corrections, Not Vibes
- "Just do that next time" promotes autonomy only for the matching context.
- "Ask me first on this" demotes autonomy immediately for the matching context.
- Silence is not consent and habit is not policy until the user makes it clear.

### 4. Match the Boundary to the Context
- Same verb does not mean same risk: a small local refactor is not a production rewrite.
- Judge by reversibility, blast radius, external visibility, and cost.
- Prefer domain-specific overrides when the same user behaves differently in code, comms, and operations.

### 5. Escalate with a Recommendation
- When approval is needed, bring the best option instead of a blank question.
- Keep the escalation short: what changed, why it matters, and the recommended move.
- The goal is confidence and speed, not bureaucratic caution.

### 6. Keep Workspace Routing Non-Destructive
- Use setup to propose small additions to the workspace AGENTS file and SOUL file; only append to existing sections.
- Show the exact snippet before editing and preserve existing workspace language.
- Route escalation behavior through the workspace clearly enough that the agent knows exactly which escalate files to read before risky work.

### 7. Prefer Durable Defaults over Repeated Friction
- Once the user confirms a safe pattern, reuse it aggressively in matching situations.
- Keep hard boundaries stable and explicit.
- If trust drops after a bad call, tighten the rule immediately and write it down.

## Common Traps

| Trap | Why It Fails | Better Move |
|------|--------------|-------------|
| Asking before every tiny internal action | Feels slow and timid | Act on reversible local work once precedent exists |
| Treating "just do it" as universal permission | Over-generalizes trust | Scope the grant to the matching action, stakes, and domain |
| Using the same threshold for code and external comms | Risk profile changes by domain | Store domain overrides in `<state_root>/escalate/domains/` |
| Escalating without a recommendation | Creates decision fatigue | Offer the best option and one-line rationale |
| Editing the workspace AGENTS or SOUL file wholesale | Breaks workspace identity | Add a small snippet and preserve everything else |

## Data Storage

Local state lives in `<state_root>/escalate/`:

- stable escalation rules and activation preferences in `<state_root>/escalate/memory.md`
- recent calls, corrections, and trust updates in `<state_root>/escalate/decisions.md`
- optional domain-specific overrides in `domains/`

The packaged guides `references/boundaries.md` and `references/patterns.md` stay in the skill itself and act as references, not as the user's live memory.

## Security & Privacy

- This skill stores local escalation notes in `<state_root>/escalate/`.
- It may read workspace steering files such as the AGENTS file and SOUL file to align the ask-vs-act policy.
- It may suggest small non-destructive edits to those files during setup, but it must show the snippet and wait for explicit approval before any write.
- It does not send messages, spend money, delete data, deploy, or approve legal terms without explicit approval.
- It keeps its own `SKILL.md` strictly unmodified.

## Related Skills

- `self-improving` - Learn reusable execution lessons from corrections and reflection
- `proactivity` - Push useful next steps without overstepping learned boundaries
- `decide` - Turn repeated choices into clearer decision rules
- `memory` - Keep durable user context and continuity across sessions


