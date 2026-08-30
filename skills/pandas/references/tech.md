# Pandas Technical Guidelines

## Current Best Practices

- Prefer vectorized Series/DataFrame operations and method chaining for readable transforms.
- Use explicit `how=` and `validate=` on merges to catch unexpected duplication early.
- Declare dtypes at read time when files are large; convert repeated strings to `category` when cardinality is low.
- Treat missing data as a first-class decision: inspect with `isna()`, then choose `dropna()`, `fillna()`, or interpolation with a recorded reason.
- Prefer `query()` for complex boolean filters and `loc[]` for assignment to avoid chained-indexing bugs.
- Use `groupby(..., observed=True)` with categoricals and `reset_index()` when a clean flat DataFrame is the next consumer.

## Verifiable Sources

- pandas documentation — User Guide: https://pandas.pydata.org/docs/user_guide/index.html
- pandas documentation — 10 minutes to pandas: https://pandas.pydata.org/docs/user_guide/10min.html
- pandas documentation — Merging: https://pandas.pydata.org/docs/user_guide/merging.html
- pandas documentation — Group by: split-apply-combine: https://pandas.pydata.org/docs/user_guide/groupby.html
- pandas documentation — Working with missing data: https://pandas.pydata.org/docs/user_guide/missing_data.html
- pandas documentation — Scaling to large datasets: https://pandas.pydata.org/docs/user_guide/scale.html
- pandas documentation — Enhancing performance: https://pandas.pydata.org/docs/user_guide/enhancingperf.html
- Wikipedia — Pandas (software): https://en.wikipedia.org/wiki/Pandas_(software)
