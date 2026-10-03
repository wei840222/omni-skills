# Gate 6 sources (verified 2026-10-03)

Full URLs used for domain claims. Prefer these over model memory. This skill
gives non-diagnostic triage language only; clinical decisions remain with a
licensed veterinarian.

## Agent Skills format

- https://agentskills.io/llms.txt
- https://agentskills.io/specification.md
- https://github.com/agentskills/agentskills/tree/main/skills-ref

## Emergency and triage orientation

- https://www.akc.org/expert-advice/health/bloat-in-dogs/ — GDV/bloat warning pattern: swollen abdomen and unproductive retching need emergency care
- https://vcahospitals.com/know-your-pet/bloat-gastric-dilatation-and-volvulus-in-dogs — clinical owner-facing GDV signs and emergency framing
- https://www.aspca.org/pet-care/animal-poison-control — toxin exposure is an emergency/poison-control path, not home-dose experimentation
- https://www.aspca.org/pet-care/general-pet-care/hot-weather-safety-tips — heat injury risk framing for exercise and travel decisions
- https://www.aspca.org/pet-care/general-pet-care/travel-safety-tips — travel and transport preparation themes used in sitter/travel handoffs

## Training and behavior

- https://apdt.com/about/ — professional dog-training organization orientation favoring modern, welfare-aware practice over punishment-first defaults
- https://www.aspca.org/pet-care/dog-care/common-dog-behavior-issues — owner-facing behavior issue framing: context, management, and professional escalation

## Corrections vs older skill text

- Replaced hard-coded `~/Clawic/data/dog/` and `~/dog` setup side effects with portable `<state_root>` resolution and consent-gated creation.
- Removed Clawic homepage / star / latest-version promotion.
- Kept emergency bloat and heat language conservative and source-backed without inventing dosages or diagnoses.
- Clarified related skills as JSON string metadata with existing repo targets only.
