# The Spatial Harness: Bringing Agents to the Canvas — Max Drake, tldraw

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `XWcXwnysmpY` · [watch](https://youtu.be/XWcXwnysmpY) · **date:** 2026-09-18 · **length:** 18:52 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Max Drake · **orgs:** tldraw, Replit, Miro, Conductor, OpenAI
- **topics:** product-ux, multi-agent, agent-architecture, coding-agents · **tags:** tldraw, infinite-canvas, spatial-ui, agent-on-canvas, multi-agent-visualization, code-mode, dependency-graph, coding-agent-task-board, desktop-agent, demo-heavy

> tldraw's Max Drake on giving LLM agents a spatial canvas: teaching them to read screenshots plus shape data, running multi-agent fairies, and driving live apps and the desktop through code.

## Summary
Max Drake, a product engineer at tldraw, argues that agents work poorly in 2D space because their native medium is text, so canvas work needs deliberate engineering. He describes a progression: first teaching an LLM to read a canvas from a screenshot plus JSON and act on it in a single prompt, then wrapping that in an agentic harness that sets its own goals and moves its viewport to search. The Fairies project adds multiplayer, with several agents on one canvas, an orchestrator agent that assigns tasks, and visible per-agent state so the user does not have to read a chat log. He notes the limit of this design: agents confined to the canvas cannot easily touch real-world data or tools. His experiment, Tech Tree, is a dependency graph where each node is a coding-agent task that can be launched from the UI. In the closing demos, the desktop tldraw app exposes its editor to external agents such as Claude Code, which write plain JavaScript against it, and an agent uses the app as a window manager. The live demo of a build did not finish within the talk, which the speaker acknowledged.

## Key ideas
- **Agents are weak at 2D spatial reasoning because their native medium is text, so canvas use needs explicit engineering.** — The speaker frames LLMs as text-in, text-out and says they struggle to align or understand 2D layouts without special work. This is the premise for the rest of the talk. ([3:58](https://youtu.be/XWcXwnysmpY?t=238))
- **Teach the model the canvas with two inputs, a screenshot and structured shape data, plus the semantics of its own actions.** — The single-shot demo (a mouse blowing out a candle) worked because the prompt explained how to read the screenshot and JSON and how actions change the canvas. The shapes were ordinary canvas shapes, not special assets. ([5:13](https://youtu.be/XWcXwnysmpY?t=313))
- **Wrap the single-shot prompt in an agentic harness so the agent can set goals, track to-dos, and move its viewport to search the canvas.** — This turns one prompt into an autonomous loop. The agent looks around the canvas the way a coding agent searches a codebase. The starter kit is MIT licensed. ([6:16](https://youtu.be/XWcXwnysmpY?t=376))
- **Multi-agent work becomes easier to follow when agent state is shown spatially rather than in a chat log.** — Each agent has a visual identity (hat, color, a leg slider) so you can tell them apart. An orchestrator agent writes a plan and assigns tasks. The user can see task state at a glance and does not need to read a transcript. ([9:48](https://youtu.be/XWcXwnysmpY?t=588))
- **A harness built for an in-app canvas agent does not reach the outside world, so the next step was to open the editor to external agents.** — The Fairies model requires the whole harness to live inside the canvas, which limits access to real data. The fix was to expose the running app's editor through a local server. ([11:15](https://youtu.be/XWcXwnysmpY?t=675))
- **Task management can be a dependency graph where each node is a coding-agent run that can be started from the UI.** — The Tech Tree prototype turns a launch-planning graph into a board of tasks. Each task is kicked off as a coding agent, and the speaker compares it to Conductor and OpenAI Symphony. Merged PRs and progress show on the board. ([12:12](https://youtu.be/XWcXwnysmpY?t=732))
- **Exposing the running app's editor to external agents turns the app into a scripting surface.** — A local server lets any agent, here Claude Code, write plain JavaScript against the live editor. The speaker calls this code mode for a canvas app. It also means the agent can act on the app while it runs. ([14:52](https://youtu.be/XWcXwnysmpY?t=892))
- **Agents with computer access can use the canvas as a live UI layer on the desktop, not only as a sandbox.** — A colleague used the tldraw desktop app as a window manager, and a Pong game ran through the desktop windows. The speaker presents these as ephemeral UIs that act on real data, such as Gmail and Notion. ([16:20](https://youtu.be/XWcXwnysmpY?t=980))

## Techniques
- **Screenshot plus structured data as canvas context** — Give the model a screenshot of the canvas together with a JSON description of the shapes, and explain in the prompt how to interpret both and how each action changes the canvas. *When:* When an LLM must understand or edit a 2D spatial UI and text alone is not enough.
- **Agentic canvas harness with self-set goals** — Put a loop around the single-shot prompt. Let the agent write its own to-do list, pan or zoom its viewport to find content, and keep acting until the goals are met. *When:* When a one-off prompt is too limited and the task needs several steps across a large workspace.
- **Visual agent identity and on-canvas task state** — Give each agent a distinct look and show its task status on the canvas, so a user watching many agents can see who is doing what without reading a chat log. *When:* When several agents run in parallel and humans must monitor or intervene.
- **Orchestrator agent posting tasks to a shared board** — One agent writes a plan and creates tasks. Worker agents pick them up, and the orchestrator is notified to review results. *When:* When splitting work across several agents that share one workspace.
- **Local editor server for code-mode agents** — Expose the running desktop app's editor instance through a local server, so an external agent such as Claude Code can run plain JavaScript against live app state. *When:* When you want a coding agent to script or drive an interactive app without a special plugin.
- **Dependency graph of agent tasks** — Model work as nodes with dependencies. Each node is a coding-agent run that can be launched, watched, and reviewed from the graph view. *When:* When planning a larger project with many interdependent pieces that agents can build in parallel.

## Numbers
- The live demo build had been running for 13 minutes and had not finished when the talk ended. The speaker said this was fine. ([14:52](https://youtu.be/XWcXwnysmpY?t=892))
- Replit's agent canvas is built on the tldraw SDK, per the speaker. ([1:12](https://youtu.be/XWcXwnysmpY?t=72))
- The tldraw agent starter kit is MIT licensed. ([6:16](https://youtu.be/XWcXwnysmpY?t=376))

## Hot takes
- Agents are bad at 2D spatial reasoning and need explicit engineering to work on a canvas.
- A spatial view of many agents' state is easier to read than a chat transcript.
- A canvas can serve as the control surface for a graph of coding-agent tasks.
- Exposing a running app's editor to a coding agent as a JavaScript API is a practical way to script it.

## Tools mentioned
tldraw SDK, tldraw desktop app, Claude Code, Notion, Gmail, Conductor, OpenAI Symphony

## Relevance to our work
- **prosharness** (1/3): The Tech Tree idea shows a dependency graph of tasks, each a coding-agent run that can be started and watched. ProsHarness already runs Claude Code and has loops and schedules, so the same task-graph view could apply to plan steps. → *Sketch a dependency-graph view of ProsHarness plan steps where each node tracks one Claude Code run's status and start is gated by its dependencies.*
- **general** (1/3): Useful general pattern for multi-agent monitoring: visual state of parallel agents on a shared surface, instead of reading chat logs. → *Read the Fairies and orchestrator description (about 8:47 to 11:15) when designing how multiple subagents report status.*
