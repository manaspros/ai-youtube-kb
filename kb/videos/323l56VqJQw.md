# Context7 MCP Tutorial: Get Instant RAG for Your AI Coders

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `323l56VqJQw` · [watch](https://youtu.be/323l56VqJQw) · **date:** 2025-11-02 · **length:** 6:43 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Cursor, Context7
- **topics:** mcp-and-tools, coding-agents, context-engineering · **tags:** context7, mcp, cursor, version-aware-docs, documentation-retrieval, mcp-use, playwright-mcp, cursorignore, claude-3.7

> Tutorial on wiring the Context7 MCP server into Cursor so the agent pulls current, targeted library docs instead of stale training data or whole doc files; the evidence is one informal before/after build.

## Summary
The speaker argues that coding agents are limited by training cutoffs, so they suggest outdated install commands for libraries such as shadcn/ui. Cursor's add-docs feature loads whole documentation sets into context, which the speaker says makes the context heavy and the output worse on larger projects. He presents Context7, an MCP server that exposes a curated doc index with code examples, and shows setup in Cursor via the MCP settings panel using the install snippet from the project's GitHub README. In a single comparison, he builds an mcp-use Airbnb agent once with the docs feature (a small single-file doc) and once with Context7; the Context7 run added a Playwright MCP integration and extra features, which he attributes to pulling only the relevant pieces. He also notes that API keys in a .env file can be kept out of the agent through .cursorignore, and tours the Context7 site, which lists about 800 frameworks with token counts and an adjustable token limit. Versioned docs are described as a requested feature, not yet available.

## Key ideas
- **Coding agents trained on a cutoff suggest outdated APIs and install commands (example: an old shadcn/ui install command). Fixing that needs current docs in context.** — The speaker names Claude 3.7 as the model in use and says the agent kept running a replaced shadcn/ui install command. ([0:00](https://youtu.be/323l56VqJQw?t=0))
- **Cursor's add-docs feature is weak for larger projects because the agent pulls from both the project and the docs at once, which bloats context and degrades output.** — He says it works on small projects with a single-file library, but breaks down on a Next.js app with microservices. ([0:00](https://youtu.be/323l56VqJQw?t=0))
- **Targeted doc lookups beat attaching a whole doc set. In one build, the Context7 run went further than the attached-docs run.** — The docs-feature run used one small mcp-use doc file and produced a basic agent. The Context7 run pulled specific sections, added a Playwright MCP integration, and extended the agent. This is a single anecdotal comparison with no metrics. ([1:25](https://youtu.be/323l56VqJQw?t=85))
- **Context7 is set up as a standard MCP server with no API key or auth. The same install command works across MCP clients.** — Install support is listed for Cursor, Windsurf and VS Code (GitHub Copilot agent). Cursor's MCP settings take the pasted config. If tools don't appear, refresh, then restart the editor. ([3:54](https://youtu.be/323l56VqJQw?t=234))
- **Secrets can be kept out of agent context with a .cursorignore entry for the .env file, which also disables AI features on it.** — The speaker shows AI features disabled for the .env file containing API keys, and says the file is declared in .cursorignore. ([3:54](https://youtu.be/323l56VqJQw?t=234))
- **The Context7 site indexes about 800 frameworks and shows token counts per doc page. You can raise the token limit for broader results and copy the content into any LLM or editor.** — Searching a page for a term such as Pages Router filters the relevant sections. Per-version docs are described as a feature being requested, not yet available. ([5:22](https://youtu.be/323l56VqJQw?t=322))

## Techniques
- **Add Context7 as an MCP server in Cursor** — Open Cursor Settings, go to the MCP section, add a new MCP server, paste the config copied from the Context7 GitHub repo's install instructions, and save. Return to the MCP panel to confirm the Context7 tools are listed. The video does not show the config JSON itself, so copy it from the repo README. *When:* Use it when the agent is writing code against a library or framework whose API may have changed since the model's training cutoff.
- **Recover missing MCP tools** — If the tools don't show after adding the server, refresh the MCP list first. If they still don't appear, quit Cursor completely and reopen it. *When:* Use it right after adding any MCP server, when its tools are missing from the agent.
- **Pull targeted doc sections instead of attaching whole docs** — Let the agent query the MCP server for the specific topic it needs, rather than attaching the entire documentation set. On the Context7 site, you can browse a library's docs, search for a term, check the token count, and raise the token limit if you need broader results. *When:* Use it on large frameworks or multi-service projects, where a full doc attachment would crowd out project code in context.
- **Keep API keys out of agent context** — List the .env file in .cursorignore, so the agent does not read it, and confirm AI features are off for that file. *When:* Use it in any workspace that holds API keys or other secrets and is handled by a coding agent.

## Numbers
- Context7 covers about 800 frameworks, with token counts shown per doc page and an adjustable token limit. ([5:22](https://youtu.be/323l56VqJQw?t=322))
- Context7 needs no authentication or API key, and the speaker calls it free. ([3:54](https://youtu.be/323l56VqJQw?t=234))
- Model named as the example: Claude 3.7 (training cutoff example). ([0:00](https://youtu.be/323l56VqJQw?t=0))
- The Context7 vs docs-feature comparison is a single informal run with no timing, token or success metrics. ([1:25](https://youtu.be/323l56VqJQw?t=85))

## Hot takes
- The title's 'Instant RAG' is a misnomer. Context7 retrieves curated third-party library docs, not retrieval over your own data.
- The one before/after comparison is anecdotal, with no measurement of context size, cost or correctness, and the author ran it only once.
- The video shows the Cursor setup but not the config JSON, so a viewer must copy it from the repo README.
- Versioned docs, which the speaker says matter for larger projects, are described as a requested feature and not yet available.
- Not sponsored. The end asks for donations and the tool is free, so the quality cap is set by thin substance and the hype title, not by a sponsor.

## Tools mentioned
Cursor, Context7 MCP server (context7.com), mcp-use (auto-caption 'mcpus'; the Python agent framework built in the demo), Playwright MCP, Claude 3.7 (model named by the speaker), shadcn/ui (example library), Next.js (example framework), Windsurf, VS Code with GitHub Copilot agent, .cursorignore

## Relevance to our work
- **prosharness** (1/3): ProsHarness drives Claude Code, and this shows a version-aware docs MCP as a context-engineering option versus attaching docs. → *Test a version-aware docs MCP such as Context7 on a library-heavy ProsHarness task against a pasted-docs baseline, and compare context size and task success before adopting it.*
