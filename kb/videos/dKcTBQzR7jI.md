# Skill issue: stop deploying vision language models, use them with Skills — Merve Noyan, Hugging Face

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `dKcTBQzR7jI` · [watch](https://youtu.be/dKcTBQzR7jI) · **date:** 2026-09-27 · **length:** 19:14 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Merve Noyan · **orgs:** Hugging Face, TII, Roboflow
- **topics:** voice-multimodal, data-engineering, training-finetuning-rl, evals · **tags:** vision-language-models, object-detection, RF-DETR, auto-labeling, VLM-as-judge, ensemble-judges, license-selection, coding-agents, Hugging-Face, small-models, segmentation, distillation-to-detector

> Merve Noyan (Hugging Face) argues against running VLMs for real-time vision and shows a pipeline where VLMs label and judge data to train small Apache-2.0 detectors such as RF-DETR, plus a toolkit of models exposed as agent tools.

## Summary
The speaker says developers use vision language models (VLMs) for everything, which rules out real-time use, and that small trained detectors like RF-DETR beat VLMs on detection. She also warns about licenses, asking people to prefer Apache 2.0 or MIT models over YOLO (AGPL). She built a toolkit (called Vibevision in the transcript) that gives her favorite vision models to a coding agent as tools and includes a "vibe training" pipeline. In that pipeline a small VLM labels an image dataset, two small VLM judges (Gemma 4 E4B and LFM2.5-VL) check each labeled box by overlaying it on the image, and their verdicts are merged by minimum agreement rather than consensus. The trained RF-DETR model is then fine-tuned on the result, and she reports it works on road-sign detection (checked against ground truth) and on document parsing (where it even found a signature the labeler missed). The run uses Hugging Face jobs, serverless inference providers and buckets, and she estimates the whole pipeline costs about three to four dollars. She also lists findings: judges disagree a lot, prompt generation still needs human approval, and coding agents lack computer-vision common sense (for example flipping traffic signs horizontally). The talk ends with a list of recommended open models and future ideas like image-guided detection and IoU-based judging.

## Key ideas
- **Do not run VLMs for real-time vision; train a small specialized detector instead.** — VLMs do not reach real-time frame rates on modest hardware, and a trained RF-DETR-style detector outperforms them on detection. The VLM is used offline as a labeler, not at inference. ([1:04](https://youtu.be/dKcTBQzR7jI?t=64))
- **Check the license before the model.** — Developers often deploy AGPL models such as YOLO without knowing the obligations. License is the first filter, then benchmark performance, then personal judgement. ([1:04](https://youtu.be/dKcTBQzR7jI?t=64))
- **Pipeline: VLM labels, small VLM judges verify, then train the detector.** — A VLM labels an unlabeled image set, two smaller judges verify the boxes, and the merged verdicts become training labels for RF-DETR. The coding agent runs this long-horizon pipeline with a human supervising. ([4:05](https://youtu.be/dKcTBQzR7jI?t=245))
- **Use an ensemble of small judges, not one large judge.** — She read that several smaller judges are better than one, and says asking a VLM for a numeric confidence score does not work when judges differ in size. She uses yes/no verdicts. ([6:00](https://youtu.be/dKcTBQzR7jI?t=360))
- **Overlay the box on the image and ask a yes/no question per box.** — The labeled bounding boxes are drawn onto the image and passed to the judge with the label description. The judge only approves or rejects each box, which avoids having to parse coordinates from the judge. ([7:17](https://youtu.be/dKcTBQzR7jI?t=437))
- **Merge judges by minimum agreement (any yes keeps the example), not consensus.** — One judge (LFM) rejects far more than the other, so requiring agreement would leave very few examples. Keeping an example when either judge approves gave a usable dataset. She notes that for recall-sensitive large datasets a consensus approach could be preferable. ([11:48](https://youtu.be/dKcTBQzR7jI?t=708))
- **Coding agents lack computer-vision common sense.** — Even a strong coding agent proposed a horizontal flip on traffic signs and jitter on traffic lights, which would corrupt the data. She added explicit augmentation rules to the agent's instructions. ([13:02](https://youtu.be/dKcTBQzR7jI?t=782))
- **Human approval is still needed for generated judge prompts.** — The agent drafts the label descriptions and judge prompts, but a person must check them against the dataset. She says there is no escape from looking at the data. ([11:48](https://youtu.be/dKcTBQzR7jI?t=708))

## Techniques
- **VLM as offline labeler, small detector at runtime** — Label an unlabeled image set with a ~3.5B VLM, then train an RF-DETR detector on the labels so inference is fast and cheap. *When:* You need real-time detection but have images without labels.
- **Overlay-and-ask judging** — Draw each candidate bounding box onto the image, pass the image with the label description to a small VLM judge, and ask approve or reject for that box. *When:* You want to verify auto-generated boxes without parsing VLM coordinate output.
- **Ensemble of small judges with any-yes merge** — Run two or more small judges of different families over the same items and keep an item if any judge approves it. Do not use numeric scores across different model sizes. *When:* A single judge is unreliable or one judge is too strict and consensus would discard most data.
- **License-first model selection** — Filter candidate models to Apache 2.0 or MIT before comparing benchmarks; check license per size variant because one size may differ. *When:* Choosing models for anything that will be deployed commercially.
- **Agent with domain rules and human checkpoints** — Let a coding agent run the multi-step labeling and training pipeline, add explicit domain rules such as which augmentations are forbidden, and require a person to approve generated prompts or labels. *When:* Running long pipelines where the agent lacks domain common sense.
- **Models exposed as agent tools** — Package favourite models as callable tools so a coding agent can pick a detector, segmenter or OCR model for a task. *When:* Giving a coding agent the ability to build vision apps without deep domain knowledge.

## Numbers
- VLMs typically reach only about 30-40 FPS on a toaster-class device in the speaker's comparison, which is not real time. ([1:04](https://youtu.be/dKcTBQzR7jI?t=64))
- Whole pipeline (labeling, judging, training) costs about 3-4 dollars per run per the speaker's benchmark. ([8:40](https://youtu.be/dKcTBQzR7jI?t=520))
- Labeling was cheapest on DeepInfra serverless; Together is said to be better for batch processing; judging ran on Hugging Face jobs; training on an L4 GPU. ([8:40](https://youtu.be/dKcTBQzR7jI?t=520))
- Document-parsing and road-sign tests reported only a 'good' mAP@50 with a bit of a gap to ground-truth annotations; no exact figure was given. ([9:44](https://youtu.be/dKcTBQzR7jI?t=584))
- Falcon Perception is about 600 million parameters under Apache 2.0. ([14:17](https://youtu.be/dKcTBQzR7jI?t=857))
- The large depth-estimation model has a non-commercial license while the other sizes are Apache 2.0. ([15:29](https://youtu.be/dKcTBQzR7jI?t=929))

## Hot takes
- Stop deploying VLMs directly for vision tasks; train a small detector instead.
- Most developers do not read licenses and deploy AGPL models such as YOLO without realising the obligations.
- Asking a VLM for a confidence score is unreliable when judges differ in size; use yes/no verdicts.
- Coding agents are clueless computer-vision engineers without explicit domain rules.

## Tools mentioned
RF-DETR, Gemma 4 E4B, LFM2.5-VL, Qwen VLM (auto-caption reads 'Q1 3.5', ~3.5B), Falcon Perception, Moondream 3, MM Grounding DINO, SAM 3.1, Supervision (Roboflow), Hugging Face Jobs, Hugging Face Inference Providers, Hugging Face buckets, DeepInfra, Together, transformers v5, OlmOCR benchmark, Claude Opus 4.8, GLM 5.2, YOLO

## Relevance to our work
- **general** (2/3): Relevant to cheap-model pipelines and LLM-as-judge: small judges with yes/no per item and a merge rule, plus the recall-versus-consensus trade-off, applies to entity resolution and data-quality labeling. → *Read the judge-ensemble section around 6:00 to 11:48 and test a yes/no per-item judge with any-yes merging on an entity-resolution labeling sample.*
- **agentos** (1/3): Ensemble-judge labeling for small models is loosely related to MemoryMesh or SkillForge evals, but the talk is about vision. → *Optional: when next building an LLM-as-judge eval for AgentOS, compare any-yes versus consensus merging on a labeled slice and measure recall.*
- **prosharness** (1/3): Shows a long-horizon agent pipeline that needs human checkpoints and explicit domain rules, which matches the ProsHarness plan and approval flow. → *Consider adding a per-domain rules file and a required human approval step before the agent runs destructive or data-changing actions in long ProsHarness loops.*
