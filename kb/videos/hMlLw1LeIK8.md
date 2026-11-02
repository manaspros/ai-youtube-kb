# Designing Voice Agents for Real Conversations - Chintan Agrawal & Daniel Wirjo, AWS

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `hMlLw1LeIK8` · [watch](https://youtu.be/hMlLw1LeIK8) · **date:** 2026-08-18 · **length:** 32:57 · **format:** talk · **quality:** 4/5 · **depth:** practitioner
- **speakers:** Chintan Agrawal, Daniel Wirjo · **orgs:** AWS, Cartesia, Deepgram, Pipecat, Salesforce, Daily
- **topics:** voice-multimodal, infra-cost-scaling · **tags:** voice-agents, turn-taking, vad, silero, smart-turn, pipecat, barge-in, latency-budget, p95, cascaded-pipeline, endpointing, interruptions

> AWS solutions architects walk through turn-taking in voice agents: three levels from Silero VAD silence timers to Smart Turn, plus latency budgets and production issues. Includes live Pipecat demos.

## Summary
Chintan Agrawal and Daniel Wirjo (AWS startups team) argue that turn-taking in voice agents is an audio-pipeline problem, not an LLM problem, and that humans switch turns in about 200 ms. They compare three ways to decide when the user has finished: a Silero VAD silence timer you fully own, STT-native endpointing from Cartesia and Deepgram (accurate but opaque), and a hybrid of VAD plus the open Smart Turn v3 model that runs during silence with the VAD timer as fallback. They also cover barge-in handling, where interruptions can be classified so that corrections stop the agent while backchannels and noise do not. The latency section breaks a cascaded pipeline into stages; the LLM time-to-first-token and STT with endpointing dominate, and typical cloud-API setups land around 800 to 1300 ms voice-to-voice. They argue P95 matters more than P50 for voice, and that instruction following can drift after 15 to 20 turns. Daniel then demos the three approaches in Pipecat, showing that a fixed 300 ms stop timer can cut users off mid-sentence and that the Smart Turn logs show whether the model or the silence timer ended the turn.

## Key ideas
- **Turn-taking is an audio problem, not a model problem** — A perfect LLM still feels broken if the system misjudges when the user stopped talking. Humans switch turns in about 200 ms, and latency above roughly 800 ms feels off while 1.5 s makes users hang up. The same LLM gave very different experiences depending only on the audio pipeline's interruption handling. ([0:03](https://youtu.be/hMlLw1LeIK8?t=3))
- **Level 1 (Silero VAD + silence timer) cannot tell intent apart** — Silero is a small (~300k parameter, ~2 MB) speech/no-speech model. A fixed minimum-silence setting is the whole UX knob: low values cut people off, high values cause dead air. VAD sees a breath pause, a finished thought, a backchannel and a barge-in as the same silence, so it cannot separate them. Tuning depends on the domain (about 200 ms for sales, 1000 to 1200 ms where users need time). ([5:17](https://youtu.be/hMlLw1LeIK8?t=317))
- **Level 2: let the STT provider decide the end of turn** — Cartesia and Deepgram run endpointing inside the STT websocket using full audio plus linguistic context, so they are usually smarter than a VAD timer. The trade-off is observability: when they cut someone off, there is no log explaining why, so the failure is hard to debug. ([7:55](https://youtu.be/hMlLw1LeIK8?t=475))
- **Level 3: VAD for speech, Smart Turn for the end-of-turn call, timer as safety net** — Keep local VAD for the basic speech signal and run Smart Turn v3.2 (BSD-2, about 8 MB) during silence to judge whether the utterance is complete from prosody and intonation. It catches about 6 in 10 completed sentences quickly. When it does not fire, the configured silence timer (for example 300 ms) still ends the turn, so the agent is never stuck. The team says it is the best deployable open option today. ([9:16](https://youtu.be/hMlLw1LeIK8?t=556))
- **Barge-in should be classified, not always treated as a stop** — Interruptions are detected in about 32 ms, and the pipeline flush (TTS stop, LLM cancel) takes about 15 ms. The speaker argues that most systems stop on every sound, but a correction should stop the agent while a filler or acknowledgement should let it keep going, possibly quieter. Owning the classifier (Level 3) makes this possible. ([12:14](https://youtu.be/hMlLw1LeIK8?t=734))
- **Tail latency (P95) matters more than median in voice** — GPT-4.1 has a good P50 (about 536 ms time-to-first-token) but spikes to about 1.7 s at P95 and over 4 s on the worst cases. In a live conversation one slow turn breaks the flow, so averages hide the real problem. The team's target is under 700 ms time-to-first-token. ([19:02](https://youtu.be/hMlLw1LeIK8?t=1142))
- **Multi-turn drift and false interrupts have product costs** — After 15 to 20 turns the model may ignore system-prompt parts, become verbose, or drift off persona, and walls of text are bad in voice. Context pruning or session resets are suggested. False interruptions raise the escalation-to-human rate, so turn-taking errors are a business metric as well as a UX one. ([19:02](https://youtu.be/hMlLw1LeIK8?t=1142))

## Techniques
- **Hybrid VAD + learned end-of-turn model with timer fallback** — Run a local VAD (Silero) for speech presence. Run Smart Turn during silence to decide whether the utterance is complete. If it does not fire within the configured silence window, end the turn anyway. Swap the turn analyzer in Pipecat via configuration; the rest of the pipeline stays the same. *When:* When you need control, auditability and portability (for example for compliance) and can run a small model locally or on a GPU. Use it when a learned end-of-turn signal is worth the extra model.
- **Interruption classification at barge-in** — When the user speaks while the agent is talking, classify the sound (correction, filler/backchannel, background noise) instead of always flushing. Flush TTS and cancel LLM generation only for corrections. *When:* When false stops are hurting the experience or escalation rate and you own the turn-detection stage.
- **Per-stage latency budget with P50 and P95 tracking** — Break voice-to-voice latency into encode, network/JWT, STT plus endpointing, LLM time-to-first-byte, and network out plus playback. Measure P50 and P95 per stage, and set a target (for example under 700 ms time-to-first-token for the LLM). *When:* When choosing models or regions for a real-time agent, or when diagnosing why total latency is high.
- **Co-location to remove network hops** — Place STT, LLM and TTS in the same GPU cluster or region to remove inter-service network round trips. *When:* When you can invest in self-hosted infrastructure and need latency close to 500 ms voice-to-voice rather than 800 to 1300 ms over cloud APIs.
- **Session pruning or reset for long voice sessions** — Monitor instruction-following and verbosity across turns, then prune context or start a new session after about 15 to 20 turns when the agent starts drifting. *When:* For long-running voice or chat sessions where the system prompt is being ignored or responses are growing too long.
- **Config-only swap between turn-detection strategies for A/B tests** — Keep the Pipecat pipeline identical and change only the turn-detection analyzer (Silero VAD, Cartesia Turns STT, or Silero plus Smart Turn). Compare debug logs for end-of-turn decisions. *When:* When evaluating which turn-taking approach fits your domain before committing.

## Numbers
- Human turn-switch time is about 200 ms; latency around 800 ms feels off and about 1.5 s causes users to hang up ([1:37](https://youtu.be/hMlLw1LeIK8?t=97))
- Salesforce's published best voice response time (March 2025 per speaker) was 755 ms, which the speaker says is about 4x slower than human turn-taking ([2:58](https://youtu.be/hMlLw1LeIK8?t=178))
- Silero VAD is about 300k parameters and about 2 MB ([5:17](https://youtu.be/hMlLw1LeIK8?t=317))
- Cartesia endpointing P50 about 300 ms; Deepgram Nova 3 endpointing P50 about 250 ms ([7:55](https://youtu.be/hMlLw1LeIK8?t=475))
- Smart Turn v3.2: about 58.9% recall and 68.4% precision on completed sentences, roughly 6 of 10 caught quickly; a March paper reported 87.7% recall but released no code; Smart Turn is about 8 MB and BSD-2 licensed ([9:16](https://youtu.be/hMlLw1LeIK8?t=556))
- Interruption detected in about 32 ms; pipeline flush takes about 15 ms ([10:44](https://youtu.be/hMlLw1LeIK8?t=644))
- Latency breakdown: encode about 40 ms, network/JWT about 52 ms, STT plus endpointing about 300 ms, LLM time-to-first-byte 500 to 650 ms (the dominant term), network out plus playback about 120 to 185 ms; total about 1100 to 1300 ms on standard cloud APIs ([14:46](https://youtu.be/hMlLw1LeIK8?t=886))
- Co-located models in one GPU cluster reached about 500 ms voice-to-voice; typical developer API setups are about 800 to 1300 ms ([16:15](https://youtu.be/hMlLw1LeIK8?t=975))
- Time-to-first-token P50 (June 2026 benchmark): Nemotron 3 Ultra 529 ms, GPT-4.1 536 ms; target under 700 ms ([16:15](https://youtu.be/hMlLw1LeIK8?t=975))
- GPT-4.1 P95 about 1.7 s, with some outliers over 4 s ([19:02](https://youtu.be/hMlLw1LeIK8?t=1142))
- Speaker cites 755 ms as the best measured voice-to-voice for a cascaded pipeline ([19:02](https://youtu.be/hMlLw1LeIK8?t=1142))
- Demo: default Silero stop timer of 300 ms ended the user's turn mid-sentence ([24:43](https://youtu.be/hMlLw1LeIK8?t=1483))

## Hot takes
- Most voice-agent turn-taking failures are audio-pipeline failures, not LLM failures.
- Always stopping on every interruption is the default and it is wrong; corrections should stop the agent, acknowledgements should not.
- For voice, P95 time-to-first-token matters far more than P50, because one slow turn breaks the conversation.
- Opaque STT-native turn detection is a debugging risk: when it cuts users off you cannot see why.
- Escalation-to-human rates rise with false interruptions, so turn-taking is a business metric.

## Tools mentioned
Pipecat, Silero VAD, Smart Turn v3, Cartesia (STT and Sonic TTS), Deepgram Nova 3, Claude Haiku, GPT-4.1, Nemotron 3 Ultra

## Relevance to our work
- **agentos** (1/3): AgentOS has no voice pillar, but the talk's point that opaque turn decisions are hard to debug maps loosely to the L4 observability and audit goals. → *Only if voice enters AgentOS: require any turn or endpoint decision made by a provider to be logged with its reason before adopting it.*
- **prosharness** (1/3): The talk's observation that instruction-following drifts after 15 to 20 turns is a data point for when long Claude Code runs need checkpointing or a session reset. → *Consider using the 15 to 20 turn drift observation as a rough default trigger for a checkpoint or fresh-session resume in long ProsHarness runs, then check it against our own logs.*
- **general** (1/3): Useful as a reference on how to split latency budgets and how to structure configurable pipeline stages, but not a direct change to our work. → *Read the Pipecat turn-detection docs and Smart Turn repo if we ever build a voice interface.*
