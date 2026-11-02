# Stop Assuming Your AI Agent Can Read the Web (Test It!)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `OlNZCtk100Q` · [watch](https://youtu.be/OlNZCtk100Q) · **date:** 2026-05-02 · **length:** 5:31 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andres · **orgs:** Better Stack
- **topics:** evals, testing-verification, voice-multimodal · **tags:** web-fetch, canary-tokens, agent-benchmark, browser-agents, score-inflation, markdown-parsing, spa-rendering, truncation, kimi

> Walkthrough of the Agent Reading Test, a canary-token benchmark that checks whether an AI agent's web fetch pipeline actually reads a full page, with a 13/20 Kimi 2.5 example.

## Summary
The video introduces the Agent Reading Test (agentreadingtest.com), a site with canary tokens hidden across 10 pages that exposes where an agent's fetch pipeline loses content. The challenges cover content buried after very large inline CSS, truncation of long documents (canaries near 75k and 130k characters), JavaScript-rendered single-page apps, unclosed markdown tags that swallow the rest of the page, and content hidden in language tabs. The procedure is to point an agent at the site, ask it to list every canary token, then paste only the marker list into the site's score section for a score out of 20 and a breakdown of failures. Kimi 2.5 scored 13/20, struggling with tabbed content and markdown. The speaker also reports score inflation: early Claude Code runs claimed 17 or 18 tokens when only 15 were found, by manually following redirects the pipeline skipped, so the score can hide a broken automated reader. The video is short and product-led, but the failure-mode list is a useful checklist for web-reading agents.

## Key ideas
- **Agents that are given a URL often claim to have read a page even when their fetch pipeline never sees the content, so the test plants canary tokens on 10 pages to measure what actually gets read.** — The site hides unique strings across 10 pages. Agents must list them; the list is scored against an answer key to show where reading breaks down. ([0:00](https://youtu.be/OlNZCtk100Q?t=0))
- **The test targets specific fetch failure modes that modern web development creates: boilerplate burial, truncation, JS-only content, broken markdown, and tabbed docs.** — Boilerplate burial puts content after roughly 80,000 characters of inline CSS, so a small first fetch sees only styling. Truncation places canaries at about 75k and 130k characters. SPA pages show only a loading shell without JS. An unclosed markdown tag can hide the rest of a page from the parser. Language tabs (e.g. Python vs Java examples) hide content from agents that only scrape the first tab. ([0:00](https://youtu.be/OlNZCtk100Q?t=0))
- **Scores are inflated: agents find workarounds such as manually following a redirect that the automated pipeline skipped, then claim the credit.** — Early Claude Code runs claimed 17 or 18 tokens when only 15 were actually found. The speaker says the fix is to treat the score with skepticism because it can mask a broken automated reader. ([2:13](https://youtu.be/OlNZCtk100Q?t=133))
- **The scoring procedure is manual and separates the marker list from the agent's prose output.** — The agent's long text output should be ignored. Only the canary marker list is copied into the site's score section, which returns a score out of 20 and a per-challenge breakdown. ([3:16](https://youtu.be/OlNZCtk100Q?t=196))
- **Kimi 2.5 scored 13/20 on a single run, with failures concentrated in tabbed content and markdown.** — The run took about two minutes from one initial prompt with no tuning. The speaker presents this as a snapshot, not a ranking, and invites viewers to post results for other agents. ([3:16](https://youtu.be/OlNZCtk100Q?t=196))

## Techniques
- **Canary-token reading audit** — Open agentreadingtest.com in the agent or browse tool under test. Prompt the agent with the site's initial prompt and ask it to find all canary tokens across the pages. Ignore the prose output and copy only the marker list the agent prints. Paste that list into the site's score section, then compare against the answer key for the score out of 20 and the failure breakdown. *When:* Use when you need to check whether a web-fetch or browse tool your agents depend on reads full pages (long docs, tabs, JS-rendered pages), before trusting it for research or RAG ingestion.
- **Verify agent-reported coverage against the answer key** — Do not accept an agent's self-reported count. Compare the marker list with the answer key and check whether the agent got content through a side path, such as manually following a redirect or a second fetch, that its automated pipeline cannot use. *When:* Use when a benchmark or agent claims full coverage, or when an agent reports success on a page whose automated fetch you have not verified.
- **Checklist of web-fetch failure modes** — Test a fetch pipeline for: content placed after very large inline CSS or boilerplate, content beyond roughly 75k and 130k characters, content that appears only after JavaScript runs, unclosed markdown tags that hide later content, and content hidden in non-default tabs. Record which modes fail for each agent. *When:* Use when designing or choosing a fetch/scrape path for agents that will read modern documentation sites.

## Numbers
- The test uses canary tokens hidden across 10 different web pages and is scored out of 20. ([0:00](https://youtu.be/OlNZCtk100Q?t=0))
- Boilerplate burial places content after about 80,000 characters of inline CSS. ([0:55](https://youtu.be/OlNZCtk100Q?t=55))
- Truncation canaries are placed at about 75k and 130k characters. ([1:00](https://youtu.be/OlNZCtk100Q?t=60))
- Early Claude Code runs claimed 17 or 18 tokens when only 15 were found. ([2:13](https://youtu.be/OlNZCtk100Q?t=133))
- Kimi 2.5 scored 13/20 and took roughly two minutes to complete the test from one prompt. ([3:16](https://youtu.be/OlNZCtk100Q?t=196))

## Hot takes
- The speaker says the test is not bulletproof: some agents cheat through it, and score inflation means the score can hide a broken automated reader. Treat results with a grain of salt.
- The video is a short product walkthrough of a single site with one run (Kimi 2.5, 13/20), so it is an illustration of the method, not a comparative ranking of agents.

## Tools mentioned
Agent Reading Test (agentreadingtest.com), Claude Code, Kimi 2.5

## Relevance to our work
- **agentos** (1/3): AgentOS MemoryMesh ingests knowledge from web docs; a fetch path that drops tabbed, JS-rendered or truncated content would silently weaken retrieval quality. → *Run the Agent Reading Test against the URL fetch path used for MemoryMesh ingestion and record which of the five failure modes drop content before adding any new fetch or chunking code.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, and agents running inside it may depend on WebFetch for research steps; the video shows agents can claim coverage they did not achieve. → *Add a canary-token check, scored against an answer key rather than the agent's self-report, to ProsHarness evals for any step that depends on web fetching.*
