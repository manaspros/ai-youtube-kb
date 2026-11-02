# Training Krea 2: What matters in generative model training — Sangwu Lee, Krea.ai

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `-tviRdpmHvs` · [watch](https://youtu.be/-tviRdpmHvs) · **date:** 2026-09-18 · **length:** 21:46 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sangwoo Lee · **orgs:** Krea.ai
- **topics:** models-research, data-engineering, training-finetuning-rl · **tags:** image-generation, diffusion, data-curation, deduplication, captioning, sparse-autoencoders, rlhf, grpo, prompt-expansion, synthetic-data, stylistic-diversity

> Krea's Sangwoo Lee on training the Krea 2 image model: data curation for stylistic diversity, cascaded dedup and classifier filters, and an LLM-style post-training pipeline with RL.

## Summary
Sangwoo Lee from Krea.ai describes how the team trained Krea 2, an image foundation model, and open-sourced a medium variant. The stated goal is stylistic diversity, as opposed to the mode-collapsed, reliable-but-average outputs he attributes to large-lab models. He argues that after the architecture is fixed, most of the work is data curation, and that the data outlasts any particular training code. The data pipeline covers a cascade of hash-based then embedding-based deduplication, a two-pass captioner (OCR then a vision-language model), and filters distilled from large VLM judgments into small classifiers. Sparse autoencoder features are used as an unsupervised tagger for artifacts such as watermarks, and Wikipedia PageRank is used to check that important concepts are covered. Training follows an LLM-like sequence: progressive resolution pretraining (256 to 1K), mid-training, SFT, preference optimization, GRPO-style RL against reward servers, and a prompt-expander LLM that lengthens user prompts. He closes with future directions: multi-expert on-policy distillation, removing the VAE and text encoder, and using VLM-generated bounding boxes or scene graphs as conditioning.

## Key ideas
- **Krea 2 targets stylistic diversity, not average-looking consistency** — Speaker contrasts large-lab image models, which are slow and reliable but mode-collapse toward a boring average (for example, a centered average person), with a faster, more exploratory model for creative studios. ([0:12](https://youtu.be/-tviRdpmHvs?t=12))
- **Data is most of the work once the architecture is locked** — Speaker says data is 'quite everything'. The team avoids cutting stylistic diversity by accident, such as dropping low-res CRT aesthetics, and does not rely only on standard aesthetic or quality scores. ([5:19](https://youtu.be/-tviRdpmHvs?t=319))
- **Bad data is defined by specific failure modes** — Named failure modes: duplicates, overrepresented concepts, captioner blind spots (for example, a painting's wall-hanging context is never mentioned), text-dense images at low resolution, and AI-generated images. ([6:40](https://youtu.be/-tviRdpmHvs?t=400))
- **Synthetic AI images are excluded because they make the model sticky** — Training on ChatGPT or Nano Banana outputs gives a shortcut to a good model but imprints that house aesthetic, which the speaker says he can recognize. He also says distillation-only work is not the research he wants to do. ([6:40](https://youtu.be/-tviRdpmHvs?t=400))
- **Captioning is a multi-stage pipeline** — OCR extracts visible text first (text rendering matters), optional metadata such as a famous person's identity is added, a VLM writes a detailed caption, and a final step rewrites the caption into the target prompt format. ([8:04](https://youtu.be/-tviRdpmHvs?t=484))
- **Deduplication runs as a cascade over 2 to 10 billion images** — Cheap hash-based dedup (pHash or MD5) runs first. Embedding-based near-duplicate removal is used only once the set is smaller. ([9:28](https://youtu.be/-tviRdpmHvs?t=568))
- **Large VLM judgments are distilled into small classifiers** — A VLM is prompted to judge properties such as 'looks like an AI image'. Its decisions are distilled into a small CLIP-style (SigLIP-sized) classifier so it can run over a billion images. He cites a text-data analogue where a big LLM labels data and a ~500M model is distilled to run at pretraining scale. ([9:28](https://youtu.be/-tviRdpmHvs?t=568))
- **Sparse autoencoder features work as unsupervised tags** — Features from an SAE trained on a vision model fire on concepts such as horse or black-and-white or blurry, and can flag watermarks, signatures, and border artifacts for removal or oversampling. ([12:08](https://youtu.be/-tviRdpmHvs?t=728))
- **Concept coverage is checked against Wikipedia PageRank** — Wikipedia concepts in the top ~10% by PageRank are treated as important. Those keywords are searched in the dataset by plain text or embedding search to confirm coverage. About 30 to 40 in-house classifiers and heuristics were used in total. ([13:31](https://youtu.be/-tviRdpmHvs?t=811))
- **Training follows an LLM-style recipe with progressive resolution** — Pretraining starts at low resolution, where text-to-image semantics are learned, and scales to 1K. The sequence is then mid-training, SFT, preference optimization, and RL. ([14:56](https://youtu.be/-tviRdpmHvs?t=896))
- **RL uses reward servers, GRPO-style** — The model generates images that are scored by reward servers. The signal is used to improve text rendering and anatomy/structure. The speaker says RL is now standard in diffusion as it is in LLMs. ([16:15](https://youtu.be/-tviRdpmHvs?t=975))
- **A prompt-expander LLM is required for production** — A small LLM expands a short user prompt into a long detailed prompt, which the speaker says is closer to the training distribution and produces better images. ([17:39](https://youtu.be/-tviRdpmHvs?t=1059))
- **Iteration speed and low hyperparameter count matter most** — Speaker says data is durable while code and training recipes change, so good data stays valuable. He prefers recipes with few hyperparameters and reuses LLM kernels and research. ([19:04](https://youtu.be/-tviRdpmHvs?t=1144))

## Techniques
- **Cascaded dedup** — Run cheap hash dedup (pHash or MD5) over the full corpus, then embedding-based near-duplicate and semantic dedup on the smaller remainder. *When:* Very large image or text corpora where embedding dedup over everything is too expensive.
- **VLM-judge distillation into a small classifier** — Prompt a large VLM to make a quality or property decision (for example, AI-generated or not), then train a small CLIP/SigLIP-sized classifier on those labels and run it over the whole dataset. *When:* Filtering at billion-item scale where calling the big model per item is too costly.
- **SAE feature tagging for data hygiene** — Train a sparse autoencoder on the vision encoder. Use activated features as off-the-shelf tags and filter or oversample on features for artifacts such as watermarks or borders. *When:* Finding unwanted visual artifacts without labeled data.
- **Two-pass captioning with OCR** — OCR extracts visible text, optional metadata is attached, a VLM writes a detailed caption, and a final rewrite produces the target format. Then check captions for systematic omissions. *When:* Training text-to-image models where text rendering and specific context must be captured.
- **Concept coverage via external importance ranking** — Rank Wikipedia concepts by PageRank, take the top percentile as important, and search the dataset for each keyword by text or embedding to confirm coverage. *When:* Making sure a training set covers important concepts without hand-listing them.
- **Progressive resolution pretraining** — Train at low resolution first to learn semantics, then scale resolution up (here 256 to 1K) to learn structure and detail. *When:* Diffusion or image model pretraining where high-resolution training is expensive.
- **Prompt expansion model** — Use a small LLM to expand short user prompts into long detailed prompts that resemble the training captions. *When:* Production image models where users type short prompts.

## Numbers
- Large-lab image models take up to about 1 to 2 minutes per output (speaker's estimate) ([1:30](https://youtu.be/-tviRdpmHvs?t=90))
- Training corpus of 2 to 10 billion images, which is why cheap hash dedup comes first ([9:28](https://youtu.be/-tviRdpmHvs?t=568))
- Resolution scaled progressively from 256 to 1K ([14:56](https://youtu.be/-tviRdpmHvs?t=896))
- Concept importance threshold: top ~10% by Wikipedia PageRank ([13:31](https://youtu.be/-tviRdpmHvs?t=811))
- About 30 to 40 in-house classifiers, heuristics and filters ([13:31](https://youtu.be/-tviRdpmHvs?t=811))
- Distillation target of roughly 500M parameters for text filtering, cited from the EssentialWeb literature ([10:46](https://youtu.be/-tviRdpmHvs?t=646))

## Hot takes
- Once the architecture is locked, data curation is most of the work, and data outlasts any training code.
- Training image models on AI-generated images is a shortcut that makes every model share one recognizable house aesthetic, so AI images should be removed.
- Image generation is a proxy for progress in multimodal LLMs, so better visual-language models should drive better image conditioning, such as bounding boxes and scene graphs.

## Tools mentioned
Krea 2, pHash, MD5, SSCD, SigLIP, CLIP, sparse autoencoder, GRPO, OCR, VLM

## Relevance to our work
- **general** (2/3): The distill-a-big-judge-into-a-small-classifier filter pattern and the cascaded dedup approach apply to LLM-driven data quality and entity-resolution pair labeling, and to cheap-model pipelines. → *For the ER pair-labeling work, try distilling a large-model judgment pass into a small classifier, with a held-out check against the large model, and cascade a cheap hash or blocking pass before any embedding step.*
