# Skill lifecycle actions

Installation, updates, removal, and periodic audit. Always resolve
`<state_root>` first (see `SKILL.md`) and keep inventory at
`<state_root>/inventory.md`.

## Tooling (verified)

Primary CLI is **Clawic** via `npx clawic` (catalog discovery/install into
detected agents). Confirmed command surface:

| Action | Command |
|--------|---------|
| Search catalog | `npx clawic search "<query>"` |
| List catalog | `npx clawic list` |
| Show one skill | `npx clawic show <slug>` |
| Install into every detected agent | `npx clawic add <slug>` |
| Install into one directory | `npx clawic install <slug>` |
| Update one or many | `npx clawic update [slugs...]` / `npx clawic update --all` |
| Active registry URL | `npx clawic registry` |

There is **no** uninstall subcommand. Removal is a manual folder delete from
each agent skills directory where the package was installed (for example
`.claude/skills/<slug>/`, `.codex/skills/<slug>/`, OpenClaw/Cursor skill
roots the host actually uses). Confirm paths with the user before deleting.

Do **not** substitute `agentskills` / `uvx --from skills-ref agentskills` for
install or update. That package is the Agent Skills **validator/reference**
(`validate`, `read-properties`, `to-prompt`), not a catalog installer.

## Installation

When the user consents to install a specific slug:

```bash
npx clawic add <slug>
```

On success, append or update inventory:

```markdown
## Installed
- slug@1.0.0 — "purpose in user words" — YYYY-MM-DD
```

Use `npx clawic show <slug>` when version/purpose are not already known.

## Checking updates

```bash
npx clawic show <slug>
```

Compare published version with the inventory row. If newer:

> `<slug>` has an update (`vX` → `vY`). Update now?

For multi-skill drift during audit, prefer one bulk confirmation over N
one-by-one prompts when the user wants everything current.

## Updating

Single skill after consent:

```bash
npx clawic update <slug>
```

Bulk after explicit bulk consent:

```bash
npx clawic update --all
```

Then refresh versions in `<state_root>/inventory.md`.

When the user needs preview, backup, local-edit collision handling, or
rollback, hand off to `skill-update` instead of a bare update.

## Removal

1. Confirm the slug and that removal is intentional.
2. Delete the skill folder from each detected install location the user
   authorizes (Clawic has no uninstall command yet).
3. Remove the row from `## Installed` in inventory.
4. Optionally offer to record a Declined reason if they never want it
   re-suggested.

## Periodic audit

Triggers: "what skills do I have?", "cleanup skills", "prune unused skills".

1. Read `<state_root>/inventory.md` (and say if missing).
2. For each Installed row, ask whether they still use it for the recorded
   purpose.
3. On "no", offer removal and only delete after confirmation.
4. On "yes", keep the row unchanged.
5. Offer update checks for rows that look stale only when useful.

## Rules

- Consent is per mutating action (install, update one, update all, remove).
- Track purpose so audits stay meaningful.
- Keep inventory current after successful mutations.
- Scope file reads/writes for this skill to `<state_root>/` plus the skill
  package itself when inspecting local skill trees the user pointed at.
- Suggest and manage from **current task context**; do not count repetition
  or infer struggle from long-run behavior patterns.
