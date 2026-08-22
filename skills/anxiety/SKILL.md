---
name: anxiety
description: Record anxiety episodes, build trigger maps, and plan coping strategies. Trigger when the user wants to log anxiety symptoms, conduct thought records, or create exposure ladders. Route diagnosis requests to appropriate medical care rather than treating this as a diagnostic skill.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"A"}'
  related-skills: '{"therapist":"supportive therapeutic conversation framing","psychologist":"structured behavior and cognition guidance","mindfulness":"grounding and attention training practices","journal":"reflective writing and pattern capture","sleep":"sleep stability support for anxiety management"}'
---

## Setup

On first use, read `references/setup.md` for integration guidance and local memory initialization.

## When to Use

User wants to track anxiety symptoms, panic episodes, worry spirals, avoidance patterns, or coping outcomes.
Agent keeps logs clinically useful for therapy, supports anxiety reduction with structured plans, and escalates safety-sensitive situations immediately.

## State location

Resolve `<state_root>` before reading, creating, updating, or deleting anxiety records:

1. Use an explicitly configured state path when the user or host provides one.
2. Otherwise use the first existing directory in this order: `<workspace>/anxiety/`, `<workspace>/memory/anxiety/`, then `~/anxiety/`.
3. If none exists and the user confirms they want persistent tracking, create `<workspace>/anxiety/` and use it as `<state_root>` for this invocation.
4. If more than one candidate exists, use only the highest-precedence directory and tell the user that separate copies exist; do not merge or synchronize them automatically.

Use the selected `<state_root>` for every anxiety record. See `references/memory-template.md` for the record structure and starter templates.

```text
<state_root>/
├── memory.md                 # Status, mode, baseline, and active priorities
├── logs/events.md            # Episode-level anxiety event logs
├── logs/thought-records.md   # CBT-style thought records for reframing
├── plans/current.md          # Active coping and exposure plan
├── triggers.md               # Trigger map and safety behavior patterns
├── exposures.md              # Exposure ladder and session outcomes
└── reviews/weekly.md         # Weekly trend review and plan decisions
```

## Quick Reference

| Topic | File | When to load |
|-------|------|--------------|
| Domain Knowledge | `references/domain-knowledge.md` | When seeking clinical guidelines on anxiety, CBT, or exposure therapy |
| Setup and activation behavior | `references/setup.md` | When initializing the skill for the first time |
| Memory structure and templates | `references/memory-template.md` | When setting up or modifying memory structure |
| Goal modes and switching logic | `references/tracking-modes.md` | When determining tracking approach (track, reduce, recover) |
| Anxiety event logging format | `references/event-log-template.md` | When capturing a new anxiety event |
| Thought record workflow | `references/thought-record.md` | When user wants reframing or pattern analysis |
| Coping responses by intensity | `references/regulation-playbook.md` | When selecting responses by anxiety intensity |
| Graded exposure planning | `references/exposure-ladder.md` | When building an exposure ladder |
| Weekly review and decision rules | `references/weekly-review.md` | When performing a weekly trend review |
| Red and amber triage rules | `references/triage-rules.md` | When observing severe symptoms or red flags |

## Data Storage

Local notes stay in `<state_root>`.
Before creating or changing local files, present the planned write and ask for user confirmation.

## Core Rules

### 1. Set the Active Goal Mode Before Intervention
Start with mode selection from `references/tracking-modes.md`:
- `track` for observation without behavior change pressure
- `reduce` for gradual anxiety intensity and frequency reduction
- `recover` for post-episode stabilization and relapse prevention
Only initiate reduction or exposure planning if the user explicitly requests it; otherwise, default to observation mode.

### 2. Capture Episodes With Therapy-Relevant Fields
Use `references/event-log-template.md` for each meaningful event.
At minimum capture time, context, trigger, body symptoms, anxiety intensity, behavior, and short outcome.
Ensure all entries capture specific, reviewable details before saving.

### 3. Separate Event Logging From Cognitive Work
Use `<state_root>/logs/events.md` for what happened and `<state_root>/logs/thought-records.md` for interpretation.
Apply `references/thought-record.md` only when the user wants reframing or pattern analysis.
Keep raw observations in `<state_root>/logs/events.md` and cognitive conclusions in `<state_root>/logs/thought-records.md` separately.

### 4. Track Avoidance and Safety Behaviors Explicitly
Log what the user avoided and what they did to feel temporarily safe.
Use these patterns to guide exposure planning from `references/exposure-ladder.md`.
If avoidance is shrinking life function, name it clearly and propose one small reversal step.

### 5. Match Regulation Strategy to Intensity Zone
Use `references/regulation-playbook.md` to select responses by intensity:
- low: prevent escalation and maintain function
- medium: down-regulate physiology and narrow focus
- high: safety-first grounding and immediate support routing
Always select a specific intensity zone before recommending coping strategies.

### 6. Use Graded Exposures Only With Consent and Structure
When the user wants long-term anxiety reduction, build a ladder using `references/exposure-ladder.md`.
Use small, repeatable steps with before/after ratings and recovery windows.
Always start with low-intensity, repeatable tasks when building an exposure ladder.

### 7. Escalate Risk Signals Immediately
Use `references/triage-rules.md` whenever severe symptoms, self-harm thoughts, substance crisis, or medical red flags appear.
For emergency patterns, provide urgent care guidance first and pause routine coaching.
This skill supports tracking and behavior change planning, not diagnosis or emergency treatment.

## Common Traps

- Logging only "felt anxious" without context -> no actionable pattern detection.
- Tracking too many fields on day one -> user fatigue and dropout.
- Treating all anxiety episodes as the same -> wrong interventions for the trigger type.
- Skipping avoidance tracking -> exposure plan misses the real maintaining loop.
- Using thought reframing in acute panic peak -> low effectiveness and frustration.
- Proposing large exposure jumps -> backlash, avoidance rebound, and trust loss.
- Giving clinical diagnosis language -> safety and scope violation.

## External Endpoints

This skill makes NO external network requests.

| Endpoint | Data Sent | Purpose |
|----------|-----------|---------|
| None | None | N/A |

No other data is sent externally.

## Security & Privacy

**Data that leaves your machine:**
- Nothing by default. This skill is instruction-only and local unless the user explicitly requests export.

**Data stored locally:**
- anxiety logs, thought records, trigger patterns, exposure outcomes, and weekly reviews approved by the user.
- stored in `<state_root>`.

**This skill does NOT:**
- diagnose psychiatric or medical conditions.
- make undeclared network calls.
- write local memory without explicit user confirmation.
- force exposure tasks without user consent.
- modify its own core instructions or auxiliary files.

## Trust

This is an instruction-only anxiety tracking and coping support skill.
No credentials are required and no third-party service access is needed.
