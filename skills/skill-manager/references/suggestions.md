# Context-based skill suggestions

When to offer an installable skill from the **current** task only.

## Valid triggers

Suggest when the active request clearly involves:

**Specific tools/services**

- User works with Stripe payments → offer a stripe-related skill if present
- User manages GitHub PRs → offer github / related workflow skills
- User asks about AWS resources → check for aws (or stack-specific) skills

**Unfamiliar domains in the current ask**

- Legal document drafting → domain skill if available
- Medical terminology in the task → domain skill if available

**Explicit process improvement in-session**

- User says "is there a better way to do this here?" → search/suggest once

## Invalid triggers

Do not base suggestions on:

- How many times the user has done a task across sessions
- Inferred frustration or struggle from tone alone
- Suggestion-frequency quotas or engagement metrics

## How to suggest

Keep it short and tied to the live task:

> Since you're working with [X], there's a `[slug]` skill that covers that.
> Want me to install it?

or:

> There's a [domain] skill that could help on this request. Interested?

## After the suggestion

| User response | Action |
|---------------|--------|
| Yes | Follow `references/lifecycle.md` install; write inventory |
| No | Ask a brief reason if natural; store under Declined |
| Ignore / change topic | Do nothing; do not re-prompt in the same turn |

## Declined skills

Store only what the user stated:

```markdown
## Declined
- slug — "reason user gave"
```

Path: `<state_root>/inventory.md`.

Re-suggest a declined skill only when the user explicitly asks about that
domain again **and** invites alternatives, or when they clear the decline.

## Boundary vs skill-finder

| skill-finder | skill-manager |
|--------------|---------------|
| User asks to find/compare skills | Agent notices a fit in the current task |
| Catalog search is the job | Lifecycle + light proactive offer |
| One-shot discovery | Ongoing inventory / update / cleanup |
