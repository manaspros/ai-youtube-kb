# Program Claude Code to be your new UI Designer (+ works with any IDE)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `TyGx277x9hQ` · [watch](https://youtu.be/TyGx277x9hQ) · **date:** 2025-11-02 · **length:** 13:12 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** AI LABS host (unnamed in transcript) · **orgs:** Anthropic, Cursor, OpenAI, Apple
- **topics:** claude-code, vibe-coding-app-building, coding-agents, context-engineering · **tags:** claude-code, cursor, chatgpt, swiftui, xcode, ios, html-to-swiftui, ui-prototyping, liquid-glass, plan-mode, image-input, reference-images, convert-md, todo-list

> Walkthrough of using Claude Code plus ChatGPT planning to turn an HTML UI prototype into a SwiftUI iOS app and re-skin it in Apple's Liquid Glass style; practical but anecdotal.

## Summary
The AI LABS host shows a UI-first workflow with Claude Code: a screenshot is cloned into an HTML prototype, and Claude Code works through its own built-in to-do list. Before coding, the host drafts plans in ChatGPT to save Claude Code tokens. The working prototype is converted into a SwiftUI app in Xcode, guided by a convert.md rules file that ChatGPT wrote after a web search for conversion best practices. The app is then restyled to Apple's Liquid Glass look by giving Claude Code two Apple screenshots plus a ChatGPT-written design-language report covering appearance and animation. Bugs are fixed by sending Claude Code screenshots of each problem. The host prefers Claude Code's terminal workflow over Cursor, and uses Cursor for straightforward tasks once a structure is planned. The results are shown only in an iOS simulator, with no timings, costs or metrics, and the video ends by noting models still struggle beyond Python, JavaScript and related frameworks.

## Key ideas
- **Plan and research in a chat model first, then hand the result to Claude Code, to save agent tokens.** — The host drafts the conversion approach in ChatGPT, asks it to web search best practices, and then gives the resulting context to Claude Code. He calls this a best practice for token savings. ([4:59](https://youtu.be/TyGx277x9hQ?t=299))
- **Claude Code runs its own to-do list and checks off tasks one by one, with no external task manager.** — The host contrasts this with Cursor, where he says external task tools are often needed to force a task list. ([2:48](https://youtu.be/TyGx277x9hQ?t=168))
- **Screenshots can be dropped straight into Claude Code as a reference to clone a UI into a static HTML prototype.** — Each page is generated as a separate screen in one HTML file (fitnessapp.html in the example). Functionality is not implemented at this stage. ([2:48](https://youtu.be/TyGx277x9hQ?t=168))
- **The host's split between tools: Claude Code for terminal-based planning and building, Cursor for executing structures that are already planned.** — He cites Claude Code's larger context limit and Cursor's Max mode, which is billed at API pricing. He uses Cursor for straightforward tasks on an existing structure, and converted the HTML prototype to Next.js there. ([1:27](https://youtu.be/TyGx277x9hQ?t=87))
- **A rules file (convert.md) directs the cross-format conversion from HTML prototype to SwiftUI.** — ChatGPT produced the rules after a web search for conversion best practices, and the host placed them in convert.md in the repo before Claude Code converted the app. The contents of the rules are not shown in the video. ([8:51](https://youtu.be/TyGx277x9hQ?t=531))
- **Visual style can be transferred by pairing reference screenshots with a model-written design-language report that includes animation behavior.** — He gave Claude Code two Apple screenshots (side panel and navigation bar) with a ChatGPT report on how the design looks and animates, and Claude Code recognized the Liquid Glass style and applied it. ([9:58](https://youtu.be/TyGx277x9hQ?t=598))
- **Refinement after the first pass: ask for the design to be applied across all components, and fix bugs by sending screenshots of each one.** — The host says screenshots of the bugs sped up debugging. He notes that Claude Code took a while to build and test the output. ([10:59](https://youtu.be/TyGx277x9hQ?t=659))
- **Models still struggle outside Python, JavaScript and their frameworks, so other languages need more explicit context.** — This is the host's own caveat, and he offers no evidence for it in the video. ([12:18](https://youtu.be/TyGx277x9hQ?t=738))

## Techniques
- **Plan-in-chat, then execute in agent** — Discuss the conversion or design approach in ChatGPT with web search enabled. Ask it for a comprehensive plan or rules set, then paste the result into the repo as context before running Claude Code. Switch Claude Code modes with Shift+Tab between auto-accept edits and plan mode. *When:* Before any cross-framework port (for example HTML to SwiftUI) or when adopting an unfamiliar framework, to reduce agent token spend.
- **Screenshot-to-HTML prototype** — Drop the reference image into Claude Code and prompt it to clone the pages into one HTML file. Ask for each page to be displayed separately rather than as a single prototype app. Let Claude Code track its own task list. *When:* Fast UI prototyping from a visual reference, before any functional work.
- **Conversion rules file** — Create a markdown file (the host uses convert.md) in the repo that lists the translation rules for the target stack, generated from a web-searched best-practices pass. Point Claude Code at it for the conversion. *When:* Porting between formats or frameworks where the agent needs a stable spec to follow.
- **Style transfer from references** — Collect two or three official reference images. Have a chat model with web search analyze them and write a full design-language report covering appearance and animation. Give Claude Code the report and the images together, and ask it to apply the style across all components. *When:* Re-skinning an app to match a visual system the codebase does not already contain.
- **Visual bug reporting** — After the first pass, send Claude Code a screenshot for each visible bug or inconsistency, and ask it to fix all issues and polish. *When:* UI debugging, where describing the visual problem in text is slower and less precise.
- **Start from the native project template** — In Xcode, create a new project from the iOS or macOS template, then have Claude Code convert the prototype into it. *When:* Native app work where you need a correctly configured project skeleton before the agent writes code.

## Numbers
- No benchmarks, latencies, costs or token counts are given. The only quantities are qualitative: Cursor Max mode billed at API pricing, Claude Code's larger context limit, and two reference screenshots. ([1:27](https://youtu.be/TyGx277x9hQ?t=87))
- Two official Apple reference screenshots (side panel and navigation bar) were used for the Liquid Glass restyle. ([9:58](https://youtu.be/TyGx277x9hQ?t=598))
- Video length is 13:12 (metadata). The restyle was tested only in an iOS simulator, which the host calls laggy. ([10:59](https://youtu.be/TyGx277x9hQ?t=659))

## Hot takes
- The title's claim that the UI design industry is dead is hype. The substance is a single-author demo of one app.
- The claim that the apps are fully functional and can be sold is not backed by evidence in the video. Results are shown only in a simulator, and there is no App Store submission.
- The advice to plan in ChatGPT to save tokens is asserted without any token measurement.
- The convert.md rules and the design-language report are never shown, so the reproducible part is the workflow shape, not the actual rules.
- The host says models struggle beyond Python and JavaScript, but gives no example.
- Quality is capped at 2 because the title is hype and the substance is thin and anecdotal, even though the workflow steps are concrete.

## Tools mentioned
Claude Code, Claude 4 Sonnet, Claude Opus (Claude 4), Cursor (Max mode), ChatGPT, Xcode, SwiftUI, Swift, Next.js, HTML/CSS, iOS Simulator, Apple Liquid Glass design, macOS native dictation

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps the Claude Code CLI and has a plan stage. The video's pattern of drafting the plan and research in a cheaper chat model, then handing a context file to Claude Code, is a related token-saving variant. → *Try drafting the ProsHarness plan stage in a cheaper chat model with web search, hand Claude Code a rules file, and measure whether Claude Code token use drops before the plan-critique loop runs.*
