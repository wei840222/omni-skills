# Schema Design & Data Ingestion

## Tags vs Fields (Critical)

- Tags are indexed, fields are not. Filter on tags, aggregate on fields.
- Tag values must be strings. Numbers as tags work but waste index space.
- Fields support numbers, strings, and booleans. Store metrics as fields.
- The choice between tag and field cannot be changed after data is written.

## Cardinality Trap

- High-cardinality tags destroy performance. Storing unique user IDs as tags leads to disaster.
- Cardinality equals unique combinations of tag values and grows multiplicatively.
- Check with `SHOW CARDINALITY` (1.x) or `influx bucket inspect` (2.x).
- Rule of thumb: <100K series per measurement; millions indicate a problem.

## Line Protocol

- Format: `measurement,tag1=v1,tag2=v2 field1=1,field2="str" timestamp`
- No spaces around `=` in tags. Space separates tags from fields.
- String fields require quotes, whereas tag values remain unquoted: `field="text"` vs `tag=text`.
- Timestamps are in nanoseconds by default. Specify precision to ensure accurate data ingestion.

## Timestamps

- Default precision is nanoseconds. Sending seconds without a precision flag inserts data in the year 2000.
- Specify precision on write: `precision=s` for seconds, `precision=ms` for milliseconds.
- Missing timestamps use server time, which is usually fine for real-time ingestion.
- Timestamps are UTC. Client timezone is irrelevant.

## Schema Architecture

- Measurement name acts as table name (e.g., one per metric type like cpu, memory, requests).
- Use tags for dimensions you filter/group by (host, region, service).
- Use fields for values you aggregate (usage_percent, count, latency_ms).
- Encode data as tags rather than in measurement names (e.g., use `cpu` + `host=host1` rather than `cpu.host1`).
