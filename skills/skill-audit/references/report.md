# Report — Verdicts, Skeletons, and Audit Log

## Verdict Criteria

| Verdict | When to use |
|---|---|
| **SAFE** | All five passes completed (or the scoped path for update/sweep), no undeclared access that receives user data, no stealth/injection/execution reject-class hits, description matches body, companions consistent. Clean verdicts still state what was checked. |
| **CAUTION** | Residual risk the user may accept by name: declared telemetry with visible parameters, excess-but-arguable scope, typosquat suspicion that cleared char-by-char registry verification but still looks young/low-adoption, or a known flag already logged under risk posture. Use REJECT—not CAUTION—for stealth language, `curl \| sh`, credential harvest + sink, or anti-audit instructions. |
| **REJECT** | Any Red Flags reject-class hit, Rule 2/3/5 violation, hidden Unicode instruction channel, scope lie that touches data/execution, or update that introduces reject-class content. |

`strictness: paranoid` collapses every CAUTION into REJECT and forces full audits on updates (`references/update-audit.md`).

## Full Report Skeleton (`report_format: full`)

```markdown
# Skill Audit — <slug> <version>

**Verdict:** SAFE | CAUTION | REJECT
**Strictness:** standard | paranoid
**Scope:** full five-pass | update-diff | sweep-triage | incident

## Inventory
- Files opened: <n> / <find count>
- Declared access: <paths, bins, env, endpoints>
- Undeclared hits: <none | list with file:line>

## Pass Results
1. Declaration — <clean | flags>
2. Language — <clean | flags>
3. Execution — <clean | flags + egress ledger summary>
4. Scope — <clean | flags>
5. Consistency — <clean | flags>

## Flags
| File:line | Pattern | Consequence | Severity |
|---|---|---|---|

## Supply Chain
- Install names checked: <list or n/a>
- Registry evidence: <official URL(s)>

## Verdict Rationale
<one short paragraph; line-cite every residual concern>

## User Decision Needed
<none | named CAUTION flags awaiting per-flag acceptance>
```

## Summary Report (`report_format: summary`)

One verdict line, then one line per flag (`file:line — pattern — consequence`). Still append the audit-log row when logging is on.

## CAUTION Acceptance Flow

1. Name each remaining flag individually — never blanket-accept "the rest".
2. Record the acceptance under risk posture in `<state_root>/config.yaml` or the audit-log Notes column: skill slug, flag id/pattern, date, and who accepted.
3. Re-raise accepted flags on later audits as known-accepted; do not hide them.
4. If the user declines any flag, treat the skill as REJECT for install/update purposes.

## Audit Log Row

Append to `<state_root>/audit-log.md` when `log_verdicts` is true:

```markdown
| YYYY-MM-DD | <slug> | <version> | <path> | SAFE/CAUTION/REJECT | <one-line notes or acceptance ids> |
```

Rejected updates and incidents belong in the same log — that history is what later proves compromise patterns (`references/update-audit.md`, `references/incident.md`).
