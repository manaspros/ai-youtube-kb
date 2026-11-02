# Why MLX — Prince Canuma, Neywa Labs

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `zTLJNHj0DeQ` · [watch](https://youtu.be/zTLJNHj0DeQ) · **date:** 2026-05-18 · **length:** 23:10 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Prince Canuma · **orgs:** Neywa Labs, Apple, Roboflow, LM Studio, Liquid AI, Google, Meta
- **topics:** local-ai, inference-serving, voice-multimodal · **tags:** mlx, apple-silicon, on-device, local-inference, kv-cache, turboquant, quantization, tts, speech-to-speech, vision, robotics, gemma-4, qwen3-omni, core-ml

> Prince Canuma argues for running agents, voice, and vision models fully on Apple Silicon with MLX to cut cloud subscription costs and work offline. Demos are mixed, and the talk ends with a TurboQuant KV-cache claim.

## Summary
The speaker, who contributes to the MLX array framework for Apple Silicon, makes the case for on-device AI: offload cloud subscription spend and work without internet. He covers MLX-VLM for vision, MLX-Audio for speech-to-text, text-to-speech and speech-to-speech, and a modular pipeline that chains separate ASR, LLM and TTS models. Live demos of real-time detection, background blur, and a Gemma 4 chat UI ran partly, and the rest were shown as community videos. He claims models of hundreds of billions of parameters can run locally by using storage, though speed is reasonable only for some models. In Q&A he says MLX uses the GPU rather than the Neural Engine, and he describes a TurboQuant KV-cache implementation with about 4x memory reduction and about 2x throughput at 300k context. Most numbers are self-reported and no detailed benchmark is shown.

## Key ideas
- **Motivation for on-device AI** — The speaker argues that running agents on the user's own hardware removes cloud subscription spend (paying only the energy bill) and works where connectivity is poor, such as the speaker's father's situation in Africa. ([0:00](https://youtu.be/zTLJNHj0DeQ?t=0))
- **MLX as an Apple Silicon array framework** — MLX is presented as a PyTorch-like framework for Apple Silicon. The speaker says the community has ported over 4,000 models, with day-zero support for some frontier open models such as Gemma 4. ([2:12](https://youtu.be/zTLJNHj0DeQ?t=132))
- **Vision and speech stacks run locally** — Real-time detection (RF-DETR), background blur, and speech-to-speech run on the device. Marvis TTS is a custom model that generates audio in under 100 ms. ([4:57](https://youtu.be/zTLJNHj0DeQ?t=297))
- **Modular speech pipeline** — Instead of one speech-to-speech model, the speaker chains a chosen ASR model, a chosen LLM and a chosen TTS model. This lets the same app fit different hardware budgets, from an early M1 to newer chips. ([6:18](https://youtu.be/zTLJNHj0DeQ?t=378))
- **Large models from storage on phones** — The speaker claims models in the tens of billions of parameters (he cites a Gemma 4 26B-class model) can run on an iPhone by using storage, with reasonable speeds. He calls the 96 GB machine used in the demo the reason all demo models could run at once. ([9:05](https://youtu.be/zTLJNHj0DeQ?t=545))
- **Honest limit: capability gap with frontier cloud models** — He says local open models will not match current frontier cloud models for now, so the UX should be set to match the local model's expected quality. He expects the gap to narrow over months. ([20:19](https://youtu.be/zTLJNHj0DeQ?t=1219))
- **TurboQuant for KV cache** — He implemented TurboQuant publicly within about 30 minutes of the paper and reports about 4x KV-cache reduction with similar output match. At around 300k context, he reports throughput roughly doubling. ([21:57](https://youtu.be/zTLJNHj0DeQ?t=1317))

## Techniques
- **Modular speech pipeline** — Chain separate ASR, LLM and TTS models behind one interface and swap each stage independently to match hardware. *When:* Building voice agents on constrained or mixed Apple hardware, where one end-to-end speech model is too heavy.
- **Chained short-clip video generation** — Generate a short clip, then continue generation from its frames, repeating to build a longer coherent story instead of one-shot generation. *When:* Local video generation on limited VRAM (speaker cites 16 GB) where single-shot length is capped.
- **Grounded visual reasoning on video** — Run a perception or detection model on each frame and ask a VLM questions about the detected items in footage. *When:* Offline analysis of camera or dash-cam footage without sending video to a cloud API.
- **Storage-backed model loading on phones** — Load weights from device storage so models larger than RAM can run, accepting slower speed. *When:* You need a large model on a memory-limited device and can tolerate lower throughput.
- **TurboQuant-style KV-cache quantization** — Quantize the KV cache (speaker reports 4x reduction) and compare output match and throughput against the full-precision cache at long context. *When:* Long-context inference where KV-cache memory is the bottleneck on a single device.
- **Live GPU monitoring during inference** — Use the MacTop tool to watch GPU and CPU load while a model runs, as a quick check that inference is on the GPU. *When:* Confirming where local inference actually runs and tracking its performance on a Mac.

## Numbers
- MLX has over 1.5 million downloads and over 4,000 models ported (speaker's figures) ([2:12](https://youtu.be/zTLJNHj0DeQ?t=132))
- Marvis TTS generates audio in under 100 ms ([4:57](https://youtu.be/zTLJNHj0DeQ?t=297))
- Demo machine has 96 GB of memory and runs all demo models at once ([10:41](https://youtu.be/zTLJNHj0DeQ?t=641))
- Chained video generation runs on a MacBook with 16 GB VRAM (community project) ([12:42](https://youtu.be/zTLJNHj0DeQ?t=762))
- Qwen3-Omni is around 30B parameters and can run on device ([20:19](https://youtu.be/zTLJNHj0DeQ?t=1219))
- Claimed context up to 1 million tokens on device using TurboQuant, depending on model and hardware ([20:19](https://youtu.be/zTLJNHj0DeQ?t=1219))
- TurboQuant: full-model KV cache about 1 GB, reduced about 4x with similar output quality (exact-match comparison shown) ([21:57](https://youtu.be/zTLJNHj0DeQ?t=1317))
- TurboQuant: throughput almost doubles at about 300k context ([21:57](https://youtu.be/zTLJNHj0DeQ?t=1317))
- The TurboQuant tweet reached about 700,000 views ([21:57](https://youtu.be/zTLJNHj0DeQ?t=1317))

## Hot takes
- Cloud agent subscriptions can be largely replaced by on-device models, leaving only the energy bill.
- Models with hundreds of billions of parameters can run on a MacBook or iPhone with the right tricks.
- MLX uses the GPU, not the Neural Engine, and Core ML is not yet practical for developers on Apple Silicon.
- Open models will reach current frontier-cloud performance within about six months (speaker's guess).

## Tools mentioned
MLX, MLX-VLM, MLX-Audio, Marvis TTS, RF-DETR, Gemma 4, Qwen3-Omni, Core ML, Gradio, MacTop, Reachy Mini, LM Studio, Swift, Python, Claude Code, Codex

## Relevance to our work
- **agentos** (1/3): MLX is Apple-only, so it does not replace the RTX 5090 vLLM stack. The TurboQuant KV-cache claim is relevant to InferCraft's pluggable KV-cache strategies, but it is unverified and shown without a benchmark. → *Benchmark a TurboQuant-style KV-cache quantization as a candidate in InferCraft's KV-cache strategy set on the RTX 5090, measuring output match and throughput at long context before adopting the 4x memory claim.*
