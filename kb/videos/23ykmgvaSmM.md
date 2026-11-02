# I Made MCP AI Agents That Automate Every App I Build.

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `23ykmgvaSmM` · [watch](https://youtu.be/23ykmgvaSmM) · **date:** 2025-11-02 · **length:** 8:30 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Cursor, Windsurf, Anthropic
- **topics:** mcp-and-tools, coding-agents, vibe-coding-app-building · **tags:** fastapi, fastapi-mcp, mcp, cursor, windsurf, claude-desktop, nextjs, tool-naming, mcp-client, python

> Tutorial on wrapping an existing FastAPI to-do app with the FastAPI MCP server so Cursor, Windsurf, Claude Desktop, or a Python MCP-client agent can call its endpoints as tools. Covers setup, tool naming, and a registration gotcha.

## Summary
The video shows how to expose an existing FastAPI backend as MCP tools using the fastapi-mcp package, using a Next.js and FastAPI to-do app as the example. The speaker installs the package into a Python virtualenv, pastes the basic usage example from the repo, and asks Cursor to add it to the main file. Each endpoint becomes a tool, and the speaker recommends setting an operation ID per endpoint so tools get readable names instead of auto-generated ones. A gotcha: tools did not appear until the MCP server was set up after all endpoints were declared, or a re-register call was added at the bottom of the file. The backend's local MCP URL (with /mcp appended, as spoken) is then added as a global server in Cursor's mcp.json, with the same approach for Claude and Windsurf. For non-IDE agents, the speaker uses a separate Python "MCP use" client library with an agent file and a config.json that lists the MCP server, and shows an agent adding four tasks to the app. The video is short and light on detail: no code is shown in full, and there is no discussion of auth or destructive endpoints.

## Key ideas
- **A FastAPI app can be exposed to agents by adding an MCP layer that turns its endpoints into callable tools.** — The premise is that every API that drives an app becomes a ready-made tool an LLM can call. The speaker says any project can plug in, and that the same server works for Cursor, Windsurf, or Claude Desktop, or for a custom agent. ([0:00](https://youtu.be/23ykmgvaSmM?t=0))
- **Setup is an install plus pasting the repo's basic example into the main file.** — Install the FastAPI MCP package into the project's virtualenv with pip or uv (the speaker used pip), then copy the usage example from the GitHub repo and have the coding agent insert it into the main file. ([2:35](https://youtu.be/23ykmgvaSmM?t=155))
- **Tool names are auto-generated unless set explicitly, and explicit names are recommended.** — The speaker says to set an operation ID on each endpoint to control the tool name. Without this, names are generated automatically. The speaker does not show the exact parameter syntax on screen. ([4:01](https://youtu.be/23ykmgvaSmM?t=241))
- **Tools may not appear unless the MCP server is registered after all endpoints are declared.** — This was the speaker's main debugging problem. The fix is either to set up the MCP server after all endpoints are defined, or to call a re-register function at the bottom of the file. The speaker does not name the function in the transcript. ([4:01](https://youtu.be/23ykmgvaSmM?t=241))
- **Clients connect by pointing at the backend's local MCP URL, with the frontend and backend run separately.** — Run the backend with the repo's command, copy the local URL it prints, then add a new global server in Cursor's mcp.json using that URL with /mcp appended as spoken. The speaker says Claude and Windsurf are configured the same way. ([5:24](https://youtu.be/23ykmgvaSmM?t=324))
- **For agents beyond IDE clients, a separate Python MCP-client framework connects an agent to the server through a config file.** — The speaker's code uses an agent file and a config.json that holds the MCP server entry, like the client configs above. Running the agent script lets a natural-language request, such as adding four random tasks, call the server's tools. ([6:27](https://youtu.be/23ykmgvaSmM?t=387))
- **The demo is a proof of the pattern, not an evaluation.** — The speaker shows a live to-do list updating through the MCP tools, including a task created by Cursor and four tasks created by the Python agent. No failure cases, tool-call counts, latency, or security controls are covered. ([7:41](https://youtu.be/23ykmgvaSmM?t=461))

## Techniques
- **Expose a FastAPI app as MCP tools** — 1) In the project's Python virtualenv, run `pip install` for the FastAPI MCP package (uv also works). 2) Copy the basic usage example from the fastapi-mcp GitHub repo and have the coding agent add it to the main FastAPI file. This adds the MCP server to the app. 3) Run the backend with the repo's run command and copy the local URL it prints. *When:* When an existing FastAPI backend should be callable by an MCP client or an agent without writing separate tool wrappers.
- **Name MCP tools with operation IDs** — Set an operation ID on each endpoint, using a name that describes its purpose. The speaker had the coding agent add one to every endpoint. The exact FastAPI parameter is not shown on screen; the speaker refers to it as the operation ID tag. *When:* When you want readable, stable tool names for the model to pick from, instead of auto-generated names.
- **Register MCP after all endpoints are declared** — Place the MCP setup after every route is defined in the file. If it sits above some routes, call the re-register function at the very bottom of the file. The speaker says this made the tools appear. *When:* When the server runs and the MCP client connects, but no tools are listed.
- **Add the MCP server to an IDE client** — Open Cursor's mcp.json and add a new global MCP server entry that points at the backend's local URL with /mcp at the end, as spoken in the video. The speaker says Claude Desktop and Windsurf use the same approach. *When:* When you want Cursor, Windsurf, or Claude Desktop agents to call the app's endpoints during development.
- **Drive the MCP server from a custom Python agent** — Create an agent file that uses the MCP-client library (the speaker calls it the MCP use framework, name as spoken) and a config.json that holds the MCP server entry, mirroring the IDE config. Run the agent script and give it a natural-language request, such as adding four random tasks. *When:* When you want a standalone agent application to control the app through MCP, not only an IDE assistant.

## Numbers
- The agent added four random tasks in one request, and all four appeared in the app. ([7:41](https://youtu.be/23ykmgvaSmM?t=461))
- The front-end refreshes every second so tool-driven changes show live. ([5:24](https://youtu.be/23ykmgvaSmM?t=324))

## Hot takes
- The title ('Automate Every App I Build') and the opening claim about the end of buttons and dashboards overstate what a one-package endpoint wrapper shows.
- The demo is a trivial to-do app. No auth, authorization, destructive-endpoint handling, or tool-count limits are discussed, which matter for 'every app'.
- The re-registration fix is described vaguely and the function name is not given, so a viewer cannot reproduce it from the video alone.
- Thin substance for the length: no code is shown in full and the agent code is only referenced. The video also includes a subscribe and donate plug; this is not a sponsored segment.
- The speaker tells viewers to 'ignore the small front-end issue', so the demo has a visible bug left in.

## Tools mentioned
FastAPI, fastapi-mcp (FastAPI MCP package), Next.js, Cursor, Windsurf, Claude Desktop, pip, uv, MCP use framework (Python MCP client library, name as spoken), mcp.json, config.json

## Relevance to our work
- **agentos** (1/3): AgentOS's L1 proxy and tool-facing story touch MCP tool surfaces, but this video only shows wrapping a single FastAPI app as MCP tools, with no proxy, budgets, or audit layer. → *Skim the fastapi-mcp repo's operation-ID naming to see whether AgentOS tool names should be explicit and stable rather than auto-generated.*
