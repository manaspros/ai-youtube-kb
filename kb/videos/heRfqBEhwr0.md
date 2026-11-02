# The BEST Terminal Just Launched - Ghostty 👻

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `heRfqBEhwr0` · [watch](https://youtu.be/heRfqBEhwr0) · **date:** 2025-11-02 · **length:** 6:02 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed Better Stack host · **orgs:** Better Stack, Ghostty, HashiCorp, iTerm2, Warp
- **topics:** dev-tools · **tags:** terminal emulator, ghostty, zig, theming, nerd fonts, kitty graphics protocol, quick terminal, terminal inspector, libghostty, macos, linux

> Better Stack walkthrough of Ghostty 1.0, a fast native terminal emulator; covers theme and font setup, native macOS features, quick terminal, and its standards-first approach. Mostly a feature tour with little depth.

## Summary
The host introduces Ghostty as a newly available version 1 terminal emulator, written mainly in Zig by Mitchell Hashimoto, that supports macOS and Linux and aims for zero configuration with sensible defaults. He changes the theme, which Ghostty ships with iTerm2 color schemes that can be previewed from the CLI. He notes the built-in JetBrains Mono font with ligatures, Metal rendering on macOS and OpenGL on Linux. The video then highlights native UI behavior on macOS (native tabs and splits, a global-hotkey quick terminal, secure keyboard entry, Quick Look, a proxy icon) and rendering features (Kitty graphics protocol and a Doomfire benchmark near 480 FPS). It closes with the Terminal Inspector, which is experimental and read-only, and LibGhostty, the core library that is not yet a stable public API. The piece is a feature tour with little engineering depth, and it adds no evidence beyond the presenter's own impressions.

## Key ideas
- **Ghostty 1.0 is presented as widely available, a fast, feature-rich, native terminal written mostly in Zig, with zero-config defaults.** — Installs like a normal macOS app; the presenter says it feels fast compared with other terminals he has used. Supports macOS and Linux (install methods are in the docs). ([0:00](https://youtu.be/heRfqBEhwr0?t=0))
- **Themes come built in, drawn from the iTerm2 color scheme collection, and can be previewed from the CLI.** — Running `ghostty +list-themes` (transcript says 'Ghosty plus list-themes') lets you scroll through them. Pick one, add it to the config file, then reload with cmd+shift+comma. ([1:06](https://youtu.be/heRfqBEhwr0?t=66))
- **Font support is built in: a bundled Nerd Font set includes JetBrains Mono, with configurable ligatures.** — The presenter says it uses Metal directly on macOS and has a ligature-capable Metal renderer, which only iTerm also has. Linux uses OpenGL. ([1:06](https://youtu.be/heRfqBEhwr0?t=66))
- **The app uses native macOS components for tabs, splits and system features, which the presenter credits for its smoothness.** — Features: secure keyboard entry (padlock at password prompts), Force Touch Quick Look, and a proxy icon in the title bar for dragging the session file path. ([2:32](https://youtu.be/heRfqBEhwr0?t=152))
- **A quick (top-down or Quake-style) terminal bound to a global keybinding is the standout workflow feature.** — It is reachable even when the app is not focused, useful for launching a Docker container without context switching. ([2:32](https://youtu.be/heRfqBEhwr0?t=152))
- **Rendering speed comes from the Kitty graphics protocol, and the presenter cites a Doomfire benchmark of about 480 FPS on his MacBook Pro.** — Per the presenter, Mitchell Hashimoto ranks it second among the terminals he tested, behind Alacritty; the gap is a deliberate trade-off to save memory. ([3:49](https://youtu.be/heRfqBEhwr0?t=229))
- **Feature behavior follows a stated precedence: formal standards first, then XTerm, then other popular terminals.** — The goal is compatibility with legacy apps while still supporting modern features for new ones. ([3:49](https://youtu.be/heRfqBEhwr0?t=229))
- **The Terminal Inspector is a per-terminal, live-updating panel similar to a web inspector. It is experimental and read-only, with read-write planned.** — Targets terminal developers who need to see terminal state while building. ([4:52](https://youtu.be/heRfqBEhwr0?t=292))
- **LibGhostty, the cross-platform core library behind Ghostty, is not yet stable or a public API, but the plan is to release it as a standalone library and expand to WebAssembly.** — The presenter frames this as a way for other developers to get standards-compliant terminal emulation for free. ([4:52](https://youtu.be/heRfqBEhwr0?t=292))

## Techniques
- **Switch theme via the Ghostty CLI** — Run `ghostty +list-themes` to preview the bundled iTerm2-derived themes. Add the chosen theme to the config file, then reload it with cmd+shift+comma. The presenter uses Catppuccin, which the captions render as 'Capuchin'. Only the theme is changed; the rest stays at defaults. *When:* Customizing the look without writing a custom color scheme.
- **Global quick terminal** — Bind the quick terminal (top-down or Quake-style) to a global keybinding so it works while another app has focus. The config key is not named in the video. *When:* Running a one-off command such as launching a Docker container while staying in your current app.
- **Use bundled font with ligatures** — Use the bundled JetBrains Mono (Nerd Font variant), which is the default, and turn on the configurable ligature support in the config. Config key names are not shown. *When:* You want programming ligatures without installing fonts separately.

## Numbers
- Doomfire benchmark at about 480 FPS on the presenter's MacBook Pro; Ghostty ranks second behind Alacritty per Mitchell Hashimoto, with the gap attributed to a memory trade-off. ([3:49](https://youtu.be/heRfqBEhwr0?t=229))
- Ghostty 1.0 (version 1) became widely available; the video runs 6:02. ([0:00](https://youtu.be/heRfqBEhwr0?t=0))

## Hot takes
- The title ('The BEST Terminal Just Launched') is hype, and the content is a feature tour with limited technical depth; quality is capped at 2 on that basis.
- The performance ranking and the Mitchell Hashimoto comparison are the presenter's secondhand account, with no independent benchmark shown.
- The presenter calls the Mac terminal experience 'what the default Mac terminal should be' and recommends trying it, which is opinion, not evidence.
- Auto-caption errors were fixed in the notes: 'Ghosty' to Ghostty, 'Capuchin' to Catppuccin, 'Westerm' to WezTerm.

## Tools mentioned
Ghostty (version 1), Zig, Metal, OpenGL, iTerm2 color schemes, JetBrains Mono, Nerd Fonts, Oh My Zsh, tmux, Kitty graphics protocol, Alacritty, Warp, Terraform, Docker, LibGhostty, Catppuccin (theme named in the video; the captions render it as 'Capuchin')
