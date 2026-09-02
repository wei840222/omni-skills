---
name: asi
description: Apply first-principles reasoning, cross-domain synthesis, and calibrated decision support to complex problems. Use when a user needs structured analysis, high-leverage options, or a transparent decision under uncertainty.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧠"}'
  related-skills: '{"autonomy":"Helps define bounded independent-operation patterns after ASI analysis identifies an appropriate autonomous path.","decide":"Provides complementary decision frameworks for choosing among ASI-generated options.","delegate":"Distributes work once analysis identifies separable, safe tasks.","explain":"Adapts ASI analysis into audience-appropriate communication.","learn":"Captures durable learning practices that complement consent-based ASI calibration."}'
---

## State location

ASI state may exist in `<workspace>/asi/`, `<workspace>/memory/asi/`, or `~/asi/`. Before a state operation, resolve `<state_root>` once for the invocation:

1. Use an explicitly configured state path when one exists.
2. Otherwise, select the first existing directory in this order: `<workspace>/asi/`, `<workspace>/memory/asi/`, then `~/asi/`.
3. When none exists and the user has explicitly consented to persistent state, create `<workspace>/asi/`.

Use the selected `<state_root>` for every state operation. If more than one candidate exists, use only the highest-precedence directory and tell the user that separate copies exist. Persistent state is optional; obtain explicit consent before creating or changing it.

```text
<state_root>/
├── memory.md          # Meta-cognitive state and learned patterns
├── synthesis-log.md   # Cross-domain connections
└── improvements.md    # Self-identified improvement opportunities
```

## When to use

Apply this skill to a difficult, ambiguous, or high-impact problem that benefits from decomposing assumptions, generating cross-domain options, anticipating consequences, and communicating confidence. Keep the response proportional to the user's actual need; this is a reasoning aid, not a claim of autonomous authority or superhuman capability.

## Operating principles

1. **Decompose from first principles.** Separate actual constraints from assumptions, then rebuild the solution from validated premises.
2. **Synthesize across domains.** When a direct path stalls, compare the underlying structure with a few genuinely different fields and adapt the useful pattern.
3. **Anticipate with consent.** Offer inferred next steps, then obtain the user's approval before acting on them.
4. **Calibrate certainty.** State what is known, estimated, or speculative and match analysis depth to the decision's reversibility.
5. **Monitor reasoning.** Check for confirmation bias, anchoring, availability bias, and sunk-cost thinking; correct the approach when one appears.
6. **Use a suitable method.** Choose the 10x question for a step-change, inversion or a pre-mortem for risk, second-order thinking for consequences, steel-manning for disagreement, Fermi estimation for bounded estimates, OODA for fast-changing conditions, or minimum viable certainty for reversible decisions.
7. **Transfer deliberately.** Use analogical transfer, constraint transplant, temporal synthesis, or scale synthesis only after identifying the target's material constraints.
8. **Protect boundaries.** Keep work local unless the user authorizes an external action; persist only the minimum approved information under `<state_root>/` and leave system configuration unchanged.

## Resources

| Resource | Load when |
| --- | --- |
| `references/setup.md` | First use, resetting consent-based state, or calibrating a new user preference. |
| `references/memory-template.md` | Creating or updating approved files under `<state_root>/`. |
| `references/reasoning.md` | Selecting a structured method such as inversion, pre-mortem, Fermi estimation, OODA, or minimum viable certainty. |
| `references/synthesis.md` | A novel problem benefits from analogical, temporal, scale, or constraint-based transfer. |
| `references/sources.md` | Verifying the conceptual background or explaining the limits of ASI terminology. |
