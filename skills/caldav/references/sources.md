# Sources - CalDAV skill

Last checked: 2026-09-18

Use these primary references when verifying protocol behavior, client commands, or server collection expectations. Prefer the live page over memorized flags.

## Protocol and standards
- CalConnect CalDAV resource guide — protocol orientation and related specs via https://www.calconnect.org/resources/caldav
- RFC 4791 (CalDAV) — calendar extensions to WebDAV via https://www.rfc-editor.org/rfc/rfc4791
- RFC 5545 (iCalendar) — event data model underlying local `.ics` storage via https://www.rfc-editor.org/rfc/rfc5545

## Local client stack
- vdirsyncer documentation — discover/sync pairs, storage backends, and conflict handling via https://vdirsyncer.pimutils.org/en/stable/
- khal documentation — non-interactive listing/creation limits and interactive edit behavior via https://khal.readthedocs.io/en/latest/

## Common server families (verify current setup docs per host)
- Nextcloud Calendar / CalDAV docs — collection paths and client setup via https://docs.nextcloud.com/server/latest/user_manual/en/groupware/calendar.html
- Fastmail CalDAV help — account calendar URLs and app-password expectations via https://www.fastmail.help/hc/en-us/articles/1500000279941-Calendars-overview

## Operational note
Provider base URLs, app-password rules, and client flag surfaces change. Re-open the installed `vdirsyncer`/`khal` docs and the user's server help page before changing auth, conflict policy, or storage paths.
