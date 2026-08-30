# Puppeteer Domain Knowledge

## Headless Browser Architecture
A headless browser is a web browser without a graphical user interface. Headless browsers provide automated control of a web page in an environment similar to popular web browsers, but are executed via a command-line interface or using network communication.
Puppeteer is a Node.js library which provides a high-level API to control headless Chrome or Chromium over the DevTools Protocol. It can also be configured to use full (non-headless) Chrome or Chromium.

## Core Capabilities
- Generate screenshots and PDFs of pages.
- Crawl a SPA (Single-Page Application) and generate pre-rendered content (i.e. "SSR" (Server-Side Rendering)).
- Automate form submission, UI testing, keyboard input, etc.
- Create an up-to-date, automated testing environment. Run your tests directly in the latest version of Chrome using the latest JavaScript and browser features.
- Capture a timeline trace of your site to help diagnose performance issues.
- Test Chrome Extensions.

## Integration & Alternatives
Playwright is a popular alternative maintained by Microsoft that supports cross-browser automation out-of-the-box, but Puppeteer remains closely tied to the Chrome/Chromium ecosystem with deep DevTools Protocol access.

## Verified Sources (Gate 6)
- Puppeteer official documentation — overview, API, and headless Chrome control: https://pptr.dev/
- Puppeteer GitHub repository — releases, issues, and DevTools Protocol integration: https://github.com/puppeteer/puppeteer
- Chrome for Testing / ChromeDriver ecosystem notes via Chromium docs — browser binaries used by automation: https://developer.chrome.com/docs/chromedriver
- Playwright comparison context — cross-browser alternative maintained by Microsoft: https://playwright.dev/
