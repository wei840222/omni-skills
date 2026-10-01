# Setup — SEO

Read this on first use to load user preferences. Use stated preferences; do not open with a questionnaire.

## Your Attitude

SEO is full of folklore and of work that cannot be measured. Be the practitioner who names the mechanism, sizes the prize before doing the work, and states timing as a range tied to a mechanism. Concrete recommendations against named URLs; no scores invented to look rigorous.

## How To Load Preferences

1. Read `<state_root>/config.yaml` if it exists. Apply its values.
2. For anything absent, use the defaults in the Configuration table of `references/core-processes.md`.
   - `site_type: auto`, `target_market: en-US`, `tool_access: gsc-only`, `risk_posture: conservative`, `cms: auto`, `voice_file: none`, `min_impressions: 100`.
3. Read `<state_root>/memory.md` for prior context: site profiles, past audits, the tracked keyword basket, what has already been tried. Absence is fine; proceed without comment.
4. Universal preferences (locale, units, timezone) fall back to host profile files when this skill's own config does not set them.

Work from defaults immediately. Begin from the user's stated goal and available evidence.

## Recording Preferences (only when the user declares one)

Write to config or memory **only** when the user states a preference in the course of the work.

- User names their platform, market, tooling, or type of site → update the matching key in `<state_root>/config.yaml`.
- User expresses a stance (report depth, who ships the change, how aggressive to be with link tactics or generated pages, which KPI leads) → record it under the relevant preference area in `<state_root>/memory.md`.
- User corrects earlier guidance → update the stored value so it is not repeated.

If the user has said nothing, store nothing.

## Workspace

Persistent files live under `<state_root>/`:

```
<state_root>/
├── config.yaml      # declared preferences (Configuration table)
├── memory.md        # observed context: site profiles, audit history, keyword basket
├── audits/          # audit reports, one file per site and date
└── content/         # drafts and briefs
```

Create the subdirectories the first time something needs saving, not before. `assets/memory-template.md` holds the file format for each of them.

## What Memory Holds

Site profiles (domain, type, platform, market), the tracked keyword basket with dates, what was audited and what was fixed, which recommendations the user rejected and why, and the shipping constraints of their team. Only what the work actually reveals.
