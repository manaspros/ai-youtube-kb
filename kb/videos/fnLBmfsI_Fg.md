# Your Voice Agent Doesn't Need a Frontier Model - Joel Allou & Ornella Bahidika, Microsoft

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `fnLBmfsI_Fg` · [watch](https://youtu.be/fnLBmfsI_Fg) · **date:** 2026-08-18 · **length:** 5:45 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Joel Allou, Ornella Bahidika · **orgs:** Microsoft
- **topics:** voice-multimodal, agent-architecture, infra-cost-scaling · **tags:** voice-agent, latency, small-model, state-machine, scaffolding, haiku-4.5, opus-4.7, tutoring, time-to-first-word

> Microsoft's ACE live voice tutor uses a small model (Haiku 4.5) for speech only, moving reasoning, lesson state and planning into a code state machine to hit about 900ms response time.

## Summary
The speakers built ACE, a live AI voice tutor, and argue a small model is the right choice for voice because latency matters more than raw intelligence. Voice replies need to start within about 950ms, and a frontier model that reasons for a second or more loses the caller. Their design pulls decisions out of the model: a state machine tracks lesson steps, a mastery layer tracks what the student knows, and code decides what is displayed and how questions are answered. Each turn the model receives a summary and only has to speak it. In a live comparison, Opus 4.7 with visible reasoning took several seconds, while Haiku 4.5 with this scaffolding answered in about 900ms. The cost is that a small model without scaffolding drifts on long structures and needs strict rules, but that scaffolding is written once in code rather than paid on every turn. Their rule is to pick the fastest model the latency budget allows and spend the effort on harness logic outside the model, which matters most for high-volume workloads.

## Key ideas
- **Voice budgets are about latency, not intelligence** — The speaker says a voice agent should start talking in about 950ms. A frontier model that thinks for a full second has already lost the caller, however good the answer is. That is why they chose a small model on purpose. ([0:00](https://youtu.be/fnLBmfsI_Fg?t=0))
- **Take the hard jobs away from the model** — The model does not decide what happened in the lesson, track what the student knows, or plan the next step. Code does those jobs and hands the model a summary each turn. The model is left to do one thing well: talk. ([1:06](https://youtu.be/fnLBmfsI_Fg?t=66))
- **A state machine owns lesson flow** — They enumerated the scenarios a lesson can hit and built a state machine to move between steps. A mastery layer decides when the student has learned enough. Next step, what to display, and how to answer are all decided outside the model. ([2:29](https://youtu.be/fnLBmfsI_Fg?t=149))
- **Measured result: Haiku with scaffolding vs Opus with reasoning** — A live demo compared Opus 4.7 answering a simple lesson question, where it reasons for a couple of seconds, with Haiku 4.5 plus the scaffolding, which answered in about 900ms. The speaker says the difference is the logic moved into code. ([3:51](https://youtu.be/fnLBmfsI_Fg?t=231))
- **Scaffolding is the price, paid once** — A small model with no scaffolding tends to drift on long structure and needs explicit rules to stay organized. The speaker says that cost is paid once in code instead of on every turn. ([3:51](https://youtu.be/fnLBmfsI_Fg?t=231))
- **Rule: fastest model within budget, then build the harness** — Choose the fastest model your latency budget allows, then spend the remaining effort on states, reasoning steps and scenario handling outside the model. The speaker says this applies to voice, to other latency-sensitive apps, and most to high-volume work where the model is the smallest part of the system. ([4:47](https://youtu.be/fnLBmfsI_Fg?t=287))

## Techniques
- **Externalised state machine for a small speaking model** — Enumerate the scenarios in the flow, encode step-to-step transitions and mastery checks in code, and pass the model a per-turn summary of what to say. The model is never asked to plan, decide or track state. *When:* Real-time, latency-sensitive agents where the model's job is narrow (speaking, phrasing) and the workflow is largely known in advance.
- **Per-turn summary handoff** — Each turn, a deterministic layer computes the current lesson state and passes a compact summary to the model. The model's context carries the decision, not the reasoning. *When:* Any multi-turn agent where a small model would otherwise have to re-derive state each turn.
- **Strict rules to keep small models on track** — Give a small model explicit, hard rules for structure, since without them it drifts on long, multi-step interactions. Accept that this costs upfront engineering effort. *When:* Using a cheap or fast model over long structured interactions.
- **Model selection by latency budget** — Work backward from the latency target to pick the fastest model that fits, then put the effort into harness logic. Do not default to the most capable model. *When:* Picking a model for high-volume or latency-sensitive production paths.

## Numbers
- Target: AI model should start speaking in about 950 milliseconds (latency budget for voice) ([0:00](https://youtu.be/fnLBmfsI_Fg?t=0))
- Haiku 4.5 with scaffolding answers the demo question in about 900 milliseconds ([3:51](https://youtu.be/fnLBmfsI_Fg?t=231))
- Opus 4.7 with reasoning takes a couple of seconds to return the same answer in the demo (qualitative, no exact figure given) ([2:29](https://youtu.be/fnLBmfsI_Fg?t=149))

## Hot takes
- In high-volume voice systems the model is the smallest part of the system, so the surrounding code deserves most of the effort.
- A frontier model that thinks for a second has already lost the room in voice, however good the answer.

## Tools mentioned
Claude Opus 4.7, Claude Haiku 4.5

## Relevance to our work
- **agentos** (1/3): L2B InferCraft already cares about latency on a single GPU, and this talk's point that the model should do narrow speaking while code does state and planning is a latency-first design view worth noting for routing. → *Skim the state-machine-around-small-model pattern when designing AgentOS's priority scheduler or routing, to see if some decisions can move out of the LLM path.*
- **prosharness** (1/3): ProsHarness is a harness around the Claude Code CLI, and this talk argues for pulling decisions and state out of the model into code. It is the same instinct, applied to a voice flow. → *Consider whether plan, checkpoint and resume state in ProsHarness should live in code and be passed to the model as summaries, not re-derived by the model each turn.*
- **general** (1/3): Cheap-model (Haiku) pipelines are a recurring interest, and this talk gives one concrete example of a small model staying reliable when the harness carries the logic. → *Note the 'pick the fastest model within budget, then build the harness' rule as a default when designing Haiku-based pipelines.*
