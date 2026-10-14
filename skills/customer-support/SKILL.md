---
name: customer-support
description: >
  Resolve customer issues with low effort, clear empathy, identity-safe
  handling, and durable follow-through across chat, email, ticket, or voice
  coaching. Use when drafting replies, coaching agents, de-escalating anger,
  refusing policy exceptions, handling renewals/refunds/cancellations/chargebacks, or
  turning a support thread into a loyal outcome. Prefer `empathy` for pure
  emotional processing, `call-center` for live voice scripts, `zendesk` for
  Zendesk API ops, `triage` for queue priority only, and `crm` once the case is
  already a CRM contact/deal problem.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎧"}'
  related-skills: '{"empathy":"Deep emotional simulation and intensity calibration when the need is pure affect work, not full case resolution.","call-center":"Live voice/inbound-outbound call scripts, AHT/FCR framing, and call logging.","zendesk":"Zendesk Support API tickets, users, and automation once the work is platform ops.","triage":"P0–P3 cost-of-delay ordering for a mixed work pile before writing the customer reply.","crm":"Contact, account, and pipeline hygiene after the support issue becomes a CRM record problem.","chat":"General conversational channel mechanics when the medium—not support judgment—is the blocker.","escalate":"Ask-vs-act thresholds when the agent must decide autonomy vs human approval."}'
---

# Customer Support

Make the next right customer action **easy**: acknowledge the real problem,
verify identity before sensitive data, solve (or clearly route) on this contact
when possible, set plain-language expectations, and close only after the
customer can see the outcome.

This skill is **stateless by default** for one-shot reply coaching. Optional
macros, playbooks, and non-PII pattern notes may live under a resolved
`<state_root>` only when the user wants continuity. Never store real customer
PII, payment data, auth secrets, or full ticket dumps in the skill package.

## State location

Support macros and optional local notes may exist in
`<workspace>/customer-support/`, `<workspace>/memory/customer-support/`, or
`~/customer-support/`. Before reading or writing state, resolve `<state_root>`:

1. Use an explicitly configured path when one exists (host config or user override).
2. Otherwise use the first existing directory in this order:
   `<workspace>/customer-support/`, `<workspace>/memory/customer-support/`,
   `~/customer-support/`.
3. If several candidate directories exist, use only the highest-precedence one and
   report the separate copies; do not merge or cross-write.
4. If none exists and the user explicitly wants continuity, create
   `<workspace>/customer-support/` by default.
5. If the host cannot supply `<workspace>`, read an existing
   `~/customer-support/` only; otherwise ask for a state root before creating data.
6. If older data exists only under `~/clawic/customer-support/` or
   `~/Clawic/data/customer-support/`, move it into the resolved `<state_root>/`
   after the user confirms, and say in one line that you moved it and from where.

Use the selected `<state_root>` for every state operation in this skill.
Typical layout (create children only when needed):

- `<state_root>/macros/` — reusable reply skeletons (no live customer data)
- `<state_root>/playbooks/` — product-specific resolution paths
- `<state_root>/patterns.md` — recurring defect signals (sanitized)

## When to use

- Draft or rewrite a customer-facing reply (chat, email, ticket comment)
- Coach an agent through anger, ALL-CAPS, refund, cancel, or policy-no moments
- Lower customer effort: avoid re-explain, re-transfer, and repeat contacts
- Verify identity before account changes; refuse unsafe disclosure
- Decide escalate vs resolve vs schedule follow-up
- Capture internal notes and pattern flags without dumping PII into chat history

Prefer `empathy` when the only job is emotional attunement.
Prefer `call-center` for live phone/voice script structure and call KPIs.
Prefer `zendesk` once the remaining work is Zendesk API/ticket mechanics.
Prefer `triage` when the blocker is queue priority across mixed work.
Prefer `crm` after the case is already a contact/account/pipeline problem.

## Safety order (always)

1. **Identity before account data** — verify the customer before sharing profile
   details, sending resets, or changing billing. Prefer phishing-resistant
   channels already bound to the account; never collect passwords or full card
   PANs in free-text chat. Orient to NIST SP 800-63B authenticator guidance.
2. **Least data** — quote only the fields needed for this resolution; keep full
   dumps and secrets out of reusable notes and skill state.
3. **Promise only what policy and systems allow** — no invented refunds, SLAs,
   legal outcomes, or supervisor availability.
4. **Channel honesty** — if the fix needs another channel (shipping carrier,
   bank, specialist queue), say why and give the exact next step; do not bounce
   the customer without a handoff.
5. **Accessible, plain language** — short sentences, concrete next steps, no
   unexplained jargon (Plain Language principles; keep web-facing help paths
   accessible per ADA web guidance orientation).
6. **Escalate on authority, safety, legal, fraud, or third failed attempt** —
   load `references/escalation.md`.

## Quick workflow

1. Read the **whole** thread and account timeline before asking the customer to repeat.
2. Acknowledge the impact in one plain sentence; name the issue, not a slogan.
3. Confirm the goal (refund, cancel future renewals, restore access, status).
4. Apply identity / data checks if the next action is sensitive.
5. Solve on this contact when policy allows; otherwise give a dated path and owner.
6. Anticipate the **next** related failure (billing after cancel, tracking after reship).
7. Close with what changed, what happens next, and how to reopen if needed.
8. Write internal notes + pattern flags; hand off to `zendesk` / `crm` / `call-center` when the medium requires it.

## Routing

| Need | File |
| --- | --- |
| Core resolution and communication rules | `references/domain.md` |
| Anger, refusal, and escalation paths | `references/escalation.md` |
| Low-effort recovery and loyalty tactics | `references/recovery.md` |
| Verified source URLs (Gate 6) | `references/sources.md` |

## Core rules (summary)

1. **Loyalty tracks low effort, not theatrical delight** — solve cleanly; skip
   empty wow scripts (HBR Customer Effort research).
2. **Acknowledge → investigate → act → confirm** every contact.
3. **One question at a time** when information is missing; never re-ask data already in the thread.
4. **Match tone without matching abuse** — stay steady; validate situation, not insults.
5. **Lead with what you can do** when refusing; pair the no with a real alternative.
6. **First-contact resolution when feasible** — industry FCR guidance treats complete resolution quality as the goal, not a gamed percentage.
7. **CSAT is a post-interaction satisfaction pulse** (commonly % of top-box scores); use it as feedback, not a reason to over-promise.
8. **Document non-obvious context** for the next agent; sanitize PII in reusable macros.
9. **Negative feedback is product signal** — flag repeats upward without blaming the customer.
10. **Follow up only when promised** — silence after a dated commitment destroys trust.

Load `references/domain.md` for the full playbook.
Load `references/escalation.md` before supervisor/legal/fraud paths.
Load `references/recovery.md` when repairing a broken experience.
Load `references/sources.md` before restating metrics, auth, or legal orientation.
