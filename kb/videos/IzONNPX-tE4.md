# The BEST way to Create Desktop Apps (Electron)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `IzONNPX-tE4` · [watch](https://youtu.be/IzONNPX-tE4) · **date:** 2025-11-02 · **length:** 5:15 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** Bernard · **orgs:** Better Stack
- **topics:** dev-tools · **tags:** electron, desktop-apps, npm, preload-script, contextBridge, ipc, browserwindow, javascript

> Beginner Electron tutorial: scaffold an npm project, load local HTML in a BrowserWindow, and use a preload script with contextBridge to build a simple audio player.

## Summary
Bernard from Better Stack walks through building a small desktop audio player with Electron, starting from an empty folder. He creates an npm project, installs Electron as a dev dependency, and adds a start script that runs Electron against the current directory. He then creates a window in the main process, sets its size to 600 by 280, and loads a local index.html, noting that an Electron desktop app is essentially local HTML, CSS and JavaScript running inside Electron. He hides the menu bar and explains the split between the main process and the renderer. The file-open dialog lives in the main process, and a preload script uses contextBridge to expose one narrow openFile method to the page. The renderer then handles play/pause, a play-state flag, and a time display. The transcript ends at about 4:44 with the speaker saying the track can be played, so the last few seconds of the 5:15 video are not captured.

## Key ideas
- **An Electron desktop app is web tech (HTML, CSS, JavaScript) running inside Electron. The speaker's point is that a desktop app is just local HTML in Electron, the same way a web app like Figma runs in a browser.** — Contrasts the browser and desktop versions of one web app to make the point that the window is just a page. ([0:00](https://youtu.be/IzONNPX-tE4?t=0))
- **Project setup is minimal: npm init -y, install electron as a dev dependency, and add a start script that runs Electron on the current directory. npm run start then confirms the app launches.** — Console.log in index.js is the first smoke test before any window is created. ([0:00](https://youtu.be/IzONNPX-tE4?t=0))
- **The main process (index.js) creates the window only after the app is ready, and loads a local index.html into it. Hiding the menu bar is a window-level option.** — Speaker uses app.whenReady before createWindow, then win.loadFile for the HTML file. ([1:09](https://youtu.be/IzONNPX-tE4?t=69))
- **Privileged work such as the open-file dialog happens in the main process. The renderer reaches it only through a preload script that exposes one specific method.** — The speaker says the preload runs before anything else in the renderer and exposes a narrow API rather than full access. ([2:17](https://youtu.be/IzONNPX-tE4?t=137))
- **The first attempt fails silently. Calling the file-open API from the page does nothing until it is exposed through the preload script, and the speaker says that is expected at this step.** — This is the step where the audio player stops working for the first time and the reader has to wire the preload into the window options. ([2:17](https://youtu.be/IzONNPX-tE4?t=137))
- **The player logic is ordinary DOM code in a renderer script. Open-file sets the audio source and loads it. Play/pause toggles on an is-playing flag, play and pause events keep the button label in sync, and a helper updates the time display.** — No framework is used. The renderer script is app.js in a scripts folder. ([3:36](https://youtu.be/IzONNPX-tE4?t=216))

## Techniques
- **Bootstrap a minimal Electron project** — Run npm init -y to create package.json. Run npm install electron -D (dev dependency). Add a start script to package.json that runs the electron command on the current directory. Run npm run start; a console.log in index.js confirms the main process runs. *When:* Starting any new Electron app from an empty folder.
- **Create a window and load local HTML** — In index.js, import app and BrowserWindow from electron. Call app.whenReady() and then createWindow(). In createWindow, construct a BrowserWindow with width 600 and height 280, then call win.loadFile on index.html. Set the menu bar visibility option to false to remove the default menu. *When:* Any small desktop UI where the window should show local HTML with no menu bar.
- **Preload script with contextBridge for one privileged method** — Create preload.js and use contextBridge to expose a global object (called Electron API in the video) with a single openFile method. That method sends a message to the main process and waits for the result. In the BrowserWindow options, point the preload option at preload.js. In the main process, handle the message by opening the file dialog, with filters for allowed file types. *When:* When the renderer needs a specific OS capability (here, a file dialog) and you want to avoid giving the page full Node or IPC access.
- **Renderer-side player wiring** — In a renderer script (app.js in a scripts folder), query the open-file button, play button, audio element and time display. On open, call the exposed API and, if a path comes back, set it as the audio source and load it. On play click, check an is-playing flag: pause if true, otherwise play. Listen to the audio play and pause events to update the button label and the flag. Update the time display from the audio's duration and current time. *When:* Small media or utility UIs in an Electron renderer with no framework.

## Numbers
- Starter window size: width 600, height 280 ([1:09](https://youtu.be/IzONNPX-tE4?t=69))

## Hot takes
- The title says 'The BEST way', but this is a beginner walkthrough of one approach. It has no comparison with other desktop frameworks and nothing on packaging or distribution.
- The transcript ends at about 4:44 with 'play it.' The last part of the 5:15 video, including any final demo, is not captured, so the working end-to-end claim is only as good as the speaker's word.
- The speaker points to a source code link in the description, which is not part of the captions.

## Tools mentioned
Electron, npm, Figma (cited only as a web app that also ships a desktop version)

## Relevance to our work
- **prosharness** (1/3): ProsHarness is a harness around the Claude Code CLI with phone-driven approvals. If it ever gets a desktop status or approval UI, this video shows the main/renderer/preload split with contextBridge. → *If a desktop UI for ProsHarness is planned, follow the preload + contextBridge pattern and expose one narrow method rather than giving the page full access.*
