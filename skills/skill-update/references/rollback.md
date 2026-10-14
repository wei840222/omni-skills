# Rollback — When a Skill Breaks After an Update

Diagnose first when the cause is unclear; restore first when the user just wants
the old behavior back.

## Symptom → cause

Work top-down; each row is a check, not a guess.

| Symptom after update | Likely cause | Check |
|---|---|---|
| Skill stopped triggering at all | Description rewritten — trigger surface changed | Diff frontmatter `description` old vs new |
| Skill triggers but behaves differently | Instruction section rewritten or removed | Diff the section; search new version for old wording |
| Errors about missing binary, env var, or account | New setup requirement | New requirements vs machine; setup may be the fix, not rollback |
| Can't read saved data | Data format changed; migration skipped or wrong | Open data folder; compare shape to what new version expects (`migrate.md`) |
| Reads data but lost personalization | Migration dropped or mis-mapped learned values | Compare data folder against backup field by field |
| References inside the skill 404 | Files renamed or moved | List old vs new folder |
| Only one agent shows the problem | That agent has a different copy or version | `multi-agent.md` — inventory every install |
| Else | Unknown — treat as full breakage | Restore, then re-run the preview on the missed diff |

A setup-requirement failure is the one row where rolling back is usually wrong:
installing the requirement gets the user the new version they wanted.

## Restore procedure

1. Locate the backup:
   `<state_root>/backups/<slug>-<version>-<timestamp>/` — the update log
   (`<state_root>/update-log.md`) maps dates to versions and paths when several
   backups exist.
2. Confirm with the user which version to restore.
3. Copy the backed-up skill folder over the installed one — every install
   location, not just the first (`multi-agent.md`).
4. **If a migration ran during the update, restore the data folder from the same
   timestamp.** Old skill + migrated data is a second breakage, not a fix.
5. Verify: run the task that surfaced the problem. Still broken → the update was
   not the cause; put the new version back and keep diagnosing.
6. Log the rollback in `<state_root>/update-log.md` (date · slug · restored
   version · reason).

## After a successful rollback

- Add the skill to `pinned_skills` if the user wants it held; otherwise note the
  failing version so the next sweep does not re-propose it blind.
- Report upstream in the user's name only if the user agrees, using the registry
  channel they already use for that catalog (for example `npx clawic show
  <slug>` metadata or the publisher's documented feedback path).
- When a fixed release appears, preview it against the version that worked, not
  against the one that broke.

## No backup exists

The update predates this skill's involvement, or retention expired:

1. Reinstall the last known-good version if the registry serves it.
2. If only latest is served: reconstruct what broke from the diff between the
   two published versions and patch the local copy as a stopgap — flag it as a
   local edit (`local-changes.md`) so the next update does not silently erase it.
3. Data loss with no backup and no export is unrecoverable — say so plainly
   rather than improvising a partial reconstruction that looks whole.

## Rolling back a migration alone

Skill version is fine but the migrated data is wrong:

1. Restore only the data folder from the backup timestamp.
2. Re-run the migration with the mapping corrected (`migrate.md`, Handling
   failures).
3. Verify with a task that exercises the migrated values — file counts do not
   catch semantic mapping errors.
