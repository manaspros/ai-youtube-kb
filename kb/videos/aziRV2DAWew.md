# MCP-UI could be the future - Here's Why

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `aziRV2DAWew` · [watch](https://youtu.be/aziRV2DAWew) · **date:** 2025-11-02 · **length:** 7:35 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Shopify, Anthropic, OpenAI, Block (Goose), Apple, Amazon, Nike
- **topics:** mcp-and-tools, product-ux · **tags:** mcp-ui, mcp, ui-resources, iframe, remote-dom, goose, postmessage, tanstack-router, react, agent-ui, chat-commerce

> Better Stack demos MCP-UI, an add-on that lets MCP tools return sandboxed UI components (mainly iframes) instead of text, and argues it could shape how chat apps handle commerce and brand-controlled UI.

## Summary
The host argues that MCP tool results are usually walls of text, which is a poor shopping experience, and shows MCP-UI as a way for an MCP server to return interactive UI components. In the demo, a Goose chat client shows a shirt shop's own variant picker and live stock indicator, rendered from the shop's website. Clicking add-to-cart sends a prompt back to the client, which triggers a second MCP tool (checkout). Server-side, MCP-UI is a thin layer over the Anthropic MCP SDK: one import and one createUIResource call that returns an external-URL iframe resource. The website side needs no MCP-UI package, only a React page plus two small helpers (a init hook that reports document height so the host can resize the iframe, and a message function that posts to window.parent). The host mentions two other content types, rawHtml and Shopify's Remote DOM, but says he does not fully understand Remote DOM. The closing argument is that brand control and richer in-chat UI (seat pickers, games) are the upside, while whether OpenAI adopts the spec, and whether it becomes a paid app store, are open questions. The video is a short intro with little code and mostly speculation about the future.

## Key ideas
- **MCP tools returning plain text are a poor UI for things like shopping. MCP-UI lets an MCP server return UI components the client can render.** — Demo compares a text dump of two shirts with the same data shown as a proper interactive component. The speaker says the text is accurate but the experience is bad. ([0:00](https://youtu.be/aziRV2DAWew?t=0))
- **The UI is owned by the website, so its data stays current. The component can also send actions back to the client, which then calls another MCP tool.** — The variant picker updates the image, and stock per variant comes from the shop's own data. Add-to-cart sends a prompt to the client that triggers a checkout tool. The spec can also send tool calls automatically, but Goose has not implemented that yet. ([1:12](https://youtu.be/aziRV2DAWew?t=72))
- **On the server, MCP-UI is a small add-on to the standard Anthropic MCP SDK. Only one import and one resource-creating call are MCP-UI specific.** — The tool returns createUIResource output as content. The resource type is externalUrl, and the payload is the iframe URL. Everything else is a normal MCP server. ([2:14](https://youtu.be/aziRV2DAWew?t=134))
- **The simplest content type is an iframe pointing at a page on your own site. The idea is to split UI into small per-component pages, not to embed the whole site.** — The shirt component is a /shirts route pulled out of the larger app. Other types are rawHtml (an HTML string, for very simple cases) and remoteDom (Shopify's project, which runs UI logic in a restricted sandbox while rendering happens on the client; the speaker only skims it). ([3:35](https://youtu.be/aziRV2DAWew?t=215))
- **The website needs no MCP-UI package. It is a plain React page with two helpers: one reports document size so the host can auto-size the iframe, and one posts messages to the parent window.** — The message helper first checks that the page is inside an iframe, so the same code can run on the normal site without errors. Messages go through window.parent.postMessage, which is standard browser iframe messaging. ([4:58](https://youtu.be/aziRV2DAWew?t=298))
- **The speaker's case for the approach is brand control, keeping UX designers in the loop, and richer chat UI such as a concert seat picker or an in-chat game.** — He says brands like Apple, Amazon or Nike would not want all shopping to be plain text in ChatGPT with no custom branding. ([5:55](https://youtu.be/aziRV2DAWew?t=355))
- **Open questions are whether OpenAI would adopt the spec, and whether it turns into an approved-integrations app store that takes a cut of purchases.** — He is skeptical about OpenAI, but says it could work for approved integrations. The cut is speculation, not something shown. ([7:05](https://youtu.be/aziRV2DAWew?t=425))

## Techniques
- **Return an iframe UI resource from an MCP tool** — Install the MCP-UI add-on alongside the Anthropic MCP SDK (package name not shown in the video). In the tool handler, call createUIResource with a custom UI name and content of type externalUrl whose payload is the iframe URL, then return the resource as tool content. Use the normal MCP server otherwise. *When:* When a tool's answer is better as an interactive component (a product variant picker, a stock indicator) and you control the UI in the website.
- **Extract one component into its own route** — Pull a single piece of your UI (the demo uses a /shirts route in TanStack Router) into its own page, and use that page as the iframe. Do not iframe the whole site. *When:* Always, for chat UIs. Keeps the chat from becoming a browser and keeps each iframe focused.
- **Auto-size the iframe from the page** — On page load, a helper hook reports the document's size to the host via postMessage. The host resizes the iframe to fit, so the component looks native. *When:* Any iframe-based MCP UI whose height varies with content.
- **Send component actions back to the host as messages** — Inside the iframe, guard with a check that the page is actually framed, then call window.parent.postMessage. The demo's sendMCPMessage turns an add-to-cart click into a prompt that makes the client call a checkout tool. The exact message schema is not shown. *When:* When a UI action should drive a second tool call (add to cart, then checkout), and the host supports it. Note that auto tool-call messages are in the spec but were not implemented in Goose at the time.
- **Pick the content type by complexity** — Use externalUrl (a full page you host) by default. Use rawHtml only for one-off, self-contained markup. Treat remoteDom (Shopify) as a separate, more complex option that runs UI logic in a sandbox; the speaker does not cover how to use it. *When:* externalUrl for production-like components, rawHtml for quick prototypes, remoteDom only after reading its own docs.

## Numbers
- Demo shop has two shirts in stock; the text-only answer was accurate but was a poor experience. ([0:00](https://youtu.be/aziRV2DAWew?t=0))
- Speaker says iframes date from 1997 in Internet Explorer, so the technology is old and well understood. ([2:14](https://youtu.be/aziRV2DAWew?t=134))
- Video length is about 7:35, and it is a single-demo intro rather than a benchmark or cost study. ([0:00](https://youtu.be/aziRV2DAWew?t=0))

## Hot takes
- MCP servers should return UI components, not text, and that UI should be owned by the brand that built it.
- The simplest route (an iframe to a site you already run) is the right default. Remote DOM is too complex to recommend yet.
- OpenAI may adopt this only for approved integrations, which could become an app store that takes a cut of purchases. This is speculation only.

## Tools mentioned
MCP-UI, Model Context Protocol (MCP) SDK (Anthropic), Goose (client), ChatGPT, Remote DOM (Shopify), React, TanStack Router, iframe / window.postMessage

## Relevance to our work
- **prosharness** (1/3): ProsHarness has phone-driven approvals. An MCP tool that returns a small approval card could be a richer approval surface than plain text, but the video only shows one-way clicks in a chat client. → *Only if ProsHarness exposes approvals through an MCP server, prototype one approval card as an externalUrl MCP-UI resource and compare it with the current phone flow. Otherwise skip.*
