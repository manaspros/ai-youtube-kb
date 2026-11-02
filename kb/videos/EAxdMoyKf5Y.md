# 10 Chrome DevTools Tricks You Didn't Know! (3rd is Crazy)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `EAxdMoyKf5Y` · [watch](https://youtu.be/EAxdMoyKf5Y) · **date:** 2025-11-02 · **length:** 7:22 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** ?
- **topics:** dev-tools, observability · **tags:** chrome-devtools, browser-debugging, network-throttling, local-overrides, console-logging, screenshots, keyboard-shortcuts, front-end

> A 7-minute, beginner-level tour of ten Chrome DevTools tricks: local overrides, keyboard shortcuts, focus emulation, node screenshots, the animation editor, network throttling, styled console logs and AI assistance.

## Summary
The host walks through ten Chrome DevTools tricks in a short tutorial, mostly aimed at front-end developers. The most practical is local overrides: edit a response in the Network tab, save with Ctrl+S, and the change persists across reloads without touching a server. The rest are keyboard shortcuts (Ctrl+P file search, Ctrl+Shift+P command palette, "?" for the shortcut list), "Emulate a focused page" to keep focus-dependent dropdowns open while inspecting, screenshots of a full page or single element via "Capture node screenshot", the Animations panel for adjusting timing and easing, network throttling presets with "Disable cache", styled console.log output using a base64 background image, and the built-in AI assistant. Nearly all of this is documented, basic DevTools usage. The video is short and light on depth, and its title promises a "crazy" third trick that is not especially distinctive.

## Key ideas
- **Local overrides make page edits persist across reloads without changing any server or database: override a network response in the Network tab and save.** — The speaker frames this as the riskiest trick and says the edit survives a reload because it is stored as a local override, not a server change. ([0:00](https://youtu.be/EAxdMoyKf5Y?t=0))
- **DevTools can be opened with a keyboard shortcut when the browser menu or right-click is unavailable, for example in Google Docs.** — Ctrl+Shift+I opens DevTools where the three-dot menu route is hard to find. ([0:00](https://youtu.be/EAxdMoyKf5Y?t=0))
- **Keyboard-driven navigation: Ctrl+P for files, Ctrl+Shift+P for the command palette, and '?' for the list of panel shortcuts.** — The speaker suggests this for people who avoid the mouse, and points to the official DevTools shortcut docs for the full list. ([1:25](https://youtu.be/EAxdMoyKf5Y?t=85))
- **Emulate a focused page keeps focus-dependent UI (such as dropdowns that close on blur) open while you inspect them.** — The speaker says the old workaround was a debugger statement inside setTimeout. The option is described as being under the styles area, and with it enabled the document reports hasFocus as true. ([2:13](https://youtu.be/EAxdMoyKf5Y?t=133))
- **Screenshots can come from DevTools rather than an extension: capture a full-page or single-element screenshot from the Elements panel, or from the command palette.** — Right-click the body tag and choose Capture node screenshot for the full page, or use the same option on any element to capture only that section. ([3:16](https://youtu.be/EAxdMoyKf5Y?t=196))
- **The Animations panel lets you edit timing, start offset, speed and easing visually, then copy the result into CSS.** — DevTools applies the changes as inline styles while you edit, and you can also tweak the easing in the Styles pane before copying it out. ([4:11](https://youtu.be/EAxdMoyKf5Y?t=251))
- **Use network throttling presets such as 3G or slow 4G, together with Disable cache, to test how an app performs on slow connections.** — The speaker recommends this for every web app and presents it as a consideration for users on slow networks. ([5:38](https://youtu.be/EAxdMoyKf5Y?t=338))
- **console.log can take CSS via the %c format specifier, including a base64 image background, so log output can be styled.** — Any CSS property works here, including font size, colour, padding and borders. The speaker presents it as a fun trick rather than a debugging technique. ([5:38](https://youtu.be/EAxdMoyKf5Y?t=338))

## Techniques
- **Persist page edits with local overrides** — Open DevTools (Ctrl+Shift+I). In the Network tab, find the API request that returns the data you want to change. Right-click it and choose Override content. Search for the value, edit it, press Ctrl+S, then reload the page. The change persists locally because it is an override, not a server change. *When:* Prototyping how a page looks with different data, or demonstrating a UI state without changing the backend. Not for anything that must be shared.
- **Keyboard navigation of DevTools** — Ctrl+P opens the Sources file search, where you can type a file name such as a CSS or JS file. Ctrl+Shift+P opens the command palette, which lists commands to run. Typing '?' shows the panel's shortcut help. The official DevTools docs list more shortcuts. *When:* Working without a mouse, or when a file is easier to find by name than by walking the Network tab.
- **Keep focus-dependent UI open for inspection** — Enable the 'Emulate a focused page' option (the speaker says it sits under the styles area). Open the dropdown, then click elsewhere. The element stays open, and document.hasFocus() returns true. Before this option existed, the speaker used a debugger statement inside setTimeout to pause and inspect. *When:* Inspecting menus, popovers or tooltips that close when the window loses focus.
- **Capture screenshots from DevTools** — In the Elements panel, right-click the body tag (full page) or a specific element (that section) and choose 'Capture node screenshot', which downloads a PNG. Alternatively, search for 'screenshot' in the command palette. *When:* Capturing a page or component for a bug report or docs, without installing an extension.
- **Edit CSS animations in the Animations panel** — Open the Animations panel to see a timeline of every animated element. Drag to adjust start time, duration and playback speed. Edit the easing in the Styles pane. DevTools writes the changes as inline styles, and you can copy the final animation CSS out. *When:* Tuning timing and easing curves visually rather than by trial and error in code.
- **Simulate slow networks** — In the Network tab, change the throttling dropdown from 'No throttling' to a preset such as 3G or slow 4G. Tick 'Disable cache' (the speaker says it is under the Wi-Fi icon in the same toolbar) so that each test reflects a cold load. *When:* Testing loading states, perceived performance and failure modes on slow connections during development.
- **Style console output with %c** — Call console.log with a format string that includes %c and pass a CSS string as the second argument. The CSS can include a base64 image as background, plus font size, colour, padding or border. *When:* Making important log lines easy to spot while debugging. Cosmetic, but cheap to do.
- **Ask the built-in AI assistant** — Use DevTools' AI assistance panel to ask questions about the page's files, CSS styles or performance. The speaker presents it as a chat assistant inside the browser. *When:* Quick questions while debugging a specific page. The speaker does not go into detail or reliability.

## Numbers
- Video presents 10 DevTools tricks in 7:22 total runtime ([0:00](https://youtu.be/EAxdMoyKf5Y?t=0))
- Throttling presets named in the video are 3G and slow 4G; no bandwidth or latency values are given ([5:38](https://youtu.be/EAxdMoyKf5Y?t=338))
- The video gives no benchmarks, costs or adoption statistics ([0:00](https://youtu.be/EAxdMoyKf5Y?t=0))

## Hot takes
- The title's 'the 3rd is crazy' promise is not delivered: the content is standard, documented DevTools usage aimed at beginners.
- Local overrides are the most useful trick here for prototyping, but the video does not mention the risks of forgetting that edits are local-only or of stale overrides shadowing real API changes.
- The video is short and light on depth (most tricks get 30 to 60 seconds), so it works better as a quick reference than as a deep dive.

## Tools mentioned
Chrome DevTools, Chrome, Google Docs, ChatGPT (mentioned in passing as a comparison)

## Relevance to our work
- **agentos** (1/3): Could help debug a web dashboard built on AgentOS, but nothing here is specific to agents, LLMs or the proxy. → *When building or debugging the AgentOS UI, use DevTools Network 'Override content' to fake API responses and throttling to test slow paths.*
