# Degree Management

Paths below use the resolved `<state_root>` from `SKILL.md`.

## Setting Up a New Degree

### Autodidact Mode (Full Replacement)
1. **Explore interests** — Ask diagnostic questions, analyze responses, suggest 3-5 fitting careers
2. **Compare options** — Generate table: job market signals, time required, difficulty, ROI proxies, trends (cite live sources; no invented salaries)
3. **Reality check** — Describe "day in the life" for chosen career
4. **Generate curriculum** — Full program equivalent to a multi-year degree:
   - Modules with dependencies mapped
   - Resources curated per topic (books, courses, papers)
   - Practical components (projects, cases, labs)
   - Official certifications to pursue
5. **Create timeline** — Based on available hours/week at ≤80% capacity
6. **Store** — Create `<state_root>/degrees/[name]/` with `curriculum.md`, `progress.md`, `calendar.md`

### Student Mode (University Support)
1. **Import course list** — Extract from syllabus/schedule
2. **Add exam dates** — From PDFs or manual entry
3. **Link resources** — Connect uploaded materials to courses
4. **Generate study plans** — Per exam, with spaced review
5. **Track across semesters** — Unified view of all courses under distinct folders

### Career Change Mode
1. **Assess current skills** — What transfers to target field?
2. **Gap analysis** — What's missing for employability?
3. **Prioritize by ROI** — Skills that unlock jobs fastest
4. **Portfolio projects** — Generate ideas that demonstrate skills
5. **Certification roadmap** — Which exams validate progress?
6. **Timeline with milestones** — Explicit 30/90/180-day checkpoints

### Exam Prep Mode (Certifications/Competitive)
1. **Import official syllabus** — Structure by topics and weights from the live board page
2. **Analyze past exams** — Topic frequency and format (when lawfully available)
3. **Create study plan** — Weighted by topic importance
4. **Generate unlimited practice** — Tests, cases, oral simulations
5. **Track mastery** — Per topic, with readiness bands (not guaranteed scores)
6. **Monitor changes** — Re-check official sources if the syllabus may have updated

### Tutor Mode (Helping Others)
1. **Learner profile** — Age/level band, goals, constraints, guardian expectations if relevant
2. **Shared plan** — Curriculum + calendar the tutor and learner both can follow
3. **Session logs** — What was taught, what was verified, what is next
4. **Progress reports** — Mastery and time invested without shaming language
5. **Handoff** — When multi-learner parent dashboards dominate, route to `tutor`

## Folder contract per program

```text
<state_root>/degrees/[program-name]/
├── curriculum.md
├── progress.md
├── calendar.md
└── modules/
```

Update `degrees/index.md` whenever a program is added, paused, completed, or abandoned.
