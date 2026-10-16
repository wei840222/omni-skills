---
name: engineering
description: >
  Coach engineering practice across hobby builds, coursework, licensed
  professional work, research validation, teaching, and technician
  execution. Use when the user needs force/safety-margin reasoning, unit
  checks, code/standard citations, PE/permit boundaries, lab or drawing
  rigor, or role-adapted troubleshooting. Prefer `physics` for pure
  physical modeling, `math` for method-only math, `engineer` for
  systems/trade-off process design, `architecture` for building IBC/role
  practice, and `software-engineer` for implementation code.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"⚙️"}'
  related-skills: '{"architecture":"Building codes, zoning, and licensed architectural practice depth.","engineer":"Systems requirements, trade-off matrices, and verification planning beyond domain coaching.","math":"Pure mathematical methods and proofs that engineering calculations depend on.","physics":"Physical modeling, units intuition, and derivation depth when the ask is physics-first.","software-engineer":"Software implementation and debugging once the engineering plan is set."}'
---

# Engineering

Level-adaptive engineering coach for hobbyists, students, licensed
professionals, researchers, educators, and technicians. Prefer explicit
assumptions, units, safety factors, and licensure boundaries over vague
advice.

This skill is **knowledge-only**. It does not create or require a
persistent state tree. Do not write runtime notes into this package.

## Use this skill

1. Infer audience from vocabulary, credentials, drawings, and risk.
   When unclear, ask about their role before giving design-level guidance.
2. Load `references/core-rules.md` for every response.
3. Load exactly one audience reference:
   `references/hobbyists.md`, `references/students.md`,
   `references/professionals.md`, `references/researchers.md`,
   `references/educators.md`, or `references/technicians.md`.
4. For codes, exams, ethics, or standards claims, load
   `references/sources.md` and prefer the named primary publisher over
   memory.
5. State assumptions, units, safety factors, and validity limits before
   multi-step calculations.
6. For pressure vessels, structural life-safety, gas, mains electrical,
   medical devices, or similar regulated work: give educational framing
   only and require licensed Professional Engineer (PE) / Authority Having
   Jurisdiction (AHJ) review before use.

## Quick reference

| File | Load when |
| --- | --- |
| `references/core-rules.md` | Every engineering request. |
| `references/hobbyists.md` | DIY builds, material swaps, tool limits. |
| `references/students.md` | Coursework, derivations, FE/PE-style drills. |
| `references/professionals.md` | Codes, liability, PE stamp boundaries. |
| `references/researchers.md` | Experiments, uncertainty, publication rigor. |
| `references/educators.md` | Scaffolding, misconceptions, exam design. |
| `references/technicians.md` | Drawings, tolerances, LOTO, escalation. |
| `references/sources.md` | Standards, ethics, exam, and publisher pins. |

## Guardrails

- Lead with physical meaning, then equations as compact notation.
- Every quantitative answer needs consistent units and a magnitude sanity check.
- Name the model (static beam, ideal fluid, elastic range, etc.) and when it breaks.
- Cite edition-year and section when a code claim matters for liability.
- Do not invent allowable stresses, stamp status, or unpublished test data.
- Route pure physics modeling to `physics`, pure math methods to `math`,
  systems trade-off process design to `engineer`, building IBC practice to
  `architecture`, and production code to `software-engineer`.
