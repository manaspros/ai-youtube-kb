# Trae AI: The New Cursor AI Alternative

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `cdLnorNbewA` · [watch](https://youtu.be/cdLnorNbewA) · **date:** 2025-11-02 · **length:** 6:59 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Unnamed narrator (AI LABS channel host) · **orgs:** ByteDance
- **topics:** coding-agents, vibe-coding-app-building, testing-verification · **tags:** Trae, ByteDance, IDE, VS Code fork, Claude 3.5 Sonnet, Cursor comparison, Windsurf, screenshot-to-code, React, Tailwind CSS, PostCSS, agent workflow, hands-on review

> Hands-on test of Trae, ByteDance's VS Code-fork IDE with a single-agent workflow and free Claude access; a to-do app and a Spotify screenshot clone show a basic UI with missing-config errors, verdict "hype".

## Summary
The video tests Trae, a new VS Code-fork IDE from ByteDance that offers free Claude usage and markets a main agent that delegates to smaller agents. The reviewer finds the UI cleaner than Cursor's but notes that only Claude 3.5 Sonnet is available and that users cannot choose models per task. The built-in to-do list example generates an app where task text is invisible, which the reviewer scores as a fail, while other features work. A Spotify screenshot clone looks rough at first, improves over several iterations, and needs images supplied manually. Much of the struggle came from a missing Tailwind/PostCSS configuration that the agent only identified after repeated prompting. The reviewer concludes the agent-based workflow is rigid, error-prone and inferior to Cursor, so Trae feels more like hype than a reliable tool.

## Key ideas
- **Trae is pitched as a single main agent that automatically assigns work to smaller agents, with no per-task model choice.** — The site describes an agent-based workflow where one agent controls several agents. The reviewer says users cannot pick models or use different LLMs per use case, and calls the workflow rigid. ([0:00](https://youtu.be/cdLnorNbewA?t=0))
- **Free Claude access is the main draw, but only Claude 3.5 Sonnet is offered at review time.** — The reviewer notes the GPT-4.0 model the makers had promised is absent. The free-usage perk is called a nice perk, not a differentiator. ([2:40](https://youtu.be/cdLnorNbewA?t=160))
- **The built-in to-do app example generated a broken task card: the task name never renders.** — Add, complete, and delete work, but the text is invisible, so the reviewer scores the test as a fail. The example is noted as pre-baked, so it is weak evidence of real coding performance. ([2:40](https://youtu.be/cdLnorNbewA?t=160))
- **The agent runs terminal commands on approval and applies file edits as reviewable changes.** — It asks permission for dependency installs and for starting the dev server, and the user accepts file changes with Accept All. Edits and commands are gated by the user at each step. ([2:40](https://youtu.be/cdLnorNbewA?t=160))
- **A Spotify screenshot clone starts bare and improves only through several prompt iterations.** — The first output barely resembles the target site. Animations are inferred from the screenshot, and images must be supplied manually, so the clone is not fully self-sufficient. ([4:04](https://youtu.be/cdLnorNbewA?t=244))
- **The agent's 'done' state hid a missing Tailwind/PostCSS setup, found only after repeated prompting.** — Tailwind CSS was not properly installed and postcss.config.js was missing. Styling broke until the configuration was fixed, showing that generated apps need a check beyond the agent's own report. ([5:29](https://youtu.be/cdLnorNbewA?t=329))
- **Verdict: the end result looks good, but reliability and the rigid agent flow make the IDE frustrating; Cursor is the better experience.** — The reviewer concedes the final clone looks spot-on, but counts many errors and limited flexibility against the product's promises. ([6:50](https://youtu.be/cdLnorNbewA?t=410))

## Techniques
- **Screenshot-to-app clone prompt** — Open a project folder in Trae, attach a screenshot in the AI chat, and ask it to clone the screenshot into a fully functional app. The agent lists dependencies, asks to run install commands, creates the React project and files one by one, then you review and click Accept All before starting the dev server. *When:* Quick prototyping from a design screenshot where you will iterate heavily and check every page manually. Only the page in the screenshot was cloned; other routes did not work.
- **Built-in web view preview** — After the dev server starts, open the app in the editor's web view panel instead of a separate browser tab for a quick look. *When:* Fast visual checks during an agent-driven build loop without leaving the IDE.
- **Manual behavioural check of agent output** — Write a task in the generated to-do app, toggle complete, and delete, then confirm each visible result. Verify UI text and styling, not only that the server starts. *When:* Before trusting any agent-generated app. The reviewer caught an invisible-text bug this way.
- **Config-first debugging for missing styles** — When Tailwind styling is absent, check that the Tailwind install and postcss.config.js exist rather than re-prompting about the UI. The fix was to add the missing configuration. *When:* Generated React/Tailwind projects where the agent claims success but the styles do not apply.

## Numbers
- Only one model (Claude 3.5 Sonnet) is available in Trae at review time, with GPT-4.0 absent. ([2:40](https://youtu.be/cdLnorNbewA?t=160))
- The to-do app example has 1 major failure (task name not visible) out of the features tested; add, complete, and delete work. ([2:40](https://youtu.be/cdLnorNbewA?t=160))
- The video runs about 7 minutes (6:59) and has no benchmarks, latency, or cost figures. ([0:00](https://youtu.be/cdLnorNbewA?t=0))

## Hot takes
- Trae is 'more like hype than a reliable tool' (reviewer's verdict).
- Cursor offers a much better experience than Trae.
- Single-agent, auto-assigned workflow with no per-task model choice is too rigid.
- Built-in example apps are pre-baked, so they do not show real coding performance.
- Free Claude usage is a nice perk but does not fix the IDE's reliability.
- Trae's UI looks better than Cursor's and does not feel like a VS Code fork anymore.

## Tools mentioned
Trae (ByteDance IDE), Claude 3.5 Sonnet, GPT-4.0 (mentioned as promised, not available), Cursor, Windsurf, VS Code, React, Tailwind CSS, PostCSS

## Relevance to our work
- **prosharness** (1/3): The agent declared a generated app ready while a Tailwind/PostCSS config was missing, which is the kind of false 'done' a ProsHarness run could miss. → *When a harness run reports success for a generated web app, add an automated smoke check (build, start the dev server, fetch the page, assert it renders) before accepting completion.*
