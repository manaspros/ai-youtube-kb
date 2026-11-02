# The Missing Layer in Agentic AI — Giedrius Šteimantas, Oxylabs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XsvUhpnHepE` · [watch](https://youtu.be/XsvUhpnHepE) · **date:** 2026-09-18 · **length:** 15:04 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Giedrius Šteimantas · **orgs:** Oxylabs
- **topics:** voice-multimodal, mcp-and-tools, infra-cost-scaling, token-cost-efficiency · **tags:** web-scraping, browser-agents, playwright-mcp, captcha, token-cost, content-validation, search-api, geolocation, agent-infrastructure, vendor-talk

> Oxylabs' Giedrius Šteimantas argues web-using agents need a scraping infrastructure layer: use browsers only when required, validate content before it reaches the LLM, and fix the failing discovery and purchase stages of a shopping agent.

## Summary
The speaker describes a friend's personal-shopping agent that worked poorly: browser automation got captchas, was slow and expensive, and checked only HTTP status and page size, so blocked pages reached the model. He splits the agent into discovery, decision and purchase stages and rebuilds each one. Discovery moves from a predefined site list in a browser to a search API that returns compact results. Decision uses a scraper API that returns only valid content, fails loudly on blocks, and bills only successful results. Purchase still needs a browser, so a managed headless browser with stealth, residential proxies and geolocation replaces the stock Playwright MCP browser as a drop-in. The talk is vendor-led, since the speaker works for Oxylabs and promotes its products, but the concrete failure modes and the validate-before-LLM point are useful regardless of vendor.

## Key ideas
- **Agents that act on the open web need an infrastructure layer, and most agent failures come from its absence** — The speaker's friend built a shopping agent that was blocked by captchas and was slow and costly because it used browser automation for everything. The speaker frames the missing piece as an infrastructure layer. ([0:14](https://youtu.be/XsvUhpnHepE?t=14))
- **Two scraping principles carry over to agents: use a browser only when you must, and validate content** — HTTP 200 does not mean the page is usable. Lighter content is better, since pages are full of JS and CSS that cost tokens and deliver nothing. ([2:39](https://youtu.be/XsvUhpnHepE?t=159))
- **Discovery should use a search API, not a browser over a fixed site list** — A fixed list of retailer sites is deterministic, limits item choice, and misses location-dependent stock. The agent generates fan-out queries and picks URLs from compact search results. ([6:45](https://youtu.be/XsvUhpnHepE?t=405))
- **Most token waste comes from invalid pages that the agent still reads** — Checking only size and status code let blocked pages through. In one example, 3 of 10 pages were valid but all 10 were sent to the model, so about 70% of tokens were wasted. ([8:12](https://youtu.be/XsvUhpnHepE?t=492))
- **Fix validity before compression** — The speaker first thought compression was the fix, then saw that the real problem was invalid content. Filtering out blocks before the model sees them comes before any compression. ([9:47](https://youtu.be/XsvUhpnHepE?t=587))
- **Fail loudly and bill only for success** — A scraper API returns only valid content and gives an explicit error on CAPTCHAs or blocks. The speaker says customers pay only for successful results, so failures cost nothing. ([10:48](https://youtu.be/XsvUhpnHepE?t=648))
- **The purchase step needs a real browser, so swap in a managed one instead of a stock Playwright MCP browser** — The speaker keeps a human approval step before purchase. A managed headless browser with stealth, a residential proxy and geolocation is a drop-in for Playwright MCP. ([11:54](https://youtu.be/XsvUhpnHepE?t=714))

## Techniques
- **Validate page content before the LLM sees it** — Check that the response is real content, not a captcha or block page, before any tokens are spent. Do not rely on HTTP status code or response size. Treat a blocked page as an explicit failure. *When:* Any agent that reads web pages, especially when many pages are fetched in parallel and only some are valid.
- **Search API for discovery, not a browser** — Give the agent a search tool that returns compact JSON. The agent writes several fan-out queries, reads the results, and picks the URLs to visit. Use a model that is cheap and fast for this step. *When:* Open-ended discovery, such as finding products or pages across the web, where the list of sites is not known in advance.
- **Tiered web access: API first, browser last** — Use search and scraper APIs for reads. Reserve a browser for stateful interactive steps such as cart, form input and checkout. Keep a human approval step between the decision and the purchase. *When:* Agents that both research and act on the web, where cost and reliability matter more than speed of implementation.
- **Markdown and geolocated output from the scraper** — Request Markdown instead of raw HTML so the model gets fewer tokens. Set a geolocation so prices and stock match the user's region. *When:* Feeding web content to an LLM, especially for location-dependent results such as stock and pricing.
- **Drop-in managed browser for Playwright MCP** — Point the existing Playwright MCP setup at a managed headless browser endpoint instead of a local browser. The speaker reports no other code changes. *When:* A browser agent is blocked by anti-bot checks and the team does not want to build stealth or proxy handling itself.

## Numbers
- Search API response is under 2,000 tokens and returns in under 700 ms on average (Fast Search API) ([6:45](https://youtu.be/XsvUhpnHepE?t=405))
- About 70% of tokens wasted when 10 pages are sent to the model and only 3 are valid ([8:12](https://youtu.be/XsvUhpnHepE?t=492))
- Oxylabs has spent about 10 years supplying web data to companies that train large language models ([2:39](https://youtu.be/XsvUhpnHepE?t=159))
- Customers pay only for successful scrapes; failed requests cost nothing ([10:48](https://youtu.be/XsvUhpnHepE?t=648))
- Hundreds of requests can be run in parallel against the scraper API ([10:48](https://youtu.be/XsvUhpnHepE?t=648))

## Hot takes
- Use a browser only when you absolutely have to; most agent web access should be an API call
- HTTP 200 and a large response body do not mean the page is valid
- The problem is invalid content, not token count, so fix validity before compressing
- Agent builders should not build their own stealth and proxy layer; buy it as infrastructure

## Tools mentioned
Playwright MCP, Oxylabs Fast Search API, Oxylabs Web Scraper API, Oxylabs Headless Browser

## Relevance to our work
- **agentos** (1/3): AgentOS has a proxy and sandbox layer but no web-access tool path in the profile; the validate-before-LLM point applies once a web-fetch tool is added. → *If AgentOS adds a web-fetch tool, reject captcha and block responses before they reach the model, and log them as failures separate from HTTP status.*
- **prosharness** (1/3): The talk's model of a human approval step before an irreversible purchase matches ProsHarness's phone-driven approvals. → *Make sure any ProsHarness run that takes an irreversible external action (purchase, send, delete) has a checkpoint and approval gate before that step.*
- **general** (1/3): The cheapest-tool-first and validate-before-LLM principles apply to any agent with tools, though this is a single vendor-led talk. → *When designing tool defaults for agents, use the cheapest reliable tool first and reserve the browser for steps that need interaction.*
