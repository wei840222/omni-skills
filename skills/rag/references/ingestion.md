# Ingestion — parse before you chunk

**Load when** PDFs, scans, spreadsheets, or transcripts come out mangled, or indexed counts do not match expected chunks.

1. Choose a parser by document class. Prefer a real text layer; run OCR only when there is none.
2. Assert non-empty text per page/section before chunking. Empty pages silently embed whitespace.
3. Normalize encoding, boilerplate headers/footers, and broken hyphenation early.
4. Attach `doc_id`, `source_uri`, `source_version`, title, and heading path before the first upsert.
5. Assert indexed count equals expected chunk count after every batch; read per-item upsert errors.

Failure modes: "ingestion succeeded" with a half-empty index; tables flattened into noise; scanned pages treated as text PDFs.
