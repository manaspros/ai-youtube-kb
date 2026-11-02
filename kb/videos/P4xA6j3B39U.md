# Google's New AI Code Editor Built My Flutter App in the Browser!"

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `P4xA6j3B39U` · [watch](https://youtu.be/P4xA6j3B39U) · **date:** 2025-11-02 · **length:** 8:37 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed host · **orgs:** Google
- **topics:** coding-agents, vibe-coding-app-building · **tags:** project-idx, gemini, flutter, browser-ide, cloud-ide, vibe-coding, apply-code-changes, android-emulator

> Hands-on review of Google's browser-based Project IDX: the host builds a Flutter task-manager app with its Gemini chat, and reports that fixes needed repeated prompting and manual insertion.

## Summary
The host tests Google's browser IDE Project IDX by building a Flutter task-manager app from a single prompt. They tour the VS Code-like interface, built-in terminal, VS Code extension support, in-browser Android emulator, and the upgraded Gemini chat, which can run terminal commands after permission and make multi-file edits. Generated code works after one revision, but a UI change breaks it. The host's fixes require pasting the whole file, and the "insert code" button places snippets at the cursor rather than the correct location, so they ask the model to write the full file and paste it in by hand. The model identifies bugs but sometimes does not edit files itself, and the animation feature takes several rounds. The verdict is that the tool is useful for browser-based app work, but it is not a full replacement for a normal setup on complex projects. The evidence is one anecdotal run with no benchmarks.

## Key ideas
- **Project IDX runs a full dev environment in the browser: VS Code-like UI, built-in terminal, VS Code extensions, and an in-browser Android emulator, so no local emulator setup is needed.** — The host says this removes system requirements and emulator setup (for example Expo) for Flutter work. ([0:00](https://youtu.be/P4xA6j3B39U?t=0))
- **The Gemini chat is an agentic upgrade over the basic chat: it can propose terminal commands for permission, run them, and make multi-file edits.** — Terminal commands need user approval before running. The host shows it listing directory contents after a command runs, and says it makes installing packages easier. ([2:01](https://youtu.be/P4xA6j3B39U?t=121))
- **A single generated prompt can produce a working app, and the chat shows a diff review before the change is applied.** — The first prompt for a task-manager app worked after the review-and-update step. The UI-change prompt that followed produced visible issues on review. ([3:26](https://youtu.be/P4xA6j3B39U?t=206))
- **Applying a fix is the weak point. The insert button places code at the cursor rather than in the right place, so the host pastes the full file manually.** — The host compares this unfavorably with Cursor. The fix that finally worked was asking the chat to write the whole file. ([4:32](https://youtu.be/P4xA6j3B39U?t=272))
- **Explicit insert requests worked where the button did not, but the host says this should be built in.** — After asking the model to insert the code directly into the file, the insertion placed it correctly. The host notes they should not have to ask for this. ([5:38](https://youtu.be/P4xA6j3B39U?t=338))
- **Multi-step fixes take many rounds, and the model sometimes diagnoses without editing.** — For the animation request, the model identified the issue but did not change the code. The host had to name the file to update, and the fix took several attempts. ([7:00](https://youtu.be/P4xA6j3B39U?t=420))
- **Verdict: useful for browser-based app building, but not yet a replacement for a normal setup on more complex projects.** — The host calls it an exciting step forward, notes it took several attempts to get the animation working, and says it is worth trying for experimentation. ([8:09](https://youtu.be/P4xA6j3B39U?t=489))

## Techniques
- **Full-file repair loop** — When the chat's snippet fix does not apply cleanly, paste the entire current file into the chat, describe the symptom, and ask for the complete updated file back. Then copy the whole file over. The host reports this worked after the snippet insert failed. *When:* The AI-suggested snippet insert places code incorrectly, or when a fix spans several parts of one file.
- **Explicit insert prompt** — Ask the chat in plain words to insert the code directly into the named file, instead of using the Insert button, then review the result. *When:* The editor's insert button misplaces code at the cursor.
- **Observable-symptom prompt** — Describe what is visible or missing on screen, for example that tasks are not visible, not the code path. The host reports this produced a usable fix where earlier generic error prompts did not. *When:* The app runs but a feature fails in the UI and the model is not converging.
- **Review diff before applying** — Open the chat's review view for proposed changes before updating the file, and check for visible issues first. *When:* Any time the chat proposes a multi-file or UI-heavy change.
- **Setup steps for the browser IDE** — Accept the terms, enable the AI features when prompted, choose a template (Next.js, Flutter, Python, Go or Node.js) or import a GitHub repo, name the app, then wait for the environment to load before prompting. *When:* Starting a new prototype in the browser without a local toolchain.

## Numbers
- Video runtime is 8:37. ([0:00](https://youtu.be/P4xA6j3B39U?t=0))
- The task-manager build took about seven prompt rounds: the app prompt, a UI-change prompt, an error prompt, a request to insert the fix, a visible-symptom prompt, an animation prompt, and an animation retry (count is from the transcript). ([2:01-8:09](https://youtu.be/P4xA6j3B39U?t=0))
- No benchmarks, latency, cost, or adoption figures are given. ([0:00](https://youtu.be/P4xA6j3B39U?t=0))

## Hot takes
- Google's in-browser IDE is convenient for Flutter prototyping, but its AI apply/insert step is less reliable than Cursor's, and the host says it should be built in.
- Gemini integration is a real step forward (terminal commands, multi-file edits), but the model often diagnoses without editing and needs manual steering.
- Single anecdotal run on one Flutter app; the host gives no measurements, so treat the verdict as a first impression rather than evidence.

## Tools mentioned
Project IDX, Gemini, Flutter, VS Code, Cursor, Windsurf, Expo, Next.js, Python, Go, Node.js

## Relevance to our work
- **prosharness** (1/3): Gives one anecdote on the apply-change step: the AI's suggestions needed manual insertion, and fixes took several rounds. Useful as a case for ProsHarness's review and approval flow, not a feature to adopt. → *When designing ProsHarness's approve-and-apply step for agent edits, make the proposed change show exactly where it will land and offer a full-file rewrite as a fallback, so an insert misplacement cannot silently break the file.*
