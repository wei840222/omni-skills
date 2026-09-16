---
name: email-marketing
description: Manage email deliverability, list health, sequences, segmentation, and campaign optimization with modern bulk-sender compliance. Trigger when the user needs email marketing strategy, deliverability fixes, nurture sequences, list hygiene, or ESP campaign operations.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📧","requires":{"configPaths":["<state_root>/"]}}'
  related-skills: '{"copywriting":"Owns persuasive email body, subject, and CTA craft.","content-marketing":"Places email inside content calendar and funnel systems.","affiliate-marketing":"Partner nurture and owned-audience conversion sequences.","growth-hacker":"Acquisition experiments that feed or measure email loops.","cmo":"Channel strategy and demand generation leadership around email."}'
---

## State location

Email Marketing state may exist in `<workspace>/email-marketing/`, `<workspace>/memory/email-marketing/`, or `~/email-marketing/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/email-marketing/`, `<workspace>/memory/email-marketing/`, `~/email-marketing/`.
3. If none exists and state must be created, default to `<workspace>/email-marketing/`.

Use the selected `<state_root>` for every state operation in this skill.

## Setup

On first use, read `references/setup.md` for activation constraints. This skill works without local storage. Only create `<state_root>/` if the user wants persistent list, sequence, and deliverability continuity.

## When to Use

User needs email marketing, deliverability diagnosis, list hygiene, segmentation, nurture sequences, campaign planning, A/B testing, or bulk-sender compliance (SPF/DKIM/DMARC, one-click unsubscribe). Agent handles domain warmup, health metrics, subject and preview strategy, automation triggers, and compliance gates.

Use this when the problem is operating owned-email acquisition and retention end to end, not just drafting a single message. The goal is inbox placement, list durability, and conversion quality under current mailbox-provider rules.

This skill is especially strong for SaaS, ecommerce, creators, B2B newsletters, and teams recovering from spam-folder or list-decay problems.

## Architecture

Local workspace is optional and only created with user consent.

```
<state_root>/
├── memory.md        # Program context, ESP, approved rules, active constraints
├── lists.md         # Segments, hygiene status, sunset policies
├── sequences.md     # Active automations, triggers, performance notes
└── incidents.md     # Deliverability incidents, blacklist hits, compliance notes
```

## Quick Reference

| Topic | When to load | File |
|-------|--------------|------|
| Setup and activation | On first use to learn ESP context and optional state. | `references/setup.md` |
| Continuity memory | When user wants persistent state across sessions. | `references/memory.md` |
| Deliverability and authentication | Domain setup, spam folder issues, warmup, blacklists. | `references/deliverability.md` |
| List health and segmentation | Hygiene, sunset, engagement tiers, growth quality. | `references/list-health.md` |
| Sequences and automation | Welcome, onboarding, cart, re-engagement flows. | `references/sequences.md` |
| Campaign craft and testing | Subject, preview, body structure, A/B design. | `references/campaigns.md` |
| Compliance and consent | CAN-SPAM, GDPR, RFC 8058, consent boundaries. | `references/compliance.md` |
| Launch and recovery playbooks | Immediate execution sprints for common failures. | `references/playbooks.md` |
| Research sources | Verified bulk-sender and compliance citations. | `references/sources.md` |

## Core Rules

### 1. Authenticate and warm before volume
- Require SPF, DKIM, and DMARC for any bulk-sending domain; missing auth is a hard blocker under current Gmail/Yahoo bulk-sender expectations.
- Warm new domains and IPs gradually (start ~50–100/day, increase ~20% daily over 2–4 weeks) instead of dumping volume.
- Use `references/deliverability.md` before recommending send volume increases.

### 2. Protect list health over list size
- Prefer organic growth; purchased lists permanently damage sender reputation.
- Remove hard bounces immediately; sunset unengaged contacts after a defined window (commonly ~90 days after a re-engagement attempt).
- Use `references/list-health.md` for metrics thresholds and segment design.

### 3. Design sequences as systems, not one-off blasts
- Map trigger → message → next action for welcome, purchase, abandoned cart, and re-engagement.
- Space most nurture emails 1–3 days apart; the first message carries the highest open rate and must deliver the promised value.
- Use `references/sequences.md` when building or debugging automations.

### 4. Optimize craft with one primary goal per send
- Subject lines ~40–50 characters; preview text is a second subject line, not “View in browser”.
- Prefer natural language over spam-trigger patterns (ALL CAPS, “free”, “act now”, excessive punctuation).
- One primary CTA; measure opens for subjects, clicks for content, conversions for offers.
- Use `references/campaigns.md` for craft and A/B discipline.

### 5. Treat compliance as launch-critical
- Physical postal address in every commercial email; honor opt-outs immediately.
- Implement one-click unsubscribe (RFC 8058) for bulk senders on major inbox providers.
- Keep spam complaint rates strictly below 0.3% (target ≤0.1%).
- Use `references/compliance.md` before launch and after any consent-model change.

### 6. Diagnose deliverability with evidence, not folklore
- Pair Postmaster / blacklist / bounce data with list and content changes before blaming “the algorithm”.
- Fix auth, list quality, and complaint rate before creative experiments.
- Use `references/playbooks.md` for recovery sprints.

### 7. Escalate regulated claims and third-party sends
- Health, finance, political, or SMS-adjacent consent claims need explicit review.
- Do not send, purchase lists, or change production ESP settings without user authorization.

## Operating Rhythm

### Before launch
- Confirm domain auth, unsubscribe path, physical address, and segment definition.
- Validate seed inbox placement and complaint/bounce baselines.

### Weekly
- Review open/click/bounce/unsubscribe/complaint rates by segment.
- End with keep, fix, suppress, re-engage, and remove decisions.

### Monthly
- Revisit sunset policy, sequence attrition, and whether volume growth is still incremental.
- Refresh creative and suppress chronically unengaged cohorts before adding new volume.

## Common Traps

- Sending every campaign to the full list → engagement and placement decay.
- Buying lists or skipping double opt-in → spam traps and sudden blocks.
- Ignoring mobile layout and preview text → wasted subject-line wins.
- Multiple competing CTAs → diluted response.
- Hard-selling before value delivery → early unsubscribes and complaints.
- Raising volume while complaint rate is already elevated → deeper reputation damage.

## Security & Privacy

**Data that stays local when the user opts in:**
- Program rules, segment definitions, sequence notes, and incident history in `<state_root>/`

**This skill does NOT:**
- Automatically send campaigns, buy lists, or change ESP production settings
- Create local files without explicit user consent
- Access ESPs, CRMs, or analytics unless the user explicitly requests a separate approved tool workflow
- Make undeclared network requests

**Guardrails:**
- Treat subscriber PII, suppression lists, and ESP credentials as restricted
- Escalate legal or policy-sensitive promotions for review before launch
