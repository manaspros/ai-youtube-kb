# Get Started with Cursor: The AI Code Editor That Lets You Build Without Coding

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `NtGagWyY1kU` · [watch](https://youtu.be/NtGagWyY1kU) · **date:** 2024-11-02 · **length:** 5:16 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Cursor
- **topics:** coding-agents, vibe-coding-app-building · **tags:** cursor, ide, ai-code-editor, inline-edit, chat, pygame, beginner, vs-code

> A 5-minute beginner walkthrough of the Cursor AI code editor: install, set up, use Ctrl+L chat and Ctrl+K inline edits to generate and modify small Pygame games. Thin, hype-framed, no review of output quality.

## Summary
The host introduces Cursor as a VS Code-style AI editor that reads project context and takes natural-language instructions. He covers the free tier limits as stated, installing the app, importing VS Code keybindings and extensions, signing in, and optionally using your own API key. The core demo has him use the built-in chat (Ctrl+L) to generate a Python Pygame tic-tac-toe game and a snake game, copying the code out and running it. He then uses Ctrl+K inline editing to slow the snake down and change its color, clicking Apply and Accept on each suggested diff. The video makes strong claims that the games "work perfectly" with no hand-written code, but it does not show errors, debugging, or code review, and the games are very small.

## Key ideas
- **Cursor is positioned as a VS Code-like editor whose AI understands project context and makes multi-file changes, not just a chat sidebar.** — The host claims it reads and changes the whole codebase; no multi-file edit is actually demonstrated in the video. ([0:00](https://youtu.be/NtGagWyY1kU?t=0))
- **Setup mirrors VS Code: you can import VS Code keybindings and extensions, pick the UI language, then sign up and sign in.** — Import happens on the first-launch setup screen before the editor opens. ([1:28](https://youtu.be/NtGagWyY1kU?t=88))
- **Model choice is configurable, and you can bring your own API key; individual AI features can be toggled off in a Features tab.** — Presented as a control and customization point for tailoring the editor. ([1:28](https://youtu.be/NtGagWyY1kU?t=88))
- **Ctrl+L opens the built-in chat, used here to generate a complete Pygame tic-tac-toe game from one prompt.** — The host copies the generated code into a file by hand and runs it; there is no in-editor run step shown. ([2:00](https://youtu.be/NtGagWyY1kU?t=120))
- **Ctrl+K inline edit takes a prompt, proposes a code diff, and applies it on Apply, with an Accept step after review.** — Used to slow the snake game down and then change the snake color; both edits are verified by running the game. ([3:01](https://youtu.be/NtGagWyY1kU?t=181))
- **The 'works perfectly, no code written' claim rests on tiny single-file games with no failures, debugging, or tests shown.** — The video ends with a general claim that the tool makes code modification a breeze and efficient and error-free, which the demo does not test. ([4:30](https://youtu.be/NtGagWyY1kU?t=270))

## Techniques
- **Chat-first prototyping of a small game** — Press Ctrl+L, give a full natural-language spec (e.g. 'tic-tac-toe in Python using Pygame'), copy the generated code into a .py file, and run it with python. *When:* Greenfield toy projects where you want to see a working artifact in minutes; the host does not show iteration on failures.
- **Inline edit with prompt, Apply, Accept** — Select or position in code, press Ctrl+K, describe the change (e.g. 'decrease the snake speed', 'change the snake color'), review the suggested diff, click Apply, then Accept, and re-run to check the change. *When:* Small, local, targeted edits to a file you can run and visually verify.
- **VS Code migration at setup** — On first launch, choose to import VS Code keybindings and extensions, and set the UI language, to keep an existing VS Code workflow. *When:* Switching from VS Code who want the same keymap and extensions.
- **Toggle AI features and bring your own model key** — Use the Features tab to turn individual AI features on or off, and configure models in settings, optionally with your own API key. *When:* When a feature misbehaves (toggle it off) or when you want to control which model and billing path is used.

## Numbers
- Free tier as stated: 2-week Pro trial, 2,000 code completions, 50 slow premium requests, 200 small Cursor uses. The figures are from the 2024-11 video and may be out of date. ([0:00](https://youtu.be/NtGagWyY1kU?t=0))
- The video is 5:16 long; the prototyping section (chat games) runs from about 2:00 to 3:00, and the inline-edit section runs from about 3:01 to 4:30. ([2:00](https://youtu.be/NtGagWyY1kU?t=120))

## Hot takes
- Title claims 'build without coding', but the video only shows generating two toy Pygame games and making two small edits, with no failures, debugging, or review.
- Presenter says the code is 'efficient and error-free' without testing any of it, which is overclaiming for a 5-minute demo.
- Free-tier limits and setup steps are 2024-era details that have likely changed; treat them as historical.

## Tools mentioned
Cursor, VS Code, Python, Pygame

## Relevance to our work
- **prosharness** (1/3): Coding-agent UX (chat plus inline apply/accept) is adjacent to the Claude Code CLI workflows ProsHarness wraps, but the video shows no agent loop, checkpointing, or automation. → *Skip unless comparing Cursor's Ctrl+K apply/accept review step against ProsHarness's approval flow for file edits.*
