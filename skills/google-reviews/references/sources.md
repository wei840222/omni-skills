# Sources — Google Reviews

Last checked: 2026-10-07 (handoff research pass). Re-check live official pages before asserting endpoint fields, reply policy, quota, or product availability for a specific account.

## Google Business Profile reviews

- Work with review data (list/get/reply/delete tutorial): https://developers.google.com/my-business/content/review-data
- REST resource `accounts.locations.reviews`: https://developers.google.com/my-business/reference/rest/v4/accounts.locations.reviews
- list: https://developers.google.com/my-business/reference/rest/v4/accounts.locations.reviews/list
- get: https://developers.google.com/my-business/reference/rest/v4/accounts.locations.reviews/get
- updateReply: https://developers.google.com/my-business/reference/rest/v4/accounts.locations.reviews/updateReply
- deleteReply: https://developers.google.com/my-business/reference/rest/v4/accounts.locations.reviews/deleteReply
- Manage customer reviews (Help Center; verification and reply policy): https://support.google.com/business/answer/3474050?hl=en
- Business Profile API overview: https://developers.google.com/my-business

## Places / Maps review signals

- Place Details (New): https://developers.google.com/maps/documentation/places/web-service/place-details
- Places API place resource reference: https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places
- Place Reviews (Maps JavaScript): https://developers.google.com/maps/documentation/javascript/place-reviews
- Legacy Place Details (compatibility checks): https://developers.google.com/maps/documentation/places/web-service/legacy/details

## Shopping / merchant / structured review context

- Merchant API landing: https://developers.google.com/merchant/api
- Merchant API REST reference index: https://developers.google.com/merchant/api/reference/rest
- Review snippet structured data (Search Central): https://developers.google.com/search/docs/appearance/structured-data/review-snippet
- Product structured data including product reviews section: https://developers.google.com/search/docs/appearance/structured-data/product#product-reviews

## Practical use rule

Use these sources when answering:

- owner-side Business Profile review list/reply capabilities and policy timing
- whether a Places field mask can return ratings/reviews for the configured API
- product versus location review boundaries for Shopping / merchant contexts
- attribution and public-display expectations for review text

Prefer the live official page over cached skill prose for account eligibility, API availability, and reply moderation behavior. If an endpoint or product surface is unavailable for the user's project, say so and fall back to export or user-approved page verification.
