# Troubleshooting

Name the real blocker precisely. Do not improvise a write path when the safe action is read-only.

## Common failure modes

| Symptom | Likely cause | First move |
|---|---|---|
| Empty or missing calendars | Collection not discovered / path changed | `vdirsyncer discover`, then sync |
| Stale times or missing new events | Skipped sync or stale khal cache | Sync; only then consider cache repair |
| Auth / 401 / 403 | Credential or collection ACL problem | Fix account config before retries |
| TLS / certificate errors | Trust chain broken | Fix certificates; do not bypass casually |
| Wrong event changed | Title-only match across calendars | Re-query with window + calendar + UID |
| Brief "fix" after deleting `khal.db` | Cache reset hid the real sync bug | Restore discipline: discover → sync → verify |
| WebDAV URL accepted but calendar fails | URL is not a CalDAV collection | Confirm calendar collection path |

## Cache and local state

- Deleting `khal`'s cache database is a troubleshooting move for stale cache behavior, not a default fix.
- Manual edits under the vdir storage path can desync remote state; treat them as last resort and verify with sync + read-back.
- Keep private base URLs, tokens, and app-specific passwords out of casual summaries.

## Finish criteria when blocked

Report:

1. calendar scope attempted
2. time window
3. exact blocker (`missing vdirsyncer`, `missing khal`, `missing TTY`, `undiscovered collections`, `login failure`, `TLS failure`, or `ambiguous event match`)
4. safest next step that does not destroy data
