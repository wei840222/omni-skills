# Source Notes — self-discipline

Gate 6 research notes for the compliance / root-cause / automated-validator workflow.
All URLs below were used to verify domain guidance retained or strengthened in this refactor.

## Root cause and incident learning

- **5 Whys** — iterative causal questioning for recurring process failures via https://en.wikipedia.org/wiki/Five_whys
- **Google SRE Book — Postmortem Culture** — blameless incident writeups, action items, and prevention loops via https://sre.google/sre-book/postmortem-culture/
- **Google SRE Workbook — Postmortem analysis** — practical postmortem structure and follow-up tracking via https://sre.google/workbook/postmortem-analysis/

## Guardrails, hooks, and automated checks

- **Pre-commit framework** — local automated gates before commits via https://pre-commit.com/
- **Git hooks documentation** — client-side hook lifecycle for pre-commit / pre-push enforcement via https://git-scm.com/docs/githooks
- **OWASP Secrets Management Cheat Sheet** — secret handling and leak-prevention patterns for pre-send validators via https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html

## Agent skill packaging (repo-local standards)

- **Agent Skills specification compatibility** — validated with `uvx --from skills-ref agentskills validate skills/self-discipline`
- **Repo workflows** — `.agents/workflows/skill-refactor.md` Gates 1–9 and `.agents/AGENTS.md` selection / packaging rules

## Obsolete / removed

- Hard-coded `~/Clawic/data/self-discipline/` and clawic.com homepage / changelog promo paths (Gate 3 + Gate 5)
- Root-level reference dumps and `_meta.json` packaging residue (Gate 2)
- Non-portable absolute validator paths; replaced with portable `<state_root>/` placeholders
