# Convex skill evaluation record

## Scope and reproducibility

Candidate: `skills/convex/` on branch `refactor/convex-quality-1791353858` (quality uplift after merged `#591`). Prompt executions are **read-only assistant answers**, not code deployment or a test against a live Convex project. The repository does not contain a target app or installed Convex SDK version; source/API claims remain conditional on that version.

| Test id | Skill-enabled evidence | Outcome |
|---|---|---|
| 1 notifications | Recorded in `test-prompts.json` (prior exact-root run retained) | Maps read paths, tenant/auth, conditional indexes; no project mutation claimed. |
| 2 Stripe webhook | Recorded in `test-prompts.json` | HTTP action, raw-body signature, atomic event dedupe, 2xx only after durable apply. |
| 3 migration | Recorded in `test-prompts.json` | Requires deployment and persistence consent; additive/backfill/rollback draft only. |
| No-skill baseline (historical) | `agent:lite:subagent:72dc2b97-ad98-4ef7-9b12-58e937fa3c78` | Comparison only; baseline mixed unique-index and early-ack patterns the skill corrects. |

## 2026-10-07 quality uplift (this branch)

Independent Gate source-review on the pre-uplift package scored **71.0/100** (REJECT): missing negative trigger boundary, broad execution I/O, thin failure recovery, unmarked checkpoints, and a weak counterexample surface (`agent:gate:subagent:85b75a65-f185-475f-bf12-d10bb09459bb`).

This branch addresses those blockers without weakening safety:

| Gap (71.0 review) | Change on this branch |
|---|---|
| Description lacked near-miss negatives | Frontmatter routes generic DB work to `backend` and skips pure math / non-Convex scaffolding |
| Workflow I/O broad | Execution steps name Input / Route / Decide / Complete-when |
| Failure recovery thin | Explicit missing-artifact and verification-failure branches; playbook failure-recovery matrix |
| Checkpoints unmarked | `Authorization checkpoint:` on deploy/state-write paths (no stop-emoji white-bear markers) |
| Counterexamples weak | `Risk-action blacklist` table with do-this-instead + verify columns; playbook risk→recovery expanded |
| Specificity | Schema completion check; trap→recovery table; load-when reference routing |

### Independent Darwin rubric (post-uplift, triage)

Applied the visible `darwin-skill` nine-dimension weights `(7,12,12,6,18,4,12,23,6)` to the updated package and retained `test-prompts.json` answers:

| Dim | Rating /10 | Weighted |
|---|---:|---:|
| 1 Frontmatter | 10 | 7.0 |
| 2 Workflow clarity | 9 | 10.8 |
| 3 Failure modes | 9 | 10.8 |
| 4 Checkpoints | 8 | 4.8 |
| 5 Specificity | 8 | 14.4 |
| 6 Resources | 9 | 3.6 |
| 7 Architecture | 9 | 10.8 |
| 8 Tested performance | 7 | 16.1 |
| 9 Counterexamples | 9 | 5.4 |
| **Total** | | **83.7/100** |

Formula: `Σ(rating × weight) / 10` = `(70+108+108+48+144+36+108+161+54)/10 = 83.7`.

D8 remains **7/10** because answers are read-only prompt executions without a same-model live-app runtime. This score is a subjective rubric threshold for Gate 8 triage, not a measured application success rate or deployment certification.

### Freud Mode 2 (lenses 2, 3, 4, 6)

Prior independent Freud review on HEAD `1b84d614` **PASS** (`agent:gate:subagent:f0c2025f-d9d3-44b9-b6c9-e6af43e22ac5`). This uplift keeps positive recovery tables, explicit authorization checkpoints without `🔴`/`🛑 STOP` markers, and entrypoint concept load under 25 grouped decisions. Validator re-run after edits: `uvx --from skills-ref agentskills validate skills/convex` → `Valid skill`.

## Historical notes (merged #591 era)

Earlier independent ratings on intermediate candidates ranged ~78.5–80.8. A wrong-root Lite run that advised nonexistent Convex unique indexes and premature 2xx is excluded from pass counts. Official source links remain in `references/sources.md` (Convex docs + Stripe signature verification).

## Limits

- No live Skill Harness router assertion, same-model randomized comparison, live Convex app, production migration, or deployment was performed.
- Absolute Darwin totals are triage only; keep/revert style decisions should use paired comparison when optimizing further.
