# Query recipes — Apple Health MCP

Load after authorized `health_schema` discovery. Adapt table/column names to actual schema; all examples assume the listed columns exist. Inspect source names, units, category labels and date coverage before choosing a query. Each call contains one analytical statement.

Examples use fixed synthetic windows so an old export does not silently become a "last 30 days" claim. Replace both bounds with the user's actual reporting window and state it. End bounds are exclusive; per-day counts use stored local clock dates.

## 1. Resting heart rate over 30 days

```sql
SELECT DATE(startDate) AS day, sourceName, unit,
       ROUND(AVG(value), 1) AS average_rhr, COUNT(*) AS readings
FROM hkquantitytypeidentifierrestingheartrate
WHERE startDate >= TIMESTAMP '2026-09-01 00:00:00'
  AND startDate < TIMESTAMP '2026-10-01 00:00:00'
GROUP BY DATE(startDate), sourceName, unit
ORDER BY day, sourceName, unit;
```

Keep units visible and verify the observed unit is bpm before naming `average_rhr` as bpm. This is a sample mean, not necessarily a time-weighted or clinical baseline. Compare at most two explicit windows.

## 2. Asleep duration over 14 days

```sql
SELECT DATE(startDate) AS start_day, sourceName,
       ROUND(SUM(DATE_DIFF('second', startDate, endDate)) / 3600.0, 2) AS hours_asleep
FROM hkcategorytypeidentifiersleepanalysis
WHERE LOWER(valueText) LIKE '%asleep%'
  AND startDate >= TIMESTAMP '2026-09-17 00:00:00'
  AND startDate < TIMESTAMP '2026-10-01 00:00:00'
  AND endDate > startDate
GROUP BY DATE(startDate), sourceName
ORDER BY start_day, sourceName;
```

Use this sum only after inspecting labels and establishing that asleep intervals within each source do not overlap. Awake/in-bed rows are excluded. If detailed stages overlap a summary asleep interval, union intervals or choose the non-overlapping representation; summing both overcounts. Keep different sources separate until the user chooses a device/overlap policy.

`start_day` means interval start date, not an inferred bedtime/night label. Cross-midnight intervals retain their whole duration under that start date; intervals crossing window boundaries require clipping if the requested metric is time strictly inside the window. State that convention or adapt it explicitly.

## 3. Workout counts over 12 weeks

Discover the actual workout tables using `commonPatterns.workouts`. When schema returns `hkworkoutactivitytyperunning`, a per-table example is:

```sql
SELECT DATE_TRUNC('week', startDate) AS week, sourceName,
       COUNT(*) AS workouts
FROM hkworkoutactivitytyperunning
WHERE startDate >= TIMESTAMP '2026-07-09 00:00:00'
  AND startDate < TIMESTAMP '2026-10-01 00:00:00'
GROUP BY DATE_TRUNC('week', startDate), sourceName
ORDER BY week, sourceName;
```

Use each discovered activity table or a schema-driven union; do not assume one combined `hkworkoutactivitytype` exists. Check duplicate recordings before adding counts across sources. Durations use `DATE_DIFF('second', startDate, endDate) / 60.0` minutes. For a verified overview, `health_report` aggregates discovered workout tables, but does not replace overlap/time/privacy checks.

## Tool and time semantics

- `health_query` arguments contain `query` and `format` (`json`, `csv` or `summary`). Construct one real SELECT-family statement from observed schema.
- `health_report` supports weekly/monthly/custom; custom uses `start_date` and `end_date` in YYYY-MM-DD form. Verify the live tool schema rather than assuming report end-bound semantics match SQL.
- The importer strips source timezone offsets and stores local clocks as TIMESTAMP. A returned JSON `Z` is not proof of UTC. `CAST(startDate AS VARCHAR)` can expose the stored clock time; it cannot reconstruct the lost offset. Cross-zone chronology needs the original export/timezone evidence.
- Full CSV history is loaded for every touched table regardless of query bounds. A memory failure is not zero recorded activity.
- Report exact window, unit, per-source/overlap policy, export freshness and missing dates. Keep output aggregate by default and apply SKILL.md client/provider authorization before all tools, including schema.

Verified derivation and current limitations: `references/sources.md`.
