# An Open-Source Alternative to ElevenLabs

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `chH2tlh_Vvk` · [watch](https://youtu.be/chH2tlh_Vvk) · **date:** 2026-01-02 · **length:** 4:27 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Resemble AI, Better Stack, ElevenLabs
- **topics:** voice-multimodal, local-ai · **tags:** tts, voice-agents, open-source, local-inference, voice-cloning, elevenlabs-alternative, chatterbox, watermarking

> Quick hands-on look at Resemble AI's open-source, MIT-licensed Chatterbox Turbo TTS: runs locally, fast enough for agents, with honest drawbacks around overacting and tail artifacts.

## Summary
Better Stack presents Chatterbox, an open-source text-to-speech family from Resemble AI, focusing on the Turbo variant. The pitch is that it is MIT-licensed, runs locally with Python and Torch, and is fast enough for real-time voice agents, so there are no API rate limits or per-usage fees. The presenter runs a short live demo in a conda environment and claims text-to-audio latency under 150 ms. He covers the three variants (Turbo for English speed, Multilingual for 23 languages with voice cloning, and the original for expressive English), plus zero-shot cloning from about 10 seconds of reference audio and built-in Perth watermarking. Drawbacks get real airtime: overacting on long text, breathing or silence tails that need trimming, and slow CPU performance that calls for a decent GPU. The closing argument is that the momentum (16,000+ GitHub stars, MLX audio integrations) signals voice AI going open source. The video is short and mostly a demo, so the latency and preference numbers are unverified claims.

## Key ideas
- **Chatterbox Turbo is an open-source TTS from Resemble AI, MIT-licensed, and runs locally with Python and Torch with no API or cloud call.** — The pitch is unlimited offline generation with no rate limits, usage pricing, or vendor lock-in, which matters for prototyping voice agents. ([0:00](https://youtu.be/chH2tlh_Vvk?t=0))
- **The family has three variants with distinct jobs.** — Turbo is English-only and tuned for speed and agents. Multilingual covers 23 languages with voice cloning. The original is English with more expressive controls. ([0:00](https://youtu.be/chH2tlh_Vvk?t=0))
- **Speed is the differentiator: the presenter claims text-to-audio under 150 ms on his own machine, shown in a live demo.** — The claim is a single demo run, not a published benchmark. The point is that the latency is low enough to feel real time for agents. ([1:09](https://youtu.be/chH2tlh_Vvk?t=69))
- **Expressiveness is controlled with inline tokens (laugh, sigh, pause) plus exaggeration and CFG weight knobs.** — Exaggeration controls expressiveness and CFG weight controls prompt adherence. The presenter says the expressive tokens on Turbo need a Hugging Face token. ([1:09](https://youtu.be/chH2tlh_Vvk?t=69))
- **The speaker is candid about drawbacks: overacting on longer text, weaker for casual dialogue, and breathing or silence artifacts at the tail of generations that need trimming.** — He recommends testing on your own hardware and locking the model behind product constraints before betting a product on it. ([2:20](https://youtu.be/chH2tlh_Vvk?t=140))
- **Claimed quality and adoption: beat ElevenLabs in over 63% of blind pairwise comparisons, with about two years of production use inside Resemble.** — This is second-hand (the presenter is relaying someone else's blind test) and the test design is not described. ([2:20](https://youtu.be/chH2tlh_Vvk?t=140))
- **Performance depends on hardware: CPU inference is slow, so a decent GPU is effectively required, and torch installs can be painful.** — Watermarking is included but the presenter says voice cloning still carries risk. ([3:24](https://youtu.be/chH2tlh_Vvk?t=204))
- **The wider signal is that voice AI is going open source in a serious way, with 16,000+ GitHub stars and early MLX audio integrations.** — People are benchmarking it against Spark TTS for real-time use. ([3:24](https://youtu.be/chH2tlh_Vvk?t=204))

## Techniques
- **Local offline TTS setup** — Create a conda environment as the Git repo recommends, install the Python and Torch dependencies, and run the model locally with no API call. The video does not show the exact commands. *When:* Prototyping voice agents, NPCs or accessibility tools where API rate limits and per-character cost would get in the way.
- **Zero-shot voice cloning from short reference audio** — Supply about 10 seconds of reference audio. The Multilingual variant is the one that covers 23 languages with cloning. *When:* You need a consistent voice persona across generations, in a language other than English, without fine-tuning.
- **Tune expressiveness with exaggeration, CFG weight and inline tags** — Raise or lower exaggeration for expressiveness and CFG weight for prompt adherence. Insert inline tokens such as laugh, sigh or pause in the text. On Turbo, the expressive tokens need a Hugging Face token. *When:* Agent speech needs emotional range, and you have to trade expressiveness against fidelity to the text.
- **Post-process generations to remove tail artifacts** — Trim trailing breathing, silence or noise from the end of each generated clip before playback. *When:* Any generated audio goes to end users, especially for longer outputs where tail artifacts appear.
- **Benchmark on your own hardware before committing** — Run the model on the target GPU and measure latency and quality with your own text, then decide whether to ship it. The presenter recommends locking it behind product constraints. *When:* Choosing a local TTS for a production voice path.

## Numbers
- Three variants: Turbo (English, speed), Multilingual (23 languages, voice cloning), original (English, expressive controls) ([0:00](https://youtu.be/chH2tlh_Vvk?t=0))
- Zero-shot voice cloning from about 10 seconds of reference audio ([0:00](https://youtu.be/chH2tlh_Vvk?t=0))
- Text-to-audio latency claimed under 150 ms in a live demo on the presenter's machine ([1:09](https://youtu.be/chH2tlh_Vvk?t=69))
- Beat ElevenLabs in over 63% of blind pairwise comparisons (relayed from a third-party test) ([2:20](https://youtu.be/chH2tlh_Vvk?t=140))
- About two years of production use inside Resemble before open-sourcing ([2:20](https://youtu.be/chH2tlh_Vvk?t=140))
- Over 16,000 GitHub stars ([3:24](https://youtu.be/chH2tlh_Vvk?t=204))

## Hot takes
- The sub-150 ms latency is a single live demo, not a benchmark. Treat it as unverified until measured on your own GPU.
- The 63% preference win over ElevenLabs is second-hand, and the test design is not described.
- The most useful part is the drawbacks segment (overacting, tail artifacts, slow CPU), not the pitch.
- Voice cloning risk is raised in passing but not explored.

## Tools mentioned
Chatterbox Turbo, Chatterbox Multilingual, Chatterbox (original), Python, Torch, conda, Gradio, Hugging Face, MLX audio, Spark TTS, ElevenLabs, Perth watermarking

## Relevance to our work
- **agentos** (1/3): AgentOS is GPU-bound on a single RTX 5090 with vLLM serving. A local TTS would compete for the same VRAM, and the video offers no serving or memory numbers. → *If AgentOS adds a voice path, benchmark Chatterbox Turbo latency and VRAM next to the vLLM stack on the 5090 before choosing a local TTS.*
