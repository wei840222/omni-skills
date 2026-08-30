# Common Traps

- **SettingWithCopyWarning** → Use `.loc[]` for assignment: `df.loc[mask, 'col'] = value`
- **Slow loops** → Replace `iterrows()` with vectorized ops or `apply()`
- **Memory explosion** → Use `dtype` in `read_csv()`: `pd.read_csv(f, dtype={'id': 'int32'})`
- **Silent data loss** → Check shape before/after merge: `print(f"Before: {len(df1)}, After: {len(result)}")`
- **Index confusion** → Use `reset_index()` after `groupby()` to get clean DataFrame
- **Chained indexing** → `df['a']['b']` fails silently; use `df.loc[:, ['a', 'b']]`
