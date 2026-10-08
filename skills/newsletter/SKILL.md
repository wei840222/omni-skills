---
name: newsletter
description: >
  Advise on email newsletter strategy: subject lines, preview text, issue structure,
  cadence, list growth, landing pages, welcome sequences, segmentation, deliverability
  (SPF/DKIM/DMARC, one-click unsubscribe), metrics, sponsorships, and re-engagement.
  Use when starting a newsletter, fixing low opens/clicks, improving inbox placement,
  planning monetization, or cleaning an inactive list. Not for one-off interpersonal
  sends (`message`), marketing landing-page systems (`copywriting`), long-form prose
  craft (`writing`), or inbox triage queues (`email-management`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📧"}'
  related-skills: '{"copywriting":"Landing pages, lead magnets, and campaign CTAs beyond newsletter issue craft.","writing":"Long-form voice and rewrite craft when the deliverable is prose quality, not list ops.","message":"One-off interpersonal or channel-safe outbound drafts rather than broadcast list sends.","email-management":"Inbox triage and follow-up queues rather than publishing a list.","growth":"Broader acquisition systems when email is only one channel."}'
---

# Newsletter strategy

Stateless domain skill for **email newsletter creation, growth, deliverability, metrics, and monetization**. It does not store ESP credentials, subscriber lists, or campaign history in the package.

## When to load

Load when the user needs:

- start a newsletter (positioning, cadence, welcome sequence, landing page)
- raise opens/clicks with subject lines, preview text, structure, or list hygiene
- fix deliverability (auth, complaints, unsubscribes, warm-up)
- segment, re-engage, or clean inactive subscribers
- monetize via sponsorships, premium tiers, products, or affiliates

Hand off when a sibling owns the job:

| Job | Skill |
| --- | --- |
| One-off interpersonal send / tone on a channel | `message` |
| Landing-page / ad CTA systems | `copywriting` |
| Long-form prose voice beyond an issue draft | `writing` |
| Inbox triage and follow-up ledgers | `email-management` |
| Multi-channel acquisition systems | `growth` |

## Core path

1. **Clarify job** — launch, content craft, growth, deliverability, metrics, or monetization.
2. **Constraints first** — audience, cadence capacity, ESP, geography (compliance differs), and whether mail is marketing vs transactional.
3. **Load depth on demand** — prefer one section of `references/domain.md` over the whole file.
4. **Cite fragile facts** — auth thresholds, complaint rates, bulk-sender rules, and legal requirements only after `references/sources.md` (and re-check the live page before the user changes DNS or contracts an ESP).
5. **One next action** — a concrete subject test, auth checklist, win-back step, or sponsor brief beats a generic “best practices” dump.

## Depth on demand

| Need | Load |
| --- | --- |
| Subject lines, structure, growth, metrics, monetization, traps | `references/domain.md` |
| Official sender requirements and citation rules | `references/sources.md` |
| Evaluation harness only | `test-prompts.json` |

## Safety defaults

- Do not invent ESP pricing, inbox placement guarantees, or jurisdiction-specific legal advice from memory.
- Never recommend purchased lists, scraped addresses, or hiding unsubscribe controls.
- Treat subscriber PII and ESP API keys as secrets; keep them out of skill files and examples.
- For commercial US email, surface CAN-SPAM obligations (honest headers, physical address, working opt-out) and note other regions need local counsel — this skill is strategy guidance, not legal representation.
- Prefer organic permission-based lists and measurable experiments over vanity open-rate targets inflated by Apple Mail Privacy Protection.
