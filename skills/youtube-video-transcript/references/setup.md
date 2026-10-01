# Setup — YouTube Video Transcript

Read when `<state_root>/` is missing/empty, `yt-dlp` may be absent, or the user has not set cache preferences yet.

## Attitude

Offer reading-first access to video speech. Adapt to researcher, student, creator, or casual reader needs without blocking the first request behind setup questionnaires.

## Verify yt-dlp

```bash
command -v yt-dlp && yt-dlp --version
```

If missing, offer install help and wait for confirmation before installing:

- Homebrew: `brew install yt-dlp`
- pip: `pip install -U yt-dlp`
- Documented project: https://github.com/yt-dlp/yt-dlp

Re-check version after install. Prefer a current release; subtitle flag names (`--write-subs`, `--write-auto-subs`) differ from older `--write-sub` aliases.

## Priority order

1. **Immediate request first.** If the user already shared a URL, run metadata → list-subs → extract and answer before preference questions.
2. **Cache preference second.** After the first useful transcript: ask whether to save under `<state_root>/videos/`. Respect no.
3. **Light integration last.** Only when natural: remember preferred format (markdown/srt/text), timestamp density, or summary style in `<state_root>/memory.md`.

## What may be saved (consent required)

Write `<state_root>/memory.md` from `assets/memory-template.md` only after the user agrees to remember preferences or cache:

- preferred format: markdown / text / srt / vtt
- timestamp preference: always / sometimes / never
- summary style: brief / detailed / chapter-based
- caching_consent: yes / no / pending
- recent video index rows (id, title, date, path)

## First-run checklist

- [ ] `yt-dlp` present
- [ ] `<state_root>` resolved (or deferred until persist requested)
- [ ] First video answered without forcing setup
- [ ] Consent asked before any cache write
- [ ] User told the exact path if something was saved
