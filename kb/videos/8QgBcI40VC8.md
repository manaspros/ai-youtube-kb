# The Best Agent IDE I've ever used (Orca)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `8QgBcI40VC8` · [watch](https://youtu.be/8QgBcI40VC8) · **date:** 2026-10-24 · **length:** 7:05 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (name not in transcript) · **orgs:** Better Stack, GitHub, Linear
- **topics:** coding-agents, multi-agent, dev-tools · **tags:** orca, git-worktree, parallel-agents, claude-code, codex, agent-orchestration, agent-ui, usage-tracking, element-annotation, mobile-monitoring, keep-awake

> Walkthrough of Orca, a free open-source desktop app that runs Claude Code, Codex and other coding CLIs side by side with per-task git worktrees, a browser with element annotation, and multi-agent orchestration.

## Summary
The host presents Orca, an open-source desktop app that wraps real terminals so Claude Code, Codex and other coding-agent CLIs run side by side with a sidebar of per-agent progress indicators. The main workflow is one git worktree per task: type a branch name, pick an agent, and Orca creates the worktree and launches the agent inside it, while deleting the task removes the worktree too. Around the terminals it adds a file viewer with markdown rendering, an embedded browser where page elements can be annotated and sent to an agent as a targeted fix, a persistent usage meter across providers, and native git views for diffs and PR creation. Orchestration is enabled by installing a set of skills, after which a single prompt can split work between Claude and Codex or run the same feature in parallel worktrees for comparison. The host says he switched from Herdr inside Ghostty because that setup under-reported progress for subagents and background bash tasks. Other features mentioned are scheduled automations, a mobile app for monitoring agents, an orca CLI, GitHub and Linear integration, and a keep-awake option. The evidence is one user's demo and opinion, with no benchmarks or cost measurements; the orchestration demo was prompted explicitly to force multi-agent behaviour.

## Key ideas
- **Orca is an open-source desktop app that runs Claude Code, Codex and other coding CLIs side by side in one window, and each tab is a plain terminal.** — The host says it is free and has over 100,000 GitHub stars. Terminal users keep their CLI workflow and get a UI layer on top, including progress indicators per agent. ([0:00](https://youtu.be/8QgBcI40VC8?t=0))
- **Each task gets its own git worktree, created and launched from the app.** — Clicking plus, typing a branch name, choosing an agent (Claude, Codex, Goose, Kimi and others are listed) and clicking create worktree makes a git worktree and starts the agent inside it. Deleting the task in Orca also deletes the worktree in git. ([1:07](https://youtu.be/8QgBcI40VC8?t=67))
- **A built-in browser lets the user click page elements and send the exact element, with the instruction, to an agent as a fix request.** — The demo changes a page title by annotating the element and asking for the change. The agent receives the element target and works on it automatically. The host calls this the coolest part of the app. ([2:03](https://youtu.be/8QgBcI40VC8?t=123))
- **Orchestration works through installed skills. A single prompt can split work across providers or run the same feature in parallel for comparison.** — After installing a set of orchestration skills in settings, a prompt to redesign a dashboard using a named skill and both Claude and Codex launched two extra tabs, one per provider. The host also describes splitting backend and frontend work between agents, or having both work the same feature in separate worktrees and comparing results. ([3:21](https://youtu.be/8QgBcI40VC8?t=201))
- **The host switched from Herdr inside Ghostty because that setup under-reported background progress.** — His complaint was that Herdr marked an agent as finished while subagents or background bash tasks were still running. He says Orca tracks this better and keeps the terminal feel without the full UI being inside the terminal. ([4:35](https://youtu.be/8QgBcI40VC8?t=275))
- **A persistent usage meter shows weekly usage across providers, and a mobile app monitors all agents in one place.** — The footer shows usage for Claude, Codex and Cursor; in the demo Claude was at 1% of its weekly limit and Codex and Cursor at 0%. The mobile app shows agents from any provider in one place, where the host previously needed both the Claude and ChatGPT mobile apps. ([2:03](https://youtu.be/8QgBcI40VC8?t=123))
- **Native git and automation features cover diffs, PRs, scheduled runs and keeping the machine awake.** — Changes and diffs can be annotated and sent back to agents. PRs are created and pushed to the linked GitHub repo. Scheduled tasks such as weekly runs are supported. An option keeps the computer awake all the time or only while an agent is working, replacing caffeinate in a terminal. ([3:21](https://youtu.be/8QgBcI40VC8?t=201))

## Techniques
- **Worktree-per-task agent launch** — In Orca, click plus, enter a branch name such as feature-redesign, pick an agent, and click create worktree. The agent starts inside that worktree. Open more agents in the same worktree with cmd+D. Delete the task to remove the worktree from git as well. *When:* Running several agents on parallel features or on the same feature with different models, without branch collisions or manual worktree setup.
- **Element-annotated fix requests from an embedded browser** — Open the dev server (the demo used localhost:5173) in an Orca browser tab, use the annotate icon to select a page element, write the change request, and send it to a chosen agent. The agent receives the exact element target with the instruction. *When:* Making small UI copy or layout fixes on a running local app without describing the DOM target in the prompt.
- **Forced multi-provider split for comparison** — After installing the orchestration skills from Orca settings, give one prompt that names a skill and asks for both Claude and Codex. Orca starts a tab per provider. Compare outputs at the end, or ask for a backend/frontend split across providers. *When:* Getting a second opinion on a design or implementation from two models, or dividing a feature by strength.
- **Run the orca CLI from the terminal** — The host mentions the orca command for driving the app from a terminal. No flags or subcommands are shown in the video. *When:* Scripting Orca from shell alongside the GUI.

## Numbers
- Orca has over 100,000 stars on GitHub. ([0:08](https://youtu.be/8QgBcI40VC8?t=8))
- Usage shown in the demo: Claude at 1% of weekly usage, Codex and Cursor at 0%. ([2:03](https://youtu.be/8QgBcI40VC8?t=123))
- Video length is 7:05. ([0:00](https://youtu.be/8QgBcI40VC8?t=0))

## Hot takes
- Calls Orca 'the best tool for running agents I have ever used' and 'the biggest improvement I've ever seen', based on one user's daily use. No measurements or comparisons are given.
- The orchestration demo was prompted to force multi-provider behaviour; the host says so himself. Automatic task splitting is claimed but not shown in an unprompted run.
- The Herdr comparison rests on one anecdote about background progress tracking, not a test.
- No sponsorship is stated. Substance is a feature tour with real UI detail, so quality stays at the practitioner level rather than the sales-pitch level.

## Tools mentioned
Orca, Claude Code, Codex, Goose, Kimi (transcript says 'kimmy'), Cursor, Herdr (transcript says 'Herder'), Ghostty (transcript says 'Ghosty'), GitHub, Linear, caffeinate, Apple Design skill (named in demo, source not stated)

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI with checkpoints, loops, schedules and phone-driven approvals. Orca has overlapping pieces: scheduled automations, mobile monitoring across providers, and per-task worktrees. Its subagent and background-bash progress tracking is the gap the host calls out. → *Look at how Orca surfaces subagent and background-bash progress in its sidebar, and check whether ProsHarness's checkpoint/resume view reports the same running tasks correctly.*
