# Gemma 4 Deep Dive — Cassidy Hardin, Researcher, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_A367W_qvc8` · [watch](https://youtu.be/_A367W_qvc8) · **date:** 2026-05-18 · **length:** 19:03 · **format:** talk · **quality:** 4/5 · **depth:** deep
- **speakers:** Cassidy Hardin · **orgs:** Google DeepMind
- **topics:** models-research, inference-serving, local-ai · **tags:** gemma-4, open-weights, attention, sliding-window, grouped-query-attention, mixture-of-experts, per-layer-embeddings, on-device, vision-encoder, audio-conformer, apache-2.0, kv-cache

> Google DeepMind researcher walks through Gemma 4's architecture: interleaved local/global attention, asymmetric GQA, per-layer embeddings in flash memory, a shared-expert MoE, and flexible image token budgets.

## Summary
Cassidy Hardin, a Google DeepMind researcher, presents the technical design of the Gemma 4 open model family, released the week before the talk under an Apache 2.0 license. The family has four sizes: two on-device "effective" models (E2B, E4B) that take text, vision and audio input, a 26B mixture-of-experts model, and a 31B dense model. The attention design interleaves local sliding-window layers with global layers, and the global layers use a different grouped-query ratio with larger key/value heads. The on-device models store a per-layer embedding table in flash memory instead of VRAM, which the speaker presents as the main memory saving. The talk then covers vision (variable aspect ratio and resolution, with a selectable soft-token budget that replaces Gemma 3's pan-and-scan), audio (a 305M conformer on mel-spectrogram features), and the deployment options (self-host or cloud). Most numbers are self-reported and the talk contains a few internal inconsistencies, such as the 26B active-parameter count.

## Key ideas
- **Gemma 4 has four sizes: two on-device effective models (E2B, E4B) plus a 26B MoE and a 31B dense model, all released under Apache 2.0.** — The license change was made on purpose so everyday developers can use the models from testing through deployment. The on-device models take text, vision and audio input and produce text output. ([0:00](https://youtu.be/_A367W_qvc8?t=0))
- **The attention stack interleaves local sliding-window layers with global layers, and the last layer is always global.** — The larger models use a 5:1 local-to-global ratio and the 2B uses 4:1. The sliding windows are 512 tokens on small models and 1,024 on large ones. Global layers still attend to all preceding tokens, which keeps them the expensive part. ([3:46](https://youtu.be/_A367W_qvc8?t=226))
- **Grouped-query attention is set differently for local and global layers.** — Local layers share one key/value head across 2 queries. Global layers share one across 8 queries and use a key/value head dimension of 512 instead of 256, to offset the quality loss from fewer KV heads while keeping memory and serving cost low. ([5:03](https://youtu.be/_A367W_qvc8?t=303))
- **The 26B model is a MoE with one always-on shared expert and 128 routed experts, of which 8 are selected per token.** — The shared expert is about three times the size of a routed expert. The speaker gives the active parameter count as 3.9B in one place and 3.8B in another. ([1:02](https://youtu.be/_A367W_qvc8?t=62))
- **On-device models move the per-layer embedding table into flash memory instead of VRAM.** — Each layer gets its own 256-dimensional lookup for every token, which is projected up to the model width at the end of each block. The speaker says VRAM is the main limit on phones and laptops, so this trades a small amount of extra compute for much less VRAM. ([7:35](https://youtu.be/_A367W_qvc8?t=455))
- **Images use variable aspect ratio and variable resolution, with a token budget chosen by the developer.** — Gemma 3's pan-and-scan split an image into squares and sent several crops through the model one after another. Gemma 4 keeps spatial position encodings and offers five resolution and soft-token budget levels, so OCR and detection can get a larger budget while text-only apps use a smaller one. ([11:02](https://youtu.be/_A367W_qvc8?t=662))
- **Audio uses a mel-spectrogram front end, two convolution layers, and a 305M conformer on the E2B and E4B models.** — The conformer adds a convolution layer to the architecture used by the dense and MoE models. It targets speech recognition and translation. ([16:15](https://youtu.be/_A367W_qvc8?t=975))

## Techniques
- **Interleaved local/global attention with sliding windows** — Most layers attend only to a fixed window of recent tokens (512 small, 1,024 large); a periodic global layer, always including the last one, attends to the full context. Global layers get their own GQA ratio. *When:* Long context (256K on the 31B) where full attention in every layer is too costly in memory and serving time.
- **Asymmetric GQA by layer type** — Use many queries per KV head in global layers (8:1) and fewer in local layers (2:1), and make the global KV heads wider (512 vs 256) to recover quality. *When:* When the layers that need full context are the main memory cost and you want to cut their KV size without losing too much capacity.
- **Per-layer embedding tables offloaded to flash** — Keep a low-dimensional (256) per-layer token embedding table in flash storage, look up each token's entry at the end of each block, and project it up to the model width. *When:* On-device inference where VRAM or RAM is the binding constraint and some extra latency per layer is acceptable.
- **Developer-selected image token budget** — Feed images at native aspect ratio and pick one of five resolution/soft-token budgets, pooling each 3x3 group of 16x16 patches into one soft token. *When:* Choose a high budget (560 or 1120) for OCR and object detection and a low budget when images are incidental.
- **Shared-plus-routed MoE** — Route each token through one always-active shared expert, which is larger than the others, plus the top 8 of 128 small routed experts. *When:* When you want more total capacity than a dense model of the same per-token compute allows.

## Numbers
- 31B dense model ranks #3 on the global AI arena leaderboard, which the speaker says beats models more than 20 times its size (self-reported) ([2:18](https://youtu.be/_A367W_qvc8?t=138))
- 26B and 31B models both rank in the top six of open-source models on LM Arena ([1:02](https://youtu.be/_A367W_qvc8?t=62))
- 31B context length is 256K tokens ([2:18](https://youtu.be/_A367W_qvc8?t=138))
- 26B MoE has 128 experts, 8 active per token, with about 3.8-3.9B active parameters (the speaker gives both numbers) ([1:02](https://youtu.be/_A367W_qvc8?t=62))
- Sliding windows of 512 tokens (small models) and 1,024 tokens (large models); local-to-global ratio 5:1 (4:1 on the 2B) ([5:03](https://youtu.be/_A367W_qvc8?t=303))
- Global layers use 8 queries per KV head and a KV head dimension of 512, versus 2 queries per KV head and 256 in local layers ([6:08](https://youtu.be/_A367W_qvc8?t=368))
- E2B has effective ~2.3B parameters and ~5.1B total representational parameters ([7:35](https://youtu.be/_A367W_qvc8?t=455))
- Embedding dimension is 1,536 for E2B and 2,560 for E4B; the per-layer embedding dimension is 256; layer counts are 35 (2B) and 42 (larger) ([8:56](https://youtu.be/_A367W_qvc8?t=536))
- Vision encoder is 550M parameters for 31B and 26B, and 150M for E2B and E4B ([11:02](https://youtu.be/_A367W_qvc8?t=662))
- Five resolution / soft-token budget levels; 560 and 1,120 are the high-budget options for OCR and detection ([13:42](https://youtu.be/_A367W_qvc8?t=822))
- A 280 soft-token budget corresponds to 2,520 patches (3x3 patch groups per token) ([15:00](https://youtu.be/_A367W_qvc8?t=900))
- Audio conformer is 305M parameters, and the audio tokenizer downsamples to N/4 soft tokens ([16:15](https://youtu.be/_A367W_qvc8?t=975))

## Hot takes
- Apache 2.0 licensing was chosen deliberately to make the models accessible to everyday developers.
- Pan-and-scan is replaced by variable-resolution image encoding, which keeps spatial position information intact.
- Storing per-layer embeddings in flash rather than VRAM is the key trick that makes the on-device models practical.

## Tools mentioned
Gemma 4, Hugging Face, Kaggle, Ollama, Google AI Studio, Vertex AI

## Relevance to our work
- **agentos** (2/3): InferCraft runs vLLM on one RTX 5090 with pluggable KV-cache strategies. The sliding-window local layers and the wider global KV heads change the KV sizing that those strategies assume. → *Pull the Gemma 4 model config (layer types, sliding_window, KV head counts and dims) and check whether InferCraft's KV-cache sizing and offload policies need a per-layer-type case.*
- **general** (1/3): Small on-device and open-weight models with multimodal input are relevant to the cheap-model pipeline interest, but the talk gives no evaluation data for agent tasks. → *Add Gemma 4 E4B and 26B MoE to the list of cheap-model candidates to benchmark on our own extraction or classification tasks.*
