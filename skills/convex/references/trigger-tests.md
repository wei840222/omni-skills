# Convex discovery trigger checks (2026-09-28)

Scope: compare the `description` at `skills/convex/SKILL.md:3` with a user intent. This is a read-only routing judgment, not an OpenClaw Skill Harness runtime activation test.

| Prompt | Expected | Description result | Reason |
|---|---|---|---|
| "How should I index notifications in my Convex app?" | trigger | trigger | Named Convex schema/index design. |
| "Stripe webhooks keep retrying my Convex HTTP action" | trigger | trigger | Named Convex webhook retry boundary. |
| "How do I migrate a field in production Convex?" | trigger | trigger | Named Convex data migration. |
| "Choose a PostgreSQL index for a notification inbox" | no trigger | no trigger | Generic relational database without Convex target; route to backend. |
| "Show me how to use the Convex optimization theorem in geometry" | no trigger | no trigger | Mathematical word overlap, not Convex backend work. |
| "Design an authorization layer for a generic REST API" | no trigger | no trigger | No Convex project; route to backend. |

Result: 3/3 positive and 3/3 near-miss distinctions by direct description inspection. Live Skill Harness router behavior remains untested.
