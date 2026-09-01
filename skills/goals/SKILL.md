---
name: goals
description: Structure, track, and review personal outcome goals with milestones and lightweight progress logs. Use when the user defines an aspiration, asks to create or update a goal, reports goal progress or a blocker, or requests a weekly, monthly, quarterly, or yearly goal review. Use task or project planning skills for immediate to-dos and execution plans.
metadata:
  openclaw: '{"emoji":"🎯"}'
---

## State location

Goals state may exist in `<workspace>/goals/`, `<workspace>/memory/goals/`, or `~/goals/`. Before a state operation, resolve `<state_root>` once for the invocation:

1. Use an explicitly configured state path when one is supplied.
2. Otherwise, use the first existing directory in this order: `<workspace>/goals/`, `<workspace>/memory/goals/`, then `~/goals/`.
3. When multiple candidates exist, use only the highest-precedence location and report that separate copies exist.
4. When none exists and the user requests persistent goal tracking, create `<workspace>/goals/`.
5. When the host does not provide `<workspace>`, use an existing `~/goals/`; otherwise request a state path before creating data.

Keep the selected `<state_root>` for all state operations. Create `active/`, `achieved/`, `abandoned/`, and `someday.md` only when the corresponding goal-management action needs them.

## Workflow

1. Classify the request with `references/goal-structure.md`: a goal is an outcome, a project is a defined body of work, and a habit is recurring behavior. Route immediate execution work to task or project planning rather than treating it as a goal.
2. For a new goal, clarify the success condition, target date, motivation, first step, and a small set of observable milestones. Load `references/domain-knowledge.md` when calibrating challenge, feedback, or blocker plans.
3. When the user asks to save or track it, resolve `<state_root>`, then create or update `<state_root>/active/<goal-name>.md` with the outcome, why, target date, milestones, current status, and dated progress log.
4. For progress updates and reviews, load `references/tracking-and-review.md`; record concise evidence, blockers, and the next meaningful action.
5. For stalled, paused, or completed goals, load `references/management-and-motivation.md`. Preserve the user’s decision: break down a still-valued goal, move a reprioritized goal to `<state_root>/abandoned/` with a reason, or record a future idea in `<state_root>/someday.md`.

If the user cannot yet state an outcome or deadline, capture the aspiration as a question and ask for the next smallest clarification rather than fabricating a target. If an existing goal file conflicts with the user’s current intent, present the conflict and obtain the user’s chosen update before changing saved state.

## Reference routing

| Resource | Load when |
| --- | --- |
| `references/goal-structure.md` | Classifying a goal, project, or habit; defining milestones; creating a goal file |
| `references/tracking-and-review.md` | Logging progress or conducting weekly, monthly, quarterly, or yearly reviews |
| `references/management-and-motivation.md` | A goal stalls, priorities change, a milestone completes, or motivation needs support |
| `references/domain-knowledge.md` | Calibrating specificity, difficulty, feedback, commitment, or implementation intentions |

## Working principles

- Keep the active set small: three to five active goals, with one demanding goal receiving primary focus.
- Use clear outcomes and evidence-based progress; a lightweight file and dated entries are sufficient.
- Treat a changed priority as a valid decision. Record its rationale so a future review can learn from it.
- Celebrate completed milestones before choosing the next objective.

## Cognitive-load audit

Keep the main path to classification, clarification, saving, and review. Load one routed reference when its situation occurs, and use the concrete next action or question it provides rather than repeating every policy in the response.
