# Newsletter sources

Load when citing deliverability thresholds, bulk-sender rules, one-click unsubscribe mechanics, commercial-email law, or Agent Skills format. Keep original windows and scope. Re-check live URLs before the user changes DNS, ESP contracts, or compliance copy.

## Agent Skills format

| Source | URL | Use |
| --- | --- | --- |
| Agent Skills specification | https://agentskills.io/specification | Package format, progressive disclosure, metadata shape |
| Best practices for skill creators | https://agentskills.io/skill-creation/best-practices | Scope and calibration |
| Optimizing skill descriptions | https://agentskills.io/skill-creation/optimizing-descriptions | Trigger-rich descriptions |

## Gmail / Google sender requirements

| Source | URL | Notes (refactor-time read) |
| --- | --- | --- |
| Gmail Email sender guidelines | https://support.google.com/mail/answer/81126 | Personal Gmail delivery requirements. All senders: SPF **or** DKIM; valid forward/reverse DNS; TLS. **≥ ~5,000 messages/day** path: SPF + DKIM + DMARC; DMARC alignment; one-click unsubscribe + visible link for marketing/subscribed mail. Guidelines describe Feb 2024 requirement window. |
| Gmail Email sender guidelines FAQ | https://support.google.com/mail/answer/14229414 | Bulk sender ≈ ~5,000+/day to personal Gmail; spam rate **> 0.3%** called out; missing DMARC `p=none` minimum and missing one-click unsubscribe affect support/mitigations; unsubscribe honor window discussed (**48 hours** class guidance); RFC 8058 header pair described; enforcement ramps called out including Nov 2025 non-compliant traffic pressure. |

## Yahoo sender requirements

| Source | URL | Notes (refactor-time read) |
| --- | --- | --- |
| Yahoo Sender Best Practices | https://senders.yahooinc.com/best-practices/ | All senders: SPF or DKIM; spam rate **below 0.3%**; valid forward/reverse DNS; RFC 5321/5322. Bulk: SPF+DKIM; DMARC at least `p=none` with pass/alignment; one-click List-Unsubscribe (RFC 8058 POST preferred); visible unsub link; honor unsubscribes within **2 days**. References CAN-SPAM compliance. Enforcement noted from Feb 2024 with gradual rollout language. |

## One-click unsubscribe standard

| Source | URL | Notes |
| --- | --- | --- |
| RFC 8058 — Signaling One-Click Functionality for List Email Headers | https://datatracker.ietf.org/doc/html/rfc8058 | `List-Unsubscribe` + `List-Unsubscribe-Post: List-Unsubscribe=One-Click`; POST semantics to avoid accidental GET unsubscribes by scanners |
| RFC 8058 plain text | https://www.rfc-editor.org/rfc/rfc8058.txt | Same standard, plain-text mirror |

## US commercial email law (scope-limited)

| Source | URL | Notes |
| --- | --- | --- |
| FTC — CAN-SPAM Act: A Compliance Guide for Business | https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business | Applies to **commercial** messages (not only bulk). Key themes: accurate headers, non-deceptive subjects, disclose ads when required, include valid **physical postal address**, provide working opt-out and honor it. Not a substitute for counsel; other countries have separate regimes (e.g. GDPR/ePrivacy) not fully covered here. |

## Citation rules

1. Quote complaint caps (**0.3%**), bulk volume (**~5,000/day**), and unsubscribe SLAs only with the provider page + date window.
2. Do not treat “40%+ open rate is good” as an official benchmark — that heuristic is product guidance and is weakened by mail-client privacy proxies.
3. Never cite blocked or 404 URLs from memory; log failures below.
4. Legal claims outside the FTC CAN-SPAM guide require a jurisdiction-specific primary source before advice hardens.

## Failed or blocked lookups this refactor

| URL | Result |
| --- | --- |
| https://blog.google/products/gmail/gmail-security-authentication-spam-protection-2024/ | HTTP 404 at refactor time — do not cite |
| https://www.m3aawg.org/sites/default/files/m3aawg-sending-domain-best-practices-2018-11.pdf | HTTP 404 at refactor time — Yahoo still references M3AAWG conceptually; use Yahoo page + Gmail pages instead of the dead PDF path |
| https://www.legislation.gov.uk/uksi/2003/2426/contents/made | Timeout in refactor environment — do not claim UK PECR details from memory |
