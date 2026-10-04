# People memory template

Create only after State location resolution and named consent.

## `<state_root>/memory.md`

```markdown
# People memory

## Boxes
<!-- path | read when condition -->

## Due
<!-- hygiene and date scans -->

## Open Loops
<!-- YYYY-MM-DD | person | loop | status -->

## Dates
<!-- optional index; person files remain source of truth -->
```

## `<state_root>/config.yaml`

```yaml
nudge_style: on-ask
reconnect_months: 6
birthday_lead_days: 5
brief_lines: 5
sensitive_details: minimal
roster_review: quarter
name_order: as-given
```

## `<state_root>/do-not-surface.md`

```markdown
# Do not surface
<!-- name | key | reason | since -->
```

## Shared contacts row

`Name | Key | Role | Preferred channel | Context | Last contact | File`
