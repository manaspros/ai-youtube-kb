# Agents on the Canvas in tldraw — Steve Ruiz, tldraw

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `sPUjIBH5Cwg` · [watch](https://youtu.be/sPUjIBH5Cwg) · **date:** 2026-05-18 · **length:** 19:54 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Steve Ruiz · **orgs:** tldraw, Replit, Lovable, Google Stitch, Cursor, Spotify, OpenClaw
- **topics:** multi-agent, product-ux, sandboxing-execution, security-guardrails · **tags:** tldraw, canvas agents, whiteboard SDK, multi-agent coordination, leader-follower, shared state, structured output drawing, vision model limits, Electron, local-first, desktop agents, sandbox trade-offs, Make Real, fairies

> Steve Ruiz (tldraw) shows how agents moved from one-shot drawing on a whiteboard to multiple agents working as a team on a shared canvas, and the safety trade-offs of letting them script a desktop app.

## Summary
Steve Ruiz of tldraw walks through the company's progression of AI features on its whiteboard SDK, starting with Make Real (2023), which turned a canvas sketch into a working prototype. Drawing on the canvas worked through structured text outputs (shape tool calls) rather than image generation, and he notes that vision models struggle with spatial conventions like y-axis direction. He then moved to an agent loop that produces output, reviews it, and iterates, and finally to multiple agents ("fairies") on the canvas that see each other's work, elect a leader, and delegate a to-do list. For more access he could not use a browser sandbox, because the agent needed the DOM and screenshots, so he wrapped the app in an Electron desktop shell with a local endpoint that executes posted JavaScript, which he openly calls a bad idea outside an offline, file-based app. The talk ends with examples of agents modifying installed desktop software and his view that such sharp tools should be handed to users with the risk made explicit. It is a demo-heavy product talk with few hard numbers, so the reusable value is the coordination and safety patterns rather than benchmarks.

## Key ideas
- **Drawing via text structured outputs beats image generation for canvas work.** — Agents on the canvas emit tool calls that create shapes, not pixels. The speaker says this is why the output stays editable and matches what a human could draw with the same tools. ([4:39](https://youtu.be/sPUjIBH5Cwg?t=279))
- **Vision models handle spatial data poorly, so prompt for conventions explicitly.** — Speaker says there is less vision training data than text, and the training data conflicts (for example, the y-axis points down on screens but up on graphs, and 'left' is ambiguous). Getting predictable placement took a lot of prompt engineering. ([6:41](https://youtu.be/sPUjIBH5Cwg?t=401))
- **A produce, review, iterate agent loop beats one-shot generation.** — He moved from one-shot prompts to an agent loop that generates output, reviews it, and repeats until it judges the work done. He copied the conventions of coding agents, such as showing rejections and visible reasoning. ([6:41](https://youtu.be/sPUjIBH5Cwg?t=401))
- **Multiple agents on a shared canvas need shared state and an observer.** — Each agent can see the others' actions and where they are working. A leader scouts the canvas, writes a to-do list, delegates it, and judges whether each piece is done. The speaker frames the hard problems as shared state, leader/follower roles, and avoiding overlap when agents are effectively blind while they work. ([10:43](https://youtu.be/sPUjIBH5Cwg?t=643))
- **The browser sandbox was ruled out, which pushed the design to a desktop wrapper.** — The agent needed the DOM, the browser view, and screenshots to see what it was doing, so a sandboxed code runner did not work. He wrapped the app in Electron and exposed a local HTTP endpoint that runs posted JavaScript. He calls this a terrible idea for a normal app but acceptable for an offline, file-based desktop app. ([13:52](https://youtu.be/sPUjIBH5Cwg?t=832))
- **Letting the agent write code against the editor runtime gives behaviour the canvas lacks.** — tldraw has no primitives for hover or click. Because the editor exposes a runtime API, the agent can write code against it to make a drawn UI interactive, for example a leg length or shirt colour control. ([15:22](https://youtu.be/sPUjIBH5Cwg?t=922))
- **Agents with local desktop access will do unexpected things, so risk has to be handed to the user explicitly.** — He describes an agent that read a minified Spotify bundle to remove podcasts on request, and he says these tools have no qualms about changing files on the user's machine. He argues that maximum agency means accepting risk, and that the user should be told this plainly ('sharp tools'). ([16:22](https://youtu.be/sPUjIBH5Cwg?t=982))

## Techniques
- **Structured-output shape drawing** — Expose the canvas's own shape-creation operations as tools and have the model emit structured calls instead of generating an image. Results stay editable. *When:* Any agent that must produce diagrams, wireframes, or layouts in a structured editor or whiteboard.
- **Produce-review-iterate loop** — The agent generates output, inspects the result (for example a screenshot), and loops until it judges the work done. Show rejections and reasoning to the user. *When:* Visual or structured output where one-shot generation is not reliable enough.
- **Leader/follower multi-agent on shared state** — Elect one agent as leader. The leader scouts the shared workspace, writes a to-do list, delegates items to followers, and checks completion. Followers can read each other's actions to avoid overlap. *When:* Several agents working on one artifact, where overlap and missed work are the main risks.
- **Expose a runtime API for agent-written code** — Give the agent a documented editor/runtime API it can call from generated code, so it can add behaviour the product does not provide natively. Speaker mentions doing this via a local HTTP endpoint in a desktop wrapper. *When:* A product that is hackable or local-first and where users want agent-driven customisation.
- **Prompt for spatial and coordinate conventions** — State the coordinate system and layout rules in the prompt, since models confuse screen and graph conventions. *When:* Agents placing elements by position on a 2D surface.

## Numbers
- Three agents (Ferris, Helen, Joan) were given one canvas task; one was elected leader and delegated a to-do list to the other two. ([10:43](https://youtu.be/sPUjIBH5Cwg?t=643))
- The multi-agent canvas work was being built around October/December of the prior year (about 2025), in parallel with industry agent-orchestration work. ([11:45](https://youtu.be/sPUjIBH5Cwg?t=705))
- Make Real, the first canvas-to-prototype app, dates from 2023 when vision models came out. ([2:38](https://youtu.be/sPUjIBH5Cwg?t=158))
- The talk is 19:54 long, and the speaker mentions a rotated API key after a live demo. ([3:40](https://youtu.be/sPUjIBH5Cwg?t=220))

## Hot takes
- Letting an agent run arbitrary JavaScript from an HTTP endpoint is a terrible idea for most apps, but acceptable for an offline, file-based desktop app.
- Agents will modify installed desktop software (for example, reading a minified Spotify bundle) without hesitation, so maximum agency means handing users the risk directly.
- Sandboxed code execution does not fit agents that need the DOM and screenshots; a desktop wrapper was the practical choice.

## Tools mentioned
tldraw, Electron, Claude, Cursor, Make Real

## Relevance to our work
- **prosharness** (2/3): The leader that decomposes work, delegates a to-do list, and judges completion matches ProsHarness's plan, critique, and debate flow. → *Compare ProsHarness's critique step with a leader-judges-completion role: check whether a single judge pass after delegated subtasks catches missed work.*
- **agentos** (1/3): The talk shows a browser-style sandbox fails when the agent needs DOM access and screenshots, which bears on Crucible's sandbox design. → *When scoping Crucible's sandbox, decide whether UI-driving agents need DOM and screenshot access; if so, the bare code-exec sandbox will not cover them.*
- **general** (1/3): Shared canvas state and blind-agent overlap are general multi-agent coordination problems, and the speaker names them without solutions. → *Read the tldraw fairies write-up or demo for how shared state and leader election were handled, to compare with the subagent design.*
