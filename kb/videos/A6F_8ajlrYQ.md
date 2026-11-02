# LazyGIt - A Faster, Easier Way to Use Git on Terminal & NeoVim

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `A6F_8ajlrYQ` · [watch](https://youtu.be/A6F_8ajlrYQ) · **date:** 2025-11-02 · **length:** 7:26 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** lazygit, git, terminal-ui, neovim, homebrew, hunk-staging, interactive-rebase, merge-conflicts, squash, keyboard-driven

> Better Stack's 7-minute tour of lazygit, a keyboard-driven terminal UI for git, covering hunk staging, commits, push, reset, merge, conflict resolution and squashing.

## Summary
The presenter introduces lazygit as a terminal UI that makes everyday and complex git work (partial staging, interactive rebase) faster from the keyboard, with Neovim integration. He installs it via Homebrew's tap version, launches it inside a repo, and tours the panes: status, files, branches, commits and stash. He then walks through a realistic flow: create a branch, stage whole files and individual hunks, commit with a summary and description, and push with an upstream. He shows recovering from a diverged branch by viewing the upstream divergence and hard-resetting to it. The rest of the video covers merging with squash options, resolving a merge conflict hunk by hunk, squashing selected commits, and toggling a full-screen view with a commit graph. The demo does not show cherry-pick or bisect, which he mentions as also being easier. Overall it is a feature tour with no benchmarks or comparisons.

## Key ideas
- **lazygit is a keyboard-first terminal UI for git that makes partial staging, rebasing and similar operations quicker than raw git commands** — Presented as a way to speed up git from the CLI, with Neovim integration. Works on macOS, Linux and Windows. The presenter installs it with Homebrew's tap build, which he recommends for more frequent updates. ([0:00](https://youtu.be/A6F_8ajlrYQ?t=0))
- **Contextual key hints and a help overlay make the UI discoverable** — Hints for the current pane appear at the bottom. ? opens the full keybinding list for the focused pane, and / searches within it. Esc backs out of views. ([1:11](https://youtu.be/A6F_8ajlrYQ?t=71))
- **Staging works at file, all-files and individual-hunk level** — Space stages or unstages a file, A stages everything, and Enter on a file followed by Space stages a single hunk. Left and right move between hunks, and Tab moves to the staged-changes pane to unstage. ([2:27](https://youtu.be/A6F_8ajlrYQ?t=147))
- **The commit pane exposes history-rewriting actions behind single keys** — Squash, fixup, reword, edit and interactive rebase are all available from the commit pane, and ? lists them. Capital P pushes and prompts to create the upstream branch on first push. ([3:42](https://youtu.be/A6F_8ajlrYQ?t=222))
- **Divergence from upstream can be undone by hard-resetting to the remote branch** — After a reword made the branch diverge from origin, he cancelled the force push. He then opened the upstream options, chose to view divergence from the upstream, and used G on the original commit to hard-reset the branch to upstream. ([3:42](https://youtu.be/A6F_8ajlrYQ?t=222))
- **Merges and conflicts are handled inside the UI** — Capital M opens a merge menu with regular merge, squash merge leaving changes uncommitted, and squash merge with commit. For conflicts, hunks are resolved with Space one at a time, or B to take all hunks, then the merge is continued. ([5:08](https://youtu.be/A6F_8ajlrYQ?t=308))
- **Commits can be squashed by multi-selecting them** — Shift-select a range in the commits pane, press S, and confirm to squash the selected commits into the one below. The same can be done via interactive rebase with i. ([6:22](https://youtu.be/A6F_8ajlrYQ?t=382))
- **A full-screen view mode with a commit graph is available** — Shift+plus cycles view modes and shift+minus cycles backward. The expanded view on a branch with merges shows a commit graph, and in full-screen mode the rebase actions (squash, pick) are also available. ([6:22](https://youtu.be/A6F_8ajlrYQ?t=382))

## Techniques
- **Launch lazygit inside a repo** — Install lazygit with Homebrew's tap version (the exact command is shown on screen, not spoken). cd into a git repository and run `lazygit`. Panes show branch status, working files, local branches, commits and stash. Navigate with the keyboard, with mouse support also available. *When:* Any time you want a visual overview of repo state and keyboard-driven git without memorizing commands.
- **Create and switch branches** — From the main view, press N to create a new branch and enter its name, which creates and checks it out. To switch, select a branch and press Space to check it out. *When:* Starting work on a new feature branch from inside the UI.
- **Hunk-level staging** — In the files pane, press Enter on a modified file to open its diff, then press Space to stage the current hunk. Use Left and Right to move between hunks. Press Tab to go to the staged pane and press Space there to unstage a hunk. *When:* Splitting a working tree into several focused commits, or committing only part of a file.
- **Commit and skip hooks** — Press C to open the commit view, enter a summary and description, then press Enter. Press W instead to commit without running the pre-commit hook. *When:* Normal commits, or when a pre-commit hook needs to be bypassed.
- **Push a new branch with upstream** — Press capital P. On first push lazygit asks for the upstream remote branch name, here origin. Enter confirms. *When:* Publishing a new local branch for the first time.
- **Recover from a diverged branch** — Go to the branches pane (press 3) and press u to open upstream options. Choose the view that shows divergence from the upstream. Select the commit to return to and press G, then confirm the hard reset. *When:* Local rewrites (such as a reword) have made the branch diverge from its remote, and you want the local branch to match the remote again instead of force-pushing.
- **Merge with squash options** — Select the target branch and press Space to check it out. Select the source branch and press capital M. Choose regular merge, squash and leave changes uncommitted, or squash and commit. *When:* Merging a feature branch into main as a single squashed commit.
- **Resolve conflicts by hunk** — After a conflicted merge, open the conflicted file from the files view. Move between hunks with Up and Down and between conflicts with Left and Right. Press Space to resolve the current hunk, or B to resolve all hunks. When everything is resolved, confirm to continue the merge. *When:* Resolving merge conflicts file by file without leaving the TUI.
- **Squash a range of commits** — In the commits pane, hold Shift and select the commits to combine, then press S and confirm. The selection is squashed into the commit below it. Alternatively, press i to start an interactive rebase. *When:* Cleaning up a series of WIP commits before opening a PR.
- **Toggle full-screen and commit graph view** — Press Shift+plus to cycle view modes and reach a full-screen layout, and Shift+minus to cycle back. The expanded commits view shows a commit graph on branches with merges. *When:* Inspecting history topology or working on a long commit list.

## Hot takes
- Feature tour with no benchmarks or comparison to plain git or other TUIs; the value claim is demonstrated through keystroke convenience only.
- The closing claim that lazygit makes anything git does easier, including cherry-pick and bisect, is asserted but not shown in the demo.
- The video is short and solid for a tool intro, but it does not cover configuration, custom keybindings or the Neovim integration it mentions at the start.

## Tools mentioned
lazygit, git, Homebrew, Neovim

## Relevance to our work
- **prosharness** (1/3): ProsHarness drives Claude Code runs that write code. A human-friendly git UI helps inspect and hunk-stage agent edits before committing, but the video is not about agents. → *Try lazygit to review and selectively stage changes made by a Claude Code run in a scratch repo, so the human checkpoint before commit is easier.*
