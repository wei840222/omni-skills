# Customer Support — domain playbook

Runtime guidance for drafting replies and coaching agents. Load this when the
summary rules in `SKILL.md` are not enough. Metrics and external claims stay
anchored in `sources.md`.

## Contact loop

1. **Orient** — read the full thread, prior tickets, and account flags first.
2. **Acknowledge** — one sentence on the impact (“I see the renewal charged after you asked to cancel”).
3. **Frame the goal** — restate the desired outcome in the customer’s words.
4. **Verify** — identity and entitlement checks before sensitive actions.
5. **Act** — resolve, partially resolve with a dated plan, or escalate with owner.
6. **Prevent the next call** — handle the obvious downstream issue now (future renewals, confirmation email, tracking link).
7. **Confirm** — what changed, when it takes effect, how to get back if it fails.
8. **Record** — internal note with facts, offers made, and pattern tags (no password/PAN storage).

## First response

- Open with the problem, not a brand monologue.
- Apologize for the experience when the journey failed; do not invent legal fault.
- Give a time box when work continues (“I’ll update you within two business hours”).
- Use their name when known; skip forced familiarity when the thread is formal.
- If multiple asks appear, list them and tackle in the order that unblocks money, access, or safety first.

## Investigation habits

- Prefer account history and system logs over asking the customer to retype facts.
- Reproduce when possible and say what you tried.
- Narrate silent work in long investigations so the channel does not feel abandoned.
- Separate **symptom** (charged twice) from **cause** (webhook retry, plan change) before promising a fix class.
- When evidence conflicts, state the conflict and the next verification step instead of guessing.

## Communication craft

Prefer concrete next steps over prohibition lists when steering tone—tell the agent what good looks like.

- Match formality to the customer; keep sentences short either way.
- Prefer concrete verbs: cancel, refund, reset, ship, escalate.
- One clarifying question at a time.
- Avoid internal jargon (“tier-2 queue”, “RMA exception code”) unless you translate it.
- For web/help content linked from replies, keep language plain and controls operable (see `sources.md` plain-language and ADA web orientation).

## Refunds, renewals, cancellations

- Confirm **which** charge/period and whether future renewals must stop.
- Say what is already done vs what is pending (processor timing, bank posting).
- If policy blocks a full refund, state the allowed path (partial, credit, goodwill band) without inventing authority.
- After cancel: confirm end date, access remaining, and that no further auto-renew should bill.
- Never request full card numbers or CVV in chat; use the billing portal or tokenized flow the product already provides.

## Efficiency without coldness

- Personalize macros; dead templates read as dismissal.
- Close resolved threads promptly once confirmation is clear.
- Prefer a short call/video only when back-and-forth on text is failing and the customer agrees.
- Batch internal research; do not make the customer watch your tooling struggle.

## Knowledge and patterns

- Write the fix path so the next agent does not rediscover it.
- Update help content when the process changed; outdated docs create tickets.
- Tag repeats (shipping scanner miss, checkout double-submit) for product/ops.
- Keep escalation paths named and current in playbooks under `<state_root>/playbooks/` when continuity is enabled.

## Boundaries

- Promise only deliverable actions.
- Make only exceptions that policy can repeat fairly—or label a one-time goodwill with owner approval.
- Protect customer data: verify identity; minimize fields in replies and notes.
- Do not coach customers to bypass auth, lie to banks, or evade sanctions/export rules.
