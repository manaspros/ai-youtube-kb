# From Scratch to SOTA: Training a 3B State-Space Vision Model — Krishna Prasad Srinivasan, Sarvam

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `T72nqdC92PM` · [watch](https://youtu.be/T72nqdC92PM) · **date:** 2026-09-27 · **length:** 21:09 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Krishna Prasad Srinivasan · **orgs:** Sarvam
- **topics:** data-engineering, training-finetuning-rl, models-research, voice-multimodal · **tags:** document-ocr, state-space-model, ssm, vlm, indic-languages, low-resource-languages, rlvr, synthetic-data, block-level-ocr, sovereign-ai, olmocr-bench, omnidocbench, curriculum-training

> Sarvam's Krishna Prasad Srinivasan on training Servam Vision, a 3B state-space document-OCR model built from scratch for English and 22 Indian languages, using block-level OCR, a four-stage curriculum and RL with machine-checkable rewards.

## Summary
The speaker, a GM at Sarvam, presents Servam Vision, a 3B-parameter vision-language model for document OCR. It uses a state-space model (SSM) language backbone instead of a transformer, so compute grows linearly and memory stays constant on long visual-token inputs. The team bet on block-level OCR with separate layout and reading-order modules feeding a small VLM, rather than a monolithic page-level VLM. Training runs in four stages: text-only pretraining, continual pretraining on image-text pairs, supervised fine-tuning on OCR samples, and RL with rewards that unit tests can check. The speaker argues the real moat is the data engine for low-resource Indic scripts and a curated eval layer. Reported results include SOTA claims on OlmOCR-Bench and OmniDocBench and an unbeaten lead on 22 Indian languages against frontier models, all self-reported. The talk closes with sovereignty arguments and deployments that have digitized 35M pages.

## Key ideas
- **Block-level OCR beats page-level monolithic VLMs for this task** — The team bet early (late 2025) on block-level OCR with separate layout and reading-order modules around a small VLM, instead of one model that reads whole pages. The speaker says many 2026 models converged on the same pattern. ([3:05](https://youtu.be/T72nqdC92PM?t=185))
- **SSMs trade lossy recall for linear compute on long visual-token documents** — Transformers cost grows with the square of sequence length, and long pages can reach 5k-10k visual tokens. An SSM keeps one state updated token by token, so compute is linear and memory is constant. The speaker says the lossy recall is acceptable for block-level OCR. ([4:18](https://youtu.be/T72nqdC92PM?t=258))
- **Staged curriculum: build the language prior before the model sees pixels** — Stage 1 is text-only pretraining (13T tokens across English, Indic text, math and code). Stage 2 is continual pretraining on 300M image-text pairs. Stage 3 is SFT on 100M OCR samples across 22 languages and document components. Stage 4 is RL. The speaker argues a strong language prior helps the model resolve smudged or ambiguous text. ([5:41](https://youtu.be/T72nqdC92PM?t=341))
- **The moat is the data engine and the eval layer, not the RL recipe** — The speaker calls RL a standard recipe. The real differentiators are pipelines that create synthetic and real-document data for languages with no labels, and curated evals meant to measure end-user usefulness, not just benchmark scores. ([7:59](https://youtu.be/T72nqdC92PM?t=479))
- **OCR suits RLVR because correctness is machine-checkable** — Each sampled output is scored with unit-test-style rewards, such as character error rate, table structure, or equation correctness. The model is then reinforced toward outputs above the group average. Real complex documents are preferred over synthetic ones for building these reward tests. ([8:56](https://youtu.be/T72nqdC92PM?t=536))
- **Fidelity over helpfulness: OCR should not silently correct text** — Transliteration and translation are not used, because a mistake in the image should be extracted as-is rather than changed by the model. The speaker says transliteration-based data is now appearing in OCR training, and its quality is still unclear. ([17:28](https://youtu.be/T72nqdC92PM?t=1048))
- **Sovereignty is the adoption driver for government and insurance buyers** — Customers want control over where data goes, when it is used, and how much is used. The speaker says this demand, plus the lack of Indic document coverage in frontier models, drove adoption. ([17:28](https://youtu.be/T72nqdC92PM?t=1048))

## Techniques
- **Block-level OCR with layout and reading-order modules** — Run separate layout and reading-order modules to find blocks, then send each block to a small VLM for recognition. Do not rely on one model to read whole pages. *When:* Long, dense documents where page-level VLM inference is too expensive or the output must be grounded per block.
- **Four-stage training curriculum for a domain VLM** — Pretrain the language backbone on text only, then continually pretrain on image-text pairs, then SFT on task samples, then RL. Each stage builds on the previous one. *When:* Building a specialised vision-language model from scratch, where the language backbone must be strong before vision training.
- **RLVR with unit-test rewards** — Sample a group of outputs per input, score each with deterministic checks (for example character error rate, table structure, math equivalence), and reinforce outputs that beat the group average. Repeat. *When:* Tasks where correctness can be checked by code, such as OCR, extraction or structured output.
- **Real complex documents as RL reward sources, synthetic documents for SFT** — Use synthetic documents for supervised post-training. For RL, use real complex documents so the reward tests reflect real layouts and content. *When:* Post-training where real labelled data is scarce but reward signals must be realistic.
- **Human-in-the-loop workbench with confidence scores and block grounding** — Show per-block confidence and grounding back to the source image, and let reviewers proofread with an agent, so errors can be fixed before ingestion. *When:* Enterprise document digitization where output must be auditable.

## Numbers
- Servam Vision has 3B parameters and runs on a single GPU; the speaker claims it beats models about 100x larger on document AI ([0:16](https://youtu.be/T72nqdC92PM?t=16))
- Well under 1% of the common corpus used to train frontier models has Indian-language representation (cited from a published language distribution study) ([1:41](https://youtu.be/T72nqdC92PM?t=101))
- Visual tokens per long page can reach 5,000-10,000, which makes transformer compute and memory costly ([5:41](https://youtu.be/T72nqdC92PM?t=341))
- Stage 1 text pretraining: 13 trillion tokens ([5:41](https://youtu.be/T72nqdC92PM?t=341))
- Stage 2 continual pretraining: 300 million image-text pairs ([6:36](https://youtu.be/T72nqdC92PM?t=396))
- Stage 3 SFT: 100 million OCR samples across 22 Indian languages plus English ([6:36](https://youtu.be/T72nqdC92PM?t=396))
- OlmOCR-Bench score at launch: 84.3 (SOTA claim, self-reported) ([10:04](https://youtu.be/T72nqdC92PM?t=604))
- OmniDocBench score at launch: 93.2 (SOTA claim, self-reported) ([10:04](https://youtu.be/T72nqdC92PM?t=604))
- Claimed unbeaten lead on 22 Indian languages against Gemini, ChatGPT and Opus (no numbers given) ([10:04](https://youtu.be/T72nqdC92PM?t=604))
- More than 35 million pages digitized by large enterprises and governments about four months after launch ([11:28](https://youtu.be/T72nqdC92PM?t=688))
- Training data is about 40% Indic, with the rest English, math and code (answer to a Q&A question) ([19:58](https://youtu.be/T72nqdC92PM?t=1198))

## Hot takes
- Frontier models do not handle complex Indian-language documents well, and sovereign data-creation is needed before personalised agents in local languages are possible.
- For OCR, RL with machine-checkable rewards scales far better than most post-training work, because correctness is deterministic.
- Block-level small-model OCR beats the page-level monolithic VLM trend for production document work.
- The speaker argues the data engine and evals are the real moat, not the training recipe.

## Tools mentioned
Servam Vision, Akshar (agentic document workbench), OlmOCR-Bench, OmniDocBench, Qwen, Gemma

## Relevance to our work
- **agentos** (1/3): The RLVR-with-deterministic-rewards pattern and the emphasis on eval as the moat are loosely related to AgentOS SkillForge's open question about a success signal for skill-worthiness. The talk is about training a vision model, which is outside AgentOS's current scope. → *Optional read: note how deterministic unit-test rewards define success in RLVR, and consider whether the same checks could define a success signal for SkillForge skill mining.*
