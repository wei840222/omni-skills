---
name: office
description: >
  Route Excel/Sheets, Word/Docs, PowerPoint/Slides, and light office-admin
  how-tos: formulas and lookups, Styles/TOC/mail merge, Slide Master and
  Presenter View, plus supplies/vendor/space basics. Use when the user asks
  how to do something in Microsoft 365 or Google Workspace apps, or needs
  facility/admin checklists. Prefer `spreadsheet` / `excel-xlsx` for file
  analysis or programmatic workbooks, `word` / `word-docx` for live or OOXML
  document edits, `powerpoint` / `powerpoint-pptx` for live or PPTX decks,
  and `google-workspace-cli` for API/CLI automation.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏢"}'
---

# Office

Cross-app how-to router for Microsoft 365 and Google Workspace productivity
tasks (Excel/Sheets, Word/Docs, PowerPoint/Slides), plus light physical-office administration. Stay in **advise** mode:
give steps the human can run; do not send mail merges, alter shared calendars,
or change vendor contracts without explicit authorization for that action.

## Progressive disclosure

Keep this file as the always-on contract. Load **at most one** reference for
the current ask; do not preload every deep dive.

| Signal | Context | Load |
| --- | --- | --- |
| Formulas, pivot tables, VLOOKUP/XLOOKUP, macros | Spreadsheets | `references/spreadsheets.md` |
| Styles, headers, mail merge, TOC | Documents | `references/documents.md` |
| Slide Master, animations, Presenter View | Presentations | `references/presentations.md` |
| Supplies, vendors, facilities, space | Office admin | `references/facilities.md` |
| Re-check primary docs / Gate 6 ledger | Sources | `references/sources.md` |

## Routing boundaries

- Spreadsheet **file** analysis, schema memory, or CSV/Sheets edits as artifacts → `spreadsheet` or `excel-xlsx`.
- Live Word window / track changes / selection-aware edits on macOS → `word`; offline DOCX → `word-docx`.
- Live PowerPoint presenter/window state on macOS → `powerpoint`; offline PPTX → `powerpoint-pptx`.
- Gmail/Drive/Calendar bulk ops, OAuth, or Admin SDK via CLI → `google-workspace-cli`.
- Personal ID/contract vault tracking → `documents` (different skill).

## Critical rules

1. **Advise only** — draft steps and formulas; do not execute destructive shared-mailbox, calendar, or contract changes unless the user authorizes that specific action.
2. **Prefer modern lookups** — for Excel 365+, prefer `XLOOKUP` over `VLOOKUP` when teaching new formulas; keep `INDEX`/`MATCH` for compatibility paths.
3. **Styles before cosmetics** — structure Word/Docs with Heading styles before building a TOC or fixing spacing by hand.
4. **One idea per slide** — keep Presenter View / Slide Master guidance practical; avoid animation theatre.
5. **Source mutable facts** — quote supplier discounts, SLA numbers, or product limits only from a current primary source in `references/sources.md` or a newly verified URL.
6. **Route adjacent tools** — hand off to the related skills above when the user needs file mutation, live app control, or Workspace API automation rather than how-to guidance.

## Quick reference

| Task | Excel/Sheets | Word/Docs | PowerPoint/Slides |
| --- | --- | --- | --- |
| Find value | `XLOOKUP` / `VLOOKUP` / `INDEX`+`MATCH` | Find & Replace | Find & Replace |
| Structure | Tables + Pivot | Heading styles + TOC | Slide Master layouts |
| Personalize at scale | Formulas | Mail merge | Linked content / notes |
| Export | Save/Download as PDF | Save/Download as PDF | Export as PDF |
