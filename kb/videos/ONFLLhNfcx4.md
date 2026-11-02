# Electrobun: No Node, No Chromium, Just Pure Bun Performance

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ONFLLhNfcx4` · [watch](https://youtu.be/ONFLLhNfcx4) · **date:** 2026-04-02 · **length:** 5:49 · **format:** tutorial · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, Anthropic, Blackboard
- **topics:** dev-tools · **tags:** electrobun, bun, desktop-apps, electron-alternative, native-webview, cross-platform, typescript

> A 6-minute Better Stack walkthrough of Electrobun, a Bun-based desktop app framework that uses OS-native webviews instead of Chromium, with a from-scratch React example and an honest list of its rough edges.

## Summary
The video introduces Electrobun, a cross-platform desktop app framework built on Bun that uses no Node.js or V8, needs no Rust, and renders through each OS's native webview rather than bundled Chromium. The presenter builds a small Bun React app into a native Mac app, covering the config file, the entry point, and the views setup needed because Bun moves build output to a different directory. A production build of the example produced a 17 MB DMG and a 65 MB app, against roughly 271 MB for a Hello World Electron app. The presenter notes cross-platform caveats from the native webviews (WebKit, Edge WebView2, WebKitGTK) and an optional Chromium Embedded Framework mode that restores consistency at a size and performance cost. Other features mentioned are out-of-process iframes, typed RPC, ZSTD compression, a self-extracting wrapper, and code signing. The presenter reports missing docs around the entry file, a page flash on full reloads, and inspector use disturbing the layout, and frames Electrobun as the closest thing to a Bun-based Electron alternative after Bun's acquisition by Anthropic. The framework is very new (first commit in February 2026, per the video).

## Key ideas
- **Electrobun is a desktop app framework on Bun with no Node.js, no V8 and no Rust, and it renders through OS-native webviews.** — Positioned as an Electron-style alternative built on Bun's own C++ wrappers. The presenter says the Bun team's acquisition by Anthropic makes a Bun-native Electron less likely, so Electrobun is the closest option. ([0:00](https://youtu.be/ONFLLhNfcx4?t=0))
- **Native webviews make bundles much smaller than Electron, but the cross-platform behavior has to be handled per platform.** — Mac uses WebKit, Windows uses Edge WebView2, and Linux uses WebKitGTK. Features those webviews lack must be considered when building cross-platform apps. ([3:19](https://youtu.be/ONFLLhNfcx4?t=199))
- **Chromium Embedded Framework is available as an option for consistent rendering across platforms.** — The presenter says it brings back size and performance costs close to Electron's, which removes much of the reason to choose Electrobun. ([3:19](https://youtu.be/ONFLLhNfcx4?t=199))
- **Bun's build step moves output files, so the entry point must reference the built views rather than the source paths.** — A blank window results when the entry point points at the wrong location after bun builds and tree-shakes the app. The fix is to declare a views object in the Electrobun config and reference the built view from the entry point. ([2:03](https://youtu.be/ONFLLhNfcx4?t=123))
- **Other built-in features include out-of-process iframes, typed RPC, ZSTD compression, a self-extracting wrapper and code signing.** — The presenter lists these but does not demonstrate them. ([4:25](https://youtu.be/ONFLLhNfcx4?t=265))
- **The presenter found rough edges: thin docs around the entry file, a page flash on full reloads, and inspector use that disturbs the layout.** — The first commit dates to February 2026, so the presenter expects these to be fixed over time. The presenter's judgment is that Electrobun is currently the best available bet for a Bun-powered cross-platform desktop app. ([4:25](https://youtu.be/ONFLLhNfcx4?t=265))
- **The example project is small, and the size difference is the headline result.** — A production build gave a 17 MB DMG and a 65 MB .app. A Hello World Electron app measured 271 MB, which the presenter calls more than four times larger. ([3:19](https://youtu.be/ONFLLhNfcx4?t=199))
- **Electrobun ships with templates such as a note-taking app, a multi-window app and a tray app, and any JS framework can be used.** — The presenter names Svelte, Vue, SolidJS and Angular as options, then builds a Bun React app from scratch. ([0:42](https://youtu.be/ONFLLhNfcx4?t=42))

## Techniques
- **Scaffold from an Electrobun template** — Run the Electrobun init and pick a template (basic note-taking app, multi-window app, or tray app that opens docs in the browser). Any JS framework works in the webview. *When:* Starting a new desktop app to learn the structure before adding your own UI.
- **Config file, entry point and views for a Bun app** — In the project root, create the Electrobun configuration file with the app name, identifier and a Bun build entry point. Add a bun folder under src with an index.ts that instantiates the browser window class with a title and a URL. Add a `views` object to the config with a view named `main` whose entry point is `index.html` (which loads the bundled frontend JS and CSS). In index.ts, point the window URL at the built views/main location, not the source path. *When:* Fixing the blank-window problem that appears after bun build moves and tree-shakes output files.
- **Window chrome and menu tweaks** — Set a window property to hide the title bar for a more app-like feel. Use the application menu object to define a custom menu. The presenter does not show the exact property name in the video. *When:* Polishing a desktop app beyond a bare webview window.
- **Scripted dev and production builds** — The example project uses a dev-build script and a build script. `bun start` runs the app. The production build outputs a DMG and an app bundle. *When:* Running the app locally during development and packaging it for distribution.

## Numbers
- Electrobun production build: 17 MB DMG and 65 MB app. ([3:19](https://youtu.be/ONFLLhNfcx4?t=199))
- Hello World Electron app: 271 MB, more than 4x the Electrobun app size. ([3:19](https://youtu.be/ONFLLhNfcx4?t=199))
- Electrobun's first commit dates to February (2026, per the video date); the presenter says there may be more commits before that. ([4:25](https://youtu.be/ONFLLhNfcx4?t=265))
- Video length is 5:49. ([0:00](https://youtu.be/ONFLLhNfcx4?t=0))

## Hot takes
- Electrobun is the closest thing to a Bun-based Electron alternative, and it is the best option for a Bun desktop app right now (presenter's opinion).
- The Bun team's acquisition by Anthropic has pushed Bun toward CLI and executable work and away from desktop frameworks (presenter's claim, not verified in the video).
- Electrobun needs no Rust, unlike Tauri (the transcript reads 'Towery'; Tauri is the likely name).
- Electrobun's bundles are far smaller than Electron's, but its advantage shrinks if Chromium Embedded Framework is enabled.

## Tools mentioned
Electrobun, Bun, React, Electron, Tauri (transcribed as 'Towery'), Chromium Embedded Framework, WebKit, Edge WebView2, WebKitGTK, Svelte, Vue, SolidJS, Angular, ZSTD, Qwen, WebGPU, Colab (a hybrid browser, terminal and code editor app built by a Blackboard developer)
