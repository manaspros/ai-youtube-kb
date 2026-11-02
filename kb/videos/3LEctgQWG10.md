# Superfile - AMAZING Terminal File Manager Created by a High School Kid

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `3LEctgQWG10` · [watch](https://youtu.be/3LEctgQWG10) · **date:** 2025-11-02 · **length:** 4:46 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** dev-tools · **tags:** terminal-file-manager, tui, superfile, vim-keybindings, neovim, nerd-fonts, homebrew, toml-config, linux-cli, macos

> Short walkthrough of Superfile, a customizable Vim-keybinding terminal file manager, covering navigation, copy/move/delete, pinning, and TOML config for themes, editor and hotkeys.

## Summary
Better Stack presents Superfile (launched with the spf command), a terminal file manager with a file preview pane, Vim-style navigation, and heavy customization. The presenter walks through navigating folders with h/j/k/l or arrow keys, toggling the preview with f, searching with a forward slash, and switching the sidebar, process and metadata panels. He covers the select-then-yank, paste, cut and delete workflow, multiple panels, pinning folders with Shift+P, and creating files and folders with A. The customization section shows how to locate the config files, change the theme in config.toml, set Neovim as the editor, and remap keys in hotkeys.toml, where each key can be an array of bindings. He ends by noting rough edges: pixelated image previews, occasional crashes, and a project under a year old at recording time. The video is a feature tour with no benchmarks, and the presenter has changed the default hotkeys to Vim-style, so his keys differ from the defaults.

## Key ideas
- **Superfile is a terminal file manager pitched as a faster alternative to Finder and cd for moving around the filesystem.** — Launch it with `spf` in the terminal. It needs a Nerd Font for icons. The presenter installs it with Homebrew on a Mac but notes there are other install methods. ([0:00](https://youtu.be/3LEctgQWG10?t=0))
- **Navigation uses Vim-style keys, with the arrow keys also working.** — h/j/k/l move around, l or right enters a folder, h or left goes to the parent. A preview pane shows folder contents, which the presenter says works well for code. f hides the preview, ctrl+f or shift+f toggles the footer, / searches, and ctrl+s or s, ctrl+p or p, and ctrl+d or m open the sidebar, process and metadata panels. ([0:00](https://youtu.be/3LEctgQWG10?t=0))
- **Copy, cut, paste and delete follow a select-then-act model.** — v switches from browse mode to select mode. Shift plus up/down selects a range. y or ctrl+c yanks to the clipboard, p pastes, x cuts, and d deletes after a confirmation prompt. The presenter says Superfile logs the paste operation. ([1:25](https://youtu.be/3LEctgQWG10?t=85))
- **Sorting, hidden files and panels are single-key toggles.** — o opens sort options (name, size, and so on), Shift+R reverses the order, and . shows hidden files. n creates a new panel and Tab or Shift+Tab switches between panels. The presenter says he rarely uses panels. ([1:25](https://youtu.be/3LEctgQWG10?t=85))
- **Folders can be pinned to the sidebar, and file or folder creation is a single key.** — Shift+P pins or unpins the current folder. a creates a file, and a folder is created by typing a name followed by a trailing slash, which also allows creating a folder and a file in one go. ([2:48](https://youtu.be/3LEctgQWG10?t=168))
- **Most behaviour is configured through TOML files rather than a settings UI.** — After exiting with ctrl+c, `spf pl` (the presenter types it with a space, most likely the -pl flag) lists the Superfile config and directories. config.toml sets the theme, which is picked from a themes folder, and the editor. The example switches the theme from Tokyo Night to Blood, and the presenter reverts it afterwards. ([2:48](https://youtu.be/3LEctgQWG10?t=168))
- **Editor integration lets Superfile hand files off to Neovim and return.** — With Neovim set as the editor, e opens the selected file in it, and quitting Neovim returns straight to Superfile. Shift+E opens the whole current directory in the editor. ([2:48](https://youtu.be/3LEctgQWG10?t=168))
- **Hotkeys are remappable, and each key can be bound to multiple inputs.** — Keys are set in hotkeys.toml, and each binding accepts an array so several keys can trigger the same action. The presenter changed the defaults to Vim-style mappings, so his keys differ from the shipped defaults. ([4:12](https://youtu.be/3LEctgQWG10?t=252))
- **The presenter flags current limitations: image previews are pixelated, there are occasional crashes, and the project is under a year old.** — He expects improvement over time and points to the project website for more detail. He gives no benchmarks or comparisons with other file managers such as ranger, yazi or nnn. ([4:12](https://youtu.be/3LEctgQWG10?t=252))

## Techniques
- **Install and launch Superfile** — On macOS, install with Homebrew (the exact formula name is not shown). Install a Nerd Font for icons. Start the app by typing `spf` in the terminal. Other platforms are mentioned but not shown. *When:* When you want a keyboard-driven file browser inside the terminal instead of Finder or repeated cd.
- **Vim-style navigation and preview** — Use h/j/k/l or arrows to move. Use l to enter a folder and h to go to the parent. Use f to toggle the preview pane and / to search, then Enter. Use . to show hidden files. *When:* Browsing code or project trees where a preview of folder contents helps.
- **Select, yank, paste** — Press v to enter select mode. Hold Shift with up/down to select a range. Press y (or ctrl+c) to yank, navigate to the destination, then press p to paste. For a move, use x instead of y, then p. *When:* Batch copying or moving files between folders without a mouse.
- **Pin frequently used folders** — Navigate to the folder and press Shift+P to pin it to the sidebar. Press Shift+P again on a pinned folder to unpin it. *When:* Keeping a few working directories one keypress away.
- **Locate and edit the config** — Quit with ctrl+c, then run `spf pl` (as typed in the video, most likely the -pl flag) to list the Superfile config directory. Edit config.toml to change theme (themes come from a themes folder) and set the editor. Restart Superfile to apply. *When:* Changing the theme, or wiring Superfile to your own editor.
- **Editor handoff** — With an editor set in config.toml (Neovim in the demo), press e on a file to open it in the editor, then quit the editor to return to Superfile. Press Shift+E to open the current directory in the editor. *When:* Jumping from file browsing straight into editing without leaving the file manager.
- **Remap hotkeys** — Edit hotkeys.toml. Each action takes an array of keys, so add extra keys to an action by adding entries to its array. The presenter re-mapped the defaults to Vim keys. *When:* Matching the file manager to your existing editor or Vim muscle memory.

## Numbers
- Video length is 4:46. ([0:00](https://youtu.be/3LEctgQWG10?t=0))
- The Superfile project was less than a year old at recording time. ([4:12](https://youtu.be/3LEctgQWG10?t=252))
- The presenter says the Superfile author was a 16-year-old Taiwanese student. ([0:00](https://youtu.be/3LEctgQWG10?t=0))

## Hot takes
- The title hook (AMAZING, made by a high school kid) is more emphasis than substance, but the walkthrough itself is practical and has no sponsor segment.
- The presenter's remapped Vim hotkeys mean viewers following along must check their own hotkeys.toml, since the on-screen keys will not match the defaults.
- The claim that Superfile beats Finder and cd for navigation is asserted, not compared, and no alternatives are mentioned.

## Tools mentioned
Superfile (spf), Neovim, Homebrew, Nerd Fonts, Finder (named as the comparison), Tokyo Night theme, Blood theme

## Relevance to our work
- **general** (1/3): Could be a handy terminal file browser alongside coding-agent sessions, with no direct link to what we build. → *Optionally install Superfile on the dev machine, set Vim keys in hotkeys.toml, and use it to browse the repo while agents run.*
