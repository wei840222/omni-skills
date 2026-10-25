---
name: outreach
description: >
  Plan, personalize, and track multi-touch outreach for sales, PR/media,
  SEO link building, recruiting, and partnership/investor asks. Use when
  drafting cold email or LinkedIn sequences, choosing timing and cadence,
  pitching journalists with exclusives, qualifying guest-post or broken-link
  targets, writing recruiting InMails, logging response patterns, or deciding
  when to stop. Prefer `crm` for durable pipeline records, `b2b` for single-deal
  MEDDIC strategy, `recruiter` for hiring process beyond copy, `seo` for SEO
  strategy beyond link outreach, `influencer` / `affiliate-marketing` for
  creator or affiliate partner programs, and `email-marketing` for owned-list
  nurture rather than cold first-touch.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📣"}'
---

# Outreach

Campaign-level guidance for cold and warm outreach across sales, PR, SEO link
building, recruiting, and BD. Advise by default. Draft messages only when asked;
the user sends, offers exclusives, and owns compliance.

Load `references/sources.md` before restating CAN-SPAM/PECR rules, Gmail sender
thresholds, LinkedIn InMail limits, or numeric response benchmarks.

## State location

Optional campaign memory may exist in `<workspace>/outreach/`,
`<workspace>/memory/outreach/`, or `~/outreach/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when the user or host supplies one.
2. Otherwise use the first existing directory in this order:
   `<workspace>/outreach/`, `<workspace>/memory/outreach/`, `~/outreach/`.
3. If several candidates exist, use only the highest-precedence directory,
   report the split copies, and do not merge or cross-write.
4. If none exists and durable notes are needed, create
   `<workspace>/outreach/` when `<workspace>` is available; otherwise ask for
   a state root before creating data.

Use the selected `<state_root>` for every state operation in this skill.
Keep it fixed for the rest of the invocation. Never write the literal string
`<state_root>` to disk. Do not write runtime state into this skill package.

Suggested layout once persistence is enabled:

```text
<state_root>/memory.md
<state_root>/campaigns/<slug>.md
<state_root>/exclusives.md
<state_root>/suppression.md
```

Legacy Clawic paths (`~/Clawic/data/outreach/`, `~/clawic/outreach/`) are
migration sources only — offer copy / validate / cutover / rollback; do not
silently move or delete them.

## When to use

- Drafting cold email, LinkedIn, or multi-channel sequences with a clear ask
- Choosing timing, follow-up cadence, and when to close the loop
- PR/media pitches that need a news hook and exclusive discipline
- SEO outreach: guest posts, resource pages, broken-link replacements
- Recruiting first-touch that references specific work
- Investor/BD asks when a warm path is unavailable
- Logging what worked so the next campaign improves

Hand off when a sibling owns the job:

| Job | Skill |
|-----|-------|
| CRM records, imports, do-not-contact list as system of record | `crm` |
| One enterprise deal / MEDDIC / forecast | `b2b` |
| Hiring process after the first reply | `recruiter` |
| SEO strategy beyond earning links | `seo` |
| Creator/affiliate program operations | `influencer` / `affiliate-marketing` |
| Owned-list nurture after consent | `email-marketing` |
| Term bargaining once interest exists | `negotiate` |

## Situation detection

| Context | Load |
|---------|------|
| Cold emails, follow-ups, subject lines, objection replies | `references/templates.md` |
| Sales / PR / SEO / recruiting / BD playbooks | `references/by-type.md` |
| Response logging, exclusives, benchmarks, re-engage lists | `references/tracking.md` |
| Verified sources for compliance and craft claims | `references/sources.md` |

## Universal rules

**The Formula:** Who (verified contact) + Why Now (trigger) + WIIFT (their gain).

**Personalization:** Cite something specific — not "loved your work" but "your
piece on X changed how I think about Y." If no hook exists, research further
before drafting.

**Timing (default guidance, not a guarantee):**
- Prefer Tuesday–Thursday mornings in the recipient's timezone when no better
  signal exists
- Prefer those windows over Monday-morning blasts, Friday afternoons, holidays,
  and major news days unless the news *is* the hook
- If they just posted or published, strike while relevant

**Follow-up cadence:**

| Touch | Timing | Purpose |
|-------|--------|---------|
| 1 | Day 0 | Value-first intro, specific ask |
| 2 | Day 3–5 | New angle or additional value |
| 3 | Day 7–10 | Different channel when available |
| 4 | Day 14+ | Break-up / close-the-loop email |

Conclude after 3–4 touches. "Bumping this up" without new value is spam.

## Quick checks

**Before sending:**
- [ ] Verified email (prefer named inbox over generic info@)
- [ ] Personalization hook is specific
- [ ] Cold body under ~150 words
- [ ] Links instead of attachments for first touch
- [ ] Clear CTA (specific ask, not "let me know")
- [ ] Subject under ~50 characters (mobile preview often cuts earlier)
- [ ] Suppression / exclusive / do-not-contact checked when those lists exist

**Anti-patterns (rewrite before send):**
- "I came across your profile..." with no proof of research
- Full pitch in the first message when curiosity would open the door
- "Per my last email..." guilt framing
- Asking for "exposure" without budget or a concrete mutual exchange
- Parallel exclusive angles to competing outlets

## Compliance and delivery

- Treat commercial email as regulated: identify the sender, avoid deceptive
  subjects, honor opt-out, and keep a suppression list under `<state_root>/`
  when persistence is enabled (`references/sources.md` — US CAN-SPAM / UK PECR)
- Prefer authenticated, low-complaint sending practices; Gmail sender guidelines
  apply when volume grows (`references/sources.md`)
- LinkedIn connection notes and InMails have hard length and product limits —
  keep first touches shorter than email (`references/sources.md`)
- Credentials, ESP API keys, and scraped contact dumps stay outside
  `<state_root>/`

## Outreach profile

Build over time in `<state_root>/memory.md` after campaigns:

### What works
<!-- "Subject: question format lifted opens" "Tue 10am local best" -->

### What fails
<!-- "Long emails ignored" "Connect-only LinkedIn <10% accept" -->

### Templates that convert
<!-- "Follow-up #2: new value + same ask" -->

### Channel preferences by persona
<!-- "Execs: email via EA" "Journalists: email > DM" -->

### Archived contacts
<!-- "Reporter X: rarely responds" "VC Y: requires warm intro" -->

Empty means nothing learned yet. Update after every campaign.

## Output gates

Before delivering a draft or cadence plan:

- Is the Who / Why Now / WIIFT explicit and evidence-bound?
- Did I check suppression, exclusives, and sibling ownership (`crm` / `b2b` / …)?
- Are numeric benchmarks labeled as directional, with sources loaded when quoted?
- If durable learning appeared, is it written under `<state_root>/`?
