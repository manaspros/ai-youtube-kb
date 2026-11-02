# The agent-ready web: Simplify user actions with WebMCP — Tara Agyemang, Google

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `ghJmWQCIHRM` · [watch](https://youtu.be/ghJmWQCIHRM) · **date:** 2026-06-18 · **length:** 21:34 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Tara Agyemang · **orgs:** Google, Google Chrome, Google DeepMind
- **topics:** mcp-and-tools, voice-multimodal, product-ux · **tags:** WebMCP, browser agents, Chrome, declarative API, imperative API, registerTool, structured tools, accessibility, semantic HTML, early preview, evals CLI, model context tool inspector

> Google Chrome DevRel on WebMCP, a proposed browser standard that lets a website expose its actions as structured tools for in-browser AI agents, with declarative and imperative APIs and an early-preview setup guide.

## Summary
Tara Agyemang from the Google Chrome team argues that agents currently scrape the DOM, accessibility tree and screenshots to act on websites, which is slow, token-heavy and brittle. She says sites should first fix semantic HTML, accessibility and Core Web Vitals, then add WebMCP, a proposed standard where a page registers its capabilities as tools an agent can call. She compares it to MCP: WebMCP is the tools part of MCP running client-side in the browser, so the tab must be open and no server is needed. Two APIs are shown: a declarative one that turns annotated HTML forms into tools with an auto-generated JSON schema, and an imperative registerTool API for multi-step UI flows, which she says is the more-used of the two. Live demos (a maze game and a vibe-coded concert ticket site) show the agent calling tools and the UI updating in step with them. The API is in early preview in Chrome 146+ behind a flag, and the speaker asks for feedback and points to an evals CLI for testing a site's tools.

## Key ideas
- **Browser agents waste effort reverse-engineering pages** — Agents pass the full DOM, read the accessibility tree, take screenshots and estimate click coordinates. The speaker says this is long, brittle and token-expensive, and an ad loading late can still break the click. ([1:10](https://youtu.be/ghJmWQCIHRM?t=70))
- **Fix web foundations before adding WebMCP** — Semantic HTML, robust accessibility, fast load times (Core Web Vitals) and clean UX flows make a site agent-ready by default. She says WebMCP only makes sense after these are in place. ([1:10](https://youtu.be/ghJmWQCIHRM?t=70))
- **WebMCP lets a site publish its actions as tools** — Instead of an agent guessing what a site does, the site gives the agent a menu of named, described actions. The speaker says this improves agent speed and reliability on the site, but gives no measured figures. ([3:46](https://youtu.be/ghJmWQCIHRM?t=226))
- **WebMCP is client-side; MCP is server-side** — MCP connects agents to a server you run, reachable at any time. WebMCP tools live in the open browser tab and only work while the user is on the page. The speaker calls the two complementary. ([10:54](https://youtu.be/ghJmWQCIHRM?t=654))
- **Declarative API for plain forms** — Adding a tool name and description to a standard HTML form makes the browser generate a JSON schema from the form fields. Extra attributes can mark whether an agent or a human filled the form. ([12:23](https://youtu.be/ghJmWQCIHRM?t=743))
- **Imperative API for complex flows** — registerTool takes a name, a description the agent uses to decide when to call it, a hand-written schema and an execute function. Execute can wrap existing JavaScript, validate input and return a result the agent reads for its next step. The speaker says this is the API most people use. ([13:48](https://youtu.be/ghJmWQCIHRM?t=828))
- **Keep the UI in sync with tool calls** — In the concert demo each tool call updates the visible page (selected VIP, quantity, a notice), so the user can follow what the agent did. The speaker recommends leaving the final checkout step to the human. ([16:34](https://youtu.be/ghJmWQCIHRM?t=994))
- **Prompt specificity changes agent efficiency** — In the maze, a vague prompt made the agent backtrack. Telling it the exit is bottom-right made its route more direct. Tool descriptions and user prompts both shape the path the agent takes. ([8:09](https://youtu.be/ghJmWQCIHRM?t=489))

## Techniques
- **Declarative tool exposure from HTML forms** — Add tool name and tool description attributes to an existing form. The browser builds the JSON schema from the form fields. Use agent-invoked attributes to tell agent-filled submissions from human ones. *When:* A standard form already does the job and you want an agent to fill it in with no extra JavaScript.
- **Imperative registerTool for multi-step UI** — Call registerTool with a name, a detailed description, a manual JSON schema and an execute function. Wrap existing JS functions, validate and trim inputs, update the DOM, and return a structured result the agent can act on. *When:* The flow spans several steps or needs custom logic that a plain form cannot express.
- **Mirror tool calls in the visible UI** — Have each tool update the on-screen state (selections, quantities, confirmations) so the user sees what the agent did and can take over at any point. *When:* Agents act on a page a human is watching, or hand control back and forth with the user.
- **Hybrid browse-then-delegate flow** — Let the user browse normally, hand a task to the agent, and take control back at any time. The page must support both the UI path and the tool path. *When:* Complex sites where users want to start manually and let the agent finish a sub-task.
- **Test tools with an inspector and evals CLI** — Use the model context tool inspector extension to list tools and call them directly or via prompt. Use the evals CLI from the GitHub repo to test your own site's tools. *When:* Before shipping WebMCP tools, to check that the agent selects and calls them correctly.

## Numbers
- WebMCP is enabled in Chrome 146 and later, behind a testing flag, and the speaker recommends Chrome Canary ([17:58](https://youtu.be/ghJmWQCIHRM?t=1078))
- The repo has about six or seven demos and an evals CLI for testing your own site's tools ([19:21](https://youtu.be/ghJmWQCIHRM?t=1161))
- Demo purchase: two VIP tickets, with the agent's three tool calls (search concerts, open concert page, purchase ticket) completing the order; the notice shows about 356 pounds spent (demo data, not a measurement) ([16:34](https://youtu.be/ghJmWQCIHRM?t=994))
- Speaker says WebMCP 'significantly improves' agent performance and reliability, but shows no benchmark numbers ([3:46](https://youtu.be/ghJmWQCIHRM?t=226))

## Hot takes
- WebMCP is the 'USB-C of AI agent interactions'
- Every website can become a high-performance API for agents
- Agents should not have to settle for token-heavy screen scraping

## Tools mentioned
WebMCP, Chrome Canary, Model Context Tool Inspector (Chrome extension), Gemini, Chrome DevTools-style flag (WebMCP testing flag), WebMCP evals CLI

## Relevance to our work
- **general** (1/3): The talk's main claim, that semantic HTML and accessibility make a site usable by agents, is a cheap general check for any web-facing agent work. → *Read the WebMCP early-preview docs and the GitHub demo repo only if browser-agent tool design comes up again.*
