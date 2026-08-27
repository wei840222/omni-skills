## Output Gates

Before handing back any Markdown:

- Which target is this for, and does every construct I used exist there (Support Matrix)?
- Blank line above and below each list, table, fence, and blockquote?
- Every fence closed, closing run ≥ opening run, language tag present?
- Every nested list at the content-column indent Rule 3 gives for its parent marker?
- Every link destination free of raw spaces and parens; every anchor derived from the target's slug rule, not invented?
- Every image with alt text that says what it is for, and no heading level skipped?
- No secret in any code sample, curl line, config snippet, or env block — and none written into `<workspace>/`?
- Editing an existing file: is the diff limited to the lines the task named?
- Did this session produce something durable — a target and its quirk, a doc set, a config that finally passed, a conversion recipe, a template, a sweep result? Then it is written to its box in `<state_root>/memory.md`, with its `## Boxes` line, in this same turn.
