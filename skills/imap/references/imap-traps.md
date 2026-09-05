# IMAP Traps and Recovery

- Use UIDs for durable follow-up work; sequence numbers change after mailbox updates.
- Preserve `\Seen` during read-only review with read-only selection and non-mutating fetch forms. If a provider changes flags unexpectedly, record the behavior and use its safer read path next time.
- Scope searches server-side and fetch metadata first; narrow the UID window before reading bodies or attachments.
- When `UIDVALIDITY` changes, replace the cached UID window with a fresh folder checkpoint.
- Gate `MOVE`, `IDLE`, Gmail-style folders, and other extensions on advertised capability or provider documentation.
- Inspect MIME structure, filenames, charsets, and disposition before downloading a part.
