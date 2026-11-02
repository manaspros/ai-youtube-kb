# Think You Can Build a Game with AI? Think Again! - Danielle An & David Hoe, Meta

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `grdoOC1BT1s` · [watch](https://youtu.be/grdoOC1BT1s) · **date:** 2026-07-18 · **length:** 18:00 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Danielle An, David Hoe · **orgs:** Meta
- **topics:** product-ux, vibe-coding-app-building, multi-agent · **tags:** ai-game-development, runtime-llm, npc-agents, key-art-anchoring, taste, playtesting, nondeterminism, content-safety, interactive-slides

> Two Meta game-creation leads argue that AI prompting makes basic games easy, so taste, art cohesion, playtesting and runtime-LLM NPCs decide quality, with undeterminism as the open engineering problem.

## Summary
Danielle An and David Hoe, who lead AI-driven game creation work at Meta, argue that prompting a basic game is now easy but generic output all looks alike. They say differentiation comes from aesthetics, cohesion across UI, story and art, playtesting with real players, and taste about which players a game is for. They show a key-art image used as an anchor so an image model keeps one art style and gameplay feel across sessions. They demo a multiplayer game built in days where each NPC is driven by an LLM with a personality and makes unscripted decisions. They argue AI shortens the old linear waterfall pipeline so teams work in parallel and iterate in hours or days. They flag open problems: runtime LLMs are still being explored, and agentic stacks are nondeterministic, so model or prompt changes can break systems and make debugging hard. The talk gives no benchmarks, costs or evaluation method, and it is mostly an interactive opener with a few practitioner tips.

## Key ideas
- **Prompted games look alike; quality comes from taste and differentiation** — Basic prompted games (platformers, Tetris) are impressive at first, but the novelty wears off because prompts converge. What sets a game apart is aesthetics, cohesion across UI, story and art, playtesting with real people, and a clear sense of which players it is for. ([3:03](https://youtu.be/grdoOC1BT1s?t=183))
- **A single key-art image can anchor an image model's style and gameplay** — An art director used one key-art image as an anchor. It set the art style for downstream assets and also hinted at gameplay, which helped the LLM stay cohesive across sessions. ([5:50](https://youtu.be/grdoOC1BT1s?t=350))
- **Runtime LLMs make each NPC a live decision-maker** — In a four-player competitive demo, each NPC is driven by an LLM and given a personality (thief, honorable, fast). They take unscripted actions such as stealing, blocking or kicking, so every game plays out differently. ([8:36](https://youtu.be/grdoOC1BT1s?t=516))
- **AI turns the linear game waterfall into parallel work** — Previously, decisions made upstream (design, art, modeling, animation) were costly to revisit. With AI, teams work in parallel and iterate in hours or days instead of months, which means more playtests. ([11:02](https://youtu.be/grdoOC1BT1s?t=662))
- **Runtime LLM as game master is useful, but the use case is still unclear** — One example is an LLM that compensates for a player's weaker coordination in co-op so the player still feels part of the team. The speaker says the technology does not by itself make a product better and that the team is still exploring. ([12:27](https://youtu.be/grdoOC1BT1s?t=747))
- **Nondeterminism across the whole agentic stack is the hard engineering problem** — Model upgrades or prompt changes can break a system that otherwise relied on stable code, tests and debugging. The speaker says at scale teams are still struggling with how to debug and engage such systems. No solution is given. ([13:55](https://youtu.be/grdoOC1BT1s?t=835))

## Techniques
- **Key-art anchoring for image generation** — Generate or pick one key-art image as the reference style, then derive asset images from it so the art style stays consistent. The same anchor image can also carry gameplay hints. *When:* When building a multi-asset visual project with an image model and needing cohesion across many generation sessions.
- **Personality-driven LLM NPCs in a shared game loop** — Give each NPC a persona in its prompt (e.g. thief, honorable, fast). Each NPC then decides its own actions at runtime toward a shared goal, such as collecting cubes, which yields emergent competition. *When:* When you want emergent, non-scripted multi-agent behavior in a small, short-lived simulation that can be built in days.
- **Parallel AI-assisted production with frequent playtests** — Run design, art and content work in parallel and iterate each change in hours or days, then playtest often with real players instead of executing a fixed linear plan. *When:* When upstream decisions are expensive to revisit under a waterfall process and fast feedback is possible.
- **Runtime LLM game master for per-player adjustment** — A runtime LLM watches a player and adjusts the game to suit them, for example easing a co-op role for a player who struggles with coordination. *When:* When a game should adapt to individual players during play. The speaker treats this as exploratory.

## Numbers
- Team has been doing AI-driven game creation work for over a year ([1:03](https://youtu.be/grdoOC1BT1s?t=63))
- A game the speakers showed was made by David in the last 12 hours ([2:04](https://youtu.be/grdoOC1BT1s?t=124))
- Runtime-LLM NPC multiplayer demo was built over a couple of days; four players ([8:36](https://youtu.be/grdoOC1BT1s?t=516))
- Lessons come from about 12 months of directing cross-discipline teams; the speaker says it felt like 12 years ([11:02](https://youtu.be/grdoOC1BT1s?t=662))
- Iteration on updates moved from months to hours or days with parallel AI-assisted teams (qualitative, no measured figures) ([11:02](https://youtu.be/grdoOC1BT1s?t=662))

## Hot takes
- Once prompting is commoditized, taste is the only real differentiator for AI-built games.
- Nondeterminism across the whole agentic stack is the core unsolved problem for engineers at scale, more than model quality.
- Runtime LLMs in games are still exploratory and do not by themselves make a product better.

## Tools mentioned
Gemini, Nano Banana, Meshy, Manus, Labubu (demo subject)

## Relevance to our work
- **agentos** (1/3): Speaker names content safety for runtime-generated content as an open challenge with no method given, which is a loose fit for the guardrail pillar. → *Note only: when reviewing AgentOS guardrails, consider scanning model-generated output at runtime, not only user input; the talk raised this at [16:01] without a solution.*
- **prosharness** (1/3): Speaker says model or prompt changes can break a system and debugging is hard, which relates to checkpoint/resume of long runs. He gives no method. → *Low priority: write down the open question of how to detect that a model or prompt change invalidates a resumed run, since the talk raises it at [13:55] without an answer.*
- **general** (1/3): Key-art anchoring keeps an image model cohesive across sessions, a loose analogy to pinning a stable reference artifact in context. Only one anecdote is given. → *Optional read: none needed; treat the key-art example at [5:50] as one anecdote about stable reference context, not evidence.*
