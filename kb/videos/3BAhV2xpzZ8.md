# Is This A Better Way to Use Git?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `3BAhV2xpzZ8` · [watch](https://youtu.be/3BAhV2xpzZ8) · **date:** 2026-03-02 · **length:** 5:29 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host (not named in the transcript) · **orgs:** GitButler, GitHub, Better Stack
- **topics:** dev-tools, coding-agents · **tags:** gitbutler, git, virtual-branches, stacked-prs, commit-messages, github-pr, git-gui, mcp, claude, cursor, vs-code

> A 5-minute walkthrough of GitButler, a GUI layer over Git that adds virtual branches, AI commit messages, and easier history rewriting, with an honest pros and cons take.

## Summary
The host introduces GitButler, a Git client built by Scott Chacon, and runs it on a normal existing repo with no migration. GitButler sits on top of Git rather than replacing it, and the presenter uses the GUI while noting a CLI also exists. The main idea is virtual branches: edits in the single working tree can be dragged hunk by hunk into separate logical branches, so the presenter avoids stashing and branch switching while the files stay in place. AI generates commit messages, commits can be reordered, and history can be rewritten by dragging, squashing or amending commits, with a timeline that allows undo. The presenter opens a PR straight from the app, and teammates see an ordinary GitHub PR. The pros are parallel work, easy history editing, and safer experimentation. The cons are a GUI-first design, beta-level bugs, possible slowness on huge repos, and AI features that need your own API keys. The presenter recommends it most for people using AI coding tools, stacked PRs, or multiple tasks as a solo developer, and says it is free during beta.

## Key ideas
- **GitButler is a layer on top of Git, not a replacement. The repo stays a normal Git repo with no migration.** — Setup is a GUI install from the GitButler site. You set the target branch to main, authenticate GitHub, and it takes about a minute. ([1:21](https://youtu.be/3BAhV2xpzZ8?t=81))
- **Virtual branches let you split one working tree into several logical branches without stashing.** — You drag individual hunks from the working tree into a virtual branch. Physically the files stay where they are, while the changes are logically separated. ([1:21](https://youtu.be/3BAhV2xpzZ8?t=81))
- **AI commit messages and commit reordering are built into the commit flow.** — Clicking generate writes a commit message with AI, and commits can be reordered before pushing. ([1:21](https://youtu.be/3BAhV2xpzZ8?t=81))
- **Rewriting history becomes low-friction, with an undo timeline that makes experiments safer.** — Commits can be dragged, squashed and amended, and the whole operation can be undone through a full timeline of changes. ([2:45](https://youtu.be/3BAhV2xpzZ8?t=165))
- **PRs can be opened from the app and look like normal PRs to the team.** — After pushing the branch, the presenter opens the PR from GitButler. Teammates do not need GitButler, and the PR looks like any other GitHub PR. ([2:45](https://youtu.be/3BAhV2xpzZ8?t=165))
- **The presenter's honest downsides are a learning curve, GUI-first design, beta bugs, possible slowness on huge repos, and BYO API keys for AI features.** — The CLI exists but is secondary. The presenter says the setup could be learned in under an hour. ([3:52](https://youtu.be/3BAhV2xpzZ8?t=232))
- **Best fit is AI-heavy workflows, stacked PRs, or juggling several tasks as a solo developer. It is less useful for strictly linear CLI-only work.** — This is the presenter's own judgment after a single short demo on one simple repo. ([3:52](https://youtu.be/3BAhV2xpzZ8?t=232))
- **Adoption tips: start with the GUI, bring in the CLI later for scripts, and integrate MCP early for agent-style work.** — The presenter cites over 18,000 GitHub stars as a sign of interest. This is a popularity figure, not evidence of quality. ([4:48](https://youtu.be/3BAhV2xpzZ8?t=288))

## Techniques
- **Virtual branches for parallel work on one working tree** — Keep editing in the single working tree. Open GitButler, create a virtual branch, then drag individual hunks into it. Each virtual branch holds its own logical set of changes, so you avoid stashing and branch switching. Files are never moved on disk. *When:* You are mid-feature and need to fix something unrelated, or you are running several tasks at once as a solo developer.
- **AI-generated commit messages** — Stage the hunks into a virtual branch, click generate in the commit flow to get an AI-written message, then edit as needed. Reorder commits before pushing if needed. *When:* Commit messages are a chore, and you want a clean history without writing each message by hand.
- **Drag, squash and amend commits with undo** — Rewrite history in the GUI by dragging commits into a new order, squashing, or amending. Use the timeline to undo any step if the result is wrong. *When:* Cleaning up a branch before a PR, where you would otherwise reach for interactive rebase.
- **Open a PR from the app** — Push the virtual branch from GitButler, then open the PR from inside the app. It uses your authenticated GitHub connection. Reviewers see a standard PR. *When:* Shipping work to a team that does not use GitButler.
- **Adoption path for GitButler** — Start with the GUI for daily work. Bring in the CLI later for scripts. If you run agent-style AI work, connect MCP early. *When:* Evaluating GitButler for a team or for AI-assisted coding workflows. The presenter gives no further detail on MCP setup.

## Numbers
- Setup takes about one minute: install, set target branch to main, authenticate GitHub. ([1:21](https://youtu.be/3BAhV2xpzZ8?t=81))
- Learning curve described as under an hour for this workflow. ([3:52](https://youtu.be/3BAhV2xpzZ8?t=232))
- GitButler has over 18,000 GitHub stars, as stated by the presenter. ([4:48](https://youtu.be/3BAhV2xpzZ8?t=288))
- The app is free during beta, per the presenter. AI features require the user's own API keys. ([2:45](https://youtu.be/3BAhV2xpzZ8?t=165))

## Hot takes
- Presented as a Git workflow fix with a 'better way' title, but the demo is a single short session on one simple repo, with no measurements of speed, reliability, or large-repo behavior.
- The presenter calls it a game changer for AI-heavy workflows, but that is relayed popularity and personal opinion, not evidence.
- The presenter says it is worth trying but also acknowledges a learning curve, beta bugs, and possible slowness on huge repos. The pros and cons are balanced.

## Tools mentioned
GitButler (GUI and CLI, beta, free during beta per the presenter), Git, GitHub, VS Code, Claude, Cursor, MCP

## Relevance to our work
- **prosharness** (1/3): ProsHarness runs Claude Code, and GitButler's virtual branches could separate concurrent agent edits. The MCP mention is passing, with no detail. → *Test whether GitButler virtual branches can keep edits from two concurrent Claude Code runs in separate logical branches, and check whether its MCP support lets a harness create commits or PRs.*
