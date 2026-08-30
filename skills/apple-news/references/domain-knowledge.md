# Domain knowledge: Apple News

Apple News is Apple's news app. This skill automates only local macOS launches, Apple News URL handoff, and user-owned Shortcuts; it does not use Apple News publisher APIs.

## Product constraints

- Apple documents News.app use on Mac, including News+ actions in its sidebar.
- Apple News and News+ availability varies by country, region, and device.
- The App Store describes Apple News as a curated and personalized news app; it does not establish a supported command-line or AppleScript automation API.
- Treat `https://apple.news/...` URLs as the only article-link format this skill accepts. The registered macOS URL handler determines which app receives the link.

## Sources

- **Apple Support — Subscribe to Apple News+ on your iPhone, iPad, and Mac:** https://support.apple.com/en-us/102209
  Documents News.app use on Mac and regional availability.
- **Apple App Store — Apple News:** https://apps.apple.com/us/app/apple-news/id1066498020
  Describes Apple News' app scope, privacy claims, and availability caveat.
- **Apple Developer — Apple News Format:** https://developer.apple.com/documentation/apple_news
  Publisher packaging reference; outside this skill's local launch workflow.
