# Official Sources & Platform References

This document records official resources and platform specifications for Udio AI music generation.

## Official Platform Resources

- **Udio Official Portal**: [https://www.udio.com/](https://www.udio.com/)
  - Direct web interface for music generation, track extension, remixing, and community library sharing.

## Audio Architecture & Sizing Conventions

- **Model Engine**:
  - Udio v1 / v1.5 audio synthesis engine: Supports high-fidelity stereo generation across diverse musical genres and vocal styles.
- **Generation & Extension Windows**:
  - Initial generation: 32-second high-fidelity audio chunks.
  - Extension chaining: Add introductory sections, outro fade-outs, or extend mid-track by appending 32-second extensions forward or backward in time.
- **Stem Extraction & Advanced Workflows**:
  - Stem separation (isolated vocal, bass, drum, and instrumental tracks) supported for downstream DAW editing and mixing.
