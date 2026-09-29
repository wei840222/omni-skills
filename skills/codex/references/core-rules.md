# Core Rules


### 1. Preflight the Task Before Codex Acts
- Lock five facts first: target repo, current directory, dirty worktree state, required permissions, and expected verification.
- If any of those are unclear, pause and resolve them before running Codex with write capability.
- "Start coding" must be deferred until familiarization steps are complete in an unfamiliar repo.

### 2. Choose the Operating Mode Explicitly
- Use interactive Codex for exploratory repo work, `codex exec` for bounded non-interactive execution, and `codex review` for review-first tasks.
- If resuming or branching prior work, prefer `resume` or `fork` over re-describing the entire context from scratch.
- Treat cloud, app-server, and MCP-assisted runs as separate modes with separate risk.

### 3. Match Sandbox and Approval to Blast Radius
- Read-only fits inspection, planning, and low-trust exploration.
- Workspace-write fits normal local coding in the approved repo.
- Full access or dangerous bypass is a special-case mode that needs explicit user intent and an external sandbox story.
- Reserve high-trust modes strictly for necessary, explicit use cases.

### 4. Read the Repo Before Editing It
- Inspect tree shape, git status, entrypoints, conventions, and test surface before proposing edits.
- When the worktree is already dirty, separate user changes from agent changes and preserve existing untracked files.
- Codex should adapt to the repo, not force the repo into a generic workflow.

### 5. Keep Changes Reviewable and Scoped
- Favor minimal diffs, targeted commands, and explicit file ownership.
- Restrict edits strictly to requested tasks, ignoring speculative refactors and unrelated cleanup.
- If a command or edit expands scope, pause execution and surface that expansion immediately.

### 6. Treat Auth, MCP, and Cloud as Trust Boundaries
- A tool being available does not mean it is approved.
- Review each MCP server for scope, data access, and side effects before enabling it.
- Use existing login sessions when possible; request explicit user intent before reading secrets from local files.
- Inspect cloud diffs before applying them locally.

### 7. Verify Outcomes and Leave a Handoff Trail
- A successful Codex run ends with checks, not with code edits alone.
- Report what changed, what was verified, what failed, and what remains risky.
- For interrupted or long-running work, leave a crisp continuation state that another operator can resume without guesswork.

