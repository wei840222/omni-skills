---
name: skill-manager
description: >
  Manage installed agent-skill lifecycle: suggest by current task context, track
  installs and declines, check/update versions, and clean up unused skills with
  explicit consent. Use when the user asks what skills they have, whether to
  install or update one, how to clean unused skills, or when the current task
  clearly matches an installable skill the user has not declined. Prefer
  skill-finder for user-initiated catalog search, skill-update for
  preview/backup/rollback of one upgrade, and skill-audit before trusting a
  new package. Not for authoring skills (skill-builder) or publishing
  (skill-publish).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧩","requires":{"bins":["npx"]}}'
  related-skills: '{"skill-finder":"User-initiated catalog search and first-time install discovery.","skill-update":"Safe single-skill upgrade with preview, backup, and rollback.","skill-audit":"Security and supply-chain scan before install or after updates.","skill-test":"Isolated trial before a candidate graduates to tracked install."}'
---

## State location

Skill-manager inventory may live under `<workspace>/skill-manager/`,
`<workspace>/memory/skill-manager/`, or `~/skill-manager/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/skill-manager/`, `<workspace>/memory/skill-manager/`,
   `~/skill-manager/`.
3. If none exists and durable state must be created, default to
   `<workspace>/skill-manager/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell
   cwd. An existing `~/skill-manager/` may be read; otherwise ask before
   creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

**Legacy paths.** Historical notes may exist under
`~/Clawic/data/skill-manager/` or `~/clawic/skill-manager/`. They are **not**
in the active lookup order and must **not** be moved, merged, or deleted during
ordinary sessions. Migration is a separate user decision.

## When to load

Load for **lifecycle** work on skills the agent already knows about or can
suggest from the **current** task:

- contextual suggestion tied to tools/domains in the active request
- inventory list, install/update consent flow, unused-skill cleanup
- declined-skill memory so the same offer is not repeated

Do **not** load as the primary skill for catalog search (`skill-finder`),
safe upgrade with backup/rollback (`skill-update`), security scanning
(`skill-audit`), authoring (`skill-builder`), or registry publish
(`skill-publish`).

## Routing

Load supporting resources only on demand:

| Need | Load |
|------|------|
| Whether/how to suggest from current context | `references/suggestions.md` |
| Install, update, remove, periodic audit commands | `references/lifecycle.md` |
| Inventory file format and first-use init | `references/memory-storage.md` |

## Security

Lifecycle actions use `npx clawic`, which downloads and executes catalog code
into detected agent skill directories. Before any install or update:

1. Name the slug and intended agent targets.
2. Prefer a quick look via `npx clawic show <slug>` when the user wants details.
3. Proceed only after explicit user consent for that action.
4. Keep all inventory reads/writes inside `<state_root>/`.

## Core loop

1. Resolve `<state_root>` and read `<state_root>/inventory.md` when it exists.
2. For suggestion opportunities, follow `references/suggestions.md` (current
   context only; honor Declined).
3. For install/update/remove/audit, follow `references/lifecycle.md` and update
   inventory after successful consented actions.
4. Never install, update, or remove without explicit user confirmation for that
   slug (or an explicit bulk update confirmation for `update --all`).
