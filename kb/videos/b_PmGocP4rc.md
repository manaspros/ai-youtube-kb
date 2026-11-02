# Evaling Video Slop — Maor Bril, Character.ai

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `b_PmGocP4rc` · [watch](https://youtu.be/b_PmGocP4rc) · **date:** 2026-08-18 · **length:** 23:13 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Maor Bril · **orgs:** Character.ai
- **topics:** evals, testing-verification, voice-multimodal, agent-architecture · **tags:** video-generation, llm-as-judge, pairwise-comparison, distillation, vlm, human-calibration, eval-in-the-loop, shortcut-learning, qwen, dolby-atmos

> Maor Bril (Character.ai) on evaluating AI video: frame-level metrics miss story, physics and pacing, so he distilled a judge committee into a small fast VLM trained on pairwise comparisons and run inside the generation loop.

## Summary
The speaker argues that video generation improved quickly but video evaluation did not, because common metrics such as CLIP-style scores and frame-drift checks look at single frames and prompt match, not whether the story works. Human judging is accurate but slow and costly, and LLM judges are slow and sensitive to prompt wording. He built a repeatable benchmark that combines frame metrics with LLM judges calibrated by periodic human annotation sessions. The main move was distilling that expert committee into a small VLM that scores a 15-second video in about 3 seconds and explains its low scores. Training on absolute 1-10 ratings produced confident but wrong scores, so he switched to pairwise A-vs-B training with manufactured bad videos. A later real-versus-AI pairing step risked teaching an AI detector, which he guarded against with matched encoding and identical annotation. He also moved from a fixed pipeline to an agent that validates its own output, and closed with three rules: compare relatively, score the axes you care about, and put eval inside the generation loop.

## Key ideas
- **Video evaluation has lagged video generation.** — Generation is cheap and strong, but judging quality still relies on squinting. Tools built for text and images (CLIP-style prompt match, frame-drift checks) judge single frames and prompt match, not whether the story was told. ([0:08](https://youtu.be/b_PmGocP4rc?t=8))
- **Frame metrics miss the axes that matter for video.** — Story, physics, character identity across shots, pacing and audio-visual sync only exist over time. Frame-level tools cannot see them, so they need separate measures. ([2:20](https://youtu.be/b_PmGocP4rc?t=140))
- **LLM-as-judge is slow, expensive and prompt-sensitive, so calibrate it with humans.** — Each harness report gets human annotation, and that feedback is fed back into the judge prompt. Because humans are costly, the judge is only as good as its calibration. ([4:35](https://youtu.be/b_PmGocP4rc?t=275))
- **Catch drift early, before stitching.** — Starting frames for shots are generated from earlier frames, so a character drifting between two starting frames is cheap to fix. Long videos are many short clips, so a drifted 6-second clip should be regenerated before assembly. ([5:48](https://youtu.be/b_PmGocP4rc?t=348))
- **Distill an expert committee into one small, fast model that explains its verdict.** — The small VLM returns why a clip is low (extra limb, bad physics, audio out of sync), not just a number. A bigger model scored better but was too slow, so the smaller model was chosen. Scoring a 15-second clip takes about 3 seconds. ([8:08](https://youtu.be/b_PmGocP4rc?t=488))
- **Train on pairwise comparisons, not absolute ratings.** — People disagree on what a 6 means but agree on which of two clips tells a better story. Training on A-vs-B pairs generalises to better-or-worse, and bad examples were manufactured by corrupting good clips or generating random flops. ([9:24](https://youtu.be/b_PmGocP4rc?t=564))
- **The first version was confidently wrong because it learned the vibe, not the axes.** — It gave a 9.2 for camera work on a clip where the camera did not move for four seconds. It learned the polished gloss of generated video rather than whether the story held. The label scheme, not the model, was the cause. ([10:41](https://youtu.be/b_PmGocP4rc?t=641))
- **Real-vs-AI pairs help, but they can teach an AI-detector shortcut.** — Pairing real footage with AI footage raised the risk of the model learning to spot AI rather than quality. Mitigations were matching the encoding of both sides and annotating all axes the same way on both. ([11:58](https://youtu.be/b_PmGocP4rc?t=718))
- **Replace the fixed pipeline with an agent that verifies its own output.** — Pipelines fit narrow use cases but drift when users bring their own characters, images and voices. Giving an agent validation tools lets it check and fix its work as it goes. ([13:10](https://youtu.be/b_PmGocP4rc?t=790))
- **Three rules: compare relative, score the real axes, and put eval inside the generation loop.** — Pairwise comparison beats absolute scores. Score the axes you care about (storytelling, pacing, physics) rather than hoping they appear. Move evaluation as close to generation as possible, because earlier catches are cheaper. ([14:15](https://youtu.be/b_PmGocP4rc?t=855))
- **Audio sync is checked by timestamp and loudness, and lip sync is still unsolved.** — Dolby Atmos is used to keep audio quality understandable. The model matches sound spikes to the timestamps of frames where a prompted event such as a door slam happens. Lip sync for talking animations is still unsolved. ([15:42](https://youtu.be/b_PmGocP4rc?t=942))
- **Human annotation is a standing process that also produces training data.** — Teams run 10-15 minute annotation sessions with randomly assigned clips and axes. The results calibrate the AI judges and become the dataset for the next model version. Taste is subjective, so this is ongoing rather than one-off. ([18:32](https://youtu.be/b_PmGocP4rc?t=1112))
- **Cost depends on scale and the build-versus-buy trade.** — A small model can be served on one GPU or scaled to many instances. The trade is training and curation time against serving cost, compared with calling a frontier model per clip, which adds up at thousands per day. ([20:58](https://youtu.be/b_PmGocP4rc?t=1258))

## Techniques
- **Pairwise A-vs-B judge training** — Collect pairs of clips and label which is better on one axis instead of asking for 1-10 scores. Train the judge on the pairs, then use it for relative ranking. *When:* Subjective quality where absolute scores drift between raters, such as storytelling or taste.
- **Manufactured negatives** — Build bad examples by corrupting good clips (for example by breaking frames or sync) or by generating random flops, and pair them with good clips. *When:* Good examples are plentiful but bad ones are rare or unlabeled.
- **Matched-encoding real-vs-AI pairing with identical annotation** — Pair real footage with AI footage only after encoding both sides the same way and annotating all axes with the same procedure, so the model cannot separate them by artifacts. *When:* You want a quality judge from real-vs-generated contrast but must avoid training an AI detector.
- **Expert-committee distillation into a small VLM** — Run a set of metric and frontier-model judges to produce labels, train a small VLM on them, and have it output reasons along with scores. *When:* The judge must run inside a fast generation loop and cost or latency rules out calling large models each time.
- **Eval inside the generation loop** — Score each short generation as it is made and regenerate drifted pieces before they are assembled into a longer output. *When:* Errors are cheaper to fix early, and long outputs are built from many short segments.
- **Calibration sessions with randomized annotation** — Run short recurring human sessions where raters label randomly assigned items across several axes, then use the labels to recalibrate the judge and as training data for the next version. *When:* The judge needs ongoing alignment with human taste and the domain has no fixed ground truth.
- **Agent with validation tools** — Give the generating agent tools that score its own output so it can check and correct as it works, instead of running a fixed multi-step pipeline. *When:* Users bring varied inputs that break a fixed pipeline.

## Numbers
- Small VLM scores a 15-second video in about 3 seconds; a bigger model was better but significantly slower. ([8:08](https://youtu.be/b_PmGocP4rc?t=488))
- V1 gave a 9.2 for camera work on a clip where the camera did not move for four seconds. ([10:41](https://youtu.be/b_PmGocP4rc?t=641))
- Regenerating a drifted 6-second clip before assembly is the unit of correction for long-form video. ([5:48](https://youtu.be/b_PmGocP4rc?t=348))
- Human annotation sessions run 10-15 minutes each, periodically. ([18:32](https://youtu.be/b_PmGocP4rc?t=1112))
- Speaker has been at the company a bit over two years. ([0:08](https://youtu.be/b_PmGocP4rc?t=8))

## Hot takes
- Pairwise A-vs-B judgments beat absolute 1-10 scores for subjective quality, because raters agree on which of two is better but not on what a 6 means.
- A judge trained on absolute ratings of generated media learns the polished gloss, not the axes you care about.
- Real-vs-AI pairs are a trap unless encodings and annotation are matched, since the model will learn to detect AI rather than judge quality.
- Evaluation should sit inside the generation loop, because catching drift early is much cheaper than fixing a finished long video.

## Tools mentioned
Qwen (small VLM, post-trained), Dolby Atmos (audio quality), CLIP-style frame metrics, frame-drift metrics, Kling, Seedance, Veo, Sora, OpenTelemetry (requested, planned for harness)

## Relevance to our work
- **prosharness** (2/3): ProsHarness checks plan critiques and loop outputs. The talk's point that relative comparison beats absolute scoring, and that verification should sit inside the agent loop, applies directly to the plan to critique to debate flow. → *Try a pairwise check in the ProsHarness critique step: have the reviewer pick the better of two plans rather than give each a score, and log whether the verdicts agree across runs.*
- **general** (2/3): Entity-resolution match review is a pairwise decision, and the talk's warning about shortcut learning from manufactured negatives applies to the ER harness. → *On the ER hard cases, test pairwise judging ('which of these two record pairs is the same entity') against absolute match scores, and check whether the judge learns a shortcut such as the fils/associes pattern.*
- **agentos** (1/3): The lesson on distilling a multi-judge committee into a small fast model applies to eval serving on InferCraft, but the talk is about video and does not cover LLM serving. → *Read only if we build a small judge model for AgentOS evals; otherwise skip.*
