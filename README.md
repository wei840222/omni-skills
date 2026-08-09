# Omni Skills

> "Omni" means everything.

Special thanks to the upstream project [clawic/skills](https://github.com/clawic/skills).

## Repository layout

```text
omni-skills/
├── AGENTS.md
├── CHANGELOG.md
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── LICENSE
├── README.md
├── docs/
│   ├── refactor-guide.md
│   ├── review-guide.md
│   ├── pull-request-template.md
│   └── pull-request-review-template.md
└── skills/
    └── <slug>/
        ├── SKILL.md
        └── (optional scripts/, references/, resources/)
```

## Notes

- All agent skills live in `skills/<slug>/` and conform to the [Agent Skills specification](https://agentskills.io/specification).
- Refactoring standards, quality gates (1–9), and review workflows are documented in [`docs/refactor-guide.md`](docs/refactor-guide.md) and [`docs/review-guide.md`](docs/review-guide.md).
- Agent execution rules and instructions are configured in [`AGENTS.md`](AGENTS.md).
