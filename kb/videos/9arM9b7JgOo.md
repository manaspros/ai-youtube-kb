# Develop at Idea Velocity - Jeffrey Lee-Chan, Snapchat

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `9arM9b7JgOo` · [watch](https://youtu.be/9arM9b7JgOo) · **date:** 2026-07-18 · **length:** 15:28 · **format:** workshop · **quality:** 2/5 · **depth:** intro
- **speakers:** Jeffrey Lee-Chan, Austin (CMUX co-creator, first name only) · **orgs:** Snapchat, CMUX
- **topics:** coding-agents, multi-agent, context-engineering · **tags:** OpenClaw, manager-worker, git-worktrees, parallel-agents, CMUX, Claude Code, staging-environment, browser-tests, token-budget, model-switching, workshop

> Snapchat engineer Jeffrey Lee-Chan demos his personal coding-agent workflow built on OpenClaw: a manager agent with memory delegates work to parallel worktree workers, and separating the manager's context from the workers' reduces overclaiming.

## Summary
Jeffrey Lee-Chan of Snapchat walks through how he runs parallel coding agents for development, with OpenClaw as a persistent manager and Claude Code workers in git worktrees, viewed through CMUX terminals. He argues that a manager agent whose context holds specs, goals and history rather than code gives more honest status than working directly with a coding model, which he says tends to call its own work great. He describes layered verification: non-visual tests first, browser and visual checks last, and says agents now handle browser tests that failed a year earlier. He also describes a local-dev, staging, then production flow, noting that a staging instance raises token usage but may add reliability. Model choice is cost-driven: he orchestrates with Codex 5.3, finds GPT-5.4 uses more tokens, and switches to a cheaper model when budget runs low. The transcript is anecdotal and workshop-style, and it stops at about 15:08 of a 15:28 video, so the Q&A portion is missing.

## Key ideas
- **A persistent manager agent with memory lets brief instructions work most of the time.** — Because OpenClaw keeps context and memory across sessions, a short message like 'fix the skeptic agent' is usually enough. He estimates that when everything works, a brief description is enough about 70% of the time. Debugging is still needed sometimes, for example a timeout that needs a longer limit. ([0:00](https://youtu.be/9arM9b7JgOo?t=0))
- **Control of agents runs on a spectrum from loose to tight, with a manager layer over the workers.** — He gives the agent broad access on purpose. OpenClaw's orchestrator manages worker agents, and CMUX terminals give him direct control when he wants it. Each worker runs Claude Code, which can spawn its own subagents. He says the Claude Code layer is the part of the stack he changes most often. ([3:51](https://youtu.be/9arM9b7JgOo?t=231))
- **Keep the orchestrator's context about the spec, not the code.** — His stated reason for using OpenClaw instead of plain Claude Code is specialization. Claude Code loads CLAUDE.md files, skills and MCP definitions at startup, which he estimates can take about 25% of context before any task starts. The orchestrator context stays on goals, history and Slack messages, and it builds the spec from them. ([5:21](https://youtu.be/9arM9b7JgOo?t=321))
- **Verify in layers and push the human-only checks to the end.** — He suggests starting with non-visual checks, then CSS or JS tests, and leaving visual and browser checks for last. He asks which problems really need a human. He says agent reliability on browser tests improves each quarter and that agents now handle popups and login flows that they failed on months earlier. ([6:25](https://youtu.be/9arM9b7JgOo?t=385))
- **A manager whose context is separate from the workers' context reduces self-bias and overclaiming.** — He says that when he codes directly with a model it tends to call the work great. A manager reviewing a worker's PR caught that another PR superseded it and suggested closing it. He thinks the manager's different context is what produces this more critical review. ([9:36](https://youtu.be/9arM9b7JgOo?t=576))
- **Notifications and vertical tabs let one person supervise many parallel agents.** — He uses CMUX's vertical tab layout and completion notifications so he can work as a manager instead of a coder. He says his efficiency rose a lot after switching to this setup. He also says he only needs to look when a notification arrives. ([9:36](https://youtu.be/9arM9b7JgOo?t=576))
- **Use a staging instance for integration tests before production, and be clear about what 'sandbox' means.** — He separates two meanings of sandbox: Docker or an isolated environment, and his own staging OpenClaw instance. Flow: develop locally, run integration tests on staging, then merge and deploy to production. He says this raises token usage, but he expects better reliability in return. He is still debugging the setup. ([14:07](https://youtu.be/9arM9b7JgOo?t=847))

## Techniques
- **Manager and worker split with a separate-context reviewer** — A manager agent holds the spec, goals and task history but not the implementation files. It hands tasks to worker agents, each running in its own git worktree, and reviews their status reports. Workers finish and send notifications, and the manager decides whether to merge, close or supersede each PR. *When:* Use when several tasks run in parallel and you want honest status and less self-bias than a worker reporting on its own output.
- **Layered verification with humans last** — Run non-visual tests first (unit, then CSS or JS checks). Reserve browser and visual checks for last. Re-check each quarter which steps still need a person, since agents keep improving at browser tests. *When:* Use when deciding how much of the test suite can be handed to an agent, especially for UI work.
- **Context budgeting for the orchestrator** — Keep the orchestrator's context free of what the task does not need. Put implementation rules, skills and MCP definitions in the worker's context instead, so the manager stays focused on goals and history. *When:* Use when the default startup context (CLAUDE.md, skills, MCP) takes a large share of the window before any work begins.
- **Local, staging, then production flow for agent changes** — Develop locally. Run integration tests against a separate staging instance of the agent system. Merge and deploy to production only after staging passes. *When:* Use when agent changes need a reliability check before they reach a production agent. Expect higher token usage.
- **Cost-tiered model switching** — Use a strong orchestrator model for most work. Switch to a cheaper model when the budget runs low, accepting lower quality for routine tasks. *When:* Use when token spend is the main constraint and some tasks can tolerate a weaker model.

## Numbers
- A brief task description works about 70% of the time when everything is working (speaker's estimate; the wording is somewhat unclear). ([0:00](https://youtu.be/9arM9b7JgOo?t=0))
- Claude Code's startup context (CLAUDE.md, skills, MCP) may take about 25% of context before a task begins (speaker's estimate). ([5:21](https://youtu.be/9arM9b7JgOo?t=321))
- Speaker's recommended test order: non-visual tests first, visual or browser tests last. He says agents' browser-test reliability improves every quarter or month. ([6:25](https://youtu.be/9arM9b7JgOo?t=385))
- Running the same work on both a staging and a production instance could double token use. He says a staging-then-production flow raises usage but does not double it. ([14:07](https://youtu.be/9arM9b7JgOo?t=847))

## Hot takes
- An agent could replace the speaker in his current role.
- A manager agent with separate context gives more honest review than a coding model reviewing its own work.
- Browser and visual tests are becoming routine for agents, so the human-only share of testing keeps shrinking.

## Tools mentioned
OpenClaw, CMUX, Claude Code, Claude Code Teams, Codex 5.3, GPT-5.4, MiniMax, git worktrees, Docker

## Relevance to our work
- **prosharness** (2/3): The manager and worker split with a separate-context reviewer maps onto the plan, critique and debate loop. The speaker's point that a fresh-context reviewer catches overclaiming and superseded work applies directly to the critique step. → *Add a critique step that runs in a fresh session and sees only the worker's spec and summary, not its diff or transcript. Compare its verdicts on superseded or overclaimed work against the current critique step, using a few finished runs.*
