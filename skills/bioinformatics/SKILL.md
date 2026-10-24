---
name: bioinformatics
description: "Process and analyze biological sequences. Run genomic pipelines for sequence alignment, variant calling, and expression analysis on DNA, RNA, or protein data. Use when executing BLAST searches, processing FASTQ/BAM files, variant calling, or analyzing gene expression."
metadata:
  openclaw: '{"emoji":"🧬","requires":{"bins":["samtools","bcftools","bedtools","bwa","fastqc","fastp"],"config":["<state_root>/bioinformatics/"]},"os":["linux","darwin"]}'
  related-skills: '{"data-analysis": "Statistical tables, plots, and tabular post-processing of alignment or expression outputs.", "science": "Broader scientific method, experiment design, and non-sequence lab workflows outside genomics toolchains.", "statistics": "Hypothesis tests, multiple-testing correction, and quantitative interpretation of variant or expression results."}'
---
## When to load

Load this skill when the user provides biological sequence data (FASTQ, FASTA, BAM, VCF) or explicitly requests genomic analysis, sequence alignment, or variant calling. Limit loading to biological data processing exclusively.

## State location

Bioinformatics state may exist in `<workspace>/bioinformatics/`, `<workspace>/memory/bioinformatics/`, or `~/bioinformatics/`.
Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured path when one exists.
2. Otherwise use the first existing directory in this order:
   `<workspace>/bioinformatics/`, `<workspace>/memory/bioinformatics/`, `~/bioinformatics/`.
3. If none exists and state must be created, default to `<workspace>/bioinformatics/`.

Use the selected `<state_root>` for every state operation in this skill.

- State root: `<state_root>/bioinformatics/`
- Memory schema: `assets/memory-template.md`

Read `references/setup.md` on first use for environment configuration.

## Required Reading

Before executing bioinformatics pipelines, you must read the relevant domain specifications:

- **Core Rules**: Read `references/core-rules.md` for required quality checks and resource traps.
- **Formats**: Read `references/formats.md` for FASTA, BAM, VCF conventions.
- **Tools**: Read `references/tools.md` for BWA, Samtools, and BCFtools parameters.
- **RNA-seq**: Read `references/rnaseq.md` for expression analysis workflows.
- **Variants**: Read `references/variants.md` for germline/somatic calling pipelines.

## Security and Privacy

- Process all sequences locally.
- Keep all analysis data local without making external API calls.
- Leave original source files (FASTQ, BAM) read-only; perform operations on copies.
