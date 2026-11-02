# Cursor AI Just Got a Massive Upgrade Over Claude Code

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `WKy71aZHx20` · [watch](https://youtu.be/WKy71aZHx20) · **date:** 2025-11-02 · **length:** 12:21 · **format:** review · **quality:** 2/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Cursor, Anthropic, ScaleKit, Warp
- **topics:** coding-agents, claude-code, token-cost-efficiency · **tags:** cursor, claude-code, plan-mode, slash-commands, hooks, git-worktrees, browser-automation, playwright, mcp, background-agents, usage-limits, pricing, auto-mode

> A solo creator's hands-on comparison of Cursor's new agent features (plan mode, hooks, slash commands, worktrees, browser control) against Claude Code, concluding Cursor wins on usability and that subscribing to both is the best setup.

## Summary
The speaker, who had used Claude Code heavily, tried Cursor's recent releases and argues Cursor has caught up on plan mode, custom slash commands, to-do tracking, context summarization, hooks, multi-agent management and git-worktree isolation. The most distinctive feature he demos is Cursor's native browser tool, which drives a Playwright-backed browser inside the chat so the agent can click through an app, read console output, errors and network traffic, and fix bugs it finds. He also covers background agents with Linear, Slack and GitHub integrations, OS notifications, menu-bar agent monitoring, and deep links that preload a prompt into a new chat. The usability argument is the core: Cursor configures MCP servers, hooks and commands through visual UI, while Claude Code requires hand-editing files and a terminal. On pricing, he describes Cursor's usage-based plan and Claude Code's 5-hour and weekly limits, and recommends paying for both, using Claude for large tasks and Cursor's Auto mode for the rest. The segment is a single-user impression with no benchmarks, and a sponsored ScaleKit read sits in the middle.

## Key ideas
- **Cursor has closed much of the gap with Claude Code** — Speaker lists plan mode, custom slash commands, auto-tracked to-dos, better localhost server management, a more reliable background terminal, and sandboxed terminals for auto-run mode. Much of this re-announces features Claude Code already had. ([0:00](https://youtu.be/WKy71aZHx20?t=0))
- **Cursor plan mode mirrors Claude Code's plan flow** — The agent asks follow-up questions, writes a detailed plan shown in a clean pane with to-dos, and starts building once the plan is accepted. The plan is saved as markdown in the interface. ([1:09](https://youtu.be/WKy71aZHx20?t=69))
- **Native multi-agent window and git-worktree isolation** — Cursor adds an agent window for parallel agents and an option to launch each agent in its own git worktree. Background agents report back via Linear, Slack and GitHub integrations. The speaker credits Conductor with the worktree idea for Claude Code. ([2:20](https://youtu.be/WKy71aZHx20?t=140))
- **Context handling is closing the gap** — Cursor now shows context usage and has a summarize slash command plus automatic summarization. Before this, a full context simply ended the chat and forced a new window, which the speaker called a major drawback. ([3:19](https://youtu.be/WKy71aZHx20?t=199))
- **Hooks guard destructive commands** — Cursor now has hooks similar to Claude Code's: shell commands that run before or after specific tools. The speaker demos a hook that stops a remove command from deleting critical files, and Cursor also has built-in sound notifications. ([3:19](https://youtu.be/WKy71aZHx20?t=199))
- **Built-in browser control turns the agent into a test-and-fix loop** — The agent drives a browser attached to the chat through Playwright on the backend. It can navigate, click, type, scroll, take screenshots, and read console output, errors and network requests. When it hits an error it fixes the code and re-tests. The speaker says it ran more smoothly than Playwright MCP, which he says often gets stuck. ([5:39](https://youtu.be/WKy71aZHx20?t=339))
- **Auto-test pass finds UI issues and adds notifications** — Asking the agent to test for errors led it to check responsiveness, resize elements, fix icon padding and repeated close buttons, and fix accessibility issues. The speaker also highlights OS notifications, menu-bar monitoring of agents, and deep links that open a new chat with a preloaded prompt. ([7:04](https://youtu.be/WKy71aZHx20?t=424))
- **Usability is the main reason people pick Cursor** — Cursor offers visual setup: a ready-made mcp.json, a visual hooks editor, and a UI for creating commands. The speaker says Claude Code needs manual JSON or settings.json edits and a terminal, and that the MCP file can fail in dangerously-skip-permissions mode. He keeps files open in Cursor while running Claude Code in a terminal. ([9:27](https://youtu.be/WKy71aZHx20?t=567))
- **Use both subscriptions, with Cursor Auto mode for most work** — Cursor's usage-based billing used to be the reason people left it. The speaker describes Claude Code's 5-hour windows and new weekly caps, and recommends Claude models for large, complex tasks and Cursor's Auto mode, which picks smaller models when suitable, for the rest. ([10:50](https://youtu.be/WKy71aZHx20?t=650))

## Techniques
- **Share custom commands between Cursor and Claude Code** — Create a .cursor folder with a commands subfolder and add markdown prompt files, the same format Claude Code uses for custom slash commands. Existing Claude Code command files can be copied over directly. *When:* When you want the same reusable prompts in both tools without rewriting them.
- **Plan first, then build** — Describe the app in the agent chat. Answer its follow-up questions, review the to-do plan it writes in the side pane, then accept it so the build starts. The plan stays visible as markdown in the interface. *When:* For longer agent runs where you want a reviewed plan before code is written.
- **One git worktree per agent** — Enable the option to launch agents in separate git worktrees so each agent works on its own full clone of the repo. *When:* When running several agents in parallel on different tasks in the same repository.
- **Browser test-and-fix loop** — Attach the browser tool to the chat, then ask the agent to test the running app and verify all functionality. The agent reads console output, errors and network requests, edits the code to fix what it finds, and re-tests. *When:* For UI QA after an app is built, and for catching accessibility or layout issues.
- **Shareable prompt deep links** — Use Cursor's link generator to create a deep link for a prompt. Opening it in the browser prompts you to open Cursor, and it starts a new chat with the prompt loaded. *When:* For sharing a reproducible task or prompt with a teammate without copy-paste.
- **Guard auto-run with before/after tool hooks** — Attach shell commands that run before or after named tools such as file read or write. The demo blocks a remove command that would delete critical files. A simpler hook plays a sound after the write tool finishes. The speaker says Claude Code configures hooks in settings.json, while Cursor offers a visual editor. *When:* When running agents in auto-run mode and you want a hard stop for destructive commands.
- **Split models across two subscriptions** — Use Claude models in the Claude plan for large, complex tasks, and Cursor's Auto mode for routine work. Auto mode selects a model per task. *When:* When you hit Claude's 5-hour or weekly limits but still want the strongest model for hard work.

## Numbers
- Cursor's Auto mode is excellent for roughly 90% of use cases, per the speaker. ([11:56](https://youtu.be/WKy71aZHx20?t=716))
- The speaker says $20 of Cursor usage goes far because Auto mode switches to smaller models when appropriate. ([9:27](https://youtu.be/WKy71aZHx20?t=567))
- Claude Code uses 5-hour usage windows with rate limits that reset every 5 hours. Users report that Sonnet 4.5 can exhaust a limit after about 30 minutes of work. Weekly caps were added on top. ([10:50](https://youtu.be/WKy71aZHx20?t=650))
- The Cursor browser-control feature had been released about 20 days before the video. ([7:04](https://youtu.be/WKy71aZHx20?t=424))

## Hot takes
- Cursor is easier to use mainly because everything is visual, so Claude Code is for terminal-comfortable developers.
- Cursor's native browser agent is more efficient and reliable than Playwright MCP. This is a single-session impression with no benchmark.
- The best setup is to pay for both: Claude models for big tasks and Cursor Auto mode for the other 90%.
- The title's 'massive upgrade' overstates it. Much of the list (plan mode, slash commands, worktrees, multi-agent windows) already existed in Claude Code.
- Sponsored segment (ScaleKit) in the middle. Hype title and mostly re-announced features cap quality at 2.

## Tools mentioned
Cursor, Cursor Auto mode, Cursor CLI, Claude Code, Claude Code VS Code extension, Claude Sonnet 4.5, Playwright, Playwright MCP, Conductor, Warp Code, Claude Router, Linear, Slack, GitHub, ScaleKit

## Relevance to our work
- **prosharness** (2/3): ProsHarness drives Claude Code runs. Git-worktree-per-agent isolation, notifications for background agents, and menu-bar monitoring map directly to multi-run and phone-approval UX. → *Check whether ProsHarness isolates parallel runs in separate git worktrees, and treat Cursor's per-agent OS notifications and menu-bar status as the UX bar for phone-driven approvals.*
- **agentos** (1/3): Cursor's sandboxed auto-run terminal and before/after tool hooks that block destructive commands are a practitioner reference for exec-style guardrails, similar in spirit to Crucible. → *When writing up Crucible's exec-gate, compare it with the pre-tool hook pattern in this video: a hook that blocks rm on protected paths.*
