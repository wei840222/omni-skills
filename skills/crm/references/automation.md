# CRM Automation

Automate only what clean data can survive. Every automation has a named owner in `## System` or the artifact log.

## Safe to automate early

- Bounce / invalid-email flags from the mail provider
- Calendar → interaction metadata (who, when, subject) without body text
- Reminder creation from an existing next-step date
- Nightly export to `<state_root>/crm/exports/`

## Automate only after hygiene

- Enrichment of company-level firmographics
- Sequenced follow-up mail
- Webhook writes back into deals or people
- Lead routing / assignment

Run bounce sweep and merge pass first (`references/hygiene.md`). Automating duplicates or stale first names advertises the rot.

## Logging rules

1. Record the automation's owner and the fields it may write.
2. Prefer metadata sync over full body sync unless the user explicitly consents to store message bodies.
3. Never let an automation bypass `do-not-contact.md`.
4. Disable write-back when fill quality or bounce rate degrades; fix data before re-enabling.
