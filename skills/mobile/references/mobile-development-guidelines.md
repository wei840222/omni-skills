# Mobile Development Guidelines

## Lifecycle Awareness

- App can be killed anytime in background—save state before backgrounding
- Restore state on return—user expects to continue where they left off
- Handle low memory warnings—release caches, non-essential resources
- Background tasks have time limits—complete or request extension

## Permissions

- Ask in context, not at launch—explain why when requesting
- Degrade gracefully if denied—app should still work with reduced features
- Request only necessary permissions—users notice and distrust
- Re-request after demonstrating value—wait until a relevant action occurs

## Offline First

- Assume network is unreliable—design for offline, sync when possible
- Cache aggressively—previous content better than loading spinner
- Queue actions for retry—ensure continued functionality during network errors
- Conflict resolution strategy—last write wins or manual merge
- Show sync status—user should know if data is current

## Performance

- Target 60fps—dropped frames feel janky
- Main thread for UI only—heavy work on background threads
- Memory matters more than desktop—constrained devices, aggressive OS killing
- Battery awareness—reduce location polling, network requests when possible
- Startup time under 2 seconds—first impression matters

## Navigation Patterns

- Follow platform conventions—iOS back gesture, Android back button
- Navigation stack manageable—keep the stack shallow and manageable
- Deep link to any screen—shareable, notification taps work
- Preserve scroll position on return—maintain the previous position

## Notifications

- Push for time-sensitive external events—new message, delivery update
- Local for reminders, timers—user-initiated
- Send notifications thoughtfully—users will disable; quality over quantity
- Actionable when possible—reply, mark done from notification
- Group related notifications—less intrusive

## Deep Linking

- Universal Links (iOS) / App Links (Android) for owned domains
- Handle gracefully when app not installed—fallback to web
- Parse parameters safely—malicious links exist
- Test all entry points—not just main launch

## Storage

- Secure storage for tokens, credentials—Keychain, Keystore
- User data survives reinstall where appropriate—cloud backup
- Cache is cache—can be cleared; avoid storing critical data here
- Large files: consider on-demand download—instead of bundling them in the app

## Input Handling

- Keyboard avoidance—content shifts to stay visible
- Dismiss keyboard appropriately—tap outside, scroll, submit
- Input accessories for relevant actions—next field, done, toolbar
- Paste, autofill support—reduce typing on small keyboards

## Touch and Gestures

- 44pt minimum touch target—consistent with platform guidelines
- System gestures reserved—reserve edge swipes for the system
- Gesture discoverability—provide an onboarding hint or teachable moment for non-obvious gestures
- Haptic feedback for significant actions—confirmation, errors

## Accessibility

- VoiceOver (iOS) / TalkBack (Android) testing—navigate entire app
- Dynamic type support—text scales with user preference
- Sufficient contrast—check in accessibility inspector
- Labels on all interactive elements—include accessible names for icon-only controls

## Testing

- Real devices essential—simulators miss performance, sensors, edge cases
- Multiple OS versions—support at least current minus 2
- Different screen sizes—small phones to tablets
- Network conditions—slow, intermittent, offline

## App Store Survival

- Read rejection reasons before submitting—common pitfalls documented
- Privacy policy required—explain data collection
- Login test account for reviewers—if auth required
- No placeholder content—everything functional in review build
- Update regularly—abandoned apps get deprioritized
