# Google Scholar domain rules

Runtime guidance for query construction, filters, result reading, full-text access,
citation trails, and common failure modes. Prefer official Scholar Help wording when
UI labels matter; re-open `sources.md` URLs if product copy drifts.

## Query construction

- Exact phrases in quotes: `"machine learning"` matches the phrase, not separate words.
- Exclude terms with minus: `neural networks -deep` drops many deep-learning hits.
- `OR` for alternatives must be uppercase: `"global warming" OR "climate change"`.
- Author operator: `author:"d knuth"` or `author:"donald e knuth"` (Scholar Help).
- Title search: put the paper title in quotations, e.g. `"A History of the China Sea"`.
- Publication / source field: use Advanced search (side drawer) for publication limits,
  or patterns such as `source:"Nature"` when the UI/operator still applies.
- `intitle:` can force a term into the title when broad keyword noise is high
  (treat as a common web-style aid; confirm on live UI if results look wrong).
- Advanced search (side drawer): author, title, publication fields and date limits.

## Time filters and alerts

- Results are normally sorted by **relevance**, not date (Scholar Search Help).
- **Since Year** (left sidebar): only recently published papers, still relevance-ranked —
  often better than pure date sort for “recent but important.”
- **Sort by date**: newest additions first; use when watching the frontier, not when
  you need the most cited foundations.
- On small screens, year controls may sit in the **Year** dropdown under the search button.
- Envelope / email alerts: deliver new results periodically for a saved query.
- “Since 2023” vs “Since 2020” style windows trade vetting time against novelty; pick
  explicitly for the user’s risk tolerance.

## Understanding results

- Ranking aims to weigh full text (when available), venue, authors, and how often /
  how recently the work is cited (About Google Scholar) — still opaque in detail.
- Citation count ≈ influence proxy, **not** quality or correctness.
- **Cited by**: forward citation trail; newer citing works are often more specific.
- **Related articles**: similar documents to the selected result.
- **All versions** / version count: preprints, publisher copies, repositories.
- Quotation marks in snippets highlight exact matches — still verify before citing.
- If results are too narrow, read **References** in a hit for more general works.
- If results are too basic, open **Cited by** for more specific follow-ons.
- Secondary sources (e.g. Wikipedia terminology) can supply better Scholar keywords.

## Finding full text

- Abstracts are often free; full text may need subscription (Scholar Help).
- Try, in order of legitimacy:
  1. Library link (e.g. FindIt@Harvard) when shown
  2. **[PDF]** / **[HTML]** access links to the right of the result
  3. **All versions** for alternate hosts and repositories
  4. **Related articles** / **Cited by** for substitutes if the exact PDF is closed
  5. Author request, institutional repository, or known open preprint servers
- Campus network: access links can include the library’s subscriptions automatically.
- Off-campus: Scholar may reuse recorded campus subscriptions for the same access links
  after an on-campus visit (see official Access help); library proxy/VPN remains valid.
- `filetype:pdf` can surface direct PDFs but is noisy — not a substitute for versions/library.
- Do **not** recommend pirate shadow libraries or credential sharing.

## Citation analysis and profiles

- Author profiles can show publications, who cites them, graphs, and automatic metrics.
- h-index and similar metrics on profiles measure productivity/impact proxies only.
- **Cited by** sorted usefully surfaces influential forward citations — still read them.
- Review papers accumulate citations heavily; self-citations can inflate counts.
- Recent citations matter more for living debates; old habit citations less so.
- Profile hygiene: wrong articles get attached to similar names — authors must curate.
- Manually added profile articles may lag before citations appear (Profiles help).

## Alerts, library, export

- Create alerts for search terms to email new matches.
- Follow public author profiles for ongoing work when relevant.
- **Cite** export targets common managers (BibTeX, EndNote, RefMan, etc.).
- Saving to Scholar library needs a Google account — optional; do not require it for advice.
- Keep personal library contents and account state out of this skill package.

## Coverage and limitations

- Indexes articles, theses, books, abstracts, court opinions, and other scholarly literature
  from publishers, societies, repositories, universities, and the web (About).
- Coverage is uneven: English/STEM bias is widely reported; humanities and non-English
  work can be underrepresented relative to specialist indexes.
- **No quality gate**: predatory and low-quality venues can appear (public criticism; treat as risk).
- Older / pre-digital material may be missing or incomplete.
- Metadata-oriented retrieval is common; do not assume reliable full-text search of every PDF.
- Ranking details are not fully disclosed — explain uncertainty instead of inventing weights.
- Court opinions: use **Case law** mode; jurisdiction filters via **Select courts**. Informational only.

## Evaluating sources

- Journal reputation / impact factor ≈ venue prestige guide, not paper-level truth.
- Preprints lack peer review — fast but preliminary; label them.
- Conference vs journal norms differ by field (e.g. CS vs medicine).
- Check for retractions, expressions of concern, and corrections before high-stakes cites.
- Theses/dissertations = gray literature — useful, cite cautiously.
- Prefer primary papers over blog restatements of the same claim.

## Search strategies

1. Start broad enough not to miss the cluster, then narrow with operators and year filters.
2. Pair Scholar with domain databases (PubMed, IEEE Xplore, ACM DL, SSRN, etc.) when the field has a canonical index.
3. Snowball: one good paper → references + Cited by + Related articles + author list.
4. Use review / survey papers for map-making, then drop to primary studies.
5. Run synonym and spelling variants; terminology drifts across disciplines.
6. For law: Case law option + court selection; never present hits as legal advice.
7. For author lookup: `author:` plus affiliation/topic keywords; verify identity on profiles.

## Common mistakes

- Treating citation count as quality
- Ignoring publication date in fast-moving fields
- Stopping at the first result page
- Citing from the abstract without methods/limitations
- Missing free preprint/repository versions
- Skipping retraction checks
- Using Sort by date when Since Year + relevance is more appropriate
- Forcing Scholar when PubMed/MeSH or a subject database is the right primary tool
- Storing library credentials or bulk-scraping PDFs in automation

## Delivery shape (agent)

When answering from this skill:

1. Give the recommended query string(s) and filter settings first.
2. State what each top strategy optimizes (recall, recency, author precision).
3. List caveats: access walls, predatory risk, preprint status, law disclaimer if needed.
4. Offer the next expansion move (Cited by / Related / field database) instead of dumping every table.
