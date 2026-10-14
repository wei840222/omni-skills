# Cybersecurity domain

Load this file for configuration defaults, operational traps, and contested judgement calls.
Play depth lives in `playbooks.md`. Citation URLs live in `sources.md`.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/cybersecurity/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| org_profile | solo \| startup \| smb \| enterprise \| msp | smb | Scale and sequence of everything in `references/playbooks.md` (program), and whether advice assumes a security owner exists |
| report_audience | practitioner \| mixed \| executive | mixed | Depth, severity language and structure of every finding and summary (`references/reporting.md`) |
| containment_bias | evidence-first \| recovery-first | evidence-first | Rule 2's ordering: whether volatile evidence is captured before isolation, reimaging or restore (`references/playbooks.md` (incident response)) |
| severity_scale | cvss \| kev-epss \| owner-defined | kev-epss | Which prioritization formula Rule 4 and `references/playbooks.md` (vulnerabilities) apply, and how findings are labelled |
| remediation_sla_days | list (critical/high/medium/low) | 7/30/90/next cycle | The due date attached to every finding (Rule 6) and the overdue rows in the `## Due` table |
| siem_platform | splunk \| sentinel \| elastic \| chronicle \| opensearch \| none | none | Dialect of every detection in `references/playbooks.md` (detection); `none` produces vendor-neutral pseudo-rules plus the fields they need |
| edr_platform | defender \| crowdstrike \| sentinelone \| elastic \| osquery \| none | none | Which containment lever and which telemetry `references/playbooks.md` (incident response) and `references/playbooks.md` (endpoints) assume |
| primary_cloud | aws \| azure \| gcp \| on-prem \| multi | multi | Control set, log sources and identity model used by `references/playbooks.md` (cloud) |
| compliance_regime | list: none \| soc2 \| iso27001 \| pci \| hipaa \| gdpr \| nis2 \| dora | none | Mandatory controls, retention minimums, evidence format, and which Notification Clocks rows apply |
| authorized_scope_file | path | none | Long text at `<state_root>/cybersecurity/<file>.md` listing systems, exclusions and allowed disruption; the Rule 1 gate reads it |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — scanner, ticketing system, secrets manager, MDM, mail gateway, vulnerability and asset sources of truth — affects where every finding and every log query is expressed
- **Conventions** — finding id scheme, severity wording, ticket titles, naming of assets and environments, report template — affects `references/reporting.md` and every artifact written
- **Platform** — identity provider, OS mix across the fleet, on-prem versus cloud weighting, OT/ICS or medical devices in scope — affects `references/playbooks.md` (identity), `references/playbooks.md` (endpoints) and which scans are safe at all
- **Safety posture** — whether the agent may run any command against live systems or only describe them, appetite for noisy or attacker-visible actions, approval chain for containment — affects Rule 1, Output Gates and `references/playbooks.md` (authorization)
- **Exclusions** — systems never to touch, third parties out of scope, jurisdictions with distinct rules, data the user will not have summarized — affects the authorization gate and evidence handling
- **Cadence** — access reviews, key rotation, restore drills, tabletops, pentests, phishing simulations, vendor reassessment — every accepted cadence becomes a row in the `## Due` table of `memory.md`
- **Output register** — timeline-first versus recommendation-first, how much attacker detail to include, whether to name techniques by ATT&CK id — affects every answer's shape

## Traps

| Trap | Why it fails | Do instead |
|------|-------------|------------|
| Reimaging or rebooting the first infected host | Deletes memory, running processes and the network state that prove scope — you now have one clean machine and no idea how many others are dirty | Isolate at the network layer first, capture volatile state, then rebuild (Rule 2) |
| Password reset as containment | Sessions, refresh tokens, app passwords, API keys and consent grants all survive it | The full eviction list in `references/playbooks.md` (identity) (Rule 5) |
| Blocking the C2 address and calling it eradicated | Infrastructure is disposable and the persistence is still installed | Hunt persistence before declaring recovery (`references/playbooks.md` (incident response)) |
| Patching the exploited vulnerability and stopping there | The patch closes the door the attacker used to come in, not the one they left open | Patch, then hunt for accounts, keys, tasks and grants created since the intrusion |
| Cleaning a compromised host instead of rebuilding it | You are betting your judgement against an operator who chose their persistence deliberately | Rebuild from known-good; keep the disk image for analysis |
| Prioritizing purely by CVSS | Optimizes for wound severity while ignoring whether anyone is swinging | KEV, then EPSS with exposure, then crown-jewel reachability (Rule 4) |
| Turning on every detection the vendor ships | Precision collapses, the queue is abandoned, and the real alert arrives into a queue nobody reads | Deploy by technique with a response action and a precision target (Rule 8) |
| Deleting the malware sample "to be safe" | Destroys the only thing that identifies the actor and the campaign | Preserve in the case store; never in `<state_root>/` (`references/playbooks.md` (forensics)) |
| "Just turn on MFA" | SMS and push are phishable, and AiTM proxies defeat both | Phishing-resistant factors on the accounts that matter first (Rule 7) |
| Notifying customers or posting publicly before counsel and the insurer | Voids coverage, contradicts the later legal filing, and burns the one credible statement you get to make | Fact pattern to counsel, counsel owns the wording (Notification Clocks) |
| Treating the pentest report as the security program | A pentest samples one path at one moment; the report's absence of findings is not evidence of anything | Findings feed the backlog; the program is built from attack paths (`references/playbooks.md` (program)) |
| Aggressive scanning of OT, medical or legacy devices | Some fail on a single unexpected packet — the outage becomes your incident | Passive discovery and vendor guidance for those segments (`references/playbooks.md` (network)) |
| Severity inflated to force attention | Works twice; after that every finding is discounted, including the real one | Argue exploitability, exposure and impact, and let a medium be a medium (`references/reporting.md`) |
| Risk accepted verbally | Reappears in the next audit with nobody's name on it | A dated acceptance with an owner and an expiry in `## Risk Accepted` (`findings.md` once split), plus its `## Due` row (Rule 6) |
| Analysis of a system whose ownership nobody has confirmed | Legal exposure for the user and for you, whatever the intention | The authorization gate and its fallbacks (Rule 1) |

## Where Experts Disagree

- **Isolate immediately versus watch to learn scope.** Watching gives you the true footprint and avoids tipping off an operator who would then detonate; isolating stops the damage now. The frontier is who you face: commodity intrusion or a ticking encryption timer → isolate; a quiet, targeted actor with a mature team watching → observe under a strict, written time box.
- **Paying extortion.** No consensus exists. What is not disputed: the decryptor is slow and partial so you restore from backups anyway for a meaningful share of systems, payment does not delete stolen data, and paying an entity under sanctions is itself a legal exposure that counsel — not the technical team — must clear (`references/playbooks.md` (ransomware)).
- **CVSS-driven SLAs versus risk-based prioritization.** Auditors reward a simple severity-to-days table and it is easy to defend; risk-based ranking fixes more real exposure per hour of engineering. Common resolution: keep the CVSS table as the contractual floor, and run KEV/EPSS/exposure as the working order inside it.
- **In-house detection versus MDR.** Below roughly the size where you can staff a 24/7 rota — which needs several analysts, not one — coverage is the argument and MDR wins. Above it, context is the argument and in-house wins. The hybrid that works is MDR for triage with in-house owning detection engineering and response decisions.
- **Periodic password rotation.** NIST SP 800-63B removed routine expiry in favour of screening against breached-password lists and phishing-resistant factors; several compliance regimes and auditors still expect a rotation policy. Where an auditor demands it, comply with the letter and put the actual defence into MFA and breach-list screening.

## State boxes (after `<state_root>` resolve)

| Path | Role | Create when |
|---|---|---|
| `<state_root>/config.yaml` | Declared preferences | First durable preference |
| `<state_root>/memory.md` | Observed context, Boxes, Due, Scope | First observed state |
| `<state_root>/assets.md` | Environment past split threshold | ~15 env entries |
| `<state_root>/findings.md` | Findings past split | ~15 findings |
| `<state_root>/detections.md` | Detection inventory past split | ~15 rules |
| `<state_root>/vendors.md` | Vendor assessments past split | ~15 vendors |
| `<state_root>/incidents/<year>.md` | Incident timeline | First incident |
| `<state_root>/indicators.md` | Standing IOC rows | First indicator |
| `<state_root>/artifacts/<kebab>.md` | Re-readable work products | First long artifact |
| Shared servers/contacts/domains/devices/finances/projects | Cross-skill inventories | When entity must be shared |

Optional paths are created only when needed. Never pre-expand empty trees.
