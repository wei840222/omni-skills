# Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/crm/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| crm_tool | files \| sqlite \| notion \| airtable \| hubspot \| pipedrive \| attio \| folk \| salesforce \| other | files | The system of record every write targets (Rule 1) and which section of `references/tools.md` applies; while unset, name the assumed target before writing |
| pipeline_stages | list | Lead, Qualified, Proposal, Negotiation, Closed | Replaces the stage table in `references/pipeline.md`; every stage still needs one verifiable exit criterion |
| stale_days | number (days) | 90 | Recency threshold for the overdue sweep in `references/followup.md`; applies to contacts without an open deal |
| stall_days | number (days) | 21 | Days in one stage before a deal joins the stalled list at review (Rule 3) |
| email_logging | manual \| bcc \| sync | bcc | Whether interactions are typed, captured via a BCC address, or pulled by an inbox integration (`references/automation.md`) |
| privacy_regime | none \| gdpr \| ccpa \| both | none | Which retention, consent and response-window rules apply in `references/privacy.md`; any EU/UK contact makes this `gdpr` regardless of the stored value |
| review_day | text (weekday) \| none | Monday | Day the pipeline review lands in the `## Due` table and what "this week" means in `references/metrics.md` |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Conventions** — tag vocabulary, naming of stages and sources, required-vs-optional fields, id scheme, how organizations are keyed — affects `references/schema.md` and every record you create
- **Tooling** — where the data physically lives, export format and cadence, spreadsheet vs database for one-off analysis — affects `references/tools.md` and `references/import.md`
- **Reporting** — which metrics matter, review cadence, currency and rounding, whether forecasts are weighted or commit-based — affects `references/metrics.md`
- **Safety posture** — confirmation before bulk edits, merges and deletes; whether hard delete is allowed at all; appetite for third-party enrichment and scraping — affects `references/hygiene.md` and Output Gates
- **Relationship posture** — how aggressive follow-up is, personal notes vs templates, what counts as a reason to reach out, tiering rules — affects `references/followup.md`
- **Integrations** — inbox and calendar providers, form and enrichment vendors, which systems may write back — affects `references/automation.md`
