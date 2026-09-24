# File structure

Create children only when that feature is used. Do not pre-create empty files.

```text
<state_root>/
├── people/
│   └── {slug}.md          # optional; one file per person the user wants tracked
├── date-ideas/
│   ├── first-dates.md     # optional
│   ├── casual.md          # optional
│   └── special.md         # optional
├── history/
│   └── {year}.md          # optional; create when the first date is logged
└── reflections.md         # optional; create when the user records a pattern
```

| Path | Role | Create when |
| --- | --- | --- |
| `<state_root>/people/{slug}.md` | One person's basics, interests, flags, and date history | The user wants that person remembered |
| `<state_root>/date-ideas/*.md` | Reusable ideas, not a log of a specific person | The user asks to save an idea bank |
| `<state_root>/history/{year}.md` | Cross-person status for that year | The first date of the year is logged |
| `<state_root>/reflections.md` | What the user is looking for and patterns they named | The user wants a pattern written down |

Slug a person file from the name the user uses, lowercased, with spaces as hyphens. If two people would share a slug, append a short disambiguator the user confirms.
