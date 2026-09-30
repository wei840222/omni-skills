# Scrape — Code Patterns

## robots.txt Check (Do First)

```python
from urllib.robotparser import RobotFileParser
from urllib.parse import urlparse

def can_scrape(url: str, user_agent: str = "*") -> bool:
    parsed = urlparse(url)
    robots_url = f"{parsed.scheme}://{parsed.netloc}/robots.txt"

    rp = RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
    except Exception:
        # Missing or unreadable robots.txt: treat as allowed but log the gap.
        return True
    return rp.can_fetch(user_agent, url)
```

## Session Setup

```python
import requests

def create_session(contact_email: str) -> requests.Session:
    session = requests.Session()
    session.headers.update({
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            f"Chrome/120.0.0.0 Safari/537.36 (contact: {contact_email})"
        ),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    })
    return session
```

## Rate-Limited Fetcher

```python
import time
import random
import logging

logger = logging.getLogger(__name__)

def fetch_politely(session, url, min_delay=2.0, max_retries=5):
    """Fetch with rate limiting, backoff, and audit logging."""

    for attempt in range(max_retries):
        delay = min_delay + random.uniform(0, 0.5)
        time.sleep(delay)

        response = session.get(url, timeout=30)

        logger.info("SCRAPE url=%s status=%s", url, response.status_code)

        remaining = response.headers.get("X-RateLimit-Remaining")
        if remaining and remaining.isdigit() and int(remaining) < 5:
            logger.warning("Rate limit low: %s remaining", remaining)
            time.sleep(10)

        if response.status_code == 429:
            retry_after = response.headers.get("Retry-After", "60")
            wait = int(retry_after) if str(retry_after).isdigit() else 60
            logger.warning("429 received, waiting %ss", wait)
            time.sleep(wait)
            continue

        # Success or non-429 client error: return (caller decides on 4xx).
        if response.status_code < 500:
            return response

        wait = min(2 ** attempt + random.uniform(0, 1), 60)
        logger.warning("5xx error, retry in %.1fs", wait)
        time.sleep(wait)

    raise RuntimeError(f"Failed after {max_retries} retries: {url}")
```

## Full Example

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

contact = "operator@example.com"
target = "https://example.com/products"

if not can_scrape(target, user_agent="*"):
    raise SystemExit("Blocked by robots.txt")

session = create_session(contact)
response = fetch_politely(session, target)
print(f"Got {len(response.text)} bytes status={response.status_code}")
```

## Notes

- Prefer site APIs when they cover the job.
- Do not add cookie jars from authenticated sessions unless the user authorized that surface.
- For JS-rendered DOM extraction, hand off to `playwright` or `puppeteer` rather than stretching `requests`.
