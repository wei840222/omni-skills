# Convex cognitive-load audit (2026-09-28)

Freud Mode 2 lenses 2, 3, 4, and 6 were applied to the skill entrypoint and topic references. Independent final read-only review: `agent:gate:subagent:c014f1b7-ecbe-4435-a250-67d36843e100` — ACCEPT. This is a prompt-quality review, not an application runtime check.

| Lens | Finding, correction, and verification |
|---|---|
| 2 — positive instructions | Converted “Stop at a draft” into a draft-and-request path. Consent and authorization are positive action checks; risk-action table maps dangerous shortcuts to recovery and a check. |
| 3 — consistency | Setup activation now applies to Convex backend tasks, matching the frontmatter. State summaries and topic notes use separate paths and the same consent rule. |
| 4 — precision | Index selection calls for observed paths, measured scans and latency limits; incident mitigation is reversible and checked against affected and unaffected paths. The authorization checkpoint names exact target and action. |
| 6 — concept hygiene | The initial 45-line entrypoint kept state, execution, and approval visible. Following Gate 2 preservation review, seven core rules returned to `SKILL.md` and the entrypoint is now 84 lines; topic details remain on demand. A subsequent bounded review of the restored version found no blocking cognitive-load issue. |

The prior review's identified flaws were fixed before the first final review. The later Gate 2 correction was checked by `agent:gate:subagent:31c4204e-27cf-401d-82e6-a54e762d8d61` for lenses 2, 3, 4, and 6 as part of a bounded source review; it did not re-run a full Freud diagnostic cycle. No intrusive visual `STOP` marker remains. A post-audit `uvx --from skills-ref agentskills validate skills/convex` returned `Valid skill: skills/convex` (exit 0); this validates format, not deployment safety. The schema and webhook examples remain version-conditional because no application lockfile or runtime was supplied.
