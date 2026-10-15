# Apple Mail SQLite Queries

macOS-only indexed reads against Mail.app's Envelope Index. Prefer this path for fast local search when Mail.app is already syncing accounts. Use himalaya when you need send or cross-platform IMAP.

## Database location

Live host path (typical):

```bash
ls "$HOME"/Library/Mail/V*/MailData/Envelope\ Index
# Often V10 or V11
```

When documenting portable skill state, refer to:

```text
<state_root>/Library/Mail/V*/MailData/Envelope Index
```

only if the host maps the user home under the resolved `<state_root>`. Never invent a second copy of the mailbox database inside the skill package.

Force sync before querying — the SQLite index lags otherwise:

```bash
osascript -e 'tell app "Mail" to check for new mail'
```

## Schema essentials

| Table | Key columns |
|-------|-------------|
| `messages` | subject, sender, date_received, attachment_count, message_id |
| `addresses` | address, comment (display name) |
| `mailboxes` | url (folder path), unread_count |

## Common queries

### Recent emails (last 7 days)

```sql
SELECT m.subject, a.address, datetime(m.date_received, 'unixepoch')
FROM messages m
JOIN addresses a ON m.sender = a.ROWID
WHERE m.date_received > strftime('%s','now','-7 days')
ORDER BY m.date_received DESC
LIMIT 50;
```

### Unread count by folder

```sql
SELECT url, unread_count FROM mailboxes WHERE unread_count > 0;
```

### Search by sender domain

```sql
SELECT m.subject, a.address
FROM messages m
JOIN addresses a ON m.sender = a.ROWID
WHERE a.address LIKE '%@example.com';
```

## Attachments

Attachment files may live under:

```text
$HOME/Library/Mail/V*/MAILBOX/Messages/
```

`attachment_count > 0` does **not** guarantee the attachment bytes are downloaded locally.

## Traps

- **Stale data** — always sync Mail.app first.
- **`date_received` is Unix seconds** — wrap with `datetime(..., 'unixepoch')`.
- **Path escaping** — quote `Envelope Index` or escape the space.
- **Read-only** — do not UPDATE/DELETE the Envelope Index through this skill; mutate mail via Mail.app UI/`apple-mail-macos` or himalaya after confirmation.
- **Do not mix** with himalaya mutations in the same task.
