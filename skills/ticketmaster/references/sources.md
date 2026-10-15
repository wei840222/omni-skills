# Ticketmaster Sources

Verified against official Ticketmaster developer documentation during this
refactor. Prefer these pages over model memory when quotas, paging, or endpoint
shapes change.

## Official documentation

| Topic | URL | Notes verified here |
|-------|-----|---------------------|
| Discovery API v2 | https://developer.ticketmaster.com/products-and-docs/apis/discovery-api/v2/ | Event/venue/attraction/classification paths; deep paging boundary `size * page < 1000`; `apikey` query parameter |
| Getting started / rate limits | https://developer.ticketmaster.com/products-and-docs/apis/getting-started/ | Default quota 5000 calls/day; 5 requests/second; response headers `Rate-Limit*` and HTTP 429 over quota |

## Domain facts pinned from those sources

- Open Discovery surface is search and lookup. Cart, checkout, hold, and partner
  offer mutation flows are outside this skill.
- Deep paging is supported only while `size * page < 1000`.
- Default quota is 5000 API calls per day with 5 requests per second unless
  Ticketmaster raises the limit for an application.
