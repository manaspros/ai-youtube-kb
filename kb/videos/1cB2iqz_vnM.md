# How I Build Beautiful Websites With AI

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `1cB2iqz_vnM` · [watch](https://youtu.be/1cB2iqz_vnM) · **date:** 2025-11-02 · **length:** 10:25 · **format:** tutorial · **quality:** 2/5 · **depth:** practitioner
- **speakers:** AI LABS host (unnamed, on-screen presenter) · **orgs:** Lumi (sponsor), TweakCN
- **topics:** claude-code, coding-agents, vibe-coding-app-building, context-engineering · **tags:** drawbridge, browser-extension, visual-editor, task-queue, slash-commands, claude-md, landing-pages, shadcn, tweakcn, client-prototyping, cursor, localhost

> Walkthrough of Drawbridge, an open-source Chrome extension that turns clicks on a localhost page into a queued task list for Claude Code or Cursor, with landing-page and client-prototyping use cases. Main takeaway: UI fixes become batched, position-aware agent tasks.

## Summary
The host introduces Drawbridge, a Chrome extension that lets you click elements on a localhost web app, describe the change, and queue it in a to-do/doing/done list. Tasks are written into a `.mode` folder in the project (a tasks markdown file with element, required change and page position, plus a task-details JSON). A workflow rule tells the coding agent to work through the tasks one at a time and update their status. In the demo, Cursor failed to find the workflow rule, so the host copies it into a Claude Code slash command, keeping the task files beside it. Claude Code then completed four queued UI edits (remove a sidebar section, turn a label into a button, swap an icon, rename a header) without the host re-describing elements. The video closes with two use cases: building landing pages section by section from text, with a DESIGN language file and a shadcn theme from TweakCN, and sharing the UI with clients so they can mark up changes. Note that the screenshot feature was broken at recording time, and about 40 seconds of the video is a sponsor read.

## Key ideas
- **The core problem is that agent-built sites have many small UI mistakes, and fixing them one prompt at a time is slow.** — Drawbridge's answer is to pick elements on the live page and queue the changes as tasks, so the agent can batch them. ([0:00](https://youtu.be/1cB2iqz_vnM?t=0))
- **Element selection replaces describing the UI in words.** — You open the extension (or press C), click any element, and write the change. It is added to the to-do list. The screenshot attachment feature was not working at recording time. ([1:07](https://youtu.be/1cB2iqz_vnM?t=67))
- **Tasks persist as files in the project, and a workflow rule drives the agent.** — Connecting a project folder creates a `.mode` folder with tasks.md (element, required change, page position) and a task-details JSON. A workflow rule file tells the agent to process tasks one by one and track status. ([2:28](https://youtu.be/1cB2iqz_vnM?t=148))
- **The workflow rule failed in Cursor but worked in Claude Code.** — The host's Cursor attempts could not find the .mdc rule. Converting it to a Claude Code slash command worked, but only after the task files were kept beside the command folder, not moved away from it. This is one demo and the host's own view. ([3:35](https://youtu.be/1cB2iqz_vnM?t=215))
- **Position-aware batching is the main productivity claim.** — Claude completed four queued tasks in order and summarized each one. The host says it never had to explain which element each task meant. This is a single demo, not a measured comparison. ([5:03](https://youtu.be/1cB2iqz_vnM?t=303))
- **Setup needs a localhost app, a loaded Chrome extension and a connected folder.** — Drawbridge refuses to open on non-localhost pages. The host recommends Claude Code over Cursor and says Cursor needs the two task files specified manually. ([6:09](https://youtu.be/1cB2iqz_vnM?t=369))
- **Landing pages work well when built section by section from text.** — The host queued five sections (hero, social proof, problem/solution, features, how it works) as separate tasks, each with height and content notes, and the agent built them. Real apps need integration, so the host says landing pages suit this best. ([7:35](https://youtu.be/1cB2iqz_vnM?t=455))
- **A design-language file in CLAUDE.md plus a shadcn theme sets the visual style.** — The host wrote the desired look into a design-language markdown file, referenced it from CLAUDE.md, and used a theme from TweakCN. Text and colours were pulled from that theme. ([8:42](https://youtu.be/1cB2iqz_vnM?t=522))
- **Clients can mark up a prototype directly.** — The host proposes giving clients the extension so they can select boxes and type requested changes, which then go to the agent. This is a proposed workflow, not a tested client result. ([9:49](https://youtu.be/1cB2iqz_vnM?t=589))

## Techniques
- **Install Drawbridge as an unpacked Chrome extension** — Clone the Drawbridge repo. In Chrome's extensions page, choose 'Load unpacked' and select the `mode chrome` folder inside the clone. Open the extension from the extensions tab, then use its option to connect the project folder that runs on localhost. This creates the `.mode` folder. *When:* Before any UI-fix session. The app must run on localhost, because the extension refuses other origins.
- **Queue element-level UI changes** — Open the extension, press the new button or the C key, click the element, and type the change (for example 'change Documents to Dashboard'). Submit to add it to the to-do list. Move items through to-do, doing and done. *When:* When the agent keeps missing small visual or text fixes that would take many prompts to describe.
- **Have the agent process the queue** — The `.mode` folder holds tasks.md (element, required change, position on page) and a task-details JSON. The workflow rule tells the agent to take tasks one at a time and update their status. Run it in one pass to batch several changes. *When:* After you have queued several changes and want them done without re-explaining each element.
- **Turn the Cursor workflow rule into a Claude Code slash command** — Copy the Drawbridge workflow `.mdc` rule file. Create a `claude` folder in the project with a `command` subfolder (captions say 'cloud folder with a command subfolder'). Put the workflow file there, rename it from `.mdc` to `.md`, and save. Keep the task files (tasks.md and the task-details JSON) beside the command folder, not inside it. Run the slash command once per chat to load the task data. *When:* When Cursor cannot find the Drawbridge rule and you want Claude Code to run the same task loop.
- **Build a landing page section by section** — Make one task per section (hero, social proof, problem/solution, features, how it works). Give each a height and the content it needs. Submit them as a batch. Later, select individual elements and comment changes in batches. *When:* For marketing or landing pages made mostly of independent sections. The host says real apps with connected interfaces suit it less well.
- **Keep a design language in files the agent reads** — Write the target look into a designlanguage.md file. Reference it from CLAUDE.md. For shadcn projects, copy a theme from TweakCN; the host says the agent adapts it to other components too. *When:* When you want consistent styling across agent-built pages without restating it in every prompt.

## Numbers
- Three tasks were already in the to-do list at the start of the demo. ([1:07](https://youtu.be/1cB2iqz_vnM?t=67))
- Four queued tasks were completed in one Claude Code pass. ([5:03](https://youtu.be/1cB2iqz_vnM?t=303))
- Five landing-page sections (hero, social proof, problem/solution, features, how it works) were described as separate tasks. ([7:35](https://youtu.be/1cB2iqz_vnM?t=455))
- Video length is 10:25. The Lumi sponsor read runs about 0:40 to 1:20. No benchmark or cost figures are given. ([0:00](https://youtu.be/1cB2iqz_vnM?t=0))

## Hot takes
- Sponsored segment (Lumi, roughly 0:40 to 1:20) caps quality at 2 under the rubric.
- The host says the repo's low star count is unfair given how useful it is. This is opinion, not evidence.
- Cursor failures are one anecdote from the host (tried two or three times). The claim that Claude Code 'performs much better' rests on this single demo.
- The screenshot-attachment feature was broken during recording, which the host attributes to low adoption without evidence.
- Drawbridge only works on localhost pages, which limits it to local dev workflows and rules out production or staging sites.

## Tools mentioned
Drawbridge (open-source Chrome extension and visual editor for coding agents), Chrome (extensions, load unpacked), Cursor, Claude Code, shadcn/ui, TweakCN (shadcn theme site), Lumi (sponsored AI website builder), Git (used to revert the demo project)

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps Claude Code CLI with checkpoint/resume and loops. A queued-task file that the agent works through with status updates is a similar pattern, but this is a UI-editing tool, not a harness. → *Compare Drawbridge's tasks.md plus status-tracking workflow rule with ProsHarness checkpoint state to see whether a human-queued task file is a simple input format worth adding.*
