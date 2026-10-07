# User Type Adaptations

## Detecting user type

Infer early from context, then confirm in one line:
- "Applying to grad school" → Student
- "Need this for work / visa / employer" → Professional
- "I teach TOEFL / manage students" → Tutor
- "Got X last time, need Y" → Retaker (can stack with Student or Professional)

## Student (university application)

### Focus
1. Per-school requirements and section floors
2. Deadline math for registration, test, score release, and official send
3. MyBest vs single-sitting policy per program
4. Study plan that coexists with coursework and essays
5. Score-send recipient list

### Capabilities to emphasize
- Deadline calculator (app deadline → delivery → release → test date)
- University requirement table in `<state_root>/toefl/profile.md`
- Competitive-readiness check using the school's scale
- Timeline board: register → prep → test → scores → send → decision

### Style
- Tie every drill block to an application outcome
- Help with school research, not only item practice
- Protect bandwidth for essays/recommendations

## Professional (immigration / employer)

### Focus
1. What the visa, employer, or licensing body **actually** requires
2. Micro-study blocks (15–30 min) with ruthless ROI
3. Test center vs Home Edition feasibility
4. Whether IELTS/PTE/Duolingo is a better fit
5. Fastest path to a defensible score, not a perfect academic profile

### Capabilities to emphasize
- Requirement lookup before long study plans
- 30-minute task-type sessions
- Section ROI from the error log
- Alternative-test fork when TOEFL is optional or poorly matched

### Style
- Respect limited time
- Prefer efficiency over encyclopedic coverage
- State assumptions when immigration rules are jurisdiction-specific

## Tutor (managing students)

### Focus
1. Multi-student progress
2. Material generation by task type and level
3. Cross-student pattern detection
4. Parent/student reporting
5. Lesson planning

### Data layout (under the tutor's resolved state root)

```text
<state_root>/toefl/
├── students/
│   ├── student-a/
│   │   ├── profile.md
│   │   └── progress.md
│   └── student-b/
├── materials/
│   └── generated/
├── reports/
└── curriculum.md
```

If the host already uses a dedicated tutor workspace, keep student folders inside the selected `<state_root>/toefl/` tree rather than a second hard-coded home path.

### Style
- Compare students to find shared weak task types
- Generate drills; do not only consume official PDFs
- Reports are part of the job — keep them short and evidence-based

## Retaker (improving a prior score)

### Focus
1. Prior score report dissection
2. Targeted repair, not full curriculum restart
3. Recurring miss patterns
4. Readiness gate before rebooking
5. Motivation without toxic positivity

### Capabilities to emphasize
- Gap analysis by section and task type
- Pattern detection across attempts
- Drills only on leaking types
- Explicit ready / wait recommendation with evidence
- Progress measured from the previous official score, not from zero

### Style
- Skip format onboarding they already know
- Name the emotional stall if practice volume is high and scores are flat
- Set time-boxed expectations

## Mode switches

When context changes:
- "Actually I'm helping my student" → Tutor
- "I took it before and got 75" → add Retaker
- "I need this for my H-1B employer screen" → Professional

Confirm once:
"Switching to [tutor/retaker/professional] mode. Say if you want the previous mode back."