# Why WezTerm Beats Ghostty, Warp, and tmux COMBINED

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `kYBvkzwM8Iw` · [watch](https://youtu.be/kYBvkzwM8Iw) · **date:** 2025-11-02 · **length:** 7:12 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** wezterm, terminal, lua-config, tmux, multiplexer, ghostty, warp, fish, ssh, keybindings, asciicast

> A Better Stack walkthrough of configuring WezTerm (a Lua-configured, GPU-accelerated Rust terminal) to look like Warp, rebind keys, and use its built-in remote multiplexer as a tmux replacement.

## Summary
The presenter moves from Warp to WezTerm and walks through a Lua config file in the home directory: font, line height, color scheme, cursor colors, and removing the title bar and tab bar. He then changes keybindings so closing a pane skips the confirmation prompt and splits are easier to reach, and adds a clear-screen shortcut. He shows the WezTerm CLI and remote multiplexing over an SSH domain, which he says mostly removes his need for tmux. He compares WezTerm with Ghostty (an early stability problem with AeroSpace, which he admits may be outdated) and Warp (which he keeps for debugging and AI features). The claims that WezTerm is the fastest terminal he has used and that it replaces tmux are anecdotal, with no benchmarks. The video is a single-user config walkthrough rather than the head-to-head comparison its title suggests.

## Key ideas
- **WezTerm is configured entirely in Lua, with almost no settings UI** — A fresh install looks basic. Settings go in a ~/.wezterm.lua file that builds a config table and returns it. The presenter says WezTerm picked up his fish shell config, autocomplete plugin and Starship prompt without extra setup. ([0:00](https://youtu.be/kYBvkzwM8Iw?t=0))
- **Warp-like look is reproduced with a few config keys** — He sets font size, line height, a Nerd Font and the TokyoNight Night color scheme, then fixes the cursor border so it matches the cursor color in split panes. He removes the title bar with window decorations set to RESIZE and hides the tab bar. ([1:24](https://youtu.be/kYBvkzwM8Iw?t=84))
- **Keybindings are the main customization point** — Closing a pane (Cmd+W) can skip the confirmation prompt. Horizontal and vertical splits get Cmd-style shortcuts, using the current pane's domain so splits stay local or remote. Cmd+K is bound to clear. He notes the command palette (Shift+Ctrl+P) lists actions and that a leader key is possible, as in Neovim. ([2:51](https://youtu.be/kYBvkzwM8Iw?t=171))
- **The built-in remote multiplexer is the main reason to use it over tmux** — After installing WezTerm on a remote server and defining that server as a domain in the config, running wezterm connect to that domain lets new tabs and splits open inside the remote session without re-SSHing. He says this almost removes his need for tmux. ([4:16](https://youtu.be/kYBvkzwM8Iw?t=256))
- **Ghostty and Warp are both rejected for different reasons** — His early Ghostty trial hit a problem with the AeroSpace window manager that the docs' fix did not solve. He says he has not rechecked since. Warp stays in his toolkit for debugging and its AI features, but he prefers WezTerm's rendering, customizability and speed. ([5:43](https://youtu.be/kYBvkzwM8Iw?t=343))
- **Quick select and image protocols are built in** — Shift+Ctrl+Space opens a quick-select mode for common patterns such as paths and hashes. WezTerm also supports several inline image protocols, ligatures and hyperlinks. ([5:43](https://youtu.be/kYBvkzwM8Iw?t=343))

## Techniques
- **Minimal ~/.wezterm.lua skeleton** — Create ~/.wezterm.lua. Load the WezTerm API, create a local config from the config builder, set keys on it, and return it at the end of the file. Save and the change applies. The presenter demonstrates a font size change this way. *When:* Starting a new WezTerm config. The config builder gives validation of config keys.
- **Warp-style visuals** — Set font_size = 19, line_height = 1.2, font = wezterm.font 'Black Mono Nerd Font' (transcribed name; check the exact family), color_scheme = 'TokyoNight Night' (as spoken). Set the cursor background to a light blue and set the cursor border to the same color, otherwise split panes show a white border. Set window_decorations to RESIZE to drop the title bar, and enable_tab_bar = false to hide tabs. *When:* Making WezTerm look clean and close to Warp, with no chrome. The cursor border fix matters once you use splits.
- **Close pane without confirmation** — Under config.keys, bind Cmd+W to the close-current-pane action with the confirmation disabled (the speaker pasted a binding he had saved earlier; the exact action name was not shown). The command palette (Shift+Ctrl+P) lists available actions. *When:* Using tabs and panes often and finding the kill-tab prompt annoying.
- **Split bindings with domain awareness** — Bind Cmd+D to a vertical split and Shift+Cmd+D to a horizontal split. Set the split's domain to the current pane's domain so new panes stay on the same local or remote host. (The transcript contradicts itself on which key makes which split; the demo shows Cmd+D = vertical, Shift+Cmd+D = horizontal.) *When:* Splitting panes into local or remote SSH sessions without tmux-style prefix keys.
- **Clear-screen binding** — Bind Cmd+K to send the clear command to the shell (likely a SendString action that sends clear plus a newline; not shown explicitly). *When:* Restoring a Cmd+K clear shortcut, which the presenter says his setup lacked.
- **Fish PATH for the WezTerm CLI** — Add the directory that contains the wezterm binary to the fish config (path not named in the video). Without it the CLI does not work from fish. *When:* Using wezterm cli subcommands, such as the multiplexer server, from fish.
- **Remote multiplexing without tmux** — 1) Define the remote server as an SSH domain in the WezTerm config. 2) Install WezTerm on the remote host. 3) Run wezterm connect <domain-name>. 4) Create tabs and splits as usual; they stay on the remote host. *When:* Working on remote servers and wanting tabs and splits to persist without re-SSH and without tmux. Note the video gives no details on session persistence after the local window closes.
- **Terminal session recording with the CLI** — Use the wezterm CLI to record and replay terminal sessions in asciicast format, to open new windows, and to list or kill panes on the multiplexer server. Exact commands were not shown. *When:* Recording demos or sharing terminal sessions in a reproducible format.

## Numbers
- Demo font size set to 19, line height 1.2 ([0:00](https://youtu.be/kYBvkzwM8Iw?t=0))
- Line height set to 1.2 ([1:24](https://youtu.be/kYBvkzwM8Iw?t=84))
- Presenter calls WezTerm the fastest terminal he has used. Anecdotal, no benchmark given. ([5:43](https://youtu.be/kYBvkzwM8Iw?t=343))
- Video length is 7:12. No latency, memory or throughput measurements are shown. ([0:00](https://youtu.be/kYBvkzwM8Iw?t=0))

## Hot takes
- WezTerm's built-in multiplexer almost makes tmux unnecessary (anecdotal, one user's experience).
- WezTerm is the fastest terminal he has used, with no benchmark behind it.
- Ghostty was unstable with AeroSpace, but he admits he has not retested since his early trial.
- The title promises a combined comparison against Ghostty, Warp and tmux, but the video is a single-user config walkthrough with light comparison.

## Tools mentioned
WezTerm, Lua (config language), fish shell, Starship, Warp, Ghostty, tmux, AeroSpace, Neovim, TokyoNight Night (color scheme, as spoken), Nerd Font (named 'Black's Mono Nerd Font' in the auto-captions), asciicast

## Relevance to our work
- **prosharness** (1/3): ProsHarness runs long Claude Code sessions. A terminal with built-in remote multiplexing is a possible alternative to tmux for keeping those sessions alive, but the video does not address agent workflows. → *Low priority: if ProsHarness needs a persistent remote session host for long Claude Code runs, compare WezTerm's multiplexer (wezterm connect over an SSH domain) with tmux before choosing.*
