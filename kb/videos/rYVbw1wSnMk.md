# Copilot Kit Made My React App Think For Itself Using AI

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `rYVbw1wSnMk` · [watch](https://youtu.be/rYVbw1wSnMk) · **date:** 2025-11-02 · **length:** 4:50 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** CopilotKit, Anthropic, Composio, Vercel, Better Stack
- **topics:** mcp-and-tools, product-ux, dev-tools · **tags:** copilotkit, react, vite, express, mcp, composio, vercel-ai-sdk, self-hosted, frontend-actions, readable-context, chat-ui

> A 5-minute walkthrough of CopilotKit, which lets a React app expose its data to an LLM, let the model change app state, and call MCP tools, with a self-hosted Express runtime.

## Summary
The video demos CopilotKit on a Vite + React starter app. The chat can answer questions about on-page text and the counter value, and it can change the counter from 4 to 23 through an action. The narrator says it can also call GitHub tools through a Composio MCP server. The architecture has three parts: a self-hosted Express runtime endpoint on port 4000 that holds the Anthropic key and talks to the LLM, a frontend wrapped in the CopilotKit provider pointed at that endpoint, and hooks that supply readable app data and define actions. Self-hosted MCP was the hard part. The MCP SDK's types did not match what CopilotKit expected, so the narrator used Vercel's AI SDK experimental MCP client with a specific transport config, while cloud-hosted MCP needed only frontend changes. The narrator also says CopilotKit's suggestions, predictive text and local-storage chat persistence work, but does not show them, and lists unmet wishes: other models via LiteLLM and stdio MCP transport. Code is not shown on screen, so the steps are not reproducible from the video alone.

## Key ideas
- **CopilotKit gives a React app LLM chat that can read app data, change app state, and call MCP tools without a custom backend.** — The narrator frames it as works with any React or React-based framework such as Next.js, and says setup is simple even for someone new to AI features. ([0:00](https://youtu.be/rYVbw1wSnMk?t=0))
- **The demo shows read and write access. The model describes on-page text, then changes the counter from 4 to 23.** — The narrator says the model can control the app and suggests uses like creating a playlist or categorizing emails. It also lists GitHub tools available through Composio MCP. He notes the first attempt errored and needed a page refresh. ([1:16](https://youtu.be/rYVbw1wSnMk?t=76))
- **The architecture has three parts: a server-side runtime endpoint, a provider wrapping the app, and hooks for context and actions.** — An Express server with CopilotKit runtime middleware holds the Anthropic API key and runs on port 4000. The frontend wraps the app in the CopilotKit provider pointed at that URL, plus a chat component with a title and LLM instructions. ([2:36](https://youtu.be/rYVbw1wSnMk?t=156))
- **Models have no app data by default, so the app's data must be passed in explicitly through a hook. Actions are a separate hook.** — The narrator puts the site's text into an object and passes it to a hook. The same approach works for dynamic data. Actions defined with a hook can do arbitrary things, including rendering UI elements in the chat. ([2:36](https://youtu.be/rYVbw1wSnMk?t=156))
- **Self-hosted MCP is the hard part. Cloud-hosted MCP needs only frontend configuration.** — The official MCP SDK client did not produce the type CopilotKit expected. The narrator read the source and switched to Vercel's AI SDK, whose MCP client is experimental and needs a specific transport configuration. ([3:58](https://youtu.be/rYVbw1wSnMk?t=238))
- **Known gaps: the narrator could not use other models via LiteLLM or stdio MCP transport, only server-sent events.** — He also says suggestions, predictive text and chat persistence in local storage exist but he did not set them up. ([3:58](https://youtu.be/rYVbw1wSnMk?t=238))

## Techniques
- **Server-side runtime endpoint for the LLM key** — Run a small Express server with the CopilotKit runtime middleware, add the Anthropic API key on the server, and listen on port 4000. The frontend provider points at this endpoint, so the key never reaches the browser. The video does not show the code, so the exact package and middleware names are not given. *When:* You want a React app to call an LLM without writing a full backend, and you want to self-host the chat runtime.
- **Expose app data to the model via a readable-context hook** — Put the data the model should see (page text, counters, dynamic values) in an object and pass it to CopilotKit's readable-data hook. Re-passing dynamic data keeps the model's view current. *When:* The user will ask questions about what is on screen, or the model needs live app state to answer.
- **Let the model change app state via an action hook** — Define actions with CopilotKit's action hook. Each action runs app code when the model calls it, for example setting a counter. Actions can also render UI elements inside the chat. *When:* The chat should do things in the app (update values, trigger workflows), not only answer questions.
- **Self-hosted MCP through the Vercel AI SDK MCP client** — Do not wire MCP through the official MCP SDK client, because its types did not match CopilotKit's expected type. Instead, use the experimental MCP client from Vercel's AI SDK on the backend with a specific transport configuration (the narrator uses server-sent events). The transport settings are not shown in the video. *When:* You need MCP tools (for example GitHub through Composio) available to the model in a self-hosted CopilotKit setup.
- **Cloud-hosted MCP as a frontend-only change** — With CopilotKit's cloud-hosted option, add the MCP server to the frontend configuration. No backend MCP code is needed. *When:* You want MCP tools without running a backend MCP client, and you accept CopilotKit's hosting.

## Numbers
- Demo counter changed from 4 to 23 by a natural-language instruction, showing the model can drive app state. ([1:16](https://youtu.be/rYVbw1wSnMk?t=76))
- Self-hosted runtime Express server listens on port 4000, with the Anthropic API key added to it. ([2:36](https://youtu.be/rYVbw1wSnMk?t=156))
- Narrator says self-hosting CopilotKit is free, but LLM API token costs are not discussed. ([1:16](https://youtu.be/rYVbw1wSnMk?t=76))
- Video length 4:50. ([0:00](https://youtu.be/rYVbw1wSnMk?t=0))

## Hot takes
- Cost framing is partial: the 'completely free forever' claim covers self-hosting the CopilotKit runtime, while the Anthropic API bill is not discussed.
- Self-hosted MCP is presented as much harder than cloud-hosted MCP, and the workaround (Vercel AI SDK instead of the MCP SDK) is undocumented, so a reader needs the source code or docs.
- The walkthrough is light on code: no file contents, package names or config keys are shown, so it is more of a product tour than a tutorial.
- Title hype ('Think For Itself') is well above what the video demonstrates. Capabilities like suggestions and persistence are mentioned but not shown.
- Quality capped at 2: the hype title and thin, code-free substance, with no sponsor segment seen.

## Tools mentioned
CopilotKit, React, Vite, Tailwind CSS, Next.js, Express, Anthropic API (Claude), Composio (MCP server), GitHub (via Composio MCP tools), Model Context Protocol SDK, Vercel AI SDK (experimental MCP client), LiteLLM (mentioned as a wish, unmet), DeepSeek and Llama (mentioned as wishes)

## Relevance to our work
- **agentos** (1/3): The runtime endpoint that keeps the LLM key server-side and proxies chat is a similar shape to the proxy layer AgentOS wants, but this is a frontend-facing thin layer, not a gateway. → *Check how an AgentOS-style gateway would expose MCP tools to a browser client, and whether its MCP transport supports stdio as well as SSE.*
