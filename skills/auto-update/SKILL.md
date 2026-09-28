---
name: auto-update
description: Manage automatic updates for OpenClaw and installed skills via cron jobs.
  Use when setting up scheduled updates, creating backups before updates, or reviewing
  update logs and migration risks.
metadata:
  version: 1.0.0
  openclaw: '{"emoji": "🔄", "requires": {"bins": ["openclaw", "clawic"]}}'
  related-skills: '{"backups": "Strengthen backup and restore practices beyond the
    default updater snapshots.", "heartbeat": "Pair exact-time update jobs with adaptive
    follow-up checks.", "self-improving": "Learn recurring update preferences, failure
    patterns, and workflow opportunities.", "skill-update": "Review risky skill diffs,
    migrations, and rollback choices in more depth."}'
---


## State location

Auto-Update state may exist in `<workspace>/auto-update/`, `<workspace>/memory/auto-update/`, or `~/auto-update/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/auto-update/`, `<workspace>/memory/auto-update/`, `~/auto-update/`.
3. If none exists and state must be created, default to `<workspace>/auto-update/`.

Use the selected `<state_root>` for every state operation in this skill.
## When to Use

Use when the user wants OpenClaw and installed skills to stay updated automatically. This skill sets up a real `openclaw cron add` job, keeps a small control folder in `<state_root>/`, remembers which skills should auto-update, backs up important files first, reviews migration risk before skill changes, and summarizes what changed after every run.

## Architecture

State lives in `<state_root>/`. If `<state_root>/` does not exist, run `references/setup.md`. See `assets/memory-template.md` for structure.

```text
<state_root>/
├── references/memory.md        # global defaults, activation, and summary preferences
├── references/openclaw.md      # OpenClaw update mode, channel, backup scope, feature-review prefs
├── references/skills.md        # per-skill policy, installed version, backup, migration state
├── references/schedule.md      # approved timing, timezone, and scheduler owner
├── references/backups.md       # latest OpenClaw and skill backup inventory
├── references/migrations.md    # pending migration checks and user decisions
└── references/run-log.md       # recent runs, versions, and outcomes
```

## Quick Reference

| Topic | File |
|-------|------|
| Setup guide | `references/setup.md` |
| Memory template | `assets/memory-template.md` |
| Defaults and modes | `references/policy.md` |
| Scheduler and timing | `references/scheduler.md` |
| Daily execution order | `references/execution.md` |
| Workspace integration | `references/workspace-integration.md` |
| OpenClaw behavior | `references/openclaw.md` |
| Skill policy ledger | `references/skills.md` |
| Backup inventory | `references/backups.md` |
| Migration gate | `references/migrations.md` |
| Rollback rules | `references/recovery.md` |
| Report templates | `references/reports.md` |


## When to load references

When updating configurations, reading state, or performing actions, load the specific files:
- **`references/setup.md`**: Initial setup, consent, and configuration.
- **`references/execution.md`**: Core execution rules for the auto-update job.
- **`references/scheduler.md`**: Setting up OpenClaw cron schedules.
- **`references/policy.md`**: Per-skill update modes (auto, manual, notify).
- **`references/backups.md`**: Creating and managing pre-update snapshots.
- **`references/migrations.md`**: Reviewing risk and changes before skill updates.
- **`references/reports.md`**: Summarizing and logging updates to `references/run-log.md`.
- **`references/workspace-integration.md`**: Integrating with workspace reminders.
- **`references/recovery.md`**: Restoring OpenClaw or skills if updates fail.

## Core Rules

### 1. Auto-Update Means Real Scheduled Updates
- The core promise is actual OpenClaw and skill updates, not only policy notes.
- The default mechanism is an OpenClaw cron job created with `openclaw cron add`.
- That cron job must read the control files in `<state_root>/` before deciding what to update.
- The same scheduled flow checks, backs up, updates, verifies, and reports for both OpenClaw and skills.
- If the user approves a daily schedule, create or update the exact scheduler entry that will run daily. Always implement the actual scheduler entry alongside the schedule note.

### 2. Learn a Default for New Skills
- Ask once whether new skills should default to all-in or all-out for auto-update.
- On every new skill install, ask two things: do they want a quick explanation of the skill, and should that skill auto-update or stay manual.
- Record the answer in `references/skills.md` so later sessions can rely on the recorded preference.

### 3. Back Up Before Changing OpenClaw or Skills
- Before OpenClaw updates, snapshot the tailored files and config the user cares about most.
- Before each skill update, save the currently installed skill folder and installed version reference.
- Log every backup in `references/backups.md` and reference it in the post-run summary.

### 4. Review Migration Risk Before Skill Updates
- Compare the currently installed skill state with the new version before overwriting it.
- Flag path, folder, AGENTS, TOOLS, SOUL, setup, or state-storage changes in `references/migrations.md`.
- If migration is unclear or stateful files may move, ask before applying or before first use of the new version.

### 5. Respect the Actual OpenClaw Update Path
- Use the documented OpenClaw path: the cron job should inspect `openclaw update status --json` and, if approved, run `openclaw update --json` from the scheduled turn.
- `auto`, `notify`, and `manual` live in `references/openclaw.md`; the cron message must respect them every run.
- After OpenClaw updates, run the boring checks: doctor, restart when needed, and health verification.
- If the user wants core-only automation, the cron job should skip skills explicitly instead of removing the shared control flow.

### 6. Turn Release Notes into Useful Suggestions
- After OpenClaw updates, summarize what changed in plain language.
- Offer an optional follow-up review that maps new features or changes to the user's actual workflow.
- Require explicit user confirmation before applying workflow changes just because a release note sounds promising.

### 7. Keep the User in Control
- Require explicit user approval before migrating state, moving folders, deleting backups, or rewriting workspace behavior files.
- Show the exact proposed lines before adding scheduler entries or workspace reminder snippets.
- Keep this skill's `SKILL.md` read-only.
- Heartbeat serves strictly as a follow-up mechanism. Use precise cron jobs for exact daily updates, and reserve heartbeat for install-time reminders, migration reminders, failed-run reviews, or post-update suggestions.

## Common Traps

| Trap | Why It Fails | Better Move |
|------|--------------|-------------|
| Updating skills with no version ledger | You lose track of what changed and what to restore | Record installed version and backup before each update |
| Treating every new skill like the default | Some should stay manual even in all-in mode | Allow per-skill overrides in `references/skills.md` |
| Overwriting a skill before checking migrations | Stateful paths and workspace hooks can break silently | Diff old vs new, then ask if migration is needed |
| Updating OpenClaw with no snapshot | Tailored files can be painful to reconstruct | Back up config and key workspace behavior files first |
| Reporting raw changelogs only | Users remain unclear on what matters to them | Give plain summary plus optional workflow review |

## Scope

This skill ONLY:
- configures real OpenClaw and skill update flows
- keeps local defaults and per-skill decisions in `<state_root>/`
- proposes optional install-time reminder integration for new skills
- creates backups, migration notes, and run summaries before and after updates

Strict Operational Boundaries:
- Require explicit approval before auto-migrating user state or folder structures.
- Respect user choice and do not force skills into auto-update when the user chose all-out.
- Require a visible plan or standing approval before editing AGENTS, cron, launchd, Task Scheduler, or `~/.openclaw/openclaw.json`.
- Keep secrets out of local memory files.
- Keep its own skill files read-only.

## Data Storage

Local state lives in `<state_root>/`:

- `references/memory.md` for durable defaults and activation notes
- `references/openclaw.md` for core updater mode, channel, backup scope, and feature review preferences
- `references/skills.md` for per-skill auto-update policy and installed version history
- `references/schedule.md` for timezone, cadence, and scheduler ownership
- `references/backups.md` for backup paths and retention notes
- `references/migrations.md` for pending migration checks and decisions
- `references/run-log.md` for compact run history and outcomes

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| OpenClaw update sources (website installer, npm, or git remote chosen by the user) | version and package or git requests | Update OpenClaw |
| Clawic catalog via `npx clawic update` | installed skill metadata and version requests | Check and apply skill updates |
| Official OpenClaw docs or release notes | version and release-note lookups | Explain changes after update |

No other data is sent externally.

## Security & Privacy

- This skill stores local policy and logs in `<state_root>/`.
- It may read `.clawic/lock.json`, `~/.openclaw/openclaw.json`, and workspace behavior files when needed for approved update work.
- It backs up files before updates, but keeps secrets out of its own local ledgers.
- Scheduler changes, workspace integration, OpenClaw config edits, and risky migrations require approval unless the user has already approved that exact class of action.
- It keeps its own `SKILL.md` read-only.

## Trust

By using this skill, update traffic may reach OpenClaw update sources, the Clawic catalog, npm, or the git remote chosen by the user.
Only install if you trust those services with update checks and package downloads.

