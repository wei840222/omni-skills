# Domain Knowledge - multi-engine-web-search

## Search Engines

Use an engine appropriate to the query and the user's region. Replace `{keyword}` with URL-encoded query text.

### Global and privacy-focused engines

| Engine | URL |
|---|---|
| Google | `https://www.google.com/search?q={keyword}` |
| Google HK | `https://www.google.com.hk/search?q={keyword}` |
| Bing | `https://www.bing.com/search?q={keyword}` |
| Yahoo | `https://search.yahoo.com/search?p={keyword}` |
| DuckDuckGo | `https://duckduckgo.com/html/?q={keyword}` |
| Brave | `https://search.brave.com/search?q={keyword}` |
| Startpage | `https://www.startpage.com/sp/search?query={keyword}` |
| Qwant | `https://www.qwant.com/?q={keyword}` |
| Ecosia | `https://www.ecosia.org/search?q={keyword}` |
| Mojeek | `https://www.mojeek.com/search?q={keyword}` |
| Swisscows | `https://swisscows.com/web?query={keyword}` |
| AOL Search | `https://search.aol.com/aol/search?q={keyword}` |

### Regional engines

| Engine | URL |
|---|---|
| Baidu | `https://www.baidu.com/s?wd={keyword}` |
| Bing CN | `https://cn.bing.com/search?q={keyword}&ensearch=0` |
| Bing INT (CN endpoint) | `https://cn.bing.com/search?q={keyword}&ensearch=1` |
| Sogou | `https://www.sogou.com/web?query={keyword}` |
| 360 Search | `https://www.so.com/s?q={keyword}` |
| Yandex | `https://yandex.com/search/?text={keyword}` |
| Naver | `https://search.naver.com/search.naver?query={keyword}` |
| Seznam | `https://search.seznam.cz/?q={keyword}` |
| CocCoc | `https://coccoc.com/search?query={keyword}` |

### Knowledge and developer engines

| Engine | URL |
|---|---|
| WolframAlpha | `https://www.wolframalpha.com/input?i={keyword}` |
| Wikipedia | `https://en.wikipedia.org/w/index.php?search={keyword}` |
| GitHub Search | `https://github.com/search?q={keyword}` |
| Stack Overflow Search | `https://stackoverflow.com/search?q={keyword}` |
| Semantic Scholar | `https://www.semanticscholar.org/search?q={keyword}` |
| PubMed | `https://pubmed.ncbi.nlm.nih.gov/?term={keyword}` |

## Query Patterns

| Need | Pattern |
|---|---|
| Limit to one domain | `site:arxiv.org agentic ai` |
| Find a format | `filetype:pdf model card` |
| Match an exact phrase | `"context window"` |
| Exclude a noisy term | `python -snake` |
| Compare alternatives | `llama OR mistral` |
| Search titles or URLs | `intitle:benchmark llm`, `inurl:docs authentication` |
| Bound a date range | `ai act after:2025-01-01 before:2026-03-01` |
| Google recent window | `tbs=qdr:h`, `tbs=qdr:d`, or `tbs=qdr:w` |

## Reference

Read `references/sources.md` when validating query operators, date filters, or evidence-quality guidance.

## Evidence Quality

Treat results as discovery leads, then verify them before relying on them. Count repeated syndicated articles as one evidence trail. For high-impact decisions, add a contradiction query and cite the primary material that resolves it. For rapidly changing topics, state both the source publication date and the event date when they differ.

## External Data

Queries are sent to the selected public search engine or specialist endpoint. Use the minimum query text needed for the research task, and keep credentials, personal data, and private identifiers out of queries.
