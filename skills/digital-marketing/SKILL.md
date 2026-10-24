---
name: digital-marketing
description: >
  Plan and optimize digital marketing systems across market modeling, channel
  orchestration, short-form video, funnels, measurement, and revenue experiments.
  Use when the user needs launch planning, growth marketing, full-funnel
  execution, trend response, content-to-revenue systems, or coordinated paid plus
  organic campaigns. Prefer `content-marketing` for editorial calendars alone,
  `seo` for search-intent work, `growth-hacker` for ICE experiments and viral
  loops, `email-marketing` for deliverability and sequences, and `tiktok-ads`
  for TikTok paid creative specifics.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"📈","requires":{"config":["<state_root>/"]},"os":["linux","darwin","win32"],"displayName":"Digital Marketing"}'
  related-skills: '{"content-marketing": "Editorial planning and repurposing when the ask is content systems, not full-funnel orchestration.", "email-marketing": "Deliverability, segmentation, and campaign sequences as the owned channel.", "growth-hacker": "Experiment backlog, viral loops, and unconventional acquisition tactics.", "seo": "Search intent, technical fixes, and ranking workflows instead of multi-channel campaign ownership.", "tiktok-ads": "Platform-specific short-form paid creative rules on TikTok."}'
---

## State location

Digital-marketing state may exist in `<workspace>/digital-marketing/`, `<workspace>/memory/digital-marketing/`, or `~/digital-marketing/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/digital-marketing/`, `<workspace>/memory/digital-marketing/`, `~/digital-marketing/`.
3. If none exists and state must be created, default to `<workspace>/digital-marketing/` after the user consents.
4. If more than one candidate exists, use the highest-precedence directory and tell the user that other copies were found. Leave the other copies untouched.
5. If `<workspace>` cannot be resolved, read an existing `~/digital-marketing/` only. Otherwise ask for a state root before creating files.

Use the selected `<state_root>` for every state operation in this skill. Never write the literal string `<state_root>` to disk. Treat legacy `~/Clawic/data/digital-marketing/` as a migration source only—ask before migrating.

## Setup

On first use, read `references/setup.md` for activation and consent. This skill works without local storage. Only create `<state_root>/` if the user wants ongoing continuity.

## When to Use

User needs one system for digital marketing, growth marketing, or full-funnel execution. Agent handles market modeling, messaging, content, SEO coordination, short-form video, lifecycle campaigns, paid and organic orchestration, and performance review.

Use this when the problem is orchestration, not a single channel in isolation. The goal is to turn business priorities into assets, campaigns, experiments, and clear next actions.

This skill is especially strong when the user needs launch planning, trend response, content-to-revenue systems, or one operator that can connect demand creation with demand capture.

Skip loading this skill for pure editorial calendars (`content-marketing`), search-only work (`seo`), ICE experiment design without channel orchestration (`growth-hacker`), email deliverability (`email-marketing`), or TikTok Ads Manager specifics (`tiktok-ads`).

## Architecture

Local workspace is optional and only created with user consent.

```text
<state_root>/
├── memory.md        # Business context, winning angles, active constraints
├── campaigns.md     # Current campaign plans and channel bundles
├── experiments.md   # Tests, thresholds, outcomes, next steps
└── signals.md       # Metrics, anomalies, and reusable learnings
```

## Quick Reference

Load only the file needed for the current bottleneck. Prefer `references/market-model.md` before channel or creative work.

| Topic | When to load | File |
|-------|--------------|------|
| Setup and activation | First use, consent, storage decision | `references/setup.md` |
| Continuity memory semantics | Persistent status values and support files | `references/memory.md` |
| Data templates | Creating memory/campaigns/experiments/signals files | `assets/data-templates.md` |
| Market model and message map | Before drafting campaigns or channel plans | `references/market-model.md` |
| Channel orchestration | Turning one thesis into channel bundles | `references/channel-system.md` |
| Native short-form video | Viral/testing hooks and creator-style cuts | `references/short-form-video.md` |
| Funnel and lifecycle ops | Route-to-value and conversion paths | `references/funnels.md` |
| Measurement and reviews | KPI trees, UTM, weekly keep/kill/scale/recycle | `references/measurement.md` |
| Experiment backlog | Hypotheses, thresholds, kill rules | `references/experiments.md` |
| Launch / trend / retention playbooks | Speed execution sprints | `references/playbooks.md` |
| Research sources | Refreshing domain claims with primary URLs | `references/sources.md` |

## Core Rules

### 1. Model the market before touching channels
- Define audience, buying trigger, painful problem, offer, proof, and objection before drafting assets.
- If those pieces are blurry, outputs become generic and channel execution turns into guesswork.
- Use `references/market-model.md` to build a minimal message map first.

### 2. One growth thesis must drive every channel
- Start with one clear angle, then adapt it for SEO, content, social, video, email, and paid media.
- Organic signals should inform paid creative. Paid winners should feed new organic content.
- Use `references/channel-system.md` to decide what each channel is supposed to do in the same campaign.

### 3. Treat short-form video as the fastest message lab
- Test hooks, claims, objections, and demos in short-form before scaling a narrative everywhere else.
- Native cuts, captions, proof moments, and comment mining matter more than polished production.
- Use `references/short-form-video.md` when the user wants viral growth, creator-style content, or fast creative iteration.

### 4. Build full-funnel systems, not isolated campaigns
- Every acquisition push needs a conversion path: traffic source, landing angle, CTA, follow-up, retargeting, and handoff.
- Traffic without route-to-value creates vanity metrics and wasted spend.
- Use `references/funnels.md` to map channel-to-offer paths before launch.

### 5. Operate on leading indicators and revenue together
- Track both early signals and business outcomes: hook rate, CTR, reply quality, conversion rate, CAC, payback, and influenced pipeline.
- Never recommend channel changes from impressions or views alone.
- Use `references/measurement.md` for KPI trees, anomaly triggers, and review cadence.

### 6. Every campaign ships with tests, kill rules, and recycling rules
- Launch with specific hypotheses, test cells, thresholds, and next actions if a variant wins or loses.
- Reuse winning hooks across ads, landing pages, emails, and short-form video.
- Use `references/experiments.md` to keep activity compounding instead of restarting every week.

### 7. Escalate risky claims and irreversible actions
- Treat pricing claims, competitor comparisons, regulated statements, and high-spend decisions as approval moments.
- Do not invent proof, testimonials, performance claims, or customer language.
- Prefer clear caveats and human review over persuasive but unsupported marketing.
- Refresh contested numbers from `references/sources.md` instead of model memory.

## Operating Rhythm

### Daily
- Watch for spend spikes, CTR drops, broken follow-up, low-quality leads, and message fatigue.
- Pull the clearest signal from comments, replies, search queries, or sales feedback.

### Weekly
- Pick one growth thesis, one channel bundle, and up to three meaningful experiments.
- Publish one core idea, then repurpose it across formats instead of starting from zero each time.
- End the week with keep, kill, scale, and recycle decisions.
- If no experiment had a named win/kill threshold, stop launching new tests until the backlog uses `references/experiments.md`.

### Monthly
- Reallocate effort based on payback, lead quality, content compounding, and conversion path health.
- Refresh stale offers, hooks, and landing angles before adding more channels.

## Common Traps

- Starting with channels instead of buyers and triggers → activity rises but message-market fit stays weak.
- Chasing virality without a capture path → views grow while leads and revenue stay flat.
- Cross-posting the same asset everywhere → each platform underperforms because format and expectation differ.
- Treating organic and paid as separate worlds → learnings stay siloed and creative fatigue arrives faster.
- Measuring clicks without lead quality or payback → cheap traffic hides bad economics.
- Scaling spend before fixing landing friction or follow-up → CAC rises because the funnel leaks downstream.
- Publishing high-volume AI content without proof or specificity → content looks busy but builds no trust.

## Security & Privacy

**Data that stays local when the user opts in:**
- Business context, channel priorities, and winning angles in `<state_root>/`
- Campaign plans, experiment logs, and review notes in local markdown files

**This skill does NOT:**
- Automatically post content, buy ads, or spend money
- Create local files without explicit user consent
- Access ad accounts, analytics tools, or third-party platforms unless the user explicitly requests a separate tool workflow
- Make undeclared network requests

**Guardrails:**
- Treat external metrics as user-provided unless a separate approved integration is used
- Flag unsupported claims, sensitive categories, and compliance-heavy copy for review
- Never store live credentials or account tokens in the skill package or in git
