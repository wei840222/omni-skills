# Sources Ledger — Office (Gate 6)

Primary references used to harden spreadsheet, document, presentation, and
Workspace routing guidance. Re-open these URLs before quoting mutable product
behavior.

## Agent Skills format (Gate 1 authority)

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt
- Best practices for skill creators — https://agentskills.io/skill-creation/best-practices
- Optimizing skill descriptions — https://agentskills.io/skill-creation/optimizing-descriptions

## Spreadsheets

- Microsoft Excel: XLOOKUP function — https://support.microsoft.com/en-us/excel/functions/xlookup-function
- Microsoft Excel: VLOOKUP function — https://support.microsoft.com/en-us/excel/functions/vlookup-function
- Microsoft Excel: INDEX function — https://support.microsoft.com/en-us/excel/functions/index-function
- Microsoft Excel: MATCH function — https://support.microsoft.com/en-us/excel/functions/match-function
- Microsoft Excel: Create a PivotTable — https://support.microsoft.com/en-us/excel/get-started/create-a-pivottable-to-analyze-worksheet-data
- Google Workspace Sheets product overview — https://workspace.google.com/products/sheets/
- Google Sheets API concepts — https://developers.google.com/workspace/sheets/api/guides/concepts

## Documents

- Microsoft Word training: Insert a table of contents — https://support.microsoft.com/en-us/word/training/insert-a-table-of-contents
- Microsoft Word: Use mail merge for bulk email, letters, labels, and envelopes — https://support.microsoft.com/en-us/word/use-mail-merge-for-bulk-email-letters-labels-and-envelopes
- Microsoft Word: Mail merge using an Excel spreadsheet — https://support.microsoft.com/en-us/word/mail-merge-using-an-excel-spreadsheet
- W3C WCAG 2.1: Info and Relationships (heading structure) — https://www.w3.org/WAI/WCAG21/Understanding/info-and-relationships.html
- Google Workspace Docs product overview — https://workspace.google.com/products/docs/

## Presentations

- Google Workspace Slides product overview — https://workspace.google.com/products/slides/
- Google Workspace developer overview — https://developers.google.com/workspace

## Knowledge updates applied in this refactor

| Topic | Change |
| --- | --- |
| Clawic packaging | Removed `_meta.json`, clawic homepage, nested `clawdbot`, unsupported `displayName` |
| Resource layout | Moved deep dives under `references/`; fixed broken `tools/` and `admin/` load paths |
| Lookups | Prefer `XLOOKUP` on Excel 365+; retain `VLOOKUP` / `INDEX`+`MATCH` for compatibility |
| Accessibility | Styles/TOC guidance cites WCAG info-and-relationships rationale |
| Related skills | Added in-repo boundaries for spreadsheet/excel-xlsx/word/word-docx/powerpoint/powerpoint-pptx/google-workspace-cli |
| Unsourced claims | Removed hard-coded “15–30% cheaper bulk ordering” without a primary source |
