# Bioinformatics Core Rules and Traps

## Quality and Reference
1. Run FastQC and check input data quality before analysis. Bad input equals bad output.
2. Maintain consistent reference genomes (e.g., GRCh38) per project. Store reference info in `<state_root>/bioinformatics/memory.md`.

## Resource Awareness
Bioinformatics commands consume massive resources:
- Estimate memory needs (BWA requires ~6GB for human genomes).
- Use streaming when possible (`samtools view | ...`).
- Warn the user before running operations exceeding 10 minutes.

## Common Traps
- **Chromosome naming**: Mismatches (`chr1` vs `1`) cause silent failures.
- **Missing indices**: BAM requires `.bai`, VCF requires `.tbi`. Regenerate indices after modifications.
- **Coordinates**: BED is 0-based; VCF/GFF are 1-based. Ensure coordinates align properly to prevent off-by-one errors.
- **Unsorted data**: Many tools fail silently with unsorted BAM files.
