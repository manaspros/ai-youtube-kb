# I Built an App in 10 Minutes WITHOUT Coding! | Using Cursor Composer

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `LrIhNW2BN28` · [watch](https://youtu.be/LrIhNW2BN28) · **date:** 2024-11-02 · **length:** 5:44 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Cursor
- **topics:** vibe-coding-app-building, coding-agents, context-engineering · **tags:** cursor, composer, multi-file-generation, spec-file, vibe-coding, ide-agent, inline-edit, codebase-context

> Short Cursor promo that builds a budget tracker and a task app from plain-text requirements with Composer; shows multi-file generation, but the evidence is two cherry-picked demos.

## Summary
The AI LABS channel walks through Cursor's Composer feature by building two small front-end apps: a personal budget tracker and a task-management board. The method is to write the requirements into a plain text file in the project folder, then open Composer (Ctrl+I) and tell it to build from that file. The narrator says Composer creates several files at once and wires them together, and the side panel shows the file tree forming. The second app's first output looks plain, so a follow-up prompt asks for a better design, and remaining bugs are fixed through Composer and the chat panel. The video also tours Cursor's Tab completions and chat context references (@Codebase, @Web, @Docs, @file/symbol) and the Ctrl+K inline edit. It is mostly a product pitch with a download call to action at the start and end, and it shows no tests, code review, or measured timings.

## Key ideas
- **Composer generates a whole small app from one prompt, creating multiple files and connecting them** — The narrator says Composer reads all project files at once and produces a working multi-file front-end app (budget tracker) in one generation, with the file structure visible in the side panel. The claim that it reads all files at once is not checked in the video. ([0:00](https://youtu.be/LrIhNW2BN28?t=0))
- **Write requirements in a plain text file first, then point Composer at it** — The workflow starts by creating a text file that lists the features, then opening Composer and telling it to follow that file. Cursor's autocomplete helps while the requirements are being typed. ([0:00](https://youtu.be/LrIhNW2BN28?t=0))
- **Composer narrates the code it writes, and the narrator claims this helps beginners** — The narrator says Composer explains the generated code, so a newcomer can build it and an experienced developer can see what each feature does. No example of the explanation is shown. ([1:30](https://youtu.be/LrIhNW2BN28?t=90))
- **Chat context references and Ctrl+K cover the questions and edits outside Composer** — In chat, @Codebase (Ctrl+Enter) searches the project, @file and @symbol point at specific code, @Web fetches recent information, and @Docs or a library name adds documentation. Ctrl+K edits a selected region from a description. ([2:57](https://youtu.be/LrIhNW2BN28?t=177))
- **Tab completions and smart rewrites are presented as the everyday editing layer** — Tab offers multi-line edits, predicts the next edit from recent changes, and suggests fixes. This is a feature tour and is not tied to the app builds. ([2:57](https://youtu.be/LrIhNW2BN28?t=177))
- **The second app took three passes: generate, improve the design, then fix bugs** — The first output of the task app looked unpolished, so the narrator asked Composer for a better design. Bugs remained after that, so Composer and the chat panel were used together to fix them. This is the only shown iteration loop. ([4:42](https://youtu.be/LrIhNW2BN28?t=282))
- **The final result is a card-based task board, presented as proof that a non-coder can ship it** — The task app has list columns where cards can be moved, and the narrator calls it fully functional. The video shows no test run or real usage, only the UI and the narrator's claim. ([4:42](https://youtu.be/LrIhNW2BN28?t=282))

## Techniques
- **Requirements file, then generate** — Create a plain text file in the project folder listing features and screens. Open Composer with Ctrl+I and say to build the app following that file. Keep the file in the repo so it can be re-read later. *When:* Greenfield small apps or prototypes where a single-page spec is enough.
- **Enable Composer before first use** — Open the command palette, type Composer, and enable it if it is off by default. This is a one-time setup step shown at the start of the video. *When:* First run of Cursor Composer.
- **Generate, then re-prompt for design, then fix bugs** — After the first generation, send a separate Composer prompt that asks only for better visual design. Then fix the remaining bugs in a separate pass, using Composer for multi-file edits and the chat panel for targeted questions. *When:* When the first output works but looks rough or has bugs. Keep each pass to one concern.
- **Scope chat with @-references** — Use @Codebase (Ctrl+Enter in chat) to ask questions across the project. Use @file or @symbol to point at specific code. Use @Web for recent information and @Docs or a library name for documentation. Paste images into chat for visual context. *When:* Questions about a larger codebase or APIs that the model may not know.
- **Ctrl+K for local edits** — Select a region of code, press Ctrl+K, and describe the change. Use it for small, local edits rather than multi-file changes. *When:* Local edits inside one file where the diff is small.

## Numbers
- Title claims the app was built in 10 minutes; the video shows no timer and runs 5:44 for two apps ([0:00](https://youtu.be/LrIhNW2BN28?t=0))
- Narrator says Cursor is free (no pricing shown) ([0:00](https://youtu.be/LrIhNW2BN28?t=0))
- Budget tracker built from one Composer generation, no manual code (no count of files or time shown) ([1:30](https://youtu.be/LrIhNW2BN28?t=90))

## Hot takes
- Mostly a product pitch: download calls at the start and end, and the narrator says it is free and does everything without code. No pricing or limits are shown.
- The first budget app is shown working with no bug pass. The task app needed a design pass and bug fixes, so the one-shot claim is weaker than the title suggests.
- No tests, code review, or real-usage check. 'Fully functional' is the narrator's word only.
- 'Reads all of your files at the same time' and 'explains the code clearly' are stated, not demonstrated.

## Tools mentioned
Cursor, Cursor Composer, Cursor Tab (completions), Cursor Chat (@-references), Cursor Ctrl+K inline edit

## Relevance to our work
- **prosharness** (1/3): Writing requirements to a file before a coding agent builds from it is close to ProsHarness's plan-first flow. The video gives no evidence that it improves results. → *Check whether ProsHarness's plan step can take a requirements file as input, so the spec is saved in the repo and can be re-read between runs.*
