# SOTA Generative Media Panel — Dumitru Erhan, Shane Gu & Nicole Brichtova, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `KLDdXOw6jIc` · [watch](https://youtu.be/KLDdXOw6jIc) · **date:** 2026-09-18 · **length:** 56:59 · **format:** panel · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Dumitru Erhan, Shane Gu, Nicole Brichtova · **orgs:** Google DeepMind, Google, Google Cloud, YouTube, Cognition, xAI, Character AI, Replicate
- **topics:** models-research, voice-multimodal, evals · **tags:** generative-media, video-generation, veo, gemini-omni, nano-banana, human-evals, reward-hacking, world-models, joint-audio-video, captioning, forward-deployed-engineers, data-quality

> Google DeepMind panel on generative media (Veo, Gemini Omni, Nano Banana): why language is a lossy conditioning channel, why human preference evals mislead, and why real-task data and FDE feedback matter.

## Summary
Three Google DeepMind researchers recap recent launches (Nano Banana 2 Lite, Gemini Omni Flash API) and then discuss where generative media is heading. They argue that video models are a complementary foundation model for space and time, and that a single generative process for audio and video (first done with Veo 3) is the right design. They say language is a useful but lossy conditioning channel, and that the field has not settled on a better intermediate representation (captions, code, or something else). On evals, they say human side-by-side preference is the main signal for close calls but is biased toward sharp, saturated output, and that free-form video editing is the hardest case to evaluate. They also describe the risks of reward hacking, the need to amortize human labels, and the value of real-world task trajectories, which mostly live inside first-party products. The talk is mostly opinion and product color with few hard numbers.

## Key ideas
- **Language is a useful but lossy conditioning channel for generation** — Speakers argue that detailed captions gave image and video generation its start, since text conditions the model on causal information. They also say language is too coarse for sound, skin tone, taste and room acoustics, so richer representations are needed. ([8:17](https://youtu.be/KLDdXOw6jIc?t=497))
- **Video models as zero-shot space-time learners** — A prior paper argued video models can solve many classic vision tasks zero-shot, and the team sees video models as a complementary foundation model next to language models. They think the long-term direction is combining visual and text reasoning, though they expect that to be incremental rather than a single unified model right away. ([9:40](https://youtu.be/KLDdXOw6jIc?t=580))
- **Veo 3 generated audio and video in one latent process** — Joint audio-visual generation was presented as the right design because lip movement and sound come from the same underlying process. The older approach of generating pixels first and syncing lips afterward was called very bad. ([24:31](https://youtu.be/KLDdXOw6jIc?t=1471))
- **Human preference can reward the wrong thing** — In side-by-side tests, people often preferred generated video over real videos with the same caption, because the output looked sharper and more HDR. Speakers warn that a human's preference is not a reliable guide to what should be optimized, and that trained experts notice details that average raters miss. ([33:28](https://youtu.be/KLDdXOw6jIc?t=2008))
- **Default aesthetic is a product decision, and reward hacking shows up in odd ways** — A Nano Banana Pro infographic trend was too cluttered, and the team had to tune the default. A tester found that the model kept adding wedding rings to hands, which the speaker called a common reward-hacking pattern. ([38:10](https://youtu.be/KLDdXOw6jIc?t=2290))
- **Free-form video editing is the hardest thing to evaluate** — Automated judges are less mature for media than for LLMs. The team relies on large human eval runs, live experiments, and early-access testers who use the models in real workflows. Text rendering is easier to check automatically, for example with OCR, because one wrong letter makes the asset unusable. ([42:42](https://youtu.be/KLDdXOw6jIc?t=2562))
- **Amortize human labels into automated evaluators** — Speakers say human judgment work should gradually be turned into learned evaluators. They point to video understanding, such as detecting AI-generated inconsistencies in famous scenes, as an important task in its own right. ([45:18](https://youtu.be/KLDdXOw6jIc?t=2718))
- **Real-task trajectories are scarce and mostly live inside products** — The most useful data would be how people actually move through a task, such as a campaign from one product photo to many ad formats. That data often sits in first-party product surfaces or with vendors, not in public video, so it is hard to collect. The speakers say 99 percent of the information is inside people, and that the internet holds only the outputs. ([50:39](https://youtu.be/KLDdXOw6jIc?t=3039))
- **Forward-deployed engineers as a feedback loop into model training** — The speakers want FDEs to do more than sales. They should collect failure cases from customers, such as a rug pattern at a custom size or brand colors that must match a specific shade, and send them upstream to model teams and eval work. ([52:44](https://youtu.be/KLDdXOw6jIc?t=3164))

## Techniques
- **Side-by-side human preference eval for close model comparisons** — Show raters or an internal room two outputs from candidate checkpoints, ask which they prefer, and decide based on the pattern. Use a trusted-tester group with weekly feedback calls for continuous signal. *When:* When two checkpoints are close and automated metrics do not separate them. Watch for bias toward sharp, saturated, or dense output, and check the result against expert judgment.
- **Deterministic checks for rendered text** — Run OCR over generated images and check the text. Any single wrong character marks the asset as failed. *When:* For image generation tasks where text must be correct, such as infographics, ads, or product instructions.
- **Early-access programs before broad release** — Give a set of expert users the model before launch, collect feedback on their real workflows, and fix regressions before wider release. *When:* For creative or media models, where a benchmark can improve while a real workflow breaks, and where experts notice details that metrics miss.
- **Amortizing human labels into a learned evaluator** — Use human judgments to train an automated judge or classifier for the same question, then reuse it at scale and keep humans for audits. *When:* When human labels are expensive and the eval must run on many outputs, such as checking video consistency.
- **Joint generation of coupled modalities in one model** — Generate video and audio together in a single generative process instead of generating one and then syncing the other with a separate hack. *When:* When the modalities depend on each other in time, such as lip sync or sound that matches the scene distance.

## Numbers
- Nano Banana 2 Lite gives about three-second latency and is described as faster, cheaper, and better than the original Nano Banana (speaker's claim). ([2:28](https://youtu.be/KLDdXOw6jIc?t=148))
- Gemini Omni Flash API is priced the same as Veo 3 Fast (speaker's statement). ([2:28](https://youtu.be/KLDdXOw6jIc?t=148))
- In a side-by-side test, human raters largely preferred Omni-generated video over real videos made from the same captions. No sample size was given. ([33:28](https://youtu.be/KLDdXOw6jIc?t=2008))
- The team runs human evals on thousands of items per release, and sometimes uses live experiments for small differences at large scale. ([43:59](https://youtu.be/KLDdXOw6jIc?t=2639))

## Hot takes
- Captioning is probably an inefficient intermediate representation, and code (such as Manim or FFmpeg) may be a better one.
- Prompt engineering will not disappear, because fine sensitivity to output is what lets a person control the model.
- Video models are a missing foundation model needed for AGI, not only a tool for pretty videos.
- Human preference is not a reliable target to optimize for.
- Multiple specialized generative models will likely coexist for at least the next six months, despite the Omni name.

## Tools mentioned
Veo 3, Gemini Omni, Nano Banana, Nano Banana Pro, Nano Banana 2 Lite, Manim, FFmpeg, Stable Diffusion, OCR

## Relevance to our work
- **agentos** (1/3): Human preference and LLM judgments are noisy for generative outputs. The talk points out where a deterministic check exists, such as OCR for text, and that is useful for AgentOS evals of generated content. → *Where an agent output has a checkable property (text, schema, format), add a deterministic check to the eval set and keep human or judge scores as a secondary signal.*
