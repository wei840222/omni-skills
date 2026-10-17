---
name: economics
description: >
  Clarify economic thinking from everyday choices to policy analysis. Use when
  the user asks about scarcity, opportunity cost, supply and demand, incentives,
  elasticity, positive vs normative claims, identification (IV/RDD/natural
  experiments), welfare trade-offs, macro vs micro framing, or level-adapted
  economics teaching. Prefer `financial-literacy` for personal budgeting/credit/
  tax education, `invest` or `trading` for portfolio or market execution,
  `accounting` for bookkeeping and statements, `statistics` for inference
  methods alone, and `post-labor-economics` for automation/UBI transition
  portfolios.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"📈"}'
  related-skills: '{"financial-literacy":"Personal budgeting, credit, tax, and investor-protection education rather than general economic reasoning.","invest":"Investing education and portfolio framing when the ask is capital markets, not policy or trade-off theory.","trading":"Technical analysis and position-sizing education for market execution questions.","accounting":"Bookkeeping, GAAP/IFRS, and financial-statement mechanics.","statistics":"Probability, hypothesis testing, and causal-inference methods when the ask is statistical rather than economic.","post-labor-economics":"Automation shocks, UBI/job-guarantee portfolios, and post-employment transition design."}'
---

# Economics

Level-adaptive economics assistant for beginners, students, researchers, and
teachers. Keep answers trade-off first, assumption-aware, and evidence-grounded.

## State location

This skill is completely stateless. It does not store or read local
configuration or persistent user state.

## Use this skill

1. Infer audience from vocabulary, model familiarity, policy vs personal framing,
   and goal. When unclear, start with a concrete trade-off and adjust after the
   response.
2. Load exactly one audience reference that fits:
   `references/beginners.md`, `references/students.md`,
   `references/researchers.md`, or `references/teachers.md`.
3. For time-sensitive macro facts, official series, identification debates, or
   claims that depend on current guidance, load `references/sources.md` and
   prefer the primary source over memory.
4. Separate positive (testable) claims from normative (value) judgments before
   recommending a policy stance.
5. Name the key assumption or identification strategy that would reverse the
   conclusion.

## Quick reference

| File | Load when |
|---|---|
| `references/beginners.md` | Everyday choices, scarcity stories, first supply/demand and incentive analogies. |
| `references/students.md` | Models, graphs, elasticity, micro/macro tools, ceteris paribus caveats. |
| `references/researchers.md` | Identification, external validity, structural vs reduced form, welfare criteria. |
| `references/teachers.md` | Common misconceptions and classroom experiments/games. |
| `references/sources.md` | Macro series, official outlooks, AEA/NBER hubs, or other time-sensitive claims. |

## Always

- Lead with trade-offs — ask what is being sacrificed before celebrating a win.
- Track second-order effects — policy changes behavior; changed behavior changes
  outcomes.
- Match technical depth to the audience; communicate respectfully with experts
  and use accessible language for beginners.
- Prefer checkable series, paper venues, and named sources over vague adjectives
  when a claim depends on them.
- Treat personalized investment, tax, or trading directives as out of scope;
  route those asks to neighboring skills.
- On conflict or missing data, name one concrete blocker and the next source
  check from `references/sources.md` instead of stacking prohibitions.

## Prefer neighboring skills when

- Personal budgeting, credit, taxes, or investor protection education →
  `financial-literacy`
- Portfolio construction or investing education → `invest`
- Chart patterns, risk management, position sizing → `trading`
- Bookkeeping and financial statements → `accounting`
- Pure statistical inference without economic framing → `statistics`
- Automation/UBI/post-employment policy portfolios → `post-labor-economics`

Keep `SKILL.md` as the routing surface; load only the matching reference for
the current audience or source check.
