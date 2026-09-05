# IMAP Domain Knowledge

- IMAP4rev2 supports mailbox manipulation, selective message fetches, flags, search, and offline resynchronization.
- A message sequence number is position-dependent; a UID is stable only within one `UIDVALIDITY` epoch.
- `UIDPLUS`, `CONDSTORE`, `QRESYNC`, `MOVE`, and special-use mailboxes are extensions: use them only after capability discovery.
- `BODYSTRUCTURE` describes MIME parts so clients can fetch the needed body section rather than a full message.

## Sources

- RFC 9051 (IMAP4rev2): https://www.rfc-editor.org/rfc/rfc9051.html
- RFC 3501 (IMAP4rev1): https://www.rfc-editor.org/rfc/rfc3501.html
- RFC 6855 (IMAP UTF-8): https://www.rfc-editor.org/rfc/rfc6855.html
