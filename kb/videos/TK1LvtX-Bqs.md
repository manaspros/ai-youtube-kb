# Spotify Made an Agent Harness... I Don't Hate It

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `TK1LvtX-Bqs` · [watch](https://youtu.be/TK1LvtX-Bqs) · **date:** 2026-09-02 · **length:** 8:02 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Better Stack host (unnamed) · **orgs:** Spotify, Anthropic, OpenAI, Google
- **topics:** coding-agents, multi-agent, dev-tools · **tags:** zerp, spotify, agent-harness, session-management, git-worktree, fork-session, agent-switching, dependent-sessions, claude-code, codex, gemini, tmux, t3-code, conductor, cmux, closed-source

> Walkthrough of Spotify's closed-source agent session manager "Zerp" (Claude Code, Codex, Gemini in one GUI). Useful session features, but the host finds nothing that justifies the account and closed-source tradeoff.

## Summary
The host tries Spotify's internal agentic development environment, called Zerp (auto-captions render it as "Zurb" early on), built for over 1,300 Spotify engineers. Zerp does not replace Claude Code, Codex or Gemini; it is a GUI that manages their sessions, each of which is a real terminal instance of the agent. Its main strengths are session navigation, a grid view that shows several agents side by side, and some unusual session features: forking a session with full context, switching the agent mid-session (Claude Code to Codex, with history migrated), and dependent child sessions in a child worktree that wait for a parent session to finish. The git sidebar and diff view are usable, but the diff view is full screen, the built-in browser cannot be driven by the agent, and the project view is weak (the prompt box cannot reference skills or files, and project skills behind a symlink were not picked up). The host's verdict is that he would not use it: he prefers working one session at a time and finds T3 Code, which is open source, more polished. He also notes Zerp is pushed alongside a larger Spotify product, Portal, aimed at very large organisations. Because the content is mostly a UI tour and opinion with few hard numbers, the notes are light on reproducible detail.

## Key ideas
- **Zerp is a GUI for managing existing coding-agent sessions, not a replacement agent.** — It runs Claude Code, Codex and Gemini sessions, each a normal terminal instance, and adds a sidebar, project pages and layouts on top. Built for more than 1,300 Spotify engineers. ([0:03](https://youtu.be/TK1LvtX-Bqs?t=3))
- **Access requires a separate Spotify technology account, and the tool is closed source.** — The host counts both against it. Portal is named as the larger related product that Zerp integrates with for pulling cross-project context. ([0:03](https://youtu.be/TK1LvtX-Bqs?t=3))
- **Multi-session grid view is the main navigation win.** — Sessions can be shown side by side (four were shown), the grid size is configurable, grid handles resize rows and columns, and plain terminals can be added alongside agent sessions. The host says tmux is required under the hood. ([1:22](https://youtu.be/TK1LvtX-Bqs?t=82))
- **Forking a session clones its full context into an independent session.** — Useful for trying a different follow-up message without losing the existing thread. ([2:39](https://youtu.be/TK1LvtX-Bqs?t=159))
- **The agent behind a session can be switched mid-session, migrating the history.** — The example moves a Claude Code session that did the coding over to Codex for code review. Context and chat history carry over and the session keeps working. The host says he would not use this often. ([2:39](https://youtu.be/TK1LvtX-Bqs?t=159))
- **Dependent sessions chain work through child worktrees.** — A new session is created as a child worktree of the current one and waits for the parent to finish before starting its goal. There is also a start-now bypass. Dependent terminal sessions share the agent's worktree. ([3:52](https://youtu.be/TK1LvtX-Bqs?t=232))
- **The git view and browser pane have gaps for review and debugging.** — The git sidebar lists changed files with diffs, but the diff view is full screen (the host prefers a sidebar diff, as in Codex and T3 Code). The browser pane cannot be controlled by the agent and has no console or devtools access. ([4:49](https://youtu.be/TK1LvtX-Bqs?t=289))
- **The project view is weaker than the session view.** — The overview prompt box cannot reference project skills or files. The skills tab did not pick up project skills that were symlinked. The rules tab shows the global and project CLAUDE.md and allows editing them. There is also a basic in-app file editor. ([5:49](https://youtu.be/TK1LvtX-Bqs?t=349))
- **The verdict depends on workflow fit, not on bugs.** — The host found no major bugs apart from the skills issue. He prefers one session at a time with a quick diff sidebar, and prefers the open-source T3 Code. He notes Zerp is aimed at very large organisations. ([7:12](https://youtu.be/TK1LvtX-Bqs?t=432))

## Techniques
- **Dependent worktree chains for agent work** — From the current worktree, create a child worktree and give it a goal. It stays queued until the parent session finishes, then starts automatically, or it can be started immediately. Dependent terminal sessions can be attached to the same worktree for manual work alongside the agent. *When:* When one agent task has to finish before the next starts on the same codebase, e.g. implement then review, and you want the chain queued rather than watched.
- **Forking a session to test alternatives** — Clone a session in full, including its context, and send a different message to each copy. The copies are independent afterwards. *When:* When you want to try two follow-ups or approaches from the same point without losing the existing thread.
- **Mid-session agent handoff** — Mid-session, switch the agent (e.g. Claude Code to Codex). Chat history and context migrate, and you continue with a message such as 'continue in here'. *When:* When a different model is better suited to a later step, such as using a second model for code review after the first model wrote the code.
- **Grid monitoring of parallel agents** — Open the grid view, use add-all to place sessions into the grid, set the column and row count, and drag the grid handles to adjust. Plain terminals can be added alongside agent sessions. *When:* When supervising three or four agent sessions at once on a large monitor. The host says he prefers one-at-a-time, so this suits people who like to watch in parallel.

## Numbers
- Zerp was built for over 1,300 Spotify engineers. ([0:03](https://youtu.be/TK1LvtX-Bqs?t=3))
- A project showed six active sessions, one of them just finished and the rest idle. ([1:22](https://youtu.be/TK1LvtX-Bqs?t=82))
- The grid view showed four agent sessions side by side. ([1:22](https://youtu.be/TK1LvtX-Bqs?t=82))

## Hot takes
- Requiring a separate Spotify technology account and a closed-source app is a strike against it for a developer tool.
- Most of Zerp's features are things the host can already do with tmux or cmux, so the value is mainly for GUI-first users.
- The forking and agent-switching features are novel compared with other tools the host has used, but he does not expect to use them much.
- Zerp's design targets very large organisations and cross-project context via Portal, which the host thinks explains its feature set but makes it a poor fit for individuals.

## Tools mentioned
Zerp (Spotify internal agentic development environment; auto-captions transcribe it as Zurb), Claude Code, Codex, Gemini, Portal (Spotify product, related to Zerp), tmux, CMUX, Conductor, T3 Code, Matt Pocock's skills (referenced, not in the video)

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps Claude Code and handles checkpoint/resume, loops and schedules. Zerp's fork-session, mid-session agent handoff and dependent child-worktree sessions are the same kinds of harness primitives. → *Compare ProsHarness checkpoint/resume and loop scheduling against Zerp's fork and dependent-session model, and decide whether a 'wait for parent session, then run child goal' step should be a first-class ProsHarness primitive.*
