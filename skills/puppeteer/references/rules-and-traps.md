# Rules and Traps

## Core Rules
### 1. Always Wait Before Acting
Always wait for the element before clicking or typing after navigation:
```javascript
await page.waitForSelector('#button');
await page.click('#button');
```
Waiting for elements prevents "element not found" errors.

### 2. Use Specific Selectors
Prefer stable selectors in this order:
1. `[data-testid="submit"]` — test attributes (most stable)
2. `#unique-id` — IDs
3. `form button[type="submit"]` — semantic combinations
4. `.class-name` — classes (least stable, changes often)

Use stable selectors to prevent breakage on DOM changes (e.g., `[data-testid="submit"]` instead of `div > div > div > button`).

### 3. Handle Navigation Explicitly
After clicks that navigate, wait for navigation:
```javascript
await Promise.all([
  page.waitForNavigation(),
  page.click('a.next-page')
]);
```
Without this, the script continues before the new page loads.

### 4. Set Realistic Viewport
Always set viewport for consistent rendering:
```javascript
await page.setViewport({ width: 1280, height: 800 });
```
Default viewport is 800x600 — many sites render differently or show mobile views.

### 5. Handle Popups and Dialogs
Dismiss dialogs before they block interaction:
```javascript
page.on('dialog', async dialog => {
  await dialog.dismiss(); // or dialog.accept()
});
```
Handle dialogs to allow the script to continue without freezing.

### 6. Close Browser on Errors
Always wrap in try/finally:
```javascript
const browser = await puppeteer.launch();
try {
  // ... automation code
} finally {
  await browser.close();
}
```
Closing the browser on errors prevents leaked processes from consuming memory and ports.

### 7. Respect Rate Limits
Add delays between requests to avoid blocks:
```javascript
await page.waitForTimeout(1000 + Math.random() * 2000);
```
Respect rate limits to prevent triggering CAPTCHAs and IP bans.

## Common Traps
- `page.click()` on invisible element → fails silently, use `waitForSelector` with `visible: true`
- Screenshots of elements off-screen → blank image, scroll into view first
- `page.evaluate()` returns undefined → cannot return DOM nodes, only serializable data
- Headless blocked by site → use `headless: 'new'` or set user agent
- Form submit reloads page → `page.waitForNavigation()` or data is lost
- Shadow DOM elements invisible to selectors → use `page.evaluateHandle()` to pierce shadow roots
- Cookies not persisting → launch with `userDataDir` for session persistence