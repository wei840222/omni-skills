# Google Colab Sources (Gate 6)

Primary documentation used to verify runtime, IO, and notebook guidance in this skill. Prefer these over forum anecdotes.

## Product overview and FAQ

- Google Colaboratory FAQ — product scope, free/paid tiers, and common limits via https://research.google.com/colaboratory/faq.html
- Google Cloud Colab docs hub — managed Colab and enterprise-oriented guidance via https://cloud.google.com/colab/docs

## Official notebooks

- Colab basic features overview notebook — environment, cells, and core UX via https://colab.research.google.com/notebooks/basic_features_overview.ipynb
- Colab external data notebook — Drive mounts, uploads, and external IO patterns via https://colab.research.google.com/notebooks/io.ipynb
- Colab GPU notebook — accelerator selection and GPU workflow checks via https://colab.research.google.com/notebooks/gpu.ipynb

## Tooling and specification

- googlecolab/colabtools — upstream Colab client tooling and issue tracker via https://github.com/googlecolab/colabtools
- Agent Skills specification — package format and progressive disclosure rules via https://agentskills.io/specification

## Domain notes retained from baseline

- Treat runtime class, package pins, seeds, and split method as first-class reproducibility evidence.
- Prefer layered triage (runtime → data → model → evaluation) before random cell edits.
- Require dry-run and budget cutoffs before full-scale GPU/TPU jobs.
