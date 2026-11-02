# The Fastest Python Scraper for RAG? (Crawl4AI)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `BpsRH-1TZk4` · [watch](https://youtu.be/BpsRH-1TZk4) · **date:** 2026-03-02 · **length:** 6:23 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Better Stack
- **topics:** rag-retrieval, data-engineering · **tags:** web-scraping, crawl4ai, rag-ingestion, playwright, structured-extraction, llm-extraction, async-crawling, resumable-crawl, prefetch, markdown-output

> Better Stack walkthrough of Crawl4AI, a Python crawler that returns clean Markdown/JSON for LLM pipelines, with prefetch mode, resumable deep crawls and schema-based LLM extraction; the "fastest" claim is stated but not measured on screen.

## Summary
The presenter argues that web scraping for RAG is mostly a cleaning problem, and presents Crawl4AI as a crawler built for LLM inputs. A basic async crawl of a tech news page returns cleaned Markdown and JSON with headings and links preserved, with JavaScript handled through Playwright. Prefetch mode skips full rendering and only collects links, which the presenter shows on Hacker News and recommends for aggregators and large URL sets. For production, a BFS deep crawl saves resume state to JSON through a state-change callback, so a killed process restarts where it stopped. Semantic extraction defines a Pydantic schema (job title, company, salary) and an LLM extraction strategy with an instruction and provider, demonstrated on Indeed job listings. Tradeoffs named are Python-only, the need for API keys or local models such as Ollama for LLM features, and rate limits. The comparison covers Scrapy (rule-based, boilerplate-heavy), BeautifulSoup (parser only) and Selenium (slower, manual async). The video is a short demo-level review; speed claims are asserted rather than benchmarked.

## Key ideas
- **For RAG the hard part of scraping is cleaning messy web data, not fetching it; Crawl4AI returns clean Markdown or structured JSON with headings and links preserved.** — Presenter contrasts it with crawlers that return raw HTML. Pages are fetched, parsed, noise removed and content ranked before output, so no custom cleaning script is needed for a news summarizer or RAG prototype. ([0:00](https://youtu.be/BpsRH-1TZk4?t=0))
- **Crawl4AI handles JavaScript via Playwright and runs async so it scales to many URLs.** — Presenter says it wraps Playwright internally and exposes an async API, positioning it against Selenium which he calls slower with manual async handling. ([0:00](https://youtu.be/BpsRH-1TZk4?t=0))
- **Prefetch mode is a cheap link-discovery pass: it fetches links without full rendering, so you find targets first and extract later.** — Demonstrated on Hacker News with prefetch set to true; presenter says it was very fast. He frames the saving as scaling with hundreds or thousands of URLs. No timing is shown on screen. ([1:05](https://youtu.be/BpsRH-1TZk4?t=65))
- **Deep crawls can be made crash-safe by persisting resume state, not by restarting.** — A BFS deep crawl defines resume state and an on-state-change callback that writes JSON. The presenter kills the process mid-crawl and reruns it, and the crawl continues from the saved state. He argues this matters for large RAG knowledge bases where a restart is expensive. ([2:52](https://youtu.be/BpsRH-1TZk4?t=172))
- **Semantic extraction: define a Pydantic schema and let an LLM map the converted page onto it instead of parsing text.** — Schema fields are job title, company and salary, used with an LLM extraction strategy that takes an instruction and a provider. Pipeline is page to Markdown or JSON, then model to schema, demonstrated on Indeed job listings with clean structured output. ([2:52](https://youtu.be/BpsRH-1TZk4?t=172))
- **Tradeoffs: Python-only, LLM features need API keys unless you run a local model such as Ollama, and crawling can still hit rate limits.** — Presenter also notes the open-source project is moving fast, so expect updates. He frames it as strongest for AI-focused developers building RAG pipelines. ([3:56](https://youtu.be/BpsRH-1TZk4?t=236))
- **Positioning: Scrapy is good for large static rule-based crawls but needs boilerplate and custom LLM layers; BeautifulSoup is only a parser; Selenium renders JS but is slow and manual.** — Crawl4AI is presented as the option with built-in LLM extraction on Markdown output, a crawling engine and rendering in one package. Comparison is qualitative and the presenter says traditional rule-based crawlers remain fine for static data. ([5:03](https://youtu.be/BpsRH-1TZk4?t=303))

## Techniques
- **Basic async crawl to Markdown or JSON** — Import the async web crawler class from Crawl4AI (the presenter says he took the code from the repo and docs and tweaked a few lines), call run on the target URL, and use the returned Markdown or JSON directly as model input. Install with pip install crawl4ai (install step as described by the presenter: a plain pip install). No config values or exact class names beyond the async web crawler and run call were shown on screen. *When:* Feeding web pages into a news summarizer or RAG prototype without writing HTML cleaning code.
- **Prefetch for link discovery, then selective extraction** — Set the prefetch option to true on the same crawler config so the run fetches links asynchronously without rendering every page. Use the discovered links to choose which pages to fully extract in a second pass. *When:* Aggregators or large crawls where you need the URL list first and only want to pay full rendering cost for the subset you keep.
- **Resumable BFS deep crawl** — Use the BFS deep crawl strategy, define a resume state, and attach an on-state-change callback that persists state to a JSON file. After a crash or kill, rerun the crawl; it loads the saved JSON state and continues without restarting. *When:* Long crawls that build a RAG knowledge base where a crash would otherwise repeat expensive fetches.
- **Schema-driven LLM extraction** — Define the target record as a Pydantic model (example fields: job title, company, salary). Configure the LLM extraction strategy with a natural-language instruction and a provider. Crawl4AI converts the page to Markdown or JSON, sends it to the model with the schema, and returns structured fields. Provider or model name not stated in the video. *When:* Pulling typed fields from pages that are hard to parse with selectors, such as job listings, where the content is semi-structured.

## Numbers
- Crawl4AI described as up to 6x faster than traditional Python scrapers such as Scrapy; presenter attributes this to benchmarks that are not shown on screen ([0:00](https://youtu.be/BpsRH-1TZk4?t=0))
- Same '6x in benchmarks' claim repeated in the pros summary ([3:56](https://youtu.be/BpsRH-1TZk4?t=236))
- Prefetch run on Hacker News described as very fast; no timing or URL count shown ([1:05](https://youtu.be/BpsRH-1TZk4?t=65))

## Hot takes
- The 'fastest Python scraper' title and the 6x speed claim are not backed by any benchmark shown in the video.
- Prefetch speed is judged from a single Hacker News run, and the scaling argument for thousands of URLs is untested here.
- Comparisons with Scrapy, BeautifulSoup and Selenium are qualitative and made without measurement.
- Presenter calls LLM extraction a completely different level of capability, but the extraction demo shows one site and no accuracy check.

## Tools mentioned
Crawl4AI, Playwright, Pydantic, Ollama, Scrapy, BeautifulSoup, Selenium, pip

## Relevance to our work
- **agentos** (1/3): Web sources are not a stated AgentOS input, but a clean-Markdown crawler with schema extraction could feed MemoryMesh knowledge buckets if web content is ever ingested. → *If web ingestion is planned for MemoryMesh buckets, run Crawl4AI on three sample pages and compare its Markdown and schema-extracted fields against the current loader on cleanliness and token count.*
