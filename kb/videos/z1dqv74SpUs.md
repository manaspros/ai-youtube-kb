# Voice agents with Realtime Video — Sidney Primas, LemonSlice

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `z1dqv74SpUs` · [watch](https://youtu.be/z1dqv74SpUs) · **date:** 2026-09-18 · **length:** 26:36 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Sidney Primas · **orgs:** Lemon Slice, Microsoft
- **topics:** voice-multimodal, inference-serving, agent-architecture · **tags:** real-time video, avatars, world model, video diffusion, causal attention, one-step denoising, error accumulation, audio encoders, model harness, emotion engine, EQ model, voice agents, streaming

> Lemon Slice's CTO explains how they build real-time, photorealistic video avatars from a causal video model, covering past-only attention, one-step denoising, long error-free runs, and a GPU/CPU harness that keeps streams stutter-free.

## Summary
Sidney Primas, CTO of Lemon Slice, presents the company's goal of an avatar that passes as human on a video call. Their approach trains a video (world-model style) diffusion transformer focused on humans, with audio as the main driver of expressiveness. To make it interactive they train with an attention mask so the model only sees the past, and they cut denoising from about 30 steps to one. They say they solved error accumulation over very long runs with a method they have not disclosed, and that a demo has run for eight hours without reset. Cost is said to be close to a voice model's, which makes consumer use viable. He argues the real-time model harness (GPU/CPU orchestration, interrupts, buffering) is hard and holds much of the product value. The talk ends with the next steps: an emotion engine targeted for launch in one to two months, and a long-term bet on a single end-to-end "EQ" model in front of a separate reasoning "IQ" model.

## Key ideas
- **Goal is an avatar indistinguishable from a human on a video call, which needs more than photorealism: emotions, micro-expressions, object interaction, and an internal state.** — The speaker frames the problem as a long list of hard technical issues, not just rendering quality. ([0:13](https://youtu.be/z1dqv74SpUs?t=13))
- **Bet: build the video model around humans (a world model focused on people). It is harder to train and deploy, but full-body motion, object interaction, and micro-expressions come more 'for free' as emergent properties.** — He contrasts this with other avatar companies' approaches and says the emergent behaviour is the payoff. ([4:56](https://youtu.be/z1dqv74SpUs?t=296))
- **Positioning is a visual layer sold as an API. Customers bring their own LLM and voice, and Lemon Slice adds the video, so a voice agent becomes a video agent.** — Use cases named: language learning and AI sales calls. ([8:21](https://youtu.be/z1dqv74SpUs?t=501))
- **Audio is the main lever for expressiveness. Most audio encoders are trained on audiobooks, which are monotone, so an expressive video model needs better audio embeddings.** — He says they spent significant effort on the audio side, not only the video backbone. ([9:23](https://youtu.be/z1dqv74SpUs?t=563))
- **Real-time requires a causal model. Bidirectional video models look at future latents, so they trained with an attention mask that lets the model see only the past.** — At inference the future inputs (such as upcoming audio) do not exist yet, so the model never relies on them. ([10:47](https://youtu.be/z1dqv74SpUs?t=647))
- **Error accumulation is the hard problem. Each generated block carries error, and the next block is conditioned on it, so errors compound over long runs.** — They claim a new method, not yet disclosed, that gives no noticeable accumulation. A demo runs continuously for eight hours with no reset, and a 16-hour one is planned. ([12:11](https://youtu.be/z1dqv74SpUs?t=731))
- **Cost and serving: video is pixel-heavy, yet the speaker says cost ends up close to an audio model's, which makes consumer use cases feasible.** — This is a self-reported comparison, with no hardware or price breakdown given. ([13:41](https://youtu.be/z1dqv74SpUs?t=821))
- **The model harness is the under-rated, hard part. Many streams run across GPU and CPU threads, and interrupts, queues, and buffers must be managed so video never stutters.** — He says much of the product value will sit here, especially for any real-time application. ([14:59](https://youtu.be/z1dqv74SpUs?t=899))
- **Next step is an emotion engine that predicts the avatar's actions and emotions from the audio and the text of what it is about to say. The model can already produce such actions but is not yet controllable or deterministic enough.** — Target launch is one to two months out. ([16:24](https://youtu.be/z1dqv74SpUs?t=984))
- **Long-term architecture: a single end-to-end EQ model takes the user's audio and video and outputs avatar video and audio, with its own internal emotional state. A separate IQ model handles tool calling and deep reasoning and feeds the EQ model.** — He expects such end-to-end EQ models on the market within two to three years, and early papers already exist. ([19:41](https://youtu.be/z1dqv74SpUs?t=1181))
- **Q&A: future emotional state may live as implicit latent-space state rather than human-readable words. The team plans its own public Turing-style test with real people this year.** — They do not plan to build a fraud-style use of the tech; the goal is measuring progress. ([21:32](https://youtu.be/z1dqv74SpUs?t=1292))

## Techniques
- **Causal (past-only) attention mask for streaming video** — Train the video model with an attention mask so each frame or block can attend only to past latents and past inputs. Inference then never depends on future inputs that do not yet exist. *When:* Converting a bidirectional video or world model into a live, interactive generator where the future is unknown.
- **Collapse denoising steps for real-time output** — Reduce the number of denoising steps from about 30 to a single step so the model goes from noise to frame in one pass. The speaker does not describe the exact method. *When:* Latency budget is too tight for multi-step diffusion sampling.
- **Expressive audio encoders over default ones** — Replace encoders trained on monotone audiobook speech with embeddings that carry emotion, and spend effort on this front-end, since the video model can only be as expressive as its audio conditioning. *When:* Output must carry emotion and facial expression, not just lip sync.
- **Real-time model harness (GPU/CPU orchestration)** — Run GPU inference and CPU stream handling as separate threads with queues and buffers. Handle interrupts by cleaning queues so the output stream never stutters. *When:* Any streaming generative system that needs continuous output under user interrupts.
- **Two-layer EQ/IQ split** — Put a conversational or emotional model in front, handling audio and video I/O, and a separate reasoning model behind it for tool calls and deep thinking. *When:* A conversational agent needs fast, expressive interaction while heavy reasoning runs elsewhere.

## Numbers
- Avatar (Teddy Roosevelt) runs continuously for 8 hours with no reset, and a 16-hour run is in development. ([12:11](https://youtu.be/z1dqv74SpUs?t=731))
- Denoising steps for the real-time model reduced from about 30 to 1. ([10:47](https://youtu.be/z1dqv74SpUs?t=647))
- Cost of the video model is said to be roughly the same as a voice/audio model's, per the speaker's own comparison. ([13:41](https://youtu.be/z1dqv74SpUs?t=821))
- Target launch for the next emotion-driven model is one to two months away; it is not yet real-time. ([18:11](https://youtu.be/z1dqv74SpUs?t=1091))
- Speaker expects end-to-end EQ models on the market within two or three years. ([19:41](https://youtu.be/z1dqv74SpUs?t=1181))

## Hot takes
- Most interactions between AI and humans will eventually have a visual layer.
- A single end-to-end EQ model will sit in front of a separate IQ reasoning model in future systems.
- The model harness, not the model, will hold most of the long-term value for real-time applications.
- Future emotional state in models may be implicit latent state rather than human-interpretable.

## Relevance to our work
- **agentos** (1/3): Real-time harness patterns (queues, buffers, interrupt cleanup) are only loosely related to the AgentOS proxy and serving layers. → *Only if we add streaming responses to the proxy, reread the interrupt and queue-cleanup point at 14:59 as a design reference. No change needed now.*
- **prosharness** (1/3): The claim that the harness, not the model, holds the value supports ProsHarness's focus on checkpoint/resume and orchestration around Claude Code, though the talk gives no concrete harness design. → *Low-priority: note the harness-as-moat framing when reviewing ProsHarness's checkpoint/resume and loop design. No direct action.*
