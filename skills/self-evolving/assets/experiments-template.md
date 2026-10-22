# Experiment Log Template

Use `<state_root>/experiments.md` to keep tentative ideas separate from stable
memory.

## Entry format

```markdown
## YYYY-MM-DD HH:MM - Short experiment name
- Trigger: what failure or friction caused the test
- Baseline: what the agent was doing before
- Mutation: the one change being tested
- Outcome: better | worse | mixed
- Evidence: concrete observation, metric, or user feedback
- Next move: promote | retest | discard
```

## Promotion rule

- Promote only after three comparable wins
- If results are mixed, narrow the mutation and retest
- If the change causes instability, discard it and keep the older baseline

## Good examples

- "Added a pre-flight checklist before file edits; reduced missed references in three reviews"
- "Moved retrieval before drafting; improved consistency across repeated planning tasks"

## Weak examples

- "Be more adaptive"
- "Try harder next time"
- "Maybe this is better"
