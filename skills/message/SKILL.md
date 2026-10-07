---
name: message
description: >
  Draft and route outbound messages across Slack, email, Discord, Telegram,
  WhatsApp, iMessage, and X without social disasters. Use when sending or
  replying on the user's behalf; when tone, channel, timing, or escalation is
  unclear; when a draft might commit money, legal terms, dates, or availability;
  when a high-stakes contact (investor, board, press, lawyer, angry client) is
  involved; or when matching the user's brevity and platform formatting matters.
  Not for inbox triage queues (`email-management`), marketing copy systems
  (`copywriting`), pure prose voice work (`writing`), durable ask-vs-act policy
  (`escalate`), or provider APIs (`telegram-bot-api`, `whatsapp-business-api`).
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"💬"}'
  related-skills: '{"escalate":"Durable ask-vs-act thresholds when the decision is policy, not a single draft.","writing":"Long-form voice, structure, and rewrite craft beyond a single outbound message.","email-management":"Inbox triage, follow-up tracking, and thread queues rather than one-off sends.","customer-support":"Support empathy and issue resolution patterns when the thread is a customer case.","copywriting":"Persuasive marketing copy and CTA systems rather than interpersonal sends.","chat":"General conversational patterns when the task is dialogue design, not channel-safe delivery."}'
---

## When to use

Load this skill when the deliverable is an outbound message (or a decision not to send yet) on a real channel. Prefer siblings when the job is broader:

- `email-management` for inbox queues and follow-up ledgers
- `writing` for essays, memos, or multi-paragraph voice work
- `copywriting` for ads, landing pages, and campaign CTAs
- `escalate` for standing autonomy policy across many actions
- `telegram-bot-api` / `whatsapp-business-api` for provider HTTP APIs

## Workflow

Execute in order. Stop early only when a step already blocks send.

1. **Classify stakes** — Read `references/escalation.md`. If any financial, legal, high-stakes relationship, emotional, first-contact, or keyword trigger matches, draft for review and do not send.
2. **Pick channel and timing** — Read `references/core-rules.md` sections 4–5. Match urgency to channel; delay 3 AM recipient-local sends.
3. **Match voice** — Read `references/tone.md`. Mirror the user's last ~5 messages for length, emoji, greeting, and cadence.
4. **Format for the platform** — Read `references/platforms.md` for the target channel only.
5. **Trap check** — Scan `references/common-traps.md` before the final draft.
6. **Deliver** — Return the draft, the intended channel, and whether send is blocked pending approval. Send only with explicit current-task authorization when the message is low-stakes and non-committing.

## Quick reference

| Need | Load |
|------|------|
| Commitments, urgency, context checks | `references/core-rules.md` |
| Review-before-send matrix + keywords | `references/escalation.md` |
| Formal ↔ casual spectrum | `references/tone.md` |
| Channel formatting limits | `references/platforms.md` |
| Social foot-guns | `references/common-traps.md` |
| Verified sources | `references/sources.md` |

## Output shape

Every reply that prepares a message should include:

1. **Channel + audience** — where it goes and who sees it
2. **Risk call** — send-ready vs draft-for-review (with trigger cited)
3. **Draft** — platform-safe text only
4. **Open questions** — missing facts that would change the send
