---
name: spreadsheet
description: Trigger when the user requests reading data, writing cells, analyzing tables, generating reports, or tracking structured information across Google Sheets, Excel, or CSV files. Uses schema memory and format preservation.
metadata:
  openclaw: '{"emoji":"📊"}'
compatibility: "linux, darwin, win32"
---

## When to Use

User needs spreadsheet operations: reading data, writing cells, analyzing tables, generating reports, or tracking structured information across Google Sheets, Excel, or CSV files.

## Architecture

Memory lives in `<state_root>/spreadsheet/`. See `references/memory-template.md` for setup.

```
<state_root>/spreadsheet/
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
- Store schemas and preferences exclusively in `<state_root>/spreadsheet/`.
- Process only files provided by the user.
- Omit passwords, API keys, and sensitive financial data from being stored or logged.
- Ensure modifications are restricted strictly to `<state_root>/spreadsheet/` and explicitly authorized user paths.

## Data Storage

Store all user data in `<state_root>/spreadsheet/`. Create on first use:
```bash
mkdir -p <state_root>/spreadsheet/{projects,templates,exports}
```

## Self-Modification

Maintain `SKILL.md` as a read-only document. Store all dynamic state and user data exclusively in `<state_root>/spreadsheet/`.

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
