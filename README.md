# Omni Skills

> 🌌 Omni Skills — *Omni*, meaning all, infinite, and universal. A boundless skill constellation empowering AI to touch every horizon and do anything.

Forked from the upstream project [clawic/skills](https://github.com/clawic/skills), **Omni Skills** is continuously updated by AI agents with up-to-date real-world knowledge, adhering strictly to the universal [Agent Skills specification](https://agentskills.io/specification).

Any AI agent is welcome to continuously contribute, refactor, and enrich this library!

## Workflows & Quality Contract

- **Workflow 1: Skill Refactor**: Structured 7-phase refactoring process (Phases 0–6 covering Gates 1–9), documented in [`docs/refactor-guide.md`](docs/refactor-guide.md).
- **Workflow 2: Skill Review**: Three-lens PR review procedure (`code-review-and-quality`, `writing-for-agents`, `darwin-skill`), documented in [`docs/review-guide.md`](docs/review-guide.md).
- **Agent Rules**: Execution rules and dispatcher instructions are configured in [`.agents/AGENTS.md`](.agents/AGENTS.md).

## Prerequisites & Required Tools

To execute refactor and review SOPs, the following CLI tools and evaluation sub-skills are required:

### Command-Line Utilities (CLI)
- **`git`**: Branch management, atomic commit history, and git submodules.
- **`gh`**: GitHub CLI for PR creation, list fetching, checkout, review submission, and merging.
- **`uv` / `uvx`**: Python package runner used to execute the official reference validator on demand (`uvx --from skills-ref agentskills validate skills/<slug>`), no separate installation required.
- **`curl` & `jq`**: UNIX CLI utilities for fetching and parsing GitHub REST API pull request data.

### Evaluation & Audit Sub-Skills (`.agents/skills/`)
- **[`darwin-skill`](.agents/skills/darwin-skill/SKILL.md)**: Quantitative evaluation engine, test prompt (`test-prompts.json`) execution, and 9-dimension scoring ($\ge 80/100$).
- **[`freud-skill`](.agents/skills/freud-skill/SKILL.md)**: Cognitive load audit, white-bear effect elimination, and positive instruction reframing.
- **[`code-review-and-quality`](.agents/skills/agent-skills/skills/code-review-and-quality/SKILL.md)**: Quality review lens for code correctness, security, performance, and architecture.
- **[`writing-for-agents`](.agents/skills/mattpocock-skills/skills/productivity/writing-for-agents/SKILL.md)**: Quality review lens for progressive disclosure, trigger description tuning, and information hierarchy.
- **[`anysearch-skill`](.agents/skills/anysearch-skill/SKILL.md) / `research`**: Real-time web search and primary source cross-verification for Gate 6 domain accuracy.

## Repository Layout

```text
omni-skills/
├── .agents/
│   ├── AGENTS.md               # Core agent mission & workflow dispatcher rules
│   └── skills/                 # Evaluation & review submodules
│       ├── agent-skills/       # Contains code-review-and-quality
│       ├── anysearch-skill/    # Real-time search engine for Gate 6 research
│       ├── darwin-skill/       # Quantitative evaluation engine (Gate 8)
│       ├── freud-skill/        # Cognitive load audit engine (Gate 9)
│       └── mattpocock-skills/  # Contains writing-for-agents
├── CHANGELOG.md                # Skill refactor tracking table & score log
├── docs/
│   ├── refactor-guide.md       # Canonical 7-phase refactor guide (Gates 1–9)
│   ├── review-guide.md         # Canonical 3-lens PR review guide
│   ├── pull-request-template.md
│   └── pull-request-review-template.md
└── skills/                     # 960+ universal Agent Skill packages
    └── <slug>/
        ├── SKILL.md
        └── (optional references/, assets/, scripts/)
```
