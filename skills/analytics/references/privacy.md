# Privacy, GDPR, and retention

## Consent and legal basis

- **GDPR personal data** includes identifiers that can single out a person. Product analytics that attach person profiles, emails, or stable IDs generally need a lawful basis — PostHog’s GDPR guide emphasizes **unambiguous consent** when required, secure handling, and care with EU data transfers.
- **Cookie-free ≠ consent-free in every jurisdiction**. Plausible markets no-cookie, privacy-focused analytics and publishes compliance positioning, but **EU deployments that still collect identifiers or combine logs may still need a legal review**. Do not promise “no consent banner ever” as universal law; frame it as product capability + counsel review.
- Before enabling tracking for EU visitors: confirm consent/CMP state or another documented basis, then load scripts.

Sources: https://posthog.com/docs/privacy/gdpr-compliance · https://plausible.io/privacy-focused-web-analytics

## PII boundaries

- **Exclude** email, real names, phone numbers, and raw IP addresses from custom event properties unless the user explicitly designs a compliant pipeline.
- Prefer opaque `distinct_id` / session identifiers over direct personal labels in client-side events.
- PostHog documents tooling for managing PII during collection and retention — use product controls rather than ad-hoc “we’ll scrub later”.

## Retention and deletion

Configure automatic retention/deletion in each product admin UI:

| Vendor | Where operators usually set retention |
|--------|----------------------------------------|
| Umami | Site/app settings → data retention controls (product UI) |
| Plausible | Site settings; plan limits apply — verify current plan retention rather than memorized “30 days max” |
| PostHog | Project settings + GDPR deletion / right-to-be-forgotten flows in docs |

When the user asks for a numeric retention default, **open current vendor docs or their project settings** instead of inventing a fixed number.

## Cookie-free warning (operational)

Umami and Plausible emphasize minimal/no cookie tracking. Still:

1. Check whether any first-party identifier, URL query PII, or server log join re-identifies users.
2. Keep marketing pixels and full third-party ad stacks out of “privacy-first” setups unless separately reviewed.
3. Document the legal basis in the user’s CMP or privacy notice — this skill does not replace counsel.
