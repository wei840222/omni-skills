---
name: designer
description: Create, specify, critique, and hand off product, brand, interface, print, and accessibility design work. Use when a user needs a design artifact, a system of design decisions, a usability or accessibility review, or a design-business deliverable; not for single-artifact visual judgment, design-tool mechanics, or front-end implementation.
compatibility: "web, android, ios"
metadata:
  version: "1.0.2"
  openclaw: '{"emoji":"🎨"}'
  related-skills: '{"branding":"Handles brand strategy, positioning, and voice before visual identity work.","css":"Implements approved design decisions in CSS.","design":"Provides one-off visual judgment for a single artifact without a maintained system.","design-system":"Extends established component-library architecture.","figma":"Handles Figma file mechanics, including auto layout, variants, variables, and Dev Mode.","frontend":"Implements approved interface designs in front-end code."}'
---

## State location

Designer state may exist in `<workspace>/designer/`, `<workspace>/memory/designer/`, or `~/designer/`. Before reading or writing state, resolve `<state_root>` as follows:

1. Use an explicitly configured state root when one exists.
2. Otherwise use the first existing directory in this order: `<workspace>/designer/`, `<workspace>/memory/designer/`, then `~/designer/`.
3. If no candidate exists and the user asks to persist design state, create `<workspace>/designer/`.

Use the selected `<state_root>` for every state operation in this invocation. If several candidate directories exist, use only the highest-precedence one and tell the user that separate copies were detected. Keep the existing files in place; migration from a legacy location requires a separate, explicit copy-and-verify decision.

## Workflow

1. Identify the design outcome, audience, content, platform, constraints, and the observable measure of success.
2. Read `<state_root>/data/designer/config.yaml` and `<state_root>/data/designer/memory.md` when persistent design state exists. Before changing a palette, type scale, spacing scale, or component, inspect its `## Brands` and `## Surfaces` records.
3. Produce the artifact by default. When the user asks for a review of their own work, return a severity-ranked list of concrete changes instead.
4. Load the smallest matching reference below; validate the output with `references/output-gates.md` before delivery.
5. For durable work, record only the requested facts under `<state_root>` using `references/memory-template.md`. Name every write or deletion, and preserve rows written by other skills as read-only.

| Resource | Load when |
| --- | --- |
| `references/situation-playbook.md` | Choosing the appropriate design play for a request. |
| `references/symptom-to-cause.md` | A user says a design looks cluttered, cheap, flat, unreadable, or otherwise “off.” |
| `references/core-rules.md` | Setting visual hierarchy, spacing, color, accessibility, state, or token rules. |
| `references/numbers-that-decide.md` | Selecting measurable thresholds for typography, accessibility, motion, performance, research, or print. |
| `references/deliverable-contract.md` | Determining what must accompany a logo, screen, system, research result, or print artifact. |
| `references/output-gates.md` | Checking a design, spec, or recommendation before delivery. |
| `references/traps.md` | Avoiding common design and handoff failures. |
| `references/expert-disagreements.md` | Explaining a contested design choice and its decision boundary. |
| `references/domain-knowledge.md` | Verifying current WCAG, Material Design, or Apple HIG guidance. |
| `references/memory-template.md` | Reading or writing persistent designer state. |

## Operating rules

Design from constraints rather than taste. State the concrete token, ratio, pixel, millimetre, platform convention, or success measure that supports a decision. Work from declared defaults when they exist; otherwise state the assumption that materially affects the artifact.

Use one primary action per view. Define empty, loading, error, hover, focus-visible, and disabled states with the primary state. Design semantic tokens rather than ad hoc values, and provide an accessibility annotation whenever an implementation detail affects contrast, focus order, target size, motion, or reading order.

Store configuration at `<state_root>/data/designer/config.yaml`, design memory at `<state_root>/data/designer/memory.md`, contacts at `<state_root>/data/contacts/contacts.md`, named projects at `<state_root>/data/projects/<project>.md`, and subscriptions at `<state_root>/data/finances/subscriptions.md`. Preserve sensitive values as a pointer such as `env:FIGMA_TOKEN`, `keychain:adobe-id`, `1password:Work/Foundry/licence`, or `file:~/.config/fontawesome`; written state contains no credentials.

## Configuration

Defaults apply until the user states a preference. Keep the selected values in `<state_root>/data/designer/config.yaml`.

| Variable | Type | Default | Effect |
| --- | --- | --- | --- |
| `design_tool` | figma \| sketch \| penpot \| affinity \| illustrator \| none | figma | Shapes the design-file structure and handoff package. |
| `target_platforms` | list: web, ios, android, email, print | web | Selects applicable platform conventions and export checks. |
| `spacing_base_px` | number: 2–8 | 8 | Sets the unit for gaps, insets, and gutters. |
| `type_scale_ratio` | number: 1.067–1.618 | 1.25 | Sets generated type-scale steps. |
| `min_body_px` | number: 14–20 | 16 | Sets the body-text floor and type-scale base. |
| `contrast_target` | aa \| aaa | aa | Sets 4.5:1 / 3:1 or 7:1 / 4.5:1 contrast targets. |
| `a11y_posture` | baseline \| strict | baseline | Adds strict AA, target-size, and keyboard review gates when selected. |
| `color_notation` | hex \| hsl \| oklch | hex | Sets palette, token, and code-sample notation. |
| `token_naming` | tier-prefixed \| semantic-only \| framework | semantic-only | Sets the emitted token-name shape. |
| `css_framework` | tailwind \| css-vars \| scss \| styled-components \| none | css-vars | Sets the token-export and spec dialect. |
| `brand_file` | path \| none | none | Points to long-form brand constraints under `<state_root>/data/designer/`. |
| `pricing_model` | hourly \| fixed \| value \| retainer \| none | none | Shapes estimates, change requests, and scope language. |
