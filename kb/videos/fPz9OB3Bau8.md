# This Open Source Tool Gives You God Mode for AI Agents (AoE)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `fPz9OB3Bau8` · [watch](https://youtu.be/fPz9OB3Bau8) · **date:** 2026-06-02 · **length:** 5:56 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** coding-agents, multi-agent, sandboxing-execution · **tags:** agent-of-empires, aoe, tui, tmux, git-worktrees, docker, parallel-agents, claude-code, mission-control

> Better Stack demo of Agent of Empires (AoE), an open-source terminal dashboard that runs many CLI coding agents side by side using git worktrees, status indicators and optional Docker sandboxes. Short and promo-leaning, with little configuration detail.

## Summary
The video introduces Agent of Empires (AoE), an open-source terminal "mission control" that sits above existing CLI coding agents such as Claude and Codex rather than replacing them. The presenter frames the problem as orchestration at 5 to 20 concurrent agents: terminal sprawl, agents stuck or idle without anyone noticing, and branch collisions in one repo. Install is shown as a single Homebrew command, then launching the TUI and pressing N creates a named agent session, with a second session started while the first runs. Each agent gets its own git worktree and branch in the same repository, which the presenter says removes collisions. Status is shown as running, waiting, idle or similar, so you can see which agent needs input without attaching to each one. Optional Docker sandboxes contain agents, sessions survive restarts, and profiles per project and built-in diffs are mentioned. The presenter positions it against tmux (persistence only) and Agent Deck (similar, less structured), and says it is for parallel work across a full repo rather than single-file IDE agents. Caveats given are a rough web dashboard with tmux bugs that were fixed quickly, a small learning curve, and a phone-access feature the presenter did not test. There are no benchmarks, config files or failure cases in the video.

## Key ideas
- **Running 5 to 10 coding agents at once becomes chaotic: many terminals, stuck agents, and branch collisions that go unnoticed.** — The presenter's core claim is that the bottleneck is managing agents, not model quality. The problems listed are terminal sprawl, status blindness, branch conflicts and unsafe full-access agents. ([0:00](https://youtu.be/fPz9OB3Bau8?t=0))
- **AoE is a control layer over existing agents, not a new coding agent.** — It runs Claude, Codex and similar tools already in the user's workflow and organizes them in one view. ([0:41](https://youtu.be/fPz9OB3Bau8?t=41))
- **Setup is one Homebrew install followed by launching the TUI; N creates a named agent session.** — The demo starts two Claude sessions, one for auth and one for refactoring an API, and shows one running while the other waits. Sessions can be grouped into folders. ([0:41](https://youtu.be/fPz9OB3Bau8?t=41))
- **Status is visible across all sessions without attaching to each one.** — Running, waiting and idle states let you jump in only when an agent needs input, which replaces repeatedly checking each terminal. ([2:02](https://youtu.be/fPz9OB3Bau8?t=122))
- **Each agent gets its own git worktree and branch in the same repo.** — This is the stated fix for agents overwriting each other. The video does not show the configuration or how merges are handled. ([3:21](https://youtu.be/fPz9OB3Bau8?t=201))
- **Optional Docker sandboxes, restart survival, per-project profiles and built-in diffs round out the feature set.** — The presenter says worktrees plus Docker make full-access agents safer. Phone access is mentioned but explicitly untested. ([3:21](https://youtu.be/fPz9OB3Bau8?t=201))
- **Fit: useful with two or more agents, not for one.** — The presenter says a single agent gets nothing from it. Caveats are a rough web dashboard and tmux bugs that were fixed quickly. ([4:42](https://youtu.be/fPz9OB3Bau8?t=282))

## Techniques
- **Run many CLI agents from one dashboard** — Install with brew install aoe, run aoe launch (spoken as 'AOE launch'), press N to create a session, give it a name, and pick the agent (Claude in the demo). Create more sessions and group them into folders. Config keys and flags are not shown. *When:* You are running two or more coding agents on the same repo and tracking them through separate terminals or tmux panes is slowing you down.
- **Per-agent git worktree isolation** — AoE gives each agent session its own git worktree and branch in the same repository. The video does not show the commands or how to merge the branches back. *When:* Parallel agents would otherwise edit the same checkout and collide on branches or overwrite each other's changes.
- **Triage agents by status instead of attaching** — Read the status indicators (running, waiting, idle) on the main screen and attach only to sessions that need input. This avoids polling each terminal. *When:* Many agents run unattended for long stretches and you need to know which one is blocked.
- **Optional Docker sandbox per agent** — Enable the Docker sandbox option for a session so the agent runs contained. The video does not show the setting or the image used. *When:* You want to give an agent full tool access without exposing the host system.

## Numbers
- Chaos starts at about 5 to 10 concurrent agents. ([0:00](https://youtu.be/fPz9OB3Bau8?t=0))
- The presenter mentions scaling to 5, 10 or 20 agents. ([0:41](https://youtu.be/fPz9OB3Bau8?t=41))
- Install is one command (brew install aoe). ([0:41](https://youtu.be/fPz9OB3Bau8?t=41))
- The main demo runs two agents at once. ([0:41](https://youtu.be/fPz9OB3Bau8?t=41))

## Hot takes
- The title's 'God Mode' framing is hype. The substance is a six-minute demo with no configuration, benchmarks or failure cases, so quality is capped at 2.
- The presenter says a single agent gets nothing from this tool, which makes the audience clear.
- Phone access is presented as a feature, but the presenter says he did not try it.
- 'Worktrees plus Docker finally made it safe' is an unverified claim in the video.
- The comparison to tmux and Agent Deck is asserted, not demonstrated.

## Tools mentioned
Agent of Empires (AoE), Claude, Codex, tmux, Git worktrees, Docker, Agent Deck, Homebrew

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs the Claude Code CLI with checkpoint and resume, loops and approvals. AoE is a parallel-session control surface with per-agent worktrees and waiting-state visibility, which overlaps with managing several Claude Code runs. → *Check whether ProsHarness gives each concurrent run its own git worktree and shows running, waiting and idle state. Use AoE's status model as a reference for that UI.*
- **agentos** (1/3): AoE's optional per-session Docker sandbox is loosely similar to Crucible's opt-in sandboxed execution. The video gives no implementation detail. → *Low priority: compare AoE's per-session sandbox toggle against Crucible's sandbox model if the Crucible design is being revisited.*
