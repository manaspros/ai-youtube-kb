# Why Your Company Needs a Context Graph (and How to Build It) — Gil Feig, Merge

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `cSz7aL2nl2U` · [watch](https://youtu.be/cSz7aL2nl2U) · **date:** 2026-10-10 · **length:** 15:11 · **format:** talk · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Gil Feig · **orgs:** Merge, OpenAI, Ramp, Netflix, Perplexity, Zendesk, Jira, NetSuite, Stripe, Qualtrics
- **topics:** context-engineering, memory, mcp-and-tools, rag-retrieval · **tags:** context-graph, provenance, live-vs-cached-lookup, mcp-limits, skills-first-routing, router-summarizer, freshness-sla, derived-context, enterprise-data

> Gil Feig (Merge) argues every company needs a "context graph" (a company brain of synced data, live lookups, memory, skills) and lays out how to route, cache, and trace it. Conceptual talk with a closing product plug.

## Summary
Gil Feig, co-founder and CTO of Merge, argues that connecting a few MCP servers is not enough for company-wide AI questions. Aggregate questions such as "which customers were upset last year" need a locally synced, vector-indexed copy of third-party data, because live API pagination times out and vendors do not offer semantic query over their APIs. He defines the context layer as third-party data, synced data, memories, and skills, and splits it into four tiers: skills and memory, live API calls, cached sync, and derived summaries. A router sends each prompt to the right place, and a summarizer compresses the combined results before they reach the agent. Skills come first because company definitions (what "upset" means) decide which source to query. Every fact should carry provenance: source, fetch time, IDs and scopes, who accessed it, transformations, and an invalidation rule. The talk has no code or benchmarks, and it ends with a pitch for Merge's Gateway, Unified, and Agent Handler products.

## Key ideas
- **A context graph is the company brain: third-party systems, synced structured data, static documents, memories, and skills all feed one context layer.** — The speaker is explicitly talking about the layer that holds company context, not graph nodes and edges. Memories are formed through use, and skills are treated as a core part of the context. ([2:35](https://youtu.be/cSz7aL2nl2U?t=155))
- **Live MCP lookups cannot answer aggregate or semantic questions over large datasets, so you need a synced local copy.** — Paginating through thousands of tickets 100 at a time times out. Vendors have little incentive to offer semantic query over their APIs because it costs them compute and reduces how often customers visit their platform. ([3:58](https://youtu.be/cSz7aL2nl2U?t=238))
- **Use live MCP for single-entity lookups and actions; use a synced vector cache for semantic or cross-dataset analysis.** — Stripe-style questions about one customer or one action can stay live. Anything that needs analysis across a large set goes into a local vector DB that you build and maintain. ([4:40](https://youtu.be/cSz7aL2nl2U?t=280))
- **A router at the entry point chooses the source, and a summarizer compresses the merged live and cached results before the agent sees them.** — Retrieved context is too large to pass back raw. The summarizer returns a condensed result to the agent that sent the prompt. ([5:22](https://youtu.be/cSz7aL2nl2U?t=322))
- **Skills and memory belong in the same layer because company definitions decide where to look.** — What counts as an upset customer, or a happy one, depends on the company. The agent checks skills and memory before choosing a source, such as looking at Qualtrics survey data before ticket counts. ([6:44](https://youtu.be/cSz7aL2nl2U?t=404))
- **Four tiers of context: skills and memory, live API calls, cached sync, and derived context (stored summaries of earlier pulls).** — Live calls are cheap and simple but limited. Cached sync is needed for deep semantic questions but costs more to keep fresh. Derived context stores summaries so later questions do not re-summarize the same data. ([7:56](https://youtu.be/cSz7aL2nl2U?t=476))
- **Query flow: check skill and memory match, then check cache freshness against an SLA, fall back to the live API, loop until context is sufficient, write memory, respond.** — The loop repeats until there is enough context. Newly discovered facts can be saved as memory before the response is generated. ([9:16](https://youtu.be/cSz7aL2nl2U?t=556))
- **Store provenance for every record and define what invalidates it, because a fact can be outdated or from the wrong scope.** — Record where and when the data was fetched, the IDs and scopes used, who accessed it, which permissions applied, whether it was transformed (and what it looked like originally), and an invalidation rule such as age. ([11:42](https://youtu.be/cSz7aL2nl2U?t=702))

## Techniques
- **Split retrieval: live MCP vs. synced vector cache** — Route single-entity lookups and actions to live MCP tools. Sync third-party data into a local vector DB for semantic or cross-record questions, with metadata attached to each chunk. *When:* Use when questions range from simple per-record lookups to analysis across thousands of records, where live pagination would time out.
- **Router plus summarizer** — A router at prompt entry decides which sources to call. A summarizer merges the live and cached results into a compact context before returning it to the agent. *When:* Use when several sources feed one answer and raw retrieved data would overflow or distract the agent.
- **Skills and memory first** — Before fetching data, check for a matching skill or memory. If a skill exists, it names the sources and the procedure. If it needs no external data, respond directly. *When:* Use when the meaning of a question depends on company-specific definitions or processes.
- **Freshness SLA check on cache** — Each cached source has an SLA. If the cached data is within it, serve it. If not, call the live API and refresh the cache. *When:* Use when a cache is used for answers and stale data would lead to bad decisions.
- **Derived-context write-back** — After summarizing a heavy pull (for example, all of a customer's tickets), store the summary in the structured store, so repeated questions reuse it. *When:* Use when the same expensive summaries recur across questions.
- **Bounded live pulls** — Limit live API results to a small number, such as the last five tickets, and do not fetch the full history. *When:* Use when live calls risk timeouts and the question needs only recent items.
- **Provenance metadata on every record** — Store fetch time, source system, IDs and scopes, accessing user, permissions used, transform history, and an invalidation rule (for example, data older than one month is never used). Surface the sources in the final answer. *When:* Use for any answer that drives business decisions or needs later investigation.

## Numbers
- Merge has over 400 enterprise customers and names OpenAI, Ramp, Netflix, and Perplexity. ([0:13](https://youtu.be/cSz7aL2nl2U?t=13))
- Merge was founded six years ago, has raised three rounds, and has 130 employees. ([1:20](https://youtu.be/cSz7aL2nl2U?t=80))
- Live API pagination of about 100 tickets at a time times out when asked for a year of tickets; no specific timings given. ([3:58](https://youtu.be/cSz7aL2nl2U?t=238))
- The Acme status example caps live Zendesk pulls at five tickets to avoid timeout risk. ([13:03](https://youtu.be/cSz7aL2nl2U?t=783))
- Example invalidation rule: data more than a month old should never be considered. ([11:42](https://youtu.be/cSz7aL2nl2U?t=702))

## Hot takes
- Closing plug for Merge's products (Gateway, Unified, Agent Handler) makes this a vendor talk; quality is capped at 2 for the sponsored close.
- Deliberately avoids naming any specific technology, so the advice stays at architecture level with no benchmarks or code.
- Claims no platform is incentivized to offer semantic query over its own API; this is an unverified opinion.
- Says 'it's all physics' and that the approach is simple; in practice the sync, freshness, and provenance layers are where the difficulty lies, and the talk does not cover them in depth.

## Tools mentioned
MCP (Model Context Protocol), Zendesk, Jira, NetSuite, Stripe, Qualtrics, vector database (unnamed), Merge Unified, Merge Agent Handler, Merge Gateway

## Relevance to our work
- **agentos** (2/3): The MemoryMesh tiered memory, the cache-vs-live split, and provenance fields map directly onto this context-graph design, and provenance is missing from the current plan. → *Add provenance fields (source system, fetched_at, IDs and scopes, accessing user, transform history, invalidation rule) to MemoryMesh records, and enforce a freshness SLA check before serving cached data.*
- **prosharness** (1/3): Skills-first routing and derived-summary write-back are reusable patterns for long, checkpointed agent runs. → *Check skills and memory before any external fetch in long runs, and store summaries of heavy intermediate pulls so resumed runs do not repeat them.*
