# Chunking — answer-sized units

**Load when** chunks are the "right size" but useless, or long documents never match.

- Target `chunk_tokens` ≈ p90 length of a self-contained answer in this corpus.
- Overlap = `chunk_overlap_pct` × `chunk_tokens` (default ~12%). Overlap is not a substitute for context.
- Never split inside a table, fenced code block, or numbered procedure.
- Prepend document title and heading path to every chunk (~20–40 tokens) so pronouns have a subject.
- Prefer structure-aware recursive splits. Use semantic boundary detection only when documents truly lack structure (transcripts, scanned prose)—it costs an extra embedding pass and gains are corpus-dependent.
- Parent-child: retrieve children, expand to parents when the answer needs surrounding sections.
