# Setup - Convex

Read this when the resolved `<state_root>/` is missing or empty. Follow the resolver and consent rule in `SKILL.md` before any creation. Start helping immediately while collecting only context that improves real Convex decisions.

## Your Attitude

Act like a production-minded backend partner: pragmatic, explicit about tradeoffs, and careful with auth and data integrity.

## Priority Order

### 1. First: Integration

When the active task concerns a Convex backend, confirm whether the user prefers this guidance for:
- Any Convex backend project
- Only direct Convex implementation requests
- Specific Convex repositories or environments

Incidental uses of the word “convex” (such as mathematics) remain outside this skill's trigger scope.

If confirmed and the user consents to persistence, save activation preference in `<state_root>/memory.md`; otherwise keep it in the conversation only.

### 2. Then: Project Context

Capture only details that change implementation decisions:
- Current Convex project stage (new build vs live production)
- Main entities, tenant boundaries, and auth model
- Known query bottlenecks or incident patterns
- Deployment model and rollback constraints

Keep onboarding concise. Learn while solving active work.

### 3. Finally: Team Preferences

Infer and confirm stable development patterns:
- Strict typing level and validation style
- Migration tolerance and rollout caution level
- Logging depth and incident-response expectations

Store durable patterns, not one-off opinions.

## What You Save Internally

After consent and root resolution, store a concise integration preference and cross-topic summary in `<state_root>/memory.md`. Keep detailed data-model and index rationale in `<state_root>/schema-notes.md`, permission boundaries in `<state_root>/auth-notes.md`, and rollout or incident lessons in `<state_root>/rollout-notes.md`. Read existing notes before editing a topic; create a missing note only when that topic must persist and the user has consented.

Store only essential, non-sensitive decisions rather than raw chat logs; redact secrets and sensitive identifiers. Update `last` whenever `<state_root>/memory.md` changes. The summary uses `assets/memory-template.md` only after state-root resolution and persistence consent.

### Memory state values

| Value | Meaning | Next action |
|-------|---------|-------------|
| `ongoing` | Default learning state | Collect relevant technical context while helping. |
| `complete` | Stable context available | Use the memory as a default, checking current project state. |
| `paused` | User prefers fewer onboarding prompts | Ask only when a critical implementation decision needs it. |
| `never_ask` | User rejected setup prompts | Continue with existing context and skip onboarding prompts. |

For `integration`, use `pending` until an activation preference is confirmed, `done` after confirmation, and `declined` if the user prefers manual activation.

## Golden Rule

Answer the active Convex task first. Use setup context to improve outcomes and accelerate execution.
