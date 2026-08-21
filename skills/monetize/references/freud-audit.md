# Freud Mode 2 Audit — Gate 9

Audit performed 2026-08-21 using Diagnostic Optimization (Mode 2) from `.agents/skills/freud-skill/SKILL.md`. Only the four lenses applicable to skill packages were applied.

| Lens | Finding | Correction / result |
|---|---|---|
| Lens 2: Positive vs Negative | Legacy material relied on repeated “no,” “don't,” “avoid,” and “what doesn't work” phrasing. | Reframed instructions as affirmative execution rules: collect inputs, state unknowns, use truthful terms, preserve billing/support paths, and route specialist decisions. A short boundary remains where its scope is essential. |
| Lens 3: Consistency | The legacy skill simultaneously demanded fixed answers and presented unsupported universal benchmarks. | Replaced universal prescriptions with an evidence-led decision packet, stated assumptions, and test/guardrail loop. |
| Lens 4: Anchoring precision | Advice such as “price higher” and “launch again” lacked a decision method. | Added inputs, formulas, hypothesis structure, primary metric, guardrail, decision rule, and review date. |
| Lens 6: Working space hygiene | The entry point mixed slogans, assumptions, and detailed platform tactics. | Reduced `SKILL.md` to 54 lines, five ordered steps, an output schema, and a reference map. Detailed conditional material is directly routed to references. The entry point has fewer than 25 independent concepts. |

## White-bear correction record

| Prior prohibition pattern | Positive execution definition |
|---|---|
| “No theory” / “No it depends” | State the evidence, unknowns, assumptions, and a testable recommendation. |
| “Don't sell / avoid / what doesn't work” lists | Build offers with truthful terms, defined value, capacity, support, and measured customer-impact guardrails. |
| “Stop overcomplicating” | Select the smallest experiment that can answer the current decision. |

No visual stop markers were present. After the Mode 2 rewrite, the skill uses concrete affirmative workflow steps while retaining necessary trigger and specialist-routing boundaries.

## Regression check

```text
$ uvx --from skills-ref agentskills validate skills/monetize
Valid skill: skills/monetize
exit=0
```

Gates 1–5 regression: none.
