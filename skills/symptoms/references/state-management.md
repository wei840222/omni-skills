# State management

## Resolver

Before the first read or write in an invocation:

1. Use an explicit state root if the user or host configured one.
2. Otherwise use the first existing directory among `<workspace>/symptoms/`, `<workspace>/memory/symptoms/`, and `~/symptoms/`.
3. If more than one exists, use only the highest-precedence directory and tell the user. Do not merge or sync copies.
4. If none exists and the user wants to save a log, create `<workspace>/symptoms/`. If `<workspace>` is unavailable, ask for a path before creating files.

Keep the chosen `<state_root>` fixed for the rest of the invocation.

## Layout

```text
<state_root>/
├── log/
│   └── YYYY/
│       └── MM/
│           └── DD.md
├── patterns.md
├── for-doctor/
│   └── appointment-YYYY-MM-DD.md
└── medications.md
```

| Path | Required? | Role | Create when |
|---|---|---|---|
| `<state_root>/log/YYYY/MM/DD.md` | Optional until first entry | Daily symptom entries | The first symptom that day is recorded |
| `<state_root>/patterns.md` | Optional | Repeated factors the user asked to keep | A pattern is spotted and the user wants it saved |
| `<state_root>/for-doctor/appointment-YYYY-MM-DD.md` | Optional | One visit summary | The user asks to prepare for an appointment |
| `<state_root>/medications.md` | Optional | Medicines and home measures the user already named | The user reports a medicine or a measure they tried |

Do not create the optional files in advance. Resource files in this package (`references/`, `assets/`) are not state and do not use `<state_root>`.

## Legacy path

`~/Clawic/data/symptoms/` is not in the lookup order. Do not read it as the live log and do not delete it during a refactor. Copy only after the user asks, then confirm the destination file count before they retire the original.

## Write limits

- Health notes stay under `<state_root>/`.
- Do not write secrets, portal passwords, tokens, or national ID numbers. Replace a pasted secret with a pointer and say so in one line.
- Do not write state into the skill package or a path relative to the current working directory.
