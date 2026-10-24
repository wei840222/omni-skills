---
name: vr
description: "Configure VR hardware and optimize virtual reality experiences. Use when setting up PC VR and standalone headsets (Quest/Index/PSVR), troubleshooting tracking or display stutter, optimizing comfort, or selecting VR software."
metadata:
  openclaw: '{"emoji":"🥽","displayName":"VR"}'
  related-skills: '{"fitness": "Hand off when the user wants workout planning, sweat/recovery routines, or training load beyond headset-specific VR fitness tips.", "games": "Hand off when the user wants broader game discovery outside VR-native titles and platforms.", "mobile": "Hand off when phone or tablet workflows matter more than headset play-space setup.", "unreal-engine": "Hand off when the user is building Unreal XR/VR projects beyond headset setup guidance."}'
---

# VR Skill

This skill helps set up VR headsets, troubleshoot common issues, optimize comfort, and recommend experiences by use case. Trigger this skill when users ask about purchasing a VR headset, setting up a play space, fixing PC VR or standalone headset issues, overcoming motion sickness, or finding specific types of VR content.

## Before Recommending Headsets

- Ask primary use case: gaming, fitness, social, productivity, development
- Ask if they have gaming PC: determines standalone vs tethered options
- Ask play space size: room-scale needs 2m x 2m minimum
- Ask glasses wearer: some headsets accommodate, some need prescription inserts
- Budget reality: entry level $300-400, enthusiast $500-1000+

## References

Load the following references on demand based on the user's explicit needs:

| Reference | When to Load |
| --------- | ------------ |
| `references/headset-landscape.md` | When recommending a headset based on budget or specs. |
| `references/setup-and-comfort.md` | When helping a user set up a space, prevent motion sickness, or optimize physical comfort. |
| `references/use-cases.md` | When asked about fitness, social, development, or content recommendations. |
| `references/troubleshooting.md` | When troubleshooting PC VR issues, link cables, or common hardware issues (blurry, drift, fogging). |
