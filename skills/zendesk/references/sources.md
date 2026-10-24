# Official Sources & Technical Specifications

This document records the official developer documentation and API reference for Zendesk Support.

## Official Zendesk Developer Documentation

- **Zendesk Developer Portal**: [https://developer.zendesk.com/](https://developer.zendesk.com/)
  - Developer platform overview, app framework, API conventions, and webhook/event integrations.
- **Zendesk Support REST API v2 (Tickets)**: [https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/](https://developer.zendesk.com/api-reference/ticketing/tickets/tickets/)
  - Ticket management endpoints (`GET /api/v2/tickets`, `POST /api/v2/tickets`, `PUT /api/v2/tickets/{id}`), sideloading options, comment formatting, and custom field values.
- **Zendesk API Rate Limits & Policies**: [https://developer.zendesk.com/api-reference/introduction/rate-limits/](https://developer.zendesk.com/api-reference/introduction/rate-limits/)
  - Per-minute rate limit calculations across subscription plans, `Retry-After` header handling, and safe exponential backoff strategies for HTTP 429 responses.
