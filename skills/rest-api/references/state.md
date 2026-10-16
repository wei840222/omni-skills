# REST API State

Optional continuity for multi-session API design work. Skip this file for
one-shot reviews. Never store secrets, live tokens, connection strings, or
customer payloads under `<state_root>/` — store pointers only
(`env:API_SIGNING_KEY`, `gsm:projects/.../secrets/...`, `file:~/.config/...`).

## Resolver (repeat from SKILL.md)

1. Explicit host/user override wins.
2. Else first existing: `<workspace>/rest-api/`, `<workspace>/memory/rest-api/`,
   `~/rest-api/`.
3. If multiple exist, use highest precedence only; report the others; do not merge.
4. If none exist and the user wants continuity, create `<workspace>/rest-api/`.
5. Without `<workspace>`, read existing `~/rest-api/` only; otherwise ask before create.
6. Migrate `~/clawic/rest-api/` or `~/Clawic/data/rest-api/` only after confirmation.

## Suggested layout

```text
<state_root>/
├── memory.md          # HOT: status, product context, resource map, risks
├── contracts/         # WARM: OpenAPI drafts, compatibility notes
├── decisions/         # WARM: short ADRs
├── tests/             # WARM: gate evidence pointers (no secrets)
├── operations/        # WARM: runbooks, release check results
└── archive/           # COLD: closed projects / old versions
```

## memory.md template

```markdown
# REST API Memory

## Status
status: ongoing
version: 1.0.0
last: YYYY-MM-DD
integration: pending | done | declined

## Product Context
- Domain:
- API consumers:
- Business goal:
- Deadline:

## Architecture Decisions
| Date | Decision | Why | Impact | Owner |
|------|----------|-----|--------|-------|
| YYYY-MM-DD | Use cursor pagination | Stable ordering at scale | Client changes required | Team |

## Resource Map
| Resource | Endpoints | Auth Required | Data Owner | Notes |
|----------|-----------|---------------|------------|-------|
| users | GET/POST /users | yes | account service | |

## Quality Gates
| Gate | Status | Evidence |
|------|--------|----------|
| OpenAPI contract complete | pending | |
| Auth and authz reviewed | pending | |
| Integration tests passing | pending | |
| Observability dashboards ready | pending | |

## Release Risks
- Risk:
  Mitigation:
  Owner:

## Backlog
- [ ]

## Notes
- Stable context and caveats worth remembering.
```

## Status values

| Value | Meaning | Behavior |
| --- | --- | --- |
| `ongoing` | Context still evolving | Keep gathering constraints |
| `complete` | Core setup done | Focus on implementation / release |
| `paused` | User postponed setup | Continue without setup prompts |
| `opt_out` | User opted out permanently | Bypass setup questions |

Former label `never_ask` maps to `opt_out`.

## Hygiene

- Keep decisions and evidence linked; risks need owners and mitigations.
- Update `last` after meaningful progress.
- Decline setup → set `integration: declined` and continue useful work immediately.
