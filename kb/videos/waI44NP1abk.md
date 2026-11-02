# Rebuilding the web for agents — Liad Yosef, MCP Apps

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `waI44NP1abk` · [watch](https://youtu.be/waI44NP1abk) · **date:** 2026-09-18 · **length:** 20:41 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Liad Yosef · **orgs:** Aura, Shopify, Anthropic, OpenAI, Google, Vercel, Cloudflare, Salesforce, Sentry, Mixpanel, PostHog
- **topics:** mcp-and-tools, product-ux · **tags:** MCP Apps, WebMCP, agentic web, llms.txt, AI Catalog.json, agentic resource discovery, headless web, agent readiness, Aura Journey, harness comparison, accessibility

> Liad Yosef (MCP Apps co-maintainer) argues the web is shifting to assistant-driven, headless-plus-UI interaction, and that agent-readiness should be measured from agents' real behaviour, not from best-practice files.

## Summary
The speaker, a co-maintainer of the MCP Apps spec and co-founder of Aura, argues that assistants are becoming the main entry point to the web. MCP Apps lets a service send UI pieces into a chat, which covers the "last mile" where a human must pick a hotel, seat or option. He says websites are going headless and that a "nearly headless web" will serve agents through APIs and tools, returning UI only when a human must choose. He contrasts browser-driving agents with Google's WebMCP, where the page exposes JavaScript tools, and calls screenshot-based browsing a faster-horse approach. For agent-readiness he points to discovery, description, auth and payment as separate problems. His main empirical finding is that about half of tested sites publish llms.txt but agents almost never read it, so he proposes measuring real agent paths across several harnesses rather than writing best practices. He ends by proposing AI Catalog.json and agentic resource discovery as the missing discovery layer, and says human accessibility and agent accessibility overlap. Several claims are promotional for his company's tools and are unverified in the talk.

## Key ideas
- **MCP Apps sends UI components into chat, so services keep their brand and fill the last mile of interaction.** — Agents can do much autonomously, but a human still chooses a hotel, a seat or a 3D model. MCP Apps lets the service's own UI appear inside the chat, which keeps user trust because the user sees who they are dealing with. ([1:08](https://youtu.be/waI44NP1abk?t=68))
- **The agentic web means assistants compose services' UI atoms around the user's intent.** — Instead of visiting many sites and re-stating the same intent in each, the assistant pulls only the pieces it needs (e.g. a map from a booking service). Services then skip building their own integrations with the user's calendar or other tools. ([3:35](https://youtu.be/waI44NP1abk?t=215))
- **Browser-driving agents are a stopgap; WebMCP has the site expose tools instead of screenshots.** — The speaker calls computer-use and browser agents a faster-horse solution that inherits human UI limits such as filters and pagination. Google's WebMCP lets the page publish JavaScript tools for the agent to call. He says the approach works for simple cases like finding deals but not for a full internal dashboard. ([6:27](https://youtu.be/waI44NP1abk?t=387))
- **The web is going nearly headless: agents use APIs and tools, and UI comes back only when a human must choose.** — He cites Salesforce, Cloudflare and Sentry moving toward API-first surfaces. Agent-ready sites must serve both agent-to-site calls and human customers who still browse. Agent experience is split from the human experience, and he estimates 90% of interaction will rely on agents. ([9:10](https://youtu.be/waI44NP1abk?t=550))
- **Agent-readiness is more than discovery; it covers description, interaction, auth and payment.** — Discovery (AEO/SEO/GEO) is only the first step. After discovery an agent must know what the service is, how to call it, how to authenticate the user and how to pay headlessly. He notes brand loyalty weakens: a coding agent picked PostHog over Mixpanel because of better MCP and API quality. ([11:34](https://youtu.be/waI44NP1abk?t=694))
- **Published agent-readiness files like llms.txt are ignored by most agents in practice.** — Across the sites his team tested, about half published llms.txt, but almost no agent read it. Agents went to the docs and home pages. Agents that did read it had been pointed there by the docs. He concludes that best-practice guides go stale fast, so the agent's own feedback should define what agents need. ([13:57](https://youtu.be/waI44NP1abk?t=837))
- **Run several harnesses on the same site and intent to see the real agent path.** — His Aura Journey tool runs Claude Code, Vercel's harness and ChatGPT with the same intent and records each path. Paths differ a lot by harness, which shows that one agent's behaviour does not generalise and that the path data is what to act on. ([15:28](https://youtu.be/waI44NP1abk?t=928))
- **Discovery needs a standard layer: per-site AI Catalog.json plus a queryable directory, not web search or one central registry.** — Web search rewards human SEO, per-app registries are closed, and a central MCP registry raises curation and governance questions. He points to AI Catalog.json and the agentic resource discovery standard, which together describe how a domain and a directory expose agent resources. His team's directory is built this way. ([18:23](https://youtu.be/waI44NP1abk?t=1103))
- **Human accessibility and agent accessibility reinforce each other.** — Agents arriving at a page are like users who cannot see it, so they need the same explicit signals. Improving accessibility tends to improve agent access, and the reverse holds too. ([19:23](https://youtu.be/waI44NP1abk?t=1163))

## Techniques
- **Expose UI as MCP Apps for the last mile** — Have the MCP server return UI resources that render inside the chat, so the user can pick options (seat, hotel, 3D model) with the service's own branded UI. *When:* A tool call needs a human choice that text cannot carry well.
- **WebMCP: publish page tools instead of screenshots** — Expose JavaScript tools from a web page so in-browser agents call a defined function rather than parsing screenshots. *When:* A site wants an in-browser agent to act on it without visual scraping; best for narrow, simple actions.
- **Measure agent paths, not best-practice checklists** — Run multiple agent harnesses against the same site with the same intent, record the navigation path, and see which files or pages agents actually read before changing the site. *When:* Deciding what machine-readable files or docs to publish for agents, instead of trusting published guidance.
- **Per-domain AI Catalog.json plus a queryable directory** — Publish a catalog file per domain listing MCP and API endpoints, and expose an aggregating directory that agents can query under the agentic resource discovery standard. *When:* Building a discovery layer for agent-accessible services or a registry of agent resources.
- **Design an API-first surface, then add UI for the last mile** — Make the service callable headlessly first, and render UI only for steps that need human choice. *When:* Designing a product that agents will mainly use but humans still review or approve.

## Numbers
- About 50% of the websites tested by his team published an llms.txt file. ([13:57](https://youtu.be/waI44NP1abk?t=837))
- About 40% of the agents that used llms.txt did so only because the docs pointed to it; almost all others went straight to the docs and home pages. ([13:57](https://youtu.be/waI44NP1abk?t=837))
- Aura Journey has been run tens of thousands of times to see how agents move through websites. ([15:28](https://youtu.be/waI44NP1abk?t=928))
- He says MCP server best practice moved from three-paragraph tool descriptions six months ago to three lines now. ([13:57](https://youtu.be/waI44NP1abk?t=837))
- He estimates 90% of web interaction will rely on agent experiences. ([10:36](https://youtu.be/waI44NP1abk?t=636))
- MCP Apps is supported across every chat agent except Gemini, per the speaker. ([3:35](https://youtu.be/waI44NP1abk?t=215))
- He cites a Cloudflare CEO post saying agent traffic has surpassed human traffic on the web (unverified claim, repeated from a tweet). ([9:10](https://youtu.be/waI44NP1abk?t=550))

## Hot takes
- Websites as the source of truth will go away, and assistants will be the only gate to the web.
- Browser and computer-use agents are a faster-horse solution; the right path is services exposing tools.
- Published llms.txt and similar best-practice files are mostly ignored by agents, so agents should define what they need.
- Agent-readiness and human accessibility are essentially the same problem.

## Tools mentioned
MCP Apps, WebMCP, llms.txt, AI Catalog.json, Agentic Resource Discovery standard, auth.md, pricing.md, x402, Aura Journey, Aura readiness benchmark, Claude Code, ChatGPT

## Relevance to our work
- **general** (2/3): The llms.txt finding and the multi-harness path comparison are a concrete method for checking whether an agent-facing file is used, with no vendor-neutral numbers. → *Before adding agent-facing docs or context files, run two or three agent harnesses on the same task and log which files they actually read.*
- **prosharness** (1/3): MCP Apps could give ProsHarness phone-driven approvals a richer UI than plain text, but the talk does not address harnesses that wrap the Claude Code CLI. → *Check the MCP Apps spec to see if a phone approval prompt could be rendered as an app UI instead of text.*
