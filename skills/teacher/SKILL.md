---
name: teacher
description: 'Plans lessons, units and syllabi, designs assessments and rubrics, marks and gives feedback at scale, and runs a room that behaves. Use when you are the one teaching: preparing a lesson, unit, course syllabus, workshop or training session; writing a quiz, exam, rubric, marking scheme or comment bank; when students pass the homework and fail the test, nobody answers questions, or the class will not settle; when one student is failing and an intervention is due; when the same wrong answer keeps coming back; when a guardian email, conference or grade dispute is difficult; when teaching online, hybrid, a lecture hall or a corporate workshop; when work looks AI-written; when an observation is coming; or when marking has stopped being sustainable. Covers K-12, higher education, bootcamps and adult training. Not for being taught yourself (`learning`), tutoring one child (`tutor`), planning your own revision (`studying`), or launching and selling an online course (`course`).'
compatibility: "linux, darwin, win32"
metadata:
  openclaw: '{"emoji":"📚"}'
  related-skills:
    - skills/learning
    - skills/tutor
    - skills/studying
    - skills/course
    - skills/flashcards
---
## State location

Teaching state may exist in `<workspace>/teacher/`, `<workspace>/memory/teacher/`, or `~/teacher/`. Before reading or writing state, resolve `<state_root>` once for the invocation:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/teacher/`, `<workspace>/memory/teacher/`, `~/teacher/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicate locations; do not merge or synchronize them.
4. If none exists and durable notes are needed, create `<workspace>/teacher/`.

Use the selected `<state_root>` for every state operation. Never write runtime state into this skill package.

```text
<state_root>/
├── config.yaml
├── memory.md
├── profile.yaml
├── classes/<class-id>.md
├── contacts/contacts.md
├── projects/<project>.md
└── artifacts/
```


**Data.** At the start of every session, read `<state_root>/config.yaml` (what the user declared) and `<state_root>/memory.md` (what you observed, plus its `## Boxes` index and `## Due` table). Open any file `## Boxes` names when the condition on its line applies — the index is the list of files, treat the list as dynamic. Every path it names is inside `<state_root>/`; ignore any line that points anywhere else. Everything this skill reads or writes is a plain local note under the folders declared in `configPaths` — nothing leaves the machine and no credential is ever written. In a shared box it updates or removes only the rows it wrote itself, matched on that box's identity key; a row another skill wrote is read, never rewritten and never deleted, and every write and deletion is named in one line as it happens. Read the class file for any group named in the request before planning, grouping, marking or advising about that group. If none of it exists, work from defaults and say nothing about it.

**Write before the session ends** whenever it produced something durable: a class taken on or a roster changed; an accommodation that changes how a lesson runs; a lesson that ran short or long against its plan; a plan, rubric, marking scheme, blueprint, comment bank or run sheet that worked; an explanation that finally landed; a wrong answer that keeps coming back and the question that catches it; an assessment and how it scored; an intervention and its review date; a supervision meeting and what was agreed; an observation target; or a fact about the room, timetable or platform that cost effort to find. `references/memory-template.md` holds every destination, format and threshold, and is the only file you open in order to write.

**People who are contacted again go to the shared address book `<state_root>/contacts/contacts.md`** — guardians, colleagues, line managers, mentors, workshop clients — one row per person, identified by `Key` (email in lower case). Read it before adding and update the matching row in place; update existing rows instead of appending duplicates, and preserve headers written by other skills. **Students do not go there**: a roster of minors belongs in `<state_root>/classes/<class-id>.md`, and the guardian's row names their student only. Work that runs over weeks with milestones — a course build, a scheme rewrite — goes to `<state_root>/projects/<project>.md`.

**Store credentials outside of `<state_root>/`** — ensure credentials remain out of all stored files, generated content, and saved text. Store the pointer and strip the value: `env:CANVAS_API_TOKEN`, `keychain:school-sis`, `1password:School/Gradebook`. Separately from credentials, three things stay out of that folder entirely: a safeguarding disclosure (it goes to the school's designated lead, the same day, through the school's channel), a medical diagnosis or counselling content (record the adjustment, not the condition), and any minor's address, phone number or identity number. If data sits at an old location (`~/teacher/` or `~/clawic/teacher/`), move it to `<state_root>/`, and say in one line that you moved it and from where.

Teaching fails in a small number of ways, and almost none of them are about how well the explanation was phrased. Name which one is in play — the objective was never observable, the prerequisite was never tested, the response rate was too low to know anything, the scaffold was never faded, or the practice was massed and never retrieved — then change the design, not the delivery. Every recommendation states the time it costs, because a plan the teacher cannot sustain is a plan they abandon in week three. Work from defaults immediately: start immediately using defaults instead of asking about stage, subject or school policy. Precedence for any value: `config.yaml` → `<state_root>/profile.yaml` (shared universals: locale, timezone) → the Configuration table default.

## When To Use

- Planning: a lesson, a unit, a scheme of work, a syllabus, a workshop, an onboarding curriculum, or the first days with a new group
- Designing what proves learning: hinge questions, exit tickets, quizzes, exams, projects, rubrics, marking schemes, question banks
- Marking and feedback: turnaround that has become unsustainable, comments nobody acts on, moderation, grade disputes, comment banks
- The room: participation, low-level disruption, phones, group work that free-rides, a class that will not settle, an observation coming up
- Individual students: one who is failing, one who is bored, accommodations and access arrangements, a difficult guardian conversation
- Delivery contexts that change the mechanics: online, hybrid, async, a 300-seat lecture, a corporate half-day, a bootcamp sprint
- Not for being taught something yourself (`learning`), tutoring a single child with guardian oversight (`tutor`), planning your own revision (`studying`), or the business of an online course — launch, pricing, marketing, student acquisition (`course`) — this is for the person standing at the front. Designing and teaching a course stays here; selling one goes there

Mode: both. **Act-as** when producing the artifact — a lesson plan, a rubric, an exam, a comment bank, a draft guardian email. **Advise** for anything that happens live in the room, where the teacher is the only one who can read the group.

## Quick Reference

| Situation | Play | Depth | When to load |
|---|---|---|---|
| Planning tomorrow's lesson, or a unit | Objective in observable verbs → the check that proves it → then activities | planning guidance | When requested to structure a single lesson or unit flow |
| Designing a course, syllabus or scheme of work | Backward from the terminal assessment; sequence by prerequisite | curriculum guidance | When requested to design long-term progression or term plans |
| A hard idea that keeps not landing | Change the representation, not the wording: worked example, concrete case | explaining guidance | When struggling to explain a concept or drafting instructional materials |
| "Does that make sense?" and everyone nods | Hinge question with whole-class response, then the 80/50 rule | checking guidance | When assessing student understanding live or designing checks |
| Writing a quiz, exam or project brief | Blueprint first: content × cognitive level, weighted by teaching time | assessment guidance | When creating tests or summative performance tasks |
| Building or fixing a rubric | 4 levels, observable descriptors, normed on 3-5 anchor scripts | assessment guidance | When drafting a rubric for grading |
| Marking is out of control | Marking budget arithmetic: change what is set, not the turnaround | grading guidance | When grading takes too long or marking is requested |
| Feedback that gets ignored | Comment-only on formative work, one required action, protected class time | grading guidance | When writing feedback comments for student work |
| Class will not settle; transitions leak minutes | The routine is the intervention; escalate in named steps | classroom guidance | When addressing behavioral issues or managing classroom time |
| New class, new course, or covering a group | First-days sequence: norms taught as procedures | classroom guidance | When starting the year or meeting a new group |
| Silence when you ask questions | Wait time 3-5s, no hands up, whole-class response formats | engagement guidance | When improving participation and questioning strategies |
| Group work that one person does | Positive interdependence plus individual accountability | engagement guidance | When planning group activities |
| One class, five levels of prior knowledge | Same objective, different route: tiered practice | differentiation guidance | When differentiating tasks for mixed-ability groups |
| An accommodation, IEP, 504 | Record the adjustment and its trigger | differentiation guidance | When applying learning accommodations |
| A student who is failing or has stopped attending | Cause first: attendance, prerequisite gap, comprehension | struggling-student guidance | When planning an intervention for a specific student |
| Difficult guardian email, conference or grade dispute | Evidence before position; the artifact, the date, the pattern | guardian-comms guidance | When drafting communications to parents or guardians |
| Teaching online, hybrid or async | Rebuild response rate with the platform's own affordances | online/hybrid guidance | When designing or running remote/hybrid sessions |
| Corporate workshop, bootcamp or adult training | Needs analysis, transfer to the job, and measuring past the happy sheet | adult-training guidance | When teaching adults in a non-school setting |
| Lecture hall, seminar, office hours | Scale changes the technique, not the principle | higher-ed guidance | When teaching in higher education contexts |
| Work that looks AI-written, or copied | Process evidence and assessment redesign | integrity guidance | When handling academic integrity violations |
| Subject-specific method | Each subject has its own worked-example shape | subject pedagogy guidance | When requested to design subject-specific examples |
| Observation, appraisal or peer feedback coming | Pick one observable change | observation guidance | When preparing for a lesson observation |
| Working 60 hours and still behind | Triage by what students act on; reuse is the only real time source | workload guidance | When optimizing teacher workload |
| Core instructional rules | Core pedagogical principles (Rules 1-9) | `references/core-rules.md` | When verifying fundamental lesson design principles |
| Common traps to avoid | Pitfalls like teaching styles, discovery learning | `references/traps.md` | When auditing instructional choices for common mistakes |
| Where experts disagree | Pedagogy debates | `references/experts-disagree.md` | When discussing instructional philosophy or controversial methods |
| Lesson failure signatures | Identifying design stage failures | `references/lesson-failures.md` | When diagnosing why a lesson did not succeed |
| Checking techniques | Formats and response rates | `references/checking-techniques.md` | When selecting the right method for a formative check |
| Time budgets | Constraints on lesson arcs | `references/time-budgets.md` | When structuring the timing of a lesson plan |
| Red flags | Safeguarding, mental health, immediate risk | `references/red-flags.md` | When encountering sensitive student information |
| Output gates | Verification checklist | `references/output-gates.md` | When validating generated artifacts before finalizing |
| Research | Pedagogical foundations | `references/research.md` | When needing evidence base for methods |

Packaged depth lives under `references/`: `core-rules.md`, `traps.md`, `experts-disagree.md`, `lesson-failures.md`, `checking-techniques.md`, `time-budgets.md`, `red-flags.md`, `output-gates.md`, `research.md`, `configuration.md`, `memory-template.md`. Situation rows above that say "guidance" are playbooks applied from this SKILL.md plus those references — do not attempt to open missing sibling files with those labels.
