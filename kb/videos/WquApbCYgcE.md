# The ULTIMATE Arch Linux + Hyprland Dev Setup – Omarchy

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `WquApbCYgcE` · [watch](https://youtu.be/WquApbCYgcE) · **date:** 2025-11-02 · **length:** 6:07 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack presenter (unnamed in transcript) · **orgs:** Better Stack, Omarchy (DHH), Arch Linux, Hyprland
- **topics:** dev-tools · **tags:** omarchy, arch-linux, hyprland, linux-desktop, neovim, lazyvim, dotfiles, keyboard-driven, dev-environment, wayland

> Better Stack walks through Omarchy, DHH's single-script setup for a keyboard-driven, developer-ready Arch Linux and Hyprland desktop, and how to install and customize it.

## Summary
The presenter revived an old laptop with Omarchy, a single install script that turns a fresh Arch Linux system into a preconfigured Hyprland desktop for development. The video is a five-part feature tour: keyboard-only navigation via the Super key, the preinstalled terminal tools (LazyVim, LazyGit, LazyDocker, btop, fastfetch, mise, zoxide, fzf), the GUI and web apps that ship with it, the install procedure, and customization. Customization is kept separate from defaults: personal config lives in ~/.config and is not overwritten by Omarchy. Theme switching is done from a picker that restyles the terminal and menu bar together. The content is a non-technical overview with no benchmarks, and the only reproducible steps are the install prerequisites and the one-line install command.

## Key ideas
- **Omarchy is pitched as a single-script route to a working, developer-ready Arch Linux plus Hyprland desktop, which the presenter says is otherwise hard to build by hand.** — Used to repurpose an old laptop. The presenter notes that a bricked laptop was revived by removing the battery and running on mains power only. This is an anecdote, not a general fix. ([0:00](https://youtu.be/WquApbCYgcE?t=0))
- **The desktop is meant to be driven from the keyboard, with the Super key as the entry point to everything.** — Shortcuts shown: Super+Space opens the app launcher (Wofi), Super+B browser, Super+Enter terminal, Super+J toggles the layout, Super+F file manager, Super+T activity monitor, Super+N Neovim. Caps Lock+Space+N or E types the configured name or email. The docs list the full set. ([1:04](https://youtu.be/WquApbCYgcE?t=64))
- **The terminal stack ships preconfigured with TUI tools and language version management.** — Neovim comes preconfigured with LazyVim. Also included: LazyGit, LazyDocker, btop (the activity monitor), fastfetch (the About page), mise for multiple language runtimes (Ruby, Node, Go, Python, Elixir), zoxide and fzf. ([2:20](https://youtu.be/WquApbCYgcE?t=140))
- **GUI apps are split into open-source defaults and commercial apps, and web apps can be installed as desktop apps.** — Open-source defaults named: Obsidian, mpv, LibreOffice, OBS. Commercial apps named: Spotify and 1Password. ChatGPT and YouTube are installed as app shortcuts (Super+A, Super+Y in the demo) that appear in the launcher with icons. The docs give a command for adding your own. ([3:31](https://youtu.be/WquApbCYgcE?t=211))
- **Installation is a two-stage process: a manual Arch install with disk encryption and wget, then one piped command.** — After Arch is installed (encryption enabled, wget present), the install script is fetched and piped into bash. It asks for the sudo password several times and for git details, and takes 5 to 30 minutes depending on hardware. The presenter then reboots. ([3:31](https://youtu.be/WquApbCYgcE?t=211))
- **Customization is designed to coexist with updates: personal config lives in ~/.config rather than in Omarchy's defaults.** — Monitors, Hyprland setup, workspaces, and added themes and backgrounds are configured there. The presenter says this avoids overwriting Omarchy's defaults. ([4:48](https://youtu.be/WquApbCYgcE?t=288))
- **Theming is global: one picker changes the terminal, menu bar and other components together.** — Opened with Super+Ctrl+Shift+Space. Built-in themes include Catppuccin and Matte Black, and the presenter says the change applies across components. ([4:48](https://youtu.be/WquApbCYgcE?t=288))

## Techniques
- **Keyboard-only desktop navigation** — Use Super+Space to launch apps by name, then direct chords: Super+B browser, Super+Enter terminal, Super+F files, Super+T activity monitor, Super+N Neovim, Super+J layout toggle. Caps Lock+Space+N or E inserts the configured name or email. Check the Omarchy docs for the full binding list. *When:* Working on a tiling Wayland desktop where keeping hands off the mouse is the goal.
- **Scripted developer-environment bootstrap on fresh Arch** — Install Arch with disk encryption and wget. Then run the Omarchy install script fetched with wget and piped into bash (presented as wget omarchy.org/install | bash; the video says 'amachi.org install'). Expect repeated sudo password prompts and a git identity prompt. Allow 5 to 30 minutes, then reboot. *When:* Setting up a repeatable developer machine quickly, with preconfigured tools, instead of assembling Arch and Hyprland by hand.
- **Keep personal desktop config separate from distro defaults** — Edit the Hyprland, monitor, workspace and theme configuration in ~/.config. The presenter says this avoids having Omarchy's default files overwritten. *When:* Customizing a distro-style setup that will receive updates.
- **Turn web apps into desktop apps** — Omarchy installs ChatGPT and YouTube as app shortcuts that show in the launcher with icons. The video says a simple command in the docs adds your own; the command is not shown. *When:* Wanting frequently used web tools to launch like native apps.
- **Global theme switching** — Press Super+Ctrl+Shift+Space to open the theme picker. The chosen theme applies to the terminal, menu bar and other components together. *When:* Changing the look of the whole desktop at once.

## Numbers
- Install takes between 5 and 30 minutes, depending on setup. ([3:31](https://youtu.be/WquApbCYgcE?t=211))
- Video length is 6:07, covering five favorite features (navigation, terminal tools, GUI and commercial apps, customization, install). ([0:00](https://youtu.be/WquApbCYgcE?t=0))

## Hot takes
- Presenter jokes that using a mouse is 'a sin' on Omarchy. Tongue-in-cheek, not a serious claim.
- Framing Omarchy as making Arch 'the empty box' that gets filled with everything a developer needs; the value is preconfiguration rather than novelty.
- Title asks whether this is 'the year of the Linux desktop' and calls the setup 'ULTIMATE'. The content is a feature tour with little technical depth, which is why quality is capped at 2.

## Tools mentioned
Omarchy, Arch Linux, Hyprland, Wofi, Alacritty, Neovim, LazyVim, LazyGit, LazyDocker, btop, fastfetch, mise, zoxide, fzf, Obsidian, mpv, LibreOffice, OBS, Spotify, 1Password, ChatGPT (as web app), YouTube (as web app), wget, bash
