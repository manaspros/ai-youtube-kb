# AI Memory Explained: SuperMemory MCP for Cursor, Claude & Windsurf

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `mKXzPVIMFYE` · [watch](https://youtu.be/mKXzPVIMFYE) · **date:** 2025-11-02 · **length:** 7:34 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** SuperMemory
- **topics:** memory, mcp-and-tools, context-engineering · **tags:** supermemory, mcp, cross-client-memory, cursor, claude-desktop, windsurf, persistent-context, project-rules, keyword-search

> Walkthrough of SuperMemory MCP: one hosted memory store shared across Cursor, Claude Desktop and Windsurf through add and search MCP tools, plus an IDE rule that auto-saves project changes.

## Summary
The host argues that AI tools do not share memory and that an MCP server can act as a personal memory store carried across clients. The demo builds a small plant water-tracker app in Cursor, has Cursor summarize the project (initial prompt, tools, structure, features) and save it to memory, then has Claude Desktop search that memory to plan new features. A project-specific Cursor rule is shown that tells the agent to upload any app change (structural, dependency, text edits) to memory automatically, with the rule type set to "always". The MCP exposes two tools: an add tool that stores text verbatim and a search tool that takes a keyword and returns related memories. The backend is the SuperMemory API. Installation uses a per-user MCP URL and per-client install commands; for Windsurf the host reports that the default command errors and must be edited before it runs. The video is a short, single-project tutorial with no benchmarks, no retrieval-quality or privacy discussion, and no comparison to other memory approaches.

## Key ideas
- **Memory does not persist across AI tools, and an MCP server can serve as a single memory box shared by all of them.** — The host frames the problem as jumping between Cursor, Claude and Windsurf, each with its own context, and proposes one memory layer reachable from every client over MCP. ([0:00](https://youtu.be/mKXzPVIMFYE?t=0))
- **Memories saved from one client show up in the others.** — Two use cases are given: discussing an IDE project in Claude Desktop with the same context, and keeping context across several IDE windows. ([1:15](https://youtu.be/mKXzPVIMFYE?t=75))
- **Ask the IDE agent to write a project summary, then store it with the memory tool.** — In the demo, Cursor produces a description of the original prompt, the tools used and the MVP structure and features, and saves it. A second memory document is created this way. ([2:03](https://youtu.be/mKXzPVIMFYE?t=123))
- **A new client can resume a project by searching memory first.** — Claude Desktop searches the memory store, retrieves the project details, proposes features, and the refined feature list is saved back. Cursor then searches memory before implementing. ([3:11](https://youtu.be/mKXzPVIMFYE?t=191))
- **A project rule can replace manual saves.** — The host adds an IDE project rule telling the agent to upload any change (structural, dependency, text or tag edits) to memory, and sets the rule type to always so it applies to every chat. ([4:34](https://youtu.be/mKXzPVIMFYE?t=274))
- **The server has two tools with deliberately simple semantics.** — The add tool stores the text exactly as given. The search tool takes a keyword and returns memories related to it. The backend is the SuperMemory API, which the host says can also be used directly in one's own code. ([5:34](https://youtu.be/mKXzPVIMFYE?t=334))
- **Install with a per-user MCP URL and the client-specific command, and expect to edit the Windsurf command.** — The site gives a unique MCP URL and install commands for each client. The host reports that the default Windsurf command errors, and the fix shown is to remove an extra character from the pasted command and run it again, then accept the confirmation and refresh Windsurf. ([5:34](https://youtu.be/mKXzPVIMFYE?t=334))

## Techniques
- **Cross-client memory via a hosted MCP server** — Get your unique MCP URL from the provider's site. Copy the install command for the target client (Claude, Cursor, Windsurf or a generic MCP client), paste it into a terminal, accept the confirmation prompt, then refresh the client so the server appears. The host reports the Windsurf default command failed and had to be edited first (remove an extra character, shown as an 'I'; the exact token is not clear from the transcript). *When:* You switch between several AI clients or IDE windows and want the same project context in each.
- **Milestone summary saved to memory** — At a milestone, prompt the IDE agent to write a summary covering the original prompt, the tools and libraries used, and the structure and features built so far. Then tell it to save that text with the memory add tool. The add tool stores the text as given. *When:* After a substantial build step, so a later session can recover the project state without re-explaining it.
- **Auto-sync rule for memory updates** — In the IDE's project-specific rules, instruct the agent to upload any change to the app, including structural changes, dependency updates and text or tag edits, to memory. Set the rule type to always so it attaches to every chat. *When:* The project changes often and you do not want to re-save context by hand each time.
- **Resume by searching memory first** — In a new chat or client, ask the agent to search memory for the project by keyword before doing anything else. Then refine the plan from the retrieved memories and save the refined version back. *When:* Starting a new session on a project you worked on in another client or earlier.

## Hot takes
- The opener says the most important thing about LLMs is memory and context. This is asserted, not argued.
- The host calls the backend 'solid', 'fast, efficient and well-built' without any latency, throughput or accuracy measurement.
- The demo is one anecdote. Retrieval is described as keyword-based, but the video does not test whether search finds the right memories when there are many of them.
- No discussion of where memories are stored, who can read them, or how to delete them, though it is a hosted store of project context.
- The Windsurf install fix is given without showing the exact edit, so a viewer may not be able to reproduce it from the video alone.
- Quality is capped at 2 because the video is essentially a product walkthrough with thin technical substance, and the opener overstates the claim. It is not sponsored; the channel-membership and super-thanks plugs are channel promotion only.

## Tools mentioned
SuperMemory MCP, SuperMemory API, Cursor, Claude Desktop, Windsurf, Next.js, React

## Relevance to our work
- **agentos** (1/3): AgentOS MemoryMesh already plans cross-session tiered memory. This video shows a minimal client-facing memory surface (verbatim add plus keyword search) that is useful as a baseline, but it says nothing about retrieval quality, tiering or conflict handling. → *When designing MemoryMesh's MCP-facing API, compare it against the two-tool add/search shape and decide whether verbatim storage with keyword search is enough for the first version.*
