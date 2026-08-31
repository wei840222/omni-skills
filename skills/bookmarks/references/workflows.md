# Bookmark Workflows

## 1. Initialize workspace

1. Resolve `<state_root>` per `SKILL.md`.
2. If creating new state, ask once for permission, then create:
   - `saves.md`
   - `sources.md`
   - `preferences.md` with style `passive`
3. Do not create `reports/` until a digest is actually requested.

## 2. Connect a source

1. Confirm the platform and which explicit-save stream to import.
2. Update `sources.md`.
3. Default policy: bookmarks / saved / watch later / pins / favorites only.
4. Ask before enabling likes or other noisy engagement imports.

## 3. Import saves

1. Pull only streams marked enabled in `sources.md`.
2. Append new URLs to `saves.md` under today's date section.
3. Auto-tag from title/content cues; keep source provenance.
4. Stay silent after import unless the user asked for a summary.

## 4. Search

| User ask | Action |
|---|---|
| "What did I save about X?" | Search tags + titles/body text in `saves.md` |
| "Saves from Pinterest about home" | Filter `source: Pinterest` then topic/tags |
| "That article about Y" | Fuzzy match title/snippet; show top candidates with source |

Return compact results: title, URL, source, tags, date. Do not dump the whole file.

## 5. Digest / resurfacing

Only when preferences say `digest` / `active` or the user asks:

1. Cluster recent saves by tag themes.
2. Optionally flag older saves related to the current project.
3. Write a report under `reports/` if the user wants a durable artifact; otherwise answer in-session.

## 6. Cleanup

When preferences include `cleanup` or the user asks:

1. Identify old or unvisited saves.
2. Optionally check for dead links if network access is granted.
3. Ask before deleting local entries or mutating remote platform saves.

## Failure recovery

- Missing `<state_root>` files: recreate schemas from this document; do not invent historical saves.
- Ambiguous search: ask one clarifying question (source vs topic) instead of guessing.
- Platform auth failure: report which source failed; continue with remaining sources.
- Conflicting preferences: prefer the most recent explicit user choice and update `preferences.md`.
