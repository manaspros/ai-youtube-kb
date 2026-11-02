# T3 Code: Better Than Codex?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `6x7hh6Qzm9U` · [watch](https://youtu.be/6x7hh6Qzm9U) · **date:** 2026-04-02 · **length:** 6:48 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Theo · **orgs:** T3, OpenAI, Anthropic, Cursor
- **topics:** coding-agents, multi-agent, dev-tools · **tags:** t3-code, codex, claude-code, git-worktrees, plan-mode, multi-agent-gui, quick-actions, pr-automation, open-source

> Walkthrough of T3 Code, an open-source desktop GUI for running multiple coding agents (currently Codex) on your existing subscription, with per-thread git worktrees, plan mode, one-click commit/PR, and a list of missing features.

## Summary
Theo walks through T3 Code, a free, open-source agent manager that wraps existing coding-agent CLIs rather than competing with them. In the demo it drives Codex through the user's OpenAI subscription, with Claude Code, Cursor, OpenCode and Gemini listed as planned backends. He argues that GUI-based multi-agent management beats terminal UIs and that model vendors' own harnesses are best for their models. Features shown: per-thread model, reasoning and mode settings, plan mode with markdown export, a new-git-worktree option per thread, parallel agents across projects, a commit flow that auto-writes commit messages, a push-and-open-PR button with PR status in the sidebar, per-turn diff views, quick-action buttons that run commands on worktree creation, and an integrated terminal. He praises its responsiveness with several agents running, though this is anecdotal. He then forks the repo and has Codex add small features (double-click rename, open in terminal, collapsible sidebar, running-terminal indicator). Remaining gaps he names: skill tagging in prompts, a skills and MCP servers view, and a headless cloud mode for remote agents.

## Key ideas
- **T3 Code is a GUI layered over existing coding-agent tools, not a new coding agent. In the demo, all code and responses come from Codex and bill to the user's OpenAI subscription, which is why the app itself is free.** — Motivation: the Codex app is laggy with many agents running and only offers OpenAI models. Model selector currently lists only OpenAI models; Claude Code, Cursor, OpenCode and Gemini support are planned, and Claude Code support is reportedly ready pending Anthropic's answer on whether subscriptions can be used that way. ([0:00](https://youtu.be/6x7hh6Qzm9U?t=0))
- **Argument for keeping each vendor's harness: model makers build the best harness for their own models (OpenAI models in Codex, Anthropic models in Claude Code), so a unified UI should wrap them rather than replace them.** — Theo still switches to Claude Code in the terminal for UI-design tasks, and says a single place to manage both would remove that switching. ([1:08](https://youtu.be/6x7hh6Qzm9U?t=68))
- **Per-thread controls: reasoning level, model, fast mode (OpenAI only), chat vs plan mode, full access vs supervised tool calls, and local checkout vs new git worktree.** — He leaves the thread in plan mode and on a new worktree, which keeps agent work off the main checkout. ([1:08](https://youtu.be/6x7hh6Qzm9U?t=68))
- **Parallel agents across projects, with plan-first flow. Theo runs three agents at once, and one pauses to ask a clarifying question mid-run before producing a plan he can export as markdown or save to the workspace.** — Then he approves implementation. The plan is shown in-chat and can be expanded to read in full. ([2:28](https://youtu.be/6x7hh6Qzm9U?t=148))
- **Performance is the main selling point. He reports running several agents for hours without lag, and threads, including very long ones, load immediately. This is an anecdote from one user, not a benchmark.** — He contrasts this with the Codex app, which he says he has had to restart when agents lagged. ([2:28](https://youtu.be/6x7hh6Qzm9U?t=148))
- **Ship-path buttons: the commit dialog auto-generates a message when left blank. A combined push-and-create-PR action generates the message, pushes, and opens a PR. The sidebar shows PR status, turning red when rejected and purple when merged.** — Also: diff view per turn or combined, in split or unified layout; an open-in-Cursor or Finder button; and an integrated terminal. ([3:39](https://youtu.be/6x7hh6Qzm9U?t=219))
- **Quick actions are per-project buttons bound to a command. They can run automatically when a worktree is created or be given a keybinding. His example runs an install inside the project.** — Adding a project by pasting its path is faster than browsing Finder when scaffolding in the terminal. ([4:48](https://youtu.be/6x7hh6Qzm9U?t=288))
- **Open source plus an agent means you can fix your own tool. He clones the repo and has Codex add double-click thread rename, an 'open in terminal' menu item, a Cmd+B sidebar collapse, and a running-terminal indicator. He notes the result has some formatting issues.** — Missing features he still wants: skill tagging in prompts, a view of installed skills and MCP servers, and a headless mode on a dev machine or cloud VM for managing remote agents. ([5:59](https://youtu.be/6x7hh6Qzm9U?t=359))

## Techniques
- **One git worktree per agent thread** — When starting a thread in T3 Code, pick 'new work tree' instead of 'local' and leave the base branch as main. Each agent then edits its own checkout, so several agents can run on one repo at once. *When:* Running multiple coding agents concurrently on the same repository, or on multiple projects, to avoid collisions in the working tree.
- **Plan first, then implement** — Set the thread to plan mode, let the agent explore the repo and ask any clarifying questions, review the plan in-chat, export it as markdown or save it to the workspace, then switch to implementation. *When:* Larger or ambiguous tasks, where you want to check the approach before any code changes.
- **Supervised vs full-access tool calls** — Per thread, choose 'supervised' to approve tool calls or 'full access' to let the agent run them without prompts. *When:* Use supervised mode for unfamiliar repos or risky operations; full access for trusted, sandboxed or throwaway work.
- **One-click commit, push and PR** — Use the combined commit menu action 'push and create PR' with a blank message. It generates the commit message, pushes the branch and opens a PR, and the sidebar then tracks PR status. *When:* Shipping a finished agent branch quickly without leaving the app.
- **Quick-action buttons for setup commands** — In project settings, define a command and choose whether it runs on worktree creation or from a keybinding. Example in the video: an install command. *When:* Every new worktree needs a setup step, such as installing dependencies, before an agent can run tests.
- **Fork the agent GUI and let the agent extend it** — Clone the open-source repo, then ask Codex in it to add the missing features (e.g. double-click rename, sidebar collapse, open terminal from a menu). *When:* A tool you use daily lacks a small feature. Theo treats this as a fast way to customize, though the results need review.

## Numbers
- T3 Code is free because it runs on the user's existing OpenAI subscription. No pricing figures are given. ([0:00](https://youtu.be/6x7hh6Qzm9U?t=0))
- Three agents run in parallel during the demo, one per project, and the app stayed responsive for a few hours (anecdotal). ([2:28](https://youtu.be/6x7hh6Qzm9U?t=148))
- A 6:48 video. Speaker's own multi-agent usage lasted 'a few hours' with no lag observed. This is one user's report, not a measurement. ([2:28](https://youtu.be/6x7hh6Qzm9U?t=148))

## Hot takes
- Model vendors make the best harness for their own models, so wrapper GUIs should delegate to Codex or Claude Code, not reimplement the agent loop.
- A GUI is a better interface than a terminal for managing multiple agents across projects, despite the terminal-UI hype.
- The Codex app's RAM and lag problems with many agents are the main reason to switch, and T3 Code avoids them.
- Subscription-backed GUI wrappers depend on vendor policy. Theo says Claude Code support is waiting on Anthropic's clarification.

## Tools mentioned
T3 Code, Codex, Codex app, Claude Code, Cursor, OpenCode, Gemini, git worktrees, Finder

## Relevance to our work
- **prosharness** (1/3): ProsHarness also wraps Claude Code CLI runs. T3 Code's per-thread worktree isolation, supervised vs full-access approvals, and plan-then-implement flow overlap with its checkpoint, approval and plan-critique features. → *Check whether ProsHarness runs each long agent job in its own git worktree, so parallel or resumed runs don't collide on one checkout, and look at T3 Code's supervised/full-access toggle as a model for ProsHarness's phone-driven approvals.*
