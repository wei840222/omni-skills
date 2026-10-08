---
name: collaborate
description: >
  Structure collaboration by selecting a counterpart, running a bounded exchange on
  a plan or decision, and landing one decision or a recorded disagreement. Use when
  a plan needs critique, red-teaming, or a devil's advocate before commitment; when
  giving or asking for a second opinion, design review, or draft feedback; when a
  review thread loops without anyone changing position; when a group review or
  pairing session needs structure; or when choosing between collaborating,
  delegating, and working solo. Not for routing specified work to sub-agents
  (delegate) or fanning out many parallel viewpoints (diverge).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🤝"}'
  related-skills: '{"delegate":"Routes specified work to sub-agents when acceptance criteria are already writable.","diverge":"Fans out multiple parallel viewpoints before synthesis.","six-thinking-hats":"Structured multi-hat parallel thinking for option analysis.","brainstorm":"Generates option volume before a focused collaborative exchange."}'
---

## State location

Collaborate state may exist in `<workspace>/collaborate/`, `<workspace>/memory/collaborate/`, or `~/collaborate/`.

Before reading or writing state, resolve `<state_root>` once per invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/collaborate/`, `<workspace>/memory/collaborate/`, `~/collaborate/`.
3. If none exists and the user wants persistent tracking, create `<workspace>/collaborate/`. If `<workspace>` is unavailable, ask for a state root instead of guessing from the current directory.
4. If more than one candidate exists, use only the highest-precedence directory and report the conflict; do not merge trees automatically.

Use the selected `<state_root>` for every state operation in this skill. Prefer portable `<state_root>` paths; never hard-code host-specific absolute roots. Skill resources stay under `references/`; never treat the literal string `<state_root>` as a filesystem path.

```text
<state_root>/
├── config.yaml      # round_cap, budget_share, solo_undo_threshold, counterpart_mode, log_decisions
└── decisions.md     # convergence records when log_decisions is true
```

Create or update state only after the user opts in. Store decision records and preferences only—no private credentials or third-party secrets.

Defaults and preference areas live in `references/state.md`.

## Overview

This skill structures collaboration: picking one counterpart, running a bounded exchange on a plan or decision, and landing a single design or a recorded disagreement. It prevents endless review loops and unverified echo chambers.

## Core path

1. Load `references/domain.md` for when-to-use checks, routing against solo/delegate, counterpart selection, exchange steps, output gates, and traps.
2. Run the exchange with one falsifiable question, a written position plus kill condition, and the two-round movement rule.
3. Converge to one whole design (not an average), name the strongest surviving objection, and record a revisit trigger.
4. When `log_decisions` is on, append the record under `<state_root>/decisions.md` using `references/decision-log.md`.

## Depth on demand

| Need | Load |
| --- | --- |
| Attack untested assumptions | `references/adversarial-review.md` |
| Choose between defensible options | `references/second-opinions.md` |
| Judge audience reception | `references/audience-pass.md` |
| Counterpart catalog / simulation | `references/counterparts.md` |
| Briefing and falsifiable questions | `references/briefing.md` |
| Stuck exchange / escalate | `references/deadlock.md` |
| Decision record shape | `references/convergence.md` |
| Multi-party review | `references/group-review.md` |
| Human critique register | `references/with-humans.md` |
| Agent counterpart independence | `references/with-agents.md` |
| Live driver/navigator pairing | `references/pairing.md` |
| Collaborate vs delegate routing | `references/vs-delegate.md` |
| Persistent log format | `references/decision-log.md` |

## Failure modes

- Predictable counterpart response with no kill condition → skip the exchange; own the decision.
- Acceptance criteria already writable → route to `delegate` instead of collaborating.
- Two rounds with zero movement → stop, record disagreement, escalate only if blocking.
- Simulated counterpart that shares your incentives and data → replace the lens or feed different inputs.
