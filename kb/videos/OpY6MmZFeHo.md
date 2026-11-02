# Voice Agents Can Just Do Things — Charlie Guo, OpenAI

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `OpY6MmZFeHo` · [watch](https://youtu.be/OpY6MmZFeHo) · **date:** 2026-09-18 · **length:** 15:50 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Charlie Guo · **orgs:** OpenAI
- **topics:** voice-multimodal, mcp-and-tools, product-ux · **tags:** voice agents, realtime API, speech-to-action, event-to-speech, preambles, native audio, tool calling, accessibility, proactive notifications, GPT Realtime 2

> Charlie Guo (OpenAI) argues voice agents need not always talk back and lays out three voice modes (speech-to-speech, speech-to-action, event-to-speech), with GPT Realtime 2 as the example stack.

## Summary
The speaker, a developer-experience lead at OpenAI, says the common assumption that a voice agent must respond with speech is a misunderstanding. He describes three modes: speech-to-speech (the familiar talk-and-reply loop), speech-to-action (the model calls tools while the user talks), and event-to-speech (the model receives an event and proactively speaks). He notes these modes are old ideas, but current models make them practical, and they can be combined. He calls speech-to-action the most under-explored mode and gives examples such as form-filling, voice-driven creative tools, and computer use. He suggests developers expose existing app endpoints and UI actions as tools so users can drive their current software by voice, with guardrails. He also argues that non-speech feedback (animations, state changes, highlights, a ghost cursor) often suits users better, with voice reserved for the top of an escalation path. He contrasts chained STT→LLM→TTS pipelines with native audio models, which keep tone, interruptions and background noise, and presents GPT Realtime 2 as adding reasoning, parallel tool calls and preambles. He closes by advising builders to ask what role voice should play before choosing an agent design.

## Key ideas
- **Voice agents do not have to talk back.** — Speech is one output channel among several. The speaker wants listeners to take away that a voice model can respond through actions and UI changes, not only speech. ([0:08](https://youtu.be/OpY6MmZFeHo?t=8))
- **Three voice modes: speech-to-speech, speech-to-action, event-to-speech.** — They are not new (a showtimes phone line and car GPS are early examples), but current models make them far more capable. They are remixable, and the best products combine all three. ([1:13](https://youtu.be/OpY6MmZFeHo?t=73))
- **Speech-to-action is the most under-explored mode.** — Examples given are form-filling (talk for five minutes instead of typing a long government form and then review it), voice-driven creative tools, and computer use. The speaker frames this as a large unused capability gap. ([3:43](https://youtu.be/OpY6MmZFeHo?t=223))
- **Existing app endpoints and UI actions can become voice tools.** — API endpoints and React hooks map onto model tools with relatively little work, so users can drive current software by voice. Guardrails and safety checks are still required. ([6:26](https://youtu.be/OpY6MmZFeHo?t=386))
- **Non-speech feedback is often the better channel.** — Notifications, pop-ups, colour or shadow changes, text highlights and an animated cursor let the user see what is happening without words. Voice sits at the top of an escalation path: animate, then pop up, then speak. ([7:16](https://youtu.be/OpY6MmZFeHo?t=436))
- **Event-to-speech suits hands-free use and proactive outreach.** — Examples include a recipe app while cooking and an agent that gets attention when the user is looking elsewhere. Developers receive many events and logs, and the speaker says none of them should be shown or spoken all at once. ([8:05](https://youtu.be/OpY6MmZFeHo?t=485))
- **Native audio beats chained transcription.** — Chained pipelines (transcribe, LLM, text-to-speech) drop tone, cadence, interruptions and background noise. Latency was also significantly higher in the chained ChatGPT voice modes than in advanced voice mode. ([10:40](https://youtu.be/OpY6MmZFeHo?t=640))
- **Preambles keep the user informed during reasoning and tool calls.** — A prompt can make the model announce that it is checking something, such as a travel agent saying it will look up flight prices. This keeps the conversation moving while background actions run. ([12:36](https://youtu.be/OpY6MmZFeHo?t=756))
- **Start from the role of voice, not the type of agent.** — Ask what voice and audio should do in the interaction, then what the model can perceive, what context and tools it has, which tools it should run safely, and whether it should speak now, wait, or use a visual notification. ([13:46](https://youtu.be/OpY6MmZFeHo?t=826))

## Techniques
- **Three-mode voice design** — Classify each voice feature as speech-to-speech, speech-to-action, or event-to-speech, then combine modes in one product. *When:* When deciding how a voice feature should respond, or when a product seems to need speech for every reply.
- **Expose app verbs as tools** — Map existing API endpoints, React hooks and other app actions to model tools, then let the user trigger them by voice, with guardrails and safety checks. *When:* When adding voice control to software that already has an API or UI actions.
- **Escalating attention ladder** — For proactive events, start with a silent visual change, then a pop-up or notification, and speak only if the user still has not responded. *When:* When an agent must get the user's attention for events that vary in urgency.
- **Preamble prompting** — Prompt the realtime model to tell the user before it reasons or calls tools, for example saying it is checking prices. *When:* When tool calls or reasoning add latency to a live voice conversation.
- **Native audio streaming** — Send audio directly to a native-audio realtime model and receive audio back, instead of running transcription, text generation and speech synthesis as separate steps. *When:* When tone, interruptions, latency or background context matter to the interaction.
- **Role-first voice design checklist** — Before picking an architecture, answer: what the voice is for, what the model can perceive, what context and tools it has, which tools are safe to run, and whether to speak now, wait, or use a visual cue. *When:* At the start of designing any voice agent.

## Numbers
- Realtime 2 was released a couple of months before the talk, adding reasoning, parallel tool calls and preambles. No benchmark figures were given; the speaker only says it does 'pretty well' on the latest audio benchmarks. ([12:36](https://youtu.be/OpY6MmZFeHo?t=756))
- The speaker cites a folk split of face-to-face communication: 55% body language, 38% tone of voice, 7% words. This is an unsourced rule of thumb he uses to motivate keeping tone. ([11:41](https://youtu.be/OpY6MmZFeHo?t=701))
- Chained voice modes in ChatGPT had 'significantly higher' latency than advanced voice mode, with no figures given. ([11:41](https://youtu.be/OpY6MmZFeHo?t=701))
- Form-filling example: about an hour of form-filling could drop to about five minutes of talking, with a quick review. This is an illustrative estimate, not a measurement. ([3:43](https://youtu.be/OpY6MmZFeHo?t=223))

## Hot takes
- Voice is the next capability overhang.
- Why am I talking to an app or a terminal instead of to the whole computer?
- AGI will be spoken, not typed.
- The first voice tutorial most people build is a customer-support bot, but support agents could eventually feel more pleasant to talk to than the median human agent.

## Tools mentioned
GPT Realtime 2, OpenAI Realtime API, Codex, ChatGPT advanced voice mode, CarPlay, Google Maps, Spotify

## Relevance to our work
- **prosharness** (1/3): ProsHarness has phone-driven approvals. The speaker's escalation ladder (visual, then notification, then voice) is a pattern for when an agent should interrupt the user. → *Try a tiered attention ladder for ProsHarness approval requests: status change first, push notification next, voice or call only if unanswered.*
