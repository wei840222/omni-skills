## Typo Tolerance

- Default behavior by word length: 1–4 chars = no typo allowed (prefix/same-length only); 5–8 chars = 1 typo; 9+ chars = 2 typos.
- A typo on the first character counts as 2 typos — so "tset" won't match "test" (4 chars, 0 typos allowed), but "caturday" could match "saturday" (8 chars, 1 typo allowed) only if the first letter is correct.
- Typo tolerance on IDs, SKUs, or codes causes false matches. Disable with `typoTolerance.disableOnAttributes: ["sku", "code"]` or `disableOnWords: ["exact-term"]`.
- Adjust thresholds via `typoTolerance.minWordSizeForTypos: {oneTypo: N, twoTypos: M}` where `0 ≤ oneTypo ≤ twoTypos ≤ 255`. Recommended: `oneTypo` 2–8, `twoTypos` 4–14.

## Filtering

- Filters on undeclared `filterableAttributes` return an `invalid_search_filter` error listing available filterable attributes. Always declare attributes before filtering.
- Geo-filtering requires a field named exactly `_geo` with `{lat, lng}`. The field name is hardcoded and cannot be renamed.
- Filter syntax uses custom operators. Use `TO` for ranges: `year 2020 TO 2024`.
- Empty array in `IN` clause causes an error. Validate array length before building the filter string.

## Search Behavior

- Default `limit` is 20, max is 1000. Meilisearch supports two pagination styles:
  - **offset/limit**: `offset` + `limit` (no hard cap on total results, but `limit` ≤ 1000).
  - **page/hitsPerPage**: finite pagination with `page` + `hitsPerPage` (returns `totalPages`, `totalHits`; `hitsPerPage` ≤ 1000).
- Multi-word queries match ANY word by default. Use `"exact phrase"` in the query for phrase matching.
- Highlighting only works on fields listed in `searchableAttributes` — not on stored-only fields.
- `facetsDistribution` counts include all matching documents, not just the returned page.
