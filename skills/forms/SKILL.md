---
name: forms
description: >
  Design, validate, and ship web or app forms: field selection by use case,
  progressive multi-step flows, client+server validation, conditional logic,
  accessibility, no-code vs code platforms, webhooks/CRM handoffs, and
  self-hosted options. Use when building lead, survey, application, feedback,
  or registration forms; choosing Typeform/Tally/Google Forms vs React Hook
  Form/Flutter; or hardening file upload and spam controls. Prefer `html` for
  markup-only bugs, `react`/`flutter` for framework mechanics, `webhook` for
  receiver security, and `crm` once submissions enter a sales pipeline.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📝"}'
  related-skills: '{"html":"Semantic markup, labels, autofill, and a11y when the issue is HTML form structure rather than product design.","react":"React Hook Form, controlled inputs, and component state once the stack is React.","flutter":"Flutter form widgets and builders once the client is a Flutter app.","frontend":"Broader UI layout and design-system polish beyond form field logic.","webhook":"Secure webhook receivers, signatures, and idempotency after form submit delivery.","crm":"Pipeline, contacts, and deal hygiene once form leads land in a CRM."}'
---

# Forms

Design **forms that people finish**: right fields for the job, progressive
disclosure, validation that helps instead of punishes, accessible controls, and
a clear path from submit to storage or CRM.

This skill is **stateless by default** for one-shot design advice. Optional
templates and local notes live under a resolved `<state_root>` only when the
user wants continuity across sessions. Never store real PII submissions,
API keys, or webhook secrets in the skill package.

## State location

Form templates and optional local notes may exist in `<workspace>/forms/`,
`<workspace>/memory/forms/`, or `~/forms/`. Before reading or writing state,
resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/forms/`, `<workspace>/memory/forms/`, `~/forms/`.
3. If several candidate directories exist, use only the highest-precedence one and
   report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create
   `<workspace>/forms/` by default.
5. If the host cannot supply `<workspace>`, read an existing `~/forms/` only;
   otherwise ask for a state root before creating data.

Use the selected `<state_root>` for every state operation in this skill.
Typical layout (create children only when needed):

- `<state_root>/templates/` — reusable form definitions (JSON/YAML)
- `<state_root>/feedback/` — what converts or fails (notes, not live PII dumps)
- Self-hosted submission stores belong to the deployed app/database, not this package

## When to use

- Choose fields and steps for lead capture, surveys, applications, feedback, registration
- Pick no-code (Google Forms, Typeform, Tally, Jotform) vs code (RHF+Zod, Flutter) vs self-host
- Add validation, conditional logic, honeypot/spam controls, file upload limits
- Wire submit → webhook / email / CRM without leaking secrets
- Check accessibility labels, errors, and mobile keyboard behavior

Prefer `html` when the bug is markup, labels, or native constraint validation.
Prefer `react` / `flutter` when the remaining work is framework form APIs.
Prefer `webhook` when designing the receiver signature and retry contract.
Prefer `crm` after the lead is already a contact/deal problem.

## Safety order (always)

1. Classify data sensitivity (public survey vs health/finance/HR) before choosing
   a SaaS host or self-host path.
2. Always pair client validation with **server-side** checks; never trust the browser alone.
3. Do not store real respondent PII, resumes, or payment data inside skill files or chat logs meant for reuse.
4. Keep webhook secrets, API tokens, and SMTP credentials out of examples; use unmistakable placeholders.
5. For EU/UK personal data collection, require a clear privacy notice and lawful basis (e.g. consent checkbox linking the privacy policy) before go-live advice.
6. File uploads need type allowlists, size caps, and malware scanning on the server path—not client filters alone.

## Quick workflow

1. Lock **use case** (lead / survey / application / feedback / registration), audience, and stack preference.
2. Start minimal fields; add steps only when length or sensitivity demands it.
3. Load the smallest reference for the task; do not dump every platform table first.
4. Define validation, errors, success state, and spam controls before polish styling.
5. Choose delivery (Sheets, webhook, CRM, self-host DB) and verify the security path.
6. Hand off to `html`, `react`, `flutter`, `webhook`, or `crm` when the remaining work leaves form product design.

## Routing

| Need | File |
| --- | --- |
| Core design rules and conversion hygiene | `references/domain.md` |
| Field types by use case | `references/types.md` |
| Platform comparison (no-code / self-host / libraries) | `references/platforms.md` |
| Validation patterns | `references/validation.md` |
| Code sketches (React, Flutter, HTML) | `references/code.md` |
| Webhooks, email, CRM integrations | `references/integrations.md` |
| Self-hosted options | `references/selfhosted.md` |
| State tree details | `references/state.md` |
| Verified source URLs (Gate 6) | `references/sources.md` |

## Core rules (summary)

1. Ask use case before suggesting fields — lead form ≠ job application.
2. Progressive disclosure: start minimal; reveal complexity only when needed.
3. Mobile-first: every form must work on a phone keyboard.
4. Keep lead-capture short (aim ≤7 fields); each extra field tends to hurt completion.
5. Prefer multi-step over one long page when there are 5+ fields.
6. Validate on blur **and** on the server — immediate feedback plus authoritative checks.
7. Always include clear labels, error states, and success confirmation.
8. GDPR/privacy checkbox when collecting EU personal data — link the privacy policy.
9. Prefer honeypot + rate limits over CAPTCHA when abuse is low; escalate when attacked.
10. File uploads need type + size limits and server-side enforcement.
11. Conditional logic pattern: `IF field=value THEN show/hide field` (implement per platform).
12. Test on real devices — emulators miss keyboard and autofill quirks.

Load `references/domain.md` when these rules drive the recommendation.
Load `references/sources.md` before restating product limits, APIs, or legal claims.
