# PACT Loop - Agentic Coding Protocol

PACT keeps AI coding predictable under time pressure. Ground acceptance design
in verifiable checks (tests, builds, screenshots) as described in
`references/sources.md`.

## P: Problem Framing

Write a compact brief before editing:

- Target behavior
- Current gap
- Scope boundary
- Definition of done

Output format:

```text
Objective:
Gap:
Scope:
Done when:
```

## A: Acceptance Design

Define checks before touching code.

Minimum acceptance set:

- One check that fails before changes
- One check that must pass after changes
- One guardrail that must remain unaffected

Examples:

- Bug fix: failing reproduction, then passing reproduction
- Feature: new test plus unchanged baseline tests
- Refactor: behavior parity checks plus static quality gate

For Xcode work, name the scheme/target, simulator or device, and exact test
command in the acceptance block before edits.

## C: Change Set

Implement only what the contract requires.

Rules:

- Keep file count as low as possible
- Keep behavioral changes strictly isolated from broad renames
- Split optional cleanup into follow-up contracts

## T: Trace and Test

Produce concrete evidence and decision support.

Report:

- Commands executed
- Pass or fail outcomes
- Residual risk with explicit rationale
- Recommended next action

Do not claim success from narrative alone. Show the check output.

## Escalation Triggers

Pause execution and escalate when:

- Two implementation attempts fail
- Acceptance cannot be measured with available tooling
- The requested scope conflicts with project constraints

Escalation packet:

- What was attempted
- What blocked progress
- Two alternative paths with tradeoffs
