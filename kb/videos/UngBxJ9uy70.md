# Cursor AI Had a BIG PROBLEM — I Just Found the FIX

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `UngBxJ9uy70` · [watch](https://youtu.be/UngBxJ9uy70) · **date:** 2025-11-02 · **length:** 10:01 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS host (unnamed) · **orgs:** Cursor, Google, Context7, GitMCP
- **topics:** mcp-and-tools, coding-agents, context-engineering, multi-agent · **tags:** gitmcp, mcp, context7, cursor, a2a, documentation-retrieval, hosted-mcp-server, gemini-2.5, agent-cards, rag-alternative

> AI LABS walkthrough of GitMCP, which turns any GitHub repo into a hosted MCP docs server, shown as an alternative to Context7 for keeping Cursor grounded in current docs, with a three-agent A2A demo.

## Summary
The host says Cursor's doc linking loads whole documentation sets at once, and Context7 MCP was inconsistent in his tests because Cursor sometimes ignored the instruction to use it and searched the web instead. He presents GitMCP as a free, lightweight alternative: replace github.com with gitmcp.io in a repo URL to get an MCP server scoped to that repository, then copy the provided MCP rule into the editor. He says it works with Claude Desktop, Windsurf, VS Code, Claude, and Cursor, and also with GitHub Pages docs sites, but not with docs hosted elsewhere. To test it, he had Cursor (using Gemini 2.5) build three agents that speak A2A: a main agent he talks to, an animals agent, and a plants agent, each on its own server. Routing was checked by seeing which agent's terminal received each question. He then asked the GitMCP page's chat about the tool itself and reports that it uses LLM reading of page text and READMEs rather than a vector database or classic RAG. Evidence is one anecdotal demo with no tests or benchmarks, and the title overstates the problem being solved.

## Key ideas
- **Linking whole docs into Cursor loads too much at once and hurts focus; Context7 is better but inconsistent, sometimes ignoring explicit instructions and searching the web** — Speaker's core complaint. Overlapping tools (for example MCP-related libraries) made Context7 pull unrelated content. Repo-hosted docs are especially prone to cross-linked, off-target retrieval. ([0:00](https://youtu.be/UngBxJ9uy70?t=0))
- **GitMCP turns any GitHub repo into its own scoped MCP docs server, set up by editing the URL** — Replace github.com with gitmcp.io in the repo URL. The page then provides an MCP server for that repository plus a rule to paste into the editor. Pitched as free and needing no self-hosting. ([1:22](https://youtu.be/UngBxJ9uy70?t=82))
- **Scope is limited: works with GitHub repos and GitHub Pages docs sites, not arbitrary doc sites** — He says LangGraph's Pages-hosted docs can be fed in, but docs hosted elsewhere will not work with it at the time of the video. ([2:46](https://youtu.be/UngBxJ9uy70?t=166))
- **Demo: an agent built A2A correctly from a repo's docs without the human reading the spec first** — Cursor was given the A2A protocol repo through GitMCP, then asked to build a main agent plus animal and plant specialist agents that talk over A2A. It generated the agent cards, per-agent files, a README and requirements. Speaker checked the result against the docs afterward. ([3:48](https://youtu.be/UngBxJ9uy70?t=228))
- **Multi-agent routing can be verified by watching which server logs the request** — The main agent sent a lion question to the animals agent and a plant-growth question to the plants agent. Confirmed by checking that only the target agent's server received the query. ([6:36](https://youtu.be/UngBxJ9uy70?t=396))
- **The model kept re-querying the docs while building, which he credits for the result** — He calls the continuous retrieval during the build the most important part, and says Context7 hallucinated from prompt phrasing unless explicitly told to use it. Single anecdote, not a controlled comparison. ([5:14](https://youtu.be/UngBxJ9uy70?t=314))
- **GitMCP's own chat says it does not use vector DB RAG; it reads page text and READMEs and navigates code by text search** — Speaker's self-check: the tool reportedly reads LLM-usable text from each GitHub page and README, navigates the codebase from that, and supports textual search, with no traditional retrieval-augmented generation. Evidence is the tool's self-description, so treat as unverified. ([9:13](https://youtu.be/UngBxJ9uy70?t=553))

## Techniques
- **Per-repo hosted MCP docs via URL swap** — Take a GitHub repo URL, replace github.com with gitmcp.io, open the page, copy the MCP config or rule shown there, and add it to the editor (Cursor in the demo). Keep the rule in the editor's rules so the model consults the server before answering. *When:* A library or protocol is new or post-training-cutoff, and you want the model grounded in that repo's own docs instead of pasting READMEs or linking a whole doc set.
- **Scope docs to one repo instead of a broad doc index** — Attach one MCP server per repository, not one shared index. Each server answers only from that repo's content, which limits cross-talk when several related tools (such as overlapping MCP libraries) are in use. *When:* Several overlapping tools or frameworks are in one project and a generic docs retriever keeps mixing their content.
- **Use the hosted repo chat as a post-build spec check** — After the agent implements something, open the same gitmcp.io page and ask it questions about the protocol or API to confirm the implementation matches the documented behavior. *When:* You want an independent check of generated code against docs you have not read yourself.
- **Router agent plus domain specialist agents over A2A** — One main agent receives user questions and forwards each to the right specialist (animals, plants) over A2A. Each specialist runs as its own server with its own domain-focused knowledge. Prompt the coding agent to build this way and have it write a README and requirements file. *When:* A single broad model or knowledge base is less accurate than several narrow domain agents, and you want a clear routing boundary between them.
- **Routing check by server log** — Start each agent in its own terminal. Send test questions through the main agent and confirm which specialist terminal received each one; a correct route shows up in exactly one specialist's log. *When:* You need a fast manual check that multi-agent routing works before writing automated tests.

## Numbers
- GitMCP setup is a URL edit (github.com to gitmcp.io); the host says it takes seconds ([1:22](https://youtu.be/UngBxJ9uy70?t=82))
- Demo built three agents (main, animals, plants) on separate servers ([5:14](https://youtu.be/UngBxJ9uy70?t=314))
- Host tested Gemini 2.5 inside Cursor for the build; no benchmark or error-rate data given ([0:00](https://youtu.be/UngBxJ9uy70?t=0))
- Speaker reports the chat's free models are less capable than top models but adequate for doc Q&A; no measured numbers ([3:48](https://youtu.be/UngBxJ9uy70?t=228))

## Hot takes
- The title frames a problem as big and solved, but the evidence is one anecdotal A2A demo with no tests, error rates or controlled comparison against Context7.
- The 'no errors' claim for the A2A build rests on the host's own check of routing and reading the agent cards, not on automated verification.
- Claims about GitMCP's internals (no RAG, free chat models) come from the tool's own chat, not from its source or docs.
- Context7 is criticized from one editor (Cursor) and one model (Gemini 2.5); the failure rate may depend on setup and prompt wording.

## Tools mentioned
Cursor, Gemini 2.5, GitMCP (gitmcp.io), Context7 MCP, MCP (Model Context Protocol), A2A (Google Agent-to-Agent protocol), Claude Desktop, Windsurf, VS Code, Claude, LangGraph (docs example), Three.js (demo project)

## Relevance to our work
- **agentos** (1/3): Per-repo MCP doc servers are a retrieval alternative to our knowledge-bucket RAG for code and library docs, but it is a coding-editor tool, not a replacement for MemoryMesh's hybrid retrieval. → *Try a gitmcp.io server for one dependency we use (such as vLLM or Ray Serve docs) in the editor and compare its answers against our own docs retrieval on three concrete questions before deciding whether it is worth more.*
- **prosharness** (1/3): ProsHarness wraps Claude Code, and per-repo docs MCP servers could give plan and critique stages current library docs without pasting them into context. → *Evaluate whether adding one gitmcp.io docs server to the Claude Code config for a long-run task reduces the number of plan revisions in the critique step.*
