---
name: tiktok-ads
description: >
  Plan and optimize TikTok Ads Manager campaigns: Spark Ads, native creative,
  auction structure, budgets, learning-phase pacing, Custom Audiences, Pixel +
  Events API measurement, and iOS 14.5+ dedicated campaign limits. Use when the
  user asks for TikTok paid media setup, Spark/boost mechanics, TikTok CPA/ROAS
  diagnosis, or TikTok-specific auction rules. Prefer `ads` for cross-platform
  paid strategy, `ugc` for organic creator briefs before Spark, and
  `apple-search-ads` for iOS Search Ads.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"📱"}'
  related-skills: '{"ads":"Cross-platform paid acquisition principles when TikTok is one channel among Meta/Google/LinkedIn/YouTube.","apple-search-ads":"iOS App Store search campaigns and SKAN/AdServices attribution outside TikTok auction ads.","content-marketing":"Owned funnel content programs that paid TikTok traffic may feed.","copywriting":"Headline/body/CTA craft without TikTok Ads Manager mechanics.","digital-marketing":"Channel-mix planning around TikTok paid placements.","ugc":"Creator briefs and organic short-form craft before Spark authorization or boost.","video-captions":"Burn-in caption mechanics for sound-off TikTok creative.","video-generation":"Synthetic/video-model pipelines when generating TikTok creatives."}'
---

## When to load

Load this skill for **TikTok Ads Manager** work: Spark Ads, auction campaign structure, TikTok budgets and learning-phase pacing, Custom/Lookalike audiences, Pixel + Events API measurement, and iOS 14.5+ dedicated campaign constraints.

Route elsewhere when the ask is broader paid media (`ads`), organic creator briefs without ad-account mechanics (`ugc`), pure copy (`copywriting`), or Apple Search Ads (`apple-search-ads`).

## Resource guide

| Resource | Load when |
| --- | --- |
| `references/campaign-ops.md` | Structuring campaigns/ad groups, bidding posture, learning-phase edits, scaling budgets |
| `references/creative-and-spark.md` | Native creative rules, Spark Ads authorization, captions, creative refresh |
| `references/audiences-and-measurement.md` | Custom/Lookalike audiences, Pixel + Events API, attribution caveats, iOS 14.5+ dedicated campaigns |
| `references/sources.md` | Re-opening official TikTok Ads Manager / Business Help URLs before stating live limits |

## Operating rules

1. Treat TikTok Ads Manager UI labels, budget floors, campaign quotas, and authorization durations as **live facts**. Open `references/sources.md` and the linked help article before asserting a number that can change.
2. Keep `SKILL.md` as the router. Open one reference file for the current task; do not dump every tactic into the first reply.
3. Separate **platform floors** (documented minima) from **performance heuristics** (directional creative/testing advice). Label heuristics as heuristics.
4. Prefer native vertical creative and Spark Ads from proven organic posts when the goal is auction performance with social proof.
5. For web conversions, plan Pixel + Events API together with deduplication rather than Pixel alone.
6. Keep ad-account secrets, Spark authorization codes, customer lists, and private analytics out of the skill package and out of git.

## Decision shortcuts

- **New conversion campaign**: one objective per campaign → enough budget to clear documented floors → 3–5 ad groups / 3–5 creatives → lock major edits while learning → measure with Pixel + Events API.
- **Organic winner ready to pay**: Spark Ads path in `references/creative-and-spark.md` (authorize post, preserve engagement on the organic asset).
- **CPA unstable after launch**: check learning-phase edits, budget step size, creative fatigue, and signal loss (iOS / Pixel gaps) via `references/campaign-ops.md` and `references/audiences-and-measurement.md`.
- **iOS app promotion post-ATT**: use TikTok's iOS 14.5+ dedicated campaign product and quota rules; do not mix assumptions from Android auction data.

## Freshness

Open `references/sources.md` before quoting live floors, quotas, or authorization UI labels.
