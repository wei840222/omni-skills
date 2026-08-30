---
name: pandas
description: Analyze, transform, and clean DataFrames with efficient patterns for filtering, grouping, merging, and pivoting.
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"🐼","requires":{"bins":["python3"]},"os":["linux","darwin","win32"],"displayName":"Pandas"}'
  related-skills: '{"data-analysis":"Broader analysis framing, metrics, and decision briefs beyond DataFrame mechanics","csv":"Delimited-text interchange before or after Pandas transforms","sql":"Relational query and schema work instead of in-memory DataFrames","excel-xlsx":"Native workbook editing when the artifact must remain an Excel file"}'
---

## When to Use

User needs to work with tabular data in Python. Agent handles DataFrame operations, data cleaning, aggregations, merges, pivots, and exports.

## State location

Memory may live under a portable `<state_root>/`. See `references/memory-template.md` for structure.

Resolve `<state_root>` before reading or writing state:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/pandas/`, `<workspace>/memory/pandas/`, `~/pandas/`.
3. If none exists and state must be created, ask for permission and default to `<workspace>/pandas/`.

```
<state_root>/
├── memory.md     # User preferences and common patterns
└── snippets/     # Saved code patterns (optional)
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Setup process | `references/setup.md` | When `<state_root>/` doesn't exist |
| Memory template | `references/memory-template.md` | When reading or updating user preferences |
| Core rules | `references/core-rules.md` | When writing or reviewing Pandas code |
| Common traps | `references/common-traps.md` | When debugging errors or performance issues |
| Technology overview | `references/tech.md` | When needing domain context on Pandas |

## Security & Privacy

**Data storage:**
- User preferences stored in `<state_root>/memory.md`
- All DataFrame operations run locally
- No data is sent externally

**This skill is restricted to local operations:**
- Keep all data strictly local
- Limit file access to `<state_root>/` and the working directory
- Preserve source data files unless explicitly instructed to modify them

**User control:**
- View stored preferences: `cat <state_root>/memory.md`
- Clear all data: `rm -rf <state_root>/`
