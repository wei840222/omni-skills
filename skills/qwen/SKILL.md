---
name: qwen
description: Build and route Qwen chat, coding, reasoning, and vision workflows across hosted and self-hosted endpoints with safer debugging.
metadata:
  openclaw: '{"emoji": "🧩","requires": {"bins": ["curl","jq"],"env": ["DASHSCOPE_API_KEY"],"config": ["<state_root>/qwen/"]},"primaryEnv": "DASHSCOPE_API_KEY","os": ["linux","darwin","win32"],"displayName": "Qwen"}'
  related-skills: '{"models": "Compare Qwen against other model families and choose fallbacks by workload.","api": "Reuse structured HTTP, retry, and payload-debugging patterns around DashScope or OpenAI-compatible endpoints.","coding": "Hand off general coding-agent workflow once the Qwen execution surface is stable.","chat": "Use for generic chat UX patterns that are not Qwen-specific routing.","memory": "Persist durable routing preferences outside this skill optional local state notes."}'
---

## When to load

Load this skill when the user explicitly requests Qwen models (e.g., Qwen-Max, Qwen-Coder) or needs to migrate workloads between hosted Alibaba Model Studio and self-hosted servers. Reserve this exclusively for Qwen workflows.

## Architecture

Memory lives in `<state_root>/qwen/`. If `<state_root>/qwen/` does not exist, run `references/setup.md`. See `assets/memory-template.md` for structure.

```text
<state_root>/qwen/
├── memory.md         # Status, activation rules, and deployment defaults
├── routes.md         # Preferred route per workload
├── servers.md        # Known local or hosted endpoints
├── experiments.md    # Prompt, parser, and latency notes
└── logs/             # Optional sanitized repro payloads
```

## Quick Reference

Use the smallest file that resolves the blocker.

| Topic | File |
|-------|------|
| Setup process | `references/setup.md` |
| Memory template | `assets/memory-template.md` |
| Hosted and local request patterns | `references/api-patterns.md` |
| Workload routing matrix | `references/routing-matrix.md` |
| Hosted versus self-hosted decisions | `references/deployment-paths.md` |
| Tool-calling and structured output guardrails | `references/tool-calling.md` |
| Debugging and recovery | `references/troubleshooting.md` |

## Requirements

- `curl` and `jq` for minimal endpoint checks
- Hosted Qwen usually needs a `DASHSCOPE_API_KEY`
- Self-hosted Qwen may use Ollama, vLLM, SGLang, or another OpenAI-compatible server
- Keep secrets in environment variables only

## Core Rules

### 1. Lock the Surface Before Tuning the Model
- Identify the real execution surface first: Alibaba Model Studio hosted API, another OpenAI-compatible provider, or a self-hosted server.
- Most "Qwen issues" are actually endpoint, region, server, or chat-template issues rather than model quality issues.

### 2. Verify Live Availability Before Naming Any Model
- Start with a `/models` or equivalent health check and copy the live model ID from the response.
- Rely exclusively on live model IDs from health checks for production routing.

### 3. Route by Workload, Not by Brand Loyalty
- Split the request into one of these paths: fast chat, deep reasoning, coding agent, deterministic JSON, or vision.
- Pick the smallest Qwen family and server path that can reliably do that job.

### 4. Treat Structured Output as a Separate Reliability Problem
- If Qwen is feeding tools, JSON, or downstream writes, use strict schemas, low temperature, and parser validation before acting.
- If the first pass is creative or reasoning-heavy, add a second deterministic normalization pass instead of forcing one prompt to do both.

### 5. Separate Model Problems From Server Problems
- When behavior changes after migration, isolate the variable: model family, quantization, chat template, reasoning mode, parser, or backend.
- Reproduce with one minimal payload before changing prompts, infrastructure, and business logic at the same time.

### 6. Compare Hosted and Self-Hosted Explicitly
- Hosted Qwen usually wins on speed to first success and managed multimodal access.
- Self-hosted Qwen only wins when privacy, local cost control, or offline use clearly outweigh operational overhead.

### 7. Ask Before Creating Persistent State
- Work statelessly by default.
- Only create `<state_root>/qwen/` notes, saved routes, or repro logs after the user wants continuity across Qwen tasks.

## Common Traps

- Treating "Qwen" as one interchangeable thing -> hosted APIs, Ollama, vLLM, and agent frameworks behave differently.
- Hardcoding dated model IDs -> region and release cadence make old IDs fail fast.
- Mixing free-form reasoning with strict JSON output -> parsing breaks when one prompt is asked to do both.
- Blaming the model for local slowness -> Apple Silicon and Ollama often fail because of model size, quantization, or oversized context.
- Migrating from another OpenAI-compatible backend without rechecking tool-calling -> parser and chat-template differences can break automation.

## External Endpoints

Use only the smallest hosted endpoint that answers the current question.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://dashscope.aliyuncs.com/compatible-mode/v1/models | Auth header only | Mainland China model discovery |
| https://dashscope-intl.aliyuncs.com/compatible-mode/v1/models | Auth header only | International model discovery |
| https://dashscope-us.aliyuncs.com/compatible-mode/v1/models | Auth header only | United States model discovery |
| https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions | Prompt messages and options | Hosted Qwen chat completions in Beijing region |
| https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions | Prompt messages and options | Hosted Qwen chat completions in Singapore region |
| https://dashscope-us.aliyuncs.com/compatible-mode/v1/chat/completions | Prompt messages and options | Hosted Qwen chat completions in Virginia region |

No other data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- Prompt content sent to Alibaba Cloud Model Studio when using hosted Qwen
- Optional images or multimodal payloads sent to hosted Qwen vision endpoints when requested

**Data that stays local:**
- Deployment preferences and routing notes in `<state_root>/qwen/` after user approval
- Local server URLs, workload notes, and sanitized repro payloads kept for debugging

**This skill does NOT:**
- Store API keys in markdown files
- Send data to undeclared third-party endpoints
- Assume local servers are safe to expose publicly
- Modify its own skill files

## Scope

This skill ONLY:
- routes Qwen work across hosted and self-hosted execution surfaces
- chooses model families for chat, coding, reasoning, vision, and automation
- debugs migration, parser, latency, and endpoint problems
- stores lightweight local notes only after user approval

This skill boundaries:
- invent live model availability without checking
- persist secrets in `<state_root>/qwen/`
- execute destructive downstream automation without validated output
- pretend one backend's tool-calling behavior applies everywhere

## Sources

Official and primary references used for this refactor (Gate 6):

- [Qwen / DashScope OpenAI-compatible mode](https://help.aliyun.com/zh/model-studio/developer-reference/compatibility-of-openai-with-dashscope)
- [Alibaba Cloud Model Studio international docs](https://www.alibabacloud.com/help/en/model-studio/developer-reference/use-qwen-by-calling-api)
- [Qwen GitHub organization](https://github.com/QwenLM)
- [Ollama Qwen models](https://ollama.com/library/qwen)
- [vLLM documentation](https://docs.vllm.ai/en/latest/)
- [SGLang documentation](https://docs.sglang.ai/)

## Trust

Using hosted Qwen sends prompt data to Alibaba Cloud Model Studio.
Only install if you trust that service with your data, or keep Qwen fully self-hosted.
