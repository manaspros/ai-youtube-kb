# Speech-to-Speech Model Research at Google DeepMind — Valeria Wu Fon & Tom Ouyang, Google DeepMind

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `18Um2VjMM_g` · [watch](https://youtu.be/18Um2VjMM_g) · **date:** 2026-09-18 · **length:** 16:42 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Valeria Wu Fon, Tom Ouyang · **orgs:** Google DeepMind, Google
- **topics:** voice-multimodal, models-research, product-ux · **tags:** speech-to-speech, gemini, streaming-translation, native-multimodal, live-api, search-live, proactive-audio, multilingual, realtime, avatars

> Google DeepMind's Gemini speech-to-speech team explains why one natively multimodal, promptable model beats cascaded ASR+LLM+TTS for voice agents, with live translation, Search Live and Live API demos.

## Summary
Two Gemini team members (product lead Valeria Wu Fon and engineer Tom Ouyang) argue that voice is the most natural interface and that speech-to-speech models are the right base for universal voice agents. They trace the history from multi-component ASR pipelines to end-to-end transcription models, and then to natively multimodal LLMs pretrained on interleaved audio, video and text in one token space. They describe three goals that pull against each other: conversational latency, intelligence (task completion, reasoning), and multimodal input and output. The main tension they name is that turning up thinking to improve intelligence raises latency and time to first audio. Demos cover streaming multi-speaker translation in Google Meet across 70+ languages, a shared model powering Search Live and the Live API, a proactive-audio feature for ignoring background noise, and a real-time avatar with lip sync. The talk is mostly a product showcase with little implementation detail, and it gives no benchmark numbers beyond the language count.

## Key ideas
- **Voice is the most natural interface, so speech-to-speech models are the base for robust universal voice agents.** — The speakers argue that the number of voice applications will grow fast, and that speech-to-speech is the path they choose over bolting ASR and TTS onto a text model. ([0:08](https://youtu.be/18Um2VjMM_g?t=8))
- **Older speech systems were many separate components and only transcribed speech; they could not respond, translate, or reason.** — Pre-2018 ASR had feature extraction, acoustic, pronunciation and language models plus rescoring. Even end-to-end ASR only produced a transcript and needed extra systems for tone, emotion or biasing. ([2:05](https://youtu.be/18Um2VjMM_g?t=125))
- **Native multimodal pretraining on interleaved audio, video and text puts ASR, TTS and agentic tasks in one token space.** — Pretraining uses interleaved examples such as summarizing a video with timestamps or captioning video with audio. Because the model already understands how modalities relate, audio features become prompting tasks. ([3:11](https://youtu.be/18Um2VjMM_g?t=191))
- **Streaming translation can match offline quality when it is a prompt to one multimodal model.** — The model must switch languages, keep the source speaker's voice, handle several speakers and noise, and work in real time. Cascaded systems found this hard; the LLM approach makes it mostly a prompting task. ([4:39](https://youtu.be/18Um2VjMM_g?t=279))
- **Three goals (conversational feel, intelligence, multimodality) trade off against each other.** — Raising thinking effort improves evals on intelligence but hurts latency, time to first audio, and how natural the conversation feels. The team says it tries to advance all three without sacrificing one much. ([6:02](https://youtu.be/18Um2VjMM_g?t=362))
- **Most Gemini users are non-English speakers, so every capability is tested beyond en-US.** — The speakers say the majority of their users are non-English, so the focus is on making the capabilities work across the languages customers use. ([7:13](https://youtu.be/18Um2VjMM_g?t=433))
- **Proactive audio lets the model decide when not to respond to external sound.** — Background speech or noise should not make the model stop or cut itself short. This matters because users talk on trains and walks, not in quiet offices. ([11:12](https://youtu.be/18Um2VjMM_g?t=672))
- **Alphanumeric accuracy, such as postcodes and registration plates, is a separate hard problem in voice agents.** — In the insurance roadside demo, the agent had to look up a policy by plate and postcode, which the speakers say needs strong accuracy on codes and addresses. ([12:56](https://youtu.be/18Um2VjMM_g?t=776))

## Techniques
- **Native multimodal pretraining for audio tasks** — Train on interleaved audio, video and text sequences in one token embedding space so ASR, TTS, captioning and agentic tasks share one model and become prompts. *When:* When you want one model to handle transcription, translation, response and tool use without a separate pipeline per task.
- **Streaming translation as a prompt** — Prompt the same speech model with a streaming translation task and feed it audio; it emits translated speech as the speakers talk. *When:* For live multilingual conversation where you do not know the languages in advance and need low latency.
- **Proactive audio gating** — Let the model itself decide, from the audio context, whether an input is meant for it, so background speech or noise does not interrupt its output. *When:* For voice agents used on the move or in noisy places.
- **Managing the latency vs intelligence knob** — Measure how extra thinking affects time to first audio and conversational naturalness as well as evals, and push research to improve intelligence without a large latency cost. *When:* When raising reasoning effort for a voice agent starts to hurt responsiveness.
- **One promptable model for many modes** — Use one speech model with different prompts and tools for translation, search-style Q&A, developer voice agents and avatars, instead of separate models per product. *When:* When many voice products need the same core model and differ mainly by prompt and tool set.

## Numbers
- Streaming real-time translation supports 70-plus languages. ([8:24](https://youtu.be/18Um2VjMM_g?t=504))
- Streaming translation quality is said to be about as good as offline systems that see the full utterance first (qualitative, no metric given). ([4:39](https://youtu.be/18Um2VjMM_g?t=279))
- The majority of Gemini users are non-English speakers (qualitative). ([7:13](https://youtu.be/18Um2VjMM_g?t=433))

## Hot takes
- AGI will not be typed; it will be spoken.
- Voice will be the main conversational frontier, and visual presence (avatars) will be needed alongside it.
- Cascaded ASR+LLM+TTS pipelines cannot match the quality of a single speech-to-speech model for streaming translation.

## Tools mentioned
Gemini Live, Search Live, Gemini Live API, Google Meet speech translation

## Relevance to our work
- **agentos** (1/3): Voice input/output is not in the AgentOS layers; only a small overlap with the proxy idea of one endpoint for many agent features. → *If a voice front-end is ever added to the AgentOS proxy, budget for the thinking-effort vs time-to-first-audio trade-off the speakers describe.*
