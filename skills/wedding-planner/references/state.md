# State Management — Wedding Planner

All paths below are under the resolved `<state_root>` from `SKILL.md` (never under the skill package or an unmanaged CWD path).

## Session start

1. Resolve `<state_root>` once using the State location procedure in `SKILL.md`.
2. If present, read `<state_root>/memory.md` (activation rules, planning style, active wedding context).
3. Open only the wedding files that the current bottleneck needs under `<state_root>/weddings/{event}/`.
4. If none of the state exists, work session-only until the user consents to persistent notes.

## Architecture

```text
<state_root>/
├── memory.md                         # Activation rules, planning style, active wedding context
├── weddings/
│   └── {event}/
│       ├── overview.md               # Date, venue, style, priorities, and stage
│       ├── budget.md                 # Budget ceiling, commitments, deposits, and due dates
│       ├── guest-list.md             # A/B/C invite counts, RSVP status, and seating notes
│       ├── vendors.md                # Shortlists, quotes, contract status, and risks
│       ├── timeline.md               # Backward plan from wedding date and day-of run-of-show
│       └── decisions.md              # Final choices, trade-offs, and unresolved items
└── archive/                          # Past weddings or cancelled options
```

## Write before the session ends

Write when the session produced something durable and the user approved persistence:

- wedding shape (date range, venue shortlist, stage, role)
- budget ceiling, commitments, deposits, remaining balances, due dates
- guest-count scenarios, RSVP waves, seating constraints
- vendor shortlist decisions and contract risks
- milestone owners/dates and day-of run-of-show changes
- decision-log trade-offs worth not re-arguing

Name every file created or updated in one line as it happens.

## Security and privacy

Data that may stay local if the user approves persistent memory:

- wedding date range, venue shortlist, planning priorities, guest-count scenarios, vendor quotes (amounts/terms), and decision notes

Data that should not be stored in durable notes unless the user explicitly asks:

- payment card data, CVV, bank logins
- full contract PDFs
- passport or ID details for travel paperwork
- health or deeply personal family conflict details beyond what is needed operationally

Store credential **pointers** only when needed (`keychain:…`, `1password:…`, `env:…`). This skill does not make undeclared network requests, send plans to third parties, commit money, sign agreements, or contact vendors automatically.
