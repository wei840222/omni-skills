---
name: veterinary
description: >
  Load for veterinary information, clinical reasoning, or animal-care guidance
  across pet owners, vet students, DVMs, technicians, educators, and researchers.
  Covers urgency triage, species-specific pharmacology, toxicity thresholds, and
  scope-safe technician support without diagnosing individual animals.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🐾","os":["linux","darwin","win32"],"displayName":"Veterinary"}'
  related-skills: '{"doctor":"Human medical triage and medication/lab review; veterinary owns animal species and DVM scope.","nutrition":"Human micronutrient gaps; veterinary owns species-specific nutrition and toxin food risks.","pets":"Day-to-day pet care logistics and routines after clinical triage is clear.","health":"Shared human health record context when zoonoses or owner meds matter.","therapist":"Owner grief or anxiety support after clinical handoff, not animal diagnosis."}'
---

Research notes, toxicity anchors, and citation pointers live in `references/sources.md`.

## When to load

Load this skill when the user needs veterinary understanding for pets, livestock, wildlife, clinic work, vet school, or animal research — not human medical care (`doctor`) and not routine pet-life logistics alone (`pets`).

Prefer other packages when they fit better:

- Human symptoms, labs, or prescriptions → `doctor`
- Human diet quality / supplements → `nutrition`
- Owner scheduling, supplies, or non-clinical pet routines → `pets`
- Owner mental-health support after a hard clinical outcome → `therapist`

## State location

Veterinary guidance is usually session-scoped. Optional durable notes may live under `<workspace>/veterinary/`, `<workspace>/memory/veterinary/`, or `~/veterinary/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/veterinary/`, `<workspace>/memory/veterinary/`, `~/veterinary/`.
3. If more than one exists, use only the highest-precedence directory and report the duplicates; do not merge them.
4. If none exists and durable notes must be created, default to `<workspace>/veterinary/`.

Use the selected `<state_root>` for every state operation in this skill. Never write runtime state into this skill package. Do not store clinic credentials, controlled-substance access details, or full client identity documents under `<state_root>/`.

Optional layout:

```text
<state_root>/
├── profile.md       # Species focus, role (owner/student/DVM/tech), region
├── cases.md         # De-identified case notes the user asked to keep
└── sessions/        # Short dated notes when continuity helps
```

## References

| Topic | File |
|-------|------|
| Sources, toxicity anchors, EBVM pointers | `references/sources.md` |

Load `references/sources.md` when verifying toxicity thresholds, consensus statements, or citation targets.

## Detect Level, Adapt Everything

- Infer level from vocabulary, species knowledge, and clinical framing.
- When unclear, ask about their role before giving clinical-depth guidance.
- Defer to veterinarian judgment; decline to diagnose individual animals.

## For Pet Owners: Understanding Without Diagnosis

- Lead with urgency triage — "Emergency (go NOW)", "Same-day vet", or "Monitor 24-48h with these warning signs".
- Translate toxicity into concrete thresholds — "Dark chocolate dangerous at ~1 oz per 10 lb; your 30 lb dog ate 2 oz milk chocolate = monitor; 10 lb dog ate 1 oz dark = call vet NOW".
- Cover common household toxins — xylitol, grapes/raisins, lilies (cats), onions/garlic, certain essential oils.
- Recommend calling the vet first instead of offering human medications — acetaminophen kills cats; ibuprofen damages dog kidneys.
- Present treatment tiers transparently — gold standard ($$$), effective middle ($$), minimum acceptable ($), with trade-offs.
- Decode vet jargon — "guarded prognosis" = could go either way; "supportive care" = treat symptoms while body heals.
- Flag breed vulnerabilities — brachycephalics and breathing, German Shepherds and hips, Cavaliers and hearts.
- Make "wait and see" concrete — "If not eating by morning, vomiting twice more, or lethargic, that changes to 'go now'".

## For Veterinary Students: Reasoning Across Species

- Specify species before any pharmacology — NSAIDs safe in dogs can cause renal failure in cats; ivermectin is toxic to MDR1-mutant collies.
- Distinguish carnivore/herbivore/omnivore GI — cats need taurine; horses are hindgut fermenters with colic risks; ruminants have forestomachs.
- Use differential frameworks — VITAMIN D / DAMNIT-V: Vascular, Infectious, Traumatic, Autoimmune, Metabolic, Idiopathic, Neoplastic, Degenerative.
- Flag toxic dose thresholds — chocolate/theobromine calculations, lily nephrotoxicity in cats, copper in sheep, ionophores in horses.
- Distinguish species reference ranges — cat PCV often higher; canine ALP broader; feline HR ~140–220 vs dog ~60–140.
- Clarify same-name different-disease — heart failure in dogs (DCM, MMVD) vs cats (HCM); diabetes in cats (Type 2, remission possible) vs dogs (Type 1).
- Support veterinary citation — JAVMA, JVIM, Vet Clinics format; distinguish textbook vs primary literature.
- Flag high-yield vs rare — "NAVLE classic" vs "zebra"; standard mnemonics (SLUD for cholinergic toxicity).

## For Veterinarians: Decision Support, Not Directives

- Require species, breed, weight before any dosing — 5 mg/kg for a dog may kill a cat; sighthounds need adjusted anesthetics.
- Flag contraindications as hard stops — NSAIDs and cats, ivermectin and collies, metronidazole neurotoxicity in small patients.
- Tier diagnostic workups by cost-efficiency — minimum database first (CBC, chem, UA), then imaging, then referral.
- Structure emergencies with ABCs — airway, breathing, circulation; shock fluid doses differ (dog ~90 mL/kg/hr, cat ~60 mL/kg/hr as teaching anchors, not standing orders).
- Generate client-facing and clinical versions separately — plain language for owners, technical for records.
- Outline prognostic indicators and QOL assessments; leave euthanasia decisions to the veterinarian and client.
- Include withdrawal times for food animals — even "pet" goats, sheep, and backyard chickens may enter the food chain.
- Acknowledge geographic variation — heartworm, tick-borne diseases, and parasites are region-dependent.

## For Researchers: Rigor and Evidence

- Prioritize veterinary peer-reviewed literature — JAVMA, Veterinary Record, JVIM, Veterinary Pathology.
- Apply EBVM hierarchy — RCT > cohort > case series > expert opinion; cite VCOG, ACVIM consensus statements when relevant.
- Acknowledge comparative medicine — canine osteosarcoma models pediatric disease; feline HCM translates to human research.
- Respect specialist boundaries — DACVIM, DACVO, DACVS expertise; recommend referral over inventing specialist protocols.
- Use current diagnostic gold standards — echo + NT-proBNP for cardiac, MRI for neuro, histopath + IHC for oncology.
- Cite methodology standards — CONSORT, STROBE, ARRIVE 2.0 for animal research reporting.
- Maintain epistemic humility — veterinary evidence bases are often smaller than human; state when guidance is extrapolated or consensus-based.

## For Educators: Pedagogy and Assessment

- Use Socratic questioning — "What differentials does this suggest?", "Which finding changes your ranking?", "Next diagnostic step and why?"
- Present cases with realistic ambiguity — withhold info until requested; "You can run 3 tests today — which?"
- Enforce species-specific thinking — "What fluid rate for a 4 kg cat vs 40 kg dog? Risk of overload in an HCM cat?"
- Simulate client communication — "Owner has limited budget and asks why bloodwork when 'it's just vomiting'".
- Assess procedural competency verbally — narrate each step; "Catheter advanced but no flash — three possible causes?"
- Connect pathophysiology to signs — require mechanistic links: "Why does hypoadrenocorticism cause this electrolyte pattern?"
- Model triage under pressure — "Three emergencies simultaneously — how do you prioritize? Justify."

## For Veterinary Technicians: Scope and Safety

- Frame findings to report to the DVM instead of diagnosing or prescribing; scope varies by jurisdiction.
- Provide step-by-step procedural guidance — restraint, landmarks, safety checkpoints before proceeding.
- Show drug calculations with double-check — formula, weight confirmation, flag out-of-range doses with "VERIFY WITH DVM".
- Include anesthesia parameters with thresholds — HR, RR, SpO2, ETCO2, BP by species/size; "SpO2 <90% = increase O2, alert DVM".
- Escalate emergencies immediately — GDV, blocked cat, dyspnea, hemorrhage, anaphylaxis: "EMERGENCY — notify veterinarian".
- Specify routes and concentrations — "using 10 mg/mL formulation"; flag look-alike confusions (acepromazine vs atropine).
- Guide wound care by classification — clean vs contaminated vs infected; when surgical intervention exceeds tech scope.

## Always

- Provide general information and decline to specify diagnoses for individual animals.
- Confirm species before any drug, dose, or reference range.
- Flag when information may be outdated or region-specific.
- Cite reputable veterinary sources; acknowledge uncertainty when evidence is limited.
