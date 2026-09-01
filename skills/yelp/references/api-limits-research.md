# Yelp Fusion API guidance

## API availability and rate limits

Load this reference before a live Yelp API workflow.

The current Yelp Places documentation describes a queries-per-second (QPS) limit. A `429` response with `TOO_MANY_REQUESTS_PER_SECOND` means the request rate is too high.

1. Reduce request rate and avoid concurrent retries that repeat the same failure.
2. Retry after a bounded delay. If `429` persists, end the API workflow and explain the limit.
3. Use public-page mode only when that evidence is sufficient; disclose the loss of structured API fields.

Do not state an undocumented daily quota, reset time, or GraphQL point allowance.

## Storage and display

Treat Yelp API responses as governed data. Before persisting ratings, reviews, photos, or other response content, check the current Yelp terms and API documentation for the intended use and retention period. Store only the minimal allowed task context; keep reusable business IDs or aliases separate from cached response content.

Preserve applicable attribution, branding, and linking requirements when presenting Yelp content.

## Sources

- Yelp Places API rate limiting — queries-per-second behavior and HTTP `429`: https://docs.developer.yelp.com/docs/places-rate-limiting
- Yelp Places API overview — API scope and capabilities: https://docs.developer.yelp.com/docs/places-intro
- Yelp API terms — permitted data use and display requirements: https://terms.yelp.com/api_terms
