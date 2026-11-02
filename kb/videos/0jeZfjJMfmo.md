# Reachy Mini: the $300 open source robot you can actually hack — Andres Marafioti, Hugging Face

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `0jeZfjJMfmo` · [watch](https://youtu.be/0jeZfjJMfmo) · **date:** 2026-06-18 · **length:** 21:16 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Andres Marafioti · **orgs:** Hugging Face, Mistral, Qwen (Alibaba), OpenAI
- **topics:** voice-multimodal, inference-serving, infra-cost-scaling · **tags:** reachy-mini, open-source-robotics, voice-agent, streaming-tts, qwen3-tts, static-kv-cache, cuda-graphs, speech-to-speech, latency, codex, hackable-hardware

> Hugging Face's Andres Marafioti on the open-source $300-450 Reachy Mini robot, its voice pipeline, and how a streaming TTS model was made fast enough for real-time voice agents.

## Summary
Marafioti argues that cheap, open, hackable robots are needed because current humanoids cost 50k+ and are aimed at companies, and that voice is the natural way to talk to them. He presents Reachy Mini, sold unassembled at $300 (no battery or Pi) or $450 (with Raspberry Pi and battery), with 7,500 units shipped and its conversation app as the fleet's most-used feature. The voice stack is VAD, then streaming STT (Parakeet, partial transcripts every 150 ms), then an LLM with tool calling (Qwen 3.5 27B, scaled on its own endpoints), then TTS (Qwen3-TTS), with a robot-side app handling echo cancellation, tool dispatch, and face tracking. The core technical section covers making Qwen3-TTS fast: the released model generated whole outputs before returning audio and ran about 500 autoregressive steps per audio packet with CPU-GPU round trips each step. He fixed this over about two weeks with Codex by adding streaming, switching to a static KV cache, and capturing the graph, which moved the real-time factor from below 1 to several times real-time and cut time-to-first-audio to milliseconds. He stresses that user-perceived latency includes infrastructure overhead, which can equal the model's own time. He ends by saying a non-coder could build robot apps by pointing Codex at the repo.

## Key ideas
- **Voice pipeline is VAD, then streaming STT, then LLM with tool calls, then TTS, with the robot app handling audio and actions** — Parakeet STT emits partial transcripts every 150 ms so the robot can react early. The LLM handles tool calls for movement and camera use. Qwen3-TTS produces the speech. The robot app does echo cancellation, tool dispatch, emotions, and face tracking. ([10:19](https://youtu.be/0jeZfjJMfmo?t=619))
- **Streaming TTS was slow for structural reasons, not just model quality** — The released Qwen3-TTS matched the quality shown in the paper but not its latency. It generated the full output before returning any audio, and it ran about 500 autoregressive steps per audio packet, with CPU-GPU sync on every step. ([12:56](https://youtu.be/0jeZfjJMfmo?t=776))
- **Make decode run entirely on the GPU with a static KV cache and graph capture** — The dynamic KV cache grew with input size and forced host-device round trips. A static cache uses more RAM up front but allows compiling the model and capturing the full graph, which removes most of the per-step CPU-GPU traffic. ([14:20](https://youtu.be/0jeZfjJMfmo?t=860))
- **Scale the LLM separately from conversation nodes** — Each conversation node can hold many concurrent users, but load varies a lot: eight talkative users and eight silent users load a node very differently. Separate LLM endpoints with their own load balancer use resources better. ([11:32](https://youtu.be/0jeZfjJMfmo?t=692))
- **Perceived latency is more than model time-to-first-audio** — Network and infrastructure hops add as much delay as the model itself, even though the model is quite fast. Voice-agent latency has to be budgeted across the whole path. ([15:52](https://youtu.be/0jeZfjJMfmo?t=952))
- **Coding agents make hardware apps approachable for non-coders** — He gave Codex the robot repo and a plain description of the desired movements, and it built the app. The claim is that you can start today without deep robotics knowledge. ([18:05](https://youtu.be/0jeZfjJMfmo?t=1085))

## Techniques
- **Stream TTS audio instead of generating full utterances** — Emit audio chunks as they are produced so time-to-first-audio is set by the first chunk, not the full clip length. *When:* Any voice agent where the user should hear the reply before the model finishes generating.
- **Static KV cache plus graph capture for autoregressive audio models** — Preallocate the KV cache at its maximum size, compile the model, and capture the whole decode graph so each step stays on the GPU without host sync. The cost is extra VRAM from the start. *When:* Small autoregressive models with many decode steps per output (TTS, codecs) where per-step CPU-GPU round trips dominate latency.
- **Partial STT every 150 ms** — Stream partial transcripts from the speech recognizer while the user is still talking, so the agent can start reacting before the utterance ends. *When:* Interactive voice agents that need low turn-taking latency.
- **Separate scaling of LLM inference from stateful conversation nodes** — Put conversation handling (audio I/O, tool dispatch) on nodes sized by concurrent users, and put LLM inference behind its own load-balanced endpoints sized by token load. *When:* Fleets where many users are connected but only some are generating tokens at a given time.
- **Measure the whole latency path, not just the model** — Compare model time-to-first-audio with what the client perceives, and account for transport and infrastructure overhead as separate items. *When:* Any latency SLO for agents or voice products, where model benchmarks alone understate delay.
- **Codex-driven hardware app development** — Give a coding agent the repo and a short description of the target behavior, then iterate on the result. *When:* Prototyping device or robot apps where the developer is not an expert in the hardware stack.

## Numbers
- Reachy Mini price: $300 (cheaper model with no Pi and no battery) or $450 (with Raspberry Pi and battery) ([9:18](https://youtu.be/0jeZfjJMfmo?t=558))
- Humanoid and robotaxi systems cost at least mid five figures, with some at six figures ([1:04](https://youtu.be/0jeZfjJMfmo?t=64))
- Robots shipped: 7,500, and the conversation app is the most-used app in the fleet ([10:19](https://youtu.be/0jeZfjJMfmo?t=619))
- Parakeet STT emits partial transcripts every 150 ms ([10:19](https://youtu.be/0jeZfjJMfmo?t=619))
- Real-time factor for Qwen3-TTS went from 0.8 (slower than real time) to 5.8 after optimization. The speaker later says it runs at about 4x real time, so the figures are inconsistent. ([14:20](https://youtu.be/0jeZfjJMfmo?t=860))
- Autoregressive decode used about 500 steps per audio packet, each with a CPU-GPU sync, before optimization ([12:56](https://youtu.be/0jeZfjJMfmo?t=776))
- Time to first audio fell from several seconds to a few milliseconds ([14:20](https://youtu.be/0jeZfjJMfmo?t=860))
- First-token latency under 200 ms for the optimized FasterQwen3-TTS ([15:52](https://youtu.be/0jeZfjJMfmo?t=952))
- Optimization took about two weeks of work with Codex ([12:56](https://youtu.be/0jeZfjJMfmo?t=776))
- Kokoro TTS is about 80M parameters ([3:51](https://youtu.be/0jeZfjJMfmo?t=231))

## Hot takes
- Humanoid robots copy human form for no good reason, and a non-humanoid design would be faster, more agile, and more stable
- Voice AI is mature across commercial and open-source options, but almost nobody is working on how people talk to robots
- Robots will be interacted with by voice, not by keyboard

## Tools mentioned
Reachy Mini, Raspberry Pi, Codex, Parakeet, Qwen3-TTS, Qwen 3.5 27B, Kokoro, Voxtral, Hugging Face Inference Endpoints, speech-to-speech pipeline, GPT Realtime

## Relevance to our work
- **agentos** (1/3): Static KV cache plus graph capture to remove per-step CPU-GPU sync is a decode-loop trick that could apply to InferCraft on the single 5090, but the talk is about a TTS model, not an LLM. → *Benchmark a static KV cache with CUDA graph capture on the InferCraft decode path on the 5090 and compare per-token sync overhead against the current dynamic cache.*
