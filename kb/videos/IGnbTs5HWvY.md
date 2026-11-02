# Warp + Neovim + Superfile: This Terminal Setup CHANGED How I Code

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `IGnbTs5HWvY` · [watch](https://youtu.be/IGnbTs5HWvY) · **date:** 2025-11-02 · **length:** 4:32 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Warp
- **topics:** dev-tools, coding-agents · **tags:** warp, neovim, vim-motions, lazyvim, nvchad, superfile, lazygit, fish-shell, terminal-setup, aerospace, ssh, kitty-graphics-protocol, noice, supermaven, avante, opencode

> A Better Stack presenter walks through a terminal-only workflow: Vim motions learned over about a month, NeoVim on top of LazyVim/NVChad, Warp as the terminal with its Agent used to maintain the NeoVim config, plus superfile, lazygit and fish. Mostly personal anecdote with a few transferable tips.

## Summary
The presenter says they use the terminal for almost everything and describes how they got there in under three months. The first hurdle is learning Vim motions, which they picked up with the VS Code Vim extension and about a month of regular practice alongside touch typing. They moved to NeoVim because VS Code and Cursor had coarse undo and incomplete Vim motion support. They started from NVChad and say LazyVim would have been the better base, then added a few plugins: noice for the command line and notifications, supermaven for autocomplete, and avante only for inline AI chat, with OpenCode used for full AI conversations. The Warp terminal (used for over three years) is the glue: its Agent installs plugins from a repo link, adds key mappings, and wrote a script that replays the NeoVim config on SSH hosts. Warp is also styled to match NeoVim (theme, font, Vim keybindings, hidden tabs, 20px padding), and its Kitty graphics support lets superfile preview images inline. lazygit handles large diffs, and fish replaces zsh for speed. The video offers no benchmarks and no step-by-step reproduction; the window padding comes from AeroSpace, which is only mentioned.

## Key ideas
- **Learning Vim motions is the hardest step, and the presenter says it took about a month of regular use to feel comfortable.** — They started with the VS Code Vim extension (following a FreeCodeCamp video) and practised touch typing alongside. Basics mentioned: hjkl for movement, u to undo, Ctrl+R to redo, and yank/paste. ([0:00](https://youtu.be/IGnbTs5HWvY?t=0))
- **Moved from the VS Code/Cursor Vim plugin to NeoVim because undo was not granular enough and Vim motions did not work across all of the editor.** — The presenter says the other parts of VS Code and Cursor did not support Vim motions, so navigation style kept switching. NeoVim keeps one navigation model everywhere. ([1:23](https://youtu.be/IGnbTs5HWvY?t=83))
- **Start NeoVim from LazyVim rather than NVChad if you do not need NVChad's extras.** — They began with NVChad and say that, in hindsight, LazyVim would have suited them better because they used few of NVChad's features. The base came with nvim-tree, mason for LSPs and lualine. ([1:23](https://youtu.be/IGnbTs5HWvY?t=83))
- **Warp's Agent is used to maintain the NeoVim config: installing plugins, adding mappings and tweaking the UI.** — Workflow: paste the plugin repo link into Warp and ask it to install the plugin. The same approach handles key mappings and UI adjustments. They also had it generate a setup script that recreates the NeoVim config on any SSH host. ([2:46](https://youtu.be/IGnbTs5HWvY?t=166))
- **Make the terminal look like the editor so NeoVim blends in.** — They match Warp's theme and font to NeoVim, turn on Vim key bindings, hide the tab bar, and add 20px padding. Warp supports the Kitty graphics protocol, so superfile can render image previews inside the terminal. ([2:46](https://youtu.be/IGnbTs5HWvY?t=166))
- **Small, deliberate NeoVim plugin set, with AI kept to specific roles.** — Added noice (command line and notifications) and supermaven (autocomplete). avante is kept only for inline AI chat, and OpenCode handles full AI conversations. ([1:23](https://youtu.be/IGnbTs5HWvY?t=83))
- **Shell and file-tool choices are about speed and fit: fish instead of zsh, lazygit for large diffs.** — The presenter calls fish much faster than zsh. lazygit is used to review big project changes. superfile replaces the default file browser. ([2:46](https://youtu.be/IGnbTs5HWvY?t=166))

## Techniques
- **Vim motions bootstrap via VS Code Vim extension** — Install the Vim extension in VS Code, learn hjkl movement, u undo, Ctrl+R redo and yank/paste, and practise touch typing at the same time. Expect around a month of regular use before it feels natural. *When:* Moving a team or yourself from mouse-driven editing to keyboard-first terminal work.
- **Migrate from the VS Code/Cursor Vim plugin to NeoVim** — Switch to NeoVim once the Vim extension's undo granularity and missing motion support in the rest of the editor become a problem. Use LazyVim as the starter distribution, not NVChad, unless you need its features. *When:* You want one consistent Vim navigation model across all editing and tooling.
- **Agent-maintained editor config** — Give the terminal's AI agent a plugin's repo link and ask it to install and configure the plugin. Ask it for key mappings and UI changes in the same way. Then ask it to write a script that reproduces the config on remote hosts. *When:* Your editor config changes often, or you want the same setup on remote servers reached over SSH.
- **Terminal styling that matches the editor** — In Warp: set the theme and font to match NeoVim, enable Vim key bindings, hide the tabs, and set 20px padding. Window padding is handled outside the terminal by AeroSpace (not covered in detail). *When:* Recording demos or screenshots, or when the editor and terminal should look like one surface.
- **Inline image previews in the terminal** — Use a terminal that supports the Kitty graphics protocol (the presenter uses Warp) and run superfile as the file browser to preview images in place. *When:* Browsing asset-heavy project folders without leaving the terminal.
- **Split AI roles inside the editor** — Use a narrow inline AI plugin (avante, inline chat only) for small edits, and a separate tool (OpenCode) for longer AI conversations. *When:* You want inline suggestions without a full chat panel in the editor.

## Numbers
- Got from starting Vim to a terminal-first setup in less than three months. ([0:00](https://youtu.be/IGnbTs5HWvY?t=0))
- About one month of regular Vim use before it felt comfortable. ([1:23](https://youtu.be/IGnbTs5HWvY?t=83))
- Has used Warp for more than three years. ([2:46](https://youtu.be/IGnbTs5HWvY?t=166))
- Window padding of 20 pixels in Warp. ([2:46](https://youtu.be/IGnbTs5HWvY?t=166))

## Hot takes
- Vim motions are worth the early pain; the presenter says the design of the model makes sense once learned.
- Start NeoVim with LazyVim, not NVChad (self-described hindsight).
- Let the terminal's AI agent maintain editor config and generate a portable setup script for SSH hosts.
- fish is much faster than zsh (asserted, no measurement shown).
- Quality is limited: a personal setup tour with no benchmarks, no reproducible steps, and an unverified claim about speed.

## Tools mentioned
Warp (terminal, with Warp Agent), Neovim, LazyVim, NVChad, nvim-tree, mason, lualine, noice, supermaven, avante, OpenCode, VS Code Vim extension, Cursor, superfile, lazygit, fish shell, zsh, AeroSpace, SketchyBar, Kitty graphics protocol
