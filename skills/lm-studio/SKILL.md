---
name: lm-studio
description: Run and integrate LM Studio with local model lifecycle control, OpenAI-compatible APIs, embeddings, and MCP-aware workflows. Use when the user wants a local server, lms load/unload, localhost OpenAI-compatible endpoints, embeddings, or local inference debugging.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🧪","requires":{"bins":["curl","jq"],"config":["<state_root>/"]}}'
  related-skills: '{"api":"Shape request payloads, retries, parsing, and integration debugging for the local OpenAI-compatible server.","docker":"Package helper services or MCP servers consistently on the local machine.","models":"Choose models by workload, context budget, and quality tradeoffs before loading one locally.","open-router":"Escalate from local-first execution to routed cloud models when capability gaps matter.","self-host":"Operate local infrastructure with practical reliability and security habits."}'
---

## State location

LM Studio notes may exist in `<workspace>/lm-studio/`, `<workspace>/memory/lm-studio/`, or `~/lm-studio/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/lm-studio/`, `<workspace>/memory/lm-studio/`, `~/lm-studio/`.
3. If none exists and state must be created, default to `<workspace>/lm-studio/`.

Use the selected `<state_root>` for every state operation in this skill. If more than one candidate exists, use only the highest-precedence directory and tell the user that multiple copies were found. Do not merge or cross-write them.

## When to load

Load when the user wants to run local models with LM Studio, connect an app to its local server, or debug weak local inference.

- **Setup**: Load `references/setup.md` when `<state_root>/` is missing or the first-run defaults are unset.
- **Server**: Load `references/server-workflows.md` to prove the port, start/stop the server, and run a smoke test.
- **Models**: Load `references/model-lifecycle.md` to download, load, unload, and swap models.
- **API**: Load `references/api-recipes.md` for OpenAI-compatible request patterns.
- **MCP**: Load `references/mcp-playbooks.md` only after the model path already works.
- **Debug**: Load `references/troubleshooting.md` for symptom-based recovery.
- **Memory shape**: Load `assets/memory-template.md` before creating `<state_root>/memory.md`.

## Core Rules

### 1. Prove the server is reachable before changing client code
- Use `references/server-workflows.md` to confirm the actual port, endpoint reachability, and model visibility.
- "LM Studio is open" is not enough. Require one real request to succeed before touching integration code.
- If `curl` to the advertised port fails, stop client edits and fix the server path first.

### 2. Separate downloaded, listed, loaded, and active models
- Use `references/model-lifecycle.md` for discovery, loading, unloading, and verification.
- Treat downloaded filenames, API model ids, CLI identifiers, and the active runtime instance as distinct concepts.
- If `lms ls`, `lms ps`, and `GET /v1/models` disagree, record each result before choosing an id.

### 3. Prefer OpenAI-compatible endpoints for app integration
- Start from `references/api-recipes.md` and change only the base URL and model identifier before rewriting an existing client.
- Verify each workload separately: `responses`, `chat/completions`, `embeddings`, or `completions`.
- If a workload fails, switch the model or endpoint; do not rewrite the client first.

### 4. Match model size and context to machine limits
- Treat slow first token, OOM, and context overflow as runtime-fit problems first.
- Reduce model size, quantization burden, or context length before escalating complexity.

### 5. Validate after every runtime change
- After loading a new model, changing context length, or altering server settings, run one end-to-end smoke test.
- Record the known-good combination in `<state_root>/memory.md` so the next turn reuses it.

### 6. Treat MCP as a separate risk layer
- Use `references/mcp-playbooks.md` to connect servers, but debug model serving and MCP behavior independently.
- Install only trusted MCP servers, and confirm before routing local data to a remote endpoint.
- If the model path is still failing, fix that path before adding MCP.

### 7. Escalate beyond local when the task exceeds the local setup
- LM Studio fits privacy-sensitive work, offline execution, extraction, and controlled agent loops.
- For unsupported capabilities or repeated quality failures, say so and recommend a stronger remote path.

## Common Traps

- Assuming port `1234` without a reachability check makes integrations fail while the app looks healthy.
- Treating `GET /v1/models` as proof a model is loaded accepts Just-In-Time listings before a usable runtime exists.
- Reusing cloud model names in local requests leaves the client intact and the local identifier wrong.
- Forcing JSON, tools, or vision on an unverified local model blames the prompt for a capability mismatch.
- Leaving large models loaded while debugging another issue hides the cause under RAM or VRAM pressure.
- Installing random MCP servers drops privacy and system-access boundaries.

## Security and privacy

- Local `localhost` server calls stay on the machine by default.
- Model downloads and MCP servers follow the user's explicit configuration.
- Prompt content sent to a same-machine LM Studio server stays local.
- Persistent notes live in `<state_root>/` only when the user wants continuity.
- Keep remote access closed unless the user explicitly asks to expose it.
- Keep tokens, passwords, and copied credentials out of skill memory.
- Open network access or install an MCP server only after explicit user intent.

## Requirements

- LM Studio or `llmster` is already installed.
- `curl` and `jq` are available for smoke tests and response inspection.
- `lms` is optional and preferred for repeatable server and model operations.
- Keep requests local by default.

## Data files

```text
<state_root>/
├── memory.md          # Required once persistent state is enabled
├── server-notes.md    # Optional: reachability checks and server mode
├── model-profiles.md  # Optional: verified models by workload
└── incidents.md       # Optional: repeated failures and confirmed fixes
```

Create optional files only when that feature is actually needed.
