# Research Sources — Email Marketing

Verified sources used to ground bulk-sender, unsubscribe, and compliance guidance in this package. Prefer primary vendor/standards pages over secondary blogs when refreshing knowledge.

## Bulk-sender and mailbox-provider requirements

- **Google Gmail bulk sender guidelines** — authentication (SPF/DKIM/DMARC), one-click unsubscribe, and spam-rate expectations for bulk senders via https://support.google.com/mail/answer/81126
- **Google Email sender guidelines (Help for admins)** — technical requirements overview via https://support.google.com/a/answer/81126
- **Yahoo Sender Best Practices / bulk sender requirements** — authentication and complaint handling expectations via https://senders.yahooinc.com/best-practices/

## Unsubscribe standards

- **RFC 8058** — Signaling One-Click Functionality for List-Unsubscribe via https://www.rfc-editor.org/rfc/rfc8058
- **RFC 2369** — List-Unsubscribe header field via https://www.rfc-editor.org/rfc/rfc2369

## Authentication standards

- **DMARC (RFC 7489)** — domain-based message authentication, reporting, and conformance via https://www.rfc-editor.org/rfc/rfc7489
- **DKIM (RFC 6376)** — signature basics via https://www.rfc-editor.org/rfc/rfc6376

## Legal / consumer protection baselines (operational awareness, not legal advice)

- **FTC CAN-SPAM Act: A Compliance Guide for Business** — commercial email identity, postal address, and opt-out rules via https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- **European Commission GDPR overview** — personal data and consent principles via https://commission.europa.eu/law/law-topic/data-protection_en

## Deliverability operations references

- **Google Postmaster Tools** — domain reputation and spam-rate monitoring via https://gmail.com/postmaster/
- **MXToolbox blacklist / diagnostic tools** — operational reputation checks via https://mxtoolbox.com/

## Knowledge updates applied in this refactor

- Elevated SPF/DKIM/DMARC from “best practice” to **mandatory bulk-sender baseline** aligned with 2024+ Gmail/Yahoo guidance.
- Replaced soft “unsubscribe within 10 days preferred” framing with **one-click unsubscribe (RFC 8058)** as a bulk-sender requirement on major providers.
- Set explicit spam-complaint guardrail: **&lt;0.3% hard ceiling**, **≤0.1% target**.
- Retained organic-list growth and anti-purchased-list rule as reputation-critical, not optional ethics color.
