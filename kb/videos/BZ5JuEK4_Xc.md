# Deno Desktop Can Make Your Apps 70% Smaller

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `BZ5JuEK4_Xc` · [watch](https://youtu.be/BZ5JuEK4_Xc) · **date:** 2026-08-02 · **length:** 6:17 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Warren (Better Stack) · **orgs:** Better Stack, Deno, Electron, Apple
- **topics:** dev-tools · **tags:** deno, desktop-apps, electron, typescript, webview, chromium, cef, cross-compilation, supply-chain, dependency-age

> Better Stack walks through Deno 2.9's new `deno desktop` command for building TypeScript desktop apps, comparing it to Electron: a 70 MB binary versus 248 MB, similar startup, with a caveat that the test apps are tiny.

## Summary
Warren from Better Stack introduces Deno 2.9's `deno desktop` command, which packages a TypeScript app as a desktop application without shipping Chromium by default. He builds the same note-taking app in Electron and in Deno to compare. Deno exposes a global `Dino` object for window, tray, dialog and notification APIs, plus a `bind` method for calling from the web view into backend code. Rendering defaults to the OS web view, with a bundled-Chromium option via CEF. Packaging is driven by flags or a `dino.json` file, and Windows and Linux installers are built in pure Rust so they can be cross-built from any host. On the test app, the Deno binary is 70 MB versus 248 MB for Electron, and startup times are nearly identical (375 ms vs 364 ms). Warren notes that the Deno benchmarks are its own and that the apps are too small to show how results scale. He calls the project experimental but says it is already enough to start building real apps.

## Key ideas
- **Deno 2.9 adds a `deno desktop` command that turns a TypeScript entry file into a desktop app, and it auto-detects frameworks such as Next.js and Remix in the current directory.** — No separate scaffold is needed. The speaker says it works with a hello-world file, and that framework projects are picked up automatically. The command is new in 2.9. ([0:00](https://youtu.be/BZ5JuEK4_Xc?t=0))
- **The global `Dino` object gives desktop APIs (window control, tray, native alerts), and `bind` provides a simpler backend call path than Electron's IPC.** — The speaker says Electron's IPC needs three steps and Deno's `bind` is a simpler alternative. His note app calls a binding on create and saves the note to disk from the backend. ([1:10](https://youtu.be/BZ5JuEK4_Xc?t=70))
- **Deno's default renderer is the OS web view, which is why it ships smaller than Electron. Bundling Chromium through CEF is an opt-in trade-off for identical rendering.** — The default uses WebView2 on Windows and WebKit on macOS and Linux. The CEF option brings consistent rendering across OSes at the cost of more bloat. Electron ships about 180 MB of Chromium before any app code. ([2:35](https://youtu.be/BZ5JuEK4_Xc?t=155))
- **Packaging is handled by a flag or a `dino.json` file, and any host can build the Windows and Linux installers.** — Installers are authored in pure Rust, so cross-building (for example, Windows from a Mac) does not need platform tooling. An all-targets flag builds every supported platform. ([2:35](https://youtu.be/BZ5JuEK4_Xc?t=155))
- **On the identical note app, the Deno binary is about 70 MB versus 248 MB for Electron, and startup is essentially the same.** — Warren averaged several launches: Deno 375 ms, Electron 364 ms. He says the results may diverge as apps grow, and that the Deno 2.9 performance numbers (about 2x faster cold start, up to 3.1x less memory on JSON POST) come from Deno's own benchmarks. ([3:48](https://youtu.be/BZ5JuEK4_Xc?t=228))
- **Production features come built in: auto-update, error reporting, system menus, trays, dialogs and notifications. The project still labels itself experimental and lacks Electron's feature depth.** — The speaker's judgment is that this is enough to start building real applications. He also mentions CSS module imports in 2.9 and a single `dino install` command that migrates a project away from npm, pnpm, yarn and bun. ([4:40](https://youtu.be/BZ5JuEK4_Xc?t=280))
- **A minimum dependency age is on by default in response to recent supply-chain incidents. Dependencies must be older than the set threshold (his example is 72 hours) before they can be installed.** — The setting can be disabled by setting the min release age to zero. This is a dependency-hygiene default that is independent of the desktop features. ([5:36](https://youtu.be/BZ5JuEK4_Xc?t=336))

## Techniques
- **Build a desktop app from one TypeScript file** — Run `deno desktop` and point it at a TypeScript entry file. Deno auto-detects the framework if the directory holds Next.js, Remix or a similar project. For live development, append the HMR flag (the flag name is not spoken in the video) to get hot reload. *When:* Starting a desktop wrapper for an existing web frontend, or prototyping a small local tool, when you want to avoid Electron's bundled Chromium.
- **Call backend code from the web view with `bind`** — Register a binding on the Deno backend and call it from the front end when the UI event fires (the speaker's example: create note). The backend then writes to disk. The speaker contrasts this with Electron's three-step IPC bridge. *When:* A web-view UI needs filesystem or other privileged work done in the backend without the Electron IPC setup.
- **Choose the renderer per build** — Default: the OS web view (WebView2 on Windows, WebKit on macOS and Linux). For identical rendering on every OS, pass the `backend` flag with the value `CEF` to bundle Chromium through the Chromium Embedded Framework. Expect a larger binary. *When:* Use the default for small size and native look. Use CEF when visual consistency across operating systems matters more than size.
- **Package for one or several platforms with flags or dino.json** — Pass the `output` flag with the target type: app and DMG on macOS, EXE or MSI on Windows, AppImage, DEB or RPM on Linux. Use the all-targets flag to build every platform. Cross-building (for example, Windows from macOS) works because the installers are written in pure Rust. Put the same settings in a `dino.json` file: app name and identifier, output targets, release URL and error-reporting URL. *When:* Shipping a desktop build from CI or a laptop without per-OS toolchains, or when the number of CLI flags gets unwieldy.
- **Keep the default dependency age guard** — Dino enables a minimum dependency age by default (72 hours in the speaker's example), so freshly published packages cannot be installed. To opt out, set the min release age to zero in the Deno config. The speaker does not show the exact config key. *When:* Projects that install a lot of packages automatically, where a supply-chain attack on a brand-new release would be costly. Keep the default unless you need the newest package versions immediately.

## Numbers
- Electron ships about 180 MB of Chromium before any app code is written. ([1:10](https://youtu.be/BZ5JuEK4_Xc?t=70))
- Deno 2.9 vs 2.8 (Deno's internal benchmarks): about 2x faster cold starts, and up to 3.1x less memory when executing POST requests that respond with JSON. ([3:48](https://youtu.be/BZ5JuEK4_Xc?t=228))
- Identical note-taking app binary size: Deno 70 MB vs Electron 248 MB. ([3:48](https://youtu.be/BZ5JuEK4_Xc?t=228))
- Average startup over several launches: Deno 375 ms vs Electron 364 ms (tiny apps, so the speaker warns results may diverge at scale). ([3:48](https://youtu.be/BZ5JuEK4_Xc?t=228))
- Default minimum dependency age is enforced in the example as 72 hours, and can be set to zero to disable it. ([5:36](https://youtu.be/BZ5JuEK4_Xc?t=336))

## Hot takes
- Deno Desktop is already good enough to build real apps even though Deno still calls it experimental.
- Most of Electron's size gap comes from its bundled Chromium, and Deno's default of using the OS web view is the main reason for the difference.
- The startup-time parity result says little about real apps: the test apps are tiny and the speaker says results may change as they grow.
- The 2.9 performance numbers are Deno's own internal benchmarks, not independent tests.

## Tools mentioned
Deno 2.9, deno desktop, Dino (global runtime object), Electron, Chromium, CEF (Chromium Embedded Framework), WebView2, WebKit, Next.js, Remix, dino.json, npm, pnpm, yarn, bun, CSS module imports, dino install

## Relevance to our work
- **prosharness** (1/3): ProsHarness has phone-driven approvals and could eventually need a desktop control panel. The dependency-age default is the one part that could apply now. → *Check whether ProsHarness's own npm/bun installs should set a minimum release age (72 hours was the example), as a guard against freshly published malicious packages.*
