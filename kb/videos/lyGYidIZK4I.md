# AI Just Made Physics Interactive. This Is Insane. (Anatomy)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `lyGYidIZK4I` · [watch](https://youtu.be/lyGYidIZK4I) · **date:** 2026-10-22 · **length:** 5:56 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Josh · **orgs:** Better Stack, Anthropic
- **topics:** skills-self-improvement, coding-agents, claude-code, token-cost-efficiency · **tags:** agent-skill, interactive-diagrams, explainers, svg, webgl, threejs-adjacent-3d, visualization, token-cost, claude-code-skills

> Better Stack demos "anatomy", an agent skill that explains concepts as physical machines in interactive HTML/SVG/React figures; useful, but very slow, token-hungry, and its metaphors need checking.

## Summary
Josh from Better Stack walks through "anatomy", a new agent skill (about a week old at recording) that turns a concept into an explanatory figure built around a physical machine rather than boxes and arrows. Examples include a pin-tumbler lock for a cache key, an LRU cache, a TCP handshake, and a database connection pool of 10 connections. The skill is a SKILL.md plus a drawing kit (isometric camera, solids, tubes, optional WebGL layer, 3D mode in beta) and works in Claude Code, Codex, OpenCode and Antigravity. It runs a "truth first" order: collect real numbers, build a small pure model, then draw, with on-screen readouts wired to that model, and then a browser check of geometry. The speaker contrasts it with Mermaid, D2, Excalidraw and an earlier architecture-diagram skill, arguing those show topology while anatomy explains how one mechanism behaves. The main caveats are runtime: a normal figure takes 30 to 90 minutes and a hero piece 2 to 4 hours, with a GitHub issue reporting renders over 48 hours that burn tokens. The speaker also notes the self-checks verify geometry, not facts, so the explanation is only as true as its analogy. The tone is mostly enthusiastic with a clear warning on cost.

## Key ideas
- **Anatomy's core rule: don't draw boxes and arrows. Make the agent invent a physical machine whose mechanism is the concept, so the figure shows what the parts do.** — Examples: a cache key as a pin-tumbler lock, an LRU cache run through step by step, a TCP handshake as a rope passing letters back and forth. ([0:00](https://youtu.be/lyGYidIZK4I?t=0))
- **The skill is a normal SKILL.md plus a drawing kit (isometric camera, solids, tubes, optional WebGL layer), with zero dependencies. It runs in Claude Code, Codex, OpenCode and Antigravity and outputs a standalone HTML page, an SVG, or a React component.** — Steer it with a few words such as interactive, WebGL, 3D or light/dark mode. Figures in the repo are MIT licensed, so they can be shipped on a site. ([1:57](https://youtu.be/lyGYidIZK4I?t=117))
- **Order of work is 'truth first': collect real numbers, build a small pure model of the behaviour, and only then draw. The on-screen readout is wired to the model rather than typed by hand.** — After drawing, the agent opens Chrome and checks its own geometry, looking for elements passing through each other and for parts sitting where they should. ([1:57](https://youtu.be/lyGYidIZK4I?t=117))
- **Anatomy explains one mechanism (how one thing behaves). The speaker contrasts it with Mermaid, D2 and Excalidraw, which draw topology (what connects to what) in seconds.** — Demonstrated figures include hash-map collisions, binary search, DNS resolution, a bloom filter as a fruit machine, debounce/throttle as a music box, and LLM temperature as a wheel. ([3:09](https://youtu.be/lyGYidIZK4I?t=189))
- **Runtime is the main cost. A normal figure takes 30 to 90 minutes, a hero piece 2 to 4 hours, and one GitHub issue reports some renders over 48 hours that burn all tokens. Estimates vary a lot with model choice and time of run.** — The speaker's advice is to start with the normal tier and avoid it on a tight token budget. ([3:09](https://youtu.be/lyGYidIZK4I?t=189))
- **The self-checks prove the picture, not the facts. The analogy is invented, so the explanation is only as true as the metaphor. The speaker suggests the Claude browser extension so the agent can check its own output visually.** — Treat the first render as a draft and read the metaphor before trusting the drawing. ([4:25](https://youtu.be/lyGYidIZK4I?t=265))
- **Early signs: the launch post on X passed 2 million views. A PR claiming support for any compatible agent was declined by the maintainer, who prefers to name the four agents it actually supports.** — The speaker treats much of the hype as X-driven and the project as about a week old. ([4:25](https://youtu.be/lyGYidIZK4I?t=265))

## Techniques
- **Install and invoke the anatomy skill** — Install with the skills CLI (the caption reads 'MPX', presumably npx), or clone the repo into your skills folder. Then ask for a figure with 'anatomy', the concept, and end the prompt with the word 'interactive'. Example used: 'anatomy, database connection pooling, a pool of 10 connections, requests borrow one and give it back, new requests wait in a queue when all are busy, interactive'. Runs can take a long time; the speaker sets the speed control in the output to step through scenarios. *When:* When you want an explainer for how one mechanism behaves over time, not a system topology diagram. Use it for docs, blog posts, landing pages, or teaching.
- **Truth-first figure generation** — Ask for the real numbers and a small pure model of the behaviour first, then draw. Wire on-screen readouts to the model instead of hard-coding them. Finish with a browser check that parts do not overlap and sit where they should. *When:* When a figure must show correct numbers (latency, queue depth, capacity) and not only a plausible picture.
- **Steering the output with modifiers** — Add words such as 'interactive', 'WebGL', '3D', or 'light/dark mode' to the prompt. The 3D mode is in beta and is used for effects such as fire and water. *When:* To pick the output form: a static SVG or HTML page for docs, an interactive page for explaining behaviour, or a React component to embed in an app.
- **Verify the metaphor and the draft** — Read the metaphor and check that the analogy matches how the system really behaves. Use the Claude browser extension so the agent can check the rendered output. Do not treat the first pass as final. *When:* Before publishing any figure, because the self-checks only verify geometry.
- **Budget before running** — Pick the normal figure tier first (30 to 90 minutes) rather than a hero piece (2 to 4 hours). Check how many tokens the run will consume if you are on a metered plan. *When:* On a metered plan or a tight token budget, since a run can burn all tokens.

## Numbers
- The launch post on X had over 2 million views; the repo was about a week old at recording. ([0:43](https://youtu.be/lyGYidIZK4I?t=43))
- The Raptor rocket engine example explodes into 11 assemblies with a WebGL exhaust plume. ([0:43](https://youtu.be/lyGYidIZK4I?t=43))
- Connection-pool example: a pool of 10 connections, with requests waiting in a queue once all are busy. ([1:57](https://youtu.be/lyGYidIZK4I?t=117))
- A normal figure takes 30 to 90 minutes; a hero piece takes 2 to 4 hours. ([3:09](https://youtu.be/lyGYidIZK4I?t=189))
- A GitHub issue reports some renders take over 48 hours and burn all tokens (per the maintainer). ([3:09](https://youtu.be/lyGYidIZK4I?t=189))

## Hot takes
- The speaker says most of the hype came from X and the tool is only about a week old.
- Self-checks verify geometry and line placement, not factual accuracy; the metaphor is invented and the explanation is only as good as the analogy.
- Estimated runtimes vary widely in both directions depending on model and time of run.
- Not sponsored, but the enthusiasm is strong; the speaker's own caveat is that it may eat the token budget.
- The maintainer declined a PR for any-compatible-agent support and prefers to name the four agents it actually supports (a sign of scope control).

## Tools mentioned
anatomy (Claude skill, tool name as spoken in the video), skills CLI, Claude Code, Codex, OpenCode, Antigravity, Chrome, WebGL, React, SVG, Mermaid, D2, Excalidraw, architecture-diagram skill (covered earlier by the channel), Claude browser extension

## Relevance to our work
- **agentos** (2/3): The truth-first order (build a pure model from real numbers, wire the readout to it, then render) is a directly reusable verification pattern for documenting AgentOS's benchmark and correctness work, in line with the next-phase thesis of proving results rather than demos. → *Adopt truth-first for AgentOS benchmark write-ups: generate the numbers and a pure model first, then build any figure from them, and check the output against the model rather than trusting the picture.*
- **prosharness** (1/3): The skill runs inside Claude Code, which ProsHarness wraps. Its figures could explain checkpoint/resume or plan-critique-debate flows, but the token and runtime cost are high for routine use. → *Try the anatomy skill once on a single ProsHarness flow (for example checkpoint/resume) with a token budget set in advance; keep it as a documentation tool, not a per-run step.*
