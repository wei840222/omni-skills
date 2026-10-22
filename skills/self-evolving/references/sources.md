# Research Sources — self-evolving

Verified anchors used while refactoring this skill. Prefer primary specs and
current vendor docs over blog summaries.

## Agent skill packaging and progressive disclosure

- **Agent Skills specification** — frontmatter shape, description triggers, and
  resource layout expectations via https://agentskills.io/specification
- **Agent Skills document index** — current docs map via
  https://agentskills.io/llms.txt
- **Anthropic skill authoring best practices** — keep `SKILL.md` concise, push
  detail into references, and encode evaluation prompts via
  https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/best-practices
- **Anthropic agent skills overview** — progressive disclosure model via
  https://docs.anthropic.com/en/docs/agents-and-tools/agent-skills/overview
- **OpenAI Agents SDK** — filesystem-based tool/skill loading patterns via
  https://openai.github.io/openai-agents-python/

## Continual learning and memory hygiene

- **Complementary learning systems (CLS)** — separate fast episodic capture from
  slower schema consolidation when promoting experiments via
  https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3385861/
- **Ebbinghaus / spacing effects overview** — decay and review timing rationale
  for retiring cold experiments instead of keeping every trial hot via
  https://en.wikipedia.org/wiki/Forgetting_curve
- **OWASP Secrets Management Cheat Sheet** — keep credentials and high-risk
  identifiers out of durable agent memory stores via
  https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- **NIST Privacy Framework overview** — minimize sensitive categories and keep
  purpose limitation when storing optional evolution notes via
  https://www.nist.gov/privacy-framework

## Obsolete knowledge corrected

- Removed `clawic.com` homepage / promotional packaging and `_meta.json`
  catalog residue.
- Replaced hard-coded `~/Clawic/data/self-evolving/` paths with portable
  `<state_root>` resolution plus an explicit one-line migration note.
- Moved operational detail out of package root into `references/` and `assets/`
  so `SKILL.md` stays a loader, not a full manual.
- Kept the three-comparable-wins promotion threshold as the skill's operational
  gate; treated it as a local policy, not an external universal law.
