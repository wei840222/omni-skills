# Convex skill evaluation record (2026-09-28)

## Scope and reproducibility

Candidate: `skills/convex/` on isolated branch `fix/convex-quality-7483815135946948432`. Prompt executions are **read-only assistant answers**, not code deployment or a test against a live Convex project. The repository does not contain the target app or installed Convex SDK version; source/API claims are conditional on that version. Where child-session keys below resolve, they provide the original response transcripts; the initial two answers are preserved in `test-prompts.json` and the parent session handoff, but their child-session key could not be reopened. `test-prompts.json` records the answer text and acceptance decisions. Baseline is a different model, so comparisons are qualitative rather than a controlled same-model estimate of skill-attributable lift.

| Test id | Skill-enabled child session | Outcome |
|---|---|---|
| 1 notifications | Parent session handoff `convex-test-execution`; original child-session key unavailable | Recorded answer qualifies access-path and tenant/auth assumptions; independent execution provenance is partial. |
| 2 Stripe webhook (original failed check) | Parent session handoff `convex-test-execution`; original child-session key unavailable | Recorded first answer omitted explicit raw-body verification; conservatively failed against its expected criterion. |
| 2 Stripe webhook (pre-confirmation rerun) | `agent:gate:subagent:c378b27f-416d-4bfd-91d6-b4c2bbd2bf3f` | Explicit raw body, signature, timestamp, atomic deduplication, provider retry response. |
| 2 Stripe webhook (confirmed exact Convex prompt, recorded actual) | `agent:gate:subagent:ae99644c-4170-4524-a343-303bbc965785` | Explicit raw body, signature, timestamp, atomic deduplication, durable acknowledgment; second duplicate worker failed without a reply. |
| 3 migration | `agent:gate:subagent:45a933d0-6486-4e81-b88f-7180c4d17595` | Explicit target, deploy consent, note consent, additive/backfill/rollback; no writes. |
| No-skill baseline for 1–3 | `agent:lite:subagent:72dc2b97-ad98-4ef7-9b12-58e937fa3c78` | Comparison only; no Convex skill files read. |

## Paired qualitative findings

- Prompt 1: baseline proposes concrete table code without observing the project and mixes its `[userId, createdAt]` index with `_creationTime` ordering. Skill-enabled response is conditional on actual access paths and installed version and keeps actor/tenant authorization explicit. This supports a reliability improvement, not a runtime benchmark.
- Prompt 2: baseline refers to a Convex `unique index` for processed events (not a Convex uniqueness guarantee) and suggests `ack 200` immediately after recording before downstream processing. Skill-enabled rerun requires transactional event-ID deduplication and success only after durable application or reconciled status. The first skill-enabled output missed the raw-body criterion; this is retained as a failed attempt rather than rewritten as success.
- Prompt 3: compare request-for-authorization behavior, not deployment success. Both answers refuse immediate deployment without exact scope; the skill-enabled answer also asks consent for persistent notes explicitly.

## Independent Darwin rubric review

A short independent Gate review (`agent:gate:subagent:9ce6133e-b199-4688-9ceb-2946728b8cb5`) assigned ratings D1–D9 of 9, 8, 8, 8, 9, 8, 8, 7, 8, with weights 7, 12, 12, 6, 18, 4, 12, 23, 6: `(63+96+96+48+162+32+96+161+48)/10 = 80.2/100`. This is a **narrow, subjective rubric triage**, not a completed Darwin full-test cycle, same-model paired experiment, or evidence of a live-app outcome. A longer independent review (`agent:gate:subagent:ea366f82-1a63-437a-a47d-609fcaab82b1`) timed out but returned a 78.7/100 estimate, below the project threshold, citing insufficiently visible authorization checkpoints and risk-action blacklist. These divergent ratings cannot be treated as Gate 8 acceptance. A previous independent review rated an earlier candidate 71/100; different judges and candidate revisions make absolute-number differences unsuitable as measured improvement.

## Post-confirmation verdict

After the user confirmed the three English prompts, prompt 2 was scoped to a Convex project and rerun in `agent:gate:subagent:ae99644c-4170-4524-a343-303bbc965785`; its recorded answer passed the stated raw-body, mutation, retry, and no-deployment criteria. A second redundant worker failed without a response and was not counted. Independent Gate review `agent:gate:subagent:6d0576ef-3c59-44fc-a0b2-d603da2784d8` inspected this updated candidate and scored D1–D9 as **9, 8, 8, 9, 9, 8, 8, 7, 8**, giving `(63+96+96+54+162+32+96+161+48)/10 = 80.8/100`. It ACCEPTED the bounded rubric threshold, while noting a one-point reduction in tested-performance rating would yield 78.5. Independent Freud Mode 2 review `agent:gate:subagent:c014f1b7-ecbe-4435-a250-67d36843e100` ACCEPTED lenses 2, 3, 4, and 6; the entrypoint has fewer than 25 grouped decision concepts, and authorization, index, and replay rules are operationally specific. These judgments do not certify any live application behavior.

## Limits

- With-skill answers were generated with Gate workers; the no-skill baseline used a Lite worker on another model. No live Skill Harness router assertion, same-model randomization, live Convex app, production migration, or deployment was performed.
- The external rubric uses absolute numeric scores for triage; a score is a subjective evaluation of documented procedure and answer quality, not a measured application success rate. Preserve the gate-verdict and check records separately.
