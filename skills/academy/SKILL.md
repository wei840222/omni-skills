---
name: academy
description: Operate academy admissions, capacity, staffing, billing, retention, and student-success systems end to end. Use when the user runs a training center, cohort bootcamp, tutoring business, membership academy, multi-site learning program, or asks about enrollments, class schedules, teacher load, collections, churn, or weekly academy KPIs.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🏫"}'
  related-skills: '{"booking":"Handles availability logic, scheduling tradeoffs, and reservation-style class workflows.","course":"Creates and operates structured programs and learning products the academy delivers.","crm":"Manages leads, contacts, follow-up history, and admissions pipeline discipline.","school":"Extends into family-facing education workflows when the academy serves school-age learners.","teacher":"Supports class delivery, instruction quality, and teaching behavior inside academy programs."}'
---

## State location

Academy state may exist in `<workspace>/academy/`, `<workspace>/memory/academy/`, or `~/academy/`. `<workspace>` means the workspace root provided by the host/runtime, not the shell's current working directory.

Before any state read, query, create, update, or delete, resolve `<state_root>` once:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/academy/`, `<workspace>/memory/academy/`, `~/academy/`.
3. If none exists and state must be created, default to `<workspace>/academy/`.

If multiple candidate directories exist, use only the first one, tell the user that multiple state directories were found, and leave the others untouched. Use the selected `<state_root>` for every state operation during the run. Create only the resolved filesystem path; the placeholder name `<state_root>` is documentation-only.

Legacy path `~/Clawic/data/academy/` is a migration source only. It is outside active lookup. Copy, validate, cut over, and keep a rollback path only after the user chooses migration.

## Setup

After resolving `<state_root>`, if `<state_root>/memory.md` is missing or empty, read `references/setup.md` and follow it. Confirm with the user before the first write to `<state_root>`.

## Primary workflow

Execute in order. Each step has a done-when check.

### Step 1: Resolve state and context

1. Resolve `<state_root>` with the State location procedure.
2. Load `<state_root>/memory.md` when it exists; otherwise follow Setup.
3. Identify the operator role: founder, academy manager, admissions, academic lead, or finance.

Done when: `<state_root>` is fixed for this run and the operator role is known.

### Step 2: Identify the academy model

1. Read `references/operating-models.md`.
2. Classify the business as cohort, membership, lesson-based, or multi-site/online using revenue collection, delivery format, and the binding capacity limit.
3. Record or update the model in `<state_root>/memory.md`.

Done when: one primary model is selected and later advice matches that model.

### Step 3: Diagnose the live bottleneck

Rank the current pressure point:

1. lead quality or volume
2. conversion / admissions
3. schedule or room capacity
4. teacher load or coverage
5. attendance or delivery quality
6. collections or refunds
7. renewal / churn

Load only the reference that matches the top bottleneck. Solve that constraint before expanding into a full operating blueprint.

Done when: one primary bottleneck owns the next actions.

### Step 4: Run the connected student journey

Treat admissions → onboarding → attendance → progress → billing → renewal as one system.

| Need | Load |
|------|------|
| Funnel, offers, enrollment guardrails | `references/admissions.md` |
| Timetable and seat economics | `references/schedule-capacity.md` |
| At-risk students and interventions | `references/student-ops.md` |
| Program design and delivery quality | `references/curriculum-delivery.md` |
| Roles, load, substitutes, QA | `references/staffing.md` |
| Pricing, collections, retention math | `references/finance-retention.md` |
| Weekly/monthly KPI rhythm | `references/dashboard.md` |

🔴 **Capacity decision gate:** Before recommending a new cohort, promo, or discount, confirm seat capacity, teacher availability, calendar fit, and delivery margin together. If any input is missing, request it and keep the recommendation conditional.

🔴 **Growth spend gate:** Before increasing paid acquisition, rank the live bottleneck. If collections, coverage, or renewal is the top constraint, repair that path first and state the unlock condition for ads.

Done when: the proposed action names the upstream and downstream effects on capacity, cash, and student success.

### Step 5: Write operating artifacts

Create optional companion files only when the feature is in use. Templates live in `assets/academy-data-templates.md`; lifecycle rules live in `references/memory.md`.

```text
<state_root>/
├── memory.md       # required once persistence is enabled
├── admissions.md   # optional funnel rules
├── cohorts.md      # optional calendars and capacity
├── students.md     # optional risk and intervention notes
├── staff.md        # optional load and coverage
├── finance.md      # optional pricing and collections
├── dashboard.md    # optional weekly KPI summary
└── archive/        # optional closed terms
```

Store patterns, constraints, and decisions. Keep full student dossiers, card data, passwords, and health records out of skill memory.

Done when: new or updated files sit under the resolved `<state_root>` and `memory.md` `last` date is current.

### Step 6: Close with a decision-ready cadence

Use `references/dashboard.md` to leave the operator with:

- next-7-days schedule check
- at-risk student list
- staffing gap list
- collections follow-up queue
- one owner and due window per action

Done when: each action has an owner, a trigger, and a review window.

## Architecture

State lives under the resolved `<state_root>`. Skill resources stay in `references/` and `assets/` and are separate from runtime state.

## Quick reference

| Topic | File | When to load |
|-------|------|--------------|
| First-use setup | `references/setup.md` | `<state_root>/memory.md` missing or empty |
| Memory lifecycle | `references/memory.md` | Creating or updating persistent status |
| Copyable templates | `assets/academy-data-templates.md` | Creating state files |
| Model selection | `references/operating-models.md` | Classifying the academy |
| Admissions funnel | `references/admissions.md` | Leads, trials, offers, enrollment |
| Schedule and capacity | `references/schedule-capacity.md` | Timetables, rooms, seat math |
| Student lifecycle | `references/student-ops.md` | Onboarding, risk, renewal |
| Curriculum delivery | `references/curriculum-delivery.md` | Program design and classroom quality |
| Staffing and QA | `references/staffing.md` | Hiring, load, substitutes |
| Finance and retention | `references/finance-retention.md` | Pricing, cash, LTV |
| KPI rhythm | `references/dashboard.md` | Weekly or monthly operating review |

## Core rules

### 1. Model first

Match systems to the revenue and delivery model before copying playbooks from another academy type.

### 2. Connected journey

Optimize lead generation only together with fulfillment capacity, payment friction, and student success.

### 3. Capacity lock

A class is sellable only when room, teacher, timetable, and minimum viable demand all align.

### 4. Cash with attendance

Keep payment terms, deposits, failed-payment workflow, overdue escalation, and refund boundaries visible whenever pricing or plans change.

### 5. Early intervention

Treat absence, low practice completion, delayed payment, confusion, and teacher mismatch as save opportunities while trust remains.

### 6. Simple cadences

Prefer short recurring artifacts over chat-only memory: weekly KPI review, next-7-days schedule check, at-risk list, staffing gaps, collections queue.

### 7. Role-fit output

Adjust detail, time horizon, ownership, and commercial vs pedagogical focus to the operator.

## Gotchas

- **Speed-to-contact before ad spend:** slow inquiry response burns paid leads; measure first useful human contact, not auto-replies.
- **Stage-defined conversion only:** lead-to-enroll and applicant-to-enroll are different denominators; mix them and the funnel looks fake-healthy or fake-broken.
- **Utilization bands:** staff utilization near **70–82%** is often healthier than chronic **85%+** overload or launch-level **55–65%** idle time.
- **Delivered vs scheduled:** collections, payroll, and break-even must use delivered sessions; scheduled slots overstate revenue.
- **Re-enrollment window:** start renewal communication **60–90 days** before the earliest due date with progress evidence attached.
- **Capacity lock before promo:** seats, teacher, room, and minimum viable size must all be named before opening enrollment.
- **Learning + payment risk:** combined signals need one coordinated plan the same week they appear.

## Academy traps

- Selling cohorts before teacher and room capacity are locked turns enrollments into chaos.
- Letting every teacher invent attendance and follow-up formats makes data unusable within two weeks.
- Treating unpaid invoices as finance-only issues converts collections friction into churn and morale damage.
- Measuring only revenue and enrollments hides delivery failure until refunds or dropouts appear.
- Unlimited custom exceptions erase repeatability and margin.
- Launching programs that skip a renewal path raises acquisition cost while lifetime value stays weak.
- Solving attendance with reminders alone misses schedule fit, perceived progress, or teacher mismatch.

## Counter-examples

| Anti-pattern | Do this instead |
|---|---|
| Answer “how do we grow?” with ad channel ideas first | Rank the live bottleneck; unlock ads only after capacity, cash, and renewal gates pass |
| Open a new class because a few families asked for a custom time | Fill existing viable seats or require teacher + room + min size + margin together |
| Track enrollments alone and skip attendance, delinquency, or utilization | Use the weekly core view in `references/dashboard.md` |
| Run academic save and billing chase as separate silent threads | One coordinated plan when learning risk and payment risk co-occur |
| Store full student dossiers or card details in skill memory | Store patterns, constraints, owners, and next actions under `<state_root>` |
| Copy a bootcamp launch playbook onto a membership academy | Re-classify model via revenue, delivery, and binding capacity limit first |

## Security and privacy

- Default network behavior: no outbound calls. This skill is a local operating playbook and memory system.
- Local state: academy model, programs, staffing notes, student-risk observations, and KPI summaries under `<state_root>`.
- Scope limits: payment processors, email, calendars, and CRMs stay manual unless the user explicitly authorizes a specific action.
- Memory hygiene: write patterns, constraints, owners, and next actions; card details, passwords, and private student records stay outside skill memory.
- Package integrity: leave skill package files unchanged during normal operation.

## Failure modes

### State root unresolved

If the host cannot supply `<workspace>` and no candidate directory exists, ask the user or host for an explicit state path before creating data.

### Multiple state copies

If more than one candidate exists, keep using the highest-precedence directory, report the conflict, and leave lower-precedence copies unchanged.

### Write failure

If a write fails, report the path and error, clean up partial files when safe, and pause further state changes until the user resolves the issue.

### Missing companion file

If the task needs admissions, cohorts, students, staff, finance, or dashboard state that does not exist, create it from `assets/academy-data-templates.md` only after the feature is actually needed.

### Capacity conflict

If a growth request needs seats that teacher, room, or timetable cannot support, name the blocking constraint and offer a sequenced plan: free capacity, retime, restaff, or delay the promo.

### Collections and learning risk together

If a student shows both learning risk and payment risk, treat the account as top priority and coordinate academic and billing follow-up in one plan.
