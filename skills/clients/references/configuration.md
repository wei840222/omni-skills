## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/data/clients/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| engagement_default | project \| retainer \| hourly \| value | project | The model proposed first in Engagement Models and priced first in `proposals.md` |
| payment_terms_days | number (0-90) | 30 | Terms written into every proposal and invoice line, and the zero point of the Payment Ladder |
| deposit_pct | number (0-100) | 50 | Share required before work starts (Rule 2); 0 disables the deposit gate |
| status_cadence | weekly \| biweekly \| monthly \| on-milestone | weekly | Frequency of the unasked status note (Rule 6) and the silence threshold in Warning Signals |
| invoicing_day | number (1-28) | 1 | Day of month invoices go out; seeds the recurring row in `## Due` |
| concentration_limit_pct | number (0-100) | 30 | Share of trailing-12-month revenue above which a client is flagged as risk (Rule 5, `portfolio.md`) |
| contract_required | bool | true | Whether work may begin on a written email confirmation instead of a signed document |
| no_go_list | list | none | Sectors or work types to decline outright; applied at the top of qualification in `pipeline.md` |
| rate_card_file | path | none | Long-form rates and packages at `<state_root>/data/clients/<file>`; overrides ad-hoc pricing in proposals |
| voice_file | path | none | How the user writes to clients (register, length, sign-off) at `<state_root>/data/clients/<file>`; overrides the default plain register in every draft |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — invoicing, e-signature, project tracker, time tracking, scheduling and the shared-drive convention the client work runs on; affects where `onboarding.md` sends access and where invoice references point
- **Conventions** — client slug and project-code style, file naming, proposal and status-report structure, invoice reference format; affects every artifact name and the roster
- **Communication** — default channel, response-time promise, meeting length and preferred day, language and formality per client, out-of-hours policy; affects `delivery.md` and every draft
- **Commercial** — rate floor, discount and rush-surcharge policy, retainer rollover rule, kill-fee stance, currency for quotes; affects `pricing.md` and `proposals.md`
- **Risk posture** — hardness on stop-work, tolerance for unsigned starts, appetite for a rescue versus an exit, how many missed payments end a relationship; affects `getting-paid.md` and `difficult-clients.md`
- **Cadence** — portfolio review rhythm, dormant-client re-contact window, rate-review month, testimonial-ask timing; affects the `## Due` table
