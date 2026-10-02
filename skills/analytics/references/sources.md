# Gate 6 sources (verified at handoff)

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| Plausible Stats API v2 | Plausible Docs — Stats API | https://plausible.io/docs/stats-api | Bearer auth; `site_id` is the registered domain string in examples; default **600 req/hour** per API key. |
| Plausible Events API | Plausible Docs — Events API | https://plausible.io/docs/events-api | Direct event recording with JSON `name`/`url`/`domain`; 202 responses. |
| Plausible script / SPA | Plausible Docs — Script extensions | https://plausible.io/docs/script-extensions | Manual pageviews and extensions when default load behavior is insufficient. |
| Plausible privacy positioning | Plausible — Privacy-focused analytics | https://plausible.io/privacy-focused-web-analytics | No-cookie / minimal collection product stance; still pair with legal review for identifiers. |
| Umami API overview | Umami Docs — API | https://docs.umami.is/docs/api | Self-host `/api` vs Cloud `https://api.umami.is` + API key. |
| Umami auth | Umami Docs — Authentication | https://docs.umami.is/docs/api/authentication | `Authorization: Bearer <api-key>`; Cloud is API-key only. |
| Umami send | Umami Docs — Sending stats | https://docs.umami.is/docs/api/sending-stats | `POST /api/send` with `payload.website` website ID. |
| Umami tracker | Umami Docs — Tracker configuration | https://docs.umami.is/docs/tracker-configuration | `data-website-id`, `data-host-url`, `data-domains`, manual pageviews. |
| PostHog API overview / limits | PostHog Docs — API | https://posthog.com/docs/api | Private endpoint rate limits; public capture POSTs treated differently; correct regional hosts. |
| PostHog capture / batch | PostHog Docs — Capture API | https://posthog.com/docs/api/capture | `/i/v0/e` and `/batch` as primary event ingress with project token. |
| PostHog event capture guide | PostHog Docs — Capturing events | https://posthog.com/docs/product-analytics/capture-events | Batch examples and property payload shape. |
| PostHog GDPR | PostHog Docs — GDPR compliance | https://posthog.com/docs/privacy/gdpr-compliance | Unambiguous consent when required; PII controls; deletion flows. |
| Agent Skills format | Agent Skills specification | https://agentskills.io/specification | Frontmatter, progressive disclosure, package layout. |
| Reference validator | agentskills / skills-ref | https://github.com/agentskills/agentskills/tree/main/skills-ref | `uvx --from skills-ref agentskills validate skills/analytics`. |

### Obsolete or softened claims from the pre-refactor body

- **“PostHog 1000/minute”** — not used as a hard limit. Current public docs describe private-endpoint budgets (including ~600/min personal-key cases and 480/min · 4800/hour class limits) and state public capture POSTs are not rate limited the same way.
- **“Plausible 30 days max” retention** — not restated as a universal ceiling; operators must read current plan/site settings.
- **“Never need consent if cookie-free”** — reframed: product may avoid cookies, but GDPR still hinges on personal data and lawful basis.
