---
name: period
description: Track menstrual cycles, log symptoms, predict periods and ovulation, and manage fertility signals using local state. Trigger when the user wants to log a period, report cycle symptoms, ask about cycle regularity, or configure fertility tracking.
metadata:
  version: "1.0.3"
  openclaw: '{"emoji":"🩸"}'
  related-skills: '{"doctor":"Turns flagged signals into a structured question list for an appointment.","health":"Longitudinal wellness habits beyond the cycle.","pregnancy":"Tracking shifts to prenatal once a pregnancy is confirmed.","symptoms":"General symptom tracking and doctor-visit prep outside the cycle."}'
---
## State location

Period Tracker state may exist in `<workspace>/period/`, `<workspace>/memory/period/`, or `~/period/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/period/`, `<workspace>/memory/period/`, `~/period/`.
3. If none exists and state must be created, default to `<workspace>/period/`.

Use the selected `<state_root>` for every state operation in this skill.

All data lives locally in `<state_root>/` (`assets/log-template.md` for file formats, `references/setup.md` on first use). Keep all data local. Mention cycle content only within a session she explicitly opened. This skill acts directly (logs, predicts, flags); it advises, it does not diagnose.

## Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| fertility_tracking | off \| conceive \| avoid | off | Gates Fertility Signals and `references/fertility.md`; `conceive` centers timing on the window, `avoid` adds buffer days and effectiveness caveats |
| contraception | text (method) or none | none | Hormonal methods reroute prediction to `references/contraception.md`; the ovulation back-count (rule 4) is suspended on suppressive methods |
| prediction_window | number (3-6 cycles) | 6 | How many recent cycles feed the median (rule 2); reset to 3 after a life change (postpartum, stopping the pill) invalidates the old baseline |
| temperature_unit | celsius \| fahrenheit | celsius | Converts BBT thresholds in `references/fertility.md` (0.3-0.5 C = 0.5-0.9 F) |
| heads_up_days | number (0-7) | 0 | 0 = predictions only when asked; N = if she opens a session within N days of a predicted start, mention it once |

Preference areas to record as she reveals them:

- **wording** — plain vs clinical vocabulary and how she refers to her own body; affects every reply, never the stored data
- **flow scale** — whether she counts pads/tampons, describes light/medium/heavy, or uses mL; mirror her unit
- **proactivity** — does she want pattern observations ("this is the third month you had a headache on day 2") or just a silent log?
- **off-limits** — topics she never wants raised, such as fertility or weight

## Execution and Guidelines

1. Resolve `<state_root>` before any state access, then read `references/setup.md` on first use or when loading existing state.
2. Read `references/core-rules.md` for every prediction, classification, fertility estimate, or contraception-aware cycle calculation. Read `references/output-gates.md` before replying to any cycle question; it contains the red-flag escalation rules.
3. Route the request directly: `references/symptoms.md` for symptoms; `references/pain.md` for cramps or pelvic pain; `references/pms-pmdd.md` for cyclical mood symptoms; `references/irregular.md` for late, missed, shifting, adolescent, postpartum, or perimenopausal cycles; `references/contraception.md` for method-related bleeding; and `references/fertility.md` only after an explicit fertility request or enabled fertility tracking.
4. Read `references/privacy.md` for storage, export, deletion, sharing, or legacy-data migration requests. Use `assets/log-template.md` only when creating or interpreting the local log format.
5. Read `references/traps.md` before giving a prediction or explanation that could rely on textbook assumptions. Read `references/research_domain_facts.md` when applying clinical definitions or explaining their evidence base.
