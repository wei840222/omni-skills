---
name: smtp
description: >
  Configure, test, send, and debug outbound SMTP mail with safe dry runs,
  provider-aware auth, TLS/port matching, canary sends, and inbox-placement
  diagnostics. Use when the user mentions SMTP host/port setup, STARTTLS vs
  implicit TLS, auth failures (535/534), relay denial, bounce codes, SPF/DKIM/DMARC
  alignment, or "sent but went to spam". Prefer `mail` / `email-management` for
  inbox triage and drafting; prefer provider-native APIs when the user already
  works in Gmail/Fastmail/Workspace tooling instead of raw SMTP.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📬"}'
  related-skills: '{"email-management":"Handles reading and sorting emails.","mail":"Uses Mail.app or himalaya to read and send email."}'
---

## When to Use

Use this skill when the user needs to configure, test, send, or debug outbound email over SMTP.
It is for submission and delivery work: provider setup, ports and TLS, auth failures, relay denials, canary sends, bounce interpretation, and inbox-placement diagnosis.

## State location

SMTP state may exist in `<workspace>/smtp/`, `<workspace>/memory/smtp/`, or `~/smtp/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/smtp/`, `<workspace>/memory/smtp/`, `~/smtp/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and state must be created, default to `<workspace>/smtp/` when `<workspace>` is available; otherwise ask for a state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill.

## Operating Instructions

Load only the reference required by the current failure mode; keep SKILL.md as the always-on path.

Read references only when required:
- `references/setup.md`: Read when `<state_root>` is missing or stale.
- `references/send-flow.md`: Read when sending or testing SMTP delivery.
- `references/diagnostic-playbook.md`: Read to troubleshoot connection, auth, or relay failures.
- `references/deliverability.md`: Read to troubleshoot spam placement or DKIM/SPF/DMARC issues.
- `references/sources.md`: Read when verifying protocol, provider, or deliverability claims against primary sources.

For static templates and data schemas, load assets as needed:
- `assets/swaks-recipes.md`: Swaks command recipes.
- `assets/memory-template.md`: Baseline for `<state_root>/memory.md`.
- `assets/memory.example.md`: Example shape of a live SMTP memory file.
- `assets/provider-profiles.md`: Baseline for `<state_root>/provider-profiles.md`.
- `assets/send-log.md`: Baseline for `<state_root>/send-log.md`.
- `assets/deliverability-notes.md`: Baseline for `<state_root>/deliverability-notes.md`.

## Quick Reference

| Topic | File | Use it for |
|-------|------|------------|
| Setup and first-run guardrails | `references/setup.md` | Initialize `<state_root>/` without storing secrets or sending mail too early |
| Memory structure | `assets/memory-template.md` | Create `<state_root>/memory.md` with status and stable context |
| Baseline memory example | `assets/memory.example.md` | Show the expected shape of a live SMTP memory file |
| Provider profile baseline | `assets/provider-profiles.md` | Track approved providers, ports, auth modes, and sender identities |
| Send decision log baseline | `assets/send-log.md` | Record dry runs, canaries, queue IDs, and verification evidence |
| Deliverability notes baseline | `assets/deliverability-notes.md` | Capture DNS auth status, spam-folder evidence, and bounce patterns |
| Safe execution workflow | `references/send-flow.md` | Run draft -> preflight -> canary -> verify -> scale |
| Fault isolation guide | `references/diagnostic-playbook.md` | Separate DNS, TLS, auth, relay, and placement failures |
| Deliverability rules | `references/deliverability.md` | Check SPF, DKIM, DMARC, alignment, and inbox placement |
| CLI probe patterns | `assets/swaks-recipes.md` | Use deterministic SMTP tests with placeholder-only examples |
| Primary sources | `references/sources.md` | Cite RFC and provider docs for protocol or policy claims |

## Requirements

- SMTP host access only when the user wants real network testing or live sending.
- Credentials must come from a user-approved secret source at runtime, never from files under `<state_root>/`.
- Recommended tools: `swaks` for SMTP probes, `openssl` for TLS inspection, and `dig` or `nslookup` for DNS checks.
- Explicit confirmation before any live send, external-recipient test, or multi-recipient action.

## Core Rules

### 1. Separate Draft, Probe, and Live Send
- Decide which mode the task is in before touching the network: draft-only, connectivity probe, auth probe, canary send, or live send.
- Draft and explain first. Do not jump from "help me configure SMTP" to "message sent."

### 2. Match Port, TLS, and Auth Exactly
- Port 465 means implicit TLS. Port 587 usually means STARTTLS. Port 25 is relay transport and is often blocked or policy-limited.
- Treat host, port, TLS mode, and auth mechanism as one contract. A single mismatch can look like a generic timeout or auth error.

### 3. Debug One Layer at a Time
- Validate in order: DNS and hostname, TCP reachability, TLS handshake, EHLO capabilities, auth, submission response, then mailbox placement.
- Do not tweak deliverability records before proving the connection and auth layers are healthy.

### 4. Keep Sender Identity Aligned
- Check whether the authenticated account, envelope sender, visible From address, DKIM domain, and return-path domain actually belong together.
- Misalignment often produces 550/553 rejections, spam placement, or "sent successfully" with no inbox result.

### 5. Canary Before Scale
- The first live test should target one approved canary recipient, ideally on the same org or a controlled inbox.
- Only widen recipients after you have queue acceptance, message ID evidence, and inbox-or-spam confirmation.

### 6. Handle Credentials and Logs Safely
- Store raw SMTP passwords, API tokens, or full secrets securely outside of `<state_root>/`.
- Redact logs and screenshots before storing or sharing them. Keep only the smallest evidence needed to debug.

### 7. Acceptance Is Not Delivery
- A `250 queued` or similar server response means the SMTP server accepted the message, not that the recipient inbox accepted it.
- Always verify final state through bounce evidence, mailbox placement, or downstream provider logs when available.

## Common Traps

| Trap | Why It Fails | Better Move |
|------|--------------|-------------|
| Treating port 465 and 587 as interchangeable | TLS handshake breaks or auth never starts | Match implicit TLS vs STARTTLS explicitly |
| Changing SPF before fixing auth | Wrong layer, no effect on login failure | Prove DNS, TLS, and auth separately |
| Assuming `250` means inbox success | Queue acceptance is not mailbox placement | Check spam, bounces, and final recipient evidence |
| Using external recipients as the first test | Increases blast radius and risk | Start with one approved canary inbox |
| Disabling certificate checks to "make it work" | Hides real TLS or hostname issues | Fix hostname, CA trust, or port selection instead |
| Letting From differ wildly from auth identity | Triggers relay denial or spam scoring | Align sender identity or document the relay policy |

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| Configured SMTP submission server, such as `smtp.example.com` | Message headers, recipients, body, and attachments only for approved live tests or sends | Submit or test outbound mail |
| DNS resolvers or authoritative nameservers for the sender domain | Domain names and record lookups for SPF, DKIM, DMARC, MX, and PTR checks | Diagnose deliverability and domain alignment |

No other data should be sent externally unless the user explicitly approves broader tooling.

## Data Storage

Local state in `<state_root>/` includes:

- activation state, approved providers, and safety defaults in `<state_root>/memory.md`
- known-good server profiles and sender-identity notes in `<state_root>/provider-profiles.md`
- dry-run decisions, canary evidence, and message IDs in `<state_root>/send-log.md`
- domain-auth and placement findings in `<state_root>/deliverability-notes.md`

Initialize those files from the matching templates under `assets/` when creating a new `<state_root>/`.

## Security & Privacy

**Data that leaves your machine:**
- SMTP envelope and message content only during approved probes or live sends
- DNS queries needed to validate sender-domain health and routing

**Data that stays local:**
- safe defaults and approved provider context in `<state_root>/memory.md`
- known-good provider settings and debugging evidence in `<state_root>/provider-profiles.md`, `<state_root>/send-log.md`, and `<state_root>/deliverability-notes.md`

**This skill does NOT:**
- send live mail without explicit confirmation
- store raw SMTP passwords or tokens in local memory
- modify DNS records, mailing lists, or provider settings unless the user explicitly asks
- disable TLS verification silently
- modify its own skill definition

## Trust

By using this skill, approved message content is sent to the configured SMTP provider and related DNS infrastructure.
Only install and run it if you trust those providers with your outbound mail flow.

## Scope

This skill covers:
- configure and diagnose outbound SMTP submission
- maintain small local notes in `<state_root>/`
- run canary-first send workflows with explicit confirmation gates

Prefer adjacent skills or ask when the task is inbox triage, bulk campaign tooling, or provider-native APIs instead of raw SMTP.
When live-send approval is ambiguous, stay in draft or probe mode and ask for an explicit send confirmation.
Keep credentials outside `<state_root>/`.
Treat queue acceptance as incomplete until placement or bounce evidence is known.
Keep one-off canaries one-recipient until the user confirms a wider send.
