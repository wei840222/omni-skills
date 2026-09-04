# Files and SQLite CRM

Use this when the system of record is local files or a single SQLite database.

## Files layout

Default under `<state_root>/crm/db/`:

| File / folder | Holds |
|---|---|
| `people.md` or `people.json` | Person rows keyed by lowercased email |
| `organizations.md` | Orgs keyed by domain |
| `deals.md` | Open and closed deals |
| `interactions/<year>.md` | One-line interaction log |
| `exports/<date>/` | Dated backups before bulk ops |

Keep the shared people box in `<state_root>/contacts/contacts.md`. Do not fork a second address book inside `crm/db/`.

## SQLite layout

One file, one table per entity, UUID primary keys, foreign keys for org/contact/deal links.

```sql
-- sketch only; adapt types to the chosen SQLite helper
CREATE TABLE person (
  id TEXT PRIMARY KEY,
  email TEXT UNIQUE COLLATE NOCASE,
  name TEXT NOT NULL,
  org_id TEXT,
  role TEXT,
  preferred_channel TEXT,
  tier TEXT,
  source TEXT,
  owner TEXT,
  next_step TEXT,
  next_step_on TEXT,
  suppressed INTEGER NOT NULL DEFAULT 0
);
```

Rules:

1. Backup (file copy or `.dump`) before every bulk write.
2. Wrap imports and merges in a transaction; roll back on identity-key collision.
3. Export CSV/JSON with stable ids before any migration off SQLite.
4. Move off single-file SQLite only when a second writer needs concurrent access.
