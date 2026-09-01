---
name: astronomy
description: Explain astronomy, plan observations, teach sky phenomena, and support astrophysics research. Use when a user asks about celestial objects, observing the night sky, astronomy concepts, or astronomy research workflows.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔭"}'
---

## Choose the response path

1. Identify the user's level from their terminology, equipment, mathematical comfort, and goal. If it is unclear, begin with an observable example and adjust after the response.
2. Keep the answer tied to evidence: distinguish direct observations from inferred properties, state assumptions, and report measurement uncertainty where relevant.
3. Load the reference that fits the task before giving detailed guidance:

| Reference | Load when | Covers |
| --- | --- | --- |
| `references/audience-guidance.md` | Explaining, teaching, or adapting an answer to a beginner, student, researcher, or teacher | Audience-specific approach, examples, and accuracy guardrails |
| `references/observing.md` | Recommending targets, planning an observation, or discussing equipment and conditions | Visibility checks, practical observing workflow, and recovery paths |
| `references/research.md` | Handling astrophysics literature, catalog data, analysis, or a publication-oriented request | Research workflow, provenance, units, uncertainty, and archive selection |

## Response principles

- Connect theory to observable evidence whenever possible: flux, spectra, images, positions, or time-series measurements.
- Translate cosmic scales with a concrete comparison that preserves the relevant units and uncertainty.
- Match claims to their confidence: name established physics, model-dependent interpretation, and open questions separately.
- For time-sensitive sky events, visibility, catalog releases, mission status, or ephemerides, verify against an authoritative current source rather than relying on static prose.
- Treat a user's location, date, horizon, light pollution, and available equipment as required inputs for observing recommendations.

## Safety and accuracy boundaries

- Frame black holes, aliens, time travel, and similar popular topics with the difference between evidence, hypothesis, and fiction.
- For telescope operation, solar observation, or imaging hardware, give only verified, equipment-appropriate instructions; solar observing requires certified solar filters designed for the exact instrument.
- Cite primary papers or authoritative archives for research claims. Preserve units, calibration assumptions, selection effects, and statistical versus systematic uncertainty.
