# Kimi K2.6 vs Claude Code: Why I’m Switching to the $39 Plan (Full Model Breakdown)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `icbeuJxnrKU` · [watch](https://youtu.be/icbeuJxnrKU) · **date:** 2026-05-02 · **length:** 10:22 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Andres · **orgs:** Better Stack, Moonshot AI
- **topics:** models-research, multi-agent, coding-agents, token-cost-efficiency · **tags:** kimi-k2.6, kimi-k2.5, agent-swarm, subagents, landing-page-generation, web-scraping, cli-token-counter, claude-code-comparison, moonvit, cheerio, axios, express

> Better Stack runs Kimi K2.6 through an agent-swarm research task, a landing-page build and a scraping web app, and finds it a modest step up from K2.5 with no token-cost data.

## Summary
Andres from Better Stack tests Moonshot AI's Kimi K2.6 on three agentic tasks in Kimi's own chatbot interface and CLI. The vendor claims are a swarm of up to 300 sub-agents running up to 4000 coordinated steps, a preserve-thinking mode, a 13-hour engineering task and a native vision encoder (MoonViT) for UI work. The first test is a swarm run that finds about 20 Toronto notaries with weak websites and produces audits, outreach emails and landing pages in about 40 minutes with five subagents. The landing pages all share one template, so a follow-up prompt for unique styles and generated images takes about 17 minutes more. The third test is a Node/Express price-comparison app with scrapers (Axios and Cheerio) that took about 12 minutes, and needed one follow-up to add a working compare feature. The speaker concludes K2.6 is not dramatically better than K2.5, but has quality-of-life improvements and a cheaper price than Claude Code, though he gives no token numbers to back the cost claim.

## Key ideas
- **Vendor-claimed scale-up of the agent swarm from about 100 sub-agents (K2.5) to 300 specialized agents running up to 4000 coordinated steps** — Speaker reports these as Kimi's claims, not his measurements. He frames the swarm as the headline change for running many parallel tasks at once. ([1:12](https://youtu.be/icbeuJxnrKU?t=72))
- **A preserve-thinking mode keeps the model's reasoning trace consistent across multi-turn tasks** — Stated purpose is to stop memory drift deep into long complex workflows. The speaker does not test this directly. ([1:12](https://youtu.be/icbeuJxnrKU?t=72))
- **Vendor-reported 13-hour engineering task with a 185% throughput gain** — Self-reported by Moonshot in their own tests. The speaker does not reproduce it. ([1:12](https://youtu.be/icbeuJxnrKU?t=72))
- **Swarm test: about 20 Toronto notaries with weak websites, handled by five subagents in roughly 40 minutes** — Subagents browsed sites and judged whether each was outdated. Output was an analysis report per site, an outreach email, a market-size report, generated files and a preview page. The speaker notes the swarm works from a single chat prompt in Kimi's chatbot UI. ([3:13](https://youtu.be/icbeuJxnrKU?t=193))
- **Fan-out per target entity produced near-identical landing pages, and a follow-up prompt fixed the styling** — All 20 pages looked alike. A follow-up asking for a unique style and generated images per page took about 17 minutes. The speaker suspects his first prompt lacked detail, though Kimi's own example used the same prompt. ([4:17](https://youtu.be/icbeuJxnrKU?t=257))
- **Output is still templated: same section layout and site structure on every page, and the preview page was broken** — The speaker judges the result a good start rather than a unique design, and says the approach lets one person pitch many local businesses. ([5:21](https://youtu.be/icbeuJxnrKU?t=321))
- **The model praises its own output in its replies, which the speaker finds funny** — Repeated phrasing such as stunning images and fantastic pages. A minor observation about the model's tone, not a quality measure. ([4:17](https://youtu.be/icbeuJxnrKU?t=257))
- **Coding test: a front-end and back-end RAM price-comparison app with scraping and live refresh in about 12 minutes; the first build had no working compare feature** — A follow-up added an add-to-compare button and a comparison table. Scrapers target Amazon, Newegg and Best Buy using Axios and Cheerio. Images for most products did not load. ([7:19](https://youtu.be/icbeuJxnrKU?t=439))
- **Model-chosen stack is barebones Node.js with Express and vanilla JavaScript, not React, with DOM updates through innerHTML** — The speaker calls the choice interesting and says it works. This is a model-chosen implementation pattern, not a user-specified one. ([8:26](https://youtu.be/icbeuJxnrKU?t=506))
- **Kimi's newest CLI version has a token counter, but the speaker finds no per-task token figures for the 40-minute swarm run** — He argues the swarm is cheaper than doing the same task in Claude Code, but gives no token counts to support it. He also says the Kimi swarm requires a higher paid plan. ([6:23](https://youtu.be/icbeuJxnrKU?t=383))
- **Overall verdict: K2.6 is not a big jump from K2.5, but offers quality-of-life gains and a cheaper alternative to Claude Code** — The verdict rests on three anecdotal single-run tests. The title's claim of switching plans is not argued in the body. ([8:26](https://youtu.be/icbeuJxnrKU?t=506))

## Techniques
- **Per-entity agent swarm fan-out** — Give one chat prompt that asks the model to find N entities (here, businesses) and process each one. The model spins up subagents, five in this run, each handling a subset. Each subagent browses its targets, scores them, and writes its output. A coordinating pass merges everything into a report, emails and generated files. Run in Kimi's chatbot UI with its agent swarm feature (higher paid tier needed). *When:* Research or lead-generation tasks that split cleanly per entity and run for tens of minutes. Good as a scenario to stress multi-agent throughput and collection.
- **Follow-up for per-item differentiation** — When fanned-out outputs all share one template, send a follow-up that asks each item to get a distinct style and its own generated images, instead of rerunning the whole swarm. *When:* After a swarm run produces near-identical artifacts. A cheaper fix than a full rerun, though the speaker still saw shared boilerplate structure.
- **Fix a missing feature with a targeted follow-up** — Test the generated app, find the missing behavior (here, no way to add items to the compare list), and send a single follow-up naming that behavior. The speaker used this to finish the RAM comparison app. *When:* Iterative builds where the first pass is close but misses one interaction.
- **Scraper stack used by the model** — Node.js with Express serving a vanilla JavaScript front end. Scrapers use Axios for HTTP and Cheerio to parse HTML from each store. A live refresh endpoint re-scrapes on demand. *When:* Shows the default stack the model picked when no framework was specified. Useful as a baseline for simple scrape-and-compare apps.

## Numbers
- Agent swarm scaled from about 100 sub-agents (K2.5) to 300 specialized agents, up to 4000 coordinated steps (vendor claim) ([1:12](https://youtu.be/icbeuJxnrKU?t=72))
- Vendor-reported 13-hour engineering task with 185% throughput gain (self-reported) ([1:12](https://youtu.be/icbeuJxnrKU?t=72))
- Notary swarm: 20 businesses, 5 subagents, about 40 minutes total ([3:13](https://youtu.be/icbeuJxnrKU?t=193))
- Follow-up for unique styles and generated images: about 17 minutes ([4:17](https://youtu.be/icbeuJxnrKU?t=257))
- RAM price-comparison app: about 12 minutes for the first build ([7:19](https://youtu.be/icbeuJxnrKU?t=439))
- No per-task token counts reported for the 40-minute swarm run ([6:23](https://youtu.be/icbeuJxnrKU?t=383))

## Hot takes
- Kimi K2.6 is not massively better than K2.5 and mostly offers quality-of-life improvements (speaker's verdict at 8:26).
- Swarm output is templated: the same page structure repeats across generated sites even with different styles (5:21).
- The cost advantage over Claude Code is asserted without any token data, so it remains unverified (6:23).
- Quality capped at 2: the title promises a reason to switch plans, but the body gives three anecdotal single runs, no token or cost numbers, and the switch case is not argued.

## Tools mentioned
Kimi K2.6, Kimi K2.5, Kimi chatbot interface (agent swarm feature), Kimi CLI (newest version, includes token counter), MoonViT (native vision encoder, open source), Hugging Face (model weights), GSAP, Node.js, Express, Axios, Cheerio, Claude Code

## Relevance to our work
- **agentos** (1/3): Multi-agent fan-out and cost reporting are adjacent to AgentOS telemetry and budgets. The video reports no token counts, which is the gap AgentOS would fill. → *Use the per-entity swarm pattern as a multi-agent load scenario, and record token and step counts per subagent, since this video reports none.*
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, and the video shows a CLI-level token counter as a visible way to track spend during long runs. → *Check whether ProsHarness surfaces per-run token spend, the way the new Kimi CLI counter does, before long Claude Code runs hit usage limits.*
