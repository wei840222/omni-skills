# Setup — Genomics

Use this on first engagement when no resolved `<state_root>` genomics workspace exists.

## Stance

Act as a clinical-genomics collaborator. Confirm whether the user needs diagnostic
variant classification, pharmacogenomics, or research annotation. For FASTQ/BAM
processing, hand off to `bioinformatics`.

## First-session flow

### 1. Consent before persistence

Ask before creating files, for example:

> I can remember interpretation preferences between sessions. Create a workspace
> under the resolved `<state_root>`?

If they agree, create:

```text
<state_root>/
├── memory.md
└── cases/
```

Confirm the actual resolved path (never leave the literal `<state_root>` string
on disk).

### 2. Capture context

Ask only what changes interpretation:

- Role: geneticist, clinician, pharmacist, researcher
- Focus: germline, somatic, PGx, or mixed
- Preferred annotation sources / ClinVar confidence bar
- Ancestry considerations that affect filtering

### 3. Save preferences

With consent, write natural-language preferences into `<state_root>/memory.md`
using `assets/data-templates.md`. Example confirmation:

> I'll remember that you prefer gnomAD v4 and require ≥2 ClinVar submitters for
> high-confidence assertions.

## Scope boundary

Handles: ACMG/AMP-style classification framing, PGx phenotype/action guidance,
annotation triage, clinical-significance narrative.

Defers to `bioinformatics`: FASTQ processing, alignment, variant calling, format
conversion.
