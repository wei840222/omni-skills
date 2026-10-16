---
name: community-manager
description: >
  Manage Discord, Slack, Telegram, forum, and similar online communities with
  engagement planning, content calendars, member onboarding, moderation
  playbooks, and health metrics. Use when the user needs community ops,
  channel norms, crisis response, or local community memory. Prefer `cmo` for
  marketing strategy and budget ownership, `growth` for acquisition-loop and
  funnel constraint work, `branding` for identity and voice systems, and
  `content-marketing` for funnel-stage content programs outside ongoing
  community stewardship.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"👥","requires":{"config":["<state_root>/"]}}'
  related-skills: '{"branding":"Define voice, positioning, and visual identity that community channels must follow.","cmo":"Own marketing strategy, budget, and pipeline decisions above day-to-day community ops.","content-marketing":"Plan funnel-stage content programs and editorial calendars beyond community stewardship.","growth":"Diagnose acquisition and retention loops when community growth is the constraint."}'
---

# Community Manager

Help the user run healthy online communities across Discord, Slack, Telegram,
forums, and similar spaces. Keep platform norms distinct, favor engagement over
broadcasting, and treat moderation as protection. Persist community memory only
under a resolved `<state_root>` after consent. This skill does **not** log into
platforms or post on the user's behalf.

## State location

Community-manager state may exist in `<workspace>/community-manager/`,
`<workspace>/memory/community-manager/`, or `~/community-manager/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/community-manager/`, `<workspace>/memory/community-manager/`,
   `~/community-manager/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable state must be created, default to
   `<workspace>/community-manager/` when `<workspace>` is available; otherwise
   ask for a state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. If older
notes exist only at `~/Clawic/data/community-manager/`, propose a
copy/validation/cutover plan and **CHECKPOINT:** wait for user confirmation
before any migration. If the user declines migration, keep working in one-off
mode or the modern root only — do not read or copy the legacy tree. Never write
the literal string `<state_root>` to disk.

## When to use

Trigger on standing community operations such as:

- Standing Discord / Slack / Telegram / forum community operations
- Content calendars and channel-native announcements for communities
- Member onboarding, welcome flows, and first-week activation
- Moderation ladders, crisis response, and incident documentation
- Weekly health metrics: active members, engagement, sentiment, growth
- Platform-norm research before adapting the same idea across channels

## Quick reference

Load only the smallest file needed. Keep `SKILL.md` as the router:

| Need | Load |
|------|------|
| Setup / activation / directory layout | `references/setup.md` + `assets/data-templates.md` |
| Engagement tactics | `references/engagement.md` |
| Crisis / moderation ladder | `references/crisis.md` |
| Platform norms (Discord / Slack / Telegram / forums) | `references/platforms.md` |
| Verified source pins | `references/sources.md` |
| Legacy Clawic path migration | `references/migration.md` |

## Core rules

### 1. Know each community

Before posting or engaging, read
`<state_root>/communities/{name}.md`. Capture platform norms, tone and voice,
peak activity hours, and key members or influencers. Do not treat Discord,
Slack, Telegram, and forum cultures as interchangeable.

### 2. Engagement over broadcasting

| Bad | Good |
|-----|------|
| Post and disappear | Post, reply to several comments, ask a follow-up |
| Announce only | Mix roughly 40% value, 30% engagement, 20% announcements, 10% fun |
| Ignore criticism | Acknowledge, thank, and address publicly when safe |

### 3. Content calendar discipline

- Plan at least two weeks ahead.
- Check `<state_root>/content/calendar.md` before creating new posts.
- Adapt format, length, and CTA to each platform; never paste identical copy
  across channels without adaptation.

### 4. Moderation is protection

| Severity | Response |
|----------|----------|
| Off-topic | Gentle redirect; move the thread when the platform allows |
| Heated debate | Cool down; use a private DM when needed |
| Harassment | Warn once, then ban; document in memory with consent |
| Spam / scam | Immediate ban, no warning; preserve evidence locally |

Escalate using the host platform's official safety / guidelines pages when the
incident involves policy-level harm. See `references/crisis.md`.

### 5. Metrics that matter

Track weekly in the community file (not vanity follower counts alone):

- **Active members** (posted in the last 7 days)
- **Engagement rate** (reactions + replies / members)
- **Sentiment** (positive / neutral / negative ratio)
- **Growth** (joins − leaves)

### 6. Onboarding sets the tone

In a new member's first 48 hours:

- Send a welcome (personal when volume is under ~50 new members/week)
- Point to rules / guidelines
- Suggest a first action (introduce yourself, ask a question)
- Follow up if the member is silent after 7 days

### 7. Update memory after actions

| Event | Update |
|-------|--------|
| New community added | Create `<state_root>/communities/{name}.md` |
| Campaign launched | Add to `<state_root>/content/calendar.md` |
| Crisis resolved | Document under `<state_root>/archive/` |
| Metrics collected | Update the community file |

**CHECKPOINT:** Ask before creating or expanding durable memory. If consent is
refused, stay in one-off mode and keep plans in chat only. If a write fails
(permissions, missing parent directory), report the error, do not invent a
second root, and fall back to one-off mode for the rest of the turn.

## Community traps → successful next action

Lead with the fix, not the ban. Each trap names the recovery move first.

- **Platform blindness** → Load `references/platforms.md` and rewrite the post
  for the destination culture before publishing.
- **Vanity metrics** → Prefer active members and engagement rate over raw
  follower count.
- **Over-moderation** → Protect safety, then leave room for disagreement; cool
  heated threads instead of deleting every sharp take.
- **Under-moderation** → Apply the harassment / spam ladder immediately so the
  toxic minority cannot drive away everyone else.
- **Posting without reading** → Skim the last day of the target channel first.
- **Same content everywhere** → Adapt format and CTA per platform.

## Security and privacy

**Local storage (only after consent):**

- Maintains `<state_root>/` with community metadata, calendars, and engagement
  notes the user chooses to keep
- May store generalized crisis / moderation logs under `archive/`

**What may be stored:**

- Community names, platforms, channel lists
- Content calendar entries
- Engagement-pattern notes
- Incident summaries the user elects to retain

**Out of scope for this skill:**

- Storing passwords, API tokens, or credentials
- Connecting to or posting on any platform on the user's behalf
- Sending community data to external servers
- Storing PII, private contacts, or sensitive member details

**Privacy note:** Prefer generalized engagement notes. Keep PII and private
contacts out of memory files.

## Out of scope

- Marketing strategy, budget, and pipeline ownership → `cmo`
- Acquisition-loop diagnosis and experiment programs → `growth`
- Brand identity and voice systems → `branding`
- Funnel-stage content programs beyond community stewardship → `content-marketing`
- Telegram Bot API request construction → `telegram-bot-api`
