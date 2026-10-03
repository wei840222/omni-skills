# UI Design Guidelines

Detailed checklist for product interfaces. Load when implementing or reviewing beyond the SKILL.md core rules.

## Visual Hierarchy

- One focal point per screen—eye knows where to go first
- Size, color, weight establish importance—primary action most prominent
- Group related elements—proximity implies relationship
- White space is not wasted space—breathing room aids scanning

## Typography

- Maximum 2–3 font families—more creates visual noise
- Clear size scale: title > heading > body > caption—distinct steps, not gradual
- Line height 1.4–1.6 for body text—too tight or loose hurts readability
- Line length 45–75 characters—prevents eye fatigue
- Left-align body text—centered only for short headings

## Color Usage

- Primary color for primary actions—one dominant brand color
- Semantic colors consistent: red=error, green=success, yellow=warning
- Do not rely on color alone—add icons, text, or patterns for accessibility
- Neutral palette for most UI—color for emphasis, not everywhere
- Test color blindness scenarios—about 8% of men affected by common forms

## Spacing System

- Use consistent scale: 4px, 8px, 16px, 24px, 32px, 48px
- Apply same spacing for same relationships—all card padding equal
- More space around groups than within—visual grouping through proximity
- Generous padding on touch targets—44px minimum for mobile (platform may require 48dp)

## Alignment

- Grid system for consistency—8px or 4px base grid
- Align to invisible lines—elements share edges, not scattered
- Left edge strongest for LTR—anchor content predictably
- Optical alignment when needed—visual center differs from mathematical

## Component States

- Default, hover, active, focus, disabled—all states designed
- Focus state visible and clear—keyboard users need this
- Disabled looks disabled—reduced opacity, no pointer cursor
- Loading state replaces or clearly marks content—prefer inline indicators over silent freezes
- Error state in context—border, icon, and inline message together

## Icons

- Consistent style throughout—outlined or filled, not mixed casually
- Recognizable at small sizes—simple shapes work better
- Labels when meaning ambiguous—icon + text clearer than icon alone
- Touch target larger than visual icon—~44px tap area, ~24px icon

## Imagery

- Consistent aspect ratios—do not stretch or skew
- Fallback for failed loads—placeholder, graceful degradation
- Alt text for content images—decorative images `alt=""`
- Compress appropriately—quality vs file size balance

## Responsive Design

- Design for smallest screen first—enhance for larger
- Breakpoints based on content—rather than arbitrary device widths
- Touch targets larger on touch screens—hover-only affordances are not enough on mobile
- Consider landscape orientation—especially for tablets

## Dark Mode

- Requires redesigned depth and emphasis rather than simple color inversion
- Reduce extreme contrast slightly—pure white on pure black strains eyes
- Shadows behave differently—use lighter surfaces for elevation
- Test all states—errors, success, charts, images
- Respect system preference—allow explicit override when product needs it

## Motion and Animation

- Duration 150–300ms for UI transitions—fast but perceptible
- Ease-out for entering—starts fast, settles in
- Ease-in for exiting—accelerates out of view
- Consistent timing across similar interactions
- Purpose: guide attention, show relationships, provide feedback
- Honor `prefers-reduced-motion`: keep essential feedback, drop pure decoration

## Design Tokens

- Define tokens for colors, spacing, typography—single source of truth
- Semantic naming: `color-error` rather than raw color names
- Enables theming and dark mode—swap token values
- Scales with product—change once, update everywhere

## Common Mistakes

- Too many font sizes—stick to the scale
- Inconsistent spacing—creates unpolished feel
- Low contrast text—4.5:1 minimum for normal body text (WCAG AA)
- Buttons that lack clickable affordance—affordance matters
- Different styles for same component—cards should match cards
