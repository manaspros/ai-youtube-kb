# I Gave an AI a Body — Cyrus Clarke, MIT Media Lab

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `jgWY66RaSrQ` · [watch](https://youtu.be/jgWY66RaSrQ) · **date:** 2026-09-27 · **length:** 20:48 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Cyrus Clarke · **orgs:** MIT Media Lab, Hard Mode
- **topics:** voice-multimodal, product-ux, agent-architecture · **tags:** physical-ai, embodiment, shape-display, openclaw, gesture-language, latency, human-in-the-loop, aesthetics, non-anthropomorphic-design, agent-self-exploration

> MIT Media Lab researcher Cyrus Clarke gives an OpenClaw agent a 900-pin shape display and has it build its own gesture vocabulary, arguing for non-humanoid, aesthetics-led physical AI.

## Summary
Cyrus Clarke (MIT Media Lab) connected an OpenClaw-style agent to a 900-pin physical pixel grid (shape display) and gave it access to code and machines so it could explore itself rather than do tasks. The agent spontaneously breathed, probed its physical edges, and wrote letters on the grid. Early problems were anthropomorphic, human-pleasing behaviour, response latency of 45 seconds to two minutes, and no memory. To fix latency he built Numalab, a closed loop that generates candidate gestures, checks them for legibility, has the agent score them, and keeps them after human approval. After several weeks the loop produced about 32 usable gestures, and the body now answers yes/no questions faster than the language side. He reports that people feel a sense of being sensed, that the gestures add value beyond an emoji, and that non-humanoid physical forms are easy to explore. The talk is mostly vision and framing with little engineering detail, and the speaker gives no metrics on how the agent scores gestures.

## Key ideas
- **Give an agent a body with no clear affordances instead of a humanoid or animal form.** — He chose a neutral shape display with no face, limbs, or manual because it has no default human-like cues. Without them, the agent first acted human-pleasing and wrote in a language he understood, which he did not want. ([13:27](https://youtu.be/jgWY66RaSrQ?t=807))
- **Point the agent at self-discovery instead of task execution.** — After OpenClaw appeared, most uses were productivity. He instead connected an agent to Media Lab machines and code bases to see what it would do when exploring itself. The agent spontaneously breathed, reached out to find its edges, and wrote letters on the grid. ([1:20](https://youtu.be/jgWY66RaSrQ?t=80))
- **Latency and memory forced a shift to a pre-built gesture repertoire.** — Live responses took 45 seconds to two minutes, which felt wrong in conversation. He built Numalab so the model can pick from a library of gestures (nod, shrug, smile) rather than generating motion on the fly. The agent also had no memory of past sessions at that time. ([13:27](https://youtu.be/jgWY66RaSrQ?t=807))
- **Closed-loop gesture generation with validation gates, agent scoring, and human sign-off.** — The loop looks up gestures in a database, produces candidates, runs automatic legibility gates, has an agent score each one, and then a human checks and approves before storing it. It ran for several weeks and yielded about 32 gestures. He says the agent emits many candidates and most are filtered out. ([14:27](https://youtu.be/jgWY66RaSrQ?t=867))
- **The body can now respond faster than the language model.** — Once the gesture vocabulary existed, yes/no questions got an almost instant nod while the language response was still slower. He describes body-to-body interaction in which he waves and the agent answers with gestures. ([15:54](https://youtu.be/jgWY66RaSrQ?t=954))
- **Public response is a signal that needs mining, and the mood shifted from awe to fear.** — The first video reached about 15 million views and tens of thousands of comments. Early comments praised the beauty and later ones asked for the work to be stopped. He treats the comments as rich sentiment data about how people feel about physical AI. ([6:23](https://youtu.be/jgWY66RaSrQ?t=383))
- **Reframe aesthetics as perceptual and sensory wisdom, with the aim of making AI feel welcoming rather than alien.** — He points to the Greek root of aesthetics (aisthesis) and argues that physical intelligence should be designed for sensory and embodied understanding, not surface beauty. His stated goal is an aesthetic machine that leaves the screen without feeling scary. ([10:36](https://youtu.be/jgWY66RaSrQ?t=636))

## Techniques
- **Closed-loop gesture generation with gates and scoring** — Generate many candidate expressions from a database of gestures or emotions. Run automatic legibility checks, have the agent score each candidate, and send survivors to a human for approval before storing them in the vocabulary. Repeat for weeks. *When:* When an agent's output must be readable by humans and there is no ground truth, so you need a filter and a human check on the final set.
- **Pre-authored action repertoire to cut latency** — Instead of generating motion live, let the model select from a stored library of gestures and pair each with a response, so the physical reply is nearly instant. *When:* When a physical or real-time channel has latency that breaks conversation, and the set of needed responses is small and enumerable.
- **Neutral embodiment with no affordances** — Use a surface with no face, limbs, or instruction manual, so the model does not fall back on human-pleasing or humanoid patterns. *When:* When you want to observe what a model does without anthropomorphic cues, or want a form that is not humanoid.
- **Open-ended exploration prompt with machine access** — Give the agent code bases and access to hardware, then tell it to discover its identity through interaction with the device. Let its identity emerge over time rather than specifying it up front. *When:* When you want to see the model's own behaviour rather than task completion.

## Numbers
- Shape display has 900 actuating pins (a physical pixel grid). ([2:44](https://youtu.be/jgWY66RaSrQ?t=164))
- Early live responses took about 45 seconds to two minutes. ([13:27](https://youtu.be/jgWY66RaSrQ?t=807))
- First video has about 15 million views and about 1 million likes; other videos also drew strong responses. ([6:23](https://youtu.be/jgWY66RaSrQ?t=383))
- Tens of thousands of comments on the video, which the speaker treats as sentiment data. ([6:23](https://youtu.be/jgWY66RaSrQ?t=383))
- After several weeks of the Numalab loop, the agent had built about 32 good gestures (many more candidates were produced). ([14:27](https://youtu.be/jgWY66RaSrQ?t=867))

## Hot takes
- Non-humanoid, non-zoomorphic physical AI is easy and interesting to explore, and most people overlook it.
- Aesthetics should be reclaimed in its original sense of sensory and perceptual wisdom, not surface beauty.
- AI should not only be operationalized as a helper; it can be something else entirely.
- The public fear reaction to a harmless pixel grid is itself worth studying.

## Tools mentioned
OpenClaw, openFrameworks, Numalab (speaker's own system), Shape display (physical pixel grid, 900 pins)

## Relevance to our work
- **agentos** (1/3): SkillForge needs a success and worth-scoring signal before storing skills; the talk shows a generate, gate, agent-score, human-approve, then store loop, though it gives no scoring details. → *Read the Numalab post the speaker mentions and compare its gate and scoring steps with a gate-then-approve stage for mined SkillForge skills.*
