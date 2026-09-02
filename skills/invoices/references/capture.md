# Capture

Route incoming documents before extraction.

## Format precedence
1. Native structured XML (XRechnung, FatturaPA, Facturae, Peppol UBL)
2. Hybrid PDF/A-3 with embedded XML (Factur-X / ZUGFeRD)
3. Ordinary PDF / image requiring OCR

## Intake checklist
- Prefer the embedded XML payload over OCR whenever both exist
- Keep the original bytes untouched; only rename for archive layout
- Record source channel (email attachment, portal download, scan, upload)
- Newest-first when importing a backlog; fully extract open tax periods first
