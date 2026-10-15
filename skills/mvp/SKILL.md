---
name: mvp
description: >
  Guide technical and non-technical builders through MVP scope definition,
  validation, and tradeoff management. Use when the user wants to launch a product
  fast, validate assumptions, or reduce feature bloat. Prefer `product` for
  end-to-end product + marketplace execution, `startup` for stage-wide founder
  orchestration, `founder` for founder operating-system work, and `growth` once
  retention math is sound.
metadata:
  version: "1.1.0"
  openclaw: '{"emoji":"🚀"}'
  related-skills: '{"founder":"Founder operating-system and psychology when the bottleneck is the person, not MVP scope.","growth":"Acquisition and retention systems after the MVP has validated demand.","indie-hacker":"Solo bootstrap sequencing and time protection for side-project MVPs.","product":"Broader product strategy, prioritization, and marketplace execution beyond MVP scope.","product-launch":"Go-to-market sequencing once the MVP scope is locked.","product-manager":"PM discovery, roadmaps, and stakeholder craft without MVP kill-criteria focus.","startup":"Stage-wide founder orchestration across PMF, hiring, and runway beyond a single MVP."}'
---

# MVP

Help builders ship the **smallest testable product** that can validate or invalidate one clear hypothesis.

This skill is **knowledge-only**. It does not create or require a persistent state tree. Do not write runtime notes into this package.

## First: Identify the User's Role

Determine the user context to load the correct role guide:

| Role | Key Focus | Load File |
|------|-----------|-----------|
| Technical Founder | Scope control, stop over-engineering | `references/technical.md` |
| Non-Technical Founder | Developer communication, validation before code | `references/non-technical.md` |
| Product Manager | Stakeholder alignment, scope defense | `references/pm.md` |
| Indie Hacker / Solo | Speed to market, validation without audience | `references/solo.md` |
| Investor / Advisor | Evaluating MVPs, red flag detection | `references/investor.md` |

## Universal MVP Principles

**The One-Sentence Test:** Can you state in one sentence what assumption you're testing? If not, scope is unclear.

**Minimum = Fastest Path to Learning**
- Not the smallest product. The fastest way to validate or invalidate your hypothesis.
- "What's the cheapest thing I can build to learn if anyone wants this?"

**Viable = Someone Would Pay/Use It**
- Not a demo. Not a prototype. Something that delivers enough value that a user would come back.
- If nobody would use it twice, it's not viable.

**Done Criteria:**
1. Core hypothesis is testable
2. One user flow works end-to-end
3. You can measure success/failure
4. Ship date is set and non-negotiable

## Progressive disclosure

- Scope matrices and decision logs → `references/scope.md`
- Validation techniques and kill criteria → `references/validation.md`
- Common anti-patterns → `references/traps.md`
- Role-specific coaching → the matching file in the table above

Prefer adjacent skills when they fit better:

- Broader product + marketplace execution → `product`
- Stage-wide founder orchestration → `startup`
- Founder psychology / operating system → `founder`
- Post-validation acquisition systems → `growth`
