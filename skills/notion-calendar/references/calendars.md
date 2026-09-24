# Calendar Source Mapping

Use this file as the stable map between human names and verified Notion identifiers.

## What to Store

For each approved calendar-like source, keep:
- Workspace name
- Human label used by the user
- `database_id`
- `data_source_id`
- Verified property names for title, date, status, owner, and URL

## Minimal Record Shape

```markdown
- Editorial Calendar
  - database_id: ...
  - data_source_id: ...
  - title property: Name
  - date property: Publish Date
  - status property: Status
  - last verified: YYYY-MM-DD
```

## Safety Rule

Store each human label only after `database_id` and `data_source_id` are confirmed. When two workspaces or two databases share a name, keep both records and select by ID, not by label.
