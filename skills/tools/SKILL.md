---
name: tools
description: >
  Learn and apply the user's software-tool preferences without capping capability:
  record stack choices, context rules, openness to new tools, and avoid-list
  entries; default to known tools; suggest alternatives only when the gain is
  large. Use when the user states a preference for or against a tool, framework,
  or methodology; asks what tool to use for a task; wants the agent to remember
  their stack; or asks whether to switch tools. Prefer `developer` /
  `software-engineer` for deep coding-toolchain design, `devops` for delivery
  platforms, `productivity` for whole-life capacity and priority, and `notes`
  for long-form tool research notes outside the preference ledger.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🛠️"}'
  related-skills: '{"developer":"Deep coding editor, language, and local toolchain design once a stack preference is known.","devops":"Delivery, CI/CD, container, and cloud platform choices beyond personal defaults.","notes":"Long-form research notes about tools that are not preference ledger rows.","productivity":"Whole-life capacity and priority when tool churn is really overload.","software-engineer":"Broader engineering practice and architecture when the question is not only which app to open."}'
---

## State location

Tools preference state may exist in `<workspace>/tools/`, `<workspace>/memory/tools/`, or `~/tools/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/tools/`, `<workspace>/memory/tools/`, `~/tools/`.
3. If none exists and state must be created, default to `<workspace>/tools/`.

Use the selected `<state_root>` for every state operation in this skill.
If more than one candidate exists, keep the highest-precedence directory only,
report the conflict, and do not merge or cross-write the copies.

```text
<state_root>/
└── preferences.md    # Stack, Preferences, Open To, Avoid — create on first durable preference
```

This skill writes only inside the resolved `<state_root>`. Shared host memory
such as workspace `MEMORY.md` is out of scope unless the host supplies a path
and the user consents to that external write.

## When to load

- User states a lasting tool preference, avoid-list item, or stack default
- User asks which tool to use and past preferences should shape the default
- User asks whether to switch tools or chase a trend
- Not for deep editor/CI design (`developer` / `software-engineer` / `devops`) or whole-life overload (`productivity`)

## Adaptive tool intelligence

You can use any tool and learn a new one on demand. This skill tracks **user
defaults**, not agent limits.

### Operating sequence

1. Resolve `<state_root>`. Read `<state_root>/preferences.md` when it exists.
2. Classify the request: record a preference, recommend a tool, decide whether
   to suggest a switch, or handle an unfamiliar tool name.
3. For recommendations, start from Stack and Preferences. Load
   `references/dimensions.md` when categorizing a new entry. Load
   `references/criteria.md` when deciding whether to suggest an alternative.
4. Write durable preference changes only after the user has stated them (or
   confirmed a proposed entry). Create `preferences.md` from the template below
   on first write.
5. Keep capability open: an empty Stack means "no recorded default yet", not
   "limited agent".

### Core rules

- Keep always-on guidance short; defer category taxonomies and switch thresholds
  to `references/` until those branches apply.
- Default to the user's known tools when Stack or Preferences already cover the
  category.
- Suggest an alternative only when the task is clearly harder under the current
  tool, the user asked for a better way, Open To allows it, and the expected
  gain is hours—not minutes—after switching cost.
- Learn unfamiliar tools by acknowledging the gap, researching or asking once,
  then adapting; add them to Stack only when the user uses them regularly.
- Keep entries short: `category: tool` or `context: approach`.

### `<state_root>/preferences.md` template

Create this file on first durable preference write:

```markdown
### Stack
<!-- Tools the user actively uses. Format: "category: tool" -->

### Preferences
<!-- When to use what. Format: "context: tool or approach" -->

### Open To
<!-- Appetite for new tools. Format: trait -->

### Avoid
<!-- Tools or patterns the user rejected -->
```

### Reference routing

| Reference | Load when |
|---|---|
| `references/dimensions.md` | Categorizing a tool, usage pattern, discovery appetite, or decision factor. |
| `references/criteria.md` | Deciding whether to add to Stack, keep the current tool, or suggest a switch; shaping entry wording. |
| `references/sources.md` | Citing preference-learning or progressive-disclosure sources in a review or PR. |

### Failure recovery

| Symptom | Recovery |
|---|---|
| Multiple candidate state dirs | Keep highest-precedence only; report paths; do not merge. |
| Missing `preferences.md` | Work from no defaults; create the template only when writing a real preference. |
| User rejects a suggestion | Record under Avoid or Preferences if they want it durable; continue with their choice. |
| Unfamiliar tool name | State the gap, research or ask once, then proceed with verified product facts only. |
| Preference conflicts with task needs | Name the conflict, quantify switching cost vs benefit, let the user choose. |
