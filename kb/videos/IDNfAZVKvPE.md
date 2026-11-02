# "My name is... my name is...": A Linguistic Map for Voice Agents — Midam Kim, ServiceNow

- **channel:** [AI Engineer](../channels/aie.md) · **id:** `IDNfAZVKvPE` · [watch](https://youtu.be/IDNfAZVKvPE) · **date:** 2026-09-18 · **length:** 15:05 · **format:** talk · **quality:** 3/5 · **depth:** intro
- **speakers:** Midam Kim · **orgs:** ServiceNow
- **topics:** voice-multimodal, evals, product-ux · **tags:** voice agents, linguistics, turn-taking, ASR, TTS, mental model, EvaBench, conversation design, user frustration

> Midam Kim (ServiceNow) uses a linguistics framework to explain why voice agents fail and proposes diagnosing them by listen/speak channels, timing, and the user's mental model.

## Summary
Midam Kim, an ML engineer at ServiceNow, opens with a voice-bot call where spelling, account-number capture and turn-taking all broke, and the bot never tried interactive clarification. He frames voice AI as a joint activity between two parties, the way human conversation is, rather than a one-way pipeline. His framework has two channels (listening and speaking) crossed with four layers: sounds, words, interaction (turn timing) and mental model (task intent). He argues these layers are interdependent and must be aligned, and that the conversation runs on a timeline where only the user's evolving mental model persists after the audio is gone. He lists engineering levers (ASR/TTS choice and pre/post-processing, vocabulary, turn detection, emotion handling, dynamic context retention) and says business metrics such as escalations and abandoned calls follow from linguistic failures. He points to ServiceNow's EvaBench as a way to diagnose a voice agent, and closes by saying speakers adapt and languages change, so systems must keep up. The talk gives a diagnostic lens but no fixes or measured results.

## Key ideas
- **Voice agent failures are linguistic failures, shown through a real call.** — A bot misheard M vs N in a spelled name, applied English-centric TTS reading rules to the spelling, cut the user off during an account number, and then asked for a repeat without trying clarification. The user asked for a human. ([0:08](https://youtu.be/IDNfAZVKvPE?t=8))
- **Treat voice AI as a joint activity, not a pipeline.** — Human conversation is two parties taking turns and updating shared mental models. The speaker says users expect this same mutual process from bots. ([3:29](https://youtu.be/IDNfAZVKvPE?t=209))
- **Use a two-channel by four-layer grid to locate failures.** — Listening and speaking channels each have sounds (recognition or pronunciation), words (understanding or word choice), interaction (turn timing), and mental model (intent or the information the user needs). ([6:35](https://youtu.be/IDNfAZVKvPE?t=395))
- **The layers are interdependent and must be aligned.** — Good sounds depend on word-level handling, which depends on turn-taking, which is needed for task completion. Missing any one layer makes the agent fail. ([7:38](https://youtu.be/IDNfAZVKvPE?t=458))
- **Voice is silently tracked on a timeline, so only the mental model persists.** — Unlike chat, spoken words leave no visible history. The user's evolving mental model is the only thing that remembers the call, so it is the thing to manage. ([9:09](https://youtu.be/IDNfAZVKvPE?t=549))
- **Satisfaction levers are dynamic, not one-off settings.** — The speaker lists ASR and TTS choice with pre- and post-processing, shared vocabulary, turn detection and latency, emotion handling, and context retention. All of these need to adjust during the call and fit different users, including unhappy ones. ([10:12](https://youtu.be/IDNfAZVKvPE?t=612))
- **Linguistic quality links directly to business metrics.** — Better handling should lower user frustration, task failures, live-agent escalations, abandoned calls, and silent failures. The speaker says business implications are linguistic implications. ([11:36](https://youtu.be/IDNfAZVKvPE?t=696))
- **Speakers adapt and languages drift, so systems need to keep up.** — Users adapt to the agent during a call and across calls. The speaker asks whether a system will still fit language change within months. ([13:50](https://youtu.be/IDNfAZVKvPE?t=830))

## Techniques
- **Linguistic diagnostic grid for voice agents** — Score each failure on channel (listen or speak) times layer (sounds, words, interaction, mental model) to find which layer broke, rather than blaming the whole pipeline. *When:* When debugging a voice agent or auditing a call transcript to decide whether the ASR, TTS, turn-taking or task logic is at fault.
- **Interactive clarification on recognition errors** — When the bot is unsure of a spelled name or an identifier, it confirms the specific uncertain item (for example, asking about M vs N) instead of repeating the whole request or silently proceeding. *When:* For spelled names, account numbers and other identifiers where ASR errors are common.
- **Locale-aware pre-processing for TTS and vocabulary** — Curate a shared vocabulary and pre-process text so that spelled letters, codes and names are not read with default English rules. *When:* When the agent reads back names, spelled strings or codes that the default TTS pronounces wrongly.
- **Turn-taking and barge-in control** — Tune turn detection and latency so the bot does not cut the user off mid-number and only speaks when it is its turn. *When:* When users read long strings such as account numbers, or pause while thinking.
- **Dynamic per-call context retention** — Keep track of the user's current intent and known facts across the timeline, and adapt the style for different users and emotional states during the call. *When:* For long multi-turn voice calls where users get frustrated or change plans mid-call.
- **EvaBench for diagnosing voice agents** — Run ServiceNow's EvaBench, a speech-to-speech benchmark, to diagnose a voice agent's status across the framework layers. *When:* When you need a structured voice-agent eval before tuning ASR, TTS or turn-taking.

## Hot takes
- Voice is called the most natural interface, but it is actually hard, and a bad voice bot fails catastrophically.
- Business implications of voice AI are linguistic implications, so hire linguists as well as engineers.
- Only the user's mental model persists in a voice call, so context management matters more than the audio pipeline.

## Tools mentioned
EvaBench

## Relevance to our work
- **general** (1/3): The layer-by-channel grid could serve as a rubric for failure analysis in any conversational agent eval, including chat. → *Try a listen/speak x sounds/words/interaction/mental-model tagging pass on a sample of failed transcripts from an existing agent eval to see whether the grid surfaces failure modes that a flat error label misses.*
