# AI-Assisted Learning — Hint Policy and Offload Boundary

Load when an agent answers so fast that nothing is learned, or when the learner is helpless without the model.

## `hint_policy`

| Value | Behavior |
|-------|----------|
| on-request | Hint when asked |
| after-attempt | Require a visible attempt first (default) |
| never | Withhold until the learner asks twice |

## What stays with the learner

- Wait for a visible attempt before producing the retrieval answer
- Keep edits sparse so the learner still owns the solution
- State mastery only after a dated ladder test

## Offload boundary

The agent may hold the schedule, rubric, and error log. The learner must still perform retrieval and production. If capability collapses when the agent is removed, raise `hint_policy` and rebuild with cold tests.
