# Goose + Qwen3 Is INSANE — Best AI Tool I’ve Tried So Far

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `thCFAzPJBZo` · [watch](https://youtu.be/thCFAzPJBZo) · **date:** 2025-11-02 · **length:** 7:14 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andrus (Better Stack presenter) · **orgs:** Block, Better Stack, OpenRouter
- **topics:** coding-agents, context-engineering, token-cost-efficiency · **tags:** goose, qwen3-coder, openrouter, hints-file, desktop-agent, react, zustand, greenfield-apps, per-project-instructions

> Better Stack reviews Goose, Block's open-source local coding agent, paired with Qwen3 Coder via OpenRouter; three small web apps built, with a hints file steering stack choices and a few real failure modes.

## Summary
The presenter installs Goose's desktop client, points it at Qwen3 Coder through OpenRouter, and asks it to build a webcam rock-paper-scissors game with no stack specified. The agent picks MediaPipe hand detection and finishes in about three minutes. A follow-up request for animations and SQLite persistence makes Goose restructure the project around a Node.js/Express server; it works first try and the whole project costs $0.19 on OpenRouter. The presenter then shows Goose's hints file (per-project or global) that specifies React, TypeScript and Zustand, and a dog-photo favorites app is built in about two minutes. Two gaps show up: styling is poor because Goose defaults to Tailwind, which is fixed by asking for plain CSS, and the API calls are not placed in the folder the hints file requested. The review ends positive, citing the UI, provider switching, extensions, recipes and a headless mode that is not covered.

## Key ideas
- **Goose is an open-source agent from Block that runs as a CLI or desktop client and can use commercial APIs or local models through Ollama.** — The presenter frames it as Block's attempt to compete with Claude Code and Cursor, and notes it is a different project from Goose AI. ([0:00](https://youtu.be/thCFAzPJBZo?t=0))
- **With no stack specified, Goose picked MediaPipe hand detection for a webcam rock-paper-scissors game and got the gesture recognition working.** — The build took about three minutes, and the presenter reports the gameplay worked without fixes. ([1:18](https://youtu.be/thCFAzPJBZo?t=78))
- **A follow-up feature request (persistence) made Goose restructure the project into a Node.js/Express server with SQLite, and it still worked first try.** — Scores, animations and per-name profiles persisted across a refresh. The presenter reports the whole project cost $0.19 on OpenRouter. ([2:33](https://youtu.be/thCFAzPJBZo?t=153))
- **Goose supports a hints file that sets stack, structure and conventions, either per project or globally.** — The presenter used it to require React, TypeScript and Zustand plus a project layout, and the dog-photo favorites app came out using Zustand as asked. ([3:32](https://youtu.be/thCFAzPJBZo?t=212))
- **Goose has a default styling bias toward Tailwind even when not asked, and the output looked poor until the presenter requested plain CSS.** — This is the main negative in the review: the defaults override or ignore the stated preferences unless you name the alternative explicitly. ([4:57](https://youtu.be/thCFAzPJBZo?t=297))
- **The hints file was only partly followed: the API calls were not put in the api folder the hints file asked for.** — The presenter calls this minor, but it shows that written structure rules are soft constraints for the agent. ([5:40](https://youtu.be/thCFAzPJBZo?t=340))
- **Verdict: Goose plus Qwen3 Coder is strong for small greenfield apps, with a clean UI, easy model switching, extensions, recipes and a headless mode.** — The presenter says they will keep using it. The evidence is three small apps, one author, and no benchmarks or large-codebase tests. ([6:10](https://youtu.be/thCFAzPJBZo?t=370))

## Techniques
- **Point an open agent at a cheap open-weight coder via a routing gateway** — In Goose's settings, choose a provider and model. OpenRouter was used with the Qwen3 Coder model enabled. Models not in the dropdown can be typed in manually. Check spend on the OpenRouter usage page after the run; the presenter's whole project was $0.19. *When:* Cheap, greenfield prototyping where you want model choice without a single vendor lock-in.
- **Hints file for per-project or global conventions** — Write a hints file describing the stack (React, TypeScript, Zustand here), folder layout (for example, API calls in an api folder), and tools. Attach it per project, or make it global so it applies to all projects. The exact filename and location are not shown in the video. *When:* When you need the agent to follow your stack and structure instead of its defaults. Treat it as soft: verify the output against each rule.
- **Override defaults explicitly in the prompt** — If the agent defaults to something you do not want (here Tailwind for styling), ask in the next iteration for the specific alternative, such as simple plain CSS. The presenter's result looked good after that one change. *When:* When the default library choice for styling, UI or setup clashes with your preference.
- **Iterate by feature request instead of re-specifying** — Start with a one-line brief and no stack. Then ask for one added capability at a time (animations, then SQLite persistence). Goose restructures the project as needed. *When:* Fast exploration of an idea before deciding on architecture.

## Numbers
- Rock-paper-scissors webcam game built from one vague prompt in about 3 minutes. ([1:18](https://youtu.be/thCFAzPJBZo?t=78))
- Whole project with animations and SQLite persistence cost $0.19 on OpenRouter (the presenter checked the OpenRouter page). ([2:33](https://youtu.be/thCFAzPJBZo?t=153))
- Iteration that added Node.js server and SQLite took noticeably longer than the first build; no figure given. ([2:33](https://youtu.be/thCFAzPJBZo?t=153))
- React/TypeScript/Zustand dog-photo favorites app built in about 2 minutes. ([3:32](https://youtu.be/thCFAzPJBZo?t=212))
- Cost per token or per request for Qwen3 Coder on OpenRouter is not stated in the video. ([3:32](https://youtu.be/thCFAzPJBZo?t=212))

## Hot takes
- Goose plus Qwen3 Coder works well for small greenfield apps, and the presenter says it is worth continuing with it. The title's 'INSANE' overstates the evidence from three small apps by one author.
- Written hints are soft constraints: Goose ignored the requested API folder and defaulted to Tailwind until told otherwise, so per-project instructions need verification, not trust.
- Cost of $0.19 for a full project is a useful data point for token-cost comparisons, but it is a single run with no comparison to Claude Code or Cursor.
- The review says nothing about large codebases, long sessions, or failure recovery, so it does not show whether the agent holds up beyond small greenfield builds.

## Tools mentioned
Goose (Block; open-source agent, CLI and desktop client; version not stated), Qwen3 Coder (coding model, called Quen 3 Coder in the transcript), OpenRouter (model gateway used as the provider), Ollama (local model runner Goose can use; not used in this video), Anthropic, OpenAI and Gemini (commercial providers Goose can connect to; not used in this video), Goose AI (named as an unrelated project; not reviewed), MediaPipe (hand detection library the agent chose), SQLite, Node.js, Express, VS Code, React, TypeScript, Zustand (state management; spelled ZooStand in captions), Tailwind CSS, Claude Code (named as a competitor), Cursor (named as a competitor)

## Relevance to our work
- **agentos** (1/3): Goose's hints-file scoping (per project or global) is a simple version of the context-injection question. It is a single-user desktop agent, not an infra layer, so it does not change AgentOS components. → *Read Goose's hints-file docs and compare how it scopes global versus project instructions with our CLAUDE.md and context/ files before designing AgentOS prompt/context injection.*
- **prosharness** (1/3): Goose is a competing wrapper around agent CLIs and models, and its hints file is similar in purpose to the per-project config ProsHarness would need. The video shows the soft-compliance problem: stated structure rules were only partly followed. → *Add a check to ProsHarness that verifies generated project structure against written conventions (for example, API calls in an api folder), since the hints file was only partly followed in this test.*
