# Core Rules — LM Studio

The operating rules live in `SKILL.md` so the entry point stays executable. Load this file only when a supporting note needs the same rule names.

1. Prove the server is reachable before changing client code. See `references/server-workflows.md`.
2. Keep downloaded, listed, loaded, and active model identifiers separate. See `references/model-lifecycle.md`.
3. Prefer OpenAI-compatible endpoints and verify each workload. See `references/api-recipes.md`.
4. Match model size and context to machine limits before rewriting prompts.
5. Run one smoke test after every runtime change and record it in `<state_root>/memory.md`.
6. Treat MCP as a separate risk layer. See `references/mcp-playbooks.md`.
7. Escalate beyond local when the task exceeds the verified local setup.
