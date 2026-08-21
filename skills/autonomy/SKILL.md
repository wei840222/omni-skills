---
name: autonomy
description: Identify repeated, conversation-based work and propose a consented delegation pilot with measurable boundaries. Use when a user repeats a task, describes manual friction, asks to automate a workflow, or wants to expand an agent's authority safely.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🤖"}'
---

## State location

Autonomy state may exist in `<workspace>/autonomy/`, `<workspace>/memory/autonomy/`, or `~/autonomy/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured state path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/autonomy/`, `<workspace>/memory/autonomy/`, then `~/autonomy/`.
3. If more than one candidate exists, use only the highest-precedence directory and tell the user that separate copies exist.
4. If no candidate exists and the user asks to save delegation state, create `<workspace>/autonomy/`.
5. Keep the selected `<state_root>` fixed for this invocation. The resolver selects a location; it does not authorize a write.

Use `<state_root>/tracking.md`, `<state_root>/proposals.md`, and `<state_root>/rejected.md` for delegated-work records, pending proposals, and declined proposals.

## Scope

This skill identifies repeated work from the active conversation, proposes bounded delegation opportunities, and tracks approved pilots. It uses explicit user statements, repeated conversational requests, and user-described friction as its evidence.

Keep observations in the active conversation. Before accessing an integration such as calendar or email, request the specific permission needed. Before taking a task over, obtain explicit approval for its task, authority level, and pilot boundary.

## Workflow

1. Identify a pattern from the active conversation and state the evidence: repeated request, rubber-stamp approval, or expressed frustration.
2. Load `references/bottlenecks.md` when the pattern needs a severity score, a bottleneck inventory, or a structured proposal record.
3. Propose a pilot: name the task, boundary, duration or count, notifications, success signal, and rollback path. Ask for explicit approval.
4. After approval, begin at the agreed level and record the pilot in `<state_root>/tracking.md` only when persistent tracking is authorized.
5. Load `references/expansion.md` when moving between responsibility levels, evaluating exit criteria, or handling a rollback.
6. At each expansion decision, present the measured pilot result and ask for approval before changing authority.

## Delegation proposal

```text
💡 Delegation opportunity

I noticed: [conversation evidence]
Pattern: [frequency or repeated request]

Proposal: I can handle [specific task] within [explicit boundary].
Pilot: [number or duration], with [notification/review point].
Success signal: [measurable result].
Rollback: [how authority returns to the previous level].

Do you approve this pilot?
```

## Authority levels

| Level | Operating boundary |
| --- | --- |
| L1 | Complete only the task currently requested. |
| L2 | Handle agreed gaps and edge cases within the approved task boundary. |
| L3 | Run the approved workflow after a successful pilot, with the agreed reporting cadence. |

A move to a higher level requires explicit user approval. If a pilot produces an unexpected outcome, pause that pilot, notify the user with the observed context, return to the prior agreed level, and use the rollback procedure in `references/expansion.md` before resuming.

## Resources

| Resource | Load when |
| --- | --- |
| `references/bottlenecks.md` | Assessing frequency, time cost, risk, priority, or documenting a candidate bottleneck. |
| `references/expansion.md` | Planning a pilot, evaluating a responsibility phase, rolling back, or reporting autonomy progress. |
| `references/research.md` | Explaining the human-automation trust rationale behind a delegation recommendation. |

## Completion check

A delegation proposal is complete when it contains conversation evidence, a specific boundary, an explicit approval request, a measurable pilot outcome, and a rollback route. Persistent records are updated only after the user authorizes tracking.
