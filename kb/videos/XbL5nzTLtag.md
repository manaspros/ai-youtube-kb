# Coding Test: Can CLAUDE COMPUTER USE Build Apps?

- **channel:** [AI LABS](../channels/ailabs.md) · **id:** `XbL5nzTLtag` · [watch](https://youtu.be/XbL5nzTLtag) · **date:** 2025-11-02 · **length:** 4:15 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Anthropic, OpenAI
- **topics:** coding-agents, voice-multimodal, context-engineering · **tags:** computer-use, claude-computer-use-api, app-scaffolding, token-limits, prompt-chunking, node-js, npm, agent-reliability

> A short hands-on test of Claude Computer Use building a budget-manager app: it handled terminal setup but failed at front-end code generation, and a page refresh wiped the project.

## Summary
The creator gives Claude's Computer Use API a ChatGPT-written prompt to build a Budget Manager app. The full prompt took about 6 minutes and then hit the token limit. Asked to access its own site, the agent declined to sign into other websites, which the creator frames as a privacy safeguard. The agent could install Node.js and npm in the terminal and confirm their versions. The creator then split the spec into smaller staged prompts (file structure, then routing and API structure, then front end plus wiring). The file structure and routing stages went through, but the front-end prompts produced repeated errors and clashes, the agent became unresponsive, and refreshing the page wiped the whole project. The conclusion is that the tool can run terminal tasks but could not reliably generate the app's code at the time of the test, though the creator expects improvement. This is a single anecdotal run with no detail on the environment, prompts or model settings.

## Key ideas
- **A single long app-build prompt exhausted the token budget before the app was built.** — The ChatGPT-written prompt ran about 6 minutes and then the Computer Use API stopped with a token-limit error, which the creator attributes to prompt length. ([0:00](https://youtu.be/XbL5nzTLtag?t=0))
- **The agent declined a task that required signing into other websites.** — When asked to access its own site, Claude said it could not sign into other websites, and the creator calls this a useful privacy safeguard. ([0:00](https://youtu.be/XbL5nzTLtag?t=0))
- **Terminal work was the strongest capability shown.** — The agent installed Node.js and npm and verified the installed versions in the terminal. ([1:18](https://youtu.be/XbL5nzTLtag?t=78))
- **Splitting the spec into stages let the agent make progress where one big prompt failed.** — The creator broke the ChatGPT prompt into smaller pieces, grouped some of them, and fed them in order. The file structure and then routing plus API structure were set up successfully. ([1:18](https://youtu.be/XbL5nzTLtag?t=78))
- **Front-end code generation was where the run broke down.** — The front-end prompts produced errors and clashes, the agent became unresponsive, and it asked for a page refresh. ([3:07](https://youtu.be/XbL5nzTLtag?t=187))
- **Refreshing the page lost all work.** — Following the agent's prompt to refresh wiped the project clean, so nothing from the session survived. ([3:07](https://youtu.be/XbL5nzTLtag?t=187))
- **Verdict: capable at terminal tasks but not yet at generating code, with the creator expecting improvement.** — The creator concludes the tool can perform terminal tasks but cannot generate code as reliably as Claude 3.5 did, and says it could become powerful later. ([3:07](https://youtu.be/XbL5nzTLtag?t=187))

## Techniques
- **Staged prompt decomposition for agent app builds** — Turn one large spec into ordered prompts: (1) project file structure, (2) UX layout, routing and API structure plus dependency installs, (3) front end and wiring. Group small pieces when useful and send them one stage at a time, confirming each stage before the next. The creator used ChatGPT to do the split. *When:* When a single build prompt exceeds the agent's token budget or the agent stalls partway through a large generation.
- **Verify toolchain installs in the agent's terminal** — Have the agent run version checks after installing a runtime (the creator showed Node.js and npm version checks) before moving on to code generation. *When:* At the start of a computer-use or terminal-driven build, so the environment is confirmed before code generation begins.
- **Keep recoverable copies of agent-generated work outside the agent's UI** — The creator lost the whole project to a page refresh. The video does not state this fix, but the loss suggests committing or copying progress outside the agent's browser session after each stage. *When:* Whenever an agent works through a browser or UI that can hang, reset or be refreshed mid-run.

## Numbers
- First full build prompt ran about 6 minutes before hitting the token limit. ([0:00](https://youtu.be/XbL5nzTLtag?t=0))
- Video length is 4:15; the test covers one build attempt with no benchmarks or cost figures. ([0:00](https://youtu.be/XbL5nzTLtag?t=0))

## Hot takes
- The creator says Claude Computer Use is not yet able to generate code reliably, even though it handles terminal tasks.
- The creator reads the safety refusal to sign into other sites as a privacy feature rather than a limitation.
- The creator says the test was a single run and expects the tool to improve.

## Tools mentioned
Claude Computer Use API, Claude (Claude 3.5 mentioned as the comparison model), ChatGPT (used to write and split the build prompt), Node.js, npm

## Relevance to our work
- **prosharness** (1/3): ProsHarness wraps long Claude Code runs with checkpoint/resume. This run lost all progress when the UI reset, which is the failure mode checkpointing should cover. → *Check that ProsHarness checkpoints long agent runs outside the agent's UI, so a hung or refreshed session does not lose the project.*
- **agentos** (1/3): The run shows a terminal-capable agent installing toolchains and running commands with no visible sandbox boundary. That is the case Crucible's sandboxed execution is meant for. → *If computer-use or terminal agents are added, route their commands through Crucible's sandboxed execution, not the host shell.*
