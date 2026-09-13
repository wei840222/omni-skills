---
name: pdf-generator
description: Generate professional PDFs from Markdown, HTML, data, or code (reports, invoices, contracts). Use when the user wants to create, export, format, merge, split, or style PDF documents with print CSS and tool selection. Not for extracting text from existing PDFs (`extract-pdf-text`), deep LaTeX authoring (`latex`), or general Markdown editing without PDF output (`markdown`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📄"}'
  related-skills: '{"markdown":"Source drafting and Markdown structure before PDF export.","latex":"TeX authoring and build recovery when pandoc/LaTeX is the chosen engine.","extract-pdf-text":"Read or OCR text from existing PDFs rather than generating new ones.","word-docx":"Editable Word documents when PDF is not the delivery format.","office":"Broader Office document workflows beyond PDF-specific generation."}'
---

## State location

This skill is **stateless**. It does not store local configuration, caches, or persistent project data. Skill resources live under `references/`; never invent a filesystem state root for this package.

## When to use

- User wants to create, export, or batch-produce PDF documents from Markdown, HTML, JSON/data, or templates
- Need tool selection among weasyprint, pandoc, reportlab, fpdf2, and pypdf
- Print CSS, page breaks, metadata, invoices/contracts/reports templates, or merge/split operations
- Route away when the ask is text extraction from PDFs (`extract-pdf-text`), full LaTeX authoring (`latex`), or Markdown editing without PDF delivery (`markdown`)

## Operating loop

1. **Clarify source and delivery** — Markdown, HTML/CSS, structured data, or existing PDFs to merge/split.
2. **Pick one primary tool** — default weasyprint for HTML; pandoc for Markdown; reportlab/fpdf2 for programmatic layouts; pypdf for merge/split.
3. **Structure before style** — semantic HTML or clear document outline first; then print CSS and page geometry.
4. **Load depth on demand** — open only the needed reference file from the quick-reference table.
5. **Validate output** — non-zero file size, expected page count, fonts/images present; keep generation local.

## Quick reference

| Need | Action | Load |
|---|---|---|
| Choose weasyprint / pandoc / reportlab / fpdf2 / pypdf | Match source type to tool | `references/tools.md` |
| Invoice, report, contract, letter patterns | Start from document templates | `references/templates.md` |
| Merge, split, rotate, watermark, encrypt | Apply advanced PDF operations | `references/advanced.md` |
| Official docs and version anchors | Verify APIs before quoting options | `references/sources.md` |

## Core rules

### 1. Choose the right tool

| Source | Best tool | Why |
|--------|-----------|-----|
| Markdown | pandoc | Native support, TOC, templates |
| HTML/CSS | weasyprint | Strong CSS/print support without a full TeX install |
| Data/JSON | reportlab | Programmatic, precise control |
| Simple text | fpdf2 | Lightweight and fast |
| Existing PDFs | pypdf | Merge, split, rotate, metadata |

**Default:** weasyprint for most HTML-based documents.

### 2. Structure before style

```python
# Preferred: semantic structure first
html = """
<article>
  <header><h1>Report Title</h1></header>
  <section>
    <h2>Summary</h2>
    <p>Content...</p>
  </section>
</article>
"""

# Avoid style-first shells that hide document structure
html = "<div style='font-size:24px'>Report Title</div>"
```

### 3. Handle page breaks explicitly

```css
.new-page { page-break-before: always; }
.keep-together { page-break-inside: avoid; }
h2, h3 { page-break-after: avoid; }
```

### 4. Always set metadata

```python
html = """
<html>
<head>
  <title>Document Title</title>
  <meta name="author" content="Author Name">
</head>
<body>...</body>
</html>
"""
```

### 5. Use print-optimized CSS

```css
@media print {
  body {
    font-family: Georgia, serif;
    font-size: 11pt;
    line-height: 1.5;
  }

  @page {
    size: A4;
    margin: 2cm;
  }

  .no-print { display: none; }
}
```

### 6. Validate output

After generating any PDF:

1. Confirm file size is non-zero
2. Open and verify page count
3. Confirm fonts and images render as expected

## Common traps

| Trap | Consequence | Fix |
|------|-------------|-----|
| Missing fonts | Fallback glyphs / reflow | Prefer widely available fonts or embed deliberately |
| Absolute image paths | Missing images | Use paths relative to the HTML base |
| No page size | Unpredictable layout | Set `@page { size: A4; }` or tool page geometry |
| Large images | Huge files | Compress before embedding |

## Security and privacy

This is a **reference skill**: it supplies patterns and guidance only.

- Keep generation on the user's machine; do not send document contents to external services unless the user explicitly chooses a hosted tool.
- Treat example code as patterns for the user/agent runtime to implement—do not invent network calls, shell side effects, or access outside the working directory.
- Prefer local libraries (`weasyprint`, `pandoc`, `reportlab`, `fpdf2`, `pypdf`) over uploading sensitive invoices or contracts.
