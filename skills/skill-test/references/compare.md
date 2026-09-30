# Comparing Skills

A/B testing when two skills could solve the same job.

## Setup

Place each candidate in its own disposable directory (or separate sub-agents). Do not install both into the live skill path just to compare.

```bash
mkdir -p /tmp/compare/skill-a /tmp/compare/skill-b
# Copy or install each candidate into its own folder only
```

## Comparison process

1. **Define one shared task** — same prompt, same constraints, same success criteria
2. **Run through each** — separate sub-agents or separate static traces
3. **Capture outputs** — final answer, steps taken, failures, rough token use
4. **Present side-by-side** — show both results without ranking until the user chooses
5. **Ask preference** — which feels better and why

## Comparison criteria

| Aspect | Skill A | Skill B |
|--------|---------|---------|
| Output quality | | |
| Ease of use / trigger fit | | |
| Token efficiency | | |
| Coverage of the shared task | | |
| Clarity of instructions | | |
| Safety / side effects | | |

## Asking the user

> I tested both skills on [task]:
> - Skill A: [brief result]
> - Skill B: [brief result]
>
> Which feels better for your workflow? Any hard requirements (safety, cost, latency)?

## Recording preference

After consent, append to `<state_root>/comparisons.md`:

- Date and shared task
- Winner (or tie)
- User's stated reason
- Context that should change the next recommendation

## When results are close

If quality is similar, surface maintenance signals the user can verify:

- Recent commits or release notes on the package source
- Author or maintainer continuity
- Overlap with skills already installed
- Let the user decide; do not force a winner
