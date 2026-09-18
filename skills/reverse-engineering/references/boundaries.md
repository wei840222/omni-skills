# Boundaries

Reverse engineering is legitimate only when the authorization and safety model are clear.

## Non-Negotiables

- Require lawful and authorized access to the target.
- Prefer offline copies, captures, stubs, or sandboxes over live production systems.
- Ask before any step that can write, patch, fuzz aggressively, authenticate, or alter remote state.
- Require an explicit user request for a safe handling path before retrieving, exposing, or persisting secrets.

## Default Safety Stance

Default to read-only analysis when:
- the environment is unknown
- the target is customer-facing or production
- credentials would be required
- the blast radius is unclear

## What Not To Do

- Use targeted, verified tests instead of firing exploit chains blindly.
- Clearly identify invasive actions separately from generic inspection steps.
- Communicate clearly before widening scope from one component to a whole estate.
- Accurately label offensive capability rather than presenting it as a harmless diagnostic step.

## Escalation Triggers

Pause and confirm when:
- the only next step is invasive or destructive
- the target touches regulated, customer, or third-party data
- the user asks for credential extraction, auth bypass, persistence, or stealth
- the evidence points to malware, live compromise, or active abuse

## Good Framing

Use language like:
- "read-only capture"
- "minimal replay"
- "controlled sample"
- "offline reproduction"
- "evidence-backed hypothesis"

Use language that implies transparency, temporary analysis, and authorized access.
