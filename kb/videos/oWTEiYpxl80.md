# Why AI Agents Should Have Their Own Sandbox — Philipp Schmid, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `oWTEiYpxl80` · [watch](https://youtu.be/oWTEiYpxl80) · **date:** 2026-10-08 · **length:** 20:42 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Philipp Schmid · **orgs:** Google DeepMind
- **topics:** sandboxing-execution, agent-architecture, context-engineering · **tags:** gemini-api, interactions-api, agents-api, managed-sandbox, remote-environment, server-side-state, agents-md, skills, antigravity, ai-studio, long-running-agents, product-demo

> Philipp Schmid (Google DeepMind) argues agents need their own managed, persistent sandbox per API call, shows Gemini Interactions and Agents APIs, and demos a remote Antigravity environment.

## Summary
Philipp Schmid from Google DeepMind presents the Gemini Interactions API as a server-side alternative to the OpenAI Responses API, where the same call shape works for models and agents. He argues the old user/model turn structure no longer fits reasoning models and function calling, so the API uses typed steps instead. The main new idea is a managed remote environment: a cloud sandbox that the agent loop runs in on the server, which persists across turns and can be shared between agents through the filesystem. Environments can be seeded from GCS buckets, GitHub repos or inline files, and skills or AGENTS.md files placed in them are loaded into the system instruction automatically. An Agents API lets a team bake a configured environment once, get back an environment ID, and create a reusable agent from it. The talk is mostly a product walkthrough with demos (an AI talk-radio generator and a sandbox-inspection demo), so the claims are vendor claims about their own product.

## Key ideas
- **Models, agents and modalities share one Interactions API interface, with server-side state so the client passes only a previous interaction ID for follow-up turns.** — The server concatenates the inputs so the model sees the full history. Long-running requests return an ID that the client can stream or poll, which avoids holding an HTTP connection open during slow jobs such as video generation. ([3:13](https://youtu.be/oWTEiYpxl80?t=193))
- **The speaker argues the user/model turn model no longer fits reasoning agents, so the API uses a timeline of typed steps.** — Thoughts may be hidden or shown only as a signature, and function results are not user input. Returning a tool result as a step, not as a user-role message, is presented as the cleaner model. ([6:55](https://youtu.be/oWTEiYpxl80?t=415))
- **The agent runs in a managed remote environment, a sandbox that is created per request and stays persistent across turns.** — The Antigravity agent in the Gemini API runs the same harness as the Antigravity IDE and CLI, but with its own tools and system instruction. The environment can run code, write files and install dependencies, and the client never manages the infrastructure. ([8:12](https://youtu.be/oWTEiYpxl80?t=492))
- **Several agents can share one environment, handing work over through the filesystem or through subagents.** — A follow-up interaction can reuse the environment from the previous turn. Multiple agents attached to the same environment can pick up each other's files. ([9:29](https://youtu.be/oWTEiYpxl80?t=569))
- **Skills and AGENTS.md are file-system native: files in a skills directory are discovered automatically, and AGENTS.md is appended to the system instruction.** — The agent's whole configuration is a folder of files; the speaker describes the demo agent as just an AGENTS.md, skill folders and Python helper scripts that call other Gemini models. ([10:42](https://youtu.be/oWTEiYpxl80?t=642))
- **Environment setup can be done once by an agent and captured as an environment ID, then used to create a shareable agent that starts pre-configured.** — The example is installing the GitHub CLI, adding skills and running sanity checks. The new agent reuses that environment on every call, with no Terraform or Kubernetes work on the user's side. ([10:42](https://youtu.be/oWTEiYpxl80?t=642))
- **The agent loop runs on the server, so function calls are not handled on the client; remote MCP servers can also run inside the environment.** — The client sends one request and gets the final result. Contrast this with the common pattern where the client runs each function call and sends the result back. ([19:18](https://youtu.be/oWTEiYpxl80?t=1158))

## Techniques
- **Environment snapshot as a reusable agent base** — Run a setup agent once to install tools, add skills and run checks. Save the resulting environment ID, then create an agent bound to that environment so each call starts pre-loaded. *When:* When many calls or many users need the same tools and dependencies and you want to avoid repeating setup on each run.
- **Persistent per-conversation sandbox with server-side state** — Start a request with an environment. On follow-up turns, pass only the previous interaction ID and reuse the same environment, so files and installed packages carry over between turns. *When:* For multi-turn research or build tasks where files produced in one turn are needed in later turns.
- **Filesystem handoff between agents** — Put several agents in one environment. Let one agent write files to disk and let another or a subagent read them, instead of passing large context through messages. *When:* When agents work in sequence on artifacts such as code, datasets or generated media.
- **File-based agent configuration** — Keep instructions in AGENTS.md and capabilities in a skills directory inside the environment. The platform loads them into the system instruction at startup. *When:* When you want agent behaviour to be versioned, forkable and editable as plain files, as in the AI talk-radio demo.
- **Mount sources into the sandbox** — Declare sources at environment creation: GCS buckets, GitHub repositories or inline files, so the agent starts with the data it needs. *When:* When the agent must work on an existing repo or dataset without the client copying files at each turn.

## Numbers
- Nano Banana Lite image generation costs about $0.04 per image, described as super fast and cheap (a product launch claim from the speaker). ([0:12](https://youtu.be/oWTEiYpxl80?t=12))
- First request on a fresh remote environment takes about 7 to 10 seconds to start. ([18:17](https://youtu.be/oWTEiYpxl80?t=1097))
- Default demo environment reported by the agent: Ubuntu, 8 vCPU, 16 GB memory, with Python and pip preinstalled (observed in a live demo, not a benchmark). ([18:17](https://youtu.be/oWTEiYpxl80?t=1097))
- Google AI Studio offers free daily usage for the AI talk-radio applet, and a Gmail account is enough to start (no setup needed beyond an API key). ([2:13](https://youtu.be/oWTEiYpxl80?t=133))

## Hot takes
- Function results should not be sent as a user-role message, since the output comes from the environment and not the user.
- Per-request managed sandboxes mean teams can ship agents without Terraform, Kubernetes or Firecracker work.
- The harness is the shared backend, so improvements to the model under one harness help every product built on it (IDE, CLI and API).

## Tools mentioned
Gemini API, Interactions API, Agents API, Google AI Studio, Antigravity agent, Gemini CLI (for agents, not a coding agent), Google Search tool, URL context tool, Nano Banana Lite, Omni Flash, Gemini TTS, Gemma, GCS, GitHub CLI, MCP servers

## Relevance to our work
- **prosharness** (2/3): ProsHarness checkpoints and resumes long Claude Code runs. This talk separates resume state into an interaction handle (server-side) and a persistent filesystem environment, which is a more complete checkpoint than the transcript alone. → *Extend the ProsHarness checkpoint to save the workspace filesystem alongside the session ID, and test resume after the workspace is changed between runs.*
- **agentos** (1/3): Crucible is the sandboxed code-execution layer (celld). This talk shows a managed environment that persists across turns and can be shared between agents, a design point Crucible does not yet cover. → *Check whether Crucible sessions can keep a celld environment alive across turns and let several agents attach to it, before adding shared-sandbox support.*
- **general** (1/3): The talk shows AGENTS.md and skills directories loaded automatically at sandbox startup, a file-based context pattern relevant to context engineering. → *Compare how the AGENTS.md and skills loading in this talk handles precedence with the CLAUDE.md and skills loading used in the Claude Code setup.*
