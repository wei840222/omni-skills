# QA, Balance, and Launch Checklist

Use this checklist at every milestone gate.

## Functional QA

- Core loop can be completed and restarted repeatedly.
- Failure and success states are always recoverable.
- Input remains consistent across target devices.
- Save/load behavior matches design expectations.

## Performance QA

- Frame-time budget validated in representative scenes.
- Asset loading does not freeze critical interactions.
- Memory profile remains stable through long sessions (watch disposal / `renderer.info` when using Three.js).
- Mobile fallback mode remains playable.

## Balance QA

- Early game challenge curve avoids unfair spikes.
- Reward pacing aligns with desired session duration.
- Dominant strategy has at least one counter-pressure.
- New players and returning players both show progress.

## Launch gate

- Known critical issues are resolved or mitigated.
- Crash and error logging path is validated.
- Rollback plan exists for broken releases.
- Release notes communicate player-visible changes under `<state_root>/release-notes.md`.

## Post-launch rhythm

- Review analytics and player feedback at fixed cadence.
- Ship small balance updates before major feature jumps.
- Track regressions by milestone, not by anecdote.
