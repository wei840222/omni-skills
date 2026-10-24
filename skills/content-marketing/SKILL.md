---
name: content-marketing
description: Plan, create, measure, and repurpose audience-focused content across funnel stages. Use when the user needs a content strategy, editorial calendar, campaign brief, distribution plan, performance review, or content repurposing. Route paid-media execution to an advertising workflow and standalone brand identity work to the branding skill.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📝"}'
  related-skills: '{"branding": "Defines the brand voice and identity that content must follow.", "growth-hacker": "Extends content plans with growth experiments and distribution tactics.", "seo": "Optimizes discoverability and search intent for content assets.", "writing": "Drafts and edits the individual content asset."}'
---

## State location

Content-marketing state may exist in `<workspace>/content-marketing/`, `<workspace>/memory/content-marketing/`, or `~/content-marketing/`. Before reading or writing state, resolve `<state_root>` once:

1. Use an explicitly configured state path when available.
2. Otherwise use the first existing directory in this order: `<workspace>/content-marketing/`, `<workspace>/memory/content-marketing/`, `~/content-marketing/`.
3. If multiple candidate directories exist, use only the highest-precedence directory and report the duplicate state locations.
4. When no candidate exists and the user consents to saving state, create `<workspace>/content-marketing/`.

Keep the selected `<state_root>` for the entire invocation. The host supplies `<workspace>`; when it is unavailable, use an existing `~/content-marketing/`, or obtain a state location before creating data.

## Workflow

1. Establish the objective, target audience, offer, channel constraints, and success metric. For first-time setup or changes to saved strategy, read `references/setup.md`.
2. Select one funnel stage and a next action. Read `references/funnels.md` when mapping awareness, consideration, or decision-stage content.
3. Create a brief with audience problem, promise, format, owner, publication date, distribution plan, and measurement window.
4. Produce or revise the requested asset. For voice, calendar, and reusable memory structure, read `references/memory-template.md`.
5. Plan channel-native distribution and derivative assets. Read `references/repurposing.md` when adapting an existing asset into multiple formats.
6. Review results against the objective, retain learning in `<state_root>/analytics/` only with user consent, and adjust the next brief.

## Operating rules

- Match each asset to one funnel stage and one measurable next action; document any deliberate multi-stage exception.
- Preserve a single core idea across derivatives while adapting format, length, and call to action to the destination channel.
- Separate observed metrics from hypotheses. Use a defined attribution window before declaring a format successful or unsuccessful.
- Treat content strategy, drafts, calendars, audience research, and analytics as local user data. Create or modify `<state_root>/memory.md`, `<state_root>/calendar.md`, `<state_root>/content-bank/`, or `<state_root>/analytics/` only after the user consents.
- Keep the skill useful without persistent storage: provide an in-chat plan or draft when the user declines storage.

## Resource guide

| Resource | Load when |
| --- | --- |
| `references/setup.md` | Initializing or updating saved content strategy, voice, or calendar state |
| `references/funnels.md` | Choosing a funnel stage, CTA, or content intent |
| `references/repurposing.md` | Turning a source asset into channel-specific derivatives |
| `references/memory-template.md` | Creating or changing the consented local state structure |
| `references/research.md` | Checking the foundational sources and evidence behind this skill |
| `references/core-rules.md` | Auditing a plan for common execution failures |

## Common mistakes

- A calendar without an audience problem, funnel stage, or measurement rule is a publishing list, not a strategy.
- Reuse the idea, not a verbatim post: fit derivatives to each channel's audience and format.
- Obtain consent before creating persistent files. Keep user data local; use an external destination only after separate authorization.
