# 5 Ways To Build Beautiful Websites Using Claude Code

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `VGYsHicpp34` · [watch](https://youtu.be/VGYsHicpp34) · **date:** 2026-01-02 · **length:** 5:05 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Google, Anthropic, automata.dev
- **topics:** vibe-coding-app-building, coding-agents, testing-verification · **tags:** shadcn, google-stitch, claude-code, design-to-code, background-subagents, puppeteer-mcp, drawbridge, ui-design, color-palette, prototyping

> A design-first workflow for building websites with Claude Code: shadcn presets, Coolers palettes, Google Stitch designs and prototypes, background browser-testing agents, and Drawbridge for visual fixes. Partly a promo for the presenter's agency.

## Summary
The video, from the AI LABS channel, presents five tools and workflows for making websites look better when built with Claude Code. The main idea is to settle the visual design before handing work to a coding agent, so the agent does not spend repeated prompts fixing the look. The presenter starts with shadcn/ui presets for a component style, then picks a color palette in Coolers and designs screens in Google Stitch, which can also generate a clickable prototype from all screens. Reference galleries are used as inspiration, with screenshots fed to Stitch, and the finished design is exported as a zip and imported into Claude. For testing, a Puppeteer MCP browser-testing subagent can run in the background while the main agent works on other tasks, with a warning that agents consume tokens. Drawbridge is shown for pointing at UI sections and sending visual fix requests to Claude Code. The last minute is a pitch for the presenter's agency, and no demo results or measured outcomes are shown.

## Key ideas
- **Start from a visual preset rather than a blank page** — shadcn/ui's new presets feature shows sample components beside preset styles so you can pick a look before any code is written. Choosing one generates a project with that preset installed. ([0:00](https://youtu.be/VGYsHicpp34?t=0))
- **Lock the design before the coding agent starts** — The presenter argues a finished design should exist before going to the coding agent, otherwise the agent gets asked over and over to change things that do not match the intended look. ([0:55](https://youtu.be/VGYsHicpp34?t=55))
- **Pick the color theme first** — Coolers is used to compare palettes side by side. The chosen palette is exported in a usable format and fed into the design step. ([0:55](https://youtu.be/VGYsHicpp34?t=55))
- **Google Stitch designs and then prototypes the app** — Stitch (with Gemini 3 Pro Thinking and Nano Banana for generated images) produced a minimal UI with a clear balance of main and accent colors. Selecting all screens creates a clickable prototype with navigation flows inferred automatically. ([0:55](https://youtu.be/VGYsHicpp34?t=55))
- **Use reference galleries and screenshots as design input** — The presenter takes a hero section from a gallery, screenshots it, and asks Stitch to replicate that style for their own site. The design is then exported as a zip and imported into Claude. ([2:11](https://youtu.be/VGYsHicpp34?t=131))
- **Run browser testing in a background subagent** — Claude's subagents can now run in the background. A Puppeteer MCP browser-testing agent runs while the main agent works on another task, so several agents can run side by side. The presenter warns that each agent uses tokens and costs need watching. ([2:11](https://youtu.be/VGYsHicpp34?t=131))
- **Use Drawbridge to point at UI problems** — Drawbridge lets users select UI sections and send the issue to Claude Code. The presenter says it now has Claude Code integration, more precise section selection, fixed screenshots, and an automatically installed slash command. ([3:31](https://youtu.be/VGYsHicpp34?t=211))

## Techniques
- **shadcn preset import** — Open shadcn's New Project flow, compare sample components with presets, choose one, click Create Project, select the framework (React or Next.js), copy the generated install command, and run it in the project terminal. The preset is installed into the project. *When:* At the start of a React or Next.js project, to fix a component style before the agent writes UI code.
- **Palette before layout** — Use Coolers to try several colors side by side, adjust until the combination works, then export the palette in the format your tooling needs. *When:* Before any design work, so the color system is decided and reused across generated screens.
- **Design in Stitch, then hand off to Claude** — Generate screens in Google Stitch with the chosen palette. Optionally, select all screens and generate a prototype to test navigation. Export as a zip (Stitch also offers export to AI Studio, Jules, or clipboard) and import the zip into Claude Code for implementation. *When:* When the look needs to be settled before implementation, to avoid repeated style-correction prompts to the coding agent.
- **Screenshot-driven inspiration** — Find a section you like in a design gallery (the presenter used a hero section), take a screenshot, and give it to the design tool with a request to replicate that style on your own content. *When:* When you have a visual target but no design skills, such as a hero section, navbar, footer, or 404 page.
- **Background browser-test subagent** — Configure a Puppeteer MCP server for browser testing. Give the browser-test task to a subagent that runs in the background, keep the main agent on another task, and collect the subagent's output when it finishes. Track token usage as you run more agents. *When:* When UI verification is slow and can run in parallel with implementation work.
- **Drawbridge visual issue reporting** — Install Drawbridge (it integrates with Claude Code and sets up its slash command automatically). Select the UI section with the problem in the browser, describe the issue, and send it to Claude Code for a fix. *When:* When the agent repeatedly fails to fix small UI issues from text descriptions, or when the person reporting the issue is non-technical.

## Numbers
- Stitch generated its UI in about 4 minutes ("after a good 4 minutes"). No other benchmarks, costs, or token counts are given. ([0:55](https://youtu.be/VGYsHicpp34?t=55))

## Hot takes
- Mostly a tool tour: the five steps are shown as feature descriptions with no demo output, timing data, or before-and-after comparison.
- The background-subagent claim ("Claude recently fixed this") is stated without a demonstration or source.
- The closing segment (from about 3:31) is a promo for the presenter's agency with a contact address, and the video is close to a sponsored segment. Quality is capped at 2 for that reason.

## Tools mentioned
shadcn/ui, Coolers, Google Stitch, Gemini 3 Pro, Nano Banana, Google AI Studio, Jules, Claude Code, Claude subagents (background mode), Puppeteer MCP, Drawbridge, Opus 4.5 (named as context), Superhero (design gallery)

## Relevance to our work
- **prosharness** (1/3): The background-subagent pattern for long browser-verification runs runs alongside a Claude Code workflow, which is close to ProsHarness's loops and checkpointing. The video gives no mechanics or measurements. → *Check how ProsHarness schedules long UI or browser-verification tasks, and whether they could run as parallel background subagents with token budgets.*
