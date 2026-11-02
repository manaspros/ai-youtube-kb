# Claude code vs Codex vs Cursor: Who gets the cake?

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `_Xbe7MQ2NxI` · [watch](https://youtu.be/_Xbe7MQ2NxI) · **date:** 2025-11-02 · **length:** 9:35 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, Google, OpenAI, Qwen, Cursor, GitHub, Slack, ScaleKit, Auth0
- **topics:** claude-code, coding-agents, mcp-and-tools, agent-architecture · **tags:** headless-mode, bash-tool, github-actions, agent-sdk, mcp-server, cli-agents, pricing

> Argues Claude Code and other AI CLIs are "portable agent engines": terminal agents can call each other via bash, run headless (-p), deploy to GitHub Actions and act as MCP servers. Opinion-heavy, with a sponsor segment.

## Summary
The host argues that AI labs are shipping CLI coding agents (Claude Code, Gemini CLI, Codex CLI, Qwen Code, Cursor CLI) because a terminal agent is a portable engine that can run anywhere a shell exists. He shows Claude Code invoking the Codex CLI headlessly through its bash tool to do research, which he calls "bash agents," and points to gitingest as an example of a CLI tool an agent can drive. He then covers deployment: running Claude Code on a schedule from a GitHub Actions workflow (his AI-model monitor that summarizes sites and posts to Slack), the Claude Code GitHub app for PR review, and the Agent SDK (renamed from the Claude Code SDK) for building custom agents. He notes headless (-p) mode for scripts and CI, mixing local and remote MCP servers, and someone wrapping Claude Code as an MCP server. The closing section is opinion: Claude Code is his preferred agent, models inside it are inconsistent, and pricing differs (Gemini and Qwen Code have free tiers; Claude Code and Codex draw on the $20 or $200 plan). No benchmarks or measured data are given.

## Key ideas
- **Coding CLIs are being shipped as portable agent engines, not just terminal toys.** — The host says labs release CLIs because a terminal agent (model plus tools) can be installed once, called from any folder, and deployed to any Linux server that is reachable over a shell. ([1:09](https://youtu.be/_Xbe7MQ2NxI?t=69))
- **The bash tool lets one agent call another agent's CLI.** — Claude Code runs the Codex CLI in headless mode from its bash tool to research Gemini CLI usage limits, so a whole agent becomes a callable command for another agent. ([2:12](https://youtu.be/_Xbe7MQ2NxI?t=132))
- **Any CLI tool becomes an agent capability through bash ('bash agents').** — He argues that once an agent has unrestricted bash, it can use any installed CLI. His example is gitingest, which converts a GitHub repo into LLM-readable text, and he says he used it in a workflow to extract parts of large repos. ([3:40](https://youtu.be/_Xbe7MQ2NxI?t=220))
- **A scheduled GitHub Actions workflow is his deployment target for a recurring agent.** — He modifies a workflow so Claude Code runs at set times. His monitor agent searches sites for new AI releases, summarizes them, and sends a reminder to Slack. The Claude Code GitHub app covers PR review on existing code. ([4:57](https://youtu.be/_Xbe7MQ2NxI?t=297))
- **The Agent SDK is the prebuilt Claude Code engine exposed for custom agents.** — The Agent SDK, previously the Claude Code SDK, is described as a prebuilt version of Claude Code for building custom agents. Anthropic also embeds the same core engine in Claude Code for Chrome, with Chrome-specific tools added. ([6:25](https://youtu.be/_Xbe7MQ2NxI?t=385))
- **Headless (-p) mode and MCP are the main integration points for scripts and CI.** — Headless mode processes one request and exits, so it can run in loops or CI jobs and be given role-specific prompts (e.g. checking different parts of the code). Local MCP servers are commands run in the terminal, remote ones run elsewhere, and Claude Code itself can be wrapped as an MCP server. ([7:27](https://youtu.be/_Xbe7MQ2NxI?t=447))
- **Opinion on the field: Claude Code is best overall, but its model output is inconsistent, and only some tools offer free tiers.** — He says no other agent comes close on features but the underlying model varies in quality. Claude offers no free credits, Gemini CLI and Qwen Code have free limits, and Claude Code and Codex share usage with the $20 or $200 subscription. He calls Codex's agent far less capable and Cursor's CLI less featureful. ([8:53](https://youtu.be/_Xbe7MQ2NxI?t=533))

## Techniques
- **Headless single-shot invocation** — Run the CLI with one prompt in non-interactive mode (Claude Code: claude -p "..."; the captions render the flag as 'PFLAG'). It processes the request, prints output, and exits. Loop over tasks in a script, or call it from CI. *When:* Batch LLM tasks, scripted pipelines, CI checks, or when another agent needs one answer from a CLI agent.
- **Cross-agent delegation through bash** — Let the orchestrating agent shell out to another agent's headless CLI (his example: codex run from Claude Code via bash to research a question) and read its stdout. *When:* Using a second vendor's agent for research or a second opinion without a custom integration.
- **Scheduled agent via GitHub Actions** — Edit a GitHub workflow with a cron-style schedule so it runs Claude Code headlessly. The agent uses its tools (for example web search) to produce a summary and then posts it, for example to Slack. *When:* Recurring monitoring or digest jobs that need no server of your own.
- **Claude Code GitHub app for PR review** — Install the Claude Code GitHub app on the repo so Claude can review pull requests and help with existing code. The video does not show setup steps. *When:* Adding an AI reviewer to pull requests on GitHub.
- **Mixed local and remote MCP servers** — Register local MCP servers as commands run in the terminal and remote MCP servers as endpoints running on external machines in the same client config. He also mentions wrapping Claude Code itself as an MCP server to expose it as a tool. *When:* Giving an agent both local tools and hosted tools, or exposing a specialized agent to other clients.

## Numbers
- Claude Code and Codex usage is shared with the $20 plan, or with the $200 plan if you have it. ([8:53](https://youtu.be/_Xbe7MQ2NxI?t=533))
- Claude offers no free credits. Gemini CLI and Qwen Code each have a free usage limit. ([8:53](https://youtu.be/_Xbe7MQ2NxI?t=533))
- Claude Code's early adoption is attributed to being cheap and offering large limits. No measured figures are given. ([0:00](https://youtu.be/_Xbe7MQ2NxI?t=0))

## Hot takes
- Claude Code is the best agent right now and no other agent comes close because of its feature set (his opinion, not measured).
- The models inside Claude Code are inconsistent: sometimes very good, sometimes very bad.
- Codex models are good, but the Codex agent is far less functional than Claude Code.
- Any CLI can become an agent capability once an agent has bash access ('bash agents').
- Sponsored segment (ScaleKit, roughly 3:40 to 4:57) caps quality at 2 per rubric. Substance is mostly conceptual with few reproducible steps; the video has no benchmarks.

## Tools mentioned
Claude Code, Claude Code GitHub app, Claude Code for Chrome, Claude for Excel, Agent SDK (formerly Claude Code SDK), Codex CLI, Gemini CLI, Qwen Code (transcript: QuenCode), Cursor CLI, gitingest, GitHub Actions, Slack, MCP, ScaleKit (sponsor), Auth0

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI, and this video covers its headless -p mode, scheduled runs in GitHub Actions and MCP wiring. These are the same primitives ProsHarness's loops and schedules depend on. → *Check that ProsHarness invokes Claude Code in headless mode for each scheduled loop and records the exit state per run, so resume can rely on it.*
- **agentos** (1/3): Headless CLI agents and MCP exposure are a deployment pattern for AgentOS, but the video does not discuss the proxy, budgets, or storage layers. → *Skim the Agent SDK docs for how it runs a Claude Code-equivalent loop programmatically, and compare with AgentOS's own agent-run interface.*
