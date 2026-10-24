---
name: spaced-repetition
description: >
  Explain and apply spaced-repetition scheduling: retrieval practice, forgetting-curve
  timing, SM-2 vs FSRS, atomic card design, review-load math, leeches/ease hell, and
  when SR is the wrong tool. Use when choosing intervals or desired retention, clearing
  a review backlog, rewriting failing cards, migrating SM-2→FSRS, or deciding whether
  a fact belongs in a spaced deck. Prefer `anki` for Anki UI/sync/import operations,
  `flashcards` for card-format authoring without scheduler theory, and `studying` for
  exam countdowns and study-session coaching.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"⚡"}'
  related-skills: '{"anki": "Anki product operations: deck options UI, FSRS toggles, sync, imports, templates.", "flashcards": "Atomic card authoring and TSV/export formats when the ask is writing cards, not scheduling theory.", "learning": "Broader learning strategy; use when SR is only one tactic inside a larger learning plan.", "memory": "Durable fact store for lookup; use when the goal is storing a fact to retrieve later, not practicing recall on a schedule.", "notes": "Source material and atomic notes that feed cards; use when capturing notes before carding.", "studying": "Exam countdowns, study blocks, and session coaching beyond scheduler mechanics."}'
---

This skill is knowledge-only: it does not store local configuration or persistent user state. Anki collection data stays in the user's Anki app; optional preferences for Anki itself belong to the `anki` skill's `<state_root>`.

Load `references/supermemo.md` when choosing SM-2 vs FSRS, setting desired retention, or diagnosing interval explosion / ease hell. Load `references/sources.md` when a claim needs a primary URL or version-sensitive default.

## When to use

- Picking or explaining a review schedule (expanding intervals, desired retention)
- Designing or repairing cards so retrieval—not rereading—drives learning
- Diagnosing backlog, leeches, ease hell, or review-load blow-ups
- Deciding that SR is the wrong tool (motor skills, daily procedures, one-off jargon)
- Hand off Anki clicks/sync/imports to `anki`; hand off exam plans to `studying`

## Mechanism: retrieval is the active ingredient

Spacing is the schedule; retrieval is the drug. Spacing rereading barely beats massed rereading; the retention gain lives in forcing recall, then checking.

- Active recall first, feedback second: pulling the answer out consolidates; peeking before trying is a reread.
- Testing effect: retrieval beats rereading by roughly 2× at a one-week delay, and the gap widens with longer delays (Roediger/Karpicke line of work — see `references/sources.md`).
- Desirable difficulty: slight struggle beats instant answers. Always-<1s cards are over-reviewed; always-fail cards are under-learned or badly written.
- Prefer production over recognition: typed/spoken answers beat multiple-choice familiarity.
- Honest grading: mark against the real answer. Self-flattery ("I basically had it") silently inflates intervals.

## Forgetting curve and interval ladder

- Decay is steepest early (first day); day-1 review is the highest-leverage slot. Use the forgetting-curve overview in `references/sources.md` for shape, not as a universal percentage table.
- For a fixed review budget, expanding schedules (1, 3, 7, 14, 28…) beat equal spacing.
- A typical SM-2-ish first ladder: 1d → 3d → 7d → 14d → 28d → 60d → 120d. The algorithm then adjusts from grades.
- The interval predicts when you are about to forget. Review when recall is effortful but successful; early "just in case" reviews collapse intervals and multiply load.

## Algorithms: SM-2 vs FSRS

Summary here; decision notes and URLs in `references/supermemo.md`.

- **SM-2**: ease-factor heuristic, no retention target. Weakness — ease inflation → absurd multi-month intervals.
- **FSRS**: targets desired retention (commonly 0.90 in Anki) with parameters fit on personal history; defaults until enough reviews exist.
- Treat desired retention as the workload dial. ~0.85 = fewer reviews, more forgetting; ≥0.95 balloons load; guidance near 0.97 is roughly double the reviews of 0.90 (ABC of FSRS).
- Grade by actual recall quality, not annoyance. After SM-2→FSRS migration, wait ~1 month of honest grading before judging intervals.
- Product toggles live in Anki deck options — use skill `anki` for the UI path.

## Card design

- One atomic fact per card. Miss one item in a three-fact card and you cannot tell which failed — split it.
- Minimum information: answer in a word or short phrase. A paragraph answer is a reread.
- Cloze for facts inside a sentence; Q&A when a blank would leak the answer or a produced explanation is required.
- Context-sufficient: the card must make sense months later without the surrounding deck.
- Prefer production prompts ("What is X?") over yes/no recognition.
- Bidirectional pairs need reverse cards (capital↔country, language pairs).
- Interference: near-synonyms, adjacent numbers, similar formulas — merge, distinguish with a mnemonic, or stagger.
- Use images only when recall depends on them (anatomy, maps, diagrams).
- Pre-process sources: understand first, then write 5–10 atomic cards for what must still be recallable in a year. Tag each card with its source so wrong facts can be audited.

## Review economy and target retention

- Above 0.90, marginal retention is expensive: each extra retention point costs substantial review volume (FSRS guidance; see `references/supermemo.md`).
- Sustainable new-card rate for a serious learner: about 10–20 new/day. Each new card generates roughly 7–10 reviews in its first month.
- Steady state at 0.9 with steady additions: daily reviews ≈ 7–10× daily new cards (e.g. 20 new → ~140–200 reviews).
- Backlog compounds. Prefer a short daily session over binge grading.
- If overloaded: freeze new cards first and grind due reviews down; cutting reviews while adding new cards lets the deck rot.
- Time budget: mature cards ~5–8s; new/failed ~15–30s. Grade honest even when slow — right-but-slow is Hard, not Good.

## Leeches, ease hell, and failure modes

- **Leech**: repeated failures (Anki default flag often at 8 lapses). The card is broken. Fix order: rewrite smaller → mnemonic → image → split → suspend if still failing.
- **Ease hell (SM-2)**: ease driven to the ~1.3 floor so intervals barely grow. Reset ease and fix the card, or migrate to FSRS (no ease floor).
- Lenient-grade trap: marking Good on slow recall to "keep moving" inflates intervals, then fails later and hammers ease.
- Same-day over-learning: five relearns in one day trains short-term memory. One clean recall, then trust the schedule.
- Deck bloat: huge untouched pre-made decks are not progress. Add cards already engaged with.
- Suspended-card debt: periodically delete cards you will never revive.

## When spaced repetition is the wrong tool

- Motor skills (serve, intubation): need massed, varied, feedback-driven practice — not spaced fact recall.
- Daily procedures: the job is the review; SR is overhead.
- Conceptual understanding first: learn via problems/explanation, then SR the facts that must be cold-recallable.
- Look-up-faster-than-recall trivia (rare API endpoints with durable docs).
- Near-term disposable jargon for a short project.
- Massive, rapidly rotating sets where maintenance cost exceeds value — prefer fewer high-yield cards.

## Habit and daily load

- Daily consistency beats heroic weekends; the algorithm assumes steady input.
- Prefer one consolidated daily review habit over scattered micro-decks.
- Clear due reviews before adding new cards.
- Mobile for reviews; desktop for thoughtful card creation.
- Hold a new-card ceiling for months; a motivated 100-card binge borrows future reviews at interest.
- Audit quarterly: delete leeches, rewrite confusing cards, check retention stats.
- Review when rested enough to grade honestly; halve load rather than speed-grade hundreds of cards into noise.

## Situations

| Situation | Play |
|---|---|
| 500+ reviews backlogged | Freeze new cards; set a daily review cap you will keep; grind to zero over 1–2 weeks with honest grades. |
| Failed the same card 4× today | Treat as a forming leech: rewrite/split; suspend if still failing. |
| Language deck with 50 near-synonyms | Expect interference; add distinguishing context or introduce one synonym cluster at a time. |
| Exam in 3 days | SR will not rescue you now. Massed practice + practice questions; feed survivors into SR afterward (`studying`). |
| Answer side is a paragraph | Not a card. Split into 5–8 atomic cards or delete. |
| Reviews >45 min/day | Lower desired retention toward 0.85, cut new cards, or accept the cost. |
| Want to learn a motor skill | Out of scope for SR. Massed supervised practice; SR only surrounding facts. |
| Switching SM-2 → FSRS | Enable FSRS, keep ~0.90, wait a month before judging (`references/supermemo.md`, skill `anki`). |
| Two cards keep swapping answers | Interference: merge, mnemonic, or stagger. |
| Added 80 new cards in one day | Stop. Cap at 10–20/day next week to absorb the borrowed reviews. |

## Where camps disagree

- **SM-2 vs FSRS**: FSRS wins on review economy once history exists; SM-2 remains only for brand-new profiles or tools without FSRS.
- **Cloze vs Q&A**: cloze for speed/lists; Q&A when blanks leak answers or explanations must be produced.
- **Pre-made vs self-made decks**: pre-made for bounded high-consensus facts; self-made for conceptual material (authoring is learning).
- **Cap reviews vs unlimited**: cap when load threatens the habit; uncap when daily consistency is sustainable.
- **Recognition vs recall grading**: recall wins whenever production is the goal; recognition only when recognition itself is the skill.
