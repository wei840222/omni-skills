# Backup sources (Gate 6)

Checked 2026-09-30. Re-open the live page before restating policy claims, product defaults, or API field names.

## Standards and public guidance

- **CISA — Data Backup Options (PDF)** — foundational public-sector backup option framing.
  - https://www.cisa.gov/sites/default/files/publications/data_backup_options.pdf
- **CISA StopRansomware hub** — ransomware-oriented resilience entry point.
  - https://www.cisa.gov/stopransomware
- **CISA Ransomware Guide** — defensive practices including backup resilience themes.
  - https://www.cisa.gov/stopransomware/ransomware-guide
- **NIST SP 800-34 Rev. 1** — contingency planning guidance (recovery concepts, not a backup product manual).
  - https://csrc.nist.gov/publications/detail/sp/800-34/rev-1/final
  - PDF: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-34r1.pdf

## 3-2-1 family explanations

- **Veeam — What is the 3-2-1 Backup Rule?** — widely cited 3-2-1 explanation.
  - https://www.veeam.com/blog/321-backup-rule.html
- **Backblaze — The 3-2-1 Backup Strategy** — vendor explainer of the classic rule (verify claims against your threat model).
  - https://www.backblaze.com/blog/the-3-2-1-backup-strategy/

## Cloud immutability and platform backup

- **Amazon S3 Object Lock** — WORM / retention lock mechanics for immutable object backups.
  - https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html
- **Azure Backup overview** — Microsoft backup service concepts (product-specific; confirm SKU limits live).
  - https://learn.microsoft.com/en-us/azure/backup/backup-overview

## Database and tools

- **PostgreSQL backup documentation** — logical/physical backup overview.
  - https://www.postgresql.org/docs/current/backup.html
- **PostgreSQL continuous archiving / PITR** — WAL-based recovery.
  - https://www.postgresql.org/docs/current/continuous-archiving.html
- **restic documentation** — repository model, encryption, and restore workflows.
  - https://restic.readthedocs.io/en/stable/
- **BorgBackup documentation** — deduplicating archives and restore operations.
  - https://borgbackup.readthedocs.io/en/stable/

## Skill format authority

- **Agent Skills specification** — package format and validator expectations for this repository.
  - https://agentskills.io/specification

## What this skill does not treat as a live measurement

Example retention “keep monthlies for a year,” keepalive-style operational defaults from other domains, and vendor marketing extensions of 3-2-1 (including 3-2-1-1-0 wording) are planning heuristics. Legal hold, RPO/RTO numbers, and cloud pricing must be taken from the customer’s policy and the provider’s current pricing page—not from this skill text.
