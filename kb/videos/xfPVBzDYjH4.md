# Can Your Agent Hear You Now? Building Live Voice Agents with Gemini — Thor Schaeff

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `xfPVBzDYjH4` · [watch](https://youtu.be/xfPVBzDYjH4) · **date:** 2026-10-12 · **length:** 20:14 · **format:** demo · **quality:** 2/5 · **depth:** intro
- **speakers:** Thor Schaeff · **orgs:** Google DeepMind, LiveKit, Pipecat
- **topics:** voice-multimodal, models-research, mcp-and-tools · **tags:** gemini, gemini-live-api, voice-agents, native-audio, function-calling, live-translate, interactions-api, text-to-speech, image-generation, lyria, google-ai-studio, barge-in, grounding, livekit, pipecat

> A Google DeepMind developer-experience lead demos the Gemini Live API for real-time voice and vision agents, covering native-audio sessions, tool calls, live translation and stateful image generation. Mostly a product showcase with a few useful architecture points.

## Summary
Thor Schaeff from Google DeepMind's developer experience team walks through Gemini models for real-time, multimodal agents, mostly through live demos. He covers Gemini TTS, the newly shipped Nano Banana Lite (faster image generation and editing) and Gemini Live Translate, which detects the speaker's language and translates in near real time. The core technical section explains the Live API: a stateful WebSocket session that takes streamed text, audio and video frames and returns audio chunks plus a transcript. He contrasts this native-audio model with a cascaded speech-to-text, LLM, text-to-speech pipeline, arguing that the understanding lives in the audio model, which allows fluid switching across 90 preview languages, barge-in and tool calls. Demos show a live story-illustrating agent calling the Interactions API, a radio-DJ agent that calls Lyria 3 for music, and Google Search grounding as a built-in function call. Most of the talk is a product pitch, and the claims are shown rather than benchmarked.

## Key ideas
- **Native audio model vs cascaded voice pipeline** — Live API uses a native audio model rather than STT, then LLM, then TTS. The speaker says the intelligence sits in the audio model itself, which lets it understand speech directly and switch languages fluidly. ([14:54](https://youtu.be/xfPVBzDYjH4?t=894))
- **Live API is a stateful WebSocket session** — One session takes text, audio and video frames in real time and streams back audio chunks plus a transcript. The client is responsible for playing the chunks back. ([13:35](https://youtu.be/xfPVBzDYjH4?t=815))
- **Barge-in and tool calls inside a live voice session** — Users can interrupt the model mid-speech. The session also supports function calls, so a voice agent can call an external API during a conversation, such as a music generator or a CRM lookup. ([11:01](https://youtu.be/xfPVBzDYjH4?t=661))
- **Live Translate detects language and translates as you speak** — The model starts translating once it has enough context of what is being said. The listener picks a target language from a QR-code page, and the speaker never needs to name the source language. ([7:12](https://youtu.be/xfPVBzDYjH4?t=432))
- **Stateful Interactions API chains generations for visual consistency** — Passing the previous interaction ID into the next call gives the model the earlier context. The speaker uses this to keep characters and style consistent across several image generations. ([5:46](https://youtu.be/xfPVBzDYjH4?t=346))
- **Image generation latency is the practical bottleneck in live demos** — Nano Banana Lite is pitched as cutting latency for image generation and editing. Even so, the speaker says generation still takes about two to three seconds, which is why a live agent needs a tool-call pattern for it. ([4:47](https://youtu.be/xfPVBzDYjH4?t=287))
- **Grounding with Google Search as a built-in function call** — Enabling search grounding lets the model answer questions about current events, such as today's weather, without writing a custom tool. The speaker frames it as a built-in function call. ([17:45](https://youtu.be/xfPVBzDYjH4?t=1065))

## Techniques
- **Stateful WebSocket session for real-time multimodal agents** — Open one session, stream text, audio and video frames up over the WebSocket, and stream audio chunks plus transcript back to the client. Use the transcript for logs or UI. *When:* Building low-latency voice or vision agents where a request/response API adds too much delay.
- **Tool call from a live voice agent to a slow generator** — Give the live agent a function declaration. When the user asks for something, such as a song, the agent calls the external generation API (Lyria 3 in the demo) and speaks the result when it returns. *When:* Voice agents that must trigger slow backend work (music, image, ticket creation) while keeping the conversation going.
- **Chaining generations with the previous interaction ID** — Store the interaction ID from each Interactions API response and pass it into the next call so the model keeps the earlier context. *When:* Multi-step generation where consistency across outputs matters, such as illustrating a story with the same characters.
- **Native audio vs cascaded voice pipeline** — Send raw audio to a native audio model instead of chaining STT, LLM and TTS. The speaker suggests this makes language switching and interruption easier, but gives no measurements. *When:* Real-time conversational agents that need multilingual speech and barge-in, where the speaker's claims would be tested against latency and accuracy before adopting.

## Numbers
- Image generation via Interactions API takes about two to three seconds ([4:47](https://youtu.be/xfPVBzDYjH4?t=287))
- Live API supports 90 languages in preview ([14:54](https://youtu.be/xfPVBzDYjH4?t=894))
- Gemini TTS now has lower latency than before, with streaming and inline audio steering (no figure given) ([0:12](https://youtu.be/xfPVBzDYjH4?t=12))

## Hot takes
- Native audio models should replace cascaded STT, LLM and TTS pipelines for real-time conversational agents (speaker's claim, no benchmark shown)
- Demo apps built in AI Studio are less useful as business products, but their individual components (multilingual, barge-in, tool calls) are reusable

## Tools mentioned
Gemini Live API, Gemini 3.1 Flash Live, Gemini 3.5 Live Translate, Gemini TTS, Nano Banana Lite, Omni Flash, Lyria 3, Gemini Interactions API, Google AI Studio, LiveKit, Pipecat

## Relevance to our work
- **general** (1/3): Shows a stateful interaction-ID chaining pattern and a native-audio versus cascaded pipeline comparison, with no measurements. → *If voice agents come up, check the Live API docs for the native-audio session model and compare its latency against our cascaded pipeline before choosing one.*
