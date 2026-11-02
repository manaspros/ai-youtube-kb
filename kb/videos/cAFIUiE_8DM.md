# How I Build Apps 10x Faster with this 7-Step Cursor Workflow

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `cAFIUiE_8DM` · [watch](https://youtu.be/cAFIUiE_8DM) · **date:** 2025-11-02 · **length:** 11:55 · **format:** tutorial · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Cursor, Anthropic, OpenAI, Supabase, Apple
- **topics:** coding-agents, vibe-coding-app-building, context-engineering · **tags:** cursor, claude-code, html-prototype, design-json, swiftui, supabase, supabase-mcp, mvp, git-commits, ai-app-builder, image-generation, rules-files

> A solo builder walks through a seven-step AI app workflow (idea, MVP, HTML prototype, design.json styling, SwiftUI conversion, Supabase backend, UI polish) for an iOS habit app, using Cursor and Claude Code.

## Summary
The creator builds an iOS productivity app called Sage with AI tools and presents the process as a seven-step workflow. Ideation happens in a general chat model, then the MVP structure is saved to a structure.md file in a docs folder. The layout is locked first in a plain HTML prototype, and only then is visual style applied from a design.json generated from a reference image, with the layout explicitly frozen. The HTML is converted to SwiftUI using a conversion-rules file that a chat model wrote with web search enabled, placed into Cursor rules. Supabase is added through its MCP server, which the creator says handled project creation and auth setup in about 15 minutes. Most of the remaining time went into UI polish and animation, which he moved to Claude Code. The title and intro make strong productivity claims, but the only measurements are his own anecdotal time estimates.

## Key ideas
- **Lock the app structure in a plain HTML prototype before any styling. HTML needs no dependencies, and the creator says it is the easiest format for an LLM to output and revise.** — He asks the coding agent to turn the MVP structure into an HTML prototype, then iterates on structure only (buttons vs. text vs. widgets vs. progress bars), using screenshots of what is wrong. Colors and design come later. ([4:46](https://youtu.be/cAFIUiE_8DM?t=286))
- **Define the MVP as the smallest version that tests the core idea. He had the chat model draft three pages, then added login and a cover page, then removed elements it had added unprompted.** — The final MVP outline is pasted into docs/structure.md in Cursor, and that file becomes the basis for the prototype. ([3:53](https://youtu.be/cAFIUiE_8DM?t=233))
- **Style the locked layout from a generated design.json instead of hand-styling each component. The chat model turns a reference screenshot into a JSON file of visual tokens, which is placed in the project directory.** — He says the prompt told the agent to apply design.json to the HTML prototype while forbidding any layout change, and the result matched the inspiration colors. ([5:57](https://youtu.be/cAFIUiE_8DM?t=357))
- **Finalize colors and visual elements before the native port. He says skipping this cost him time: a redesign during the iOS build took 7 hours where he estimates 5 would have sufficed.** — Effects and animations are deferred to later; the design pass is about how the app looks, not how it feels to use. ([6:30](https://youtu.be/cAFIUiE_8DM?t=390))
- **Convert the HTML prototype to a native app using a rules file rather than a one-shot prompt. He asked a chat model (with web search on for less-known frameworks) to write conversion rules between the two formats, then loaded those rules into Cursor.** — He reports the agent converted the prototype to SwiftUI with the same pages and mostly unchanged design, with only iOS-specific component differences. ([7:18](https://youtu.be/cAFIUiE_8DM?t=438))
- **Backend setup can be delegated almost entirely to an MCP server. He says the Supabase MCP created the project, the schema and auth, and Cursor installed the SDK and integrated it in about 15 minutes.** — He also wrote a data-structures doc and had Cursor scan the app to determine the tables. Supabase's free tier, with three projects, was the database choice. ([8:24](https://youtu.be/cAFIUiE_8DM?t=504))
- **Polish takes the most time. He moved from Cursor to Claude Code for animations because he judged it better at complex reasoning. He says the UI has taken about 3 hours so far, and a polished version could take a week or more.** — His claim is that single prompts do not yield good UI; the work is many small tweaks, animations and effects. The app icon was made with an image model by uploading the prototype icon and asking for improvements. ([9:26](https://youtu.be/cAFIUiE_8DM?t=566))

## Techniques
- **Stage-gated AI app build** — Run the work in fixed stages, each committed to git: (1) ideate in a chat model, (2) write the MVP page list to docs/structure.md, (3) build an HTML prototype and fix structure only, (4) apply a design.json for visuals with an explicit no-layout-change instruction, (5) convert to the target framework, (6) add backend, (7) polish. He says git commits per stage let him reproduce the build history. *When:* Greenfield single-developer app builds where you want a reviewable checkpoint at each stage and want to change one concern at a time.
- **Screenshot-driven correction loop** — When the agent's output has the right elements in the wrong form, attach a screenshot and state explicitly what is wrong and what it should be, e.g. a full widget rather than a small progress bar. *When:* Early prototype stage, when structure is right on paper but the rendered layout is not.
- **design.json from a reference image** — Give a chat model a UI inspiration image plus a prompt asking for a JSON file of visual data to reproduce the design. Save it in the project directory. Then prompt the coding agent to apply design.json to the HTML prototype while forbidding any change to the layout. He says he has tested this several times and it works. *When:* When you want a consistent visual style without hand-styling each component, and the layout is already frozen.
- **Rules-file-driven framework conversion** — Ask a chat model, with web search on for less-known frameworks, to write conversion rules from the source format to the target (here HTML to SwiftUI). Place those rules in the agent's rules file (Cursor rules) and set them to be followed, then reference the rules file at the top of the conversion prompt. *When:* Porting a working prototype to another stack where the target framework is unfamiliar to you or the agent.
- **MCP-based backend provisioning** — Add the Supabase MCP server to the coding agent. Write a data-structures document, have the agent scan the app to infer tables, then let the agent call the MCP to create the project, tables, auth, and install the SDK. Previously you wrote SQL and pasted it into the dashboard by hand. *When:* Adding Postgres and auth to a small app with a managed backend and no custom server.
- **Image model for app icon iteration** — Upload the current icon from the prototype to an image model and give specific improvement instructions. He also mentions adding dark-mode and tinted icon variants in Xcode's asset catalog. *When:* Producing an app icon without a designer.
- **Model switching by task** — Use Cursor for most edits and switch to Claude Code for animations and complex reasoning-heavy UI work. *When:* When the first tool stalls on a class of task, such as animation work.

## Numbers
- The AI tools cost about $20 per month. ([0:00](https://youtu.be/cAFIUiE_8DM?t=0))
- Supabase gives three free projects. ([8:24](https://youtu.be/cAFIUiE_8DM?t=504))
- Supabase MCP plus Cursor did database, auth and SDK integration in about 15 minutes. ([9:26](https://youtu.be/cAFIUiE_8DM?t=566))
- UI refinement so far has taken about 3 hours; a perfect app could take a week or more. ([10:32](https://youtu.be/cAFIUiE_8DM?t=632))
- Without AI, the creator estimates the build would have taken a month or two. ([10:32](https://youtu.be/cAFIUiE_8DM?t=632))
- The iOS redesign took 7 hours where 5 was expected, due to skipping the color/design finalization step. ([5:57](https://youtu.be/cAFIUiE_8DM?t=357))
- Habit rules: over 50% of points turns the progress bar blue; over 90% earns the purple achievement. ([1:27](https://youtu.be/cAFIUiE_8DM?t=87))

## Hot takes
- The title claims 10x faster, but no baseline or measurement supports that beyond the creator's own rough estimate of one month or two without AI.
- The 'zero work' Supabase setup claim covers only one 15-minute anecdote on a simple app.
- The video is a generic AI-app-builder walkthrough with little that is specific to Cursor or Claude Code. Most of the value is the stage ordering (structure before style, style before port) rather than tool-specific technique.
- Claims like 'can generate thousands' and 'apps that make real money' are unsupported.

## Tools mentioned
Cursor, Claude Code, Claude (chat), ChatGPT, OpenAI image generation model, Supabase, Supabase MCP server, Supabase SDK, SwiftUI, Swift, Xcode, Next.js (mentioned as an example template), Git

## Relevance to our work
- **prosharness** (1/3): Shows a staged, commit-per-stage Claude Code workflow and a rules file that an agent loads before a mechanical conversion. Only loosely related to ProsHarness checkpointing. → *Consider keeping a per-stage rules file for ProsHarness-driven runs, and check whether a checkpoint per stage matches the resume model.*
