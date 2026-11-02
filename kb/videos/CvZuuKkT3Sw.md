# Someone Built Ollama for Audio… and It Runs Locally

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `CvZuuKkT3Sw` · [watch](https://youtu.be/CvZuuKkT3Sw) · **date:** 2026-09-02 · **length:** 5:49 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Better Stack, GGML, llama.cpp, whisper.cpp, Ollama, Kokoro, Piper, FFmpeg, PyTorch, Apple, NVIDIA, OpenAI
- **topics:** local-ai, voice-multimodal, inference-serving · **tags:** audio, tts, speech-to-text, voice-cloning, ggml, metal, cuda, apple-silicon, openai-compatible-api, single-binary, apache-2.0, early-stage

> Walkthrough of Audio CPP, a month-old GGML single-binary runtime for about 30 local audio model families (TTS, STT, voice cloning, music); early and crash-prone, with speed claims measured only on NVIDIA.

## Summary
The host presents Audio CPP, a roughly one-month-old project that runs many audio model families (text-to-speech, speech-to-text, voice cloning, voice conversion, speaker identification, music generation) from one native binary built on GGML, with no Python runtime at inference time. The pitch is that whisper.cpp only transcribes and tools like Ollama, llama.cpp, Kokoro, Piper and FFmpeg each cover only part of the audio stack, so Audio CPP tries to cover all of it. The host runs a live demo: a 10-second reference clip of his own voice is used to clone the voice on a MacBook via the Metal backend, then reads a made-up sentence. Backends are swappable (CPU, NVIDIA, Vulkan, Metal), it has a CLI for quick runs, and a server mode that mirrors the OpenAI audio endpoints so existing client code can point at localhost. The caveats are substantial: the headline speed numbers were measured only on an RTX 5090, some models carry an MLX label but are plain GGML on Metal, there are no prebuilt Mac releases (you compile with a Metal build script and Xcode tools), model download and conversion still rely on a Python helper, and the project is essentially one maintainer with an issue tracker full of crashes, memory leaks and robotic-sounding outputs. The host reads the Apache 2.0 license from the file itself after GitHub's detector showed none, and frames the project as making the same bet llama.cpp made for text, collapsing fragile Python audio setups into one binary.

## Key ideas
- **Audio CPP aims to be a llama.cpp-style single runtime for audio: about 30 model families (TTS, STT, voice cloning, conversion, speaker ID, music) on GGML, with no Python at inference time.** — The host positions it as filling the gap that whisper.cpp (transcription only) left, and that text runtimes like Ollama and llama.cpp do not cover audio. ([0:00](https://youtu.be/CvZuuKkT3Sw?t=0))
- **Voice cloning from a short reference clip works locally on a Mac. The host cloned his voice from a 10-second clip and generated an unseen sentence, with the output varying on a second test.** — This is a live, unscripted demo on Apple Silicon with the Metal backend, not a benchmark. The host notes the second sample shows where it fails. ([1:01](https://youtu.be/CvZuuKkT3Sw?t=61))
- **Architecture is GGML math with swappable backends (CPU, NVIDIA, Vulkan, Metal). It has a CLI driven by flags for task, model family and backend, plus a server mode that matches OpenAI's audio API shape.** — The OpenAI-compatible server means existing cloud-audio client code can target localhost with the same request shape. ([2:22](https://youtu.be/CvZuuKkT3Sw?t=142))
- **Audio CPP sits where no single existing tool does: whisper.cpp only listens, llama.cpp and Ollama are text-only, Kokoro and Piper only speak, and FFmpeg moves audio without running neural models.** — The host's framing of the positioning gap, which is also why the title compares it to Ollama even though Ollama itself is text-only. ([2:22](https://youtu.be/CvZuuKkT3Sw?t=142))
- **The headline speed claim (10 hours of audio in about 3 minutes, about 5x faster than PyTorch) was measured only on an RTX 5090. No Apple Silicon numbers are published, and the host times his demo live for that reason.** — Treat performance claims as NVIDIA-only until Mac results appear. ([3:19](https://youtu.be/CvZuuKkT3Sw?t=199))
- **Practical friction: the only prebuilt releases are Windows, so a Mac user must compile with a Metal build script and Xcode tools. Model download and conversion still depend on a Python helper, which weakens the no-Python claim.** — Some models are labelled MLX but use plain GGML on Metal, not Apple's MLX framework. ([3:19](https://youtu.be/CvZuuKkT3Sw?t=199))
- **The project is early and mostly one person's work. The issue tracker reports crashes, memory leaks and a few models with robotic output, so the host recommends it only for people willing to compile and test output themselves.** — Not recommended for shipping a product yet. ([4:32](https://youtu.be/CvZuuKkT3Sw?t=272))
- **Licensing is Apache 2.0. GitHub showed no license because its detector tripped on the copyright line, so the host advises reading the license file directly.** — Commercial use appears permitted under Apache 2.0, based on the file itself. ([4:32](https://youtu.be/CvZuuKkT3Sw?t=272))
- **The thesis is that llama.cpp mattered because it turned a Python mess into one fast local binary that the ecosystem built on, and Audio CPP is making the same bet for audio.** — The host argues the early rough edges do not change the direction of the shift. ([4:32](https://youtu.be/CvZuuKkT3Sw?t=272))

## Techniques
- **Single-binary local audio runtime** — Compile the GGML-based project from source with its Metal build script and Xcode command-line tools on macOS (no prebuilt Mac release exists), then run it as one static binary. Choose task, model family and backend with CLI flags (CPU, CUDA, Vulkan or Metal). The exact flag names and build script name were not shown on screen. *When:* When you want local speech, TTS, voice cloning or music generation without managing separate Python environments and CUDA/PyTorch version matches.
- **OpenAI-compatible local audio server** — Start the server mode of the binary, which exposes the same endpoint shape as OpenAI's audio API on localhost. Point existing client code at the local base URL with no code changes beyond the URL. Behaviour compatibility was claimed, not tested in the video. *When:* When you already have OpenAI audio client code and want to swap in a local model for cost, privacy or offline use, and can accept early-stage stability.
- **Voice cloning from a short reference clip** — Provide a reference clip of about 10 seconds of the target voice along with the text to speak. Generate speech for new sentences and check each output for consistency, since the host showed one sample that held up and one that failed. *When:* When prototyping local voice cloning and you can tolerate inconsistent quality. Run it on your own hardware so no audio leaves the machine.
- **Validate speed on your own hardware** — Do not rely on the published throughput figures, which come from an RTX 5090 only. Benchmark the same audio input on your target device, such as Apple Silicon, against your current pipeline (for example PyTorch) before drawing conclusions. *When:* Before adopting the runtime for performance-sensitive audio work on hardware other than the published NVIDIA setup.

## Numbers
- Roughly 30 model families supported in one runtime ([1:01](https://youtu.be/CvZuuKkT3Sw?t=61))
- Voice cloning demo used a 10-second reference clip ([1:01](https://youtu.be/CvZuuKkT3Sw?t=61))
- Project is about one month old at time of video ([0:00](https://youtu.be/CvZuuKkT3Sw?t=0))
- 10 hours of audio transcribed in about 3 minutes, roughly 5x faster than PyTorch, measured only on an RTX 5090 (no Apple Silicon numbers published) ([3:19](https://youtu.be/CvZuuKkT3Sw?t=199))
- License is Apache 2.0 ([4:32](https://youtu.be/CvZuuKkT3Sw?t=272))

## Hot takes
- The Ollama-for-audio framing is loose: Ollama is text-only, and the host's own comparison points out that gap.
- The no-Python promise holds at inference time but not for model download and conversion, which still use a Python helper.
- Speed claims are NVIDIA-only, so they say little about Mac performance until Apple Silicon results are published.
- Some models labelled MLX are plain GGML on Metal, not Apple's MLX framework, so the label is misleading.
- Llama.cpp's real contribution was consolidating Python setups into one binary, not a flawless first release, and Audio CPP is making the same bet for audio.

## Tools mentioned
Audio CPP, GGML, llama.cpp, whisper.cpp, Ollama, Kokoro, Piper, FFmpeg, PyTorch, MLX, CUDA, Vulkan, Metal, Xcode, OpenAI audio API

## Relevance to our work
- **agentos** (1/3): AgentOS is an OpenAI-base_url proxy that routes to local inference (vLLM on the RTX 5090). A local OpenAI-compatible audio server is a possible future backend only if AgentOS adds voice modalities, which the profile does not mention. → *Note Audio CPP's OpenAI-shaped server mode as a candidate local backend if AgentOS ever adds audio routes. No change needed now.*
