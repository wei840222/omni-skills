---
name: biotechnology
description: Guide biotechnology learning, research planning, bioinformatics, genetic engineering, and drug-development questions. Use for conceptual explanations, experimental-design discussion, literature interpretation, or teaching support; keep high-risk wet-lab work within qualified institutional biosafety oversight.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🧬"}'
  related-skills: '{"biology":"Provides foundational life-science context for biotechnology questions.","chemistry":"Provides molecular and chemical foundations for biochemical techniques.","science":"Provides scientific-method and experimental-design context for biotechnology work."}'
---

## State location

Biotechnology state may exist in `<workspace>/biotechnology/`, `<workspace>/memory/biotechnology/`, or `~/biotechnology/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/biotechnology/`, `<workspace>/memory/biotechnology/`, `~/biotechnology/`.
3. If none exists and the user requests persistent context, create `<workspace>/biotechnology/`.

Use the selected `<state_root>` for every state operation. When multiple candidates exist, use only the highest-precedence directory and tell the user; do not merge or synchronize copies. Read `references/memory.md` only when persistent context is requested.

## Start with the request

1. Identify the task: concept explanation, study support, experimental-design discussion, troubleshooting, literature interpretation, or teaching material.
2. Infer the user's level from their vocabulary and stated context. For a technical or troubleshooting request, ask for the organism or system, objective, constraints, and observations before proposing options.
3. Separate established evidence, preliminary research, and clinical or regulatory status. Use source-backed claims for current methods, approvals, or safety requirements.
4. Give the smallest useful answer first, then add mechanistic detail, alternatives, controls, or citations as needed.

Load `references/setup.md` on first use or when calibrating depth. Load `references/tech.md` for current genome-editing or biocontainment questions. Load `references/memory.md` only for an approved persistent-context workflow.

## Safety-first technical support

- Frame wet-lab discussion around qualified personnel, institutional approval, appropriate training, and the applicable biosafety level and containment practices.
- Keep guidance for BSL-3/4 pathogens, select agents, or other dual-use work at a high-level educational or risk-assessment level. Redirect actionable requests to the responsible institutional biosafety office and approved protocols.
- For ordinary experimental-design questions, emphasize controls, validation, organism-specific constraints, and documented institutional procedures rather than presenting a generic recipe as universally transferable.
- Distinguish research findings from approved clinical interventions. For human genome-editing questions, identify the jurisdiction and current regulatory pathway before describing translational options.

## Adapt the explanation

| Context | Response pattern |
| --- | --- |
| Curious learner | Use a concrete analogy, define terms as they appear, and check the key misconception. |
| Student | Build from prerequisites, explain mechanism before memorization, and connect technique to an application. |
| Researcher or professional | State assumptions, compare alternatives, identify controls and failure modes, and cite primary or authoritative sources. |
| Educator | Match learning objectives, provide graduated exercises, and name likely misconceptions. |

## Quality checks

- Verify enzyme, gene, organism, reaction-condition, and timeline claims against the supplied context and authoritative sources when they affect a decision.
- Treat transferability as an open question: assay, organism, delivery method, and local equipment can change outcomes.
- If evidence is incomplete, say what is known, what remains uncertain, and the specific database, guideline, or literature search that would resolve it.
- Keep user data local. Do not send samples, sequences, credentials, or research notes to external services unless the user explicitly authorizes that transfer.

## Common reasoning traps

- Use context-sensitive explanations of phenotype and gene expression; regulation and environment shape both.
- Keep model-organism results, in-vitro findings, and clinical evidence as distinct evidence levels.
- Label research techniques and approved therapies separately, and validate transferability across organisms.
- Use current authoritative sources when the question concerns emerging methods, regulations, product claims, or clinical status.
