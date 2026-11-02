# Native Worktrees Just Killed Traditional Claude Code Workflows

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `lj_xZn-Yf18` · [watch](https://youtu.be/lj_xZn-Yf18) · **date:** 2026-03-02 · **length:** 4:35 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Anthropic
- **topics:** claude-code, coding-agents, multi-agent, dev-tools · **tags:** git-worktrees, parallel-branches, subagents, isolation, session-resume, feature-flag-bug

> A 4-minute walkthrough of Claude Code's native git worktree support: run parallel feature branches in isolated worktrees, resume them by name, and use worktree-isolated subagents, with a note on a recent breakage.

## Summary
The host calls native worktree support the biggest recent Claude Code update, letting agents work on several features or bug fixes in isolation with no manual git setup. The demo uses a small React to-do app and three features: a dark mode toggle, localStorage persistence, and editing todos. Each runs in its own worktree and branch at the same time, so one buggy feature does not hold up the others. In the test, two features worked and the localStorage one had a bug, which could be committed or PR'd separately while a dedicated session fixed the broken one. Worktrees can be kept and returned to by name, sessions can be resumed, and the host shows a tmux option that drops you into a worktree directory. Custom subagents can declare worktree isolation in their front matter so each runs in its own worktree within one session. The host closes by noting that many users hit worktree problems after a recent update, which they attribute to a broken feature flag, with a workaround of asking Claude Code to fix its own binary. Worktree hooks for non-git VCSs and for running scripts on creation are mentioned but not demonstrated.

## Key ideas
- **Native worktree support lets Claude Code agents work on multiple features in isolation with no manual git configuration.** — The host frames it as the biggest of many recent Claude Code updates. Worktrees were already available in Claude Desktop and third-party tools such as Claude Squad, but manual setup added mental load. ([0:00](https://youtu.be/lj_xZn-Yf18?t=0))
- **Separate worktrees avoid the single-branch bottleneck where one buggy feature delays every other feature.** — Bundling dark mode, localStorage and todo editing into one PR means one bug blocks all three. Worktrees let each feature live on its own branch, so the working ones can be pushed while the broken one is fixed. ([0:58](https://youtu.be/lj_xZn-Yf18?t=58))
- **Worktrees are created from the CLI with a flag, either with a generated name or a name you choose.** — Running claude with the -w flag creates a worktree with a random name, and passing a name after the flag sets it explicitly. Each one creates a new branch. Old worktrees are not deleted, so temporary ones accumulate. Requires a git repo with at least one commit. ([0:58](https://youtu.be/lj_xZn-Yf18?t=58))
- **In the test, the worktrees made the failure isolated: two features worked and only localStorage broke.** — The host could commit or open PRs for the two working features and debug the third in its own Claude session, without touching the others. ([2:26](https://youtu.be/lj_xZn-Yf18?t=146))
- **Worktrees persist, so they can be returned to, resumed, or removed later.** — Specifying the same name returns to the same worktree. Sessions can be resumed from a worktree, and Ctrl+W lists sessions in the project. The host is unsure how that list maps to the current session. ([2:26](https://youtu.be/lj_xZn-Yf18?t=146))
- **Subagents can be isolated automatically by adding a worktree setting to their front matter.** — Custom subagents with isolation set to worktree spin up their own worktree, so several subagents can work on different branches inside one main session. This is the feature the host finds most interesting. ([3:30](https://youtu.be/lj_xZn-Yf18?t=210))
- **A recent update reportedly broke worktrees for many users, attributed to a feature flag.** — The host's temporary workaround is to ask Claude Code to fix its own binary. They expect a proper fix later. ([3:30](https://youtu.be/lj_xZn-Yf18?t=210))

## Techniques
- **Parallel feature branches with named worktrees** — In a git repo with at least one commit, start one session per feature with the -w flag, e.g. claude -w <feature-name>. Each run creates a worktree under the project's .claude directory (captions read it as .claw; the exact path is not spelled out) plus a new branch. Give each feature its own session and keep the feature work separate. *When:* Several independent features or bug fixes in one repo, where one of them might break or need a separate PR.
- **Isolate a broken feature and ship the rest** — After parallel work finishes, test each worktree. Commit or open PRs for the ones that work. Open a dedicated session in the broken worktree to fix it, leaving the others untouched. *When:* A batch of features where one fails review or testing.
- **Return to or resume a worktree** — Re-run the worktree command with the same name to get back to that worktree. Resume its session from there, or press Ctrl+W to pick a session from the project list. The transcript does not show the full resume command. *When:* Coming back to unfinished work in a kept worktree.
- **Open a shell in a worktree directory with tmux** — The host runs the worktree command with a tmux flag that takes you straight to the worktree directory, then opens a split pane in it. The exact flag name is not shown in the transcript. *When:* Keeping a shell in a worktree beside the main session while working on it in parallel.
- **Worktree isolation for custom subagents** — In a custom subagent's front matter, add the isolation setting with the value worktree. Claude then gives that subagent its own worktree automatically, so several subagents can edit different branches in one session. The host shows the setting name only in passing. *When:* Delegating parallel coding tasks to subagents that must not share a working tree.
- **Clean up temporary worktrees** — Keep or remove worktrees when finished. Temporary worktrees are not deleted automatically, so remove them yourself to avoid buildup. The host does not show the removal command. *When:* After a parallel batch of work, or when temporary worktrees pile up.

## Numbers
- Test used three parallel worktrees, one per feature (dark mode, localStorage, editing todos); two worked and the localStorage one had a bug. ([0:58](https://youtu.be/lj_xZn-Yf18?t=58))
- Worktrees need a git-initialized project with at least one commit. ([0:58](https://youtu.be/lj_xZn-Yf18?t=58))

## Hot takes
- Worktrees are a major Claude Code update that makes parallel features practical, the host says, and they plan to use it more.
- Many users reportedly hit worktree breakage after a recent update, attributed to a broken feature flag; the host says it may have been released too soon.
- Temporary worktrees are not cleaned up automatically, so the host warns that they accumulate.
- The host is unsure how the Ctrl+W session list relates to the current session.

## Tools mentioned
Claude Code, Claude Desktop, git, React, tmux, Claude Squad, React Doctor, SVN, Jujutsu

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and does checkpoint/resume of long runs, loops and plan-critique-debate. Worktree isolation and name-based resume map directly onto running parallel or resumable agent work. → *Prototype running each ProsHarness parallel task in its own claude -w worktree, or as an isolation: worktree subagent, and check how it interacts with checkpoint/resume.*
- **general** (2/3): Claude Code and coding-agent workflows are a recurring interest. Worktrees plus worktree-isolated subagents are a concrete multi-agent pattern for the team's own development. → *Try claude -w for two concurrent features in one repo and an isolation: worktree subagent, and check the feature-flag breakage the host describes before relying on it.*
- **agentos** (1/3): Per-task workspace isolation is a general pattern for concurrent agents. It is adjacent to the Crucible sandbox work but not a direct change to the AgentOS stack. → *Note worktree-per-task isolation as a lightweight workspace-isolation pattern to compare against Crucible sandboxes for concurrent coding agents.*
