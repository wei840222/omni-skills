# Migration Playbook — Help Center

Use when moving from spreadsheets, legacy docs, a static site, or another provider. Thresholds marked **project policy** are adjustable defaults—record changes in `<state_root>/memory.md`.

## Phase 1: Discovery

1. Export current articles, categories, attachments, and redirects.
2. Build an inventory with status: keep, merge, rewrite, archive.
3. Capture top ticket intents from a recent window (default **last 90 days**, project policy).
4. Note compliance or legal retention requirements before deleting source content.
5. Store the inventory in `<state_root>/content-inventory.md` after consent.

## Phase 2: Mapping

1. Define target taxonomy and URL conventions before bulk import.
2. Map source categories and tags to the target structure.
3. Draft a redirect table from every public old URL to a new URL or deliberate gone page.
4. Assign an article owner per category.

## Phase 3: Dry run

1. Import a representative sample into staging (not production).
2. Validate formatting, links, search quality, permissions, and locales.
3. Test escalation from article failure or “still need help” into the ticket queue with expected tags.
4. Run acceptance with support and product owners; fix blockers before cutover.

## Phase 4: Launch

1. Freeze source edits for a named cutover window.
2. Import final content and apply redirect rules.
3. Monitor errors, search misses, and ticket spikes for the first **48 hours** (project policy).
4. Keep the rollback path ready until stability criteria pass.

## Post-launch checks (project policy defaults)

- Redirect hit success on sampled legacy URLs at or above **95%**
- No critical broken links on top intents
- Search miss rate trending down week over week
- Agents trained on the new taxonomy and tagging

If any check fails, pause further redirects, restore the rehearsed rollback or prior surface as designed, and file the incident in `<state_root>/rollout-log.md`.
