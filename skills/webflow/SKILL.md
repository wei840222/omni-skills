---
name: webflow
description: Load this skill when asked to design, develop, or optimize a Webflow
  site. It provides guidance on responsive layouts, CMS architecture, and performance
  best practices.
metadata:
  openclaw: '{"emoji": "🌐", "os": ["linux", "darwin", "win32"]}'
  related-skills: '{"ui": "General interface composition and visual hierarchy outside Webflow-specific controls.", "design": "Broader design systems and visual direction when the work is not Webflow-bound.", "landing-page": "Conversion-focused landing structure and offer messaging that Webflow then implements.", "website": "Multi-page site IA and content structure beyond a single Webflow build."}'
---
## When to load

- Load `references/design.md` for layout and responsive breakpoint guidance.
- Load `references/cms.md` for configuring CMS collections or headless APIs.
- Load `references/integrations.md` for forms, webhooks, or third-party embeds.
- Load `references/optimization.md` for SEO, accessibility, and performance checklists.

## Memory Storage

User preferences stored at `<state_root>/webflow/memory.md`. Read on activation.

**Format:**
```markdown
# Webflow Memory

## Profile
- role: freelancer | agency | founder | developer | marketer
- design-source: figma | sketch | from-scratch | template
- cms-needs: none | blog | multi-collection | headless

## Preferences
- class-naming: bem | utility | semantic
- breakpoints: mobile-first | desktop-first
```

Create folder on first use: `mkdir -p <state_root>/webflow`

## Critical Rules

1. **Always check all breakpoints** — Desktop looks great, mobile is broken. Test tablet/mobile-landscape/mobile-portrait BEFORE showing to client.

2. **Name classes semantically** — `hero-heading` not `heading-23`. You'll thank yourself during handoff.

3. **Set up CMS before content** — Define collections, fields, and relationships first. Migrating content between structures is painful.

4. **Calculate TRUE hosting cost** — Basic Hosting ≠ CMS Hosting ≠ Business Hosting. Forms, CMS items, staging all cost extra.

5. **Test forms with real submissions** — Webflow form notifications fail silently. Verify delivery before launch.

6. **Manually adjust responsive breakpoints** — Auto-generated layouts are often inaccurate. Explicitly configure and verify each breakpoint.

7. **Audit before publish** — Missing alt text, 404s, broken links, favicon, OG image, SSL, redirects. Use pre-launch checklist every time.

8. **Export code = cleanup required** — Webflow's exported HTML/CSS is bloated. Budget time for cleanup if moving off platform.

## Scope

This skill covers Webflow design, development, and project management. For general web design principles, see `ui` or `design`. For landing page conversion strategy, see `landing-page`.
