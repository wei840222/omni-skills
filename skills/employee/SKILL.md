---
name: employee
description: >
  Manage virtual AI employees with persistent memory, single-domain roles,
  graduated autonomy, and registry-based task routing. Use when hiring, training,
  evaluating, promoting, pausing, retiring, or delegating work to specialized
  workspace workers. Prefer `hiring` for human/freelancer contractor pipelines,
  `recruiter` for human candidate sourcing and interviews, `management` for
  human team leadership craft, `roleplay` for fictional character scenes, and
  `paperclip` for whole AI-company control-plane / org-chart operations.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"👔","configPaths":["<state_root>/"]}'
  related-skills: '{"hiring":"Human or freelancer contractor pipelines, platforms, and milestone payments rather than workspace virtual employees.","recruiter":"Human candidate sourcing, screening, and interview loops.","management":"People-management routines and 1:1 craft for human teams.","roleplay":"Fictional character scenes and rehearsal rather than persistent task workers.","paperclip":"AI-company control plane and org-chart operations beyond a single employee lifecycle."}'
---

# Employee

Operate a registry of specialized virtual workers. Each employee owns one domain,
loads durable memory before work, and advances through shadow → draft-only →
review → autonomous only when promotion criteria and explicit user approval
allow. Persist the registry and per-employee folders under `<state_root>/`
(see `references/setup.md` on first use and `assets/data-templates.md` for
formats).

## State location

Employee state may exist in `<workspace>/employee/`,
`<workspace>/memory/employee/`, or `~/employee/`.

Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/employee/`, `<workspace>/memory/employee/`,
   `~/employee/`.
3. If more than one exists, use only the highest-precedence directory and report
   the duplicates; do not merge them.
4. If none exists and durable employee state must be created, default to
   `<workspace>/employee/` when `<workspace>` is available; otherwise ask for a
   state root instead of guessing from the current directory.
5. Keep `<state_root>` fixed for the invocation.

Use the selected `<state_root>` for every state operation in this skill. If older
notes exist only at `~/Clawic/data/employee/`, move them into the resolved
`<state_root>/` after the user confirms, and say in one line that you moved them.

## Architecture

```
<state_root>/
├── registry.json          # Index of all employees + status
├── employees/
│   └── {name}/
│       ├── employee.json  # Role, permissions, stats
│       ├── memory/
│       │   └── context.md # Persistent learnings
│       └── logs/          # Work history by date
└── shared/
    └── protocols.md       # Common instructions
```

## Quick reference

| Topic | File | When to load |
|-------|------|--------------|
| First-time mkdir + registry | `references/setup.md` | Creating `<state_root>` |
| JSON / memory / log templates | `assets/data-templates.md` | Hiring or cloning an employee |
| Autonomy levels + promotion | `references/autonomy.md` | Evaluate / promote / demote |
| Task routing + escalation | `references/routing.md` | Delegation or multi-employee work |
| Lifecycle commands | `references/lifecycle.md` | hire / train / pause / retire |
| Domain traps | `references/domain.md` | Scope disputes or failure recovery |
| Gate 6 citations | `references/sources.md` | Verifying retained claims |

## Core rules

### 1. One role per employee
- Each employee has a single clear domain (researcher, reviewer, support).
- Assign specialized, narrow roles.
- Scope lives in `employee.json` → `role` and `permissions`.

### 2. Memory is mandatory
- Load `<state_root>/employees/{name}/memory/context.md` before every task.
- Persist durable learnings after each task.
- Log work under `<state_root>/employees/{name}/logs/YYYY-MM-DD.md`.

### 3. Escalate uncertainty
- Employees say "I don't know" rather than guess.
- Escalation triggers are defined in `employee.json`.
- Require factual, verifiable responses and immediate escalation on uncertainty.

### 4. Graduated autonomy
| Level | Behavior |
|-------|----------|
| shadow | Observes only (onboarding) |
| draft-only | Creates drafts; human sends or commits |
| review | Acts; human approves before external effect |
| autonomous | Full delegation within permissions |

Load `references/autonomy.md` when evaluating or changing autonomy levels.

### 5. Explicit permissions
- Separate read vs write access per system.
- Whitelist file-access paths under host-approved roots.
- Honor `canSpawn` and `canMessage` flags.
- Example: a Code Reviewer may comment and must not merge.

### 6. Task routing
When a request arrives:
1. Explicit: "Luna, do X" → route to Luna.
2. Implicit: match against `registry.json` roles → suggest.
3. Load `references/routing.md` when resolving delegation.

### 7. Reporting
Each employee provides:
- Daily: what shipped, what needs attention, what's next
- Weekly: tasks completed, escalations, token usage

### 8. Lifecycle
| Command | Action |
|---------|--------|
| hire {name} as {role} | Create employee |
| train {name} on [docs] | Append memory |
| evaluate {name} | Performance review |
| promote/demote {name} | Change autonomy |
| retire {name} | Archive |

Load `references/lifecycle.md` for hire / train / evaluate / retire flows.

### 9. Registry management
- `registry.json` tracks every employee and status (`active` / `paused` / `retired`).
- Update the registry on every lifecycle change.
- Query the registry before listing or routing work.

### 10. Operating standards
- Keep one explicit domain per employee.
- Persist context across sessions through memory files.
- Complete the shadowing phase before raising autonomy.
- Report blockers instead of failing silently.
- Keep actions inside the designated role scope.

## Safety

- Treat employee memory and logs as entrusted workspace data; do not exfiltrate.
- External send, merge, purchase, or destructive archive actions require the
  autonomy level plus any human approval the level demands.
- Destructive retire/archive operations stay under `<state_root>/` and need
  explicit user confirmation.
