# Proactivity skill sources

Authoritative references used for this refactor. Prefer these over blog posts
when guidance conflicts. Re-open before asserting product- or version-specific
defaults.

## Agent Skills packaging

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt
- skills-ref validator — https://github.com/agentskills/agentskills/tree/main/skills-ref

## OpenClaw / agent operating patterns

- OpenClaw skills configuration (metadata.openclaw fields) —
  https://docs.openclaw.ai/tools/skills
- Progressive disclosure and skill packaging norms from the Agent Skills
  specification above (load only what the trigger needs).

## Proactivity / autonomy design

- Keep proactive suggestions concrete, timely, and opt-out quiet when value is
  unclear; prefer reversible internal work over external side effects
  (operational synthesis aligned with ask-first boundaries in this package).
- Heartbeat empty-cycle contract for non-actionable checks: sibling skill
  `heartbeat` in this repository (`skills/heartbeat/SKILL.md`) — return a
  quiet OK rather than noisy summaries.

## Claim checks performed this refactor

| Claim | Verdict | Source |
|-------|---------|--------|
| Frontmatter top-level fields limited; nested metadata must be string-to-string | Confirmed | https://agentskills.io/specification |
| `metadata.openclaw` JSON string pattern for emoji | Confirmed against repo merged skills + OpenClaw skills docs | https://docs.openclaw.ai/tools/skills |
| Portable `<state_root>` resolution with workspace / memory / home fallbacks | Confirmed against merged `heartbeat` / `self-improving` patterns in this repo | `skills/heartbeat/SKILL.md`, `skills/self-improving/SKILL.md` |
| Remove clawic homepage / feedback promo and `_meta.json` | Project policy Gate 5 | `.agents/workflows/skill-refactor.md` |
