# Omni Skills

Omni Skills is a library of reusable skills for AI agents, forked from [clawic/skills](https://github.com/clawic/skills). Each skill lives in `skills/<slug>/` with a `SKILL.md` entrypoint and optional supporting files.

The project is progressively refactoring the library toward the [Agent Skills specification](https://agentskills.io/specification), with checks for format, domain accuracy, instruction quality, and portability. Refactor history and recorded evaluation scores are tracked in [CHANGELOG.md](CHANGELOG.md).

## Using a Skill

1. Browse [`skills/`](skills/) and choose a skill relevant to your task.
2. Read its `SKILL.md` for scope, requirements, and usage instructions.
3. Follow your agent's skill-loading instructions, keeping any `references/`, `assets/`, and `scripts/` alongside `SKILL.md`.

Check each skill's runtime and tool requirements before use; compatibility and validation coverage vary across the library.

## Contributing

Start with [CONTRIBUTING.md](CONTRIBUTING.md) for package conventions and [`.agents/AGENTS.md`](.agents/AGENTS.md) for agent execution rules. The workflows below define the detailed quality checks.

## Workflows & Quality Contract

- **Workflow 1: Skill Refactor**: Structured 7-phase refactoring process (Phases 0–6 covering Gates 1–9), documented in [`.agents/workflows/skill-refactor.md`](.agents/workflows/skill-refactor.md).
- **Workflow 2: Skill Review**: Three-lens PR review procedure (`code-review-and-quality`, `writing-for-agents`, `darwin-skill`), documented in [`.agents/workflows/skill-review.md`](.agents/workflows/skill-review.md).
- **Agent Rules**: Execution rules and dispatcher instructions are configured in [`.agents/AGENTS.md`](.agents/AGENTS.md).
- **PR Templates**: Use the [refactor template](.agents/templates/pull-request-refactor.md) or [review template](.agents/templates/pull-request-review-template.md) for the corresponding workflow.

## Prerequisites & Required Tools

These tools support the refactor and review workflows; individual skills have their own requirements.

After cloning the repository, initialize the evaluation and review submodules:

```bash
git submodule update --init --recursive
```

The evaluation links below point to their containing submodules. Their `SKILL.md` files become available locally after initialization; exact entrypoint paths are listed in the workflow guides.

### Command-Line Utilities (CLI)

- **`git`**: Branch management, atomic commit history, and git submodules.
- **`gh`**: GitHub CLI for PR creation, list fetching, checkout, review submission, and merging.
- **`uv` / `uvx`**: Python package runner used to execute the official reference validator on demand (`uvx --from skills-ref agentskills validate skills/<slug>`), no separate installation required.
- **`curl` & `jq`**: UNIX CLI utilities for fetching and parsing GitHub REST API pull request data.

### Evaluation & Audit Sub-Skills (`.agents/skills/`)

- **[`darwin-skill`](.agents/skills/darwin-skill)**: Quantitative evaluation engine, test prompt (`test-prompts.json`) execution, and 9-dimension scoring (minimum 80/100).
- **[`freud-skill`](.agents/skills/freud-skill)**: Cognitive load audit, white-bear effect elimination, and positive instruction reframing.
- **[`code-review-and-quality`](.agents/skills/agent-skills)**: Quality review lens for code correctness, security, performance, and architecture.
- **[`writing-for-agents`](.agents/skills/mattpocock-skills)**: Quality review lens for progressive disclosure, trigger description tuning, and information hierarchy.
- **[`anysearch-skill`](.agents/skills/anysearch-skill)**: Real-time web search and primary source cross-verification for Gate 6 domain accuracy.

## Repository Layout

```text
omni-skills/
├── .agents/
│   ├── AGENTS.md              # Agent mission & workflow dispatcher
│   ├── workflows/             # Canonical refactor & review guides
│   ├── templates/             # Pull request & review templates
│   └── skills/                # Evaluation, review & supporting skills
├── CHANGELOG.md               # Skill refactor history & recorded scores
├── CONTRIBUTING.md            # Contribution conventions
├── experiments/              # Skill-routing benchmarks & notebooks
└── skills/                    # Reusable skill packages
    └── <slug>/
        ├── SKILL.md
        └── (optional references/, assets/, scripts/)
```

## License

See [LICENSE](LICENSE) for the repository license.
