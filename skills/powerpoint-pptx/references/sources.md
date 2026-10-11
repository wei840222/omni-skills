# Research sources (Gate 6)

Verify mutable claims (API names, chart enums, OOXML part structure, slide
dimensions) against these pages at answer time. Do not invent library version
limits from memory.

## Agent Skills format

- Agent Skills specification — https://agentskills.io/specification
- Agent Skills document index — https://agentskills.io/llms.txt
- skills-ref validator — https://github.com/agentskills/agentskills/tree/main/skills-ref

## python-pptx

- python-pptx documentation home — https://python-pptx.readthedocs.io/en/latest/
- Quickstart — https://python-pptx.readthedocs.io/en/latest/user/quickstart.html
- Presentations API — https://python-pptx.readthedocs.io/en/latest/api/presentation.html
- Charts API — https://python-pptx.readthedocs.io/en/latest/api/chart.html
- Slides / shapes conceptual notes — https://python-pptx.readthedocs.io/en/latest/user/slides.html
- Working with charts — https://python-pptx.readthedocs.io/en/latest/user/charts.html
- PyPI package — https://pypi.org/project/python-pptx/

## OOXML / PresentationML

- ECMA-376 Office Open XML — https://www.ecma-international.org/publications-and-standards/standards/ecma-376/
- Microsoft Learn — Structure of a PresentationML document — https://learn.microsoft.com/en-us/office/open-xml/presentation/structure-of-a-presentationml-document
- Microsoft Learn — Working with presentations — https://learn.microsoft.com/en-us/office/open-xml/presentation/working-with-presentations

## Design / delivery baselines (non-normative craft)

- Prefer deck theme fonts over decorative downloads for cross-app portability.
- Standard widescreen geometry commonly used with python-pptx examples:
  13.333" × 7.5" (16:9) and 10" × 7.5" (4:3) — confirm against the actual
  template before hard-coding.
