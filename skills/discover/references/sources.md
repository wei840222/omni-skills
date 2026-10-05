# Research sources (Gate 6)

Verified during the 2026-10-05 discover refactor handoff. Prefer these URLs over model memory when updating format, novelty, or heartbeat claims.

## Agent Skills format

- Agent Skills specification — https://agentskills.io/specification
- Optional directories / progressive disclosure — https://agentskills.io/specification#optional-directories
- Agent Skills docs index — https://agentskills.io/llms.txt
- Reference validator package — https://github.com/agentskills/agentskills/tree/main/skills-ref

## Novelty, curiosity, and exploration

- Pathak, Agrawal, Efros, Darrell — Curiosity-driven Exploration by Self-supervised Prediction (ICML 2017) —
  https://proceedings.mlr.press/v70/pathak17a.html
  (intrinsic curiosity as prediction-error signal; prefer surprise that improves the forward model over raw volume)
- Schmidhuber — Formal Theory of Creativity, Fun, and Intrinsic Motivation (1990–2010) —
  https://people.idsia.ch/~juergen/creativity.html
  (compression progress / interestingness as the driver of continued exploration)
- Litman — Curiosity and the pleasures of learning (2005 overview via APA PsycNET record) —
  https://psycnet.apa.org/record/2005-13803-004
  (interest vs deprivation curiosity; useful when deciding whether a finding changes options)

## Heartbeat / quiet no-change contracts

- OpenClaw HEARTBEAT guidance (workspace convention used by this repo's heartbeat skill) —
  treat `HEARTBEAT_OK` as the quiet success path when no material novelty exists; pair with skill `heartbeat` package rules rather than inventing a new status vocabulary.
- EBU / ops analogy for alert hygiene: prefer actionable deltas over heartbeat noise; discovery logs only findings that clear `references/novelty-test.md`.

## State and workspace conventions

- omni-skills project Gate 3 state roots: `<workspace>/<skill>/`, `<workspace>/memory/<skill>/`, `~/<skill>/` with first-existing lookup and default create at `<workspace>/<skill>/`.
- Do not treat legacy vendor data-directory paths for discover as active candidate roots; migration requires explicit user consent.
