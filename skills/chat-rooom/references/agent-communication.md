# Agent Communication Patterns

## Purpose

Use this reference when selecting message structure or coordination conventions for a local room. The skill keeps its implementation deliberately local and file-backed; it does not implement a network protocol or claim protocol interoperability.

## Practical pattern

A room message has one intent (`ask`, `update`, `proposal`, `decision`, `block`, `handoff`, or `done`), a named recipient when action is assigned, and an exact path, command, or evidence reference. This maps a local operational log to the collaboration concerns covered by the references below without requiring a hosted messaging system.

## Sources

- FIPA Agent Communication Language specification: https://www.fipa.org/specs/fipa00061/SC00061G.html
- NIST AI Risk Management Framework 1.0, Govern function: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
- Agent Skills specification (portable skill-package conventions): https://agentskills.io/specification
