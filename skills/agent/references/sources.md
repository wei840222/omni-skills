# Research Sources — agent

Gate 6 anchors used while refactoring the `agent` skill. Prefer primary guidance over secondary summaries.

## Agent identity and persona design

- **OpenAI — Instruction hierarchy / model spec concepts** — system vs developer vs user instruction precedence and honesty norms — https://cdn.openai.com/spec/model-spec-2025-02-12.html
- **Anthropic — Claude system prompt / constitution-style guidance (public docs)** — helpful, honest, harmless framing for assistant behavior — https://docs.anthropic.com/en/release-notes/system-prompts
- **Google — Gemini / Gemma responsible AI guidance** — safety and grounded-response expectations for assistant products — https://ai.google.dev/gemini-api/docs/safety-settings

## Voice, anti-sycophancy, and collaboration style

- **OpenAI Cookbook — How to make LLMs say what you want (prompt patterns)** — concrete behavior instructions beat adjective-only personas — https://cookbook.openai.com/examples/how_to_make_llms_say_what_you_want
- **Anthropic docs — Prompt engineering overview** — clear role, constraints, and examples improve reliability — https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview
- **Nielsen Norman Group — Personality in design / voice & tone** — brand voice should stay consistent while register adapts to context — https://www.nngroup.com/articles/brand-tone-of-voice/

## Boundaries, escalation, and tool use

- **OWASP LLM Top 10** — over-reliance, excessive agency, and sensitive-info risks for agentic systems — https://owasp.org/www-project-top-10-for-large-language-model-applications/
- **OpenAI docs — Safety best practices** — reduce sycophancy and overconfident answers with clearer instructions — https://platform.openai.com/docs/guides/safety-checks
- **Model Context Protocol specification** — tool/context boundaries for agent systems — https://modelcontextprotocol.io/specification/

## Obsolete packaging corrected

- Removed `homepage: https://clawic.com/skills/agent` promotional coupling
- Removed legacy `metadata.clawdbot` nested object and `_meta.json`
- Replaced negative white-bear bans with positive replacement / out-of-scope framing where safe
