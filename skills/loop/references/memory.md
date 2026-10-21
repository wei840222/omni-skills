# Memory Between Iterations

## What to Persist

Stored in `<state_root>/loop/history/{loop-id}.json`:

- **learnings** — Append-only log: what tried, what happened, what to try next
- **progress** — Structured state for complex multi-step tasks
- **iteration_count** — Current iteration number

## What Not to Persist

- Full conversation history (context bloat)
- Failed code attempts (noise)
- Intermediate debugging output

## Storage Location

All loop data stored in `<state_root>/loop/`:

- `active.json` — Currently running loops
- `history/{id}.json` — Completed loop logs
- `learnings.md` — Cross-loop patterns (optional)

## Cost Awareness

Loops multiply cost. Before starting:

- Estimate tokens per iteration
- Confirm with the user if more than 10 iterations look likely
- Consider whether the approach should change rather than iterate

## Safety Note

This skill does not:

- Make Git commits automatically
- Persist data outside `<state_root>/loop/`
- Modify files without explicit task approval
