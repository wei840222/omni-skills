## Skill Refactor: real-estate-agent

### Summary
This pull request brings `real-estate-agent` into full compliance with the omni-skills Agent Skills specification and standard quality gates (1–9).

### Gates 1–5: Specification Compliance
- **Gate 1**: Removed legacy `slug`, `changelog`, `homepage`, and `clawdbot` from `SKILL.md` frontmatter. Formatted `metadata.openclaw` as a stringified JSON object. Removed duplicate `_meta.json`.
- **Gate 2**: Moved `setup.md`, `portals.md`, `analysis.md`, `listing-optimization.md` to `references/`. Moved `memory-template.md` and `memory.md` to `assets/`.
- **Gate 3**: Established the `$STATE_ROOT` and explicit workspace-first lookup order in `SKILL.md` (`<workspace>/real-estate-agent/`, `<workspace>/memory/real-estate-agent/`, `~/real-estate-agent/`). Updated all state paths across files.
- **Gate 4**: Replaced the narrative "Related Skills" section with the `metadata.related-skills` JSON mapping referencing `invest`, `legal`, and `negotiate`.
- **Gate 5**: Removed promotional `clawic.com` links and feedback sections.

### Gate 6: Fact Verification
- Verified real estate appraisal strategies using Wikipedia API.
- Added explicit domain knowledge source references to `references/analysis.md`.

### Gate 7: Description & Best Practices
- Optimized `SKILL.md` description to clearly define trigger conditions.
- Instructed explicit context awareness and loading triggers for reference files.

### Gate 8: Darwin Evaluation
- Created `test-prompts.json` with 2 representative real-estate prompts.
- Executed evaluation runs ensuring responses accurately manage state, context, and follow guidelines.
- **Final Darwin Score**: 90/100

### Gate 9: Freud Audit
- Eradicated "white bear" effects by rephrasing prohibitions (e.g., "Don't wait for the client to search" to "Instead of waiting for the client to search, actively monitor the market").

---
**Reviewer:** @ani6439walc
