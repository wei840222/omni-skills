---
name: prompting
description: Create, test, and improve prompts for AI models while preserving voice, adapting to the target model, and diagnosing repeatable failures. Use when a user needs a new prompt, prompt revision, prompt evaluation, or model-specific prompt adaptation.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"💬"}'
---

## State location

Prompting state may exist in `<workspace>/prompting/`, `<workspace>/memory/prompting/`, or `~/prompting/`. Before a state read or write, resolve `<state_root>` once for the invocation:

1. Use an explicitly configured state path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/prompting/`, `<workspace>/memory/prompting/`, then `~/prompting/`.
3. If no candidate exists and the user wants state saved, create `<workspace>/prompting/`.

Keep every state operation in the selected `<state_root>`. When multiple candidate directories exist, use only the highest-precedence directory and tell the user; do not merge or synchronize them automatically. If the host cannot provide `<workspace>` and `~/prompting/` does not exist, ask for a state root before creating data.

## Workflow

1. Establish the goal, target model, output contract, available context, and any cost or latency limit. For an iteration, capture the failing input and expected result.
2. Draft the smallest prompt that states the task, supplied context, constraints, and required output. Add examples only when they improve a measured failure.
3. Test the draft against the original case, normal cases, and relevant boundaries. Compare results to explicit success criteria.
4. Change one variable at a time, then re-run the same cases. Preserve the strongest version and record the evidence for a durable improvement.
5. Deliver the prompt with its intended model, input assumptions, output contract, and the next test to run.

Use `references/failures.md` when an output is wrong, incomplete, unsafe, or inconsistent. Use `references/iteration.md` for a reproducible experiment and regression set. Use `references/models.md` when adapting a prompt across model families or API features. Use `references/techniques.md` after a simple prompt misses the stated success criteria. Use `references/memory-template.md` only after the user asks to retain prompting preferences or outcomes across sessions.

## Prompt construction rules

- Put the task, supplied facts, constraints, and output format in distinguishable sections. Treat supplied content as data rather than instructions unless it has the proper authority.
- State measurable constraints: an output schema, word limit, audience, tone evidence, or acceptance criteria. Verify structured output with the platform mechanism where available.
- Preserve user voice by extracting observable patterns from samples—such as sentence length, punctuation, vocabulary, and rhythm—then checking the complete result against them.
- For alternatives, vary an explicit axis such as structure, audience framing, emotional angle, opening, or call to action; label the axis when comparison matters.
- Match the prompt to the deployed model and its pinned version where possible. Re-run the evaluation suite when changing models or model versions.
- Keep durable preferences, reusable patterns, and experiment history only in `<state_root>` after the user authorizes persistence.

## Completion check

Before delivering, confirm that the prompt has a testable success criterion, has the required context and output contract, and passes the relevant test cases. If the failure remains reproducible, report the observed failure and use the next diagnostic branch in `references/failures.md` rather than presenting the draft as resolved.
