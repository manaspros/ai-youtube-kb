# From MCP to Scale: Pipelines That Build Themselves — Rafael Levi, Bright Data

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `zTZ0qunQXnM` · [watch](https://youtu.be/zTZ0qunQXnM) · **date:** 2026-06-18 · **length:** 25:26 · **format:** demo · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Rafael Levi · **orgs:** Bright Data
- **topics:** data-engineering, coding-agents, mcp-and-tools, voice-multimodal · **tags:** web-scraping, bright-data, token-cost, self-healing-pipeline, anti-bot, scheduled-agents, json-output, remote-browser, vendor-demo

> A Bright Data vendor demo arguing LLMs should write a reusable scraper once instead of parsing every page, then run and self-repair it on a schedule. Useful pattern, heavy product pitch.

## Summary
Rafael Levi from Bright Data argues that parsing thousands of pages with an LLM is too expensive in tokens, so the agent should write a deterministic scraper, run it as a script, and keep it maintained. He demos Claude Code using the vendor's skill docs and MCP to build a Walmart headphone scraper in about three minutes, with the MCP's scrape-as-markdown tool returning text where a plain fetch was blocked by a bot screen. He then shows the generated script running for roughly 60 to 100 tokens, returning JSON that he says is cheaper to process than markdown. He describes scheduled agents that check output every 30 minutes and repair broken selectors, and remote browsers with simulated human input for multi-step flows. Much of the talk is product promotion, several live demo steps stalled, and the token savings are vendor-reported figures that are not consistent across the talk. The core pattern is still a practical one.

## Key ideas
- **Do not have the LLM parse every page. Have it write a scraper once, then run that script for the bulk of the data.** — Speaker says per-page LLM parsing burns tokens at scale. The script runs cheaply, and the agent is only involved when something needs fixing. ([0:00](https://youtu.be/zTZ0qunQXnM?t=0))
- **The agent should also maintain the scraper, not just write it.** — Speaker says scrapers break when sites change, and maintenance can take longer than writing. He describes an agent that checks data and fixes missing fields, and he gives a five-minute repair time. ([1:02](https://youtu.be/zTZ0qunQXnM?t=62))
- **Vendor skill docs plus an MCP that returns page content give the agent what it needs to find selectors.** — The agent reads the vendor's GitHub skill docs, fetches page text through the MCP, works out selectors, and writes the parser. He says this took about three minutes live. ([3:16](https://youtu.be/zTZ0qunQXnM?t=196))
- **Plain fetches get blocked on protected sites, while the MCP route returns usable text.** — In a live comparison, a standard fetch of Walmart hit a bot verification screen. The MCP scrape-as-markdown call returned the first product. The speaker says the unblocking is handled by the vendor's infrastructure. ([12:27](https://youtu.be/zTZ0qunQXnM?t=747))
- **Tier the fetch format: text for reading, JSON for structured output, HTML only when needed.** — Markdown saves tokens over raw HTML. Pre-built domain APIs return JSON directly. The speaker says JSON is the most token-efficient output for downstream use. ([15:16](https://youtu.be/zTZ0qunQXnM?t=916))
- **Ask the agent for a script that is reused later, not for the answer itself.** — Speaker says running the script costs very few tokens, and processing its JSON costs roughly 1,000 tokens against about 10,000 for LLM-based extraction. He says this is pennies in practice. These numbers are his, and no measurement method is shown. ([20:50](https://youtu.be/zTZ0qunQXnM?t=1250))
- **The pattern suits recurring watch-and-alert jobs as well as bulk collection.** — Examples include a scheduled listener for apartment listings under a price, and a booking-slot watcher. The scheduled agent runs the script, checks results, and notifies on a match. ([7:28](https://youtu.be/zTZ0qunQXnM?t=448))

## Techniques
- **Generate-then-run scraper** — Point the coding agent at vendor skill docs and a page-content tool. Have it inspect the page, find selectors, write a parser, and save a script that outputs a fixed JSON schema. Run the script for bulk work, and call the LLM only when it fails. *When:* Repeated extraction from the same site or set of sites where per-page LLM parsing would cost too much.
- **Scheduled self-repairing collection loop** — Schedule a short agent run (the speaker uses every 30 minutes). It checks the latest output against validation rules, such as required fields being present. If a check fails, it patches the script and reruns it. *When:* Long-running collection where sites change and someone should not have to be woken up to fix breakage.
- **Tiered fetch format** — Use a pre-built domain JSON API first, then markdown or text for reading, and raw HTML only as a fallback. *When:* Token budget matters and the target domain has a pre-built endpoint or simple text structure.
- **Remote browser with human-like input for multi-step flows** — Use a remote browser on a chosen country IP. Drive clicks and typing with pre-recorded human-like mouse and keystroke patterns. The speaker says a small model such as Haiku is enough for the browsing steps. *When:* The target needs form fills or button sequences, and the URL cannot be built directly, such as hash-based flight search.
- **Public-data-only policy check** — The speaker says to avoid login-gated data and to read site terms before scraping, since accepting terms can create legal exposure. *When:* Before building any scraper for a third-party site.

## Numbers
- Bright Data MCP free tier: 5,000 requests ([4:24](https://youtu.be/zTZ0qunQXnM?t=264))
- Speaker-reported saving of about 1 million tokens for a three-page scrape by building a scraper instead of parsing HTML with the LLM ([4:24](https://youtu.be/zTZ0qunQXnM?t=264))
- Over 150 million IPs in the vendor network ([8:39](https://youtu.be/zTZ0qunQXnM?t=519))
- Speaker-reported build time: about 3 minutes live, versus a full day or a day and a half manually ([8:39](https://youtu.be/zTZ0qunQXnM?t=519))
- MCP exposes about 66 tools ([9:39](https://youtu.be/zTZ0qunQXnM?t=579))
- About 500 pre-built domain APIs ([10:46](https://youtu.be/zTZ0qunQXnM?t=646))
- Live-run token saving of about 62% versus LLM parsing of full HTML (speaker's breakdown; one run; the speaker says this site may have structured HTML) ([13:48](https://youtu.be/zTZ0qunQXnM?t=828))
- Scheduled check interval example: every 30 minutes; repair time for a missing field: about 5 minutes ([2:14](https://youtu.be/zTZ0qunQXnM?t=134))
- Script execution cost: about 60 tokens, or about 100 tokens total for the run, per speaker ([16:52](https://youtu.be/zTZ0qunQXnM?t=1012))
- Speaker-estimated token counts: about 1,000 for the script path versus about 10,000 for LLM processing of the JSON ([20:50](https://youtu.be/zTZ0qunQXnM?t=1250))
- MCP is useful for about 20% of domains (heavily protected ones such as Akamai, DataDome and Cloudflare) ([21:54](https://youtu.be/zTZ0qunQXnM?t=1314))

## Hot takes
- LLM-per-page extraction is the wrong default for scale; a generated script is the right unit of work.
- Public data is public: the speaker says courts sided with the vendor in suits brought by Meta and by X under Elon Musk. This is his account, not verified here.
- Haiku is enough for browsing agents when the traffic is masked well (speaker's view).

## Tools mentioned
Claude Code, Codex, Bright Data MCP, Bright Data scrape-as-markdown, Bright Data Web Unlocker API, Bright Data remote browsers, Bright Data skill docs on GitHub, Haiku

## Relevance to our work
- **prosharness** (2/3): ProsHarness already has loops and schedules. The talk's pattern of a short scheduled agent run that validates output, patches a script, and reruns it fits that feature directly. → *Try a scheduled ProsHarness loop that checks the last run's output against validation rules and patches its generated script only when a check fails; keep each check run short.*
- **agentos** (1/3): The generate-a-script-then-run pattern is a cost-control idea for recurring data pulls, but AgentOS has no scraping or ingestion path today. → *When designing a recurring ingestion job, compare the cost of LLM-per-item extraction with a generated parser run on a schedule; no code change needed now.*
