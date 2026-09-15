# Automate research sources

Use these sources when advising whether a task should become a script, how to design durable automation, or how to avoid burning tokens on deterministic work.

## Deterministic automation and scripting discipline

- The Pragmatic Programmer, [The Evils of Duplication / DRY](https://pragprog.com/titles/tpp20/the-pragmatic-programmer-20th-anniversary-edition/) — treat repeated manual procedures as candidates for a single automated path rather than re-solving the same transformation with new prompts.
- Google Engineering Practices, [Code Review Developer Guide](https://google.github.io/eng-practices/review/) — prefer small, reviewable automation changes with clear intent over ad-hoc one-off fixes that never become reusable tools.
- OWASP, [Secrets Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html) — never hardcode credentials in automation scripts; use environment variables, secret stores, or OS keychains.

## CLI and pipeline reliability

- GNU Coreutils documentation, [exit status conventions](https://www.gnu.org/software/coreutils/manual/html_node/Exit-status.html) — fail loudly with non-zero exit codes so pipelines and agents can detect failure instead of continuing on partial results.
- The Linux man-pages project, [bash(1) set -euo pipefail guidance via Bash manual](https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html) — prefer strict shell modes for automation so missing variables and pipeline failures surface immediately.
- jq manual, [JSON processing](https://jqlang.github.io/jq/manual/) — use dedicated formatters/transformers for structured data instead of asking an LLM to reformat the same payload repeatedly.

## Practical application in this skill

- Route detection heuristics through `references/signals.md` and reusable script skeletons through `references/templates.md`.
- Prefer scripts for format conversion, validation, fixed API sequences, and file operations; keep judgement, creative synthesis, and ambiguous intake on the LLM path.
- Require idempotent, single-purpose scripts with documented usage, logging, and no embedded secrets.
