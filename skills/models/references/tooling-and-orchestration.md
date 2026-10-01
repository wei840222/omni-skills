# Tooling fit and orchestration

## Interactive coding agents vs long-running workers

| Shape | Fit | Tradeoff |
|-------|-----|----------|
| Interactive coding agent (Claude Code-class) | Fast iteration, UI/frontend, in-loop debugging | Developer stays engaged; huge single files can stress the loop |
| Long-running worker (Codex CLI-class) | Large refactors, background jobs, set-and-forget | Accuracy and continuity over snappy chat UX |

Both patterns are valid. Common split retained from the pre-refactor skill: interactive agent for implementation loops; stronger/long-running worker for bulk refactor and final pass when the user wants less babysitting. File-size and tool limits differ by product—confirm on current docs before stating a hard token ceiling.

## Plan → execute → review

1. **Plan** with a high-reasoning class: break the problem, name risks, define acceptance checks.
2. **Execute** with a balanced or fast class; parallelize independent subtasks when tools allow.
3. **Review** with a thorough class (or a second vendor) against tests and the plan.

This portfolio often beats one model for everything at similar total spend because cheap mistakes are caught before merge.

## Failure modes

- Using frontier models for chatbot-scale simple replies
- Ignoring context limits and paying for repeated failed chunking
- Expecting bit-identical answers across model updates
- Trusting speed-optimized models as the only reviewer on safety-critical code
- Skipping live verification for prices/ranks (`ai` + `sources.md`)
