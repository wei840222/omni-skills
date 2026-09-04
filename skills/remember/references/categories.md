# Memory categories

Use one category per durable fact. Each entry includes its recorded date, source, and confidence. Keep sensitive data out unless the user explicitly asked to persist it.

## `commitments.md`

```markdown
# Commitments

## Active
- [ ] [2026-02-15] Deploy v2 to production | source:explicit | confidence:certain

## Completed
- [x] [2026-02-10] Fix authentication bug | source:explicit | confidence:certain
```

## `preferences.md`

```markdown
# Preferences

## Communication
- Concise responses | source:explicit | recorded:2026-01-15
- Spanish casual, English technical | source:inferred | recorded:2026-01-15
```

## `corrections.md`

```markdown
# Corrections

## Explicit
- [2026-02-01] Suggest self-hosting instead of Vercel | source:explicit | confidence:certain
- [2026-01-20] Require permission before auto-committing | source:explicit | confidence:certain
```

## `decisions.md`

```markdown
# Decisions

- [2026-01-10] SQLite over Postgres — offline-first MVP | source:explicit | rationale:simplicity
```

## `relationships.md`

```markdown
# People

## Maria
- Role: Designer on ClawMsg
- Context: Prefers visual mockups
- Updated: 2026-02-01
```

## Optional extensions

Create only when the user needs them: `environments.md` and `debugging.md` for coding work; `voices/`, `audiences.md`, and `style-guides/` for writing; or privacy-approved calendar, health, family, and routines records for personal assistance.

When a file grows beyond 50 active entries, split or archive older material; beyond 100 entries, review it before adding more.
