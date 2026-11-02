# Gemma, DeepMind's Family of Open Models — Omar Sanseviero, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `_gVFUEdhCyI` · [watch](https://youtu.be/_gVFUEdhCyI) · **date:** 2026-05-18 · **length:** 15:26 · **format:** talk · **quality:** 2/5 · **depth:** intro
- **speakers:** Omar Sanseviero · **orgs:** Google DeepMind, Google
- **topics:** models-research, local-ai, inference-serving · **tags:** gemma, open-weights, on-device, llama.cpp, per-layer-embeddings, multilingual-tokenizer, apache-2, fine-tuning, shieldgemma, medgemma, android-studio

> Google DeepMind's Omar Sanseviero introduces Gemma 4, a family of open models from 2B to 32B parameters, and argues that small open models can now do multimodal and agentic work on-device.

## Summary
The speaker presents Gemma 4, released about a week before the talk, as Google's most capable open model family, spanning roughly 2B to 32B parameters. He covers the model lineup: small E2B/E4B models for phones and even a Raspberry Pi, a mixture-of-experts model for low latency, and a 31B dense model that still fits on a consumer GPU. The license moved to Apache 2.0, and the E-prefixed models use per-layer embeddings that can be offloaded to CPU or disk to reduce GPU memory. The small models support image, video, and audio input, and the tokenizer (shared with Gemini) was built for 140+ languages, which helps fine-tuning for low-resource languages. He reports ecosystem uptake (10M Gemma 4 downloads in a week, 1,000+ derivatives, 500M family downloads) and integrations with llama.cpp, MLX, Ollama, Hugging Face, vLLM, SGLang, and Android Studio's offline agent mode. He also lists official variants (ShieldGemma for safety classification, MedGemma for medical multimodal) and community efforts (AI Singapore, Sarvam). He closes by urging viewers to try on-device open models while still using API models for the highest raw capability.

## Key ideas
- **Open models are the point: download, run on your own infra or device, and fine-tune** — Gemma is positioned as a family of open weights, not an API. The speaker frames the value as control over where the model runs and what data it sees. ([0:00](https://youtu.be/_gVFUEdhCyI?t=0))
- **Gemma 4 covers phone-sized to single-consumer-GPU sizes** — Lineup runs from about 2B to 32B parameters. Small models target phones and Raspberry Pi and are multimodal with reasoning. A MoE model is for low latency and a 31B model for maximum quality, and the 31B still runs on a consumer GPU. ([1:08](https://youtu.be/_gVFUEdhCyI?t=68))
- **E-prefixed models hold more parameters than their compute cost suggests** — E2B is described as effectively 2B in compute but around 4B total parameters. Per-layer embeddings act like a lookup table rather than matrix multiplication, so they can sit on CPU or disk while the transformer compute stays on GPU. ([5:09](https://youtu.be/_gVFUEdhCyI?t=309))
- **Small models are multimodal, including audio** — The smallest models handle image, video, and audio, including speech recognition and speech translation. The larger model does finer-grained vision tasks such as pointing and object detection. ([6:32](https://youtu.be/_gVFUEdhCyI?t=392))
- **Tokenizer choice matters for low-resource languages** — The tokenizer is shared with Gemini and was designed for multilingual use across 140+ languages. The speaker argues that fine-tuning for an under-resourced language tends to work better out of the box because of this tokenizer, independent of raw model capability. ([7:53](https://youtu.be/_gVFUEdhCyI?t=473))
- **Adoption is driven by the community ecosystem and day-one tool support** — The speaker stresses that tools like llama.cpp, MLX, Ollama, Hugging Face Transformers, vLLM, and SGLang should work with Gemma immediately, so users do not need to switch frameworks (for example to Keras) to fine-tune. ([8:54](https://youtu.be/_gVFUEdhCyI?t=534))
- **Use open models on-device, keep API models for peak capability** — The speaker's closing advice: use API models when you need the most raw intelligence, and use open models for offline, private, or on-device agentic work. He expects on-device capability to keep improving. ([13:33](https://youtu.be/_gVFUEdhCyI?t=813))

## Techniques
- **Offload per-layer embeddings to CPU or disk** — In llama.cpp, use the override-tensor flag to move the per-layer embedding tables off GPU. Only the transformer weights that need matrix multiplication stay in VRAM. *When:* Running an E2B/E4B-class model on a memory-constrained phone or laptop where the full parameter count does not fit in GPU memory.
- **Parallel local generation on one machine** — Run about 10 Gemma instances at once through llama.cpp on a single laptop, each generating a different output (the demo generated SVGs). *When:* Batch-generating many candidate artifacts locally without API calls or network access.
- **Pick the model by tokenizer for low-resource language fine-tuning** — Start from a model whose tokenizer was built for multilingual coverage, then fine-tune on the target-language data. *When:* Adapting a model to a language with little digital data, such as an indigenous language.
- **Stay on the framework the team already uses** — Use Hugging Face Transformers, Keras, or the serving stack of your choice. The speaker says the models are meant to load in these tools without conversion. *When:* Fine-tuning or serving an open model inside an existing Python or GPU stack.

## Numbers
- Gemma 4 model family spans about 2B to 32B parameters; the E2B model has roughly 4B total parameters ([1:08](https://youtu.be/_gVFUEdhCyI?t=68))
- Demo: 10 Gemma instances running in parallel on one laptop via llama.cpp, at about 100 tokens per second (as stated, unverified) ([2:33](https://youtu.be/_gVFUEdhCyI?t=153))
- Gemma 4 trained on 140+ languages ([6:32](https://youtu.be/_gVFUEdhCyI?t=392))
- Gemma 4 reached 10 million downloads within about a week of release ([8:54](https://youtu.be/_gVFUEdhCyI?t=534))
- Over 1,000 community Gemma 4 derivatives (quantizations and fine-tunes) within days ([8:54](https://youtu.be/_gVFUEdhCyI?t=534))
- Whole Gemma family: over 500 million downloads; Gemmaverse over 100,000 models ([9:49](https://youtu.be/_gVFUEdhCyI?t=589))

## Hot takes
- Open models can now do highly agentic, complex tasks entirely on device.
- Open model licensing (Apache 2.0) matters as much as benchmark scores for adoption.
- Small models keep getting more capable without getting bigger, so capable models on personal devices are coming within a year or two.

## Tools mentioned
Gemma 4, llama.cpp, MLX, Ollama, Hugging Face Transformers, vLLM, SGLang, Keras, Android Studio, ShieldGemma, MedGemma, LM Arena

## Relevance to our work
- **agentos** (1/3): InferCraft serves local models with vLLM and llama.cpp-style setups on one RTX 5090. A small, multimodal, Apache-2.0 open model that runs on-device is a possible cheap local tier, but the talk gives no serving benchmarks. → *Read the Gemma 4 model card and benchmark E4B or the MoE model under llama.cpp next to our current InferCraft local model, to decide whether it belongs in the local tier.*
