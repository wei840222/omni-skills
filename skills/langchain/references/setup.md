# Setup — LangChain

Read this on first use to load user preferences. Do not interview the user.

## Your Attitude

LangChain moves fast and most published code is written against a version that no longer exists. Be concrete about which version an API belongs to, prefer the smallest abstraction that solves the problem, and name the cost of the loop before recommending an agent.

## How To Load Preferences

1. Read `<state_root>/config.yaml` if it exists. Apply its values.
2. For anything absent, use the defaults in the Configuration table of `SKILL.md`.
   - `lc_version_line: 1.x`, `chat_provider: openai`, `vector_store: chroma`, `python_runtime: 3.11+`, `async_style: sync`, `tracing: none`, `trace_pii: redact`, `structured_output_method: tool_calling`.
3. Read `<state_root>/memory.md` for prior context (their app shape, recurring pain points). Absence is fine; proceed without comment.
4. If the working directory contains a lockfile or requirements file, the versions there beat the configured `lc_version_line` — the installed code is the ground truth.

Proceed from defaults. Ask only when a missing preference blocks a concrete code choice.

## Recording Preferences (only when the user declares one)

Write to config or memory only when the user states a preference during the work.

- User names a provider, vector store, Python version, or version line → update the matching key in `<state_root>/config.yaml`.
- User expresses a habit or stance (where prompts live, LangGraph vs plain LCEL, approval before destructive tools, cost ceilings, citation requirements) → record it under the relevant preference area (tooling, conventions, platform, safety posture, cost posture, retrieval conventions, output format) in `<state_root>/memory.md`.
- User corrects earlier guidance → update the stored value so later answers match the correction.

If the user has said nothing, store nothing. Never store API keys, endpoints with credentials, or prompt content containing customer data.

## What Memory Holds

See `assets/memory-template.md` for the file format. Track the shape of their app (script, service, worker, notebook), which parts exist already (retrieval, agents, evals), pain points raised, and how much explanation they want with code — but only from what they actually reveal.
