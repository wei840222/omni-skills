# Troubleshooting — Fox News Desk

## RSS feed is slow or empty

Symptoms:
- Feed returns stale items or no visible headlines.

Actions:
1. Fall back to the matching section page on `foxnews.com`.
2. Compare the latest feed against the section page before claiming nothing changed.
3. Label the result as a page-based read instead of an RSS sweep.

## Live coverage is gated or the index is missing

Symptoms:
- `/live-news` index returns 404, a stream asks for provider login, or the page is video-heavy without enough text.

Actions:
1. Discover a current event slug from homepage/section links and open that event page.
2. Fall back to `video` clips or the closest section article.
3. State the access boundary instead of pushing credentialed playback.

## Opinion and news keep mixing

Symptoms:
- Search results or homepage links include opinion content in a straight-news request.

Actions:
1. Re-route to the specific section feed or page.
2. Exclude `opinion` unless the user asked for it.
3. Relabel any ambiguous item before keeping it in the briefing.

## Story feels too one-sided

Symptoms:
- The user wants analysis, controversy review, or credibility checking.

Actions:
1. Keep the Fox summary as the first block.
2. Add one or more independent follow-up sources as a separate block.
3. State clearly where the extra context came from and why it was added.
