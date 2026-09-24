# Blast radius

Blast radius is the impact zone of one prompt: files touched, time, and how hard a mistake is to undo. Estimate it before opening another agent.

## Sizing

| Prompt | Typical footprint | Radius | Next move |
|---|---|---|---|
| Fix a typo or label | 1 file, seconds | Tiny | Run beside other tiny tasks |
| Add a loading state | 1–2 files, a few minutes | Small | Parallel is fine when each agent has an exclusive path |
| Add one API endpoint | 3–5 files | Medium | One or two agents, watch the shared types |
| Rewrite auth or a migration | 10+ files | Large | One agent, plan before edits |
| Framework migration | Most of the tree | Massive | Phases, one checkpoint commit each |

Ask the agent to list files and a short plan when the radius is unclear. Start edits only after the user accepts that plan.

## By radius

- Tiny or small: several agents, each with an exclusive path.
- Medium: one agent on the feature, plus a second only on files the feature will not touch.
- Large: one agent. First prompt asks for options, not a patch.
- Massive: split into plan, core change, dependents, and tests. Commit at each phase boundary.

## Scope lock

State the allowed path in the prompt:

```text
Change only src/components/SubmitButton.tsx. Leave tests and copy for a later prompt.
```

A follow-up that says "while you are there" is a new radius estimate, not a free add-on.

## Mid-flight

If the agent runs longer than the estimate:

1. Pause generation.
2. Ask what files it has changed and what it plans next.
3. Choose help, a narrower prompt, or abort.

Keep large work in small, reviewable increments.
