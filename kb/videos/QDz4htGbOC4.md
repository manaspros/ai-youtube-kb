# Postman MCP Server Tutorial: Build & Run AI Agents with APIs (Postman MCP Generator + Cursor)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `QDz4htGbOC4` · [watch](https://youtu.be/QDz4htGbOC4) · **date:** 2025-11-02 · **length:** 9:44 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Postman, Cursor, OpenWeatherMap, Google Maps, Anthropic (Claude Desktop), Windsurf, Discord, Instagram, Facebook, X, Figma, OpenAI, Mastercard, Stripe
- **topics:** mcp-and-tools, coding-agents · **tags:** postman, mcp-server-generation, openapi, cursor, node, npm, env-vars, weather-api, mcp-use, tool-calling

> Tutorial on Postman's MCP generator: turn selected API requests into a locally run MCP server, then register it in Cursor and call it from the chat. Thin on depth, but the steps are reproducible.

## Summary
The host opens with a claim that front-end code is becoming less necessary because MCP servers let AI agents control an app's internal APIs. He then demos Postman's MCP generator, which builds an MCP server from chosen API requests (he uses OpenWeatherMap). Each selected request becomes one tool on a single server. Postman generates the server in 10 to 30 seconds and delivers it as a zip that runs locally, not on a hosted service. He installs dependencies with npm, starts the server with node, and puts the API key in a .env file that Postman pre-populates. He then registers the server as a global MCP server in Cursor, pointing a node command at the server file, and asks a weather question that calls the current-weather tool. He says the same approach works in Windsurf and Claude Desktop and mentions the mcp-use library for building agents on top of MCP servers, but does not demonstrate it. The video is a practical walkthrough with no sponsor segment, and its framing is mostly unsupported.

## Key ideas
- **Postman's MCP generator builds a locally hosted MCP server from any API in its catalog, not a remote one.** — The server is delivered as a zip with the full codebase so it can be embedded in an application. Any API in Postman's catalog can be used this way, including the ones he lists (Figma, OpenAI, Mastercard, Stripe, Google Maps, Discord, Instagram, Facebook, X). ([1:22](https://youtu.be/QDz4htGbOC4?t=82))
- **Each selected API request becomes one tool on a single generated MCP server.** — In the demo, three OpenWeatherMap requests were selected, which produced one server with three tools: Get Current Weather, Get Weather History and Get Forecasted Weather. ([2:36](https://youtu.be/QDz4htGbOC4?t=156))
- **API keys go in the generated .env file, not in the MCP launch command.** — Postman inserts the required variables into .env. The user pastes the real key there, and the server reads it at runtime, so the key does not have to be passed as an argument. ([4:25](https://youtu.be/QDz4htGbOC4?t=265))
- **Registering a local MCP server in Cursor is a single JSON entry.** — He adds a global server whose command is node and whose argument is the full path to the generated server file. The tools then show up in Cursor's MCP settings. The server name is arbitrary. ([5:51](https://youtu.be/QDz4htGbOC4?t=351))
- **The demo ends with a real tool call, not just a listing.** — Asked for the weather in Birmingham, the model called the current-weather tool with the location and the requested units, returned 18 degrees Celsius, and he checked that value against OpenWeatherMap directly. ([8:17](https://youtu.be/QDz4htGbOC4?t=497))
- **The 'front-end is dead' framing is an unsupported assertion.** — The argument is that because AI agents can drive an app's APIs through MCP, a traditional front-end is unnecessary. The video does not test or support this beyond a single weather query. ([0:00](https://youtu.be/QDz4htGbOC4?t=0))

## Techniques
- **Generate a local MCP server from API docs in Postman** — In Postman's API catalog, search for the API and select the requests to expose. Each request becomes a tool. Click Generate (about 10 to 30 seconds), download the zip, extract it to a folder, then run `npm install` and `node mcpserver.js` in that folder. The server is then running locally. The generated code can be modified directly. *When:* When you need a tool-callable wrapper for an existing REST API quickly, without writing the MCP server by hand. Best for read-only or low-risk endpoints, since the video shows no auth scoping or review of the generated tools.
- **Put secrets in the generated .env file** — After generation, Postman writes the required variables into .env. Paste the real API key into that file. Do not pass the key as a command-line argument to the MCP server. *When:* For any generated MCP server that needs an API key. This keeps the key out of the client's MCP config JSON.
- **Register a local MCP server in Cursor** — Open Cursor's MCP settings and add a global server. Set the command to `node` and the argument to the full absolute path of the generated server file (get it with `pwd` in the server folder, then append mcpserver.js). Give it a name and save the JSON file. The server's tools then appear in the settings list. *When:* To use a locally generated or hand-written MCP server from a coding agent in Cursor. The same pattern applies to Windsurf and Claude Desktop, according to the speaker, though he does not show those.
- **Test an MCP server through Postman** — Postman can test any MCP server, not only the ones it generates. He mentions this but does not show the steps. *When:* To check tools in isolation before wiring the server into an agent client.
- **Build an agent from an MCP server in code with mcp-use** — The mcp-use library takes an MCP server and produces an agent in your own code. He describes a voice-command weather feature built this way but does not show code. *When:* When the MCP server needs to be driven by your own application instead of an IDE chat. Treat this as a pointer to the library, not a verified pattern.

## Numbers
- The MCP server is generated in about 10 to 30 seconds after clicking Generate. ([3:22](https://youtu.be/QDz4htGbOC4?t=202))
- Three selected OpenWeatherMap requests produced a single MCP server with three tools. ([3:22](https://youtu.be/QDz4htGbOC4?t=202))
- The test query for Birmingham returned 18 degrees Celsius from the current-weather tool, which he cross-checked against OpenWeatherMap. ([8:17](https://youtu.be/QDz4htGbOC4?t=497))

## Hot takes
- The opening claim that AI agents driving an app's APIs through MCP makes a traditional front-end unnecessary is asserted, not argued or tested.
- Despite the title promising agents, the video shows a single tool call from a chat assistant in Cursor. No agent loop, multi-step task or failure case is shown.
- Generated tools are exposed without any discussion of auth scope, rate limits, or which endpoints should be exposed to a model.
- The video says the server works in Windsurf and Claude Desktop, but only Cursor is shown.

## Tools mentioned
Postman MCP generator, Postman, Model Context Protocol (MCP), FastAPI MCP library, mcp-use, Cursor, Claude Desktop, Windsurf, Node.js, npm, OpenWeatherMap API

## Relevance to our work
- **agentos** (1/3): L1 is a proxy with tool/PII scanning, and MCP tool calls would pass through it. The video only covers wiring a local MCP server into an IDE and does not touch proxy routing or budgets. → *When testing tool-call routing through the AgentOS proxy, generate one small MCP server from a public API spec with Postman's generator and use it as a fixture.*
- **prosharness** (1/3): ProsHarness has zero-token credential handling. The video's approach of keeping the API key in a .env file that the server reads, rather than in the client's MCP command, is a simple version of the same idea. → *Confirm that ProsHarness keeps MCP server keys in an env file the server reads and never passes them on the command line or in client config.*
