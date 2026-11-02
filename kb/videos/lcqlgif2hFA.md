# ChatGPT Apps vs n8n vs AgentKit: The Future of AI Automation

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `lcqlgif2hFA` · [watch](https://youtu.be/lcqlgif2hFA) · **date:** 2025-11-02 · **length:** 9:37 · **format:** tutorial · **quality:** 2/5 · **depth:** practitioner
- **speakers:** Unnamed AI LABS host · **orgs:** OpenAI, Google, ngrok, Make.com
- **topics:** mcp-and-tools, vibe-coding-app-building, product-ux · **tags:** chatgpt-apps, openai-apps-sdk, mcp, widgets, ngrok, google-places-api, developer-mode, shadcn, express, sponsored

> Walkthrough of building a ChatGPT app as a self-hosted MCP server (Express, Google Places API) exposed through ngrok and registered in ChatGPT developer mode. Title promises an n8n/AgentKit comparison that never appears.

## Summary
The host introduces OpenAI's ChatGPT apps, which run inside ChatGPT and return interactive widgets instead of plain text, and argues they point toward an app store for ChatGPT. He explains that each app is effectively an MCP server hosted behind the scenes, so a builder can host their own and give ChatGPT only the URL. The demo builds a Places app (MCP SDK + Express calling the Google Places API) and a movie-database app wrapped from an existing MCP server, using a reusable prompt that asks a coding agent (Cursor, Codex or Claude Code) to build the server from SDK and API docs. The server runs on localhost:3000, is exposed with `ngrok http 3000`, and is added in ChatGPT under Settings > Apps & Connectors with developer mode on, using the ngrok URL plus /mcp and no authentication. Iteration is done by refreshing the app to load new versions. The host closes by predicting that production versions will need proper authentication instead of ngrok. A sponsored Make.com segment opens the video, and the n8n and AgentKit comparison in the title is never covered.

## Key ideas
- **ChatGPT apps are MCP servers behind the scenes. A tool call returns a widget to render, or plain text if no widget is configured.** — This is the core architectural point: a builder can host their own MCP server and ChatGPT only needs its URL to send requests and render returned widgets. ([2:15](https://youtu.be/lcqlgif2hFA?t=135))
- **Two ways to build an app: write a new MCP server, or wrap an existing public MCP server.** — The first path is demonstrated with a Places app. The second reuses a movie-database MCP server and turns it into a ChatGPT app, skipping the API integration work. ([3:18](https://youtu.be/lcqlgif2hFA?t=198))
- **A reusable build prompt plus SDK and API docs lets a coding agent produce the server.** — The prompt asks the agent to use the MCP SDK and Express to expose one tool. The speaker attaches the apps SDK docs and the target API's docs (his example: a weather app would need the weather API docs). Cursor, Codex and Claude Code are all said to work. ([4:07](https://youtu.be/lcqlgif2hFA?t=247))
- **Local dev needs a public tunnel. The local server is exposed with ngrok, and the app stays up only while the machine is on.** — This is the speaker's own caveat, and he expects production apps to run on hosted MCP systems with real authentication rather than ngrok. ([5:20](https://youtu.be/lcqlgif2hFA?t=320))
- **Registration is done in ChatGPT's developer mode, which requires a Plus or higher account.** — Steps: Settings > Apps & Connectors > Advanced settings > enable developer mode > Create. Name and describe the app, paste the ngrok URL with /mcp appended, choose no authentication, mark it trusted, and create it. The speaker says the description field does little to help ChatGPT pick the app; this is a beta. ([6:23](https://youtu.be/lcqlgif2hFA?t=383))
- **Iteration loop: edit the server, then hit refresh on the app inside ChatGPT to load the new version. Versions are numbered; his app reached version 6.** — Widget quality is improved by asking the coding agent to use ShadCN components. The speaker calls it a subjective polish step and leaves it out of the base prompt. ([7:43](https://youtu.be/lcqlgif2hFA?t=463))
- **Speaker's thesis: ChatGPT apps are an MCP app store made accessible to non-MCP users, and visual widgets are the future interface.** — He ties this to the announced monetization path (Agentic Commerce Protocol, instant checkout such as ordering DoorDash inside ChatGPT). He notes that the available apps are limited for now and custom apps are coming. ([8:41](https://youtu.be/lcqlgif2hFA?t=521))

## Techniques
- **Prompt-driven MCP server scaffold for a ChatGPT app** — Use a template prompt in Cursor, Codex or Claude Code. Attach the ChatGPT apps SDK docs and the docs for the target API (for example, Google Places). Ask for an MCP server built with the MCP SDK and Express that exposes one tool, then fill in the API key or token the agent says to obtain and set. The prompt is said to be in the creator's Discord resources, not shown on screen. *When:* A new single-purpose tool that wraps one third-party API, where a coding agent can scaffold the server quickly.
- **Reuse an existing MCP server as a ChatGPT app** — Find a public MCP server for the data source. Run the second prompt from the video, which converts it into a ChatGPT app, instead of writing an API client. *When:* A public MCP server already covers the data you need (his example: a movie database).
- **Expose localhost with ngrok for ChatGPT** — Install ngrok, sign up, run its authentication command, then run `ngrok http 3000` (use the port the server actually listens on). Copy the forwarding URL and append /mcp. *When:* Local development and testing only. The tunnel stays up only while the machine is running.
- **Register the MCP endpoint in ChatGPT developer mode** — Settings > Apps & Connectors > Advanced settings > turn on developer mode > Create. Enter a name, a short description, and the https URL ending in /mcp. Select no authentication, mark it trusted, then create. Refresh the app after each change. *When:* Testing a self-hosted ChatGPT app with a Plus or higher account, with no auth yet.
- **Widget output over plain text, polished with ShadCN** — Configure the tool to return a widget. Without a widget it returns text. Ask the coding agent to build widgets with ShadCN components for a cleaner look. *When:* Results are better shown as cards or visual lists than as text.

## Numbers
- ChatGPT has about 800 million users (stated as 800M at the start, and later as over 700M weekly users). ([0:00 and 2:15](https://youtu.be/lcqlgif2hFA?t=0))
- The app store launch was described as still three to four months away at recording time. ([0:00](https://youtu.be/lcqlgif2hFA?t=0))
- Local server is exposed with `ngrok http 3000`, the most common setup. The port can differ, such as 3001 or 3002. ([5:20](https://youtu.be/lcqlgif2hFA?t=320))
- The speaker's movie app had reached version 6 after several iterations. ([7:43](https://youtu.be/lcqlgif2hFA?t=463))
- Sponsor claim from Make.com: over 3,000 pre-built apps. Not verified. ([1:06](https://youtu.be/lcqlgif2hFA?t=66))

## Hot takes
- ChatGPT apps 'are going to kill so many upcoming AI startups'.
- The 'golden window' for builders to get ahead before the app store launches.
- 'This is essentially an MCP store' that makes MCP accessible to anyone.
- Title promises a comparison of ChatGPT apps vs n8n vs AgentKit, but the transcript contains no n8n or AgentKit content. Clickbait-style mismatch.
- Sponsored Make.com segment at the start, about one minute of the nine-and-a-half-minute video. Quality capped at 2 per the sponsored-segment rule. The speaker also says the description field does little for ChatGPT's app recognition in beta.

## Tools mentioned
ChatGPT apps (OpenAI), OpenAI apps SDK, MCP (Model Context Protocol) SDK, Express, Google Places API, ngrok, ShadCN, Cursor, Codex, Claude Code, Make.com (sponsor), n8n (named in title only), AgentKit (named in title only), Agentic Commerce Protocol

## Relevance to our work
- **agentos** (1/3): AgentOS is an MCP-adjacent proxy. This video shows the minimal pattern for a hosted MCP server that returns UI, but nothing about routing, budgets or audit. → *Look at whether AgentOS tools need to return structured UI widgets instead of plain text, and decide whether that belongs in Crucible or the proxy layer.*
