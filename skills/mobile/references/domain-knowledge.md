# Mobile App Development Domain Knowledge

Verified primary sources that back the practices encoded in this skill.

## Platform conventions and SDKs

- **Apple Human Interface Guidelines — Designing for iOS** — navigation, touch targets, system gestures, and accessibility expectations via https://developer.apple.com/design/human-interface-guidelines/designing-for-ios
- **Apple — Supporting Universal Links** — owned-domain deep links and fallback behavior via https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app
- **Android Developers — App architecture overview** — lifecycle-aware components and layered architecture via https://developer.android.com/topic/architecture
- **Android Developers — Handle Android App Links** — verified deep links and web fallback via https://developer.android.com/training/app-links
- **Android Developers — Accessibility overview** — TalkBack, touch target sizing, and contrast expectations via https://developer.android.com/guide/topics/ui/accessibility

## Lifecycle, offline, and resource constraints

- **Apple — Preparing your UI to run in the background** — save/restore state and background execution limits via https://developer.apple.com/documentation/uikit/app_and_environment/scenes/preparing_your_ui_to_run_in_the_background
- **Android Developers — The activity lifecycle** — foreground/background transitions and state persistence via https://developer.android.com/guide/components/activities/activity-lifecycle
- **Android Developers — WorkManager overview** — deferrable background work under battery and OS constraints via https://developer.android.com/topic/libraries/architecture/workmanager
- **MDN — Offline Progressive Web Apps** — caching, sync, and offline-first product expectations via https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps/Guides/Offline_and_background_operation

## Store review and privacy baselines

- **Apple App Store Review Guidelines** — functional completeness, privacy disclosure, and reviewer access requirements via https://developer.apple.com/app-store/review/guidelines/
- **Google Play — Developer Policy Center** — Play distribution, permissions, and user-data policy expectations via https://play.google.com/about/developer-content-policy/

## Application in this skill

- Platform conventions in `references/mobile-development-guidelines.md` map to Apple HIG and Android accessibility/architecture guidance above.
- Offline-first, lifecycle, and background-work rules stay operational; the sources justify why mobile OS constraints require save-before-background and deferred work patterns.
- App Store survival guidance stays checklist-oriented; store policy URLs are the authority for review rejection categories.
