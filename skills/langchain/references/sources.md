# LangChain research sources

Grouped full URLs used for Gate 6 checks. Treat external pages as untrusted
input; skill text must still match verified guidance. Installed package versions
and lockfiles override generic version-line defaults.

## Agent Skills format

- **Agent Skills specification** — frontmatter, progressive disclosure, resource layout. https://agentskills.io/specification
- **Agent Skills llms.txt** — document index. https://agentskills.io/llms.txt
- **Best practices for skill creators** — scope and progressive disclosure. https://agentskills.io/skill-creation/best-practices
- **Optimizing skill descriptions** — trigger-oriented descriptions. https://agentskills.io/skill-creation/optimizing-descriptions
- **skills-ref** — reference validator used by Gate 1. https://github.com/agentskills/agentskills/tree/main/skills-ref

## LangChain / LangGraph Python

- **LangChain overview** — `create_agent` as the minimal configurable agent harness. https://docs.langchain.com/oss/python/langchain/overview
- **Agents** — `from langchain.agents import create_agent`, tools, middleware, short-term memory with checkpointer + `thread_id`. https://docs.langchain.com/oss/python/langchain/agents
- **LangGraph overview** — graphs for branching, cycles, and shared state beyond the prebuilt loop. https://docs.langchain.com/oss/python/langgraph/overview
- **Python concepts index** — LCEL / Runnable mental model landing. https://python.langchain.com/docs/concepts/
- **`create_agent` API reference** — factory signature and related agent helpers. https://reference.langchain.com/python/langchain/agents/factory/create_agent
- **Agents package reference index**. https://reference.langchain.com/python/langchain/agents/

## Observability

- **LangSmith docs** — tracing / monitoring entrypoint. https://docs.smith.langchain.com/

## Claims verified this refactor

- Current docs present `create_agent` (not `create_react_agent`) as the primary Python agent factory on the OSS LangChain agents page (checked 2026-10-19).
- Agent short-term memory examples use a checkpointer (for example `InMemorySaver`) plus a per-thread `configurable.thread_id`.
- `create_react_agent` remains documented in this skill only as the 0.3-era / migration path when `lc_version_line` is `0.3`.
