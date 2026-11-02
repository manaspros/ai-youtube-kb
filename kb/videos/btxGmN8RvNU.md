# Your Agent's Biggest Lie: "I Searched the Web" — Rafael Levi, Bright Data

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `btxGmN8RvNU` · [watch](https://youtu.be/btxGmN8RvNU) · **date:** 2026-06-18 · **length:** 15:49 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Rafael Levi · **orgs:** Bright Data, Cloudflare, OpenAI
- **topics:** mcp-and-tools, rag-retrieval, data-engineering · **tags:** bright-data, mcp, web-scraping, anti-bot, captcha, hallucination, silent-failure, scraping-browser, vendor-pitch, token-cost, public-data, live-demo

> Bright Data pitch: blocked web access makes LLM agents fabricate answers silently. Its MCP (search, markdown scrape, CAPTCHA-solving browser) fixed a 5-site demo, but the evidence is one unreplicated run.

## Summary
Rafael Levi of Bright Data argues that when an agent's web requests are blocked (CAPTCHAs, empty pages, bot walls), the model usually invents an answer, fake numbers or dead citations instead of reporting the failure. He cites Cloudflare's AI bot blocking and its AI Labyrinth decoy-content feature as reasons the web is getting harder for agents. The live demo gives the same five-task prompt (move.co, LinkedIn, Instagram, Amazon, TikTok) to GPT-5 with no tools, which fails all five, and to GPT-5 with the Bright Data MCP (66 tools per the speaker), which he says succeeds on four named sites. The MCP tools shown are Google/Bing/DuckDuckGo search, batch search, scrape-as-markdown, pre-built site APIs, and a remote scraping browser with fingerprinting and CAPTCHA solving. He says the approach is to make the agent behave like a human rather than to reverse-engineer detection, and he limits scope to public, non-login data. The talk closes with a pitch for a free tier of 5,000 requests, a skills page that teaches agents to build scrapers, and a claimed ~99% token saving from having the LLM write a parser once. Almost all figures are unsourced vendor claims.

## Key ideas
- **LLMs fabricate answers when web access fails, because they are tuned to please the user and get no explicit error.** — CAPTCHAs, empty pages and blocked requests produce no error the model surfaces; it fills the gap with invented numbers or citations, and he calls this the main source of hallucinations he sees in apps he builds. Stale training data is also presented as current. ([0:00](https://youtu.be/btxGmN8RvNU?t=0))
- **The web is increasingly closed to agents: AI blocking AI, plus decoy content.** — He says Cloudflare blocks AI crawling on about 20% of the web by default and that its AI Labyrinth feature feeds detected bots fake data instead of blocking them, so results get worse without any signal. ([1:08](https://youtu.be/btxGmN8RvNU?t=68))
- **Fake citations are a visible symptom of the same failure.** — He says many ChatGPT citations 404 and that product links often point nowhere. The 60% citation-failure figure is his, with no source given. ([2:29](https://youtu.be/btxGmN8RvNU?t=149))
- **Same prompt, tools off vs. on: GPT-5 with no tools fails all five sites.** — Both runs use identical prompts. The no-tool run has no browsing and reports zero successes out of five. The MCP run is shown live with 66 tools. ([3:58](https://youtu.be/btxGmN8RvNU?t=238))
- **The MCP run reports success on four named sites; the TikTok result is not clearly stated.** — He names successes for move.co, LinkedIn, Instagram and Amazon. The closing comparison in the transcript is garbled, so the TikTok outcome is unclear. ([5:33](https://youtu.be/btxGmN8RvNU?t=333))
- **Anti-bot strategy is to look human rather than out-think detection.** — The remote browser uses a unique fingerprint, recorded mouse movement and human-like typing, and he claims it can run many browser sessions in parallel. Bright Data's CAPTCHA solving is built into the browser. ([9:50](https://youtu.be/btxGmN8RvNU?t=590))
- **Scope is limited to public data, and blocking depends on the IP.** — He says data behind login is off-limits because of terms of service and cites lawsuits (LinkedIn and Amazon named). Home IPs can view only a handful of profiles before a login wall, and data-center IPs get blocked quickly. His 'nobody will sue you' remark is an informal vendor assurance, not legal advice. ([7:09](https://youtu.be/btxGmN8RvNU?t=429))
- **The LLM should write the parser, and a script should run it, instead of parsing each page with the model.** — An agent reads Bright Data's skills page, builds a scraper once, and the script handles thousands of pages. He claims about 99% token savings. This is teased for a later session and not shown here. ([12:49](https://youtu.be/btxGmN8RvNU?t=769))

## Techniques
- **Paired with/without-tools comparison** — Run an identical multi-task prompt twice, once with tools disabled and once with the MCP attached, then ask the model to compare the outputs. Demonstrated with GPT-5 over five anti-bot-heavy sites. *When:* Before trusting a tool integration: confirm it changes answers, and check whether the no-tool run is fabricating.
- **Load a narrow subset of MCP tools** — With a large MCP server (66 to 69 tools in the talk), load only the two tools a task needs, such as search plus scrape-as-markdown, instead of exposing the whole list. The speaker says the full list floods context with irrelevant tools. No config or commands were shown. *When:* When a task uses one or two tools from a large MCP server and extra tool schemas would waste context.
- **Scrape to markdown instead of HTML** — Request a URL through a scrape-as-markdown tool that returns text with HTML tags stripped, so the model never parses raw HTML. *When:* Reading page content into an LLM, to cut token use and parsing errors.
- **Batch search across many keywords** — Send up to about 100 keywords in one batch search call and get back one result set per keyword. *When:* Broad keyword sweeps where one call per query would be slow or costly.
- **LLM writes the parser, script does the extraction** — Have the agent read a vendor skills page that documents the APIs, have it generate a scraper and parser once, then run that script over many pages without LLM calls per page. Per the speaker, the skills page is a plain URL any agent can be pointed at. *When:* Bulk extraction over thousands of similar pages, where per-page LLM parsing is too expensive. The 99% saving is unverified in this talk.
- **Human-like remote browser instead of detection evasion** — Use a remote browser with a unique fingerprint, recorded mouse movement and human-like typing, plus built-in CAPTCHA solving, so the agent does not trigger blocking. The speaker says the approach is to look human, not to understand how each site detects bots. *When:* Sites with heavy anti-bot defenses, where a local or data-center IP and plain HTTP fetches fail.
- **Restrict agents to public, non-login data** — Constrain the agent to public pages and avoid login-gated data, reviewing terms of service for each target. The speaker treats this as the legal boundary. *When:* Any production web-data agent where terms-of-service and lawsuit risk matter. Get real legal review rather than relying on the talk.
- **Pre-collected datasets for non-live needs** — When data a few months old is acceptable, filter a vendor dataset (e.g., LinkedIn profiles by role and area) and give the agent access to it rather than fetching live pages. *When:* Research or analytics tasks where freshness is not critical and live scraping is blocked or costly.

## Numbers
- Cloudflare blocks AI crawling on about 20% of the web by default (speaker's claim, no source). ([1:08](https://youtu.be/btxGmN8RvNU?t=68))
- About 60% of ChatGPT citations reportedly do not work (speaker's claim, no source). ([2:29](https://youtu.be/btxGmN8RvNU?t=149))
- Baseline: GPT-5 with no tools succeeds on 0 of 5 anti-bot-heavy sites. ([3:58](https://youtu.be/btxGmN8RvNU?t=238))
- Bright Data MCP exposes 66 tools (69 later in the talk). ([3:58](https://youtu.be/btxGmN8RvNU?t=238))
- MCP run reports success on 4 named sites (move.co, LinkedIn, Instagram, Amazon); TikTok unclear. ([5:33](https://youtu.be/btxGmN8RvNU?t=333))
- Batch search accepts about 100 keywords in one call. ([5:33](https://youtu.be/btxGmN8RvNU?t=333))
- Free tier of 5,000 requests, described as per month. ([9:50](https://youtu.be/btxGmN8RvNU?t=590))
- Home IP gets about 5 to 10 profiles before a login wall (transcript reads '510'). ([7:09](https://youtu.be/btxGmN8RvNU?t=429))
- Company says it collects petabytes of data daily and saw no degradation after AI Labyrinth (no statistics shown). ([11:25](https://youtu.be/btxGmN8RvNU?t=685))
- LLM-written parser claimed to save about 99% of tokens versus per-page LLM parsing (not demonstrated). ([12:49](https://youtu.be/btxGmN8RvNU?t=769))

## Hot takes
- The main failure of agent web access is silent: no error is raised for CAPTCHAs or empty pages, so the model invents answers. The speaker says this is the core hallucination source.
- Anti-bot strategy should be to make the agent look human rather than to reverse-engineer detection.
- Evidence is weak for a sales talk: one live run over five sites, only a no-tools baseline, a garbled final comparison, and no sourced statistics. Quality is capped at 2.
- The legal reassurance (public data only, 'nobody will come knocking') is an informal vendor claim, not legal advice.

## Tools mentioned
Bright Data MCP (66 tools per speaker; 69 mentioned later), Bright Data scraping browser (remote, fingerprinted, CAPTCHA solving), Bright Data skills page, Bright Data datasets, GPT-5 (tested without tools as baseline), ChatGPT (cited for broken citations), Google, Bing and DuckDuckGo search (via MCP), Cloudflare bot blocking and AI Labyrinth (cited, not used), VS Code (demo environment)

## Relevance to our work
- **agentos** (1/3): AgentOS's proxy and Crucible sandbox are where silent tool failures would be caught. The talk's core failure mode (blocked or empty tool responses that the model papers over) is a guardrail and eval concern, but the talk does not cover AgentOS-relevant techniques directly. → *Add an eval case where a tool returns a CAPTCHA page or empty body, and check that the agent reports the failure rather than answering. Use it in the RAGAS or exec-gate test suite.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, and the talk's point about loading only the needed MCP tools per task applies to how the harness exposes tools to long runs. → *Check whether ProsHarness exposes all MCP tools to each run. If so, try loading only the subset a task needs and compare context use and answer quality.*
