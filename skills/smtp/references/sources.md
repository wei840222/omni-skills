# Sources - SMTP

Primary references used for protocol, submission, TLS, and deliverability claims.
Live-checked during the 2026-10-18 refactor handoff.

## SMTP protocol and submission

- [RFC 5321 — Simple Mail Transfer Protocol](https://datatracker.ietf.org/doc/html/rfc5321) — core SMTP verbs, reply codes, and relay semantics
- [RFC 6409 — Message Submission for Mail](https://datatracker.ietf.org/doc/html/rfc6409) — submission on port 587 and authenticated submission expectations
- [RFC 8314 — Cleartext Considered Obsolete](https://www.rfc-editor.org/rfc/rfc8314) — prefer TLS for submission; implicit TLS on 465 and STARTTLS guidance

## Domain authentication and placement

- [RFC 7208 — Sender Policy Framework (SPF)](https://datatracker.ietf.org/doc/html/rfc7208)
- [RFC 6376 — DomainKeys Identified Mail (DKIM)](https://datatracker.ietf.org/doc/html/rfc6376)
- [RFC 7489 — Domain-based Message Authentication, Reporting, and Conformance (DMARC)](https://datatracker.ietf.org/doc/html/rfc7489)

## Provider submission docs

- [Google Workspace: SMTP relay / Gmail SMTP settings](https://support.google.com/a/answer/176600) — `smtp.gmail.com`, ports 465/587, app-password / relay constraints
- [Microsoft 365: send email from a device or application](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/how-to-set-up-a-multifunction-device-or-application-to-send-email-using-microsoft-365-or-office-365) — `smtp.office365.com` and modern-auth policy caveats

## Skill format

- [Agent Skills specification](https://agentskills.io/specification) — frontmatter and package layout used by this refactor
