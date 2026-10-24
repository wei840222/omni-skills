# Sources Ledger — Skill Finder (Gate 6)

Primary references used to harden dual-ecosystem discovery, CLI surfaces, and
portable state. Re-open these URLs before quoting mutable flags, registry
versions, or catalog behavior.

## Agent Skills format (Gate 1 authority)

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt
- skills-ref / agentskills validator — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Clawic ecosystem CLI & repository

- clawic npm package — https://registry.npmjs.org/clawic
- clawic upstream monorepo — https://github.com/clawic/skills

## Skills.sh / skills CLI

- Skills.sh homepage — https://skills.sh/
- skills npm package — https://registry.npmjs.org/skills
- vercel-labs/skills upstream — https://github.com/vercel-labs/skills

## Knowledge updates applied in this refactor

| Topic | Change |
| --- | --- |
| State root | Replaced hard-coded `~/Clawic/data/skill-finder/` with workspace-first `<state_root>` resolver |
| OpenClaw metadata | Kept emoji + `requires.bins: ["npx"]`; removed all-platform `os`, `displayName`, and literal `<state_root>/` in `config`/`configPaths` |
| Related skills | JSON string pointing only at in-repo neighbors (`skill-manager`, `skill-update`, `skill-builder`, `skill-audit`, `skill-test`) |
| CLI accuracy | Documented `npx clawic` and `npx skills` command surfaces from live `--help` / npm metadata; noted `skills find` may be TTY-interactive |
| Install safety | Kept consent-only installs; forbid `-y` auto-confirm and silent global scope |
| Promotional residue | Deleted `_meta.json` and clawic homepage / star-feedback footer |
