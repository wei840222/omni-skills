# Configuration

User-dependent variables. Defaults apply until the user states a preference; store them in `<state_root>/config.yaml`.

| Variable | Type | Default | Effect |
|---|---|---|---|
| stage | elementary \| middle \| high \| higher-ed \| bootcamp \| corporate \| adult-ed | high | Selects the register, the behaviour model, the homework and attention budgets, and which of `higher-ed.md` or `training.md` leads |
| subjects | list | none | Which section of `subjects.md` is applied without being asked, and the domain every example is drawn from |
| class_size | number (1-500) | 28 | Drives the response-rate choice in Checking Techniques, group counts, and the marking arithmetic in Rule 8 |
| session_length_min | number (min, 20-240) | 50 | The lesson arc in Time Budgets and every generated plan scales to this |
| grade_scale | percent \| letter \| 1-9 \| 0-20 \| pass-fail \| ungraded | percent | How every rubric level, mark scheme and reported score is expressed |
| standards | text (framework or specification id) | none | What `curriculum.md` aligns and audits coverage against; unset means objectives are written from first principles |
| lms | google-classroom \| canvas \| moodle \| teams \| blackboard \| schoology \| none | none | Where materials, submissions and announcements are assumed to live in `online.md` and `grading.md` |
| teaching_mode | in-person \| hybrid \| online-live \| async | in-person | Which checking formats are offered and whether `online.md` guidance is applied by default |
| ai_policy | open \| limited \| banned \| unset | unset | The posture in `integrity.md`, what the assignment brief says about AI, and how much evidence moves in-class |
| grading_turnaround_days | number (days, 1-21) | 7 | The `## Due` row started when work is collected, and the triage threshold in `grading.md` |
| plan_format | brief \| detailed \| school-template | brief | Shape of every generated lesson plan: a half-page arc, a full plan with rationale, or the school's own form |
| plan_template | path | none | The school's required plan or rubric form at `<state_root>/<file>`; overrides `plan_format` layout |
| student_naming | first-initial \| first-name \| code | first-initial | How students are identified in `classes/<class-id>.md` and in anything generated — `Maya R.`, `Maya`, or `S14` |

Preference areas — customizable dimensions; a stated preference gets recorded in `config.yaml` and applied from then on:

- **Tooling** — slides, whiteboard, quizzing and polling tools, question banks, comparative-judgement platform, devices per student, printing limits — affects which checking and practice formats are offered at all
- **Conventions** — objective stem wording, rubric level count and labels, marking symbols and codes, file and unit naming, where success criteria appear on a task — affects every generated artifact
- **Platform** — school system and country, term structure and exam calendar, room and furniture constraints, timetable shape (block vs period), department scheme already in force — affects sequencing and what can be rearranged
- **Behaviour posture** — the school's escalation ladder and who owns each step, phone policy, homework policy, seating philosophy, when to involve pastoral staff — affects `classroom.md` and the point at which advice hands off to policy
- **Assessment posture** — grades versus ungrading, resubmission and retake rules, late-work policy, weighting of coursework, whether formative work is ever recorded — affects `assessment.md` and `grading.md`
- **Output register** — how much of a plan to produce versus discuss, student-facing wording versus teacher notes, reading age of generated materials, language of student-facing text — affects the shape of every deliverable
- **Cadence** — reporting cycle, guardian contact frequency, coverage audits, seating and group rotation, rubric norming before big marking batches — every accepted cadence becomes a row in the `## Due` table of `memory.md`
- **Constraints and exclusions** — mandated curriculum or specification, techniques the school forbids, accessibility requirements that apply to every material, subjects or content that must not be used as examples — affects everything generated
