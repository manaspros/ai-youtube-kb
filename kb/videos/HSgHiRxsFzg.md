# Warp Terminal - 6 GAME-CHANGING Features You Need to Know

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `HSgHiRxsFzg` · [watch](https://youtu.be/HSgHiRxsFzg) · **date:** 2025-11-02 · **length:** 5:12 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Warp, Better Stack
- **topics:** dev-tools, coding-agents · **tags:** warp, terminal, command-blocks, warp-drive, workflows, notebooks, agent-mode, shell-prompt, starship, powerlevel10k, sponsored, feature-tour

> A six-feature walkthrough of the Warp terminal (command blocks, Warp Drive, agent mode, customization), with a Better Stack sponsor segment in the middle. Light on depth, no benchmarks.

## Summary
The presenter, who says they use Warp as their main terminal, walks through six features: an IDE-style command palette, tabs and splits, theming and prompt customization, command blocks, Warp's AI features, and Warp Drive. Warp's blocks group a command with its output so you can search, copy, background, or share them. Agent mode can be toggled with Command+I, and it can run commands and make code changes on your behalf. AI memory works like Cursor rules. Warp Drive stores notebooks, workflows, environment variables and AI memories, either personally or for a team. The video is a short feature tour with no comparisons, measurements or hands-on setup steps. A Better Stack sponsor segment sits in the middle, and the video claims everything works the same on macOS, Linux and Windows.

## Key ideas
- **Warp groups each command and its output into one atomic unit called a block. Blocks can be searched, copied, run in the background with &, shared as a URL, or used to kill a background process later.** — Blocks are the core primitive. Sharing a block creates a link for collaborative debugging. Sharing a whole session lets participants join in a browser, and the speaker warns that this sends data to Warp's servers. ([1:58](https://youtu.be/HSgHiRxsFzg?t=118))
- **Warp's AI is layered into the terminal: # for command suggestions, a natural-language prompt that produces a command, and agent mode (toggled with Command+I, or by just typing) that can run commands and make code changes.** — The speaker says agent mode uses whichever LLM is selected, and that the model can be changed. Voice input is also supported. The example prompt was a trivial question about letters in a word. ([3:25](https://youtu.be/HSgHiRxsFzg?t=205))
- **AI memory is a per-user set of preferences that steer agent suggestions, similar to Cursor rules.** — Memories are stored in Warp Drive alongside notebooks, workflows and environment variables, and can be kept personal or shared with a team. No file format or setup details are given. ([3:25](https://youtu.be/HSgHiRxsFzg?t=205))
- **Warp Drive is the shared store for notebooks (markdown with runnable commands), workflows (saved commands you rarely remember), environment variables and AI memories.** — The speaker uses notebooks for onboarding and workflows for commands like reloading the zsh config. Workflows can be created from scratch, from command suggestions, or from frequently used AI prompts. ([3:25](https://youtu.be/HSgHiRxsFzg?t=205))
- **Customization covers themes (including importable theme.yaml files), window opacity and blur, prompt layout, font and line height, keybindings, and compatibility with PS1, Starship and Powerlevel10k prompts.** — Launch configurations save the layout of tabs and splits so a new window reopens as it was left. Splits can be synced with Option+Command+I, which is useful for running the same command across panes. ([1:00](https://youtu.be/HSgHiRxsFzg?t=60))
- **Warp has IDE-style features: a command palette for navigating sessions, workflows and notebooks, multi-cursor editing, Vim bindings, hover-based command inspection, error underlining, and a viewer for command history.** — The speaker says the palette and layout look familiar to VS Code or JetBrains users. Warp can also render Markdown files and run the shell commands inside them. ([0:00](https://youtu.be/HSgHiRxsFzg?t=0))
- **Sponsor segment: a Better Stack pitch for web-based log search and filtering, status pages, dashboards, alerts, uptime monitoring and on-call, with a free tier. It is not part of the Warp content.** — This is a sponsored plug inside an otherwise product-focused video, so it should not count as evidence for or against Warp. ([1:58](https://youtu.be/HSgHiRxsFzg?t=118))

## Techniques
- **Save recurring commands as Warp workflows** — Create a workflow from scratch, or from a command suggestion, and store it in Warp Drive. Examples from the video are reloading the zsh config. Workflows can also be built from frequently used AI prompts. Personal or team scope is chosen when saving. *When:* For commands you run often but forget the exact syntax of, and for sharing them with teammates.
- **Use notebooks as runnable Markdown runbooks** — Write a Markdown document in Warp Drive that contains commands the terminal can execute directly. *When:* For onboarding a new developer or keeping command-based notes that you want to run, not just read.
- **Run long commands as background blocks** — Append & to a command to run it in the background. Keep working in the terminal, then kill the background process from the block when finished. *When:* For a dev server or watcher you want out of the way while you keep using the shell.
- **Share a block for debugging** — Use the block's share action to generate a URL for one command and its output, or share the whole session so that others can join in a browser. *When:* During pair debugging. Do not share session data that contains secrets, since session sharing goes through Warp's servers.
- **Persist a split layout with launch configurations** — Arrange tabs and splits as needed and save them as a launch configuration. New windows then open in the same layout. Use Option+Command+I to sync input across splits. *When:* When you open the same multi-pane setup every day, or want to repeat one command across several panes.
- **Keep an existing prompt framework** — Warp is said to be compatible with PS1, Starship and Powerlevel10k prompts, so existing prompt configs can stay in place. Prompt order, font and line height can also be changed in Warp's settings. *When:* When you have a tuned shell prompt you do not want to rebuild.

## Numbers
- The video covers six Warp features and runs 5:12 in total. ([0:00](https://youtu.be/HSgHiRxsFzg?t=0))
- Sync splits: Option+Command+I. Agent mode toggle: Command+I (both as spoken). ([1:00](https://youtu.be/HSgHiRxsFzg?t=60))

## Hot takes
- The speaker calls Warp the terminal they could not replace, but gives no comparison with other terminals to support it.
- The Better Stack sponsor segment takes up a noticeable share of a 5-minute video. The presenter says it makes this a sponsored segment, so quality is capped at 2.
- Features are listed without demos of their output, and the agent mode example was trivial. Real evidence on agent quality or cost is absent.

## Tools mentioned
Warp, Warp Drive, Starship, Powerlevel10k, zsh, VS Code, JetBrains, Cursor, Better Stack

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI, and Warp is a terminal that could host it. Warp's agent mode and blocks overlap with the harness's run-control features, but the video shows no integration or checkpoint behavior. → *Optional: if you run ProsHarness inside Warp, check whether Warp's block-level output sharing helps with reviewing long run output. Do not change ProsHarness based on this video.*
- **general** (1/3): Warp's workflows and notebooks are a lightweight way to store recurring repo commands for a team, which is a small dev-tools idea. → *Try saving the most-used repo commands as Warp workflows and see if it beats shell aliases.*
