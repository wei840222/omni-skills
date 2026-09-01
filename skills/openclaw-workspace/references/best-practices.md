# Best Practices for OpenClaw Workspace Auditing

Use these current OpenClaw sources when a proposed workspace change depends on runtime behavior rather than the workspace's existing instructions:

| Topic | Source | Apply it when |
|---|---|---|
| Workspace location and boundary | https://docs.openclaw.ai/concepts/agent-workspace | Checking the active workspace, bootstrap scope, or sandbox implications. |
| Memory layers | https://docs.openclaw.ai/concepts/memory | Distinguishing `USER.md`, `MEMORY.md`, and dated `memory/` notes. |
| Tools, skills, and plugins | https://docs.openclaw.ai/tools | Clarifying that workspace documentation does not grant a runtime capability. |
| Recurring work | https://docs.openclaw.ai/automation/cron-jobs | Designing scheduled work with durable job state and explicit delivery behavior. |

- **Layered audits:** Separate startup behavior (`AGENTS.md`), identity (`IDENTITY.md`), personality (`SOUL.md`), long-term facts (`MEMORY.md`), and dated context (`memory/`) before proposing a change.
- **Proactivity with boundaries:** Define observable triggers, approval boundaries, and delivery behavior instead of a broad "be proactive" instruction; use the runtime's current scheduling surface for recurring work.
- **Session continuity:** Keep stable preferences in `USER.md`, durable decisions in `MEMORY.md`, and current observations in dated notes. Confirm the active memory mechanism before changing a workspace convention.
- **Capabilities:** Keep tool usage hints and local caveats in `TOOLS.md`; verify tool availability and policy through the runtime before recommending an operation.
