# Migration Strategies

How to move user data and state across a skill update without losing anything.

## Ground rules

- **Read before mapping.** Open the user's actual data first; never migrate from
  the format you assume the old version produced.
- **Copy, verify, then delete — never move.** A move that fails mid-way strands
  data; a copy that fails leaves the original intact.
- **Every step re-runnable.** If step 3 of 5 fails, re-running steps 1–2 must be
  harmless (write-if-different, create-if-missing).
- **Value translation is a decision, not a default.** Renaming a field is
  mechanical; changing a value's meaning or units is semantic — show the mapping
  and get approval before applying it.

## What needs migration

Skills may store:

- **Preferences** — user settings in SKILL.md sections or config files
- **State files** — saved data in the skill folder or the skill's data folder
  under its resolved state root
- **External references** — paths, URLs, configuration pointing into the skill
- **Learned patterns** — auto-adaptive skills with accumulated knowledge
  (highest loss cost: irreplaceable, not re-enterable)

## Migration patterns

### Pattern 1: File rename

Old: `config.md` → New: `settings.md`

1. Read content from old file
2. Show user the content: "these preferences will move"
3. Write to new location
4. Verify new content matches old (byte compare)
5. Keep old file until post-migration verification passes, then remove

### Pattern 2: Structure change

Old format:

```text
## Preferences
- theme: dark
- lang: es
```

New format:

```text
## User Settings
theme: dark
language: es
notifications: true  # new field
```

1. Parse old format — flag any line that does not parse instead of dropping it
2. Map fields to new names; list the mapping explicitly
3. Add defaults for new fields, labeled as defaults
4. Show user: "these settings migrate as-is, these are new defaults"
5. Apply with confirmation

### Pattern 3: Folder reorganization

Old: `skill/data/` → New: `skill/storage/data/`

1. List all files in old location — count them
2. Create new folder structure
3. Copy files preserving names
4. Verify file count and sizes match at destination
5. Update any internal references to old paths
6. Remove old files, then empty old folders

### Pattern 4: Data folder location move

Old: `~/<slug>/`, `~/clawic/<slug>/`, or `~/Clawic/data/<slug>/` → New: the
updated skill's resolved state root (workspace-first candidates for that skill).

1. Check all old candidate locations; a user may have data in more than one era
2. If the new location already has files, merge is a decision: show both sides;
   newest-wins is **not** the default
3. Copy to the new location, verify counts and sizes, then remove old folders
   only after user confirmation
4. Case matters: on case-insensitive filesystems `~/clawic/` and `~/Clawic/` may
   silently be the same folder — check before "merging" a folder with itself
5. Legacy Clawic-era paths are migration **sources** only; they are not active
   lookup roots after cutover

### Pattern 5: Auto-adaptive skill

Old learned preferences → new preference format

1. Export current preferences to a structured intermediate (JSON)
2. Map to new schema; anything unmappable stays in the export, never silently
   dropped
3. Import into new version
4. Run a task the old version personalized correctly; confirm same behavior
5. Keep the export alongside the backup — only recovery path for learned data

## Migration script template

```markdown
## Migrating skill-name v1 → v2

**What's moving:**
- Preferences from `old.md` → `new.md`
- Data folder from old root → resolved state root

**New defaults added:**
- `feature_x: enabled`
- `timeout: 30s`

**Steps:**
1. Backup current state ✓
2. Copy preferences [waiting approval]
3. Move data files [waiting approval]
4. Update references [waiting approval]
5. Verify [after migration]

**Proceed with migration?**
```

## Handling failures

If migration fails mid-way:

1. Stop immediately — do not improvise the remaining steps
2. Report exactly which steps succeeded and which failed
3. Offer to restore from
   `<state_root>/backups/<slug>-<version>-<timestamp>/`
4. Never leave a partial state: either roll fully back or fix and complete

## Verification

After migration:

1. All files exist in new locations; counts match the old ones
2. Content is readable and parses in the new format
3. Run one real task with the skill — the only check that catches semantic
   mapping errors
4. Ask the user to confirm everything works

Only delete backups after user confirmation (retention rule in SKILL.md).
