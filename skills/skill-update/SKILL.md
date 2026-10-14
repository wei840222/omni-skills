---
name: skill-update
description: >
  Safely update installed agent skills: version check, diff preview, backup,
  explicit approval, data migration, and rollback. Use when upgrading a skill,
  checking for a newer version, previewing what changed before apply, recovering
  after a bad update, migrating saved data across a version bump, preserving
  local edits that would collide with upstream, or bringing every install or
  every agent's copy current. Prefer skill-finder for first-time install
  discovery, skill-publish for owner-side release, and skill-manager for broader
  inventory/remove/cleanup beyond one upgrade.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🔄","displayName":"Skill Update","requires":{"bins":["npx"]}}'
  related-skills: '{"skill-finder":"Find and install skills you do not have yet.","skill-publish":"Owner-side sanitize, version, and publish a skill you own.","skill-manager":"Broader install/remove/list lifecycle and unused-skill cleanup beyond one upgrade."}'
---

## State location

Skill-update backups, update log, config, and local-edit lists may live under
`<workspace>/skill-update/`, `<workspace>/memory/skill-update/`, or
`~/skill-update/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when the user or host provides one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/skill-update/`, `<workspace>/memory/skill-update/`,
   `~/skill-update/`.
3. If none exists and durable state must be created, default to
   `<workspace>/skill-update/` only with user consent.
4. When more than one candidate exists, use only the highest-precedence path,
   report the conflict, and leave other copies unchanged.
5. If the host cannot supply `<workspace>`, do not invent it from the shell
   cwd. An existing `~/skill-update/` may be read; otherwise ask before
   creating data.
6. Once selected, keep the same `<state_root>` for the whole invocation.

Use the selected `<state_root>` for every state operation in this skill.
Outside this section, every skill-state path uses `<state_root>/...`.

**Target skill data.** When the skill being updated declares its own data
folder, treat that skill's resolved state root as a separate path (commonly
documented as `<state_root>/<updated-slug>/` in migration notes). Do not write
the literal string `<state_root>` to disk; pass the resolved filesystem path.

**Legacy paths.** Historical notes may exist under
`~/Clawic/data/skill-update/`, `~/clawic/skill-update/`, or similar Clawic-era
folders. They are **not** in the active lookup order and must **not** be moved,
merged, or deleted during ordinary sessions. Migration is a separate user
decision with copy → verify → cutover → rollback.

## When to use

- User asks to update, upgrade, or version-check an installed skill.
- A skill misbehaves, stops triggering, or loses data right after an update.
- A major bump is pending: preview breaking changes and migrate saved data.
- The installed copy was hand-edited, so a straight update would overwrite it.
- Bringing everything current: `update --all`, or the same skill across agents.
- User mentions a skill that has a newer published version — flag it once.

Do **not** use as the primary skill for first-time catalog discovery
(`skill-finder`), owner-side publish (`skill-publish`), or broad inventory /
remove / unused cleanup (`skill-manager`).

## Routing

Load supporting resources only on demand:

| Need | Load |
|------|------|
| Diff procedure, impact classes, security screen | `references/preview.md` |
| Data migration patterns and failure handling | `references/migrate.md` |
| Post-update breakage diagnosis and restore | `references/rollback.md` |
| Detecting and preserving hand edits | `references/local-changes.md` |
| Multi-skill batch and mid-batch failure | `references/batch.md` |
| Version skew across agent installs | `references/multi-agent.md` |

## Why updates break things

| Failure mode | Preview check |
|---|---|
| Renamed/moved files | Orphaned user data and references |
| Removed or rewritten instruction sections | Agent silently stops a relied-on behavior |
| New setup requirements (binary, env, account) | Skill half-works until configured |
| Changed data formats | Previously saved state unreadable |
| Overwritten local edits | Customizations vanish with no error |

## Quick reference

| Situation | Play |
|---|---|
| Single skill, patch or minor | Diff, classified summary, apply on explicit yes |
| Major pending | Full preview + migration check → `references/preview.md`; propose, then apply only after a later approval |
| Broke right after update | Symptom→cause + restore → `references/rollback.md` |
| Hand-edited install | Detect and merge first → `references/local-changes.md` |
| Same skill in several agents | Inventory every copy → `references/multi-agent.md` |
| "Update everything" | Patches/minors batched, majors one by one → `references/batch.md` |
| Data format changed | Read real data, map, apply on approval → `references/migrate.md` |
| Suspicious diff (new network, broader file access) | Security screen → `references/preview.md`; report, do not apply |
| No version history / unclear delta | Treat as major |

## Catalog commands

Primary CLI is **Clawic** via `npx clawic` (catalog list/show/update into
detected agent skill directories). Confirm the slug and intended targets before
any mutating call.

```bash
npx clawic list              # installed skills + versions
npx clawic show <slug>       # latest published version
npx clawic update <slug>     # update one skill after explicit yes
npx clawic update --all      # only when no pending major needs solo preview
```

### Version delta stance (semver claim, not a guarantee)

| Delta | Assume | Action |
|---|---|---|
| Patch (1.2.3 → 1.2.4) | Fixes only | Quick diff, apply on approval |
| Minor (1.2 → 1.3) | Additions | Diff; review modified sections, not only adds |
| Major (1.x → 2.0) | Breaking | Full preview + migration; never propose-and-apply in one turn |
| User mid-project on this skill | Risky timing | Mention once, defer until that work ships |
| Unclear / no history | Unknown risk | Treat as major |

## Core rules

1. A skill is behavior-as-text: every text diff is a behavior diff. Apply only
   after the user has seen and approved it.
2. Order is load-bearing: check → detect local edits → preview → explain →
   confirm → backup → update → verify.
3. Explicit "yes" only for **this** skill in **this** session. Silence, "hmm",
   or a topic change is not consent. Approval for skill A is never approval for
   `update --all`.
4. Diff even patch bumps. Semver is the publisher's claim; a "patch" that
   rewrites instructions is still a behavior change.
5. Verify with one real task against the updated skill, not a file listing.
6. Back up before any update. Retention: keep ≥`backup_retention_days` **and**
   until the user confirms the new version works — whichever is later.
7. A migration that fails mid-way stops, reports, and restores completely.
8. Any breaking-change signal leads the summary and needs explicit approval.
9. The diff is ground truth; the changelog sets expectations and never replaces
   the diff.

## Update flow

1. **Check** — installed vs published; inventory every install location
   (`references/multi-agent.md` if more than one).
2. **Detect local edits** — installed copy vs its published original; edits
   found → `references/local-changes.md` first.
3. **Preview** — full diff, impact classes, security screen
   (`references/preview.md`).
4. **Explain** — breaking changes first, in the user's workflow terms.
5. **Confirm** — explicit yes (Core rule 3).
6. **Backup** — copy current state before touching anything.
7. **Update** — apply the new version to every inventoried copy.
8. **Verify** — run one real task with the updated skill.

## Preview before update

Always show impact before applying. For each changed file answer: what changed,
whether the user's workflow touches it, and whether migration is needed.
Procedure and security screen: `references/preview.md`.

Breaking-change signals (any one leads the summary and needs explicit approval):

- File or folder renamed, moved, or deleted.
- Instruction section removed or rewritten.
- New required setup step.
- Format change in anything the skill saves.
- Local edits the update would overwrite.

Present breaking items first:

> Skill X has v2.0.0 available.
>
> **Breaking:** Config now in `config.md` (was in SKILL.md)
> **Added:** New `templates/` folder
> **Removed:** Old `legacy.md`
>
> **Migration needed:** Saved preferences must move. I can migrate. Proceed?

Each skill with a pending major gets its own preview.

## Applying the update

```bash
npx clawic update <slug>
npx clawic update --all
```

`update` is the consumer-side pull of what the owner already published.
Publishing a new version is a different act (`skill-publish`). Use `--all` only
when the user asked for all **and** no pending update is a major (majors go one
by one; sequencing → `references/batch.md`).

**Proactive notification:** when the user mentions a skill that has a newer
version, say so once (unless `proactive_notify` is off or the skill is in
`pinned_skills`). Do not re-raise it in the same session.

## Backup and update log

Before any update:

1. Copy the current skill folder to
   `<state_root>/backups/<slug>-<version>-<timestamp>/`.
2. If the skill being updated declares a data folder, back that up under the
   same timestamped folder — the update itself never touches it, but a migration
   might.
3. State the backup path in your response (resolved filesystem path).
4. Append one line to `<state_root>/update-log.md`: date · slug · old→new ·
   backup path · agents updated.
5. If the update fails → offer restore immediately.

## Handling migrations

When a data format changes:

1. Read the user's actual current data first.
2. Explain what moves and what defaults get added.
3. Execute only with approval.
4. Verify migrated data works.

Patterns and failure handling: `references/migrate.md`.

## Rollback

Restore = copy the backup folder back over the installed skill — and its data
folder from the same timestamp if a migration ran. Offer it unprompted when the
user reports misbehavior after an update:

```text
Something's not working? I have a backup from before the update.
Want me to restore skill X to v1.2.3?
```

Diagnosis when the cause is unclear: `references/rollback.md`.

## Output gates

Before applying any update, verify:

- Explicit yes for **this** skill, this session?
- Diff actually read (not only changelog or version number)?
- Local edits checked (installed vs published original)?
- Backup of the skill folder **and** its data folder exists, path stated?
- Every install location inventoried?

Before reporting success: one real task run against the updated skill?

## Configuration

User-dependent variables. Defaults apply until the user states a preference;
store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| backup_retention_days | number (days, ≥1) | 7 | Floor for deleting backups (Core rule 6); "until user confirms" still applies |
| proactive_notify | bool | true | Flag a newer version once when the user mentions an installed skill |
| pinned_skills | list (slugs) | none | Excluded from proactive flags and `update --all`; update only when named |
| preview_detail | summary \| full-diff | summary | Classified summary vs raw diff inline |

Preference areas (record in config.yaml when stated):

- **Tooling** — project vs global installs, which agents (Check + multi-agent)
- **Safety posture** — major sequencing and confirmation ceremony (never below
  explicit-yes)
- **Cadence** — version sweeps on request vs session start
- **Conventions** — terse vs annotated previews and batch reports

## Traps

| Trap | Why it fails | Do instead |
|---|---|---|
| Trusting a patch bump | Text skills change behavior on any edit | Diff every update |
| Verifying by file listing | Files present ≠ skill works | Run one real task |
| `update --all` after one yes | Consent covered one skill | Per-skill preview for every pending major |
| Deleting backup right after update | Breakage shows on next use | Hold ≥ retention and until confirm |
| Flagging moved text as removed | Diff shows delete + add | Search new version before calling it breaking |
| Overwriting a hand-edited install | Customizations vanish silently | Detect local edits first |
| Restoring skill but not data | Migrated data + old skill = both broken | Restore skill and data from same timestamp |
| Updating only the first copy | Other agents keep loading stale | Inventory all installs first |
| Reading changelog as the diff | Publisher summary, not ground truth | Changelog for expectations; diff decides |

## Where experts disagree

- **Update promptly vs pin and batch.** Prompt updates minimize drift from
  published fixes; pinning batches review cost into scheduled sweeps. Skills
  inside daily load-bearing workflows get pinned (`pinned_skills`) and reviewed
  deliberately; peripheral skills update as bumps appear.
