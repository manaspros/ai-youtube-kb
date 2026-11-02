# The Best Models Still Reason Like Toddlers — Andrew Dai, Elorian

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `A_I8mw8yfns` · [watch](https://youtu.be/A_I8mw8yfns) · **date:** 2026-09-27 · **length:** 18:17 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Andrew Dai · **orgs:** Elorium, Google Brain, Google DeepMind, ByteDance, Apple, xAI
- **topics:** voice-multimodal, models-research, evals · **tags:** visual reasoning, multimodal, hallucination, spatial reasoning, visual chain of thought, ARC-AGI, MMMU, synthetic data, robotics, CAD, video understanding, simulation validation

> Elorium's CEO argues frontier models (Claude, ChatGPT, Gemini) pattern-match instead of reasoning over images and video, and proposes visual chain-of-thought trained on synthetic data as the fix.

## Summary
The speaker, co-founder and CEO of Elorium (the transcript also renders it as "Elorian"), shows that frontier multimodal models fail simple visual questions such as counting white squares on a partly visible chessboard, counting rows on a Catan board, and tracking a robot arm's actions across a video. He explains the failures as pattern matching plus loss of consistency over long clips. He separates fast visual recognition, which models handle well, from slow visual reasoning, which they handle poorly, using a one-second-glance test. He says popular benchmarks mislead: ARC-AGI uses 32x32 or 64x64 images, and MMMU questions can often be answered without the image. His team's approach is to collect or generate visual reasoning data, run a synthetic data flywheel with evals, agents, SFT and RL, and train visual chain-of-thought, where the model draws boxes and reasons in image space. He names robotics, construction safety and CAD/architecture design as target use cases, with simulator-based validation of outputs. The talk is part technical argument and part company pitch, and it gives few hard numbers.

## Key ideas
- **Frontier models rely on pattern matching, and that hurts them on detailed visual questions.** — On a chessboard with part of the board visible, models assume the full 32-square pattern and answer 32. The speaker says they guess from a learned template instead of counting what is in the image. ([1:06](https://youtu.be/A_I8mw8yfns?t=66))
- **The line between visual understanding and visual reasoning is how long a human would need to answer.** — If a person can answer in about one second (what game, what flower, how many pieces on a nearly empty board), it is recognition. If the answer needs a close look, it is reasoning. Models do well on the first and fail on the second. ([3:53](https://youtu.be/A_I8mw8yfns?t=233))
- **Models lose track of state across long videos, so they miss actions.** — In a robot-arm clip, models missed that the arm lifted a lid and that it turned on a stove. The speaker calls this context amnesia and attributes it to weak consistency over time. ([2:30](https://youtu.be/A_I8mw8yfns?t=150))
- **Popular visual benchmarks do not measure what they claim.** — ARC-AGI images are 32x32 or 64x64 pixels, which the speaker says cannot represent real-world tasks. MMMU questions often can be answered without the image, so high scores overstate visual reasoning. ([5:13](https://youtu.be/A_I8mw8yfns?t=313))
- **Current perception tools are passive, so they cannot answer multi-step questions.** — Tools such as Google Lens, SAM3, YOLO and Mask R-CNN map pixels to labels well, but they have no reasoning step over what they find. ([8:07](https://youtu.be/A_I8mw8yfns?t=487))
- **Visual chain of thought means reasoning in image space, not only in text.** — For 'how many red hotels', the model first boxes all hotels, then filters by colour. The speaker says humans reason this way and text-only chain of thought in frontier models does not. ([9:27](https://youtu.be/A_I8mw8yfns?t=567))
- **Visual reasoning data is hard to get online, so the team generates it in a synthetic flywheel.** — The loop uses evals and agents to produce data, then SFT and RL to improve the model. The speaker says they also changed the transformer architecture, but gives no specifics. ([9:27](https://youtu.be/A_I8mw8yfns?t=567))
- **Outputs in mechanical design can be checked the way unit tests check code.** — The speaker proposes extracting geometric logic from blueprints or CAD, then checking it with programmatic rules or simulators such as Siemens tools. He draws a parallel to running code against tests. ([16:05](https://youtu.be/A_I8mw8yfns?t=965))

## Techniques
- **Keep visual sub-tasks simple** — Break a visual question into small checks that a glance can settle, rather than asking for a count or spatial answer over a dense image in one step. *When:* Designing any agent or pipeline that reads images or screenshots, to reduce hallucinated answers.
- **One-second test for task difficulty** — Ask whether a human could answer from a one-second look. If not, treat the task as reasoning and expect model failures. *When:* Scoping which visual tasks a model can be trusted with and where to add verification.
- **Visual chain of thought** — Have the model produce intermediate image-space steps, such as bounding boxes for all candidate objects, then filter them to answer the question. *When:* Counting or spatial questions with several conditions, such as colour plus object type.
- **Synthetic data flywheel for a hard modality** — Use evals and agents to generate task-specific data where it is not available online, then train with SFT and RL and repeat. *When:* A capability gap exists in a domain with little public data, such as physical or visual reasoning.
- **Programmatic or simulator validation of outputs** — Check model-generated designs with rules or a physics simulator, the same way unit tests check generated code. *When:* Generated artifacts can be verified mechanically, such as CAD models or geometric constraints.

## Numbers
- Frontier models score 85-90% on ARC-AGI, but its images are only 32x32 or 64x64 pixels (speaker's critique of the benchmark). ([5:13](https://youtu.be/A_I8mw8yfns?t=313))
- Design of one small part of a robot testing platform takes a mechanical engineering company 100-200 hours of human time. ([14:40](https://youtu.be/A_I8mw8yfns?t=880))
- Design of the full robot testing platform takes an estimated 2,000-3,000 hours of human time. ([14:40](https://youtu.be/A_I8mw8yfns?t=880))
- Elorium has about 20 people. ([11:59](https://youtu.be/A_I8mw8yfns?t=719))
- In the Catan example a model said there were 5 blue rows, but the correct count is 7. ([2:30](https://youtu.be/A_I8mw8yfns?t=150))
- A model API is planned for release by the end of the year, for robot scene understanding. ([11:59](https://youtu.be/A_I8mw8yfns?t=719))

## Hot takes
- Frontier models are nowhere near visual reasoning AGI, even with high ARC-AGI scores.
- ARC-AGI at 32x32 or 64x64 pixels cannot stand in for real visual tasks.
- MMMU mostly tests language knowledge, since many questions can be answered without the image.
- Google Lens-style recognition is not reasoning, however good it is.
- Text-only chain of thought cannot solve spatial problems; visual chain of thought is needed.

## Tools mentioned
Google Lens, SAM3, YOLO, Mask R-CNN, Siemens simulators, ByteDance Seedance (rendered as C-Dance in transcript)

## Relevance to our work
- **prosharness** (1/3): If ProsHarness checks screenshots or UI state from the Claude Code CLI, the talk's warning about hallucinated visual answers applies to those checks. → *When ProsHarness verifies screenshot or UI results, ask the model only narrow yes/no visual questions and confirm them with a deterministic check, such as a DOM or file assertion.*
- **general** (1/3): The one-second test and the warning about pattern-matching hallucinations apply to any agent that reads images. → *Before adding a visual check to any agent eval, write a one-second-answer test case and a harder case, and see whether the model passes both.*
