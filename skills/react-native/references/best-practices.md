# React Native Development Rules

## Component Performance
- `FlatList` for any list over 10 items — `ScrollView` with `map` loads everything in memory, FlatList virtualizes
- `keyExtractor` must return stable unique strings — using index causes bugs on reorder and deletion
- `React.memo` prevents re-renders when props unchanged — wrap pure display components
- `useCallback` for functions passed to child components — new function reference triggers child re-render
- Extract styles to `StyleSheet.create` outside the component body — inline styles create new objects every render

## State Management
- Rely on `useState` for simple component-local state (like toggles) instead of adding Redux/Zustand
- Lift state to lowest common ancestor only — higher causes unnecessary re-renders
- Reserve `useMemo` specifically for computationally expensive operations to minimize caching overhead
- Context re-renders all consumers on any change — split contexts by update frequency
- Compute derived data during render from the source state rather than storing it in state variables

## Navigation
- React Navigation is the standard — Expo Router for file-based routing in Expo projects
- Stack screens stay mounted by default — clean up subscriptions and timers in `useEffect` cleanup
- Pass serializable params only — functions and complex objects break deep linking and state persistence
- `useFocusEffect` for screen-specific side effects — runs on focus, not just mount
- `navigation.reset` for auth flows — clears back stack, prevents returning to login after sign-in

## Styling
- `StyleSheet.create` outside component body — creates styles once, not every render
- Flexbox defaults differ from web — `flexDirection: 'column'`, no `display: flex` needed
- Translate design tool dimensions into density-independent pixels for accurate rendering
- `Platform.select` for platform-specific styles — cleaner than conditionals in style objects
- Explicitly style each `Text` component independently, as React Native lacks CSS inheritance and cascading

## Native Modules
- Utilize Expo modules for common features (camera, location, notifications) to maintain a managed workflow
- `expo-dev-client` enables native modules without full eject — best of both worlds
- React Native New Architecture (Fabric, TurboModules) is opt-in — check library compatibility before enabling
- Inspect Xcode or Android Studio logs directly to diagnose native crashes, as they bypass the JS debugger

## Performance Debugging
- Hermes engine should be enabled — significantly faster startup and lower memory
- `InteractionManager.runAfterInteractions` defers heavy work — keeps animations smooth
- `useNativeDriver: true` for animations — runs on UI thread, not JS thread
- `console.log` in production kills performance — remove or use `__DEV__` guard
- Flipper for debugging — network, layout, performance profiling

## Images
- Use `resizeMode` appropriately — `cover` crops, `contain` letterboxes, `stretch` distorts
- Prefetch images for smooth UX: `Image.prefetch(url)` before displaying
- Local images need explicit dimensions — remote images can use aspect ratio if one dimension set
- SVGs via `react-native-svg` — better scaling than PNGs for icons
- Cache remote images with `react-native-fast-image` — default Image has no persistent cache

## Common Mistakes
- `async` in `useEffect` directly — must define async function inside, then call it
- Missing `key` warnings in lists — always use unique, stable keys
- Account for the absence of the DOM and CSS by adapting web React patterns to the native event system and components
- Forgetting cleanup in `useEffect` — subscriptions, timers, listeners leak without cleanup return
- Testing only on one platform — iOS and Android differ in behavior, test both regularly

## Platform Differences
- Android needs explicit `overflow: 'hidden'` for border radius clipping — iOS clips by default
- Shadows: iOS uses `shadow*` props, Android uses `elevation`
- StatusBar behavior differs — test visibility and color on both platforms
- Back button is Android-only — handle with `BackHandler` or navigation listeners
- Push notifications setup differs significantly — platform-specific configuration required

## Build & Release
- `npx react-native clean` for unexplained build failures — clears caches and derived data
- iOS: `cd ios && pod install` after adding native dependencies — often forgotten step
- Android: `cd android && ./gradlew clean` for stubborn build issues
- EAS Build (Expo) simplifies CI/CD — handles signing, versioning, submission
- Test release builds locally before submitting — development and production behavior differ
