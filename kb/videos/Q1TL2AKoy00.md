# Wails: Golang's Bet On Desktop Grade Apps To Beat Electron

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Q1TL2AKoy00` · [watch](https://youtu.be/Q1TL2AKoy00) · **date:** 2026-08-02 · **length:** 7:02 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Warren · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** wails, golang, tauri, electron, desktop-apps, cgo, objective-c, screencapturekit, benchmarks, bundle-size

> Better Stack builds the same screen recorder in Wails (Go), Tauri and Electron and compares bundle size, startup, capture performance and developer experience. Wails wins on size, Electron on startup, and Tauri on ecosystem.

## Summary
Warren from Better Stack builds a desktop screen recorder with Wails, a Go backend with a web-view frontend, and compares it against the same app in Tauri and Electron. Wails, like Tauri, uses the platform's native web view instead of bundling Chromium, so its app bundle is far smaller than Electron's (52 MB vs 324 MB). The walkthrough shows the Wails project layout and its dev mode, where Go function changes regenerate the TypeScript bindings and reload the app. Startup times favour Electron in this test, at both warm and cold start. Runtime recording is faster in the Wails and Tauri builds because they use Apple's ScreenCaptureKit directly, while the Electron build captures from the web view. The main cost is developer experience: Go has no screen-capture wrapper, so the Wails build needed about 450 lines of Objective-C linked through cgo, which the Rust crate in the Tauri build did not need. The speaker's verdict is a slight lean toward Tauri for its crate ecosystem, with Wails a reasonable choice for Go developers.

## Key ideas
- **Wails pairs a Go backend with a web-view frontend and, like Tauri, reuses the native rendering engine per platform instead of embedding a browser.** — Frontend is React/TypeScript in a frontend folder. Go methods are called from the UI as if they were local functions. ([0:00](https://youtu.be/Q1TL2AKoy00?t=0))
- **Dev mode keeps the Go-to-TypeScript contract in sync. Changing an exported Go function regenerates the TS API typings, and the app reloads.** — Commenting out a Go function made the TS import fail with a missing-symbol error. Restoring it cleared the error and reloaded the desktop app. ([2:10](https://youtu.be/Q1TL2AKoy00?t=130))
- **Bundle size is the clearest win for Wails and Tauri. Both are much smaller than Electron because neither ships Chromium.** — Wails 52 MB, Tauri 57 MB, Electron 324 MB. The speaker expects platform rendering differences to be a small concern. ([2:10](https://youtu.be/Q1TL2AKoy00?t=130))
- **Electron started faster in this test, both warm and cold, which goes against the usual assumption.** — Warm start: Electron 350 ms, Wails 395 ms, Tauri 410 ms. Cold start with the cache purged: Electron 1890 ms, Tauri 2049 ms, Wails 2337 ms. ([3:35](https://youtu.be/Q1TL2AKoy00?t=215))
- **Runtime recording is faster in Wails and Tauri because they capture natively, not through the web view.** — They use Apple's ScreenCaptureKit directly, so no frame data crosses the bridge. The Electron baseline records from the web view and forwards the data to the backend, which adds overhead. The speaker notes Electron could also use native capture with custom C code. ([3:35](https://youtu.be/Q1TL2AKoy00?t=215))
- **The main developer-experience cost in Wails is native screen capture. Go has no ScreenCaptureKit wrapper, so the speaker wrote about 450 lines of Objective-C.** — Rust's Tauri build used a community crate wrapping ScreenCaptureKit, so it needed no native code. Go's cgo lets you write plain C-callable .m code and link Apple frameworks, but you own all of that code. ([5:02](https://youtu.be/Q1TL2AKoy00?t=302))
- **Verdict: a slight lean toward Tauri because its ecosystem is stronger. Wails is a decent choice for teams that prefer Go and can accept some native code.** — The speaker calls the choice mostly a matter of preference. ([5:02](https://youtu.be/Q1TL2AKoy00?t=302))

## Techniques
- **Wails app layout and entry config** — Keep the web frontend in a frontend/ folder (React + TypeScript, src/app.tsx). Put the entry point in main.go with a main() that sets the window title, width, height and background colour. Add platform-specific options in the same file (the speaker shows Mac-only options) when macOS and Windows need to differ. *When:* Starting a Wails desktop app, or moving an Electron-style project to Go with the same frontend structure.
- **Calling Go from the frontend through generated bindings** — Export Go methods from app.go (for example ListSources, StartRecording, RequestScreenAccess, ExportVideo). Import the generated api module in the React code and call those methods. Wails regenerates the TypeScript definitions from the Go signatures on each change. *When:* Wiring UI actions to Go backend logic without writing a manual IPC layer.
- **Dev-loop check for Go/TS contract drift** — Run the app in dev mode. Comment out an exported Go method and save: the TS build reports the missing symbol. Restore it and the error clears and the app reloads. Use this to confirm that a backend signature change is reflected in the frontend. *When:* Refactoring Go-exposed methods while the frontend is live.
- **Native macOS screen capture from Go via cgo** — Write the Objective-C code in a .m file and expose plain C functions. Declare the Apple frameworks to link against through cgo, then call those C functions from Go. The speaker used about 450 lines of Objective-C to call ScreenCaptureKit (the transcript says CaptureKit). *When:* A Go app needs a platform API with no Go wrapper. Expect this work to be the main cost.
- **Startup benchmark method** — Launch each built app 10 times and average the times for warm starts. For cold starts, purge the cache before each launch and time it. *When:* Comparing desktop framework startup cost on the same machine.

## Numbers
- Bundle size: Wails 52 MB, Tauri 57 MB, Electron 324 MB. ([2:10](https://youtu.be/Q1TL2AKoy00?t=130))
- Warm startup (avg of 10 launches): Electron 350 ms, Wails 395 ms, Tauri 410 ms. ([3:35](https://youtu.be/Q1TL2AKoy00?t=215))
- Cold startup (cache purged): Electron 1890 ms, Tauri 2049 ms, Wails 2337 ms. ([3:35](https://youtu.be/Q1TL2AKoy00?t=215))
- Native screen-capture code needed for the Wails build: about 450 lines of Objective-C. ([5:02](https://youtu.be/Q1TL2AKoy00?t=302))

## Hot takes
- Electron had the fastest startup in both warm and cold tests, which cuts against the usual 'Electron is slow to start' claim. The sample is 10 launches on one machine.
- The runtime-performance comparison is not like for like. Wails and Tauri use native capture, and the Electron baseline records from the web view. The speaker concedes Electron could use native capture with custom C.
- The speaker's own verdict is that Wails is slightly behind Tauri on ecosystem for screen capture, and that developers who prefer Go can accept writing native code.
- The benchmarks appear to be macOS-only. The transcript mentions Windows only for the target platforms, not for measurements.

## Tools mentioned
Wails, Go, Tauri (called Torii in the captions), Electron, React, TypeScript, Rust, ScreenCaptureKit (transcript says CaptureKit), cgo, Objective-C

## Relevance to our work
- **general** (1/3): Mildly useful background if a desktop front end for an internal tool is ever needed. → *Skip unless a desktop UI for AgentOS or ProsHarness becomes a concrete need.*
