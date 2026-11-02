# Get Out of the Model's Way — Kevin Hou, Google Antigravity

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `buHC7bQE1X4` · [watch](https://youtu.be/buHC7bQE1X4) · **date:** 2026-10-04 · **length:** 19:01 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Kevin Hou · **orgs:** Google, Google DeepMind, Google Antigravity
- **topics:** multi-agent, coding-agents, product-ux, agent-architecture · **tags:** antigravity, subagents, agent-teams, generative-ui, sidecars, scheduled-tasks, eval-analysis, skills, gemini-3.5-flash, scaling-with-intelligence

> Google's Antigravity lead on building agent products that get out of the model's way: subagent teams, sidecar triggers and generative UI, with cost and token stats from a kernel-building run.

## Summary
Kevin Hou, who leads part of the engineering team on Google's Antigravity agentic coding product, argues that a product should scale with model intelligence and expose the frontier of the model it serves. He traces the field's shifts: 2022 deterministic autocomplete, 2024 agents with MCP and permission systems, and 2025 agent managers with skills, hooks and artifacts. He recounts backlash moments, such as users objecting when chat was removed, and says agent-first UX won out. Antigravity split its IDE from its agent manager into two apps, which he compares to a debugger sitting beside an IDE. The 2026 primitives he names are dynamic subagents, sidecars and generative UI, with agent teams in public preview behind a /teamwork command. He backs the claims with a kernel-building run (93 subagents, 12 hours, under $1,000) and an internal eval-analysis workflow that was about 90% automated. The talk is a vendor talk, so the stats are the speaker's own and unverified.

## Key ideas
- **Build the product so it scales with the model: the frontier of whatever model you serve should show up in the user's product experience.** — The speaker frames the goal as letting the model cook by removing fixed UI and heavy scaffolding. He says primitives should be re-checked against each new model release. ([0:08](https://youtu.be/buHC7bQE1X4?t=8))
- **The product primitives have shifted with each era of models: deterministic 2022 tools, 2024 agents with MCP and permissions, 2025 agent managers with skills and hooks.** — Early tools relied on embeddings, rules files and AST parsing because the models could not handle more. Later primitives followed model capability. ([3:05](https://youtu.be/buHC7bQE1X4?t=185))
- **Users push back on removing familiar UI, but agent-first UX won out once models got better at multi-step work.** — He cites the backlash to removing chat and the early fear of giving an agent a terminal. Permission systems let users ship faster and more safely as models made better run decisions. ([4:05](https://youtu.be/buHC7bQE1X4?t=245))
- **Split the agent manager from the IDE so orchestration becomes its own surface; the IDE becomes a deeper-layer tool.** — He compares the IDE to the agent manager the way a debugger relates to the IDE: you do not always need it, but it helps when you go one layer down. ([5:33](https://youtu.be/buHC7bQE1X4?t=333))
- **Agent teams: a lead agent spawns dynamically generated subagents, each with its own role and possibly a different model, and asks the user clarifying questions until the task is clear.** — Subagents run in parallel, can work in sandboxes or remote execution, and are configured and prompted on the fly by the lead. Public preview is triggered by /teamwork. ([8:05](https://youtu.be/buHC7bQE1X4?t=485))
- **Scale test: a kernel-building run with dozens of subagents and a fixed budget, reported as evidence for the teams approach.** — The speaker reports a kernel built from scratch that played Doom, with 93 subagents over 12 hours, about 15,000 requests, about 2 billion tokens and under $1,000. Photo editor and messaging app builds used hundreds of subagents each, taking about half a day. ([9:32](https://youtu.be/buHC7bQE1X4?t=572))
- **Automate internal eval analysis by fanning out one subagent per hypothesis about why two rollout sets differ, then consolidating into one report.** — A research specialist proposed 100 hypotheses about the control-versus-experiment delta, drilled into each in parallel, and returned a report with an interactive UI. The speaker says about 90% of the manual notebook workflow was automated with natural-language requests and a skills file. ([12:19](https://youtu.be/buHC7bQE1X4?t=739))
- **Sidecars: a generic long-lived plug-in process that listens to the outside world and lets the agent set its own triggers (webhooks, SMS, cron, GitHub PRs).** — Scheduled tasks in Antigravity already come from this sidecar concept. The speaker says the spec will be released later this summer so others can build on it. ([15:14](https://youtu.be/buHC7bQE1X4?t=914))
- **Generative UI replaces fixed templates and HTML files: the model renders interactive views (Kanban, timelines, charts, tables) inline in the conversation on demand.** — He argues human-written specialized UIs are becoming less needed. He says Gemini 3.5 Flash runs at about 900 tokens per second, which makes on-the-fly UI practical. ([15:14](https://youtu.be/buHC7bQE1X4?t=914))

## Techniques
- **Dynamic subagent teams under a lead agent** — A lead agent decomposes the task, then creates each subagent with its own role, prompt and context. Subagents can use different models, run in parallel, and run in sandboxes or remote environments. The lead can ask the user clarifying questions first. *When:* Large tasks that split into independent specialized pieces, such as frontend, backend, infra and QA work, or many small parallel investigations.
- **One subagent per hypothesis fan-out for eval deltas** — Generate many candidate explanations for a metric difference, spawn one subagent per hypothesis to investigate in parallel, then merge the findings into a single report. *When:* Comparing control and experiment eval runs where the cause of the difference is unknown.
- **Skills file plus natural language for internal workflow automation** — Load a skills file that encodes the codebase and tools, then ask for the workflow in plain language instead of hand-writing pipelines, async pools and judges. *When:* Recurring analysis work that used to live in notebooks.
- **Sidecar trigger process** — Run a long-lived plug-in process that listens for external events (webhooks, messages, cron, PR events) and lets the agent register its own triggers. Time-based schedules are one case of this. *When:* Agents that must react to outside events or run on schedules without a user prompting them.
- **Generative UI in the conversation instead of fixed screens** — Let the model generate the view it needs (a Kanban board, timeline, chart, or filterable table) inline, rather than shipping a fixed template or HTML file. *When:* Status checks and analysis results that users want to filter, slice or inspect beyond plain markdown.
- **Separate the orchestration surface from the editor** — Ship the agent manager as a standalone app and keep the IDE as an optional deeper layer for code-level work. *When:* Products where users manage many agents at once and only sometimes need to open code.
- **Primitive audit against the next model** — List the primitives in your product (permissions, tools, UI, triggers) and ask how each one should change as the model gets smarter, faster and cheaper. *When:* Planning a product roadmap around new model releases.

## Numbers
- Kernel-building run (played Doom): 93 subagents over 12 hours, about 15,000 requests, about 2 billion tokens, under $1,000 (speaker's figures). ([9:32](https://youtu.be/buHC7bQE1X4?t=572))
- Photo editor and messaging app builds each used hundreds of subagents and took about half a day. ([9:32](https://youtu.be/buHC7bQE1X4?t=572))
- Side-by-side eval analysis: about 90% of the workflow automated; a research specialist proposed 100 hypotheses, one subagent each. ([12:19](https://youtu.be/buHC7bQE1X4?t=739))
- Gemini 3.5 Flash in Antigravity runs at almost 900 tokens per second, which the speaker says is about 10x faster than many other frontier model experiences. ([15:14](https://youtu.be/buHC7bQE1X4?t=914))
- Antigravity launched November 2025; Antigravity 2.0 launched at Google I/O (about a month before the talk). ([0:08](https://youtu.be/buHC7bQE1X4?t=8))

## Hot takes
- Human-written specialized UIs are dying; generated UI should replace templates and HTML files.
- The removal of chat in favor of agent-only UX was painful at the time, but agent-first became the right paradigm.
- The IDE is to the agent manager what the debugger is to the IDE: useful, but not always needed.
- Agent orchestration (teams, swarms, software factories) is the future and the company is betting on it.

## Tools mentioned
Google Antigravity, Antigravity CLI, Antigravity 2.0 agent manager, Gemini 3.5 Flash, MCP, Cloud sandboxes and remote execution (unnamed), Windsurf (reference only)

## Relevance to our work
- **prosharness** (2/3): ProsHarness has loops and schedules. The sidecar model (long-lived listener that lets the agent register triggers such as cron and webhooks) and per-subagent model selection both map onto that design. → *Read the Antigravity sidecar spec when it ships this summer and compare it with the ProsHarness loop/schedule design, looking at whether triggers should be registered by the agent itself.*
- **agentos** (1/3): Eval-analysis fan-out (one subagent per hypothesis, merged report) is a concrete pattern for triaging RAGAS or eval deltas, but the talk gives no implementation detail. → *Prototype a one-subagent-per-hypothesis triage for AgentOS eval regressions, reading the delta and fanning out, and see if it finds causes faster than manual review.*
