# This New MCP Client Lets You Integrate So Many MCP Servers!!

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `xEyKT5iY0W0` · [watch](https://youtu.be/xEyKT5iY0W0) · **date:** 2025-11-02 · **length:** 9:41 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed presenter (AI LABS channel host) · **orgs:** Composio, Vercel, LangChain (LangSmith), OpenAI, Cursor, Windsurf, Google, Notion, Reddit, Trello, Discord
- **topics:** mcp-and-tools, security-guardrails · **tags:** mcp-client, composio, oauth, sse-transport, stdio-transport, open-source, langsmith, google-tasks, hacker-news-mcp, agent-auth

> Walkthrough of an open-source general-purpose MCP client that runs an agent over MCP servers outside coding IDEs, using Composio-hosted servers with agent-driven auth; the local install is slow.

## Summary
The presenter argues that Cursor and Windsurf expose MCP tools only through coding-focused agents, so non-coding MCP servers (email, drive, notes, tasks) need a separate client. He demos the open-source "Open MCP client" (hosted on Vercel, source on GitHub), which has its own agent and lets you add servers by SSE URL or by stdio command. Composio.dev is presented as a catalog of 100+ hosted MCP servers that handle execution and authentication, so no local process or API keys in config files are needed. The demo connects a Google Tasks server through an OAuth flow the agent initiates in chat, then lists tasks; the first listing failed and a retry worked, which he attributes to UI, LLM, or agent without checking. He then shows a local install (clone, env files holding LangSmith and OpenAI keys, two dev processes, pnpm and Poetry) and reports it was slow and needed full binary paths for tools. The video is an informal, promotional tour with no measurements.

## Key ideas
- **A general MCP client is needed because IDE clients limit MCP tools to coding tasks** — The presenter says Cursor and Windsurf expose MCP servers through coding-oriented agents. Non-coding servers such as Gmail, Drive, Notion or Google Meet need a separate client, and he positions the Open MCP client as one. ([0:00](https://youtu.be/xEyKT5iY0W0?t=0))
- **Servers are added by transport type, name, and URL or command** — In the client's add-server form you choose Standard IO or SSE, give the server a name, then paste an SSE URL or enter a stdio command (for example npx plus a package name). The added server then appears in the chat interface. ([1:27](https://youtu.be/xEyKT5iY0W0?t=87))
- **Composio hosts MCP servers so no local process or env vars are needed** — Composio.dev is shown as a library of 100+ automatically managed MCP servers. You paste the SSE URL it generates, and Composio runs the server and handles authentication. ([2:49](https://youtu.be/xEyKT5iY0W0?t=169))
- **Auth runs through the agent, either OAuth or an API key typed in chat** — The agent first checks whether the connection is active, then initiates it if not. OAuth opens a browser flow that completes the link. API-key services prompt for the key in chat. The presenter says this removes manual config-file key handling. ([4:13](https://youtu.be/xEyKT5iY0W0?t=253))
- **Demo: connection check, OAuth, then listing tasks** — The Google Tasks server first reports no connection, the agent produces an auth link, and after the browser form the connection is active. Listing tasks then returns two task lists with one task each. ([5:38](https://youtu.be/xEyKT5iY0W0?t=338))
- **Rough edges: the first task listing failed, and a retry worked** — Task retrieval failed on the first try. A second prompt succeeded, which he attributes to a UI issue, but he admits he could not tell whether the cause was the LLM, the UI, or the agent. ([6:50](https://youtu.be/xEyKT5iY0W0?t=410))
- **Local install is slow and has permission limits** — Running it locally needed two processes in separate terminals, which he says helped with error logs. The local build was slow, he could not tell which model the hosted version uses, and tools needed full binary paths (for example for bun). ([7:51](https://youtu.be/xEyKT5iY0W0?t=471))

## Techniques
- **Adding a remote MCP server to a generic client** — Open Add Server, choose SSE, name it (for example 'gmail mcp'), paste the URL, and the tools show up in chat. For stdio servers, pick Standard IO and enter the command and arguments, such as npx plus the package path. Composio-generated SSE URLs are shown as secret, so do not share them. *When:* When you want MCP tools from a client that is not an IDE, or when you want to avoid running servers locally.
- **Agent-driven auth for hosted MCP servers** — Step 1: ask the agent to check the connection, which runs a status tool. Step 2 (if not connected): ask it to initiate the connection. For OAuth, open the link it returns and finish the form in the browser. For an API key, paste the key into the chat when the agent asks. Step 3: re-check the connection, then use the tools. *When:* When a third-party service needs auth and you want to avoid putting API keys in env files or config. The presenter presents this as Composio's method.
- **Running the open client locally** — Clone the GitHub repo, cd into it, and create an env file (in any editor) with a LangSmith API key. He said the personal key worked and the service key was not tested. Add an OpenAI API key, since the setup uses OpenAI models. Run the two dev commands from the repo's instructions in separate terminals, with pnpm for the frontend (pnpm run dev) and Poetry installed for the Python side. Exact env variable names are not shown in the video. *When:* When you want to self-host the client instead of using the hosted Vercel version, for example to inspect or change the code. Expect a slow start and set tool paths explicitly.

## Numbers
- Composio provides over 100 automatically managed MCP servers ([2:49](https://youtu.be/xEyKT5iY0W0?t=169))
- Demo used two MCP servers (Google Tasks and Hacker News) and then added a Gmail MCP server over SSE ([1:27](https://youtu.be/xEyKT5iY0W0?t=87))
- Google Tasks demo: two task lists, one task each, after OAuth connection ([5:38](https://youtu.be/xEyKT5iY0W0?t=338))
- Task listing failed on the first attempt and succeeded on a retry ([6:50](https://youtu.be/xEyKT5iY0W0?t=410))
- Video length 9:41, published 2025-11-02 ([0:00](https://youtu.be/xEyKT5iY0W0?t=0))

## Hot takes
- The title's 'So Many MCP Servers' hype is backed mostly by a tour of one demo, not by comparisons or reliability data.
- The presenter says the open client's built-in agent is 'not quite on the level' of Cursor or Windsurf, which is an unmeasured comparison.
- The Composio segment is promotional (pitch-style, no caveats about pricing, lock-in or data handling), so it caps the quality score.
- Forecasts (voice control, Discord, Google Maps automation, personal-assistant clients) are speculation with no evidence in the video.
- Hosted credentials are described as 'secure', but the video does not explain where the tokens are stored or who holds them.

## Tools mentioned
Open MCP client (open-source MCP client app, hosted on Vercel, source on GitHub), Composio (composio.dev, hosted MCP server catalog with auth), Google Tasks MCP server, Hacker News MCP server, Gmail MCP server, Google Drive MCP server, Notion MCP server, Google Meet MCP server, Cursor, Windsurf, LangSmith, OpenAI models, pnpm, Poetry, npx, bun, ChatGPT

## Relevance to our work
- **agentos** (1/3): AgentOS is a proxy with MCP-adjacent tool and budget concerns, but this is a client-side demo of MCP servers with no architecture detail that changes AgentOS. → *Note for later: hosted MCP servers with managed OAuth could be a tool source for agent-facing connectors, if AgentOS ever needs third-party SaaS tools.*
- **prosharness** (1/3): ProsHarness has zero-token credential handling, and this video shows an agent-mediated OAuth and API-key flow that keeps keys out of config files. The approach is a useful contrast. → *Compare ProsHarness's zero-token credential handling with the agent-driven OAuth or API-key prompt flow shown here, and check that the approval path does not put raw keys in chat transcripts.*
- **general** (1/3): Mostly a client tour. Only the separation of general-purpose MCP clients from IDE agents is relevant to the recurring interest in agent tooling. → *Read the open MCP client repo's README only if MCP-based personal automation becomes a project goal.*
