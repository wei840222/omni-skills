# Source Notes — fasting

Gate 6 research notes for intermittent fasting, extended fasting safety, electrolytes, refeeding risk, and related clinical guardrails.
All URLs below were used to verify domain guidance retained or strengthened in this refactor.

## Intermittent fasting evidence and protocols

- **NHS — Intermittent fasting** — public overview of IF patterns and cautions via https://www.nhs.uk/better-health/lose-weight/
- **NEJM review — Effects of Intermittent Fasting on Health, Aging, and Disease** (de Cabo & Mattson, 2019) — timeline physiology and clinical caveats via https://www.nejm.org/doi/full/10.1056/NEJMra1905136
- **Annual Review / TRE literature summary** — time-restricted eating windows and metabolic endpoints via https://pubmed.ncbi.nlm.nih.gov/31175808/

## Electrolytes, ketosis, and extended fasts

- **Volek & Phinney nutritional ketosis framing** — blood BHB bands commonly cited for nutritional ketosis (≈0.5–3.0 mmol/L) via https://www.dietdoctor.com/low-carb/ketosis
- **Fasting electrolyte practical ranges** — sodium / potassium / magnesium targets used as operational logging guidance (not prescriptions) via https://www.dietdoctor.com/low-carb/fasting-and-electrolytes

## Safety, refeeding, and crisis routing

- **NICE CG32 — Nutrition support for adults** — refeeding-risk criteria including low BMI and prolonged very-low intake via https://www.nice.org.uk/guidance/cg32
- **American Diabetes Association — Hypoglycemia** — treat-at <70 mg/dL (3.9 mmol/L) guidance relevant to insulin/sulfonylurea + fasting stacks via https://diabetes.org/living-with-diabetes/treatment-care/hypoglycemia
- **NEDA / Crisis Text Line** — disordered-eating support routing (text NEDA to 741741) via https://www.nationaleatingdisorders.org/get-help/

## Protein and training context

- **ISSN position stand — protein and exercise** — 1.6–2.2 g/kg/day range retained for muscle preservation inside the eating window via https://jissn.biomedcentral.com/articles/10.1186/s12970-017-0177-8

## Agent skill packaging (repo-local standards)

- **Agent Skills specification compatibility** — validated with `uvx --from skills-ref agentskills validate skills/fasting`
- **Repo workflows** — `.agents/workflows/skill-refactor.md` Gates 1–9 and `.agents/AGENTS.md` selection / packaging rules

## Obsolete / removed

- Hard-coded `~/Clawic/data/fasting/` as the only path; replaced with portable `<state_root>/` resolution (Gate 3)
- clawic.com homepage, feedback stars, and promotional Related Skills chrome (Gate 5)
- `_meta.json` packaging residue and non-standard top-level reference dumps (Gate 2)
- Invalid `metadata.clawdbot` / non-JSON `metadata.openclaw` shapes (Gate 1)
