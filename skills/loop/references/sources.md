# Sources Ledger — Loop (Gate 6)

Primary references used to harden iteration caps, stop rules, retry discipline, and state portability. Re-open these URLs before quoting mutable guidance.

## Agent Skills format (Gate 1 authority)

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt

## Iteration / retry / stop rules

- Kubernetes Jobs: backoffLimit and failed pod handling — https://kubernetes.io/docs/concepts/workloads/controllers/job/
- Google SRE Workbook: Addressing Cascading Failures (retry / backoff framing) — https://sre.google/workbook/addressing-cascading-failures/
- AWS Architecture Blog: Timeouts, retries, and backoff with jitter — https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- OWASP: Error Handling and Logging Cheat Sheet — https://cheatsheetseries.owasp.org/cheatsheets/Error_Handling_Cheat_Sheet.html

## Knowledge updates applied in this refactor

| Topic | Change |
| --- | --- |
| Clawic state root | Replaced `~/Clawic/data/loop/` with portable `<state_root>/loop/` resolver |
| Scope wording | Replaced emoji NEVER lists with action-forward Critical rules; commits/deploys/config stay out of scope unless explicitly authorized |
| Related skills | Added `cycle` and `workflow` boundaries that already exist in-repo |
| OpenClaw metadata | Kept emoji only; removed all-platform `os`, empty `requires.bins`, and unsupported `displayName` |
| Stop rules | Kept hard max 10 / default 5; aligned retry framing with SRE/AWS backoff and Job backoffLimit concepts |
