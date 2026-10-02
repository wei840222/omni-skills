# QA Playbook - Animate

Require thorough testing across states beyond visual appearance.

## Minimum Validation

Check these states:
- initial load
- interrupted transition
- loading, success, error, retry
- reduced motion enabled
- fast repeated input
- backgrounding or navigation change mid-animation

## What to Look For

Visual quality:
- hierarchy stays readable
- no unexpected jumps or flashes
- enter and exit durations feel related

Behavior quality:
- interaction is acknowledged quickly
- touch, keyboard, and gesture input still work
- navigation flows freely during animation

Performance quality:
- no obvious jank on target devices
- no full-screen repaint for a tiny effect
- lists and overlays stay responsive during motion

Accessibility quality:
- reduced motion keeps the same meaning
- focus order stays predictable
- motion pairs with other signals for state change

## Shipping Artifacts

Leave behind:
- a deterministic preview, story, or demo state
- test coverage for the critical animated flow when the stack supports it
- notes on any known tradeoffs still accepted

## Fail Conditions

Block shipping if:
- motion hides latency instead of explaining it
- the app becomes harder to use under rapid interaction
- reduced motion breaks the flow
- performance is acceptable only on high-end hardware
