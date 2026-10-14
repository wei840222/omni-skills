# Multi-Agent Installs — One Skill, Many Copies

The same skill can be installed in several agents and at several scopes.
Updating "the skill" while another copy keeps loading stale is the most
confusing failure in this domain.

## Where copies live

Check every location before declaring an inventory complete:

| Scope | Locations |
|---|---|
| Project | `.claude/skills/`, `.codex/skills/`, `.gemini/skills/`, `.openclaw/skills/`, `.agents/skills/`, `.cursor/skills/` under the project root |
| Global | The same agent folders under `~` (for example `~/.claude/skills/`), plus `~/.hermes/` |

```bash
npx clawic list    # installed skills with locations and versions
```

A skill present at both project and global scope: the project copy wins inside
that project (standard agent resolution). Updating only the global copy changes
nothing in projects that shadow it — say so explicitly.

## Inventory before any update

1. List every copy of the slug: agent, scope, version.
2. Same version everywhere → treat as one skill; update all copies in the same
   operation, one backup per copy.
3. Versions differ → skew. Resolve skew **before** applying the new update;
   stacking an update onto skew produces three vintages.

## Diagnosing version skew

| Observation | Cause | Fix |
|---|---|---|
| One agent updated, others stale | Previous update ran against a single folder | Bring all copies to the target version in one pass |
| Project copy older than global | Project pinned an old version, or predates global | Ask which behavior this project wants — shadowing may be intentional |
| One copy hand-edited, others clean | User customized in one agent only | `local-changes.md` for that copy; ask whether edits should propagate |
| Same version, different behavior | Data folders differ, not the skill text | Compare what each agent actually loaded |

## Updating all copies

- One preview covers all copies (same diff), but the backup is per copy:
  `<state_root>/backups/<slug>-<version>-<timestamp>/` gains a subfolder per
  install location.
- Apply to every location in the inventory; re-list versions afterward — verify
  is "every copy reports the target version" **plus** one real task in the agent
  the user actually uses.
- Update log line records which agents were updated.

## Migrations with shared data

A target skill's data folder is typically one folder serving every agent's copy
of that skill. A data migration therefore runs **once** — after all copies are
on the new version, never between updating copy one and copy two. A migrated
data folder under a stale copy is the both-broken state (`rollback.md`, restore
rule 4).
