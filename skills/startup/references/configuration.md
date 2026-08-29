## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| stage | pre-pmf \| post-pmf \| unknown | unknown | Selects which priority set arbitrates every recommendation and agent synthesis |
| business_model | b2b-saas \| b2c \| marketplace \| unknown | unknown | Switches which benchmarks apply (burn multiple and NRR are SaaS-native; marketplaces delay monetization) |
| runway_months | number (0-36) | none | Feeds the default-alive check and raise-timing advice |
| risk_posture | bootstrap \| venture | venture | Arbitrates the raise-vs-profitability defaults in Where Experts Disagree |

Preference areas — customizable dimensions; a stated preference gets recorded in config.yaml and applied:

- **Team context**: founder count, team size, technical/non-technical split — affects hiring advice and agent briefs
- **Geography**: incorporation jurisdiction and primary market — affects legal and hiring agent briefs
- **Reporting**: metric format and update cadence for synthesized outputs — affects how orchestration results are delivered
