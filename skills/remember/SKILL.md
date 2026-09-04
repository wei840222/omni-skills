---
name: remember
description: Manage durable cross-session memory: capture, retrieve, update, archive, or forget explicit preferences, commitments, corrections, decisions, and relationship context when the user asks.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧠"}'
  related-skills: '{"loop":"Uses durable memory as input to iterative improvement.","reflection":"Reviews learned context and decisions during self-evaluation."}'
---

## State location

This skill stores user-approved durable memory. Before a state operation, resolve `<state_root>` once:

1. Use an explicit user- or host-configured path when one exists.
2. Otherwise select the first existing directory in this order: `<workspace>/remember/`, `<workspace>/memory/remember/`, `~/remember/`.
3. If none exists and the user has asked to save memory, create `<workspace>/remember/`.

Keep the selected `<state_root>` for the whole invocation. When more than one candidate exists, use the highest-precedence directory, report the duplicate copies, and leave them independent. When `<workspace>` is unavailable and `~/remember/` is absent, obtain a state root before creating data.

## Workflow

1. Identify the request: save, retrieve, update, review, archive, or forget.
2. For saves, record durable, useful information with the date, source (`explicit` or `inferred`), and confidence. Persist sensitive information only after the user explicitly asks to save it.
3. Store the entry in the matching `<state_root>/memory/` category. Create only the category files needed for the current request.
4. For a conflicting update, retain the prior record with an update note; make the newest confirmed information active.
5. For retrieval or review, load only the categories relevant to the request, then report uncertainty and stale entries plainly.
6. For a forget request, remove the requested data from the resolved state root and confirm the completed scope. Resolve an ambiguous target with the user before removing data.

## What to retain

- **High value:** explicit commitments, corrections, preferences, core relationships, and decisions with rationale.
- **Reviewable:** active project context and durable domain lessons.
- **Transient:** keep one-off questions and easily reconstructed conversation context in the current session rather than durable memory.

Apply the staleness test: would this entry help rather than mislead if retrieved in six months? Archive completed commitments after 30 days and inactive context after 60 days when the user requests maintenance.

## Category layout

Use `<state_root>/memory/` as the category root:

```text
<state_root>/memory/
├── commitments.md
├── preferences.md
├── corrections.md
├── decisions.md
├── relationships.md
├── contexts/
└── archive/
```

## Reference routing

- Read `references/categories.md` when categorizing an entry or creating a category file.
- Read `references/consolidation.md` for end-of-session review, maintenance, contradictions, archiving, or deletion decisions.
- Read `references/research.md` only when you need the background principles and sources behind memory curation.
