# Cybersecurity playbooks

Depth for Quick Reference rows. Keep observed / inferred / recommended separate.
Always satisfy Rule 1 before any live-system action.

## Incident response (after first hour)

Continue from SKILL.md "First hour". After volatile preserve + identity/network containment:

1. Expand scope with a written hypothesis list; promote only with Confirmed/Likely evidence.
2. Hunt persistence before recovery: inbox rules, OAuth grants, scheduled tasks/services, SSH keys,
   new local/cloud accounts, group memberships, API keys, mail forwarding, device registrations.
3. Eradication: rebuild compromised hosts from known-good when hands-on-keyboard is Confirmed;
   keep disk images in the case store, not under `<state_root>/`.
4. Recovery gates: identity eviction complete, crown-jewel access reviewed, detections for the
   observed path enabled with an owner, backups validated offline.
5. Post-incident review: timeline, detection gaps, control that would have removed the path,
   owners and due dates — write via `assets/data-templates.md`.

## Ransomware

- Do not reboot or reimage as the first move; volatile state and encryption progress matter.
- Size **encryption impact** and **exfiltration/extortion** as separate claims.
- Prefer network isolation + identity eviction; validate an **immutable/offline restore** before
  any payment discussion.
- Paying extortion: no technical consensus; decryptors are often partial; stolen data is not
  deleted by payment; sanctions exposure is a counsel decision (`sources.md`).
- Backups reachable with production credentials are not backups.

## Phishing / BEC

- Verify Authentication-Results (SPF/DKIM/DMARC) and full headers before trusting display names.
- Treat the **mailbox** as the incident: rules that file to RSS/Archive/Deleted, forwarding,
  delegates, and OAuth/connected apps across the tenant.
- Payment diversion: freeze outbound payments on the affected process; verify payee changes
  out-of-band; preserve mail and ticket evidence.
- User reporting rate beats click-rate shame; one-click report buttons are a control.

## Identity

Full eviction after suspected credential or session theft (password reset alone is insufficient):

1. Revoke browser sessions and refresh / primary refresh tokens
2. Revoke app passwords, personal access tokens, API keys, and service principal secrets touched
3. Review and revoke risky OAuth consent grants and mail-send permissions
4. Reset password **and** step-up MFA; prefer phishing-resistant factors (FIDO2/WebAuthn/passkeys)
5. Clear device registration / trusted device marks the actor may have used
6. Inspect mail forwarding, inbox rules, and mailbox delegates
7. Review group membership and standing admin roles for the identity and peers
8. Hunt lateral use of the same secret on other apps

Disable legacy/non-MFA auth paths that enabled password spray. Service accounts must not
authenticate interactively from workstations.

## Forensics

- Order of volatility (RFC 3227): memory → network state → running processes → disk → remote logs.
- Capture short-retention cloud/SaaS audit logs early; many cannot be obtained retroactively.
- Chain of custody: who handled what, when, hash, where stored (case store, not `<state_root>/`).
- Clearing security logs or stopping EDR is treated as Confirmed hostile until disproved.

## Vulnerabilities

Priority gate (Rule 4):

1. In CISA KEV → fix on the KEV/BOD clock (federal two-week BOD 22-01 is a defensible default)
2. Else EPSS ≥ ~0.1 **and** internet-reachable (or authenticated path to crown jewels)
3. Else crown-jewel reachability even if score is medium
4. Else CVSS-informed backlog under `remediation_sla_days`

Cyentia/FIRST EPSS research: only a small single-digit percent of CVEs are ever observed
exploited in the wild — score the wound (CVSS) separately from the swing probability (EPSS)
and the fact of exploitation (KEV).

## Design review

Before controls: inventory assets, entry points, trust boundaries, and attacker paths.
Name the path each proposed control removes. Unknown asset/entry/impact ⇒ provisional conclusion.

## Appsec

Order review by classes that drive real incidents: injection, authZ flaws, SSRF, secret leakage,
insecure deserialization, dependency reachability, and broken access on admin/API routes.
Prefer minimal diffs and regression tests; deep line-by-line repair may hand off to
`security-best-practices`.

## Detection

- Log source exists and heartbeats before writing the rule.
- Every rule states data source, analyst response, and precision `TP/(TP+FP)` over ~30 days.
- Below ~10% precision: tune or retire.
- Map coverage to techniques (e.g. ATT&CK), not enabled-rule count.
- Sudden silence on a technique is a pipeline failure until proven otherwise.

## Network

- Discover exposed services before adding complexity.
- Smallest segmentation that breaks the path; egress filter + DNS logging for C2/exfil.
- Allow-all outbound 443 is C2-permissive by construction.
- OT/medical/legacy: prefer passive discovery; aggressive scans can become the incident.
- Concrete host/cloud rule syntax → `firewall` skill when that is the remaining work.

## Cloud / SaaS

- Identity-first: admin separation, phishing-resistant MFA, hard boundaries on role assumption.
- Inventory keys, public data, and privilege paths before trusting provider "secure by default".
- Enable the audit logs you cannot reconstruct later (CloudTrail-class, Entra/M365 unified audit,
  Admin Activity, etc. per provider).
- Public storage and over-broad service accounts are crown-jewel adjacency.

## Endpoints

- Per-OS baseline; EDR in **block** mode with an owned on-call path.
- Detect-only EDR is a 3am alert without an actor.
- Unique local admin secrets per host; no shared service-account interactive logon.
- BYOD and USB policy must match crown-jewel exposure.

## Supply chain

- Reachability over raw CVE counts on dependencies.
- Build integrity: pinned versions, signed artifacts, reviewed provenance where available.
- Vendor tier by data held + access path; a vendor breach is your incident for their blast radius.
- Acquired repos get the same identity and secret scan as internal code on day one.

## Compliance

- Map controls to **evidence**, not binder chapters.
- Notification clocks are legal deadlines owned with counsel (see SKILL Notification table via
  domain clocks retained below and `sources.md`).
- Engaging non-panel IR before insurer notice can void coverage — check policy language.

### Notification clocks (technical fact pattern)

| Regime | Clock | Starts at |
|---|---|---|
| GDPR | 72h to authority; data subjects without undue delay if high risk | Awareness of personal-data breach |
| NIS2 | 24h early warning, 72h notification, 1 month final | Awareness of significant incident |
| DORA | Initial within 4h of major classification and ≤24h from awareness; intermediate 72h; final 1 month | Classification bounded by awareness |
| SEC Item 1.05 | Form 8-K within 4 business days of materiality determination | Materiality determination without unreasonable delay |
| HIPAA | Individuals 60 days; HHS 60 days if ≥500 | Discovery |
| PCI DSS | Acquirer/brands per contract — treat as immediate | Suspicion of CHD compromise |
| US state / other | Often 30–45 days from determination | Discovery or determination |
| Cyber insurance | Often days; panel counsel/IR | Awareness |
| Customer DPAs | Often 24–72h — read before the incident | Contractual trigger |

## Authorization

Before any live touch: (1) system owner, (2) written scope/exclusions, (3) allowed disruption.
`authorized_scope_file` under `<state_root>/` is the long form. "Go ahead" on someone else's
system is not scope. Fallbacks when incomplete: lab reproduction, read-only review, tabletop,
detection logic, remediation design — never "creative" expansion into ambiguity.

## Program build

Sequence by **attack path removed per unit effort**, not framework chapter order. Identity and
backup/restore usually outrank low-signal tool sprawl for small teams. Findings feed a backlog
with owners; a pentest is a sample, not the program.
