# herdr: Is This the Ultimate Agent Multiplexer?

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `PlN86TvzGy4` · [watch](https://youtu.be/PlN86TvzGy4) · **date:** 2026-07-02 · **length:** 7:10 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** coding-agents, multi-agent, dev-tools · **tags:** herdr, terminal-multiplexer, tmux, agent-status, claude-code, codex-cli, ssh, unix-socket, rust-tui, ratatui, cmux, warp

> A walkthrough of herdr, a single Rust terminal multiplexer that adds agent awareness (working, blocked, done) to tmux-style panes, lets agents drive it through a CLI or socket, and works over SSH.

## Summary
The video demos herdr, a terminal multiplexer written as one Rust binary on Ratatui with no Electron. It keeps tmux-style persistence and splits but detects coding agents such as Claude Code and Codex CLI and shows their status (working, blocked, idle or done) with system notifications. The demo installs it via Homebrew, curl or a Nix flake, then creates workspaces, tabs and splits by keyboard and mouse. Agents can also use the herdr CLI to spawn panes, give them titles, run prompts, summarise their output and close them. Remote mode runs the server on an SSH host and a thin client locally over a Unix socket, so local keybindings and themes still apply. The reviewer's main argument for it over cmux or Warp is that it runs inside an existing terminal. Windows support is weak because it depends on Unix sockets and PTYs, so WSL or Linux is recommended there. The video is a short product walkthrough with no benchmarks.

## Key ideas
- **Tmux keeps sessions alive but has no idea an agent is running in a pane. herdr combines tmux-style persistence with agent awareness in one terminal-native tool.** — tmux predates AI agents, so a harness in a pane has no status. Warp and cmux solve this by replacing the terminal, which means learning another workflow. herdr stays inside the existing terminal. ([0:00](https://youtu.be/PlN86TvzGy4?t=0))
- **Agent status detection works without configuration in the demo.** — After launching Claude Code in the top pane and Codex CLI in the bottom pane, herdr labelled Claude as blocked and Codex as idle, then showed Claude as working once it got a prompt. It also updates on prompts for Codex CLI. ([2:02](https://youtu.be/PlN86TvzGy4?t=122))
- **Agents can control herdr itself through its CLI or socket API.** — Claude Code was prompted to use the herdr CLI to open two panes running separate prompts, one summarising the largest file and one searching for hard-coded secrets. It titled the panes, read their output, summarised them, then closed both. ([3:14](https://youtu.be/PlN86TvzGy4?t=194))
- **Remote mode runs the server on the SSH host and the thin client locally, so local config applies remotely.** — The client sends keystrokes over a Unix socket to the server, which manages tabs, panes and persistence. The client uses local keybindings and themes, while the files and processes live on the remote machine. Sessions restore after reconnecting. ([4:29](https://youtu.be/PlN86TvzGy4?t=269))
- **Herder is one Rust binary rendering text, so it runs anywhere a terminal runs, including over SSH.** — The reviewer treats the terminal-native design as the main selling point. Setup needs only a single install, and a Nix flake option is included. ([1:00](https://youtu.be/PlN86TvzGy4?t=60))
- **Windows support is weak at the time of recording.** — The design depends on Unix sockets and a PTY. The reviewer recommends WSL or dual booting Linux rather than native Windows. ([6:40](https://youtu.be/PlN86TvzGy4?t=400))

## Techniques
- **Install and launch herdr** — Install with Homebrew, curl or a Nix flake, then run `herdr` in an existing terminal. Default prefix is Ctrl-B. Prefix then `?` shows keybindings, Prefix then `q` quits and leaves sessions running, and `Shift+N` creates a workspace. Prefix-driven navigation is available, but mouse use also works for tabs, splits and pane renaming. *When:* Run several coding agents side by side in one terminal and need them visible and persistent.
- **Remap the prefix key** — The reviewer changed the prefix from Ctrl-B to Ctrl-Space and set the theme to terminal in the config. The config file path was not shown, and the theme list includes Nord, Gruvbox and Catppuccin. *When:* Avoid clashing with a shell or editor binding, or match an existing terminal habit.
- **Agent-spawned panes with herdr CLI** — Inside a Claude Code session, ask it to use the herdr CLI to spawn panes, each running a named prompt. Panes get titles, the parent reads their output, summarises it, then closes them. The demo does not show the exact CLI commands. *When:* Fan a task out to parallel sub-agents, each in a visible pane, then collect and close them.
- **Remote session over SSH with local config** — Install herdr on the remote host, then connect with its remote flag (exact syntax not shown in the video) from the local terminal. The server runs remotely and the client stays local, so local keybindings and themes apply while files and agents stay on the server. *When:* Work on a remote Linux box with your usual keybindings, or reconnect to agents running there.

## Numbers
- herdr ships as a single Rust binary with no Electron or separate app. ([0:00](https://youtu.be/PlN86TvzGy4?t=0))
- Default prefix key is Ctrl-B; the reviewer remapped it to Ctrl-Space. ([2:02](https://youtu.be/PlN86TvzGy4?t=122))
- Agent state shown as blocked, idle, working and done. ([0:00](https://youtu.be/PlN86TvzGy4?t=0))

## Hot takes
- Herdr's main advantage is that it runs inside your existing terminal rather than replacing it, so you keep your own config and workflow.
- tmux is not agent-aware and cannot be fixed without something like herdr, while Warp and cmux require adopting another interface.
- Windows support is not really there yet because of the Unix socket and PTY design; recommends WSL or Linux.
- The 'ultimate' in the title is a stretch for a 7-minute walkthrough with no benchmarks or comparison beyond cmux.

## Tools mentioned
herdr, tmux, Warp, cmux, Claude Code, Codex CLI, OpenCode, Vim, Bash, Fish, Ratatui, Rust, Homebrew, Nix flake, Unix socket, WezTerm (transcribed as 'Westerm'/'West Term')

## Relevance to our work
- **prosharness** (2/3): ProsHarness wraps the Claude Code CLI and needs to show run state (working, blocked, done) and handle phone approvals. herdr detects those states from outside the agent, and its CLI and socket let an agent spawn and close sub-sessions, which overlaps with ProsHarness's subagent and loop control. → *Check whether ProsHarness exposes a machine-readable run state (working, blocked on approval, done) that an external multiplexer or CLI could read, and consider a socket or CLI interface for spawning and closing Claude Code sub-sessions. Read herdr's source for how it detects agent state from terminal output.*
