# Vercel Just Killed Electron With Zig

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `GXNjnu7UqFs` · [watch](https://youtu.be/GXNjnu7UqFs) · **date:** 2026-06-02 · **length:** 4:38 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Bun, Vercel (in title only, never spoken)
- **topics:** dev-tools, vibe-coding-app-building · **tags:** zig, zero-native, desktop-apps, webview, electron-alternative, electrobun, bun, vite, react, json-bridge, app-packaging

> Walkthrough of zero-native, a thin Zig shell that hosts a system WebView for small desktop apps, covering setup, dev loop, 2.9 MB packaging, Electrobun comparison and limits.

## Summary
The speaker demos zero-native (auto-captioned as XeroNative/ZeroNative), a Zig-based native app builder that renders a frontend in the OS system WebView (or bundles Chromium) and talks to native APIs over a JSON bridge. Setup is Zig plus the zero-native CLI, then `zero native init` scaffolds a project with a React/Svelte/Vue/Next/Vite frontend option. The dev server hot-updates the native window, and `zig build package` produced a 2.9 MB package. The speaker argues the design is thinner than Electrobun because a Zig binary alone talks to OS APIs and C libraries, with no Bun runtime. Limits he hits: app.zon cannot set title bar style or custom menus, macOS packaging failed on his first try, and system tray, code signing and mobile were not covered. The video is a short overview with no benchmarks beyond the one package size, and it never mentions Vercel despite the title.

## Key ideas
- **zero-native is a thin Zig shell that hosts a WebView; the frontend (any JS framework) talks to the Zig layer over a JSON bridge, which is how it reaches OS-level APIs.** — Can use the system web view or bundle full Chromium like Electron. Pitched for tiny binaries and near-instant rebuilds. ([0:00](https://youtu.be/GXNjnu7UqFs?t=0))
- **The Zig requirement is the main adoption risk for JS developers, though the speaker argues Zig is readable enough to pick up.** — Speaker notes Zig has no borrow checker or lifetimes and can call C directly with no glue code. He floats learning Zig on camera as a possible follow-up. ([0:00](https://youtu.be/GXNjnu7UqFs?t=0))
- **Setup is a short CLI flow: install Zig, install zero-native, scaffold a project, then run it.** — Scaffold output has app.zon, assets/, build.zig, the JS bridge and web engine, and a frontend/ directory. Running the build opens a native window. ([1:06](https://youtu.be/GXNjnu7UqFs?t=66))
- **For an existing JS project, the recommended route is to start from a minimal Vite app and replace the frontend directory contents.** — The Zig shell is kept as-is. The speaker presents this as the cleanest way to add zero-native to code that already exists. ([1:06](https://youtu.be/GXNjnu7UqFs?t=66))
- **The dev server owns the frontend lifecycle, and edits show up in the native window in real time.** — Run `zig build dev` for the loop and `zig build package` to produce a distributable build. ([2:21](https://youtu.be/GXNjnu7UqFs?t=141))
- **app.zon controls app identity and window setup: icon name, project name, web engine and window size.** — This is also where the speaker expects to change the engine or window config. Per his later remarks, title bar style and custom menu items are not configurable there yet. ([2:21](https://youtu.be/GXNjnu7UqFs?t=141))
- **Versus Electrobun, zero-native drops the JavaScript runtime from the native path: a Zig binary alone calls OS APIs and C libraries.** — In Electrobun the TypeScript main process runs in a Bun WebWorker and reaches native APIs through Bun FFI, which goes through C++ and Objective-C layers. The speaker calls zero-native the thinner shell. ([2:21](https://youtu.be/GXNjnu7UqFs?t=141))
- **The speaker's caveats: a bit of Zig or config editing is required, the feature set is smaller than Electrobun's, and the macOS package step failed on his first try.** — He suggests the open-source code can be extended with Claude. System tray, code signing and embedded iOS/Android apps were not covered in the demo. ([3:48](https://youtu.be/GXNjnu7UqFs?t=228))

## Techniques
- **Scaffold a zero-native app** — Install Zig (speaker used mise, Homebrew also works), install zero-native, then run `zero native init <project-name>` with a frontend flag set to React (spoken as `--frontend react`; the speaker names Svelte, Vue, Next and plain Vite as alternatives). Then run `zig build run` to install dependencies and open the window. *When:* Starting a new desktop app with a web UI that should ship as a small binary instead of Electron.
- **Dev loop and packaging** — `zig build dev` starts the zero-native dev server, which hot-updates the native window on frontend edits. `zig build package` builds the distributable, which the speaker found in zig-out/package at 2.9 MB. *When:* Iterating on a zero-native app and producing a distributable build.
- **Add zero-native to an existing JS project** — Start from a minimal Vite app, then replace the contents of the frontend directory with the existing app code and keep the Zig shell files (build.zig, app.zon, the JS bridge and web engine). *When:* Wrapping an existing web frontend in a native shell without rewriting it.
- **Configure the app via app.zon** — Edit app.zon to set the icon name, project name, web engine and window size. Title bar style and custom menu items are not supported there yet, per the speaker. *When:* Changing app identity, engine or window dimensions after scaffolding.
- **Call native or C code from the frontend** — The frontend sends JSON messages across the bridge to the Zig layer, which can call OS APIs or C libraries directly through a simple C import. The speaker did not show the code. *When:* Needing OS-level APIs (system tray, file dialogs and similar) from web UI code, without a Bun or Node runtime.

## Numbers
- zig-out/package build is 2.9 MB; speaker says some users have got it under 1 MB ([2:21](https://youtu.be/GXNjnu7UqFs?t=141))
- Speaker says the Bun team is moving from Zig to Rust (unverified, aside) ([0:00](https://youtu.be/GXNjnu7UqFs?t=0))

## Hot takes
- Title says Vercel killed Electron, but the speaker never mentions Vercel and does not show the claim; the framing is hype, so quality is capped at 2.
- Speaker calls zero-native a thinner native shell than Electrobun, but also says it is less feature-rich, with fewer configurable options and a flaky first macOS package build.
- The speaker suggests the open-source code can be extended by handing it to Claude; not tested in the video.
- Auto-captions garble the project name (XeroNative, ZeroNative, zero native); the notes use zero-native.

## Tools mentioned
zero-native (CLI and build via zig build), Zig, mise, Homebrew, Vite, React, Svelte, Vue, Next.js, Electron, Electrobun, Bun, Chromium, Claude
