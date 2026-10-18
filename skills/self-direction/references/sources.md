# Sources — Self-Direction

Live-checked 2026-10-18 during local Jules takeover. Only URLs that returned HTTP
200 from this runner are retained as Gate 6 evidence.

## Agent Skills format

- https://agentskills.io/llms.txt
- https://agentskills.io/specification

## Mental models and inference

- https://www.nngroup.com/articles/mental-models/
- https://www.interaction-design.org/literature/topics/mental-models
- https://www.mindtools.com/aaiod9e/the-ladder-of-inference
- https://fs.blog/mental-models/
- https://en.wikipedia.org/wiki/Mental_model

## Values and decision-making

- https://en.wikipedia.org/wiki/Value_(ethics)
- https://www.apa.org/topics/decision-making

## Autonomy / risk framing for agent systems

- https://www.nist.gov/itl/ai-risk-management-framework

## Discarded / failed live checks

- https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed/mental-models → HTTP 404
- https://hbr.org/2011/06/making-your-values-mean-something → HTTP 404

## Domain notes used in this refactor

- Mental models are internal representations that drive prediction and action;
  mismatched models explain preference conflicts (NN/g, IxDF).
- Ladder of Inference warns against leaping from thin observation to belief;
  this skill therefore separates evidence → confidence → action.
- Hard boundaries stay non-negotiable; soft preferences belong in values or
  criteria, matching the ask-vs-act split also used by `escalate`.
- NIST AI RMF supports documenting risk thresholds and human oversight for
  higher-impact autonomous action — mapped here to confidence gates and
  escalation triggers in transmission frames.
