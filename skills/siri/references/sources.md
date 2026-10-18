# Siri skill sources

Verified against live Apple documentation on 2026-10-19. Prefer these URLs when
refreshing activation, HomeKit naming, Shortcuts, or App Intents guidance.

## Official product / support

- [Use Siri on all your Apple devices](https://support.apple.com/en-us/HT204389)
- [iPhone User Guide — Use Siri](https://support.apple.com/guide/iphone/use-siri-iph3abbfb82a/ios)
- [iPhone User Guide — Control Home accessories](https://support.apple.com/guide/iphone/control-home-accessories-iph0d0e4e1f3/ios)
- [HomePod User Guide](https://support.apple.com/guide/homepod/welcome/homepod)
- [Shortcuts User Guide](https://support.apple.com/guide/shortcuts/welcome/ios)
- [Create a Shortcut](https://support.apple.com/en-us/HT209055)

## Official developer

- [App Intents](https://developer.apple.com/documentation/appintents)
- [AppIntent protocol](https://developer.apple.com/documentation/appintents/appintent)
- [SiriKit](https://developer.apple.com/documentation/sirikit)
- [HomeKit](https://developer.apple.com/documentation/homekit)
- [WWDC22: Implement App Shortcuts with App Intents](https://developer.apple.com/videos/play/wwdc2022/10032/)

## Claim checklist (2026-10-19)

| Claim in skill | Source support |
|----------------|----------------|
| "Hey Siri" / Listen for settings and retraining | HT204389, iPhone Use Siri guide |
| "Siri" alone on newer iOS Listen-for options | HT204389 / iPhone Use Siri guide |
| Home accessories controllable via Siri / Home app | iPhone Control Home accessories guide, HomeKit docs |
| Shortcuts run by voice with short names | Shortcuts User Guide, HT209055 |
| App Intents are the modern code-first Siri path (iOS 16+) | App Intents docs, WWDC22 10032 |
| Classic SiriKit remains domain-extension based | SiriKit docs |

Refresh this file when Apple changes Listen-for labels, Home security prompts,
or App Intents APIs. Do not invent pricing, hardware SKUs, or unreleased OS
behavior.
