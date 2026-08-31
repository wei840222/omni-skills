# Workspace Schemas

All paths below are relative to the resolved `<state_root>/`.

## `saves.md`

Append-only daily sections. Each bullet keeps title, URL, source, and tags.

```markdown
# saves.md
## YYYY-MM-DD
- [Title](https://example.com/path)
  source: X | tags: #topic #secondary
```

Rules:

- One bullet per save
- `source` is required (`X`, `YouTube`, `Reddit`, `Pinterest`, `Instagram`, `TikTok`, or `manual`)
- Tags use `#kebab-or-simple` tokens; keep 1–5 tags
- Do not invent titles; prefer the page title or user-provided label

## `sources.md`

Records connected platforms and import policy.

```markdown
# sources.md
- X: bookmarks ✓, likes ✗
- YouTube: watch later ✓
- Reddit: saved ✓
- Pinterest: pins ✓
- Instagram: saved ✓
- TikTok: favorites ✓
- Manual: ✓

Note: Default to explicit saves only.
Ask before importing likes (too noisy).
```

## `preferences.md`

Controls interruption style and report cadence.

```markdown
# preferences.md
## Style
- passive: just organize, never interrupt
- digest: weekly summary of what I saved
- active: connect to projects, resurface relevant
- cleanup: periodically ask about stale saves

## Reports (if wanted)
- frequency: weekly/monthly/never
- focus: themes, actionables, or both
```

Default style is `passive` until the user chooses otherwise.

## `reports/`

Create report files only when the user opted into digests or explicitly asked for a summary. Do not pre-create empty report directories beyond what the write requires.
