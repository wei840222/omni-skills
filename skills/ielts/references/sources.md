# Primary Sources (Gate 6)

Verify format, band descriptors, One Skill Retake, and score-policy claims against these pages before overriding skill memory. Record access dates in PR notes when numbers change.

## Official IELTS — test overview and format

- **IELTS homepage** — test types, booking entry, and product map via https://www.ielts.org/
- **Take IELTS / test information** — Academic vs General Training overview via https://www.ielts.org/take-a-test
- **Test format** — section order, timing, and task types via https://www.ielts.org/take-a-test/test-format
- **IELTS on computer** — computer-delivered format notes via https://www.ielts.org/take-a-test/ielts-on-computer
- **IELTS Online** — remote-proctored option availability and limits via https://www.ielts.org/take-a-test/ielts-online

## Official IELTS — scores and band descriptors

- **Understanding IELTS scores** — overall and section band explanation via https://www.ielts.org/for-test-takers/how-ielts-is-scored
- **IELTS band descriptors (Writing)** — Task Achievement/Response, Coherence & Cohesion, Lexical Resource, Grammatical Range & Accuracy via https://www.ielts.org/for-teachers/ielts-scoring-and-band-descriptors
- **IELTS band descriptors (Speaking)** — Fluency & Coherence, Lexical Resource, Grammatical Range & Accuracy, Pronunciation via the same scoring/band-descriptor hub
- **Results and validity** — typical release timing and 2-year validity policy via https://www.ielts.org/take-a-test/getting-your-results

## Official IELTS — retake and preparation

- **One Skill Retake** — eligibility window, which skills can be retaken, and how the new score combines via https://www.ielts.org/take-a-test/ielts-one-skill-retake
- **Official preparation materials** — free samples and paid prep map via https://www.ielts.org/take-a-test/preparation-resources
- **British Council IELTS** — booking/help surfaces that often host local center rules via https://www.britishcouncil.org/exam/ielts
- **IDP IELTS** — alternate official operator pages for booking and local policy via https://www.idp.com/ielts/

## Immigration and admissions mapping (verify per destination)

- **IRCC language test equivalency (Canada)** — CLB ↔ IELTS GT mappings change; always open the current IRCC language-test page before quoting CLB 7/9 cutoffs
- **Target university admissions English page** — overall and per-band minima are school-specific; never generalize one program’s cutoff
- **UKVI / professional body pages** — when the user needs a Secure English Language Test or registration pathway, open that body’s current accepted-test list

## Knowledge updates captured this refactor

- Package state paths moved from `~/Clawic/data/ielts/` to portable `<state_root>/ielts/` with an explicit resolver
- Writing Task 1 remains the primary Academic vs General Training fork (graph/process vs letter)
- One Skill Retake is treated as eligibility-gated advice, not a universal default
- US-bound users may still prefer TOEFL; route TOEFL-only workflows to `toefl` while keeping IELTS acceptance notes school-specific
