---
name: extract-pdf-text
description: Extract text, tables, and structured data from local PDFs with PyMuPDF, and use Tesseract OCR only for scanned or image-only pages. Use when a user needs to read, parse, search, summarize, or analyze a PDF without sending its contents to an external service.
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"📄","requires":{"bins":["python3","tesseract"],"pip":["pymupdf","pytesseract","pillow"]},"install":[{"id":"pymupdf","kind":"pip","package":"PyMuPDF","label":"Install PyMuPDF"},{"id":"pytesseract","kind":"pip","package":"pytesseract","label":"Install pytesseract"},{"id":"pillow","kind":"pip","package":"Pillow","label":"Install Pillow"}]}'
---

## Workflow

1. Confirm the PDF path and the requested output: plain text, reading-order text, blocks, tables, or JSON. Treat the original PDF as read-only and keep processing local.
2. Open the PDF with PyMuPDF and extract native text first. Use `page.get_text(sort=True)` when a human reading order is important.
3. For each page with no meaningful native text, read `references/ocr.md` and use the documented OCR path. Keep native-text pages on the faster native path.
4. For a corrupt, password-protected, empty, misordered, table-heavy, or large file, read `references/troubleshooting.md` before reporting the failure or choosing a recovery.
5. Return the requested result with the extraction method used and page coverage. State any pages where OCR or native extraction could not produce reliable text.

## Setup and native extraction

Install PyMuPDF in the active Python environment:

```bash
python3 -m pip install PyMuPDF
```

PyMuPDF is imported as `fitz`. Extract page by page and keep page boundaries, so the result can identify failures and OCR fallbacks:

```python
import fitz

with fitz.open("document.pdf") as doc:
    pages = [page.get_text(sort=True) for page in doc]
text = "\n\f\n".join(pages)
```

Use native extraction before OCR. A page with very little extracted text may be scanned, but treat the threshold as a signal to inspect rather than proof:

```python
def needs_ocr(page, minimum_characters=50):
    return len(page.get_text().strip()) < minimum_characters
```

For code patterns, page ranges, metadata, blocks, tables, batch extraction, and password handling, read `references/examples.md`.

## Output choices

| Need | PyMuPDF method |
| --- | --- |
| Plain text | `page.get_text(sort=True)` |
| Positioned text blocks | `page.get_text("dict")["blocks"]` |
| JSON | `page.get_text("json")` then `json.loads(...)` |
| Tables | `page.find_tables()` then `table.extract()` |

PDFs may encode text in an unexpected order. Use `sort=True` for a simple top-left-to-bottom-right order; for complex layouts, return blocks or explain the limitation instead of silently presenting a reordered result as exact.

## Boundaries and completion

- Access a PDF only after the user supplies or authorizes its path.
- Keep files and extracted content local; this skill makes no external API calls.
- Preserve the source PDF. Write any derived text, JSON, or OCR output to a separate user-approved path.
- Verify the page count and report the method for every page before presenting extraction as complete.

## Common failure patterns

| Situation | Reliable response |
| --- | --- |
| Password is unavailable or rejected | Report that the document remains locked; request a valid user-supplied password. |
| Native text is empty | Inspect the page and follow `references/ocr.md`; report OCR confidence limits. |
| Reading order is wrong | Retry with `sort=True`; return positioned blocks when layout still matters. |
| Tables do not extract cleanly | Use `find_tables()` where suitable and label imperfect results rather than inventing cell structure. |
| File is corrupt or memory is constrained | Follow `references/troubleshooting.md` and process one page at a time. |

## On-demand references

- Read `references/examples.md` for copy-ready patterns: specific pages, metadata, blocks, tables, batches, and encrypted PDFs.
- Read `references/ocr.md` when a page has no usable native text or the user explicitly requests OCR.
- Read `references/troubleshooting.md` for errors, poor text order, unreliable OCR, memory pressure, or table-extraction limits.
