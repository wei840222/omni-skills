# Core Rules

## 1. Use Vectorized Operations
- Always use vectorized operations instead of iterating over DataFrame rows with `for` loops
- Use `.apply()` only when vectorized alternatives don't exist
- Prefer `df['col'].str.method()` over `apply(lambda x: x.method())`

## 2. Chain Methods for Readability
```python
# Good: method chaining
result = (df
    .query('age > 30')
    .groupby('city')
    .agg({'salary': 'mean'})
    .reset_index())

# Bad: intermediate variables everywhere
filtered = df[df['age'] > 30]
grouped = filtered.groupby('city')
result = grouped.agg({'salary': 'mean'}).reset_index()
```

## 3. Handle Missing Data Explicitly
- Always check `df.isna().sum()` before analysis
- Choose strategy: `dropna()`, `fillna()`, or interpolation
- Document WHY missing values exist before removing them

## 4. Use Categorical for Repeated Strings
```python
# Memory savings for columns with few unique values
df['status'] = df['status'].astype('category')
df['country'] = df['country'].astype('category')
```

## 5. Merge with Validation
```python
# Always specify how and validate
result = pd.merge(
    df1, df2,
    on='id',
    how='left',
    validate='m:1'  # Many-to-one: catch unexpected duplicates
)
```

## 6. Prefer query() for Complex Filters
```python
# Readable
df.query('age > 30 and city == "NYC" and salary < 100000')

# Hard to read
df[(df['age'] > 30) & (df['city'] == 'NYC') & (df['salary'] < 100000)]
```

## 7. Set Index When Appropriate
```python
# Faster lookups, cleaner merges
df = df.set_index('user_id')
user_data = df.loc[12345]  # O(1) lookup
```
