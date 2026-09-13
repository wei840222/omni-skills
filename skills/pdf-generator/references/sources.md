# Sources — PDF generation

Primary references for tool selection and API behavior. Re-check the linked docs before quoting flags, CSS support limits, or security options; library defaults change across major versions.

## Agent Skills / package contract

- Agent Skills Specification — frontmatter, resources, and directory compatibility: https://agentskills.io/specification.md
- Agent Skills Best Practices — progressive disclosure and calibrated entry points: https://agentskills.io/skill-creation/best-practices.md

## HTML / CSS → PDF

- WeasyPrint documentation (stable) — HTML/CSS rendering, `@page`, fonts, and CLI/API: https://doc.courtbouillon.org/weasyprint/stable/
- CSS Paged Media Module Level 3 — print page model concepts used by print CSS: https://www.w3.org/TR/css-page-3/

## Markdown / conversion toolchain

- Pandoc User's Guide — Markdown→PDF paths, templates, and variables: https://pandoc.org/MANUAL.html

## Programmatic PDF libraries

- ReportLab User Guide — canvas/platypus programmatic layouts: https://www.reportlab.com/docs/reportlab-userguide.pdf
- fpdf2 documentation — lightweight PDF generation API: https://py-pdf.github.io/fpdf2/
- pypdf documentation — merge, split, rotate, encrypt, and metadata: https://pypdf.readthedocs.io/en/stable/

## Scope notes

- This skill coaches local generation patterns. Hosted SaaS converters are out of scope unless the user explicitly requests them.
- Text extraction / OCR of existing PDFs belongs to `extract-pdf-text`.
- Deep TeX authoring and build recovery belong to `latex`; use pandoc here only as a conversion path.
