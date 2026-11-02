# All My AI Apps Are Connected to One MIND — With Open Memory

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `Y2XI2nk44WE` · [watch](https://youtu.be/Y2XI2nk44WE) · **date:** 2025-11-02 · **length:** 10:36 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Unnamed AI LABS host · **orgs:** Mem0, Anthropic, Cursor, OpenAI, Docker
- **topics:** memory, mcp-and-tools · **tags:** open-memory, mem0, mcp, cross-client-memory, docker, cursor, claude-desktop, project-scoping, memory-retrieval

> Tutorial on Open Memory, a self-hosted shared memory server that several MCP clients (Claude Desktop, Cursor) can read and write, with setup steps and the failure modes the host hit.

## Summary
The host argues that AI tools need one shared memory, since clients like Claude Desktop and Cursor otherwise have no awareness of each other's work. He walks through running Open Memory, a memory server from the Mem0 repo, locally with Docker, adding its MCP server to Claude and Cursor, and saving a pasted plan that the server splits into about ten grouped memories. Cross-session continuity works in his test: a fresh Cursor chat retrieved progress notes and the app's status. He also reports two limits: only plain-text content saved properly (a directory tree came back empty), and memories from two different projects (MERN and Next.js stacks) were retrieved together with a vague query. No benchmarks are given; it is a single-developer walkthrough of a beta-like tool, with a cloud option behind a waitlist.

## Key ideas
- **Motivation: AI tools (brainstorm in Claude Desktop, build in Cursor) share no context, so a change in one is invisible to the other. Open Memory aims to be one memory space across all MCP clients.** — Local by default; cloud option is on a waitlist. Open Memory is the Mem0 project's sub-folder, so the whole Mem0 repo must be cloned. ([0:00](https://youtu.be/Y2XI2nk44WE?t=0))
- **Setup is Docker-based: build containers once, then start them on later runs. The MCP server must have Docker running, and the UI is served on localhost:3000.** — Requires an OpenAI API key placed in a .env file in the API folder, because the server calls an LLM for ingestion. ([2:03](https://youtu.be/Y2XI2nk44WE?t=123))
- **Clients are connected with generated one-click install commands (shown for Claude and Cursor) rather than hand-edited MCP config. Both clients then reach the same local server.** — Each client registers under a name the user picks; the host confirmed both showed as connected. ([3:24](https://youtu.be/Y2XI2nk44WE?t=204))
- **Ingestion is not a raw dump: pasting a whole plan led the server's LLM to split it into roughly ten tasks, grouped by plan and category.** — The grouping mechanism is explained later; the host says memories linked to the same session get grouped together. ([5:25](https://youtu.be/Y2XI2nk44WE?t=325))
- **Cross-session continuity worked in the test. Progress notes saved at the end of a Cursor session were chunked and stored, and a fresh chat retrieved them after a context-size error.** — Retrieval goes through the MCP list/search tools; the client decides when to call them, so prompt wording matters. ([6:08](https://youtu.be/Y2XI2nk44WE?t=368))
- **Limitation: structured content does not survive. Asking for a full directory tree returned an empty result, so the host concludes only plain text is saved reliably.** — The agent also looped trying to locate a front-end folder it could not see, which the host tried to fix by saving the tree to memory. ([7:11](https://youtu.be/Y2XI2nk44WE?t=431))
- **Retrieving one memory also pulls in memories from the same session, which surfaced related function context. Memory was consistent across sessions and across the local client and an MCP agent.** — This linking is the server's grouping behaviour; the host inferred it from the search calls rather than from documentation. ([8:24](https://youtu.be/Y2XI2nk44WE?t=504))
- **Main failure: no project scoping. After a MERN-stack project was stored, a vague 'which tech stack' query in a Next.js project returned both stacks together.** — The host says it breaks multi-project use and suggests adding project separation; he also notes specific prompts (e.g. naming the app) help. ([9:24](https://youtu.be/Y2XI2nk44WE?t=564))

## Techniques
- **Run Open Memory locally** — Clone the Mem0 repo (git clone <repo URL>), cd into the open-memory folder, make sure Docker is running, run `make build` once, then `make up` on later runs. Copy API/.env.example to API/.env, remove 'example' from the name, and set your OpenAI API key. The UI is at localhost:3000 and the MCP server runs alongside it. *When:* Trying a self-hosted shared memory layer for multiple MCP clients on one machine.
- **Install the MCP server via generated client commands** — In the Open Memory dashboard, copy the per-client install command (shown for Claude and Cursor) and run it; it registers the MCP server with the client automatically. Give each client a distinct server name. *When:* Connecting several MCP clients to one memory server without hand-editing config files.
- **Ingest a whole plan as one memory add** — Paste the full plan text into the memory add tool via the client. The server's LLM splits it into roughly ten task memories grouped by plan and category. *When:* Moving a plan from a brainstorming client (e.g. Claude Desktop) into a build client (e.g. Cursor).
- **End-of-session progress checkpoint** — At the end of a coding session, ask the agent to save its progress notes to memory. In a new chat, ask it to search memory for progress on the project before continuing. *When:* Long build sessions that hit context limits, to resume without re-explaining state.
- **Scope retrieval with specific project wording** — Phrase queries with the project's name (e.g. 'tech stack for this specific app') and tell the client to use the MCP memory tools only, not the file system. The host's vague query caused cross-project bleed. *When:* Several projects share one memory store, to reduce cross-project retrieval.
- **Store plain-text memories, not structure** — Save memories as prose summaries. Directory trees and other structured content came back empty in the host's test. *When:* Writing memories that must be retrieved later verbatim.

## Numbers
- One pasted plan was split by the server into about ten task memories. ([5:25](https://youtu.be/Y2XI2nk44WE?t=325))
- Setup is one `make build` for the containers, then `make up` on later runs; the UI and API are reached at localhost:3000. ([2:03](https://youtu.be/Y2XI2nk44WE?t=123))
- Single-developer test only; no latency, cost, or accuracy measurements were reported. ([10:36](https://youtu.be/Y2XI2nk44WE?t=636))

## Hot takes
- Cross-project memory bleed is a real failure mode: a vague query returned memories from two different stacks together, and the host calls it a problem that could break multi-project use (9:24).
- Only plain text saved reliably; a directory tree returned an empty result (7:11).
- Ingestion needs an OpenAI key because the server uses an LLM to split content, so saving memories is not free (2:03, 5:25).
- The title ('All My AI Apps Are Connected to One MIND') oversells a single-user test; the host's own conclusion is 'a strong start' with scoping still missing (9:24).

## Tools mentioned
Open Memory (Mem0 repo), Mem0, Claude Desktop, Claude, Cursor, Docker, make, OpenAI API, MCP, Next.js, React, TypeScript, MERN stack

## Relevance to our work
- **agentos** (2/3): MemoryMesh already plans tiered cross-session memory and conflict resolution with provenance. This video shows a shared memory server failing to scope memories per project, which is the same class of problem. → *Write a MemoryMesh test where two projects with overlapping names ('tech stack') are stored, then check that a scoped query returns only one project's memories; add a namespace or project key if it does not.*
- **prosharness** (2/3): ProsHarness does checkpoint/resume of long agent runs. The video's end-of-session progress note, then resume in a new chat, is the same pattern. Its failure (structured content lost) is a warning for checkpoint formats. → *Check that ProsHarness checkpoints survive a fresh Claude Code session when stored as plain-text summaries, and that structured state (e.g. file trees) is kept in a separate file rather than only in memory.*
