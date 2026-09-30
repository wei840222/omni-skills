# Sources for skill-test checks

Use these primary pages when validating format, progressive disclosure, or evaluation claims. Prefer opening the live page over memorized rules.

## Agent Skills specification

- Document index — https://agentskills.io/llms.txt
- Normative specification — https://agentskills.io/specification
- Optional directories — https://agentskills.io/specification#optional-directories
- Progressive disclosure — https://agentskills.io/specification#progressive-disclosure
- File references — https://agentskills.io/specification#file-references
- Reference validator package — https://github.com/agentskills/agentskills/tree/main/skills-ref

Reproducible validate command used in this repository:

```bash
uvx --from skills-ref agentskills validate skills/<slug>
```

## OpenClaw skill metadata (when the host is OpenClaw)

- OpenClaw skills overview — https://docs.openclaw.ai/tools/skills
- Creating skills — https://docs.openclaw.ai/tools/creating-skills

Confirm field support on the live docs before encoding `metadata.openclaw` keys. Unsupported display-only fields should be omitted.

## Safety and evaluation pointers

- OWASP Top 10 for LLM Applications — https://owasp.org/www-project-top-10-for-large-language-model-applications/
- NIST AI Risk Management Framework — https://www.nist.gov/itl/ai-risk-management-framework

These inform safety-lens questions; they do not replace `skill-audit` for deep supply-chain review.

## Local repository contracts

When working inside `omni-skills`, also honor:

- `.agents/AGENTS.md`
- `.agents/workflows/skill-refactor.md`
- `.agents/workflows/skill-review.md`

Those paths are repository-local, not universal Agent Skills requirements.
