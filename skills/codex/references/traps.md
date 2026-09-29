# Codex Traps


- Running Codex in the wrong directory -> edits land in the wrong repo or outside intended scope.
- Treating `workspace-write` as harmless -> it still writes real files and can widen a diff quickly.
- Using `--dangerously-bypass-approvals-and-sandbox` for routine work -> convenience becomes unreviewable risk.
- Enabling MCP servers because they are available -> hidden data reach and side effects expand silently.
- Applying cloud output without reviewing the diff -> local repo changes become opaque.
- Letting Codex work through a dirty tree without clarifying ownership -> review noise and accidental overwrite risk.
- Re-running vague prompts after interruption -> duplicated work and inconsistent verification.

