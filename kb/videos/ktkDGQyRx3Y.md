# Tauri vs Electrobun vs Deno Desktop: One Clear Winner

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ktkDGQyRx3Y` · [watch](https://youtu.be/ktkDGQyRx3Y) · **date:** 2026-08-02 · **length:** 6:33 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Warren · **orgs:** Better Stack, Bun, Deno, Tauri
- **topics:** dev-tools · **tags:** desktop-apps, cross-platform, tauri, electron, electrobun, deno-desktop, benchmarks, screen-recording, memory-footprint, startup-time

> Better Stack builds the same screen-recorder app in Tauri, Electrobun, Deno Desktop and Electron and measures size, startup, memory and developer experience; Tauri wins on size and recording, Electron is the mature TypeScript option.

## Summary
Warren from Better Stack builds one screen-recording and timeline-export app four times, once each in Tauri (Rust), Electrobun (Bun), Deno Desktop and Electron as a baseline, and compares bundle size, startup time, memory and developer experience. Tauri is by far the smallest on disk (about 57 MB against 323 MB for Electron), because it records through the native macOS ScreenCaptureKit API from the Rust backend rather than the web view. Electrobun is the largest because its screen capture path forces it to ship Chromium. Startup is not won by Tauri: Deno Desktop was fastest at about 242 ms, and Electrobun was nearly three times Electron because it boots three runtimes in a chain. Memory after launch is roughly even between Tauri and Deno, and Electrobun is about double, but the Tauri figure is only correct if you sum the system web view processes that Activity Monitor does not show as children. The developer-experience section reports that Deno Desktop quit the whole app when the last window was hidden. The verdict is Tauri for most people, Electron for TypeScript-only teams, and a caution that Deno Desktop and Electrobun are not yet mature. This is a single-author, single-app benchmark, so the numbers are indicative, not general.

## Key ideas
- **Bundle size differs by roughly 7x: Tauri about 57 MB, Deno Desktop about 111 MB, Electron 323 MB, Electrobun 418 MB. FFmpeg alone adds about 45 MB to each app.** — All four apps had identical functionality and embedded FFmpeg for MP4 export. Electrobun's extra size comes from bundling Chromium, which it needs for screen capture. ([1:28](https://youtu.be/ktkDGQyRx3Y?t=88))
- **Where the screen capture lives decides the bundle size. Tauri records in the Rust backend through macOS ScreenCaptureKit and the web view only renders UI, while JavaScript-driven apps route frames through the web view.** — Tauri's backend takes a display, a codec and a file path and writes the MP4 itself, mixing mic and system audio, so the web view never touches a frame. Electron and Deno use getDisplayMedia plus MediaRecorder. Electrobun lacks that API, so it reintroduces Chromium (about 200 MB more). ([1:28](https://youtu.be/ktkDGQyRx3Y?t=88))
- **Startup time is not where Tauri wins. Deno Desktop starts fastest, and Electrobun is an outlier because it chains a launcher, Bun and Chromium.** — Median of 10 runs: Deno about 242 ms, Electron 273 ms (baseline), Tauri about 311 ms, Electrobun about 773 ms. The speaker attributes Tauri's slight lag to the system web view engine still having to boot. ([2:55](https://youtu.be/ktkDGQyRx3Y?t=175))
- **Memory after launch is closest between Tauri (about 109 MB) and Deno (about 98 MB), with Electron at 128 MB and Electrobun at 208 MB.** — The speaker says Tauri's on-disk advantage does not carry over to runtime memory the way the marketing implies (about 10x). ([4:09](https://youtu.be/ktkDGQyRx3Y?t=249))
- **Activity Monitor undercounts Tauri because macOS starts its system web view processes as separate processes, not children of the app. Sum them to compare fairly.** — Activity Monitor shows Tauri at about 36 MB, which looks like a 3x win over Electron. Adding the web view processes brings it to about 109 MB, the figure recorded in the test. ([4:09](https://youtu.be/ktkDGQyRx3Y?t=249))
- **During recording, Tauri was noticeably smoother. The speaker attributes this to native capture: frames never cross a JavaScript bridge.** — Tauri is the choice if you need something close to 60 fps in the recording pipeline. ([4:09](https://youtu.be/ktkDGQyRx3Y?t=249))
- **Deno Desktop terminates the entire app when the last visible window is hidden, which broke a recording-then-hide flow.** — The speaker's guess is that Deno treats 'no visible screens' as 'application finished'. The workaround was to move the window off-screen instead of hiding it. ([4:09](https://youtu.be/ktkDGQyRx3Y?t=249))
- **Verdict: Tauri for most projects if Rust is acceptable, Electron for TypeScript-only teams because it is the mature platform, Deno Desktop still maturing, and Electrobun rated the worst of the four.** — The speaker explicitly frames this as a judgment for the viewer to make based on team skills and product type. ([5:37](https://youtu.be/ktkDGQyRx3Y?t=337))

## Techniques
- **Measure startup as a median over repeated launches** — A script launches each app 10 times and the median is taken, to avoid one-off noise. Startup is measured to the point the app is up, and the speaker reports medians in ms. *When:* Comparing desktop app runtimes or any cold-start benchmark where a single run is noisy.
- **Sum all related processes when measuring memory** — Include the system web view processes that macOS starts as separate processes, not children, and add them to the app's own process before comparing against Electron or other bundled-Chromium apps. Activity Monitor on its own can undercount by about 3x for Tauri. *When:* Comparing memory footprint across apps that use a system web view versus a bundled Chromium.
- **Keep screen capture in the native backend** — Use the platform capture API (ScreenCaptureKit on macOS) from the backend, handing it a display, a codec and an output file path, and let it write the MP4 with mixed mic and system audio. The web view only handles UI. *When:* Building a recording or media-processing desktop app where frame throughput and bundle size matter more than sharing one codebase between the UI and capture logic.
- **Keep a Deno Desktop app alive with no visible windows** — Instead of hiding the last window, move it off-screen, so the runtime does not treat the app as finished and terminate. *When:* Building on Deno Desktop with flows that hide the main window during a long-running task such as recording.

## Numbers
- Bundle size: Electron 323 MB (baseline), Tauri 57 MB, Electrobun 418 MB, Deno Desktop 111 MB. FFmpeg adds about 45 MB to each; Chromium adds about 200 MB to Electrobun. ([1:28](https://youtu.be/ktkDGQyRx3Y?t=88))
- Median startup (10 runs): Deno Desktop about 242 ms, Electron 273 ms (baseline), Tauri about 311 ms, Electrobun about 773 ms. ([2:55](https://youtu.be/ktkDGQyRx3Y?t=175))
- Memory after launch: Electron 128 MB (baseline), Tauri 109 MB, Electrobun 208 MB, Deno Desktop 98 MB. ([4:09](https://youtu.be/ktkDGQyRx3Y?t=249))
- Activity Monitor shows Tauri at about 36 MB; summing its system web view processes gives about 109 MB. ([4:09](https://youtu.be/ktkDGQyRx3Y?t=249))

## Hot takes
- The 10x memory improvement that Tauri's marketing implies does not hold at runtime, because the on-disk size gap is much larger than the memory gap.
- Electrobun is the worst of the four in this test: largest bundle, slowest startup, double the memory, and the most developer-experience issues.
- Deno Desktop is a reasonable option but the platform still needs time to mature, judged on the crash-on-hide behavior.
- Tauri is the recommended pick for most people, unless the team does not want to write Rust, in which case Electron is the mature TypeScript option.

## Tools mentioned
Tauri, Electrobun, Deno Desktop, Electron, Bun, Chromium, FFmpeg, ScreenCaptureKit, Rust, TypeScript, Three.js, Babylon.js, Activity Monitor, QuickTime
