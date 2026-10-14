# Sources (Gate 6)

Full URLs verified while refactoring this skill (2026-10-14). Re-check before
restating WSJF math, interruption recovery numbers, or GTD two-minute claims.

## Agent skill format

- Agent Skills specification: https://agentskills.io/specification
- Agent Skills specification index: https://agentskills.io/llms.txt
- Reference validator package: https://github.com/agentskills/agentskills/tree/main/skills-ref

## Cost of delay / WSJF

- Scaled Agile Framework — WSJF overview (canonical product page; may require
  access): https://scaledagileframework.com/wsjf/
  Supporting secondary explainer with the same formula framing:
  https://blackswanagile.com/wsjf-weighted-shortest-job-first/
  Takeaways: WSJF ranks work by cost of delay divided by job size; prefer
  highest CoD per unit effort within a priority band; job size is relative,
  not a substitute for the P0–P3 level tests.

## Interruption recovery

- Gloria Mark et al., CHI 2008 — "The Cost of Interrupted Work: More Speed and
  Stress" PDF: https://ics.uci.edu/~gmark/chi08-mark.pdf
  Author page: https://ics.uci.edu/~gmark/
  Takeaways: interrupted work can finish faster with higher stress and effort;
  people compensate under interruption load. The popular "~23 minutes to return
  to prior depth" figure is commonly attributed to Mark's interruption research
  line; treat the exact minutes as orientation, not a hard SLA, and still require
  a written parking note before mid-task switches.

## Two-minute / capture hygiene

- Getting Things Done — What is GTD?: https://gettingthingsdone.com/what-is-gtd/
  Takeaways: clarify actionable items; do immediately only when the next action
  is truly trivial relative to tracking cost (classic "two-minute" heuristic).
  Cap chains of "quick favors" so the exception does not bypass the queue.

## Priority framing (optional context)

- Eisenhower / time-management framing (secondary):
  https://en.wikipedia.org/wiki/Time_management#The_Eisenhower_Method
  Takeaways: urgent vs important is a planning lens; this skill still scores
  **cost of delay** and verifiable state tests rather than Eisenhower quadrants alone.
