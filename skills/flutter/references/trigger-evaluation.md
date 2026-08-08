# Trigger-Scope Evaluation

Use this inventory for skill-maintenance reviews of the `flutter` description and activation boundary; ordinary Flutter tasks follow the main routing table.

The evaluated description activates for Flutter app work and routes React Native and native-only Swift/Kotlin work to their respective skills. Each result below is a review observation against that boundary, not a keyword-match rule.

| ID | Prompt | Expected activation | Observed result | Pass |
|---|---|---|---|---|
| P1 | "My Flutter `Column` overflows after I add a bottom sheet. How should I debug it?" | Activate: Flutter layout/debug task | Activated: Flutter, `Column`, and debugging are in scope. | true |
| P2 | "Design a Riverpod-backed Flutter checkout flow that restores a deep link after sign-in." | Activate: Flutter architecture/routing task | Activated: Flutter state management and routing are in scope. | true |
| N1 | "Fix this React Native FlatList performance regression." | Route to React Native: outside Flutter scope | Routed outside Flutter scope. | true |
| N2 | "Add a SwiftUI widget extension to my native iOS app." | Route to native Swift: outside Flutter scope | Routed outside Flutter scope. | true |

**Result:** 2/2 positive prompts activate and 2/2 near-miss prompts stay outside scope (4/4).
