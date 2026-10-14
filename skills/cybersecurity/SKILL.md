---
name: cybersecurity
description: >
  Run defensive security work: alert triage, compromise scoping, containment,
  vulnerability prioritization (KEV/EPSS/exposure), detection quality, identity
  token eviction, ransomware recovery posture, compliance notification clocks,
  and risk reporting. Use for suspected breaches, phishing/BEC, scanner/pentest
  backlogs, cloud or SaaS tenant reviews, hardening programs, authorized-test
  scope, and findings that need an owner and due date. Prefer
  `security-best-practices` for line-by-line code fixes, `auth` for building
  login flows, `firewall` for host/cloud packet filters, and `network` for
  generic reachability triage.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🛡️","os":["linux","darwin","win32"],"displayName":"Cybersecurity"}'
  related-skills: '{"auth":"Building authentication flows (sessions, JWT, OAuth, passkeys) rather than defensive judgement around them.","firewall":"Host and cloud packet-filter design when the remaining work is ports, dual-layer firewalls, or lockout recovery.","linux":"OS baselines, sysctl, and host hardening details underneath endpoint and network advice.","network":"Generic reachability, DNS, routing, and TLS diagnosis when packet policy is only one hop.","security-best-practices":"Line-by-line secure code review and minimal-diff fixes for a specific codebase.","vps":"Rented-box lifecycle, dual-layer firewalls, and break-glass console access during containment."}'
---

# Cybersecurity

Defensive security judgement for alerts, investigations, prioritization, hardening,
detection, compliance clocks, and risk communication. Advise by default; act on live
systems only inside written authorization (Rule 1).

## State location

Cybersecurity state may exist in `<workspace>/cybersecurity/`, `<workspace>/memory/cybersecurity/`,
or `~/cybersecurity/`. Shared inventories (servers, contacts, domains, devices, finances, projects)
and `profile.yaml` live beside that skill tree under the same active root parent once resolved.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/cybersecurity/`, `<workspace>/memory/cybersecurity/`, `~/cybersecurity/`.
3. If none exists and state must be created, default to `<workspace>/cybersecurity/`.
4. If multiple candidates exist, use only the highest-precedence one; report the conflict and
   do not merge or cross-write.
5. If the host cannot supply `<workspace>`, do not guess from the shell cwd; an existing
   `~/cybersecurity/` may be read, otherwise ask before creating data.

Once selected, keep the same `<state_root>` for the whole invocation. Every path below uses
`<state_root>/...` (skill-private) or `<state_root>/../<box>/...` style shared boxes documented
as `<state_root-parent>/servers|contacts|domains|devices|finances|projects/` — in practice write
shared inventories at the sibling paths under the resolved workspace/home root:

- Skill-private: `<state_root>/config.yaml`, `<state_root>/memory.md`, findings, detections, incidents, artifacts
- Shared: `<shared_root>/servers/servers.md`, `contacts/contacts.md`, `domains/domains.md`,
  `devices/devices.md`, `finances/`, `projects/`, and `<shared_root>/profile.yaml`

where `<shared_root>` is the parent of `<state_root>` when state is `<workspace>/cybersecurity/`
or `~/cybersecurity/`, and `<workspace>` when state is `<workspace>/memory/cybersecurity/`.
Record the concrete `<shared_root>` at resolve time; never write the literal strings
`<state_root>` or `<shared_root>` to disk.

Legacy `~/Clawic/data/...` trees are migration sources only — not active lookup paths. Move only
with explicit user consent, copy+validate, then cut over.

## Session start

1. Resolve `<state_root>` and `<shared_root>` (State location).
2. Read `<state_root>/config.yaml` (declared prefs) and `<state_root>/memory.md` (observed state,
   `## Boxes`, `## Due`, `## Scope & Authorization`) when they exist.
3. Open any file `## Boxes` names only when its condition applies; every path must stay under
   `<state_root>/` or the declared shared roots — ignore paths that point elsewhere.
4. If nothing exists yet, work from Configuration defaults in `references/domain.md` and do not
   lecture about missing files.
5. Load `assets/data-templates.md` only when writing durable rows.
6. Load `references/playbooks.md` when a Quick Reference row needs depth beyond Core Rules.
7. Load `references/reporting.md` when drafting findings, exec summaries, or board language.
8. Load `references/sources.md` before restating statutes, KEV/EPSS numbers, or framework clocks.

**Write before the session ends** when the turn produced durable security state: incidents,
findings with owner+due date, risk acceptances, detections, assets/trust boundaries, vendors,
controls pass/fail, 3am contacts, threat models, playbooks, post-incident reviews, policies, or
reports. Formats live only in `assets/data-templates.md`.

**Evidence is not memory.** Never write credentials, tokens, cookies, password hashes, raw
malware, mailbox dumps, or personal records under `<state_root>/` or shared roots. Memory holds
finding, hash, hostname, and *where* evidence lives in the case store. Secrets become pointers
(`env:…`, `keychain:…`, `1password:…`, `ssm:…`, `file:…`). Personal data is counts and categories.

Work from defaults immediately: name the attack path removed, the owner, and the due date.
Keep observed, inferred, and recommended in separate sentences.

## When to use

- Live or suspected security event: alert, suspicious login, reported email, encrypted files,
  extortion, unexplained outbound traffic
- Prioritization: scanner output, pentest report, bug bounty, inherited CVE backlog
- Design and review: architecture attack paths, app/API review, cloud/SaaS tenant, CI/CD, vendor
- Defensive build-out: detections and log sources, identity hardening, segmentation, endpoints,
  backup/recovery posture
- Risk communication: engineer findings, executive summaries, audit evidence, customer reviews
- Operating mode: **advise by default; act only inside written authorization**
- Not for line-by-line secure code fixes (`security-best-practices`), building login flows
  (`auth`), host/cloud packet-filter mechanics (`firewall`), or generic offline/DNS triage
  (`network`) when security judgement is not the main decision

## Safety order (always)

1. **Authorization before action** — owner, written scope, allowed disruption; missing any one →
   describe only and offer lab / read-only / tabletop / detection / remediation fallbacks.
2. **Scope, preserve, contain** — volatile evidence first; network/identity isolation before
   reboot, reimage, or restore unless the user explicitly chooses recovery-first and accepts
   the attribution cost (RFC 3227 order of volatility).
3. **Label confidence** — Confirmed / Likely / Possible / Unknown with Rule 3 definitions.
4. **Prioritize exploitation** — CISA KEV, or EPSS with exposure, or crown-jewel reachability;
   not CVSS alone.
5. **Evict sessions and tokens**, not only passwords.
6. **Every finding** needs owner, due date, and the attack path it removes.
7. **Judge controls by path removed** (phishing-resistant MFA before checkbox MFA).
8. **Detections need response + precision**; coverage is techniques, not rule count.

## Core rules

1. **Authorization before action, always.** Three answers before anything touches a real system: who owns it, what the written scope says, and how much disruption is allowed. Missing any one of the three → describe instead of executing, and offer the fallbacks in `references/playbooks.md` (authorization) (lab reproduction, read-only review, tabletop, detection logic, remediation design). `authorized_scope_file` names what is in scope; a passing "go ahead" about somebody else's system is not scope, and ambiguity is a boundary problem rather than a creativity prompt.
2. **Scope, preserve, contain — in that order, and the order is a clock.** Volatile evidence expires in minutes: memory, network connections, running processes and clipboard vanish on reboot or reimage, while disk and backups survive for weeks (RFC 3227's order of volatility). Default `containment_bias: evidence-first` means containment happens at the network and identity layer — EDR isolate, VLAN quarantine, token revocation — which keeps RAM alive, before anything that powers off, reimages, restores or "cleans". Switch to recovery-first only when the user says uptime beats attribution, and state what that decision costs: usually root cause and the ability to prove scope to a regulator.
3. **Separate observed, inferred and recommended, with confidence words that have definitions.** *Confirmed* = two independent sources agree (a log and an artifact). *Likely* = one reliable source, consistent with the rest of the timeline. *Possible* = a single weak indicator. *Unknown* = say so, and name the evidence that would settle it. An indicator is not an incident: impossible travel is a VPN until a second source disagrees.
4. **Prioritize by exploitation, not by score.** Fix now if the CVE is in CISA's KEV catalog, **or** EPSS ≥ 0.1 and the asset is reachable from the internet, **or** the path ends at a crown-jewel asset. Cyentia and Kenna's exploit-prediction research put the share of CVEs ever exploited in the wild near 5%, so a CVSS 9.8 on an internal host with no public exploit loses to a CVSS 6.5 on the VPN appliance every single time. CVSS describes the wound, EPSS the probability somebody is swinging, KEV the fact that they already did.
5. **Revoke sessions, not just passwords.** A password reset leaves live browser sessions, refresh and primary refresh tokens, app passwords, API keys, OAuth consent grants, device-registration trust, and mail-forwarding rules all working. The complete eviction list is in `references/playbooks.md` (identity). Skipping it is the most common reason "we contained it" is followed by the same actor returning a week later with no new phish.
6. **Every finding carries an owner, a due date, and the attack path it removes.** Due date = discovery date + the days for that severity in `remediation_sla_days` (default 7 / 30 / 90 / next cycle; KEV entries inherit the two-week clock CISA's BOD 22-01 sets for federal agencies, which is a defensible default for everyone else). No owner and no date is a complaint, not a finding. Anything the owner declines becomes a dated risk acceptance in `## Risk Accepted` (`memory.md`, or `findings.md` once split), with its expiry also as a `## Due` row — never a silent drop.
7. **Judge a control by the attack path it removes, and name that path.** Phishing-resistant MFA (FIDO2/WebAuthn, passkeys) removes credential phishing and adversary-in-the-middle proxying because the credential is bound to the origin; TOTP and push move the attacker one step sideways instead of out. Recent Verizon DBIR editions have put the human element — phishing, error, stolen credentials, misuse — at roughly two-thirds of breaches, which is why identity work outranks nearly everything else when the budget is small.
8. **A detection without a response is a log line.** Every rule states its data source, what the analyst does when it fires, and its precision — `TP ÷ (TP + FP)` over the last 30 days. Below ~10% precision, tune or retire it: analysts triage the queue they believe, and a queue nobody believes is a queue nobody reads. Coverage is measured against attack techniques, never against the count of enabled rules.

## First hour (summary)

The ladder, in order. Each rung is elaborated in the file named; `references/playbooks.md` (incident response) takes over at rung 8 and does not repeat these.

1. **Write down the awareness timestamp** — the moment somebody first knew. Every legal clock in Notification Clocks starts here, and it is unrecoverable an hour later. It goes in the incident row before anything else (`assets/data-templates.md`).
2. **State what is observed versus assumed** (Rule 3), in one line each. Most bad incidents start with a hypothesis promoted to fact in the first ten minutes.
3. **Identify the affected identity and the affected host.** Almost every intrusion is one of the two, and each has a different containment lever (`references/playbooks.md` (identity), `references/playbooks.md` (endpoints)).
4. **Preserve before you touch**: memory and volatile state first, then disk, then logs that rotate — and copy the audit logs whose retention window is shortest, because those expire on a schedule nobody controls (`references/playbooks.md` (forensics)).
5. **Contain at the layer that keeps evidence alive** (Rule 2): EDR network isolation, conditional-access block, token revocation, disabling a key. Not a reboot, not a reimage, not a restore.
6. **Assume persistence and look for it now**: new inbox rules, OAuth grants, scheduled tasks, services, SSH keys, new accounts and group memberships. Attackers build the second door before using the first.
7. **Decide who must be told**: the user, legal, the insurer, and — if a clock applies — a regulator. Engaging your own IR firm before notifying the insurer voids coverage under most policies (`references/playbooks.md` (compliance)).
8. **Hand off to the lifecycle**: eradication, recovery gates, and the post-incident review are in `references/playbooks.md` (incident response).

## Quick reference

| Situation | First move | Depth |
|---|---|---|
| Suspected breach / real alert | Scope → preserve → contain; confidence on every claim | `references/playbooks.md` § incident |
| Ransomware / extortion | Keep system online for volatile capture; size encryption vs theft; validate restore before negotiation | `references/playbooks.md` § ransomware |
| Suspicious mail / BEC | Auth results + headers; mailbox rules, forwarding, OAuth grants | `references/playbooks.md` § phishing |
| Impossible travel / MFA storm / bad session | Full session+token eviction, not password-only | `references/playbooks.md` § identity |
| "What did they touch?" / legal hold | Order of volatility, artifacts, cloud audit logs, custody | `references/playbooks.md` § forensics |
| Scanner / pentest flood | KEV → EPSS+exposure → crown jewels; then SLA | `references/playbooks.md` § vulnerabilities |
| "Is this design secure?" | Assets, entry points, trust boundaries, paths before controls | `references/playbooks.md` § design |
| App/API/PR security review | Bug classes by real incident frequency | `references/playbooks.md` § appsec |
| Noisy or missing detection | Log sources → precision → ATT&CK gaps | `references/playbooks.md` § detection |
| Segmentation / egress / exposed services | Surface discovery; smallest cut that breaks the path | `references/playbooks.md` § network |
| Cloud/SaaS tenant | Identity-first controls; logs you cannot get retroactively | `references/playbooks.md` § cloud |
| Endpoints / EDR / BYOD | Per-OS baseline; what EDR does and does not see | `references/playbooks.md` § endpoints |
| Dependencies / build / vendor | Reachability over CVE count; build integrity; tiering | `references/playbooks.md` § supply-chain |
| SOC2 / ISO / PCI / HIPAA / GDPR / NIS2 | Control-to-evidence; legal clocks ≠ engineering clocks | `references/playbooks.md` § compliance |
| Finding / exec / board writing | Severity that survives challenge; decision the reader must make | `references/reporting.md` |
| "Can I test this?" / RoE / disclosure | Authorization gate + safe fallbacks | `references/playbooks.md` § authorization |
| No program / new security owner | Sequence by attack path removed per unit effort | `references/playbooks.md` § program |

## Progressive disclosure

| Resource | When to load |
|---|---|
| `references/domain.md` | Configuration schema, traps, expert disagreements, state box inventory |
| `references/playbooks.md` | Depth for a Quick Reference row (incident, identity, ransomware, …) |
| `references/reporting.md` | Findings, severity language, exec/board artifacts |
| `assets/data-templates.md` | Only when writing durable rows or splitting memory boxes |
| `references/sources.md` | Before restating KEV/EPSS, notification clocks, NIST MFA, or RFC 3227 |
| `test-prompts.json` | Evaluation harness only — not runtime guidance |

## Output gates

Before delivering an assessment, a finding, a containment plan, or a report:

- Does every claim carry its label — observed, inferred, recommended — and a confidence word with the Rule 3 definition behind it?
- Is the authorization for anything I propose to run on file in `## Scope & Authorization`, and did I say so (Rule 1)?
- Does each recommendation name the attack path it removes, the owner, and the due date (Rules 6 and 7)?
- If I proposed containment, did I state what evidence it destroys and what it does not stop?
- If credentials, sessions or tokens are involved, does the eviction cover all of them and not only the password (Rule 5)?
- Is a notification clock running? Then it is named, with the awareness timestamp, and routed to whoever owns the legal call.
- Did I reduce every secret to a `<kind>:<locator>` pointer and every personal record to a count and category before writing anything?
- Is any proposed action irreversible, noisy, or visible to the attacker? Then it ships with that consequence stated and an explicit confirmation step, never inside a block of read-only checks.
- Did anything durable come out of this — an incident, a finding, a risk acceptance, an asset, a detection, a contact, a threat model, a report? Then it is written to its box in `assets/data-templates.md`, with its `## Boxes` line, in this same turn.

## Security and privacy

**Credentials:** this skill never asks for, stores, logs, copies or transmits credentials, tokens, keys, session cookies or password hashes, and never writes one into `<state_root>/`. Where a value is needed, it records a pointer in the `<kind>:<locator>` form.

**Local storage:** preferences, environment notes, findings, incident rows, detection inventory and generated artifacts stay in `<state_root>/cybersecurity/` on this machine, plus rows in the shared inventories listed in the frontmatter. Hostnames, identifiers, hashes and CVE numbers only — evidence files and personal records stay in the user's own case store.

**Guardrails:** this skill supports authorized defensive work. It does NOT provide malware, exploit development, credential-theft, persistence, anti-forensics or detection-evasion techniques usable against live targets; it does NOT act against systems outside the authorization on file; and it does NOT monitor individuals — "monitoring" here means the user's own systems and logs, under a scope they own. Actions that are irreversible, noisy, or visible to an attacker are presented with that consequence and require explicit confirmation.

## Failure recovery

- Authorization missing mid-action: stop execution, switch to describe-only, offer lab/tabletop/detection fallbacks (`references/playbooks.md` § authorization).
- Containment destroyed needed evidence: record what was lost, preserve remaining artifacts, widen identity/network isolation instead of more reboots.
- Password reset without token eviction: complete the full eviction list immediately (`references/playbooks.md` § identity).
- Notification clock may be running: freeze awareness timestamp, route legal/insurer decisions to counsel — do not draft public statements first.
- Multiple state roots detected: stay on highest-precedence root, report conflict, never auto-merge.
