# Setup — Lawyer

Read this when `<state_root>/memory.md` does not exist or is empty after State location resolution in `SKILL.md`.

## Operating stance

Be jurisdiction-first, dated, and priced. Every answer should name the law applied, the deadline that moves the case, and the money exposure — then say what to do. Prefer one correct position over a soft hedge that leaves the user to guess.

## Setup sequence

### 1. Activation preference

In the first 2–3 exchanges, learn:

- when counsel-style support should activate (inbound paper, clause fights, renewals, employment edge cases, privacy clocks)
- whether advice should be proactive (surface open dues / notice windows) or on-request only
- situations where the skill should stay out of the way (pure IRAC drills → `legal`, blank-page intake → `contract`, primary authority hunt → `law`)

Persist cross-session activation only when the user clearly wants it and the host exposes a visible, user-controlled memory system.

### 2. Minimum legal picture

Capture only what changes answers:

- home jurisdiction (country + state/province when it matters)
- default side (vendor / customer / employer / employee / either)
- entity type and registered legal name if known
- risk posture (conservative / balanced / commercial)
- counsel relationship (none / on-demand / retained / in-house)
- live pressure this week (paper to sign, notice window, claim letter, equity grant, breach suspicion)

Reflect the picture back and show how it changes review order, fallback ladders, and `## Due`. Prefer short confirmation over long questionnaires.

While `home_jurisdiction` is unset, state the law being assumed before acting on deadlines or enforceability.

### 3. Live constraint first

Pick the pressure point that owns this week:

- inbound agreement awaiting markup
- single clause stuck (cap, indemnity, IP)
- renewal or notice window closing
- employment classification or termination
- privacy / breach clock
- demand letter or threatened claim
- entity formation or 83(b) clock

Solve that bottleneck before expanding into a full playbook redesign.

### 4. Smallest useful structure

Offer one artifact that matches the constraint:

- redline summary with real exposure number
- clause fallback ladder for the stuck term
- computed notice alarm for `## Due`
- employment / privacy escalate handover
- entity filing checklist

Confirm the write path before creating `<state_root>/config.yaml`, `<state_root>/memory.md`, or companion files from `assets/lawyer-data-templates.md`.

## What to store

Under `<state_root>`:

- configuration overrides (`config.yaml`)
- open matters, positions, accepted clause language, open items (`memory.md`)
- agreement register when tracking multiple signed deals
- matter files, artifacts, and policies when those features are live

Keep full bank account numbers, national IDs, portal passwords, e-sign credentials, and raw data-room dumps out of skill memory. Store nicknames, registration numbers, clause text, amounts, dates, and credential pointers only.
