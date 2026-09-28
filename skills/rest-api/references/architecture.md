## Architecture

Working memory lives in `<state_root>/`. See `memory-template.md` for structure and status behavior.

```
<state_root>/
├── memory.md                     # HOT: active API project context
├── contracts/                    # WARM: OpenAPI specs and compatibility notes
├── decisions/                    # WARM: ADR-style technical decisions
├── tests/                        # WARM: test plans and quality gates
├── operations/                   # WARM: runbooks and incident notes
└── archive/                      # COLD: closed projects and old versions
```

