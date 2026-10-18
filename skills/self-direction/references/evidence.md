# Evidence Logging

Use `<state_root>/self-direction/evidence.md` for raw observations that may later
promote into `direction.md`.

## Why separate evidence from the model

- Keeps the direction model concise
- Preserves provenance for confidence changes
- Makes contradictions reviewable instead of silently overwritten

## Entry shape

```text
## YYYY-MM-DDTHH:MM

signal: explicit | implicit | correction
component: values | goals | criteria | resources | boundaries | patterns
context: work | personal | both
quote_or_observation: "..."
inferred_pattern: "..."
confidence_delta: low → medium
promoted_to: direction.md#Speed-vs-Quality | none
```

## Rules

1. Log before promoting. Do not invent evidence to justify an action already taken.
2. Prefer the user's words for explicit signals.
3. Mark corrections clearly; a correction outranks older same-topic evidence.
4. Require repeated independent observations before raising confidence to high
   unless the user stated the rule explicitly.
5. Never delete conflicting evidence; move the conflict summary to
   `conflicts.md` and keep both raw entries.
6. Do not store secrets, credentials, private third-party data, or unrelated
   chat dumps in evidence files.

## Promotion checklist

Promote an observation into `direction.md` only when:

- The component is clear
- The pattern is actionable
- Confidence is set honestly
- Related boundaries were checked for conflict
