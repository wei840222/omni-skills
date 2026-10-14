# Sources (Gate 6)

Full URLs checked while refactoring this skill (2026-10-14). Re-open before restating
statutes, KEV/EPSS figures, MFA guidance, or volatility order.

## Agent skill format

- Agent Skills specification: https://agentskills.io/specification
- Agent Skills best practices: https://agentskills.io/skill-creation/best-practices
- Agent Skills optimizing descriptions: https://agentskills.io/skill-creation/optimizing-descriptions
- skills-ref validator: https://github.com/agentskills/agentskills/tree/main/skills-ref

## Vulnerability prioritization

- CISA Known Exploited Vulnerabilities catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
  Takeaways: KEV is evidence of in-the-wild exploitation used for prioritization; BOD bindings apply to federal civilian executive branch and are a common benchmark elsewhere.
- CISA BOD 22-01 (reducing risk of known exploited vulnerabilities): https://www.cisa.gov/news-events/directives/bod-22-01-reducing-risk-known-exploited-vulnerabilities
  Takeaways: two-week remediation expectation for KEV items in scope of the directive.
- FIRST EPSS: https://www.first.org/epss/
  Takeaways: exploit prediction scoring; use with exposure, not as a sole SLA.
- FIRST EPSS model / data: https://www.first.org/epss/model
- CVSS v3.1 specification (FIRST): https://www.first.org/cvss/v3-1/specification-document
  Takeaways: CVSS measures severity of the vulnerability, not likelihood of exploitation.

## Identity and authentication

- NIST SP 800-63B-4 Digital Identity Guidelines (authentication): https://pages.nist.gov/800-63-4/sp800-63b.html
  Takeaways: prefer phishing-resistant authenticators; avoid routine password expiration as primary control; screen against breached-password lists.
- Verizon DBIR (human element context; re-check latest edition before quoting percents): https://www.verizon.com/business/resources/reports/dbir/

## Forensics and evidence

- RFC 3227 Guidelines for Evidence Collection and Archiving: https://www.rfc-editor.org/rfc/rfc3227
  Takeaways: order of volatility — collect more volatile data first.

## Notification and regulatory clocks (counsel-owned; technical awareness timestamps)

- GDPR Art. 33 notification: https://gdpr-info.eu/art-33-gdpr/
  Takeaways: supervisory authority without undue delay and, where feasible, within 72 hours of awareness.
- NIS2 Commission overview: https://digital-strategy.ec.europa.eu/en/policies/nis2-directive
- DORA overview (EU digital operational resilience): https://finance.ec.europa.eu/digital-finance/digital-operational-resilience-act-dora_en
- SEC cybersecurity incident disclosure (Item 1.05 context): https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/cybersecurity-risk-management-strategy-governance-incident-disclosure-small-entity
- HHS HIPAA breach notification rule: https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html
- PCI DSS: https://www.pcisecuritystandards.org/

## Ransomware / backups (defensive)

- CISA Stop Ransomware: https://www.cisa.gov/stopransomware
  Takeaways: isolate, preserve, report; backups and tested restores reduce extortion leverage.

## Mail authentication

- DMARC overview (IETF): https://datatracker.ietf.org/doc/html/rfc7489
