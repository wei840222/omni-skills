# Multi-Agent Evaluation

Spawn specialized reviewers for pre-publish skill evaluation.

## Reviewer types

### Structure reviewer

- Is `SKILL.md` a concise entry point with progressive disclosure?
- Are details routed to `references/`, `assets/`, or `scripts/` with clear load triggers?
- Do frontmatter fields match the Agent Skills specification and project gates?
- Is there package clutter (duplicate metadata, promo sections, review-only artifacts)?

### Safety reviewer

- Personal data, credentials, or secret-shaped examples?
- Destructive defaults, unrestricted network/file writes, or hidden instructions?
- Model-locked assumptions that break portability?
- Supply-chain risk that should hand off to `skill-audit`?

### Usefulness reviewer

- Clear what it does and **when** to load it?
- Actionable steps with recovery paths?
- Would this actually help a real user task?
- Description over/under-trigger risk?

### Domain reviewer (when applicable)

- Technically correct for the domain?
- Mutable facts cited or marked unverified?
- Missing edge cases a practitioner would expect?
- Obsolete versions, prices, or APIs?

## Spawning reviewers

For each lens, spawn an isolated reviewer with:

- The skill package content (or paths) under review
- The lens-specific questions above
- A request for concise findings plus `approve` / `concerns` / `reject`

Keep reviewers separate so one strong lens cannot hide another.

## Synthesizing results

| Reviewer | Verdict | Key finding |
|----------|---------|-------------|
| Structure | ✅/⚠️/❌ | summary |
| Safety | ✅/⚠️/❌ | summary |
| Usefulness | ✅/⚠️/❌ | summary |
| Domain | ✅/⚠️/❌ | summary |

## Final recommendation

- **All ✅** → Recommend publish/install path the user named
- **Any ❌** → Reject or block; explain the failing lens and concrete fix
- **Mixed ⚠️** → Present tradeoffs; let the user decide

Route security ❌ to `skill-audit`. Route structural/authoring fixes to `skill-builder`.

## Handling conflicts

If reviewers disagree:

- Present both perspectives with evidence anchors
- Explain the tradeoff (e.g., usefulness vs safety)
- Keep the stricter safety finding visible; do not average it away
