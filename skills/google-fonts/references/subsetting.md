## Subsetting

- Default Google Fonts delivery targets Latin; add extra subsets only when the content needs them.
- Request additional character coverage deliberately (for example Latin Extended for Polish or Vietnamese) instead of enabling every available subset.
- Verify the glyphs actually used in the UI/copy, then drop unused subsets to reduce bytes.
- For CJK families, expect large payloads even when sliced; prefer the smallest workable family and subset set.
