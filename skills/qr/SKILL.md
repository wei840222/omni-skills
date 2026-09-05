---
name: qr
description: Generate and deploy scannable QR codes for URLs, Wi-Fi access, contacts, messages, locations, print, displays, and events. Use when choosing QR content, error correction, size, color, testing, or placement.
metadata:
  version: "1.0.0"
  openclaw: '{"emoji":"🔳"}'
---

## State location

This skill is stateless and stores no local configuration.

## Generate and deploy a QR code

1. Choose the payload type. Load `references/types.md` for Wi-Fi, vCard, email, SMS, and geo payload syntax.
2. Use the shortest stable payload that preserves the intended destination. For a changeable web destination, use a managed short URL or redirect that the owner controls.
3. Choose error correction for the design: L (about 7%) for clean, unbranded use; M (about 15%) for the usual default; Q (about 25%) when a logo reduces usable modules; H (about 30%) for higher damage tolerance.
4. Keep a quiet zone of at least four modules, use solid dark modules on a light background, and retain sufficient contrast for the target scanner and lighting.
5. Size the printed code for its scan distance. Start with approximately distance ÷ 10; validate the actual printed result rather than relying on a screen preview.
6. Test the final code with multiple current phone cameras in its intended lighting, at its actual size, and after any logo or styling changes.

## Deployment checks

- Confirm the destination is correct, accessible to the intended audience, and suitable for the QR code's location.
- If scanning is unreliable, first increase physical size, quiet-zone clearance, contrast, and module simplicity; then reduce payload density or raise error correction as needed.
- Load `references/deployment.md` for business, retail, event, signage, presentation, and review-collection placement patterns.
- Load `references/knowledge.md` when assessing QR design limits, sizing assumptions, error correction, or scanner reliability.

## Quick reference

| Reference file | Use when |
| --- | --- |
| `references/types.md` | Formatting a non-URL payload such as Wi-Fi, vCard, email, SMS, or geo. |
| `references/deployment.md` | Planning physical placement, timing, display duration, or context-specific rollout. |
| `references/knowledge.md` | Checking design, error-correction, quiet-zone, and scanning guidance. |
