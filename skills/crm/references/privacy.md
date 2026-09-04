# Privacy, Consent, and Deletion

CRM data is third-party personal data. Minimize it, suppress before deleting, and keep the suppression proof.

## Before contact

1. Read `<state_root>/crm/do-not-contact.md`.
2. Skip anyone listed, including names the user just typed in chat.
3. Do not add a suppressed address to outreach, enrichment, or export lists meant for campaigns.

## Erasure / unsubscribe request

1. **Suppress first** — add the email (or other identity key) to `do-not-contact.md` with date and reason.
2. **Delete across copies** — CRM boxes, shared contacts row if appropriate, exports the skill controls, and any automation queues.
3. **Keep the suppression hash/entry forever** — deleting the person must not delete their opt-out.
4. Log the request and the copies touched as an artifact.

## Regime notes

| `privacy_regime` | Extra duty |
|---|---|
| `none` | Still honor explicit opt-outs and minimize stored fields |
| `gdpr` | Lawful basis, retention limit, and timely erasure response for EU/UK contacts — treat any EU/UK contact as `gdpr` even if config says otherwise |
| `ccpa` | Honor consumer deletion/disclosure requests for covered California contacts |
| `both` | Apply the stricter overlapping controls |

## Storage boundaries

- No raw API tokens under `<state_root>/`
- No scraping a platform that forbids it
- Enrichment of personal emails is high risk; prefer company-level attributes (`references/experts.md`)
