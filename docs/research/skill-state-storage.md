# Research on Storage Locations for Agent Skill Runtime State and Memory

> Research date: 2026-08-04 (UTC+8)<br>
> Scope: the normative Agent Skills specification and official source, official OpenClaw documentation and source, official Claude Code documentation, and the XDG Base Directory Specification.<br>
> Statements labeled "RECOMMENDATION" are conclusions synthesized by this research, not requirements of the Agent Skills or OpenClaw specifications.

## Executive summary

1. **SPEC**: The Agent Skills specification defines only the skill-package structure, metadata, instructions, and bundled resources. It **does not define standard locations for runtime state, memory, cache, temporary data, or secrets**. The official client implementation guide also states that the specification defines only the contents of a skill directory and does not mandate installation locations.[1][2][3]
2. **SPEC**: `scripts/` contains executable programs, `references/` contains documents loaded on demand, and `assets/` contains static resources such as templates, images, lookup tables, and schemas. The specification does not define any of them as a runtime-state store.[1][2]
3. **UNKNOWN**: The Agent Skills specification does not explicitly require skill packages to be read-only and does not explicitly prohibit a script from modifying files inside its package. Whether a package is writable therefore depends on the host, installation method, sandbox, and permissions. "Not prohibited by the specification" must not be interpreted as a portable persistence contract.
4. **RUNTIME CONVENTION**: OpenClaw treats the agent workspace, which defaults to `~/.openclaw/workspace`, as a working directory and a location for private memory that can be backed up. It stores configuration, credentials, sessions, and runtime databases under a separate state root, which defaults to `~/.openclaw`. The two locations have different ownership and backup semantics.[4]
5. **RUNTIME CONVENTION**: OpenClaw agent memory consists of workspace files such as `USER.md`, `MEMORY.md`, and `memory/YYYY-MM-DD.md`. `MEMORY.md` is concise, curated long-term memory, not an arbitrary skill database or complete log.[5]
6. **RECOMMENDATION**: A portable skill should first accept state or memory locations supplied by the host/runtime. Without a host contract, choose project-local, workspace-scoped, or user-global storage according to data ownership. Do not derive writable locations from the skill installation path, and do not treat package resources as state.
7. **RECOMMENDATION**: `~/Clawic/data/<skill>/` may be **retained** as an explicitly documented Clawic convention and compatibility path for user-visible persistent data shared across runtimes. It should be **revised** into a fallback or project convention rather than described as an official Agent Skills or OpenClaw rule. Configuration, secrets, cache, and temporary data should not be mixed into it.

## Classification vocabulary

| Label | Meaning in this document |
| --- | --- |
| **SPEC** | A requirement or semantic rule directly defined by a normative standard. This document also uses the label for normative XDG directory semantics. |
| **RUNTIME CONVENTION** | Official behavior or paths of a specific host/runtime; valid for that runtime but not part of the general Agent Skills specification. |
| **RECOMMENDATION** | An engineering recommendation derived from the sources and from portability, security, and lifecycle considerations. |
| **UNKNOWN** | Not defined by the official specification or first-party documents reviewed here and therefore must not be inferred. |

## 1. Does the Agent Skills specification define a runtime-state location?

### What the specification actually defines

**SPEC**: A skill is a directory containing at least `SKILL.md` and may also contain `scripts/`, `references/`, `assets/`, and other files or directories. The specification then defines frontmatter, body content, optional-directory semantics, progressive disclosure, relative references, and validation.[1][2]

**SPEC**: The normative specification contains no field or section for `state`, `memory`, `cache`, `temporary`, `secret`, retention periods, or state migration.[1][2]

**SPEC**: The official client implementation guide discusses skill **discovery locations** at project, user, organization, and bundled scopes. It explicitly states that the Agent Skills specification does not mandate where skill directories are installed; it defines only their internal format.[3]

Therefore:

- **UNKNOWN**: There is no official cross-runtime "state root for each skill."
- **UNKNOWN**: No official writable data path can be derived from the location of `SKILL.md`.
- **RECOMMENDATION**: When a skill must persist state, treat the state-path contract as a host integration or an explicitly documented compatibility requirement of the skill, not as an existing Agent Skills capability.

## 2. May `scripts/`, `references/`, or `assets/` be used as mutable state?

| Directory | Specification semantics | Mutable-state assessment |
| --- | --- | --- |
| `scripts/` | Programs the agent may execute; they should be self-contained or clearly document dependencies and provide useful errors and edge-case handling.[1][2] | **Not a state store.** A script may read or write external state under a host contract, but the script itself is a package resource. |
| `references/` | Supplemental documents the agent reads when needed.[1][2] | **Not a state store.** Writing session results back into a reference confuses authored knowledge with user data. |
| `assets/` | Static resources such as templates, images, lookup tables, and schemas.[1][2] | **Not a state store.** The term "static resources" especially does not support treating this directory as continuously changing data. |
| Other package subdirectories | The specification permits other files and directories.[1][2] | **UNKNOWN**: Structural permission does not imply guarantees of writability, persistence, backup, or migration. |

### Why a package should be treated as immutable input

**RUNTIME CONVENTION**: Different clients may provision a skill at project, user, or organization scope, as a bundled asset, through a remote registry, or inside a sandbox. Cloud and sandbox runtimes may provision the package only as execution input.[3]

**RUNTIME CONVENTION**: OpenClaw skills may be installed in the workspace, under `<state-dir>/skills`, in additional directories, or bundled with the runtime. Install/update behavior and precedence apply. A skill package's lifecycle therefore differs from the lifecycle of user data.[6]

**RUNTIME CONVENTION**: Claude Code also separates project/personal skill locations from per-repository auto-memory. Skills live under `.claude/skills/` or `~/.claude/skills/`, while auto-memory lives under `~/.claude/projects/<project>/memory/`.[11][12]

**RECOMMENDATION**: Even when the current host happens to permit writes, preserve the following invariant. It matches the provisioning modes described by official clients and avoids recombining package and memory lifecycles that OpenClaw and Claude Code deliberately separate.[3][6][11]

```text
skill package = reinstallable, updatable, potentially read-only programs and resources
runtime state = mutable data outside the package, managed by the host or an explicit data root
```

This prevents skill updates from overwriting data, Git checkouts from becoming dirty, read-only installations from failing, same-named skills at different scopes from seeing the wrong state, and secrets from being published with a package.

## 3. OpenClaw workspace, memory, state, configuration, and data lifecycle

### 3.1 Workspace

**RUNTIME CONVENTION**: The OpenClaw workspace defaults to `~/.openclaw/workspace` and may be overridden by a profile, `OPENCLAW_WORKSPACE_DIR`, or per-agent configuration. It is the default working directory and workspace context for file tools, but it is not a hard sandbox.[4]

**RUNTIME CONVENTION**: The workspace may contain `AGENTS.md`, `USER.md`, `MEMORY.md`, `memory/`, `skills/`, and other files. Official guidance recommends treating it as private memory that may be backed up in a private Git repository, while explicitly warning against committing secrets.[4]

**Lifecycle**: The workspace contains durable content managed by the agent/user and may survive sessions, restarts, and machine migration. During migration, the workspace must be configured separately; runtime sessions and configuration are copied independently.[4]

### 3.2 Agent memory

**RUNTIME CONVENTION**: OpenClaw stores memory as Markdown inside the workspace:

- `USER.md`: stable preferences and the user model;
- `MEMORY.md`: curated durable facts, decisions, and concise summaries;
- `memory/YYYY-MM-DD.md`: detailed daily notes, observations, and session summaries;
- `DREAMS.md`: an optional human-review surface.[5]

**RUNTIME CONVENTION**: `MEMORY.md` is not a raw transcript or exhaustive archive. Memory tools may search daily notes, and important material is then distilled into `MEMORY.md`. An oversized `MEMORY.md` remains on disk, but content injected into context is truncated.[5]

**RECOMMENDATION**: A skill should not place a large domain database, per-event log, or binary artifact directly in `MEMORY.md`. If the underlying data lives in an external skill data root, write only a small durable summary or pointer that the agent needs in future sessions, subject to the runtime's consent and privacy rules.

### 3.3 State root and runtime-managed state

**RUNTIME CONVENTION**: The OpenClaw state root defaults to `~/.openclaw` and may be overridden by `OPENCLAW_STATE_DIR`. Official source describes it as the root for mutable data including sessions, logs, and caches.[7][8]

**RUNTIME CONVENTION**: Current official workspace documentation lists these runtime-owned locations:

```text
~/.openclaw/openclaw.json
~/.openclaw/state/openclaw.sqlite
~/.openclaw/agents/<agentId>/agent/openclaw-agent.sqlite
~/.openclaw/credentials/
~/.openclaw/agents/<agentId>/sessions/
~/.openclaw/skills/
```

These locations are outside the workspace and must not be committed to version control with workspace memory.[4]

**Lifecycle**: OpenClaw manages runtime databases, session rows, transcripts, routing state, and authentication state. Doctor migrates legacy sidecar state into SQLite and deletes the source only after database rows are verified.[4]

### 3.4 Configuration

**RUNTIME CONVENTION**: OpenClaw configuration defaults to `~/.openclaw/openclaw.json`, meaning `openclaw.json` inside the state root. `OPENCLAW_CONFIG_PATH` may point to another regular file. When configuration is absent, the runtime uses defaults.[7][8][14]

**RUNTIME CONVENTION**: OpenClaw-owned configuration writes use atomic replacement. The Gateway watches and reloads the file; invalid configuration rejects startup or reload instead of being rewritten as ordinary skill state.[14]

**RECOMMENDATION**: If a skill preference configures runtime integration, use the runtime configuration surface. If it is merely a field in user-owned domain data, store it in the skill data root. Do not call both kinds of data `memory.md`.

### 3.5 Cache and temporary data

**RUNTIME CONVENTION**: OpenClaw source includes cache in mutable data under the state root, though individual subsystems may use different locations and retention policies. For example, Gateway daily file logs default to `/tmp/openclaw/` even for named profiles, and official documentation states that dated logs are cleaned after 24 hours.[8][9]

**UNKNOWN**: The public OpenClaw documentation reviewed here does not define a general `<state-dir>/skills/<name>/state`, cache, or temporary-data API for arbitrary skills. `<state-dir>/skills` is a managed skill-package location and must not be inferred to be a skill data root.[6]

### 3.6 The boundary of "data" in OpenClaw

**UNKNOWN**: OpenClaw does not define a separate, general-purpose data home for third-party skills. Workspace memory, runtime-state databases, credentials, and managed skill packages each have distinct locations, but these do not imply an official `<workspace>/data/<skill>` or `<state-dir>/data/<skill>` convention.[4][5][6]

## 4. State-selection order for a portable skill

### Precedence

1. **RECOMMENDATION: runtime-managed** — Prefer a host-provided memory API, state database, workspace resolver, secret store, cache directory, or lifecycle callback. It is best positioned to handle profiles, agents, sandboxes, migration, backup, and deletion correctly.[4][5][10]
2. **RECOMMENDATION: project-local** — Use when the data belongs to one repository/project and must move with the project or be shared by a team.[3][11]
3. **RECOMMENDATION: workspace-scoped** — Use when the data belongs to one agent workspace and persists across sessions but must not be shared across agents or workspaces.[4][5]
4. **RECOMMENDATION: user-global** — Use only when the data genuinely belongs to the same OS user across projects and workspaces. It needs an explicit application namespace, configurable data root, and migration policy.[13]
5. **RECOMMENDATION: ephemeral** — Rebuildable cache, single-job scratch files, and IPC must not be promoted to durable memory.[13]

### Decision matrix

| Question | If yes | Recommended scope/location | Lifecycle |
| --- | --- | --- | --- |
| Does the host provide a memory/state API or canonical path? | Yes | **runtime-managed**; use the host resolver and do not hard-code. | Host manages migration, profiles, agents, and cleanup. |
| Is the data a project artifact, team knowledge, or repository-specific checkpoint? | Yes | **project-local**; version it only when the user wants sharing, otherwise use a gitignored project-local root. | Moves/deletes with the project; sensitive data must not be committed. |
| Does the data belong to one agent workspace only? | Yes | **workspace-scoped**; use the host-provided workspace path. | Backed up, archived, or deleted with the workspace. |
| Is the data portable domain data owned by one user across every project? | Yes | **user-global data root** configured by the application/user. | Survives sessions and restarts; requires export, backup, and migration. |
| Is the data history, undo, checkpoint, or resume metadata? | Yes | **user-global state root** or runtime state. | Survives restarts but need not be portable user data. |
| Can the data be reconstructed without loss? | Yes | Cache root. | May be deleted at any time; upgrades may invalidate it. |
| Is the data valid only for a process, login, or single job? | Yes | Runtime directory or secure operating-system temporary directory. | Clean up afterward; never treat as durable memory. |

### Portability considerations

**RUNTIME CONVENTION**: Project and user scope in the Agent Skills client guide describe **skill discovery scope**, not runtime-state scope. The two concepts must not be conflated.[3]

**RUNTIME CONVENTION**: Claude Code auto-memory is per repository, shared across worktrees, and local to one machine. This demonstrates that a runtime can define project-scoped memory without writing it into a skill package.[11]

**RECOMMENDATION**: A skill should explicitly document, in prose or machine-readable configuration:

- state owner: project, workspace, user, or runtime;
- how to obtain the canonical root, not only a fixed example;
- required and optional child paths;
- schema/version;
- create, read, update, and delete permissions;
- retention, backup, export, migration, and rollback;
- concurrent-writer and atomic-write strategy;
- behavior when state is absent, corrupt, or read-only.

## 5. Where should secrets, cache, and temporary data live?

### Secrets

**RUNTIME CONVENTION**: OpenClaw supports SecretRef so supported credentials need not appear as plaintext configuration. Secrets are resolved into an in-memory snapshot during activation. Official guidance also warns that any plaintext credential in a file readable by the agent can still be read by file or shell tools.[10]

**RUNTIME CONVENTION**: OpenClaw recommends sourcing provider credentials from the Gateway process environment, service/container/CI secrets, global runtime `.env`, configuration environment blocks, or SecretRef. A workspace `.env` is treated as a low-trust source; provider credentials and protected runtime controls from it are ignored.[7]

**RECOMMENDATION**:

- Do not place API keys, OAuth tokens, passwords, private keys, or recovery material in a skill package, project state, workspace memory, `~/Clawic/data/`, cache, or logs.
- Prefer a host secret manager, SecretRef, or operating-system credential store. A permission-protected process environment or runtime credential file is the second choice.
- Persist only nonsecret pointers such as a secret ID, environment-variable name, or credential-profile name, never the value.
- Credential owners must manage rotation, revocation, redaction, and backup exclusion.

### Cache

**SPEC**: XDG defines `$XDG_CACHE_HOME` as user-specific nonessential cached data and defaults it to `$HOME/.cache` when unset.[13]

**RECOMMENDATION**: A standalone Unix-like implementation may use:

```text
${XDG_CACHE_HOME:-$HOME/.cache}/clawic/<skill>/
```

Cache must be safe to delete and rebuild. Data that must persist and cannot be reconstructed is not cache. When the host supplies a cache directory, use the host path instead of applying XDG independently.

### Temporary/runtime data

**SPEC**: XDG defines `$XDG_RUNTIME_DIR` for user-specific runtime files such as sockets and named pipes. It requires access to be limited to that user, ties the lifecycle to the login period, prohibits persistence across a complete logout/login cycle or reboot, and says the directory is unsuitable for large files.[13]

**RECOMMENDATION**:

- Sockets, locks, and small IPC metadata: use the host runtime directory or `$XDG_RUNTIME_DIR/clawic/<skill>/`.
- Single-job intermediate files: create a secure operating-system temporary subdirectory and clean it when the job ends.
- Checkpoints required for crash recovery are not temporary; promote them to project, workspace, or user state.
- Do not treat the existence of a path under `/tmp` as a persistence guarantee, and do not write temporary files into the skill package.

### XDG boundaries among configuration, data, state, cache, and runtime files (Unix-like fallback)

**SPEC**: XDG separately defines `$XDG_CONFIG_HOME` (default `~/.config`), `$XDG_DATA_HOME` (default `~/.local/share`), `$XDG_STATE_HOME` (default `~/.local/state`), `$XDG_CACHE_HOME` (default `~/.cache`), and `$XDG_RUNTIME_DIR`. `XDG_STATE_HOME` is appropriate for history, recent files, view/layout state, and undo state that should persist across restarts but is less important to carry between systems than user data.[13]

| Category | Unix-like fallback | Examples |
| --- | --- | --- |
| Configuration | `${XDG_CONFIG_HOME:-~/.config}/clawic/<skill>/` | User preferences and nonsecret settings. |
| User data | `${XDG_DATA_HOME:-~/.local/share}/clawic/<skill>/` | User-owned domain data worth exporting or backing up. |
| Application state | `${XDG_STATE_HOME:-~/.local/state}/clawic/<skill>/` | History, resume checkpoints, last-opened state. |
| Cache | `${XDG_CACHE_HOME:-~/.cache}/clawic/<skill>/` | Indexes, download cache, derived data. |
| Runtime | `$XDG_RUNTIME_DIR/clawic/<skill>/` | Sockets, locks, login-bound IPC. |

**UNKNOWN**: XDG applies only to environments within its scope. It is not a cross-platform standard for Windows, macOS, mobile systems, cloud sandboxes, and every agent runtime. A portable skill should require a host-provided path resolver or leave OS mapping to the Clawic runtime/library rather than guessing from natural-language instructions.

## 6. Retain/revise recommendation for `~/Clawic/data/<skill>/`

### Decision: retain compatibility, revise its role

**RECOMMENDATION — RETAIN**: Retain `~/Clawic/data/<skill>/` for now, limited to these semantics:

- durable domain data explicitly owned by Clawic, readable, writable, and backupable by the user;
- a shared plain-file corpus that must be available across different agent runtimes;
- compatibility with existing repository skills that already publish this path, where changing it directly would disconnect existing data;
- clear documentation that it is a **Clawic project convention**, not an official Agent Skills or OpenClaw location.

**RECOMMENDATION — REVISE**: Stop treating it as one dumping ground for every kind of "memory/state":

1. **Separate semantics**: `data/` contains only user-owned durable domain data. Route configuration, runtime state, cache, temporary data, and secrets elsewhere.
2. **Configurable root**: Clawic should define one resolver, for example, "explicit configured root → host-provided user-data root → existing `~/Clawic/data` compatibility fallback." An environment-variable or configuration-key name must be formally defined by Clawic before a skill depends on it; this document does not present proposed names as existing interfaces.
3. **Respect host scope**: If data belongs to OpenClaw agent memory, use OpenClaw workspace memory. If it is a domain corpus, do not put it into `MEMORY.md` merely because execution occurs inside OpenClaw.[4][5]
4. **Separate new installations from legacy-data decisions**: A new Unix-like runtime may consider splitting data and state using XDG. Existing `~/Clawic/data` must not be silently moved. Detect it, inform the user, copy, verify, switch, and retain rollback.
5. **One primary data root per skill**: Make every child path relative to that root. List external/shared writes separately with their owner, consent, and lifecycle.
6. **Do not use managed skill roots as data roots**: OpenClaw's `<state-dir>/skills` is a package-installation location. Its update, precedence, and runtime-management semantics do not make it user data.[6]
7. **Do not misrepresent it as official**: Each skill's storage section should state:

```text
Storage convention: Clawic project convention (not Agent Skills or OpenClaw spec)
Default: ~/Clawic/data/<skill>/
Override: <resolver/config formally defined by Clawic>
Owner: user-global durable domain data
Excluded: credentials, cache, temporary files, host session state
```

### Recommended OpenClaw integration

```text
<Clawic data root>/<skill>/   # domain corpus; Clawic convention
OpenClaw workspace/MEMORY.md  # only concise, curated summaries or pointers required by future sessions
OpenClaw workspace/memory/    # host daily working memory
OpenClaw state root           # runtime-owned DB, sessions, credentials, and managed skills
```

This is a **RECOMMENDATION**, not a per-skill storage layout already defined by OpenClaw. In particular, the first line still requires a user/Clawic decision; do not claim that OpenClaw automatically discovers, backs up, indexes, or cleans it.

## 7. Recommended skill storage contract

For any stateful skill, document at least the following:

```yaml
# Illustrative only; not an Agent Skills frontmatter extension
scope: project | workspace | user | runtime
kind: data | state | config | cache | temporary | secret-reference
root_resolution:
  - host-provided
  - user-configured
  - documented-fallback
persistence: durable | restart-durable | session | job
backup: required | optional | never
contains_secrets: false
schema_version: "1"
migration: documented
```

**RECOMMENDATION**: Do not add this block directly to Agent Skills frontmatter. The normative specification defines `metadata` as a string-to-string map, and client support for custom fields varies.[1][2] First document the storage contract in `SKILL.md` or `references/`, or let Clawic define namespaced JSON-string metadata and a validator before describing it as a Clawic extension.

## 8. Unknowns and unsupported inferences

1. **UNKNOWN**: Agent Skills does not define a runtime-state API, canonical state directory, package-write permissions, or state-migration protocol.[1][2]
2. **UNKNOWN**: OpenClaw does not publish a canonical per-skill state/cache/temporary root for every third-party skill; this research found no official `<state-dir>/data/<skill>` contract.[4][6][8]
3. **UNKNOWN**: It is not documented whether OpenClaw backs up, indexes, retains, or deletes arbitrary custom skill data. Only documented surfaces such as workspace memory, runtime databases, and logs have defined behavior.[4][5][9]
4. **UNKNOWN**: Cross-platform expansion, overrides, permissions, schema versions, migration, and concurrent-write contracts for `~/Clawic/data/<skill>/` are not part of Agent Skills, OpenClaw, or XDG specifications.
5. **UNKNOWN**: No single first-party cross-runtime standard covers user-data, state, and cache paths across Linux, macOS, Windows, mobile systems, cloud sandboxes, and remote agents.

## Research method and version boundaries

- Public normative documentation was consulted first, followed by official GitHub source at pinned revisions for important specifications and path resolvers.
- Agent Skills source snapshot: `38a2ff82958afee88dadf4831509e6f7e9d8ef4e` (2026-07-09).[2]
- OpenClaw source snapshot: `36a2b5b00b3fcc3e5466f7dfb5d5de7ade5cc9e8` (2026-08-03). Official documentation was used as the entry point for workspace, memory, and skill loading.[4][5][6]
- Environment, path-resolver, and logging behavior was checked through official documentation and pinned source revisions.[7][8][9]
- Secret behavior was checked against the official secrets-management documentation.[10]
- Claude Code was used only as a first-party runtime-design cross-check; its paths were not elevated into general Agent Skills rules.[11][12]
- XDG was used only to propose Unix-like application-owned fallbacks. A host-provided location takes precedence over the XDG fallback.[13]

## Sources

[1] https://agentskills.io/specification
[2] https://github.com/agentskills/agentskills/blob/38a2ff82958afee88dadf4831509e6f7e9d8ef4e/docs/specification.mdx
[3] https://agentskills.io/client-implementation/adding-skills-support
[4] https://docs.openclaw.ai/concepts/agent-workspace
[5] https://docs.openclaw.ai/concepts/memory
[6] https://docs.openclaw.ai/tools/skills
[7] https://docs.openclaw.ai/help/environment
[8] https://github.com/openclaw/openclaw/blob/36a2b5b00b3fcc3e5466f7dfb5d5de7ade5cc9e8/src/config/paths.ts
[9] https://docs.openclaw.ai/logging
[10] https://docs.openclaw.ai/gateway/secrets
[11] https://code.claude.com/docs/en/memory
[12] https://code.claude.com/docs/en/skills
[13] https://specifications.freedesktop.org/basedir-spec/latest/
[14] https://docs.openclaw.ai/gateway/configuration
