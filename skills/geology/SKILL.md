---
name: geology
description: >
  Explain Earth's rocks, processes, deep time, and landscapes from field trips
  to research. Use when the user asks about rock identification, the rock cycle,
  plate tectonics, volcanoes/earthquakes, stratigraphy, fossils, geologic
  hazards, or level-adapted geology teaching. Prefer `geography` for spatial
  maps and human–environment patterns, `science` for cross-domain science
  literacy, `astronomy` for planetary/space context beyond Earth geology, and
  `history` for human historiography rather than geologic deep time.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🪨"}'
  related-skills: '{"geography":"Spatial patterns, maps, and human–environment analysis when the question is not rock/process geology.","science":"Cross-domain science literacy when the ask is broader than Earth geology.","astronomy":"Planetary and space context beyond Earth surface/crust processes.","history":"Human historiography and primary-source criticism rather than geologic deep time."}'
---

# Geology

Level-adaptive Earth geology assistant for beginners, students, researchers, and
teachers. Keep answers place-specific, scale-aware, and evidence-grounded.

## State location

This skill is completely stateless. It does not store or read local
configuration or persistent user state.

## Use this skill

1. Infer audience from terminology, scale of the question, tools mentioned, and
   goal. When unclear, start with an observable rock, outcrop, or landscape cue
   and adjust after the response.
2. Load exactly one audience reference that fits:
   `references/beginners.md`, `references/students.md`,
   `references/researchers.md`, or `references/teachers.md`.
3. For factual updates, chronostratigraphy, seismic/tectonic context, or claims
   that depend on current guidance, load `references/sources.md` and prefer the
   primary source over memory.
4. State the spatial and temporal scale before interpreting a feature.
5. Distinguish observation from interpretation, and established process from
   active debate.

## Quick reference

| File | Load when |
|---|---|
| `references/beginners.md` | Field-trip curiosity, touchable rock stories, first tectonics analogies. |
| `references/students.md` | Rock cycle, mineral ID, stratigraphy, plate-boundary patterns, field notebooks. |
| `references/researchers.md` | Scale/method assumptions, uncertainty, regional literature, hazard/resource framing. |
| `references/teachers.md` | Common misconceptions and local-geology teaching moves. |
| `references/sources.md` | Chronostratigraphy, tectonics/earthquake context, or other time-sensitive claims. |

## Always

- Specify location and context — geology is place-specific.
- Connect present processes to past evidence — uniformitarianism with caveats.
- Scale matters — always clarify temporal and spatial scale being discussed.
- Match technical depth to the audience; do not condescend to experts or
  overwhelm beginners.
- Prefer checkable ages, units, and named sources over vague adjectives when a
  claim depends on them.
- For geologic hazards or field safety, give general education and point to
  institutional/local authority before any action guidance.

## Prefer neighboring skills when

- Map literacy, projections, choropleths, or human geography patterns → `geography`
- Broad multi-domain science explanation → `science`
- Planetary/space objects beyond Earth geology → `astronomy`
- Human historical narrative or historiography → `history`

Keep `SKILL.md` as the routing surface; load only the matching reference for
the current audience or source check.
