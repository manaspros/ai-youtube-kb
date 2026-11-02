# 5 Open Source AI Tools That Feel ILLEGAL To Know About

- **channel:** [Kai Explains](../channels/kai.md) · **id:** `-UxcljWN49I` · [watch](https://youtu.be/-UxcljWN49I) · **date:** 2026-08-02 · **length:** 11:39 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Kai Explains host (unnamed) · **orgs:** Mendable, Cognition AI, Maersk, Novartis, Deloitte, Panasonic
- **topics:** agent-architecture, memory, coding-agents, voice-multimodal · **tags:** open-source, agent-stack, browser-agents, web-scraping, agent-memory, coding-agent, visual-workflow-builder, github-stars, tool-roundup

> Roundup of five open-source agent building blocks (Browser Use, Firecrawl, Mem0, OpenHands, Dify) mapped to read, act, remember, code and orchestrate roles. Mostly star counts and vendor stats, with no hands-on steps.

## Summary
Kai Explains argues that a useful AI agent needs four capabilities (reading the web, acting on it, memory, and a planning brain), and picks one open-source repo per slot plus one platform that ties them together. The picks are Firecrawl for turning web pages into clean markdown or JSON, Browser Use for driving a real browser through a read-decide-act loop, Mem0 for storing durable facts and retrieving only relevant ones, OpenHands for a sandboxed coding agent, and Dify as a visual canvas for building and shipping workflows. Most of the video is a tour of each project's pitch, with vendor-sourced figures such as the Browser Use WebVoyager result and Mem0's paper numbers. There are no commands, configs or code. The speaker's most useful advice is to start with two pieces (Firecrawl plus Dify) and to remember that star counts measure attention, not fit. The title oversells the content, so this is a map of the ecosystem, not a how-to.

## Key ideas
- **An agent needs four slots: reading the web, acting on it, memory, and a planning brain. The speaker assigns one open-source repo to each.** — Speaker frames the list as the minimum toolkit. Firecrawl = eyes, Browser Use = hands, Mem0 = memory, OpenHands = coding worker, Dify = brain and orchestration. One of them does two jobs. ([0:00](https://youtu.be/-UxcljWN49I?t=0))
- **Browser Use runs a read-decide-act loop instead of replaying a recorded script, so it adapts when a site changes.** — The loop reads page structure, picks the next click or type, acts, then re-reads the new state. It targets sites with no API, such as long forms, checkouts and logged-in dashboards. Model agnostic, MIT core, hosted cloud option. Speaker notes it is slower and pricier than a plain API call and can be tripped by pop-ups. ([0:00](https://youtu.be/-UxcljWN49I?t=0))
- **Firecrawl converts messy pages into clean markdown or JSON and is the most-starred repo on the list, which the speaker says is a scraper rather than an agent framework.** — Four verbs: scrape, crawl, search, extract (fields described in plain English). Renders JavaScript and handles proxies and anti-bot walls. The argument is that most retrieval pipelines begin by getting web content in, so clean input simplifies everything downstream. ([2:38](https://youtu.be/-UxcljWN49I?t=158))
- **Mem0 avoids replaying full chat history by extracting durable facts on write and retrieving only the relevant memories on read.** — Memories sit in a vector store with an optional graph mode for linking facts. Self-host or use the cloud. Memory follows the user rather than the chat window. The headline comparison is against the model's built-in memory on a long-conversation benchmark, with a claim that it is backed by a peer-reviewed paper. ([4:06](https://youtu.be/-UxcljWN49I?t=246))
- **OpenHands gives a coding agent a full sandbox with a terminal, editor, browser and file system, then runs a plan, write, test, fix loop on a GitHub issue or task.** — Positioned as the open-source answer to Devin, which the speaker says launched at $500 a month. Claims public SWE-bench results and support for 100+ model backends, self-hostable under MIT. ([5:21](https://youtu.be/-UxcljWN49I?t=321))
- **Dify (transcribed as DeFi) is the orchestration layer: a visual canvas that also carries production features such as per-step logs, timing traces, OpenTelemetry export, a worker queue, built-in RAG and A/B testing.** — The speaker's main differentiator is observability for visual builders: you can see which step fired, with what input, and where time went. Core is Apache 2.0. Speaker presents this as the canvas you prototype on and also deploy from. ([6:42](https://youtu.be/-UxcljWN49I?t=402))
- **Practical advice is to start small. Pick two (Firecrawl for ingestion and Dify for the loop) and add the rest later. Stars measure attention, not fit.** — The speaker says to judge each repo by what it solves today, not by its star count. Links are in the video description. ([10:50](https://youtu.be/-UxcljWN49I?t=650))

## Techniques
- **Read-decide-act browser agent loop** — Read the page's structure, pick the next action (click, type, scroll), perform it, then re-read the new state and repeat until the goal is met. Avoid recorded scripts so the agent can adapt when a site changes. *When:* Sites with no API, such as long forms, checkouts or pulling a figure from a logged-in dashboard. Not for calls where a plain API would do, since browser agents are slower and costlier.
- **Scrape-to-markdown before retrieval** — Send each URL to a scraper that returns clean markdown or JSON with ads, banners and navigation removed, then index or prompt on that text. The speaker names Firecrawl's four verbs: scrape, crawl, search, extract. *When:* Any RAG or agent pipeline that begins by ingesting web content. Clean input makes later retrieval simpler.
- **Two-phase memory: extract on write, retrieve on read** — After a conversation, pull the durable facts out and store them, optionally with a graph of how facts relate. On the next turn, retrieve only the relevant memories and put those in the prompt, not the full transcript. *When:* Multi-session agents where replaying history would blow up the context window and token cost.
- **Sandboxed plan-write-test-iterate coding loop** — Give the agent a sandboxed environment with a terminal, editor, browser and filesystem. Hand it a task or issue, let it read files, plan, write code, run tests, read failures and iterate until done. *When:* Autonomous coding tasks where the agent must verify its own work by running tests in isolation.
- **Per-step tracing and worker queues for visual workflows** — Log each step's input and output and its timing, export via OpenTelemetry, and run long flows on a worker queue so they do not time out for the user. The speaker describes this as built into Dify. *When:* Production agent workflows where you need to see which step failed or slowed down, and where long runs must not block a request.

## Numbers
- Five repos with over 500,000 GitHub stars combined ([0:00](https://youtu.be/-UxcljWN49I?t=0))
- Browser Use: about 89% completion on WebVoyager (586 live-website tasks), 106,000 stars ([1:16](https://youtu.be/-UxcljWN49I?t=76))
- Firecrawl: over 155,000 stars, the most on the list ([2:38](https://youtu.be/-UxcljWN49I?t=158))
- Mem0 vs model built-in memory on a long-conversation benchmark: 26% more accurate, 90% fewer tokens, 91% lower tail latency; 61,000 stars ([4:06](https://youtu.be/-UxcljWN49I?t=246))
- Devin launched early 2024 at $500/month (speaker also cites a '$1.500' monthly figure for alternatives, likely a caption error) ([5:21](https://youtu.be/-UxcljWN49I?t=321))
- OpenHands: 82,000+ stars ([6:42](https://youtu.be/-UxcljWN49I?t=402))
- Dify: passed 100,000 stars in June 2025 and 145,000+ by mid-2026; runs on 1.4M+ machines in 175 countries; raised $30M at a $180M valuation in early 2026 ([8:05](https://youtu.be/-UxcljWN49I?t=485))

## Hot takes
- Clickbait title ('feel ILLEGAL') over a generic ecosystem tour. Capped at quality 2 per the rules: thin on how-to and sourced mostly from star counts and vendor claims.
- The speaker ranks tools by GitHub stars, then concedes at the end that 'stars measure attention, not fit'.
- The Mem0 benchmark is compared only against the model's own built-in memory. It is not compared with RAG or other memory systems, so the 90% token figure is a narrow comparison.
- 'Every single one is free and open' overstates it. Browser Use, Firecrawl and Dify each have hosted paid tiers, and model calls are still paid, as the speaker concedes at 9:26.
- The Dify stats (1.4M machines, $30M raise, enterprise logos) are self-reported claims given without sources.

## Tools mentioned
Firecrawl (transcribed 'fire crawl'), Browser Use, Mem0 (transcribed 'Memzero'), OpenHands (transcribed 'open hands'), Dify (transcribed 'DeFi'), Devin (transcribed 'Devon'; Cognition AI, mentioned as a $500/month closed product), WebVoyager (benchmark, 586 tasks), SWE-bench (benchmark), Langflow (mentioned as Dify's origin comparison), OpenTelemetry (Dify export)

## Relevance to our work
- **agentos** (2/3): L2A MemoryMesh covers tiered memory and retrieval, which overlaps directly with Mem0's extract-on-write and retrieve-on-read approach. L2C Crucible's sandbox overlaps with OpenHands' sandboxed coding loop. → *Read the Mem0 memory design and its benchmark method, then compare its extract-and-retrieve pattern with MemoryMesh's tiered cross-session memory on token cost and latency.*
- **prosharness** (1/3): OpenHands' plan-write-test-iterate loop in a sandbox is adjacent to ProsHarness's checkpoint/resume of long Claude Code runs, but the video does not discuss resume or checkpointing. → *Look at how OpenHands structures its sandbox and iteration loop for ideas on checkpointing long coding runs. Treat it as optional background reading.*
