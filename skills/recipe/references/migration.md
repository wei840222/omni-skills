# Migration — recipe

Import/export between apps or backups:

- Map fields explicitly (title, yield, ingredients, steps, source, tags).
- Prefer open formats (Markdown, JSON-LD Recipe) over proprietary lock-in.
- Dedup on merge using title+source or content hash; never clobber without a note.
- Strip credentials from app exports before writing under `<state_root>/`.
