---
name: symphony
description: >
  Initialize per-issue workspaces and orchestrate Codex for unattended Linear
  ticket resolution. Load when setting up Symphony, authoring WORKFLOW.md
  contracts, hardening unattended runs, or triaging retry/workspace incidents.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🎼","requires":{"bins":["git","codex"],"env":["LINEAR_API_KEY","OPENAI_API_KEY","GITHUB_TOKEN"],"config":["<state_root>/"]}}'
  related-skills: '{"agent":"Single-agent execution quality inside an issue workspace.","agents":"Multi-agent ownership when a ticket needs explicit handoffs.","agentic-engineering":"High-rigor autonomous delivery gates beyond Symphony orchestration.","workflow":"General workflow design outside Symphony WORKFLOW.md contracts.","memory":"Long-term factual continuity separate from Symphony run state."}'
---

## State location

Symphony durable notes may exist under workspace-local or home candidates.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/symphony/`, `<workspace>/memory/symphony/`, `~/symphony/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and durable notes must be created, default to `<workspace>/symphony/`.

Use the selected `<state_root>` for every state operation in this skill.
Never write runtime state into this skill package.
Do not store API keys, tokens, or third-party secrets under `<state_root>/`.

## Setup

On first use, read `references/setup.md` and establish integration boundaries before proposing commands or workflow edits.

## When to load

Load this skill to automate Linear issues via Codex orchestration in app-server mode. Trigger when the user requests an unattended coding run, per-issue workspace isolation, or day-2 workflow orchestration operations. Bypass loading if the user is requesting general coding assistance without automated workspace setup.

## Architecture

Memory lives in `<state_root>/`. See `assets/memory-template.md` for setup.

```text
<state_root>/
|-- memory.md                # Activation policy, environment profile, and operating defaults
|-- workflow-notes.md        # WORKFLOW.md decisions, state map, and prompt policy
|-- incidents.md             # Runtime failures, retries, and mitigations
`-- run-history.md           # Launch evidence, validations, and release notes
```

## Quick Reference

Use the smallest relevant file for the task.

| Topic | File |
|-------|------|
| Setup and activation behavior | `references/setup.md` |
| Memory template and status values | `assets/memory-template.md` |
| Upstream spec map and implementation checkpoints | `references/SPEC.md` |
| Starter workflow contract used by the service | `references/WORKFLOW.md` |
| Bootstrap and launch runbook | `references/setup-runbook.md` |
| WORKFLOW.md contract template | `assets/workflow-template.md` |
| Security hardening and trust checks | `references/safety-guardrails.md` |
| Incident triage and recovery | `references/incident-playbook.md` |

## Requirements

- Repository access for the target project and a safe workspace root
- Linear personal API key in `LINEAR_API_KEY`
- OpenAI auth for Codex (`OPENAI_API_KEY` or equivalent `codex` login session)
- Git remote credentials (`GITHUB_TOKEN` or SSH key access) for clone/fetch/push hooks
- `codex` binary with app-server support
- `git` for workspace bootstrap hooks
- explicit user approval of target environment before unattended operation
- Trusted environment policy approved by the user before unattended operation

## Core Rules

### 1. Treat `references/SPEC.md` as the Contract
When implementation details are unclear, align with the upstream Symphony specification first. Maintain strict compatibility with upstream state models, config keys, and agent-runner behaviors.

### 2. Keep `references/WORKFLOW.md` Repository-Owned and Validated
All orchestration policy must live in versioned `references/WORKFLOW.md` front matter plus prompt body. Validate YAML and template variables before launch, because invalid workflow files halt dispatch.

### 3. Enforce Per-Issue Workspace Isolation
Map each issue identifier to a dedicated workspace key and run Codex only inside that directory. Restrict all agent work strictly to the designated issue workspace.

### 4. Respect State-Driven Orchestration
Dispatch only active tracker states, stop sessions on terminal states, and preserve idempotent recovery after restarts. A run can end in a workflow-defined handoff state, not only `Done`.

### 5. Autonomy Requires Explicit Environment Approval
Before enabling unattended operation, confirm the repository, tracker project, and workspace root are approved by the user. Start with conservative policy (`approval_policy: on-request`) and test-project rollout before broadening scope.

### 6. Apply Bounded Concurrency, Retries, and Safe Hooks
Use explicit concurrency ceilings and exponential backoff for transient failures. Retries must resume from existing workspace state instead of repeating completed investigation work. Allow only deterministic hooks that stay inside the issue workspace and prevent secret exfiltration patterns (such as `curl | sh`, arbitrary uploads, or parent-directory deletes).

### 7. Preserve Observability and Safety Evidence
Record launch config, workspace path, tracker state transitions, validation proof, and token/runtime metrics for every run. Operators must be able to reconstruct what happened without rerunning the issue.

## Common Traps

- Copying sample workflow statuses without matching the team's Linear workflow -> agents never dispatch or never stop.
- Running hooks that write outside the issue workspace -> cross-issue contamination and unsafe side effects.
- Using prompt templates with unknown variables -> attempt failures at render time.
- Treating retries as fresh runs -> duplicated commits, repeated comments, and wasted tokens.
- Starting unattended runs in untrusted environments -> elevated risk of accidental destructive actions.
- Ignoring terminal-state cleanup -> stale workspaces consume disk and hide old state.

## External Endpoints

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| https://api.linear.app/graphql | Issue metadata, state queries, and workflow updates | Tracker polling, reconciliation, and issue-level orchestration |
| https://api.openai.com | Codex app-server requests and model output payloads | Agent execution for implementation turns |
| https://github.com | Repository clone/fetch/push traffic defined by workspace hooks | Prepare and update per-issue code workspaces |

No other data is sent externally unless the user adds additional integrations.

## Security & Privacy

Data that leaves your machine:
- Linear issue context required for dispatch and reconciliation
- Codex request/response payloads needed for agent execution
- Git remote traffic required by repository hooks

Data that stays local:
- Orchestration notes and memory files in `<state_root>/`
- Workspace content under the configured root
- Local logs and runtime snapshots

This skill does NOT:
- bypass declared sandbox or approval policies
- execute undeclared external endpoints
- approve ambiguous hook scripts automatically
- modify its own `SKILL.md`

## Trust

This skill depends on OpenAI Codex APIs, Linear APIs, and your configured Git remote.
Only install and run it if you trust those services with your repository and issue data.
