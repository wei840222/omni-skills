---
name: spreadsheet
description: Read, write, and analyze spreadsheets with schema memory and format preservation. Use when the user requests table analysis, cell edits, reports, or structured tracking in Google Sheets, Excel, or CSV files.
metadata:
  openclaw: '{"emoji":"📊"}'
compatibility: "linux, darwin, win32"
---

## State location

Spreadsheet state may exist in `<workspace>/spreadsheet/`, `<workspace>/memory/spreadsheet/`, or `~/spreadsheet/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured state path when one exists.
2. Otherwise, use the first existing directory in this order: `<workspace>/spreadsheet/`, `<workspace>/memory/spreadsheet/`, then `~/spreadsheet/`.
3. If no candidate exists and the user asks to save state, create `<workspace>/spreadsheet/` after checking all candidates.

Use the selected `<state_root>` for every state operation during this invocation; do not merge or cross-read lower-precedence copies.

## When to Use

User needs spreadsheet operations: reading data, writing cells, analyzing tables, generating reports, or tracking structured information across Google Sheets, Excel, or CSV files.

## Architecture

Memory lives in `<state_root>/`. See `references/memory-template.md` for setup.

```
<state_root>/
  memory.md           # Preferences, recent sheets, format rules
  projects/           # Per-project schemas and configs
    {name}.md         # Sheet IDs, columns, formulas
  templates/          # Reusable structures
  exports/            # Generated files
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Memory setup | `references/memory-template.md` | When initializing or modifying state memory |
| Google Sheets API | `references/google-sheets.md` | When reading from or writing to Google Sheets |
| Excel operations | `references/excel.md` | When handling local `.xlsx` files |
| CSV handling | `references/csv.md` | When parsing or exporting `.csv` files |
| Domain knowledge | `references/domain-knowledge.md` | When needing facts about Spreadsheet concepts |

## Scope

- Read and write spreadsheets only when the user explicitly requests it.
- Store schemas and preferences exclusively in `<state_root>/`.
- Process only files provided by the user.
- Omit passwords, API keys, and sensitive financial data from being stored or logged.
- Ensure modifications are restricted strictly to `<state_root>/` and explicitly authorized user paths.

## Data Storage

Store all user data in `<state_root>/`. Create on first use:
```bash
mkdir -p <state_root>/{projects,templates,exports}
```

## Self-Modification

Maintain `SKILL.md` as a read-only document. Store all dynamic state and user data exclusively in `<state_root>/`.

## Core Rules

### 1. Schema First
On first access to any sheet:
1. Document columns (name, type, sample)
2. Save to `projects/{name}.md`
3. Reference schema in future ops

### 2. Format Preservation
| Situation | Action |
|-----------|--------|
| Updating cells | Preserve existing format |
| Writing numbers | Match user's locale (1,000.00 vs 1.000,00) |
| Writing dates | Use user's preferred format |
| Writing formulas | Retain existing formulas unless explicitly instructed to overwrite |

### 3. Large Data Strategy
| Row Count | Approach |
|-----------|----------|
| <1000 | Load fully |
| 1000-10000 | Sample + targeted queries |
| >10000 | Paginate, warn before loading |

### 4. Integration Priority
1. **Google Sheets** - if API configured
2. **Excel (.xlsx)** - local files, use openpyxl
3. **CSV** - universal fallback

### 5. Memory Updates
| Event | Action |
|-------|--------|
| New sheet accessed | Add ID + schema to memory |
| User corrects format | Save preference |
| Column renamed | Update project schema |

## Common Traps

- **Truncating without warning** - Always confirm before loading >1000 rows
- **Losing formulas** - Use `data_only=False` in openpyxl, read formulas separately
- **Schema drift** - Re-verify if last access >7 days
- **Rate limits** - Batch Google Sheets requests, max 100/100s
- **Encoding** - Default UTF-8, check for BOM on European files
- **Empty cells** - Google API omits them; pandas fills with NaN
