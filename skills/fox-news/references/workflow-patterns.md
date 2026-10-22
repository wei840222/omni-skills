# Workflow Patterns — Fox News Desk

Use these patterns to keep Fox-specific work focused and auditable.

## Section sweep

1. Confirm which section matters most.
2. Pull one official feed or section page from `feed-map.md`.
3. Return 3–7 items with timestamps and surface labels.
4. Offer follow-up only for the items the user selects.

## Breaking event follow-through

1. Discover the current event live-page slug from homepage/section links (the `/live-news` index itself 404s).
2. Open **one** `https://www.foxnews.com/live-news/<slug>` page and note the latest update time before summarizing.
3. If the user wants context, add the nearest section page or one related article.
4. If the claim is contested, add at least one independent follow-up source and label it clearly as outside verification.

## Opinion or host-focused read

1. Confirm the user wants opinion, host commentary, or show clips rather than straight reporting.
2. Route to `opinion`, `video`, or `shows` — not the general latest feed.
3. Label the output as opinion, segment, or commentary before summarizing.

## Multi-link handling

1. Show the candidate links with section labels.
2. Ask the user to choose one, or confirm opening several.
3. Require explicit confirmation before opening more than one link.
4. Report exactly what was opened or fetched.

## App and device support

1. Use the apps/products page for official product entry points.
2. Use public help or product pages to confirm supported devices, login expectations, or playback limitations when reachable.
3. If playback is gated, pivot to public clips or written coverage instead of asking for credentials.
