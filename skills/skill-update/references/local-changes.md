# Local Changes — Updating a Hand-Edited Skill

Users edit installed skills: a tweaked rule, a deleted section, an added
preference. A straight update overwrites all of it with no error. Detect first,
decide second, merge third.

## Detecting local edits

Diff the installed copy against its published original — the version the user
installed, not the latest:

```bash
# Fetch the ORIGINAL of the installed version for comparison
npx clawic install <slug> --dir /tmp/original-<slug>
diff -r <installed-skills-path>/<slug> /tmp/original-<slug>
```

If the registry only serves latest, the previous update's backup under
`<state_root>/backups/` is the reference copy. No backup and no original
available → assume edits exist and show the three-way plan before applying
anything.

Empty diff → clean install, proceed with the normal Update Flow. Any hunk →
stop and classify.

## Classifying each local edit

| Edit found | Meaning | Default handling |
|---|---|---|
| Changed wording of an instruction | User re-tuned behavior deliberately | Preserve — re-apply onto the new version |
| Deleted section or file | User suppressed unwanted behavior | Preserve the deletion unless upstream rewrote that section for the same reason |
| Added section, rule, or file | User extended the skill | Preserve — carry the addition over |
| Changed frontmatter description | User re-tuned triggers | Preserve; upstream description changes need explicit user choice |
| Edits inside a section the update also rewrites | True conflict | Show both versions side by side; user picks — never auto-merge |
| Whitespace/formatting only | Editor artifact | Ignore; take upstream |

## The three-way merge

Three states: **original** (published version installed) · **local** (installed
with edits) · **upstream** (new published version).

1. Compute `original → local` (user edits) and `original → upstream` (publisher).
2. Edits and changes touching different sections: apply both — update first,
   re-apply local edits on top.
3. Both touch the same section: conflict. Present both versions with one line on
   what each does; the user decides per conflict, not in bulk.
4. Record what was carried over in the update report — list surviving edits by
   name.

## After the merge

- Verify with a task that exercises the user's edited behavior specifically —
  the generic verify run tests upstream behavior, not the customization.
- Persist the edit list to `<state_root>/local-edits-<slug>.md` (one line per
  edit: file, section, one-line intent). Next update starts from this list.
- Suggest once: recurring edits that survive multiple updates are config, not
  forks — if the skill has a Configuration table, moving the preference into
  that skill's own state config ends the merge burden permanently. User declines
  → keep merging, do not re-raise.

## Traps specific to local edits

- Diffing local against **latest** instead of the installed original conflates
  user edits with publisher changes.
- "Take upstream for everything, it's newer" silently deletes the user's work.
- Re-applying a local edit whose target section no longer exists: park it in the
  edit list as orphaned and tell the user; do not graft it somewhere similar.
