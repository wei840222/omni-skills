# Research Sources — vibe-coding

Gate 6 anchors for domain knowledge used in this refactor. Prefer primary sources over secondary summaries.

## Origin and definition

- **Andrej Karpathy — "vibe coding" coinage (Feb 2025)** — original framing of directing AI coding by intent and results rather than line-by-line authorship via https://x.com/karpathy/status/1886192184808149383
- **Simon Willison — vibe coding vs software development** — distinction that reviewing, testing, and being able to explain the code is software development, not vibe coding via https://simonwillison.net/2025/Mar/19/vibe-coding/
- **Simon Willison — Not vibe coding** — reinforces when human review and ownership still apply via https://simonwillison.net/2025/May/1/not-vibe-coding/

## Tooling and workflow references

- **Cursor Docs — Rules** — project rules / `.cursor/rules` guidance for persistent AI conventions via https://docs.cursor.com/context/rules
- **Claude Code — CLAUDE.md / project memory** — agent project instruction patterns via https://docs.anthropic.com/en/docs/claude-code/memory
- **Bolt.new** — browser prompt-to-app prototyping product entry via https://bolt.new/
- **Lovable** — design-first AI app builder entry via https://lovable.dev/
- **Replit Agent / Docs** — browser IDE and agentic build workflows via https://docs.replit.com/

## Safety boundary rationale

- Auth, payments, secrets, and schema changes remain intervene-first because vibe-coding evaluation-by-results is insufficient for security-critical paths (see SKILL.md Core Rules 4 and 8; pitfalls.md Security Pitfalls).
