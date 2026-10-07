# Primary Sources (Gate 6)

Verify format, scoring, fees, MyBest, and send-score claims against these pages before overriding skill memory. Record access dates in PR notes when numbers change.

## Official ETS — test overview and content

- **TOEFL iBT about** — product overview and entry points via https://www.ets.org/toefl/test-takers/ibt/about.html
- **Test content and structure** — current section map, approx. timing/items, center vs Home Edition via https://www.ets.org/toefl/test-takers/ibt/about/content.html
- **Reading section** — Complete the Words, Read in Daily Life, Read an Academic Passage via https://www.ets.org/toefl/test-takers/ibt/about/content/reading.html
- **Listening section** — response, conversation, announcement, academic talk tasks via https://www.ets.org/toefl/test-takers/ibt/about/content/listening.html
- **Speaking section** — Listen and Repeat; Take an Interview via https://www.ets.org/toefl/test-takers/ibt/about/content/speaking.html
- **Writing section** — Build a Sentence; Write an Email; Academic Discussion via https://www.ets.org/toefl/test-takers/ibt/about/content/writing.html
- **Registration hub** — account, ID, disability accommodations, bulletin entry via https://www.ets.org/toefl/test-takers/ibt/register.html
- **Prepare hub** — official prep and sample materials via https://www.ets.org/toefl/test-takers/ibt/prepare.html

## Official ETS — scores, MyBest, sending

- **Scores hub** — MyBest entry, getting/sending/understanding scores via https://www.ets.org/toefl/test-takers/ibt/scores.html
- **Understanding scores** — 1–6 scale (from 21 Jan 2026), 0–120 transition overall, ~3-day release, 2-year validity, free recipient rules, comparison bands via https://www.ets.org/toefl/test-takers/ibt/scores/understand-scores.html
- **MyBest anchor on understand-scores** — superscore explanation section via https://www.ets.org/toefl/test-takers/ibt/scores/understand-scores.html#WhatareMyBestscores
- **Get scores** — availability logistics via https://www.ets.org/toefl/test-takers/ibt/scores/get-scores.html
- **Send scores** — free recipients, additional reports, delivery channels/timing via https://www.ets.org/toefl/test-takers/ibt/scores/send-scores.html

## Official ETS — fees and policy bulletins

- **Registration and service fees** — country test fee entry + service fee table (reschedule, additional reports, score review, etc.) via https://www.ets.org/toefl/test-takers/ibt/register/fees.html
- **TOEFL iBT Information Bulletin (PDF)** — linked from registration/fees pages; full policy source for deadlines and procedures (open the current bulletin from the live ETS page rather than a cached filename)

## Admissions and immigration mapping (verify per destination)

- **Target university English / graduate admissions page** — overall and section minima, MyBest/single-sitting policy, waiver text
- **IRCC language-test lists (Canada)** — do not treat TOEFL as a drop-in for Express Entry without the current accepted-test instrument
- **UKVI / professional body accepted-test lists** — when a Secure English Language Test or registration pathway is required
- **Employer or licensing board instructions** — for H-1B-adjacent or professional screens that ask for English evidence without a statutory TOEFL minimum

## Knowledge updates captured this refactor

- Replaced pre-2026 long-passage / 4-task Speaking / Integrated Writing inventory with the Jan 2026 ETS task map (short focused tasks; Listen and Repeat + Interview; Build a Sentence + Email + Academic Discussion)
- Documented dual scoring: primary 1–6 section/overall scores plus transitional comparable 0–120 overall
- Corrected score availability to ETS’s ~3-day electronic release guidance and 2-year validity
- Normalized state paths from `~/Clawic/data/toefl/` to portable `<state_root>/toefl/` with an explicit resolver
- Marked MyBest as report-included but school-optional; single-sitting rules remain common
- Service fees and additional score-report prices must be re-read from the fees page (amounts move)