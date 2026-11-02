# Pake: This CLI Tool Makes 5MB Desktop Apps

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `6bu8zc6lsHQ` · [watch](https://youtu.be/6bu8zc6lsHQ) · **date:** 2026-06-02 · **length:** 4:39 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** dev-tools · **tags:** desktop-apps, electron-alternative, rust, cli, system-webview, tauri, web-app-wrapper, css-injection

> Short demo of Pake, a Rust CLI that wraps any live website as a ~5 MB native desktop app on the system webview. Useful for web apps, but it only handles running URLs and needed a source patch to build.

## Summary
The speaker reviews Pake, a command-line tool that turns a live website into a desktop app using the system webview instead of bundling Chromium as Electron does. He describes its origin (created in 2022 by TW93, who also made the Mac tool Mole), its small custom Rust layer (about 1800 lines on top of Tauri 2), and the options it offers: debug build, frameless title bar, CSS and JS injection, and a system tray icon. He demos wrapping a locally running film-emulation project, which produced a 4.3 MB DMG and a 55 MB app using about 61 MB of RAM, against a 310 MB Electron app (Slack). The main limits he finds are that Pake wraps only running URLs (a closed dev server gives a blank window), and that installation failed on a pnpm version mismatch until he patched the source with Claude Code. He ends by pointing to Electrobun and ZeroNative for apps the user builds themselves.

## Key ideas
- **Pake turns any URL into a native desktop app with one CLI command; the apps are about 5 MB because they use the system web view rather than bundling Chromium like Electron.** — The speaker's pitch is that web apps like YouTube Music, Gmail and Instagram live only in browser tabs, and a standalone app gets its own dock icon and separation. ([0:00](https://youtu.be/6bu8zc6lsHQ?t=0))
- **Pake is a thin layer: the custom Rust code is roughly 1800 lines on top of Tauri 2, covering window management, native menus and JavaScript injection.** — The speaker says the heavy lifting comes from Tauri 2, so the wrapper itself is small. ([1:19](https://youtu.be/6bu8zc6lsHQ?t=79))
- **Demo results: a 4.3 MB DMG, a 55 MB installed app and about 61 MB of RAM, versus a 310 MB Electron app (Slack).** — The build took 5 to 10 minutes. The app did not pick up the icon, but it worked in the dock and played video. ([1:19](https://youtu.be/6bu8zc6lsHQ?t=79))
- **Look and behaviour can be changed without editing the wrapped app's source, using flags for debug devtools, a hidden title bar, CSS/JS injection and a system tray icon.** — Injecting top padding to fix a frameless title bar also added empty space at the bottom of the page to scroll through. ([2:28](https://youtu.be/6bu8zc6lsHQ?t=148))
- **Pake only wraps live URLs. If the local server is stopped, the app shows a blank screen. A 'use local file' option exists, but the speaker only found it after recording.** — The speaker calls it the wrong tool for apps you built yourself, though it worked well for wrapping YouTube Music. ([2:28](https://youtu.be/6bu8zc6lsHQ?t=148))
- **Installation can break on toolchain version skew. Pake was installed with Bun, but its internal build needed pnpm, and the newer pnpm on the machine refused to build, so the speaker patched the source with Claude Code and filed an upstream issue.** — He suggests shipping a compiled binary would avoid this. ([3:49](https://youtu.be/6bu8zc6lsHQ?t=229))
- **For apps you build yourself, the speaker points to Electrobun (a Bun runtime behind a web view) or ZeroNative (a Zig shell that can call C libraries directly).** — His verdict: Pake is the fastest way to wrap a live website, but anything beyond that needs a different tool. ([3:49](https://youtu.be/6bu8zc6lsHQ?t=229))

## Techniques
- **Wrap a live website as a desktop app** — Install Pake through Bun (the speaker used Bun; pnpm or npm is still needed internally). Run the Pake CLI with the target URL and the app name, wait about 5 to 10 minutes for it to fetch the icon and build, then install the DMG it produces by dragging it into Applications. The CLI has few flags, and the speaker says its help output resembles Mole's. *When:* A web app (dashboard, music player, Gmail-style tool) needs its own dock icon and a lighter footprint than Electron. Keep the target server running during the build and while using the app, because the wrapper loads the live URL.
- **Restyle a wrapped site with injected CSS or JS** — Use Pake's inject option to add custom CSS (or JavaScript) to the wrapped page at build time, with no source edits. The speaker used it to add top padding where the frameless title bar overlapped the page. Check the bottom of the page afterwards, because the padding can leave extra scroll space. *When:* The site was not designed for a frameless or native window and needs layout fixes in the wrapper only.
- **Native-app window options** — Use the flags the speaker names: a debug flag to build with devtools, a hide-title-bar flag for a frameless window, and a show-system-tray flag for a tray icon that shows and hides the window. The exact flag spellings are not given in the transcript, so check the CLI help. *When:* You want devtools while debugging the wrapper, a more app-like window, or a tray toggle.
- **Recover from a Pake build failure caused by pnpm version skew** — If the build refuses because the installed pnpm is newer than the version Pake's internal build expects, the speaker's fix was to patch Pake's source (he used Claude Code for this). Pinning the older pnpm version is the obvious alternative, but the speaker did not test it. *When:* Installation fails on a toolchain version mismatch. The speaker suggests an upstream fix such as shipping a compiled binary.

## Numbers
- Pake app size is about 5 MB as a headline claim, and the demo DMG is 4.3 MB, with 55 MB installed app size. ([0:00](https://youtu.be/6bu8zc6lsHQ?t=0))
- Demo app used about 61 MB of memory in Activity Monitor (compared with the Arc browser, which used much more). ([1:19](https://youtu.be/6bu8zc6lsHQ?t=79))
- Pake's custom Rust code is about 1800 lines on top of Tauri 2. ([1:19](https://youtu.be/6bu8zc6lsHQ?t=79))
- The build takes around 5 to 10 minutes. ([1:19](https://youtu.be/6bu8zc6lsHQ?t=79))
- Slack, an Electron app, is about 310 MB. ([2:28](https://youtu.be/6bu8zc6lsHQ?t=148))

## Hot takes
- Pake is the fastest way to wrap a live website, but for apps you build yourself it is the wrong tool, since it wraps URLs and does not bundle local code.
- The speaker says Pake is 'not very well built', citing the pnpm version failure and the need to patch its source.
- A 5 MB app that uses the system web view is a large saving over a 310 MB Electron app, but the saving only holds for sites that work fine in a webview.

## Tools mentioned
Pake, Tauri 2, Electron, Electrobun, ZeroNative, Bun, pnpm, npm, Mole, Claude Code, Rust, Zig, Slack, Arc browser, YouTube Music, Gmail, Instagram, Chrome, Vercel Zero Native

## Relevance to our work
- **general** (1/3): Shows a webview-based wrapper (Pake/Tauri 2) as a lighter alternative to Electron, which could matter if a local dashboard is ever shipped as a desktop app. → *If a local dashboard ever needs a desktop wrapper, compare Pake, Electrobun and Tauri on bundle size and local-file support before choosing Electron.*
