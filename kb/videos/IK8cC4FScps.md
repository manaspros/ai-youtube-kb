# Building AI Agents with Real-Time Web Data — Yohan Raju, Bright Data

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `IK8cC4FScps` · [watch](https://youtu.be/IK8cC4FScps) · **date:** 2026-10-12 · **length:** 27:29 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Yohan Raju · **orgs:** Bright Data
- **topics:** mcp-and-tools, rag-retrieval, data-engineering · **tags:** web-scraping, live-web-data, mcp, anti-bot, real-time-search, browser-automation, bright-data, product-intelligence, job-data, medallion-architecture, vendor-pitch

> Bright Data's Yohan Raju argues that live web data (scrapers, anti-bot handling, and an MCP endpoint with 60+ tools) lets AI agents answer questions that pre-indexed RAG cannot, then demos an Amazon-plus-Reddit buy/no-buy agent.

## Summary
The speaker, a solutions architect at Bright Data, frames traditional web scraping as a maintenance problem: each target site needs its own scraper, which takes days to build and breaks whenever selectors or anti-bot defenses change. He contrasts this with agents that can discover sites and use managed tools, and he splits AI answers into a live-search path and a pre-trained/indexed path, noting that some sites block AI crawlers in robots.txt. He presents Bright Data's MCP server (60+ tools covering search, page scraping as markdown or HTML, site-specific Amazon/Reddit/LinkedIn data, and browser automation) and shows a Glassdoor example where the agent is blocked without it and succeeds with it. He uses a jobs-data use case to argue for continuous, structured, reliable feeds with historical backfill. The hands-on demo pulls Amazon product data and Reddit posts via API, sends them to Gemini, and returns a buy/no-buy verdict. Most of the talk is product positioning, but the sync-vs-async routing framing and the scraper-maintenance cost argument are useful, and the demo's claims are not benchmarked.

## Key ideas
- **Traditional scraping does not scale by adding engineers: each site needs its own scraper that takes days to build and QA, and breaks when a layout, selector or anti-bot rule changes.** — Speaker estimates 3-5 days per scraper for a developer, and says scaling from 10 to 1,000 sites multiplies the maintenance work. He argues agents can discover sites and build or repair scrapers automatically. This is a vendor-side claim and is not demonstrated. ([1:43](https://youtu.be/IK8cC4FScps?t=103))
- **Route AI questions by whether the answer needs fresh data: the live-search path for time-sensitive questions, and the pre-trained or indexed (RAG) path for stable ones.** — Example: 'best time to travel to San Francisco' can be answered from pre-trained data, but 'this year' needs live search for current events. Both paths need different setup. ([9:43](https://youtu.be/IK8cC4FScps?t=583))
- **Cache answers that stay valid for a while, such as daily weather, so repeated questions do not trigger new web fetches or token spend.** — Speaker says one user asking once is enough to fill the cache for everyone who asks the same thing that day. ([9:43](https://youtu.be/IK8cC4FScps?t=583))
- **Many sites block AI crawler user agents such as GPTBot and ClaudeBot in robots.txt, so AI assistants may fail to reach their data unless a managed unblocking layer is used.** — Speaker positions Bright Data's residential IPs, real-browser behavior and anti-bot logic as the fix. He gives no measured block rates. ([12:13](https://youtu.be/IK8cC4FScps?t=733))
- **Expose many scraping and data tools behind one MCP endpoint and let the agent choose which tool to call, instead of hard-wiring pipelines.** — The endpoint has 60+ tools across search results, markdown/HTML page scraping, site-specific datasets (Amazon, Reddit, LinkedIn, Instagram), and browser actions. Example: a Claude Code agent first calls search, then scrapes each returned profile URL, and aggregates follower counts. ([13:41](https://youtu.be/IK8cC4FScps?t=821))
- **Side-by-side demo: the same Claude prompt that gets a Glassdoor page through the MCP server is blocked without it.** — Used as evidence that anti-bot handling, not the model, decides whether the agent gets data. Single example, not a systematic comparison. ([15:06](https://youtu.be/IK8cC4FScps?t=906))
- **Continuous feeds need consistent output schemas, reliability, and historical backfill, not a one-time pull.** — Job-data example: postings, salaries, locations and company hiring rates must keep flowing, and trend analysis needs past months or years. Speaker says downtime breaks the whole downstream pipeline. ([17:13](https://youtu.be/IK8cC4FScps?t=1033))
- **Validate and dedupe scraped records before they reach storage, since a failed stage can force a full re-run and backfill.** — Checks mentioned: field fill rates (e.g. price returned 90% of the time), validation rules, dedupe and enrichment, then bronze/silver/gold medallion layers. Speaker says a failure in the anti-bot or selector layer means restarting the whole process. ([8:24](https://youtu.be/IK8cC4FScps?t=504))

## Techniques
- **Live-vs-indexed query routing** — Decide per question whether the answer depends on current facts. Send time-sensitive questions to a live web-search tool and let stable questions use pre-trained or indexed knowledge. *When:* Agent products that mix static knowledge questions with questions about current events, prices or availability.
- **Response caching for time-stable answers** — Cache an agent's web-backed answer for the period it stays valid (e.g. a day for weather) and serve repeat questions from the cache. *When:* High-repeat queries where freshness is measured in hours and fetch or token costs matter.
- **One MCP endpoint with many scraping tools** — Put search, page-to-markdown, page-to-HTML, site-specific data and browser-action tools behind one MCP server. The agent picks tools per task, and you add or swap tools without rewriting the pipeline. *When:* Agents need data from many domains or many sites and per-site scrapers would be too costly to maintain.
- **Search-then-scrape chaining** — Step 1: run a search tool to collect candidate URLs. Step 2: scrape each result through a structured or markdown tool. Step 3: aggregate the results and return the answer. *When:* Entity lookups across platforms, such as finding a person's profiles and counting followers.
- **Decision agent over multi-source API data** — Pull structured product data from one API and social sentiment from another (Reddit search), pass both to an LLM, and ask for a yes/no verdict with reasons. *When:* Lightweight product or market research where you need a fast recommendation from mixed structured and unstructured sources.
- **Record validation and medallion staging** — Track field-level fill rates, apply validation rules, dedupe and enrich records, then promote them through bronze, silver and database layers, so a failure only re-runs the affected stage. *When:* Scraped or API data feeding models or analytics on a recurring schedule.

## Numbers
- Bright Data is described as the largest web data collection platform, collecting petabytes of data per month, second only to Google. ([0:12](https://youtu.be/IK8cC4FScps?t=12))
- Developing one site scraper takes about 3-5 days for a developer, including QA and running in development. ([1:43](https://youtu.be/IK8cC4FScps?t=103))
- Scraper maintenance cost rises with site count: the speaker says managing 1,000 sites needs about 2x or 4x more engineers (illustrative, not measured). ([4:17](https://youtu.be/IK8cC4FScps?t=257))
- Bright Data's MCP endpoint exposes about 60+ APIs or tools, with the count still growing. ([13:41](https://youtu.be/IK8cC4FScps?t=821))
- The speaker gives an example of an agent gathering social profiles through search followed by scraping; it is a single anecdote with no latency or success-rate figures. ([13:41](https://youtu.be/IK8cC4FScps?t=821))
- Demo: Amazon product data and a Reddit keyword search for one product produce a buy/no-buy answer in one run; no latency, token or cost numbers are shown. ([20:44](https://youtu.be/IK8cC4FScps?t=1244))

## Hot takes
- Adding engineers to manage more scrapers does not scale, and agents can replace much of that per-site work.
- AI assistants are often blocked from the web by robots.txt rules aimed at AI crawlers, so answers can be incomplete unless a managed unblocking layer is used.
- Many scraping teams spend more time figuring out what a site changed than fixing the scraper.

## Tools mentioned
Bright Data MCP server, Bright Data Web Unlocker, Bright Data Browser API, Claude Code, Claude, GPT, Gemini API, LangChain, Google Colab-style notebook, Glassdoor, Amazon, Reddit, Walmart, Shopee, Etsy, Shopify stores, Cloudflare, Akamai

## Relevance to our work
- **agentos** (1/3): Live web fetch versus indexed retrieval is a route decision that AgentOS MemoryMesh's hybrid retrieval does not currently make explicit. Caching time-stable web answers is a related idea. → *Add a freshness-based route to MemoryMesh (live fetch for time-sensitive queries, cache or index otherwise) and measure the cache hit rate on repeated questions.*
- **general** (1/3): Recurring interests include data quality with LLMs and entity resolution. The talk's record validation and dedupe-before-storage steps are relevant, though they are described only briefly. → *Compare the validation and dedupe stages described here (fill-rate checks, validation rules, staged promotion) with the ER pipeline's pre-merge checks.*
