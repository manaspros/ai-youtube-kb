# Voice AI: when is the "Her" moment? — Neil Zeghidour, CEO, Gradium AI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `P_RI1kCkRbo` · [watch](https://youtu.be/P_RI1kCkRbo) · **date:** 2026-05-18 · **length:** 19:27 · **format:** talk · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Neil Zeghidour · **orgs:** Gradium AI, ElevenLabs, OpenAI, NVIDIA, SESAME, OpenRouter
- **topics:** voice-multimodal, infra-cost-scaling, models-research · **tags:** voice-ai, full-duplex, speech-to-speech, cascaded-pipeline, backchanneling, tts-cost, on-device-tts, tool-call-latency, filler-speech, voice-cloning

> Gradium's CEO argues voice AI is not yet at the "Her" moment: cascaded pipelines hit latency limits, full-duplex speech models lack reliability and tools, and TTS cost dominates. He pitches on-device TTS as the fix.

## Summary
The speaker, CEO of Gradium AI, says voice AI is still far from the conversational ease shown in the film "Her." He describes Gradium as a model provider for voice builders that trains speech-to-text, text-to-speech, and speech-to-speech models, and not an orchestration or vertical-app company. He argues that cascaded pipelines (streaming STT, LLM, streaming TTS) are still too slow for human-like turn-taking, and that TTS alone takes over 200 ms. Tool calls are now the main latency bottleneck, and he suggests filler speech while a tool runs as a workaround. He says most speech-to-speech models are half-duplex, which breaks natural overlap and backchanneling; Moshi is the one full-duplex example, but it lacked tools, observability and paralinguistic skill. He concludes that full-duplex models will not replace cascades until they match their reliability, intelligence and personalization. Last, he says TTS, not the LLM, drives voice cost, and he demos Gradium Phonon, a sub-100M-parameter on-device TTS in private beta, as a cheap, private option. The talk is partly a product pitch, so the product claims are unverified.

## Key ideas
- **Cascaded voice stacks (STT, LLM, TTS) cannot reach human turn-taking speed** — Even a very fast streaming TTS takes over 200 ms on its own, while the speaker puts the full human response cycle (understand, answer, speak) at about 200 ms. Latency is only part of the gap, since the stack also lacks real tool use. ([5:39](https://youtu.be/P_RI1kCkRbo?t=339))
- **Tool-call latency has replaced TTS latency as the main bottleneck** — Shaving 10-20 ms off TTS matters less now than tool calls through routers, which take 500 ms to 4 s and are unpredictable. Models need to handle complex tool calls more reliably. ([7:01](https://youtu.be/P_RI1kCkRbo?t=421))
- **Filler speech during tool calls keeps the conversation natural** — The LLM dispatches a tool call and keeps talking while waiting. It then works the result back into the conversation. He shows this with a quickly vibe-coded travel agent demo, and admits it needs tuning. ([7:01](https://youtu.be/P_RI1kCkRbo?t=421))
- **Most speech-to-speech models are half-duplex, so they cannot handle human overlap** — A model either listens or speaks, so it cannot handle interruptions, coughs, or backchanneling. Human talk overlaps up to about 20% of the time, and backchanneling is culturally variable (e.g., Japanese uses a lot of it as a sign of politeness). His own demo of a half-duplex model came across as annoying. ([9:03](https://youtu.be/P_RI1kCkRbo?t=543))
- **Moshi is the full-duplex reference, but it was not usable as an agent** — Moshi handles overlap and noise well. But it had no tool calls, no observability, weak content quality, and little paralinguistic understanding. NVIDIA's PersonaPlex, built on it, had the same weakness. Full-duplex needs the same reliability, intelligence and personalization as cascades before it can replace them. ([11:19](https://youtu.be/P_RI1kCkRbo?t=679))
- **Paralinguistic cues are lost unless the training data uses them** — A speech-to-speech model can in principle detect tone, such as a speaker being uncomfortable. But if training data is only factual Q&A, the model never learns to use that signal. ([11:19](https://youtu.be/P_RI1kCkRbo?t=679))
- **Voice cost is dominated by TTS, and that drives on-device and privacy choices** — LLM and STT costs are small compared to TTS, and some startups have burned their funding on TTS bills. Many voice modes from big providers run at a loss. He pitches Gradium Phonon, an on-device TTS under 100M parameters that runs on a smartphone CPU, as a way to avoid API fees and keep data local. ([16:22](https://youtu.be/P_RI1kCkRbo?t=982))

## Techniques
- **Filler speech while a tool call runs** — Split the turn into a tool dispatch and a spoken filler. The agent keeps talking, for example by commenting on the destination, while the result is pending. Then it inserts the result naturally into the conversation. *When:* Voice agents whose tool calls take a variable and sometimes long time (500 ms to 4 s through routers), where dead air hurts the experience.
- **Stress-test full-duplex and interruption behaviour** — Run demos with overlapping speech, interruptions, and backchanneling, not scripted turn-taking. Pick the model by how it handles those cases, not by how natural the first turn sounds. *When:* Evaluating speech-to-speech or full-duplex models before using them for a live conversation.
- **On-device TTS for cost and privacy** — Run a small TTS model (under 100M parameters) on the phone CPU instead of calling a cloud TTS API, so no per-character cost and no audio leaves the device. *When:* Consumer voice apps where TTS API bills would dominate unit economics, or where users need local, private processing.
- **Keep the cascade as the default for reliable agents** — Use streaming STT, an LLM with tools, and streaming TTS with semantic VAD. Only move to speech-to-speech once it has tools, observability and content quality equal to the cascade. *When:* Building production voice agents today that must call tools, be observable, and be safe to run.

## Numbers
- TTS alone is over 200 ms, against a human response cycle of about 200 ms ([5:39](https://youtu.be/P_RI1kCkRbo?t=339))
- Tool calls through routers such as OpenRouter take 500 ms to 4 s ([7:01](https://youtu.be/P_RI1kCkRbo?t=421))
- Human conversation overlaps up to about 20% of the time ([10:23](https://youtu.be/P_RI1kCkRbo?t=623))
- Voice cloning from about 10 seconds of reference audio ([1:01](https://youtu.be/P_RI1kCkRbo?t=61))
- Gradium Phonon is under 100M parameters and runs on a smartphone CPU ([16:22](https://youtu.be/P_RI1kCkRbo?t=982))

## Hot takes
- Voice is not a commodity, contrary to what some competitors say; it is very hard, and the last mile is the most difficult.
- Every speech-to-speech model except Moshi is half-duplex, so none of them handle natural conversation yet.
- Full-duplex models will not replace cascaded systems in the near term, because cascades are more practical and reliable.
- Once LLM costs fall, TTS is the main voice cost, and many startups are burning funding on it.
- Voice modes from hyperscalers run at a loss as a marketing move.

## Tools mentioned
Moshi, Gradium Phonon, NVIDIA PersonaPlex, Kokoro, ElevenLabs, OpenRouter

## Relevance to our work
- **general** (1/3): Filler or progress output while a slow tool call runs is a reusable pattern for any long-running agent, not only voice. → *Try a short progress message during long tool calls in one agent flow, then measure whether users or downstream steps stop retrying.*
