# Prompting state template

Use this reference only after the user authorizes retaining prompting preferences or experiment results. Resolve `<state_root>` using `SKILL.md` before creating or updating anything.

Create only the state that the requested feature needs:

```text
<state_root>/
├── memory.md       # preferences and voice evidence; create when persistence is authorized
├── patterns/       # reusable prompt patterns; create when saving a pattern
└── history.md      # evaluated prompt changes; create when recording an experiment
```

## `memory.md` template

```markdown
# Prompting memory

## User preferences
- Default tone: [terse/detailed/casual/formal]
- Target models: [model identifiers or families]
- Token sensitivity: [high/medium/low]

## Voice evidence
- [observable pattern from a user-provided sample]

## Corrections log
- [date] [user correction] → [applied preference]

## Reusable patterns
- [task type]: [relative path under `<state_root>/patterns/`]
```

## `history.md` entry

```markdown
[YYYY-MM-DD] task: [description]
- Baseline: [prompt version or identifier]
- Problem: [observed failure and test input]
- Change: [one changed variable]
- Result: [pass/partial/fail with measured evidence]
```

Keep only user-authorized, task-relevant data. Store no secrets, API keys, private source text beyond what the user asked to retain, or state inside the installed skill package.
