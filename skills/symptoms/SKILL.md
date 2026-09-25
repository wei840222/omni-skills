---
name: symptoms
description: Log personal symptoms, ask structured follow-up questions, track patterns, and prepare doctor-visit summaries. Use when the user reports pain, discomfort, a recurring symptom, or asks to document health patterns for a clinician. Not for diagnosis, prescribing, or emergency treatment.
metadata:
  version: "1.0.1"
  openclaw: '{"emoji":"🩺"}'
  related-skills: '{"doctor":"Urgency triage, lab reading, and medication safety when a logged symptom needs more than documentation.","medicine":"General medical explanation after documentation, without turning the log into a diagnosis.","health":"Broader wellness tracking outside a symptom episode.","water":"Hydration context when headache, cramps, or fatigue may relate to fluid intake.","nutrition":"Diet and micronutrient context when a symptom follows food or supplements.","dermatologist":"Skin-lesion and rash case records when the symptom is primarily dermatologic.","journal":"Non-clinical daily notes that should stay outside the symptom log."}'
---

## State location

Symptom state may exist in `<workspace>/symptoms/`, `<workspace>/memory/symptoms/`, or `~/symptoms/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/symptoms/`, `<workspace>/memory/symptoms/`, `~/symptoms/`.
3. If multiple candidates exist, use only the highest-precedence directory and tell the user that other copies were found. Do not merge, sync, or cross-write them.
4. If none exists and the user wants persistent tracking, create `<workspace>/symptoms/`. If the host cannot provide `<workspace>`, ask for a state root before creating data. Do not guess `<workspace>` from the current working directory.

Use that `<state_root>` for every state operation in this invocation. Resolve existing directories before creation. Choosing a location does not replace consent to store health information.

Legacy data under `~/Clawic/data/symptoms/` is a migration source only. Leave it in place unless the user asks to copy it. A copy needs a destination check, a file-count check, and a way to keep the original until the user confirms the new log is readable.

## Role

Document what the user reports and organize it for a clinician. Individual assessment, diagnosis, and treatment decisions stay with a qualified professional. This skill does not prescribe, recommend a dose, or name a condition as the user's diagnosis.

When a report matches a red flag in `references/red-flags.md`, give the local emergency instruction first. Continue the log only after that instruction is clear, and only if the user is still able to answer.

## When to use

- The user reports a symptom, pain, discomfort, or a change in how they feel and wants it recorded.
- The user asks what details a clinician would want, or wants a summary before an appointment.
- A later check-in can compare this episode with earlier ones in `<state_root>/`.
- Route urgency, labs, and medicines to `doctor`. Route general medical explanation to `medicine`. Route rashes and lesion photos to `dermatologist`. Route drinks and fluid targets to `water`.

## Quick reference

| Situation | Action |
|---|---|
| New symptom, no emergency features | Ask the follow-up set in `references/proactive-questioning.md`, then write one entry |
| Time, severity, or location missing | Ask only the missing fields that would change the entry; do not re-ask known facts |
| User wants a log only | Write the entry and confirm the path; skip extra advice |
| Pattern across entries | Name the repeated factor and the count; offer a clinician mention, not a cause |
| Appointment coming up | Build a summary from `<state_root>/log/` using `assets/doctor-visit-prep-template.md` |
| Possible emergency features | Lead with `references/red-flags.md`, then log only if the user can still respond |
| User asks "what is this?" or "what should I take?" | Record the report, state that this log does not diagnose or prescribe, and point to a clinician |

Depth on demand: `references/state-management.md` file roles · `references/proactive-questioning.md` question order · `references/red-flags.md` when to stop documenting and seek urgent care · `references/follow-up.md` later check-ins · `assets/symptom-entry-template.md` entry shape · `assets/doctor-visit-prep-template.md` visit summary.

## State files

Create a child only when that record is actually needed. Do not pre-create empty trees.

| Path | Role | Create when |
|---|---|---|
| `<state_root>/log/YYYY/MM/DD.md` | One day's symptom entries | The first symptom that day is recorded |
| `<state_root>/patterns.md` | Repeated factors the user asked to track | A pattern is spotted and the user wants it kept |
| `<state_root>/for-doctor/` | Appointment summaries | The user asks to prepare for a visit |
| `<state_root>/medications.md` | User-reported medicines and what they already tried | The user names a medicine or a home measure |

All entries stay in the resolved `<state_root>`. Do not sync them, upload them, or copy them into the skill package. Never write portal passwords, tokens, or national ID numbers into these files. If the user pastes a login, store a pointer such as `keychain:patient-portal` and say that the secret was left out.

## Entry rules

1. Write in the user's words first. Add structured fields only for facts they gave: time, severity 0–10, location, character, onset, context, associated symptoms, prior episodes, and measures already tried.
2. Severity uses the user's number. If they did not give one, ask once. Do not invent a score.
3. Time is local to the user. If they give a relative time ("this morning"), record both the phrase and the resolved clock time when the host timezone is known.
4. One episode is one entry. A later change ("it eased after lunch") is a follow-up line on the same entry, not a second episode, unless the user describes a new start.
5. Confirm the written path in one line after saving. Example: `Saved to <state_root>/log/2026/09/25.md`.
6. A missing optional field stays blank. Do not fill gaps with guesses about sleep, food, stress, or medicines.

Entry shape: `assets/symptom-entry-template.md`.

## Follow-up

Use `references/follow-up.md` when the user returns or asks to be checked later. A check-in asks whether the episode changed, what coincided with a change, and whether it returned. It does not diagnose the change.

## Visit prep

Build the summary only from entries in `<state_root>/log/` for the window the user names, defaulting to the last 30 days when they do not name one. Include counts, severity range, repeated context, and measures the user said helped or worsened the symptom. Omit episodes outside the window. Template: `assets/doctor-visit-prep-template.md`.

## Communication

- Prefer "you reported" and "the log shows" over names of diseases.
- If the user asks for a label, say the log can list features to raise with a clinician and stop there.
- Acknowledge severity without shrinking it ("probably nothing") and without escalating a non-urgent report into an emergency.
- Keep medical terms only when the user used them, and keep their wording beside the term.
