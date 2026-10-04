# Design System Guidelines

## Core Rules

### 1. Tokens First, Components Second

Design tokens are the foundation. Before building any component:

- Define color tokens (semantic roles, not only raw hex)
- Define a spacing scale (consistent multiplier; 4px base is common)
- Define a typography scale (modular ratio or fixed steps)

Components consume tokens. Prefer token references over hardcoded values in reusable UI.

### 2. Semantic Over Literal Naming

| Prefer avoid | Prefer |
|--------------|--------|
| `blue-500` in components | `color.primary` / `bg-brand` |
| raw `14px` in product UI | `font.size.sm` |
| ad-hoc `8px` gaps | `space.2` on a documented scale |

Semantic names survive rebrand; primitives can change under stable roles.

### 3. Three-Tier Token Architecture

```text
Primitive → Semantic → Component
   ↓           ↓          ↓
 gray-900   text-primary  button-text
```

- **Primitive**: raw values (palette steps, base sizes)
- **Semantic**: meaning-based roles (primary, danger, muted)
- **Component**: specific use (button-bg, card-border)

### 4. Document Decisions Alongside Specs

Every durable token and component pattern should record:

- **What**: value or pattern
- **When**: usage context
- **Why**: decision
- **Avoid**: anti-patterns that reintroduce drift

### 5. Platform-Agnostic Source of Truth

Prefer one authoring source that can export to:

- CSS custom properties
- Tailwind / theme config
- iOS / Android tokens
- Figma variables

Use a DTCG-aligned JSON shape and/or Style Dictionary (or equivalent) so platforms do not fork by hand.

### 6. Component API Consistency

Shared components should converge on predictable props:

- naming: `variant`, `size`, `disabled` (and documented aliases only when required)
- size scale: `sm` / `md` / `lg` unless product standards differ and are written down
- variants: `primary` / `secondary` / `ghost` (extend deliberately)

Predictability beats one-off clever APIs.

### 7. Versioning and Migration

Breaking token or component contract changes need:

- version bump (semver)
- short migration guide
- deprecation window before removal
- codemods when volume justifies them

## Common Traps

- **Premature abstraction** → Build ~3 real instances before extracting a shared pattern
- **Token explosion** → Dozens of near-identical grays without roles
- **Skipping documentation** → Undocumented patterns get reimplemented wrong
- **Edge cases first** → Cover the common 80% before exotic states
- **Missing dark-mode strategy** → Retrofit is far harder than planning dual themes
- **Inconsistent spacing** → Arbitrary values instead of a scale
- **Prop sprawl** → More than ~10 props often means split the component

## Architecture & State

Memory and optional token drafts live under the resolved `<state_root>/`. See `assets/memory-template.md`.

```text
<state_root>/
├── memory.md
└── tokens/
```

## Security & Privacy

**Stays local under `<state_root>/`:**

- design decisions
- token drafts and component notes

**This skill does not:**

- access files outside `<state_root>/` and user-provided project paths
- make network requests on its own
- store credentials or secrets
