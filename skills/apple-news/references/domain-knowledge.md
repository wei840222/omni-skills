# Domain Knowledge: Apple News

Apple News is Apple's curated news reader for Apple platforms. On macOS, this skill treats **News.app** and `https://apple.news/...` links as the primary deterministic interfaces.

## Product facts agents should preserve

- News.app ships at `/System/Applications/News.app` on current macOS releases.
- Direct article/channel opens should prefer Apple News URLs (`https://apple.news/...`) over guessed custom URL schemes.
- Topic discovery that is not backed by a concrete Apple News link should stay explicit: use a user-owned Shortcut only when configured, otherwise ask for one source or one reference link.
- Bulk opens are high-impact: confirm count before launching more than one link.

## Verifiable sources used in this refactor

- Apple Support — Get started with Apple News: https://support.apple.com/guide/iphone/get-started-with-apple-news-iph3c3b7b8c4/ios
- Apple Support — Read news stories: https://support.apple.com/guide/iphone/read-news-stories-iph2f4c4f8f4/ios
- Apple News Format documentation (publisher packaging context): https://developer.apple.com/documentation/apple_news
- Apple News Format Guide PDF: https://www.apple.com/ca/apple-news/docs/Apple-News-Format.pdf

These sources support product orientation and publisher packaging context. Local launch/read automation in this skill still depends on macOS `open` / Shortcut paths, not Apple News Format publishing APIs.
