# Compliance — Enterprise

Compliance is a design input, not a post-ship checkbox. Identify the regime, the data class, and the evidence an auditor will request before changing storage, access, or residency.

## Framework quick reference

| Framework | Typical scope | Design implications |
|-----------|---------------|---------------------|
| SOC 2 | Service organizations | Access control, encryption, monitoring, change evidence |
| PCI DSS | Payment card data | Network segmentation, encryption, immutable audit |
| HIPAA | Protected health information | Access logs, encryption, BAAs, minimum necessary |
| GDPR | EU personal data | Lawful basis, deletion/portability, residency routing |
| SOX | Public-company financial controls | Segregation of duties, auditable change trails |

Primary entry points live in `sources.md` (AICPA SOC 2, PCI SSC library, EUR-Lex GDPR, NIST SP 800-53, OWASP ASVS, CSA CCM). Re-check live pages before locking a claim; statutes and attestations change.

## Data classification

Classify before building:

| Level | Examples | Baseline controls |
|-------|----------|-------------------|
| Public | Marketing content | Integrity / availability as needed |
| Internal | Employee process docs | Authentication, least privilege |
| Confidential | Customer business data | Encryption in transit/at rest, audit |
| Restricted | PII, PHI, PCI | Full control set, DLP, retention limits |

An "internal tool" that stores Restricted data still needs Restricted controls. Internal network placement is not an exemption.

## Audit trail minimum

Every material compliance regime expects:

- **Who** — authenticated identity
- **What** — action performed
- **When** — timestamp with timezone
- **Where** — source IP / service
- **Result** — success or failure

Keep audit logs immutable for the retention window; deletable audit stores defeat the control.

## Data residency

Localization rules (for example GDPR and other regional regimes) often require regional stores plus a routing layer instead of a single global database of personal data.

```text
Before: [Single Global DB]
After:  [EU DB] [US DB] [APAC DB] + routing / residency policy
```

State the residency rule in the ADR and in the data-flow diagram reviewers will ask for.

## Positive traps (what to do instead)

| Failure mode | Do this |
|--------------|---------|
| Logging PII in plaintext | Redact or tokenize; store sensitive fields encrypted |
| Unbounded retention | Define retention limits and deletion jobs with owners |
| "Internal means exempt" | Apply the data class, not the network label |
| Consent buried in ToS | Surface explicit consent where GDPR (or local law) requires it |
| Editable audit logs | Append-only / WORM storage for the retention window |

## Handoffs

- SaaS buyer questionnaires, SSO/SCIM, and DPA packaging → `saas`
- Deep control catalogs and threat models → `cybersecurity` / `security-best-practices`
- Pipeline evidence and change tickets → `devops`
