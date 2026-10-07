# Sources — tools skill

Last checked: 2026-10-07

## Agent Skills format and progressive disclosure

- Agent Skills specification — frontmatter, optional directories, progressive disclosure, file references: https://agentskills.io/specification
- Agent Skills document index: https://agentskills.io/llms.txt
- Reference validator package (`skills-ref` / `agentskills`): https://github.com/agentskills/agentskills/tree/main/skills-ref

## Preference learning and defaults (domain)

- Nielsen Norman Group — mental models and matching system to the real world (defaults should match user expectations): https://www.nngroup.com/articles/mental-models/
- Nielsen Norman Group — recognition over recall (surface known tools before asking users to re-specify): https://www.nngroup.com/articles/recognition-and-recall/
- Interaction Design Foundation — Hick's Law (more undifferentiated options increase choice time; curated defaults help): https://www.interaction-design.org/literature/article/hick-s-law-making-the-choice-easier-for-users
- The Decision Lab — status quo bias (switching cost often dominates small gains; require large benefit before suggesting change): https://thedecisionlab.com/biases/status-quo-bias

## Personal knowledge / preference ledgers

- Obsidian help — how notes and daily systems stay user-owned files (aligns with portable `<state_root>` ledgers, not vendor lock-in inside the skill package): https://help.obsidian.md/
- XDG Base Directory Specification — user-controlled config/data locations as a portability reference for state roots: https://specifications.freedesktop.org/basedir-spec/latest/

## Obsolete knowledge corrected

- Removed Clawic catalog homepage, `_meta.json`, and promotional feedback paths.
- Replaced hard-coded preference blobs inside `SKILL.md` with a portable `<state_root>/preferences.md` ledger.
- Replaced root-level `criteria.md` / `dimensions.md` with `references/` paths and explicit load triggers.
