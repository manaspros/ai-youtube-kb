# Opus 4.6 + Agent Teams Makes Claude Code Insane

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `LZyWuPqvvjU` · [watch](https://youtu.be/LZyWuPqvvjU) · **date:** 2026-03-02 · **length:** 4:52 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Anthropic, Better Stack
- **topics:** multi-agent, coding-agents, claude-code, token-cost-efficiency · **tags:** agent-teams, subagents, tmux, experimental-flag, settings-json, token-usage, opus-4.6, team-lead, shared-task-list

> Walkthrough of Claude Code's experimental Agent Teams: independent teammates with a shared task list that can message each other, viewed in tmux or in-process. Two teammates used 29% of usage, so the presenter would restrict it.

## Summary
The Better Stack host demos Claude Code's Agent Teams feature, released under an experimental flag with official docs, after an earlier hidden version. Agent teams need Claude Code 2.1.32 or later and a settings.json entry. The demo gives the team lead a plan for a Twitter video-download web tool, and the lead creates tasks and spawns a frontend teammate and a UI-styling/design teammate in parallel. The presenter runs it once inside tmux, where each teammate gets a split pane, and once outside tmux, where a single window lets you switch between teammates. Per the docs they show, teammates get separate contexts, can message each other, and share a task list, while subagents only report summaries back to the main agent. The cost is the main caveat: two teammates took 29% of usage on Opus 4.6, roughly 13,000 tokens, so the presenter expects to reserve the feature for research or cross-checking another agent's work. The video also notes that OpenCode and other harnesses already run parallel agents.

## Key ideas
- **Agent Teams is now officially released under an experimental flag, after first appearing as a hidden feature.** — Teammates can communicate with each other and challenge or argue with each other, and the feature comes with official docs. The host calls it one of the bigger Claude Code releases because it combines the Tasks feature with parallel sub-agents. ([0:00](https://youtu.be/LZyWuPqvvjU?t=0))
- **Teams need Claude Code 2.1.32 or above plus a settings.json change.** — The video says to add one line to settings.json in the Claude config directory, but the exact key is not spelled out on screen, so check the docs before copying anything. ([0:00](https://youtu.be/LZyWuPqvvjU?t=0))
- **Run teams in tmux to get a split pane per teammate.** — Teammates appear in split panes so you can watch each one and type commands to it directly while it works. Zooming the terminal in made the panes hard to read in the demo. ([1:16](https://youtu.be/LZyWuPqvvjU?t=76))
- **Without tmux, the same team shows in one window where you switch between teammates.** — Pressing enter on a teammate opens its session, where you can see what it is doing and message it. Finished teammates shut down and the team lead takes over and writes a summary. ([2:41](https://youtu.be/LZyWuPqvvjU?t=161))
- **Teams differ from sub-agents in context and communication.** — Per the docs the presenter reads, each team member has an independent context, teammates talk to each other, and they share a task list. Sub-agents report only to the main agent, which manages everything, and they return a summary to the main context. Each team member is a separate Claude instance, so it uses far more tokens. ([2:41](https://youtu.be/LZyWuPqvvjU?t=161))
- **Cost is the main reason to hold back.** — Two teammates, excluding the main lead, used 29% of usage on Opus 4.6, about 13,000 tokens. The presenter plans to use it only for research or for having one agent check another agent's work. ([4:04](https://youtu.be/LZyWuPqvvjU?t=244))
- **Parallel agents are not new to Claude Code.** — The host notes that OpenCode and other agent harnesses already offer parallel agents, so the question is how Claude Code users adopt this version. ([4:04](https://youtu.be/LZyWuPqvvjU?t=244))

## Techniques
- **Enable agent teams** — Run Claude Code 2.1.32 or later and add the experimental-flag line to settings.json in the .claude directory. The transcript does not show the exact key, so confirm it in the official docs. *When:* Before trying agent teams. Only do this when you want to pay the higher token cost.
- **Give the team lead a plan and let it spawn teammates** — Use a prompt like: read the plan, create tasks, then spawn teammates (one frontend, one UI styling/design). The lead creates tasks and starts teammates in parallel. *When:* For a multi-part feature where separate roles (frontend, design) can work at the same time on a plan file.
- **Watch teammates in tmux** — Start Claude Code inside tmux (or iTerm2 split panes) so each teammate gets its own pane. You can type commands to any teammate while it runs. *When:* When you want to watch or steer several teammates in parallel and have room for split panes.
- **Switch teammates in a single window** — Without tmux, select a teammate to open its session in the same window, see its work, and send it messages. Switch between teammates from the bar at the bottom. *When:* When tmux is not set up or the terminal is too small for split panes.
- **Inspect team state on disk** — Look in the Claude config directory's teams folder for a folder named after the project and branch. Its config.json records the team lead and the model it uses (Haiku was chosen here without being set). *When:* To check which model the lead picked and which teammates exist, or to debug a team run.
- **Reserve teams for cross-checking and research** — Use one agent to review another agent's output, or for research, rather than routine coding, given the token cost. *When:* When the extra cost of a separate Claude instance per teammate is justified by the value of an independent check.

## Numbers
- Agent Teams requires Claude Code version 2.1.32 or above. ([0:00](https://youtu.be/LZyWuPqvvjU?t=0))
- Two teammates (excluding the main lead) used 29% of usage on Opus 4.6, about 13,000 tokens. ([4:04](https://youtu.be/LZyWuPqvvjU?t=244))
- The team lead auto-selected Haiku as its model even though the presenter did not set it. ([1:16](https://youtu.be/LZyWuPqvvjU?t=76))

## Hot takes
- The presenter does not expect to use agent teams much, because the token cost is too high.
- Teams are said to be much better than sub-agents, but this is asserted in the demo and not measured.
- The feature is called the biggest Claude Code release, but the host also says parallel agents already exist in other harnesses.

## Tools mentioned
Claude Code, Claude Opus 4.6, Claude Haiku, tmux, iTerm2, OpenCode

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code CLI and runs plan, critique, and debate. Agent Teams offers a shared task list and teammate-to-teammate messaging, which could overlap that loop. → *Compare ProsHarness's plan-critique-debate loop against Agent Teams' shared task list and messaging, and measure tokens per run before adopting it.*
- **agentos** (1/3): Multi-agent cost is a data point for budget guardrails, but the video only offers one token count from one run. → *Record tokens per teammate in a multi-agent run and compare it with the 13,000-token example as a baseline for AgentOS budget tests.*
