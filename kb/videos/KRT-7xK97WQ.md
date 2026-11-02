# I Tried Agentic AI from the Terminal... Here’s What Actually Works

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `KRT-7xK97WQ` · [watch](https://youtu.be/KRT-7xK97WQ) · **date:** 2026-02-02 · **length:** 5:09 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** ASI-1
- **topics:** agent-architecture, dev-tools · **tags:** asi-1, cli, agentic-ai, python, stateful-sessions, web-search, terminal, pip

> Short hands-on look at ASI-1's new Python CLI for its agent API: it works in scripts and keeps session state, but the pip-installed mode drops context, and the API is hard to find.

## Summary
Better Stack runs ASI-1's new CLI, a Python script that calls the ASI-1 HTTP API, and tests whether an agentic model is usable from the terminal. The script version keeps conversation context across follow-up questions and can turn on web search with a parameter. The speaker then pip-installs the tool for shorter commands, but that version loses context between runs, which he calls a major drawback for automation. He defines "agentic" as stateful sessions, multi-step reasoning, and deferring work to continue later. He lists the upsides as an OpenAI-compatible API, CLI-first design, Python with no DSL or YAML, and session state held in the protocol rather than the app. The downsides he names are that the API access is hard to find, the ecosystem is small, and reliability depends on how the workflow is designed. The video is a short walkthrough with no benchmarks, no measured reliability, and no exact commands or config shown.

## Key ideas
- **ASI-1 ships a CLI-first agent tool: a Python script that calls the ASI-1 API, with streamed output, rather than a dashboard-first product.** — The speaker frames the CLI as a shift from UI-first AI products toward composable primitives that fit into scripts, SSH sessions and CI. ([0:00](https://youtu.be/KRT-7xK97WQ?t=0))
- **The script version keeps conversation context, so follow-up questions build on earlier turns.** — After a planning prompt for a log-monitoring CLI, a follow-up asking 'why?' is answered in the same session. Web search is enabled through a request parameter for fresh data. ([1:26](https://youtu.be/KRT-7xK97WQ?t=86))
- **The pip-installed command is shorter to run but does not retain context between invocations.** — The speaker calls this a huge drawback for the packaged version. The script version is the one to use if state matters. ([2:37](https://youtu.be/KRT-7xK97WQ?t=157))
- **The speaker's working definition of 'agentic' has three parts: stateful sessions, multi-step reasoning, and deferring work to resume later.** — He contrasts this with a prompt-in, text-out model and argues the bar for agent tools is whether they hold up when scripted. ([2:37](https://youtu.be/KRT-7xK97WQ?t=157))
- **The stated strengths are an OpenAI-compatible API, CLI-first design, Python with no DSL or YAML, and session state held in the protocol rather than the app.** — He presents these as the reasons the tool is worth wiring into automation. ([3:34](https://youtu.be/KRT-7xK97WQ?t=214))
- **The stated weaknesses are that API access is hard to find, the ecosystem is small, and reliability depends on how the workflow is designed.** — He says the tool is not plug-and-play and is aimed at automation and infra-level workflows rather than end-user chat. ([3:34](https://youtu.be/KRT-7xK97WQ?t=214))

## Techniques
- **Script-wrapped agent CLI with a remembered session** — Write a small Python script that posts to the agent's HTTP API with headers and JSON, streams tokens, and reuses the session so follow-up prompts keep context. The speaker describes this as plain HTTP, headers and JSON, with no chat UI in between. *When:* When the agent is called from scripts, SSH sessions or CI and the next step depends on earlier turns.
- **Test the agent in the script path before trusting it in automation** — Run the same prompts through the scripted path and the packaged path, then check whether context survives between invocations. The speaker's test is whether it holds up when scripted, not whether the demo looks good. *When:* Before adopting any agent framework or CLI for unattended workflows.
- **Pick the invocation mode by whether state must persist** — Use the script version when context must carry across calls. Use the pip-installed command for quick one-shot questions, since it does not retain context. *When:* When choosing between a packaged command and a script for repeated use.

## Hot takes
- CLI-first, Python-native agent tools are a rare and intentional design choice, and session state belongs in the protocol, not in the app.
- A packaged agent CLI that drops context between runs is a real drawback for automation, whatever its convenience.
- Most agent frameworks look good in demos and fall apart in real usage, so the test is whether they hold up when scripted.
- This is an early-stage tool with a small ecosystem, and it is not plug-and-play.
- The 'trap' framing in the intro is not resolved: the video shows outputs but no reliability tests over repeated runs. Thin substance caps quality at 2.

## Tools mentioned
ASI-1 CLI, ASI-1 API, ASI-1 (agentic model platform), Python, pip

## Relevance to our work
- **agentos** (1/3): The video is about an OpenAI-compatible agent endpoint and where session state lives. This is tangential to the L1 proxy and the stateful-session questions in AgentOS, but not a direct change. → *Note the video's example of an OpenAI-compatible agent API as one more upstream to test the Govrix Scout proxy against, not as a design input.*
- **prosharness** (1/3): The video contrasts session state held in the protocol with state held in the app, and shows that a packaged mode can drop context. This relates to checkpoint and resume of long runs. → *Use the packaged-command context-loss case as a concrete failing test for ProsHarness checkpoint/resume: confirm that a resumed run restores state from its own checkpoint, not from the CLI's session.*
