# The New Primitives: Building AI Native Software — Kwindla Kramer, Daily

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `LZuWZRze3MU` · [watch](https://youtu.be/LZuWZRze3MU) · **date:** 2026-08-18 · **length:** 21:14 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Kwindla Kramer · **orgs:** Daily, PipeCat, Tavus, Apple, Microsoft, AWS, NVIDIA, Anthropic
- **topics:** product-ux, multi-agent, voice-multimodal, agent-architecture · **tags:** AI-native software, agents++, Knowledge Navigator, Vannevar Bush, PipeCat, Gradient Bang, sub-agents, context compression, progressive skills loading, dynamic UI generation, voice agents, multimodal

> Kwindla Kramer (Daily, PipeCat) argues agents are a stage on the way to AI-native software, using 80 years of computing history and demos of a real-time Knowledge Navigator and a multiplayer LLM game.

## Summary
Kramer frames the current agent era as one step in a longer arc, starting from Vannevar Bush's 1945 essay "As We May Think" and running through programming languages, interactive computing, relational databases, the PC, the web, mobile and cloud. He argues the web's real lesson was that text, audio, video and data belong together, and that the Apple Knowledge Navigator concept video (1987) still sets the target for the current era. He positions today's work as "agents plus plus" (multi-model harnesses, copilots embedded in software) and asks what comes after. He shows a one-take, four-minute video built on real tech that recreates the Knowledge Navigator, then walks through Gradient Bang, a multiplayer game where LLMs sit at the core of every interaction and make hundreds of inference calls per moment. The game is used to show sub-agent patterns: async non-blocking context compression, long-running sub-agents sharing context, progressive skill loading and dynamic UI generation. The talk is mostly a vision and history talk with demos, not a build-along, and it is somewhat promotional for Daily and PipeCat. The speaker says the first draft ran an hour and was cut to about 21 minutes.

## Key ideas
- **Agents are a stage, not the end point** — The speaker sees today's work as agents plus plus (multi-model harnesses, software copilots, org-level harnesses) and asks what AI-native software comes after that, the way the web led past static web pages to web apps. ([3:47](https://youtu.be/LZuWZRze3MU?t=227))
- **The web was multimodal from the start** — He argues the most important thing about the 1990s web was that text, audio, video and data were treated as belonging together, not as separate programs. He presents this as a conscious attempt to make the 1987 Knowledge Navigator vision real. ([11:42](https://youtu.be/LZuWZRze3MU?t=702))
- **Knowledge Navigator is still the reference target** — The 1987 Apple concept video (foldable tablet, voice assistant, video calls, delegated tasks, continual learning) is described as updated for 40 years of progress and as anticipating the agent era. A 2026 remake built on real tech is shown as a proof point. ([17:40](https://youtu.be/LZuWZRze3MU?t=1060))
- **Spreadsheets as a counterexample to job-loss fears** — VisiCalc did not eliminate accountants. It made much more accounting-style work possible and created work categories nobody had imagined, which he uses to argue against the mass-unemployment framing of AI. ([10:06](https://youtu.be/LZuWZRze3MU?t=606))
- **Each computing era solved one bottleneck** — He sketches a sequence: 1950s, transmitting human intent to machines (languages, compilers); 1960s, two-way interaction; 1970s, scalable abstractions (relational, declarative); 1980s, personal computers; 1990s, networks; 2000s, mobile; 2010s, cloud. He frames the agent era as the next step in that sequence. ([6:08](https://youtu.be/LZuWZRze3MU?t=368))
- **LLMs as the core of every interaction in a game** — Gradient Bang is built so that every moment involves hundreds of inference calls. It is used to show that this would not have been practical about a year earlier. ([19:09](https://youtu.be/LZuWZRze3MU?t=1149))
- **Sub-agent patterns from the demo** — The game is used to name concrete patterns: asynchronous non-blocking context compression, long-running sub-agents that share context, progressive skills loading, dynamic UI generation, and conversational voice. These are presented as examples, not as a full how-to. ([19:09](https://youtu.be/LZuWZRze3MU?t=1149))

## Techniques
- **Asynchronous non-blocking context compression for sub-agents** — Compress a sub-agent's context in the background so the main interaction is not blocked. The demo shows a note being saved for later while compression runs. *When:* Long-running agent sessions where context grows and waiting for compression would stall the user.
- **Long-running sub-agents that share context** — Several sub-agents run in parallel loops (trade, exploration) against a shared context and report back to a coordinating agent. The demo shows multiple ships each on their own loop. *When:* Parallel, long-lived workers that need a common world state or memory.
- **Progressive skills loading** — Load skill or capability detail on demand rather than all at once. The speaker names it but does not show the mechanism. *When:* Many capabilities where loading all of them up front would bloat context.
- **Dynamic UI generation driven by the agent** — The agent produces interface elements at runtime in response to a request (for example, showing task history or hiding a map). *When:* Interfaces where the set of useful views depends on what the user asks for in the moment.
- **Real-time voice plus LLM orchestration with a pipeline framework** — PipeCat, an open-source vendor-neutral framework, is presented as the base for voice agents. The Knowledge Navigator remake is described as one take on real tech. *When:* Building low-latency voice or multimodal agents that need a framework rather than custom plumbing.

## Numbers
- PipeCat described as the most widely used framework for voice agents, used by AWS, NVIDIA, Anthropic and thousands of startups and enterprises (speaker's claim, not verified) ([0:08](https://youtu.be/LZuWZRze3MU?t=8))
- Gradient Bang: hundreds of inference calls at every moment of gameplay; speaker says this was not practical about a year earlier ([19:09](https://youtu.be/LZuWZRze3MU?t=1149))
- Tavus remake of Knowledge Navigator is one take, about four minutes long ([17:40](https://youtu.be/LZuWZRze3MU?t=1060))
- Speaker's company co-founded a startup in 2006 to commercialise the Minority Report interface; demo reel from 2012, six years in ([15:20](https://youtu.be/LZuWZRze3MU?t=920))
- Roughly 80 years of digital computing history used as the frame for the talk ([0:08](https://youtu.be/LZuWZRze3MU?t=8))

## Hot takes
- The web's most important property was being multimodal from the start, not the GUIs of the 1980s.
- VisiCalc is a counterargument to mass-unemployment fears from AI because it expanded accounting work.
- The current agent wave (agents plus plus) is a stage, and the next stage is AI-native software, not more agent frameworks.

## Tools mentioned
PipeCat, Gradient Bang, Daily, Tavus

## Relevance to our work
- **agentos** (1/3): Gradient Bang names sub-agent patterns (async non-blocking context compression, long-running sub-agents sharing context, progressive skills loading) that touch SkillForge and EvolveCraft, but the talk gives no implementation detail. → *Look up the Gradient Bang project and compare its sub-agent context-sharing and progressive skill loading against the SkillForge design, without adopting anything yet.*
- **prosharness** (1/3): Long-running sub-agents that share context and async context compression relate to ProsHarness checkpoint/resume and planner-worker loops, though the talk shows no mechanism. → *Note the async non-blocking context compression idea as a candidate for long-run context handling in ProsHarness; check the Gradient Bang source before designing anything.*
