# Pull Requests, Diffs, and Releases

Scope: PR descriptions, diffs, commit ranges, release notes.

## Rank by behavior change

- Lead with user/runtime behavior change and breaking changes.
- Files touched are evidence, not the summary.
- Call out migrations, flag flips, API contract changes, and rollback notes when present.

## Shape

```
Behavior change
Breaking / risk
Ops notes (migrate, flag, monitor)
Omitted (refactors with no behavior delta, if material to say so)
```

## Traps

- Listing file paths instead of effects
- Treating test-only or import-churn diffs as product changes
- Dropping "not in this PR" limitations the author stated
