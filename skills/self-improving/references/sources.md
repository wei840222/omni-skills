# Research Sources — self-improving

Verified anchors used while refactoring this skill. Prefer primary specs and
current vendor docs over blog summaries.

## Agent skill packaging and progressive disclosure

- **Agent Skills specification** — frontmatter shape, description triggers, and resource layout expectations via https://agentskills.io/specification
- **OpenAI Agents SDK skills guide** — progressive disclosure and filesystem-based skill loading patterns via https://openai.github.io/openai-agents-python/skills/
- **Anthropic skill authoring best practices** — keep SKILL.md concise, push detail into references, and encode evaluation prompts via https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices

## Memory hygiene and continual learning

- **Complementary learning systems (CLS)** — separate fast episodic correction capture from slower schema/rule consolidation when promoting lessons across tiers via https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3385861/
- **Ebbinghaus / spacing effects overview** — decay and review timing rationale for demoting cold memory instead of keeping every correction hot via https://en.wikipedia.org/wiki/Forgetting_curve
- **OWASP Secrets Management Cheat Sheet** — keep credentials and high-risk identifiers out of durable agent memory stores via https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html

## Privacy boundaries for personal agent memory

- **NIST Privacy Framework overview** — minimize sensitive categories and keep purpose limitation when storing user corrections via https://www.nist.gov/privacy-framework
- **GDPR principles summary (ICO)** — data minimization and storage limitation for optional personal notes an agent retains via https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/data-protection-principles/a-guide-to-the-data-protection-principles/

## Obsolete knowledge corrected

- Removed `clawic.com` homepage / promotional packaging and `_meta.json` catalog residue.
- Replaced hard-coded `~/Clawic/data/self-improving/` paths with portable `<state_root>` resolution plus an explicit one-line migration note.
- Moved operational detail out of package root into `references/` and `assets/` so SKILL.md stays a loader, not a full manual.
