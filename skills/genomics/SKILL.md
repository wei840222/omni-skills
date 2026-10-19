---
name: genomics
description: >
  Interpret clinical genomic variants with ACMG/AMP evidence categories,
  population-frequency checks (gnomAD), ClinVar triangulation, and CPIC/PharmGKB
  pharmacogenomics dosing phenotype guidance. Use when the user already has
  called variants or diplotypes (for example VCF-derived findings, ClinVar IDs,
  CYP2D6/* haplotypes) and needs structured classification, PGx actionability,
  or annotation triage. Prefer `bioinformatics` for FASTQ/BAM alignment and
  variant calling, `medicine` for broader clinical decision support beyond
  variant-level interpretation, and `biology`/`chemistry` for molecular or
  metabolism context without clinical reporting.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🧬"}'
  related-skills: '{"bioinformatics":"Alignment, variant calling, and raw NGS processing before interpretation.","medicine":"Broader clinical decision support beyond variant-level genomics.","biology":"Molecular mechanisms when pathway context is needed.","chemistry":"Drug metabolism chemistry underlying PGx phenotypes.","health":"Patient-care framing outside specialist genomic reporting."}'
---

# Genomics

Clinical interpretation guidance for called genomic variants and pharmacogenomic
diplotypes. This skill classifies and explains; it does not process raw NGS files
or place clinical orders.

Optional persistent notes live under a resolved `<state_root>/genomics/` tree
outside this package. Never write runtime state into the skill tree.

## State location

Before reading or writing state, resolve `<state_root>` as follows:

1. If the host or user explicitly configures a genomics state root, use that path.
2. Otherwise choose the first existing candidate:
   - `$OPENCLAW_STATE_DIR/genomics`
   - `$HOME/.openclaw/state/genomics`
   - `$HOME/.local/share/genomics`
3. If none exist and the user consents to persistence, create the preferred
   host-appropriate candidate and use it as `<state_root>`.
4. Keep the selected `<state_root>` fixed for the rest of the invocation.

Use the selected `<state_root>` for every state operation in this skill.

## When to load what

| Need | Load |
|------|------|
| First-run consent + preference capture | `references/setup.md` |
| Memory / case template shapes | `assets/data-templates.md` |
| Official URLs and claim checklist | `references/sources.md` |
| Everyday ACMG / PGx triage | Stay in this file |

Do not preload every reference on a simple classification question.
Prefer `references/sources.md` only when refreshing URLs or adjudicating a contested claim.

## Core workflow

1. Confirm context: germline vs somatic, disease rarity, ancestry considerations.
2. Check population frequency first (gnomAD v4 when available).
3. Triangulate ClinVar / OMIM / literature; never classify from one weak source.
4. Apply ACMG/AMP evidence categories; state "insufficient data" when evidence is thin.
5. For PGx: report diplotype → phenotype → CPIC/DPWG-style action, with guideline URL.
6. Keep identifiable genomic detail inside `<state_root>/` only after consent.

## ACMG/AMP classification frame

| Category | Working rule |
|----------|--------------|
| Pathogenic / Likely pathogenic | Weighted PVS/PS/PM/PP evidence meets guideline thresholds |
| VUS | Conflicting or insufficient evidence; schedule re-review |
| Likely benign / Benign | Weighted BS/BP evidence, often with population frequency support |

Never invent criteria codes. Cite the evidence you actually have.

## Population frequency

| Source | Use |
|--------|-----|
| gnomAD v4 | Primary global / ancestry-aware allele frequency |
| gnomAD non-cancer | Somatic / cancer-context filtering support |

For rare Mendelian disease, allele frequency **>1% in any well-powered population**
is ordinarily strong benign support unless a clearly defined founder exception applies.

## Pharmacogenomics quick path

High-priority CPIC Level A pairs to keep in view:

| Gene | Example drugs | Typical action class |
|------|---------------|----------------------|
| CYP2D6 | Codeine, tramadol, tamoxifen, some SSRIs | Dose / alternative |
| CYP2C19 | Clopidogrel, PPIs, voriconazole | Dose / alternative |
| CYP2C9 + VKORC1 | Warfarin | Algorithmic dosing |
| DPYD | Fluorouracil, capecitabine | Reduce / avoid |
| TPMT + NUDT15 | Thiopurines | Reduce / avoid |
| HLA-B*57:01 | Abacavir | Avoid |
| HLA-B*15:02 | Carbamazepine | Avoid (ancestry-relevant) |
| SLCO1B1 | Simvastatin | Cap dose / alternative |
| G6PD | Rasburicase, primaquine | Avoid |
| CYP3A5 | Tacrolimus | Dose adjustment |

Phenotype labels: Poor / Intermediate / Normal / Rapid / Ultra-rapid metabolizer.
Map diplotype → phenotype before recommending a dose change.

## Annotation resources (manual lookup only)

| Resource | Role |
|----------|------|
| ClinVar | Clinical assertions + submitter concordance |
| gnomAD | Population frequencies |
| OMIM / ClinGen | Gene–disease validity |
| PharmGKB / CPIC | Drug–gene guidelines |

This skill does **not** auto-call external APIs. Provide URLs and let the user
(or an explicitly authorized tool call) fetch live records.

## Common traps

Load this list only when an interpretation looks stuck or overconfident.

- Treating a single ClinVar submitter as definitive
- Ignoring ancestry-specific frequency
- Treating CADD/REVEL as stand-alone pathogenicity
- Missing compound-het / phase context
- Using outdated gnomAD major versions without saying so
- Skipping gene constraint (pLI / LOEUF) when LoF is claimed

## Privacy boundary

- No automatic network upload of patient variants
- Persist preferences/cases under `<state_root>/` only with consent
- Do not store identifiable genomic data inside the skill package
