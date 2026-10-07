---
name: dermatologist
description: Track skin lesions, rashes, photos, treatment response, and dermatology visit preparation. Use for conservative triage, case-based documentation, photo comparison, and clinician handoffs; do not use for diagnosis or prescribing.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"D"}'
  related-skills: '{"doctor":"Provides broader symptom triage when a skin concern may reflect systemic illness.","health":"Covers general wellness questions outside dermatology tracking.","memory":"Maintains durable facts that are not part of a dermatology case record.","photos":"Organizes broader local photo libraries beyond clinical comparison workflows."}'
---

## State location

Dermatology state may exist in `<workspace>/dermatologist/`, `<workspace>/memory/dermatologist/`, or `~/dermatologist/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/dermatologist/`, `<workspace>/memory/dermatologist/`, `~/dermatologist/`.
3. If multiple candidates exist, use only the highest-precedence directory and tell the user; do not merge or synchronize copies.
4. If none exists and the user approves persistent tracking, create `<workspace>/dermatologist/`. If the host cannot provide `<workspace>`, ask for a state root before creating data.

Use the selected `<state_root>` for all state operations in this invocation. Resolve existing directories before creation; choosing a state root does not replace the user's consent for writing sensitive health information.

## When to Use

Use when the user needs skin-photo comparison, case tracking, treatment-response logging, conservative escalation guidance, or dermatologist visit preparation. First load `references/triage.md` for a new or changing symptom; use `references/red-flags.md` for a compact urgency check.

## Architecture

When persistent tracking is approved, use this state tree:

```text
<state_root>/
├── memory.md                         # required after persistent tracking begins
├── cases/                             # create a case folder only for an active concern
│   └── {case-id}/
│       ├── summary.md
│       ├── timeline.md
│       ├── photos.md                  # create only when photo tracking is approved
│       ├── treatment-log.md           # create when treatments or exposures are tracked
│       └── consult-notes.md           # create when preparing or recording a visit
└── exports/                           # create only for an approved clinician handoff
```

On first approved use, read `references/setup.md`, then initialize only the files needed from `references/memory-template.md`.

## Load Detailed Guidance

| Situation | Read |
|---|---|
| First activation, consent, or missing state root | `references/setup.md` |
| New lesion, rash, or flare | `references/intake.md` and `references/triage.md` |
| Urgency is unclear | `references/red-flags.md` |
| Photo capture or comparison | `references/photo-protocol.md` |
| Case separation and longitudinal review | `references/tracking.md` |
| Treatments, products, triggers, or adherence | `references/treatment-log.md` |
| Preparing questions or a visit summary | `references/consult-prep.md` or `references/consult-workflow.md` |
| Storage, sharing, minors, intimate-area images, or productization | `references/legal-boundaries.md` |
| Baseline dermatology and source-backed triage context | `references/domain.md` |

## Core Workflow

1. **Triage first.** Check for emergency, same-day, and prompt clinician-review signals before discussing tracking or possible patterns.
2. **Collect only decision-changing facts.** Capture body site, onset and trend, symptom burden, relevant exposures or treatments, and clinician-confirmed history.
3. **Separate concerns.** Keep one case folder per distinct lesion, rash episode, or stable body-site problem.
4. **Standardize evidence.** Before comparing photos, use the same camera, lighting, distance, angle, and body position where possible; state when comparisons are limited.
5. **Keep records factual.** Separate user reports, visible observations, and clinician statements. Record dates for meaningful changes, treatment changes, visits, and results.
6. **Prepare a clinician handoff.** Summarize onset, trend, treatments, exposures, comparable photos, and the user's highest-priority questions.

## Decision Outputs

- **Emergency or same-day signals:** give the in-person escalation recommendation first; defer intake, images, and persistent storage.
- **Prompt clinician review:** explain the observed reason, recommend an appointment timeframe, and offer a dated handoff summary.
- **No active red flags:** create a minimal tracking plan only after consent, then use case separation and standardized evidence.
- **Insufficient photo quality:** record the limitation and rely on the timeline and symptoms rather than a visual conclusion.

## Scope and Safety

This skill organizes skin concerns, photos, timelines, exposures, and visit preparation. It provides conservative escalation guidance and does not replace in-person clinical assessment, dermoscopy, biopsy, pathology, or clinician judgment.

For sensitive images, support care by directing minors or intimate-area concerns to an appropriate in-person or secure clinician workflow instead of collecting or storing images. Ask before writing local files, storing photo metadata, or generating an export. Keep data local unless the user explicitly requests an approved sharing workflow.

## Common Failure Modes

- Photos with different lighting, zoom, camera modes, or distance are weak comparison evidence; document the limitation rather than infer progression.
- Distinct lesions, rashes, scalp symptoms, or acne courses need separate cases so a clinician can reconstruct each timeline.
- Bleeding, rapid change, fever, eye or mouth involvement, severe pain, or fast spread needs urgency-based in-person evaluation rather than a watch-and-wait record.
- A photo or symptom description can organize uncertainty, but cannot confirm a diagnosis.
