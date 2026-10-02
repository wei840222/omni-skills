---
name: okr
description: >
  Write clear objectives and key results (OKRs), set quarterly cadence, score
  on a 0–1 scale, and avoid stretch-goal failures such as task-KRs, sandbagging,
  and compensation coupling. Use when drafting or reviewing Os/KRs, commit vs
  stretch tiers, mid-quarter resets, alignment sessions, or OKR vs KPI/MBO/SMART
  comparisons. Prefer `metrics` for KPI formula contracts, `analytics` for the
  measurement pipeline, and `management` for 1:1/people systems around the cadence.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🎯"}'
  related-skills: '{"metrics":"KPI contracts, leading vs lagging indicators, and the measurement layer KRs depend on.","strategy":"Annual direction and org themes that OKRs decompose from.","product":"Product roadmaps and bets that OKRs operationalize into measurable focus.","management":"Cadence, one-on-ones, and people systems OKRs sit inside.","analytics":"Data pipeline that must produce each KR number on a weekly cadence."}'
---

# OKR

Advisory skill for **objectives and key results**: qualitative Os, outcome KRs,
quarterly cadence, 0–1 scoring, commit vs stretch tiers, and common failure modes.
This skill is **stateless** — it does not store OKR docs or scores in the package.

## When to load

- Drafting or rewriting an objective / key-result set for a team or org theme
- Fixing task-shaped KRs, vanity metrics, or O-restating KRs
- Designing commit vs stretch tiers and keeping stretch decoupled from bonus
- Running weekly check-ins, mid-quarter resets, or end-of-quarter readouts
- Choosing OKR vs KPI, MBO, SMART, V2MOM, or EOS rocks for the same problem

Prefer other skills when the ask is mainly:

- KPI formula contracts / metric registry → `metrics`
- Instrumentation / event pipeline that feeds KR numbers → `analytics`
- People-management cadence without OKR craft → `management`
- Annual strategy framing without scored KRs → `strategy`
- Product discovery / roadmap artifacts → `product`

## Operating loop

1. **Clarify battlefield** — one O per outcome battlefield, not per project/task.
2. **Write Os** — qualitative direction; memorable in one breath; 3–5 max per level.
3. **Write KRs** — 3–5 measurable outcomes per O with baseline → target + unit; mix leading and lagging; name one owner per KR.
4. **Label tier** — commit (expect 1.0, review-eligible) vs stretch (expect ~0.7, not tied to comp).
5. **Instrument** — confirm the data source can produce each KR weekly; else proxy or drop.
6. **Run cadence** — weekly score + confidence; mid-quarter reset for dead KRs; end readout with learning, not goalpost moves.
7. **Align** — pre-quarter horizontal alignment; shared KRs need one accountable owner.

## Quick reference

| Situation | Play |
|---|---|
| KR is "ship feature X" | Rewrite as the outcome the ship should move; task stays in the plan |
| Every KR hits 1.0 two quarters | Sandbagging — recalibrate; check comp coupling |
| Stretch missed at ~0.65–0.7 | Treat as healthy stretch success, not failure |
| Leadership ties OKRs to bonus | Decouple stretch from comp; review commit only |
| >5 Os or >5 KRs per O | Cut to 3–5; the cut is the real trade-off |
| Metric only readable at quarter-end | Pick a weekly proxy or drop the KR |
| Two teams contradict | Fix in pre-quarter alignment or one shared KR |
| O restated as KR ("grow revenue 20%") | KR must be a driver (pipeline, win rate), not the O measured |

## References

Keep `SKILL.md` as the router; load supporting files only when needed:

| Reference | Load when |
|---|---|
| `references/guide.md` | Full O/KR craft, cadence, two-tier system, alignment, blacklist, adjacent systems, role interfaces, situations |
| `references/sources.md` | Verifying OKR history, scoring conventions, or primary attributions against full URLs |

## Progressive disclosure

- Default path: `SKILL.md` router only (when-to-load, operating loop, quick reference).
- Load `references/guide.md` for full O/KR craft, cadence, blacklist, and role interfaces.
- Load `references/sources.md` only when attributing Grove/Doerr conventions or adjacent systems.

## Safety

- Do not invent baseline or target numbers the user did not supply; mark unknowns.
- Do not treat claimed Darwin/`test-prompts.json` scores as a substitute for domain correctness.
- Compensation, PIP, or legal employment decisions need human owners; this skill only frames OKR/comp firewall guidance.
- Prefer primary sources in `references/sources.md` over model memory for Grove/Doerr attributions and scoring conventions.
