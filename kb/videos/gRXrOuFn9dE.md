# 3 Things Before You FINALLY Switch to Codex CLI

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `gRXrOuFn9dE` · [watch](https://youtu.be/gRXrOuFn9dE) · **date:** 2025-11-02 · **length:** 10:34 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS host (name not stated in transcript) · **orgs:** OpenAI, Anthropic, Make.com, Cursor, Kenney
- **topics:** coding-agents, context-engineering, multi-agent · **tags:** codex-cli, claude-code, bmad-method, sub-agents, mcp, agents-md, phaser-3, angry-birds-test, ui-clients, one-shot-prompting, context-window, openai-codex-ide-extension

> Hands-on comparison of Codex CLI against Claude Code: a single-prompt game test, the GUI options for each, an MCP workaround for missing sub-agents, and the BMAD planning method for multi-step builds. Sponsored intro; thin evidence.

## Summary
The host argues that Codex CLI's main advantage over Claude Code is its 272k-token context window, while switching means giving up Claude-only features such as sub-agents. He runs one comparison, a single-prompt Angry Birds clone built with Phaser 3 and Kenney assets, and reports that both tools failed to produce a fully working game, with Codex's result judged better. He then reviews the UI options: third-party GUIs for Claude Code (Opcode, Conductor) and for Codex (OpenAgents, Codexia, where Codexia failed to install on macOS), and he prefers the official Codex IDE extension. To replace Claude Code's sub-agents he presents CodexSubagents, an open-source MCP server that spawns a fresh Codex instance per delegated task with that agent's context injected through agents.md, and notes the repo is low-activity and needed manual fixes. He closes by recommending the BMAD method, which plans first, breaks work into tested per-task files, and installs role agents such as an SM (Scrum Master) agent, as the fix for one-shot prompting. The first 74 seconds are a sponsor segment and the claims are mostly single-run anecdotes.

## Key ideas
- **Codex CLI's main draw over Claude Code is its 272k-token context window, but switching means losing Claude-only features such as sub-agents.** — The host frames the Claude-vs-Codex debate (including online claims of Claude performance loss, which he reports but does not verify) as a context-window trade-off. ([0:00](https://youtu.be/gRXrOuFn9dE?t=0))
- **Same single prompt (Angry Birds clone in Phaser 3 with Kenney assets) produced no fully working game from either tool.** — Claude Code output got stuck on play and ignored the assets; Codex (GPT-5 Codex High) produced something playable-looking but still incomplete. Judged better by the host, but this is one run per tool. ([2:24](https://youtu.be/gRXrOuFn9dE?t=144))
- **Host credits the larger context window for Codex's better result, but follow-up fix prompts became too complicated for the model.** — Conclusion: one-shotting is not possible for this kind of task; a context-engineering workflow is needed. ([2:24](https://youtu.be/gRXrOuFn9dE?t=144))
- **Third-party GUIs exist for both tools because of terminal friction for Cursor users.** — Claude Code: Opcode (formerly Claudia) and Conductor (orchestrates agents and monitors git worktrees). Codex: OpenAgents (minimal desktop GUI) and Codexia (many features, MCP and agent modes, but the macOS build was corrupted for the host). ([3:42](https://youtu.be/gRXrOuFn9dE?t=222))
- **Host's pick for a Codex UI is the official IDE extension.** — Mode and model selection, cloud environments for background agents, MCP config editable inside the editor, image paste with previews. He says Claude Code has no comparable UI. ([5:10](https://youtu.be/gRXrOuFn9dE?t=310))
- **Codex has no sub-agents, so an open-source MCP server (CodexSubagents) emulates them.** — Each delegated task runs in a new Codex instance with its own context, which is injected from agents.md. The main agent is told to route work rather than do it. ([5:10](https://youtu.be/gRXrOuFn9dE?t=310))
- **The sub-agent workaround is fragile: low star count, inactive author, manual fixes needed.** — The host suggests forking the repo and experimenting, and offers a follow-up video only if there is interest. ([6:26](https://youtu.be/gRXrOuFn9dE?t=386))
- **One-shot prompting breaks down for multi-feature software; pre-planned, chunked, tested tasks are the fix (BMAD method).** — Each task file carries what to build and where to build it, so the agent does not need to rediscover context. The host claims this removes hallucinations, which he does not demonstrate. ([7:51](https://youtu.be/gRXrOuFn9dE?t=471))
- **BMAD installs role-based agents; Codex needs them wired in by hand because it lacks slash commands.** — The SM (Scrum Master) agent takes the BRD and architecture document, creates tasks, and checks progress. The installer includes a Phaser 3 dev pack. Command syntax for the installer is not shown on screen in the transcript. ([9:08](https://youtu.be/gRXrOuFn9dE?t=548))

## Techniques
- **Sub-agent delegation through an MCP server** — An MCP server exposes a list-agents call (for confirmation) and a delegate tool. delegate picks an agent by its description, starts a new Codex instance, injects that agent's context from agents.md, and returns the result to the main agent. The main agent's agents.md tells it to route tasks and not do the work itself. *When:* You want Claude Code-style sub-agents with isolated context inside Codex CLI and cannot wait for native support.
- **Fork and patch an unmaintained community tool** — Fork the repo, connect the fork to Claude Code, and experiment; expect to fix issues by hand. *When:* A useful open-source tool is inactive or buggy and you want to adapt it instead of waiting.
- **BMAD-style plan-then-build workflow** — Write a BRD and an architecture document first. Break the work into tasks, each stating what to implement and where, with testing. Implement the tasks one at a time, testing each before moving on. Use the SM agent to generate and track the tasks. *When:* Building a multi-feature app where one-shot prompts drift or fail. The host ties it to games built with Phaser 3.
- **Manual agent wiring for Codex** — Install BMAD core, then add its agent definitions to Codex by hand, since Codex has no slash commands for invoking them. *When:* You want BMAD's role agents in Codex. Claude Code users can invoke the same agents through slash commands instead.
- **Edit MCP config from inside the Codex IDE extension** — Open the MCP config file from the extension UI and edit it there, without using the terminal. *When:* Setting up MCP servers for Codex without a terminal session.

## Numbers
- Codex context window of 272k tokens, presented as the main advantage over Claude Code. ([0:00](https://youtu.be/gRXrOuFn9dE?t=0))
- Cost of a second $200 agent subscription, cited as the reason not to just buy another tool to test. ([0:00](https://youtu.be/gRXrOuFn9dE?t=0))
- Sponsor claim: over 2,500 pre-built apps for Make.com automations. ([0:00](https://youtu.be/gRXrOuFn9dE?t=0))
- Single-run test: one prompt per tool, model GPT-5 Codex High, neither produced a fully working game. ([2:24](https://youtu.be/gRXrOuFn9dE?t=144))
- Codexia's latest release was about 18 hours old when recorded, and its macOS build was corrupted. ([3:42](https://youtu.be/gRXrOuFn9dE?t=222))

## Hot takes
- The first 74 seconds are a sponsor read for Make.com, so the intro is not technical content.
- The Codex-vs-Claude verdict rests on one unrepeated prompt test (Angry Birds clone) and is attributed mainly to the context window, with no controlled comparison.
- Claims that BMAD 'completely eliminates hallucinations' are asserted, not demonstrated.
- The host calls the Codex IDE extension the best UI and says Claude Code's UI is not good; this is opinion, not measured.
- The host repeats online claims that Claude Code had degraded performance and that Anthropic admitted it, without evidence in the video.
- Tool status (Codexia's install, Codex's lack of sub-agents, the 272k window) is dated to late 2025 and will likely have changed.

## Tools mentioned
Codex CLI (OpenAI), Codex IDE extension, GPT-5 Codex High (model used in the test), Claude Code, Phaser 3 (game engine), Kenney assets (spoken as Kenny), Three.js (spoken as 3.js), React, Next.js, shadcn/ui, Opcode (formerly Claudia), Conductor, OpenAgents (desktop GUI for Codex), Codexia, CodexSubagents MCP server, agents.md, BMAD method / BMAD core / Phaser 3 dev pack, Make.com (sponsor), Cursor, VS Code

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code with plan, critique and checkpointed runs. BMAD's per-task spec files (what, where, how, plus tests) map directly onto checkpointed, one-task-at-a-time runs. → *Trial a BMAD-style task-file format (per-task what/where/how and a test step) as the plan artifact that ProsHarness checkpoints and resumes, and compare it with the current plan format.*
- **agentos** (1/3): Sub-agent delegation via a fresh-context instance per task is a multi-agent pattern related to AgentOS routing, but this is a single anecdote about a Codex workaround. → *Skim the CodexSubagents delegate/agents.md design to compare its isolated-context-per-agent approach with AgentOS multi-agent routing; no change needed unless AgentOS lacks per-agent context isolation.*
- **general** (1/3): Context engineering through pre-planned, chunked, tested tasks ties to the recurring interest in context engineering and subagents. → *Read the BMAD method docs for its task-file template and SM-agent workflow as a reference for context-engineering practice.*
