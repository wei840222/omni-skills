# Long Sources (Chunk → Map → Reduce)

Scope: inputs too long for one reliable pass. Complements "lost in the middle" handling in `SKILL.md` (Liu et al.).

## When to chunk

- Source will not fit a faithful single pass, or middle-section degradation is unacceptable.
- The same source will be re-queried and a chunk map amortizes cost.
- Do **not** chunk a source that already fits; seams add cross-chunk loss for no gain.

## Procedure

1. **Orient** — headings, length, genre, date; choose payload strategy from `SKILL.md`.
2. **Chunk on semantic boundaries** — sections, scenes, speakers, chapters. Avoid mid-argument splits.
3. **Map** — per chunk: load-bearing claims with numbers, hedges, attribution, and location. Map is not a summary.
4. **Rank** — by consequence to the named reader; apply point budget `target words ÷ 25`.
5. **Reduce** — write the deliverable from the ranked map only.
6. **Cross-chunk pass** — restore arguments that span chunks; never drop a claim only because it straddled a boundary.
7. **Verify** — faithfulness then coverage (`verification.md`).

## Hard rules

- One generation from the source (Core Rule 5): shorter cuts go back to source or level-1 map, never to a prior short summary.
- Keep intermediate maps when `store_summaries` and Boxes say so; otherwise discard after delivery.
- Sequential "refine the summary of the summary" is forbidden.

## Failure modes

| Failure | Cause | Fix |
|---------|-------|-----|
| Table-of-contents summary | Skipped rank | Rank by reader consequence |
| Missing middle findings | One-pass on huge input | Explicit middle sample or chunk map |
| Number drift across chunks | Abstractive merge without extracts | Hybrid: extract numbers before merge |
