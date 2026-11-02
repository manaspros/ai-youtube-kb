# Firecrawl MCP = Effortless Web Scraping

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `2GHRDoFquOo` · [watch](https://youtu.be/2GHRDoFquOo) · **date:** 2025-11-02 · **length:** 9:08 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** unnamed AI LABS host · **orgs:** Firecrawl, Notion, Cursor, Windsurf, Vercel (Next.js)
- **topics:** mcp-and-tools, vibe-coding-app-building, coding-agents · **tags:** firecrawl, mcp, web-scraping, cursor, windsurf, nextjs, site-cloning, api-key-config, scrape-vs-extract

> Tutorial on wiring the Firecrawl MCP server into Cursor so an agent can scrape a live URL and generate a near-copy of a Notion landing page in Next.js. Shows setup and a single demo run, with the output's flaws called out.

## Summary
The host clones Notion's landing page by giving a coding agent the page URL rather than a text description. The agent calls the Firecrawl MCP server's scrape tool, which returns the page's structure, content, and image links, and then generates Next.js components from that data. The video walks through the Firecrawl README (scrape vs. extract tools), creating an API key, and adding the server to Cursor's MCP settings with the key pasted into the command field. It then shows the agent-mode prompt that must name the Firecrawl tool, a timeout that needed a retry, and the result. The result is close in layout and images but defaulted to dark mode, with some icons missing or low-contrast and some images cut off. The host says Windsurf setup is nearly identical and that the Windsurf version of this workflow would have been a better choice. The video is short and mostly a product walkthrough; it gives no cost analysis, no evaluation beyond eyeballing the clone, and no discussion of the legal or ToS side of copying another site.

## Key ideas
- **Give the agent a URL, not a description. The scrape tool returns the page's structure, text, and image links, so the agent can produce a far closer copy than one prompted from words alone.** — The host says the Firecrawl MCP extracted metadata and the same images from the Notion page, which produced a near one-to-one clone in a blank Next.js app. ([0:00](https://youtu.be/2GHRDoFquOo?t=0))
- **Firecrawl has two main tools with different purposes. Scrape returns raw structure and content (HTML tags, section headers, text). Extract returns LLM-structured data for populating a site from another site's content.** — Scrape was picked for cloning because it preserves layout structure. Extract has its own separate token allowance. ([1:21](https://youtu.be/2GHRDoFquOo?t=81))
- **The API key is the usual failure point. Copy the key without the duplicated 'fc' prefix, since the command already adds it.** — Repeating the prefix makes the key invalid, and requests then fail with a 401 that never reaches the MCP server. ([2:49](https://youtu.be/2GHRDoFquOo?t=169))
- **Cursor setup is a four-field form under Settings > MCP: a nickname, type 'command', the command with the key pasted in, then save. A green indicator means it connected; if not, restart Cursor, recheck the key, or hit refresh.** — The exact npx command was shown on the README, not read aloud in full in the transcript. ([4:16](https://youtu.be/2GHRDoFquOo?t=256))
- **The prompt has to name the MCP server and the agent has to be in agent mode. Without that, the model builds the page from its own knowledge instead of calling the tool.** — The host named the scrape tool explicitly and selected Claude 3.7 Sonnet in Cursor. The first scrape timed out on a large page, so the host raised the timeout and re-ran it. ([4:16](https://youtu.be/2GHRDoFquOo?t=256))
- **The generated code is organized by component (hero, features, AI section, product card) in a components directory that the agent asks permission to create. The host then runs the dev server and checks the result in the browser.** — The host reports a near one-to-one layout match. ([5:59](https://youtu.be/2GHRDoFquOo?t=359))
- **The clone has visible gaps. The scraped metadata did not include styling, so the output defaulted to dark mode. Some icons are missing or low-contrast, and some images are cut off.** — The host guesses this may be an AI error and says it is still 'extremely accurate' for structure and images. ([7:25](https://youtu.be/2GHRDoFquOo?t=445))

## Techniques
- **Register Firecrawl MCP in Cursor** — Open Cursor Settings > MCP and add a server. Name: any nickname. Type: command. Command: the npx line from the Firecrawl MCP README, with your API key pasted in. Remove the duplicate 'fc' prefix from the key. Save, then confirm the indicator is green. If it is not, restart Cursor, check the key, or press refresh. Windsurf uses the same config, in its own config file. *When:* Any time a coding agent needs live web content (scraping a page, pulling structure, pulling images) that is not in its training data or the repo.
- **Name the MCP tool in the prompt and use agent mode** — Write the prompt as 'Use the Firecrawl MCP server scrape tool on <URL> and ...'. Run in Agent mode. Without the explicit tool name, the agent may skip the tool and generate from its own knowledge. *When:* Whenever the task depends on external data from an MCP tool, so the agent actually calls it.
- **Scrape, then generate by component** — Step 1: scrape the target URL with the scrape tool to get structure, text, and image links. Step 2: have the agent write one component per section (hero, features, AI section, product card) into a components directory. Step 3: run the dev server and check the output against the source page. Re-run the scrape if a call times out, and raise the timeout first if needed. *When:* Recreating a page layout or a design reference from a live site, where section structure and image assets matter more than exact styling.
- **Pick scrape vs extract by goal** — Use scrape when you need the page's structure and raw content to rebuild it. Use extract when you need LLM-structured fields from one source to fill another site's content model. *When:* Choosing a Firecrawl tool for a given ingestion job.

## Numbers
- Free tier allows scraping up to 500 pages before a paid plan is needed. The host says pricing was shown on screen; the transcript does not give a price. ([2:49](https://youtu.be/2GHRDoFquOo?t=169))
- Extract tool has its own token allowance, separate from scrape. ([2:49](https://youtu.be/2GHRDoFquOo?t=169))
- The first scrape call needed a longer timeout and was re-run. No timing numbers were given. ([5:59](https://youtu.be/2GHRDoFquOo?t=359))
- Video length 9:08. ([0:00](https://youtu.be/2GHRDoFquOo?t=0))

## Hot takes
- The host's own result undercuts the 'one-to-one clone' framing: the output defaulted to dark mode, with missing icons and cut-off images.
- The video says nothing about the legal or ToS side of copying another company's landing page and assets, even though that is the demo's whole premise.
- Title promises 'effortless', but the clip is mostly UI setup and a single prompt-and-run, with no evaluation beyond eyeballing the result.

## Tools mentioned
Firecrawl MCP server (scrape and extract tools, npx command, API key), Cursor (agent mode, MCP settings), Windsurf (same MCP config pattern, mentioned as an alternative), Claude 3.7 Sonnet (model selected in Cursor), Next.js (blank starter app used as the target), Notion landing page (the site being cloned)

## Relevance to our work
- **agentos** (1/3): Web scraping as a data-ingestion source for knowledge buckets (MemoryMesh). Scrape (raw structure) vs extract (LLM-structured fields) is a relevant ingestion choice, but this video does not measure either. → *If MemoryMesh ingests web pages, benchmark Firecrawl scrape vs extract against a plain HTML fetch on a few pages, comparing chunk quality and token cost before adopting either.*
- **prosharness** (1/3): Shows MCP servers wired into a coding agent through a per-tool config file with an API key inline. This is a credential-handling pattern ProsHarness is designed to avoid (zero-token credential handling). → *Check how ProsHarness passes MCP server API keys to the Claude Code CLI. The video's paste-the-key-into-the-command-field approach would leak secrets into config files that may be committed.*
