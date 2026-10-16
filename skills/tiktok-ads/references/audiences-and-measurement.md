# Audiences and measurement — TikTok Ads

## Custom Audiences

From TikTok **About Custom Audiences** (verify live):

- Build from customer file, website/app activity, engagement, lead gen, shop activity, partners, and related sources.
- A Custom Audience needs **1,000 total matched users** before it can be used in an ad group.
- Common uses: retarget engagers, exclude recent converters, seed Lookalikes.
- Use the in-product **Available Audience** estimator; matched size ≠ deliverable reach (opt-in, age, location, and other filters apply).

## Lookalike audiences

Treat Lookalike percentages and seed quality as account-specific. Open TikTok’s Lookalike best-practice article before asserting that a TikTok 1% is “broader than Meta 1%” as a universal fact.

## Measurement

From TikTok **About TikTok Pixel** and **About Events API** (verify live):

- Pixel shares website events for measurement, optimization, and audience building.
- Events API sends server-side (and multi-channel) events; for web conversions TikTok recommends **Pixel + Events API with deduplication**.
- Pixel or Events API setup is a prerequisite for the Web Conversions objective.
- Expect browser/ATT gaps; reconcile platform-reported conversions with revenue systems.

Attribution windows, view-through defaults, and modeled conversions change with product settings — read the live Events Manager / reporting docs for the account’s configuration instead of hard-coding window lengths here.

## iOS 14.5+ dedicated campaigns

From TikTok iOS 14.5+ dedicated-campaign help (verify live):

- TikTok supports **dedicated campaigns** that only include iOS 14.5+ users for registered apps.
- Product limits apply (help text documents a cap such as **15 dedicated campaign IDs per iOS app** — confirm current quota in-product).
- Keep iOS dedicated delivery and reporting mentally separate from Android/web auction learning; edits and quotas follow the dedicated-campaign ruleset.
