# Sources — University (Gate 6)

Verified primaries for learning-science methods and academic-program design claims. Prefer full URLs in PR notes and user-facing citations. Program-specific weights, fees, and exam rules always come from the learner's live syllabus or exam board—not from this file.

## Retrieval, testing, and feedback

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| Testing effect | Roediger & Karpicke (2006) — Test-Enhanced Learning | https://doi.org/10.1111/j.1467-9280.2006.01693.x | Practice tests beat restudy for delayed retention; assessment loops are mandatory. |
| Unsuccessful retrieval | Kornell, Hays & Bjork — Unsuccessful retrieval attempts | https://doi.org/10.1037/a0014241 | Pretesting / failed attempts can still improve later learning. |
| Feedback timing | Butler & Roediger — Feedback timing | https://doi.org/10.3758/MC.36.3.604 | Balance immediate correction with delayed review for durable gains. |
| Hypercorrection | Butterfield & Metcalfe | https://doi.org/10.1037/0278-7393.27.6.1491 | High-confidence errors, once corrected, stick—correct them promptly. |

## Spacing, interleaving, and capacity

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| Distributed practice | Cepeda et al. meta-analysis | https://doi.org/10.1037/0033-2909.132.3.354 | Space reviews; rough gap ≈ 10–20% of retention horizon when scheduling. |
| Successive relearning | Rawson & Dunlosky | https://doi.org/10.1037/a0020076 | Multiple successful relearning sessions before retiring an item. |
| Interleaving | Rohrer & Taylor — Interleaved mathematics | https://doi.org/10.1007/s10648-007-9042-0 | Mix topics rather than pure blocking for delayed performance. |
| Working memory chunks | Cowan — Magical number 4 | https://doi.org/10.1016/S0079-7421(01)80005-9 | Cap new named concepts per session; protect cognitive load. |

## Instructional design

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| Cognitive load | Sweller — Cognitive load theory | https://doi.org/10.1207/s15326985ep3801_1 | Prefer worked examples for novices; cut redundant re-explanation. |
| Expertise reversal | Kalyuga et al. | https://doi.org/10.1207/s15326985ep3801_4 | Fade scaffolds as competence evidence appears. |
| Guidance for novices | Kirschner, Sweller & Clark | https://doi.org/10.1207/s15326985ep4102_1 | Pure discovery is a weak default for beginners building a degree path. |
| Desirable difficulties | Bjork lab overview | https://bjorklab.psych.ucla.edu/wp-content/uploads/sites/13/2016/04/RBjork_ajp1994.pdf | Effortful retrieval and spacing improve long-term retention. |

## Spaced-repetition tooling defaults

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| FSRS / open SRS research | open-spaced-repetition | https://github.com/open-spaced-repetition/fsrs4anki | Target retention near a 70–90% band when exporting review queues; verify the learner's tool docs live. |

## Skill format authority

| Topic | Source | URL | Takeaway used in skill |
|------|--------|-----|------------------------|
| Agent Skills specification | agentskills.io | https://agentskills.io/specification | Frontmatter, progressive disclosure, package layout. |
| Reference validator | skills-ref | https://github.com/agentskills/agentskills/tree/main/skills-ref | `uvx --from skills-ref agentskills validate skills/university`. |

## Practice notes

- **Do not hard-code institutional credit hours, tuition, or exam cut-scores.** Pull them from the learner's current syllabus, registrar, or exam board pages.
- Learning-science effect sizes are design inputs, not medical or clinical claims.
- When a board syllabus conflicts with a general psychology paper, the board wins for that credential.
