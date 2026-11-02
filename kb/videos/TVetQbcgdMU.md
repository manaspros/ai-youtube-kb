# Anthropic Claude AI Agentic Browser: The Claude Chrome Extension for Builders (EXCLUSIVE DEMO)

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `TVetQbcgdMU` · [watch](https://youtu.be/TVetQbcgdMU) · **date:** 2025-11-02 · **length:** 9:04 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** AI LABS host (name not given in transcript) · **orgs:** Anthropic, AI LABS
- **topics:** coding-agents, testing-verification, voice-multimodal · **tags:** claude-chrome-extension, browser-agent, visual-testing, slash-command, per-task-review, dev-server, computer-use, permissions, research-preview

> Hands-on demo of Anthropic's Claude Chrome extension as a visual-testing partner for Claude Code: a slash command reviews each finished task on a running dev server, and the browser agent reports visual and functional issues.

## Summary
The host, a Max Plan early-access user, builds a canvas-editor front end with Claude Code (Next.js, 8 task docs) and then uses the Claude browser extension to test each completed task visually. A custom review slash command reads the last completed task and produces testing requirements and visual feedback prompts, which the host pastes into the browser agent running against the dev server. The agent catches visual issues a code-only review misses, such as icons flush against a border with no padding and category colors not rendering, and proposes prioritized (high/medium/low) improvements before the next task. The host also runs the review over tasks 2 to 4 in one pass, which takes longer but yields more detailed feedback. The extension asks permission for every action, offers per-site allowlists, and is still in research preview; the host lists MCP integration and shared memory as missing features. The video is a single-user workflow demo with no measured time or bug-count results.

## Key ideas
- **Visual bugs need a browser agent that can see the page. The host argues that issues like icons stuck to a border with no padding are only caught by visual inspection, so the browser agent is used as a visual QA step after code-level work passes.** — The first task had no functional bugs but had layout problems. This is the reason the host picked a canvas editor, which has many visual elements. ([1:17](https://youtu.be/TVetQbcgdMU?t=77))
- **Per-task review loop. After each completed task, a review slash command reads the task's status and produces testing requirements and visual feedback requests for the browser agent. This keeps review tied to what was just built.** — The host says the command 'examines the last completed task' and can use the status tracked in the task files. The output is a prompt the host copies into the browser session, which runs against the running dev server. ([2:19](https://youtu.be/TVetQbcgdMU?t=139))
- **Start a fresh chat per task to avoid context overflow. The host exits the chat and starts a new one before running the review, so the review does not inherit a bloated context.** — This is the only context-management step mentioned. The video gives no token counts. ([2:19](https://youtu.be/TVetQbcgdMU?t=139))
- **Review findings are prioritized and the agent asks before moving on. The review returns high, medium and low priority suggestions, and asks whether to do the next task or apply the improvements first. The host chose the improvements first.** — One example is keyboard shortcuts for power users. The improvements were implemented before task 2. ([3:38](https://youtu.be/TVetQbcgdMU?t=218))
- **Batch review is slower but more detailed. The host ran the review over tasks 2, 3 and 4 together, which took longer and produced more detailed feedback, and it caught a bug where category colors did not display.** — The fix was proposed and implemented right away. The host presents this as a continuous improvement loop, but gives no before/after numbers. ([3:38](https://youtu.be/TVetQbcgdMU?t=218))
- **The browser agent works through a Claude-style tool set, like Claude Code does. The host says the extension has screenshot, click, type, wait, keyboard-shortcut and read/find/form-fill tools, and that the Claude 4 models were trained for tool use.** — The host lists the tools by asking the agent to enumerate them. He says the approach is similar to Claude Code's agent tool design, but gives no internals. ([6:09](https://youtu.be/TVetQbcgdMU?t=369))
- **Permission gating per action with a per-site allowlist. The extension asks to allow or deny every command, but the user can approve all actions for specific sites, and the settings keep a list of approved sites.** — Hallucinations are still possible, so the host says every action needs a human check. This is the only safety mechanism described. ([7:24](https://youtu.be/TVetQbcgdMU?t=444))

## Techniques
- **Per-task visual review slash command** — Create a slash command that takes the last completed task (from the task doc status), lists what must be tested and which visual elements need feedback, and outputs a prompt for a browser agent. The prompt is pasted into the browser session, which is pointed at the running dev server. The command's exact text is not shown in the video. *When:* When an agent builds UI in task-sized steps and code-level review misses layout or visual bugs.
- **Fresh chat per task** — Exit the current chat and start a new one before each review or implementation step to limit context growth. *When:* Long multi-task builds where the agent's context fills up with earlier work.
- **Prioritized improvement triage before the next task** — Ask the review to rank findings as high, medium or low. Then choose whether to apply the improvements before continuing the task list. *When:* When each task's feedback should be fixed before compounding into later tasks.
- **Batch review of several tasks** — Pass several completed task docs to one review run (the host did tasks 2 to 4 together). Expect longer runs and more detailed feedback. *When:* When you want a broader test pass across several finished tasks and can accept slower runs.
- **Per-site approval allowlist for browser actions** — Approve each action on first use, or approve all actions for a specific site, and keep the site on the approved list in settings. *When:* When an agent browses with your logged-in accounts and you want to limit the approval surface to trusted sites.

## Numbers
- About 1,000 Max Plan users got early access to the browser extension. ([0:00](https://youtu.be/TVetQbcgdMU?t=0))
- The demo project had 8 generated task docs. The host asked for 8 tasks, and the model produced 8 basic tasks. ([1:17](https://youtu.be/TVetQbcgdMU?t=77))
- The review covered tasks 2, 3 and 4 in one batch, taking longer than the single-task review. ([3:38](https://youtu.be/TVetQbcgdMU?t=218))
- The video is 9:04 long. There are no latency, token-cost or bug-count measurements. ([0:00](https://youtu.be/TVetQbcgdMU?t=0))

## Hot takes
- The 'exclusive demo' title oversells a single-user demo. The video offers no measured time savings, bug counts or comparisons with Playwright-based visual tests.
- The host calls the browser agent a builder tool, but the workflow depends on a human copy-pasting prompts between the review command and the browser session. The host admits MCP integration would remove that step.
- The host expects a Pro and Max launch and possible limited free access. These are speculation, not Anthropic announcements.
- Visual review catching real layout bugs (padding, color rendering) is the strongest evidence in the video. The per-action permission model is a reasonable safety default, but the host gives no failure cases.
- Quality is capped at 3 rather than higher because the substance is one concrete workflow with no data behind it, and the framing is promotional.

## Tools mentioned
Claude Code, Claude Chrome extension (Claude browser extension, research preview), Claude 4 series models, Next.js, GPT (used to brainstorm the app idea), BMAD method (mentioned, not used), Playwright MCP (compared, not used), Cursor (mentioned as a competitor)

## Relevance to our work
- **prosharness** (2/3): ProsHarness runs Claude Code in checkpointed tasks. A per-task review command that checks the running app and gives prioritized feedback before the next checkpoint fits that loop, and the per-site allowlist resembles phone-driven approvals. → *Prototype a per-task checkpoint hook in ProsHarness that runs a browser-based visual check against the dev server and gates the next task on high-priority findings.*
- **agentos** (1/3): Browser actions with per-site allowlists and per-action approval are a small example of scoped tool permissions, which is related to Crucible's exec-gate guardrails. → *Look at how Crucible's exec-gate could use per-site or per-tool allowlists with per-action approval for agent browser or code actions, instead of blanket permissions.*
