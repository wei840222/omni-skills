# Compliance programs

Load when building a compliance program, policies, or regulatory calendar.

## Pipeline

```text
regime inventory → obligations → owner → cadence → evidence
```

1. **Regime inventory** — from `compliance_regimes` plus contracts and markets actually touched (GDPR, CCPA, HIPAA, PCI, SOC 2, ISO 27001, COPPA, FERPA, sector rules)
2. **Obligations** — concrete duties, not slogan policies
3. **Owner** — named human role, not "the company"
4. **Cadence** — review/refresh dates into `## Due`
5. **Evidence** — what proves the control existed on a date (logs, training records, signed policies, tickets)

## Policy drafting rules

- Write what the organization **does**, not what it hopes to do
- Version and date every policy; pin URL policies in customer contracts
- Map each policy clause to an owner and an evidence artifact
- Security questionnaire answers must match live controls (`references/diligence.md`)

## Small-team reality

Segregate create-vendor / pay / reconcile style duties even when one person wears two hats — document compensating reviews. Compliance theater without evidence fails the first diligence request.
