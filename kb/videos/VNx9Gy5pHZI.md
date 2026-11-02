# This is How I Design With Stitch Now

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `VNx9Gy5pHZI` · [watch](https://youtu.be/VNx9Gy5pHZI) · **date:** 2026-02-02 · **length:** 9:07 · **format:** tutorial · **quality:** 3/5 · **depth:** practitioner
- **speakers:** ? · **orgs:** Google, Vercel
- **topics:** coding-agents, mcp-and-tools, testing-verification, vibe-coding-app-building · **tags:** google-stitch, stitch-mcp, mcp, claude-code, plan-mode, claude-md, ui-design, nextjs, vercel-agent-browser, browser-testing, accessibility-tree, snapshots, gemini, vibe-coding

> A Stitch-as-MCP design workflow in Claude Code: plan first, generate one long landing page, pull its HTML, then test with Vercel's snapshot-based Agent Browser. The Stitch MCP wrapper is unofficial.

## Summary
Google's Stitch design tool can now be connected as an MCP, so an agent can create projects, list and fetch screens, and generate designs from text prompts. The official setup is lengthy (Google Cloud SDK, two logins, enabling the Stitch API in a GCP project), so the speaker uses a community "Stitch MCP" wrapper that automates it, which he calls unofficial and experimental. His workflow starts in Claude Code plan mode, where he has Claude write a UI guide that avoids generic AI styling, then refines that plan heavily before any implementation. Stitch first generated the landing page section by section, so he had Claude write one long page prompt instead. Claude then retrieved the screen code through the GetScreen tool's download links, dumped it into a single file, and needed a follow-up refactor into components. For testing, he uses Vercel's Agent Browser, a CLI that works from accessibility-tree snapshots instead of screenshots, and a CLAUDE.md rule requires it for all UI testing. The agent tested the whole app in about four minutes and fixed a code editor that was not editable. The video also promotes the creator's paid AI LABS Pro community, where the rules and source are offered.

## Key ideas
- **Stitch can be driven by an agent through MCP** — The Stitch MCP lets the agent create and manage projects, list and fetch screens, and generate designs from a text prompt, so the speaker no longer hand-writes Stitch prompts. ([0:00](https://youtu.be/VNx9Gy5pHZI?t=0))
- **The official Stitch setup is heavy, and a community wrapper hides it** — Official setup means installing the Google Cloud SDK, logging in twice (as a user and as an application), and enabling the Stitch API in a GCP project that the designs bill against. The community Stitch MCP automates all of this, but the speaker says it is unofficial and experimental. ([1:04](https://youtu.be/VNx9Gy5pHZI?t=64))
- **Plan the UI in Claude Code plan mode before generating anything** — He asks for a UI guide that avoids generic AI-looking design and reads and edits the plan until satisfied. He says reviewing the plan thoroughly is essential before implementation. ([2:19](https://youtu.be/VNx9Gy5pHZI?t=139))
- **Section-by-section generation fragments a landing page** — Stitch got one prompt per section, which he expected to cause integration trouble. Asking Claude to write one long prompt for the whole page produced a coherent design that kept the section ideas. ([3:46](https://youtu.be/VNx9Gy5pHZI?t=226))
- **Stitch output comes back as downloadable code links, not inline code** — The GetScreen tool returns download links for the screen code. Claude fetched them with curl and got the HTML, then placed the design into a Next.js project. ([4:56](https://youtu.be/VNx9Gy5pHZI?t=296))
- **Agent-generated code is often dumped into one file, so ask for a component refactor** — Claude put the implementation in mainpage.tsx as a single file. A follow-up request to restructure it into components fixed the organization. ([5:30](https://youtu.be/VNx9Gy5pHZI?t=330))
- **Snapshot-based browser testing is faster than screenshot-based testing** — Agent Browser snapshots the page as an accessibility tree tagged with selectors. It runs in a separate browser, so it cannot use the user's logged-in sessions. The speaker says a full-page snapshot approach tested the whole app in about four minutes. ([6:20](https://youtu.be/VNx9Gy5pHZI?t=380))
- **Rules in CLAUDE.md can force the agent to use a specific test tool** — The speaker adds CLAUDE.md rules to use agent-browser for all testing and to consult the help command when unsure of a command. He then runs the browser in headed mode to watch it work. ([7:39](https://youtu.be/VNx9Gy5pHZI?t=459))

## Techniques
- **Stitch MCP for agent-driven design generation** — Connect a Stitch MCP to Claude Code. The official route is to install the Google Cloud SDK (the speaker used brew on a Mac), log in as user and as application, and enable the Stitch API in a GCP project. The community Stitch MCP does this setup for you. Then have Claude create a project, identify it by project ID, and send one detailed design prompt. *When:* You want the coding agent to drive design generation directly instead of copying prompts between tools.
- **Plan-mode UI guide before design** — In Claude Code plan mode, give the app idea and ask for a UI guide with an explicit constraint against generic AI-looking design. Read the whole plan, ask for changes repeatedly, and only hand off once it matches what you want. *When:* Starting a greenfield UI where the default AI look would be a problem.
- **One long page prompt instead of per-section prompts** — If the design tool returns sections separately, ask the agent to write a single detailed prompt that covers the entire page while keeping each section's ideas. Generate the page as one design. *When:* The page will ship as one implementation, so separate section designs will not integrate cleanly.
- **Pulling Stitch screen code into a project** — Ask the agent to call the GetScreen tool. Use the downloadable links it returns and fetch them with curl to get the HTML. Port that HTML into the framework project, here Next.js. *When:* Moving a Stitch design into a real codebase.
- **Follow-up refactor after code dump** — After the agent places generated UI into one file, ask it to reorganize the code into a component structure. The speaker's example is breaking one page file into components and pages. *When:* Agent output is monolithic and needs to match the framework's conventions.
- **CLAUDE.md rules that mandate a test tool** — Add CLAUDE.md rules that say to use agent-browser for all kinds of testing, and to run its help command whenever it does not know a command. Use headed mode when you want to watch the run. *When:* You want the agent to test the UI reliably with a specific tool rather than choosing one each time.
- **Snapshot-driven UI testing with Vercel Agent Browser** — Install Agent Browser globally with its install command (the command is not shown in the video). Run help to list commands. Take a full-page snapshot to get the accessibility tree with selectors. Use selectors with the click and type commands to drive the UI, and check the layout. The speaker's example edited a code editor's content after locating its selector. *When:* Fast verification of UI behavior on Chromium browsers, where you do not need the user's existing logged-in session.

## Numbers
- Full-app testing run by the agent with Agent Browser took about 4 minutes ([7:39](https://youtu.be/VNx9Gy5pHZI?t=459))
- The official Stitch setup needs two logins (user and application) and enabling the Stitch API in a GCP project ([1:04](https://youtu.be/VNx9Gy5pHZI?t=64))
- The first landing-page section was generated with Gemini 3 Flash ([3:46](https://youtu.be/VNx9Gy5pHZI?t=226))

## Hot takes
- Agent Browser has better features than Claude's Chrome extension, Playwright, and Puppeteer. This is an unbenchmarked opinion; the only evidence is one 4-minute run.
- Claude's Chrome extension has been surpassed as a browser-testing tool. This is asserted, not shown.
- He prefers Gemini's design capabilities over Claude's models for design work.
- The Stitch MCP wrapper is unofficial and experimental, and he says so himself.
- Plugs for the AI LABS Pro paid community at 1:04, 2:19 and 7:39. The rules and source files are gated behind it. Not a sponsor segment, but the workflow details are partly held back.

## Tools mentioned
Google Stitch, Stitch MCP (community, unofficial), Google Cloud SDK / gcloud CLI, Homebrew (brew), Claude Code (plan mode, CLAUDE.md), Gemini 3 Flash, Next.js, curl, Vercel Agent Browser, Claude's Chrome extension (compared), Playwright (compared), Puppeteer (compared)

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps Claude Code and uses plan-first workflows. The video shows plan-mode-first, then a CLAUDE.md rule that mandates one verification tool, which is a pattern a harness could enforce. → *Try a CLAUDE.md rule that mandates a specific UI verification tool for UI tasks, and check whether ProsHarness's plan-to-execute loop can enforce the same rule.*
