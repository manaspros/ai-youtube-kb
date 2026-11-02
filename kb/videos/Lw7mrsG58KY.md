# Qwen TTS Just Changed Open-Source Voice

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `Lw7mrsG58KY` · [watch](https://youtu.be/Lw7mrsG58KY) · **date:** 2026-03-02 · **length:** 4:55 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Alibaba (Qwen), Microsoft, ElevenLabs
- **topics:** voice-multimodal, local-ai · **tags:** tts, voice-cloning, open-source, qwen3-tts, local-inference, streaming, emotion-control, chatterbox, vibe-voice, elevenlabs

> Hands-on test of Qwen3 TTS, an Apache 2.0 open-source voice model that is steered by plain-language emotion and persona instructions and runs fully local; compares it with ElevenLabs, Chatterbox and Vibe Voice.

## Summary
The host runs Qwen3 TTS, an open-source text-to-speech model from Alibaba, through its local web UI and judges it by ear. Voice cloning uses a reference recording plus its exact transcript, and the lighter model clones from about three seconds of audio, which the host calls decent but generated-sounding. The 1.7B variant drops cloning but adds real-time streaming (about 97 ms claimed latency), ten languages and code switching. Its main feature is an instruction box where emotion and persona are described in natural language, and the host says it mostly followed prompts like "suspenseful narrator" and a sarcastic-but-friendly developer, with some misses. Compared with the others, the host says ElevenLabs is still the best but costs money and sends data off the machine, Chatterbox has good emotion, and Microsoft's Vibe Voice is the best cloner. Caveats are that output is only as good as the prompt, a GPU is recommended, and the model is still maturing in some languages. Setup is clone, install dependencies, launch, open localhost, with no API keys.

## Key ideas
- **Emotion and persona are set with a natural-language instruction box, not presets. The same sentence can be delivered as a calm read or a frustrated rant just by describing the delivery.** — The host types a delivery description (for example a suspenseful narrator with a slow build and a relieved laugh at the end) and keeps the target text separate. Results are mostly right, with some tones missed. ([0:00](https://youtu.be/Lw7mrsG58KY?t=0))
- **Two model sizes trade off features. The lighter model clones a voice from about three seconds of reference audio. The 1.7B model drops cloning but adds streaming, multilingual output and lower latency.** — Lighter model: three-second voice cloning. 1.7B: real-time streaming at a claimed 97 ms latency, 10 languages with natural code switching, Apache 2.0, fully local and free. ([0:55](https://youtu.be/Lw7mrsG58KY?t=55))
- **Voice cloning from the lighter model is only decent. Some clips sound generated. The host rates Microsoft's Vibe Voice as the best clone among those tried.** — Cloning was run by uploading a reference recording, typing its exact transcript and typing the target text. The host says it took longer to run than expected. ([1:52](https://youtu.be/Lw7mrsG58KY?t=112))
- **Persona prompting is the most useful part. Describing a character in words (young, enthusiastic, slightly sarcastic developer) replaces picking a numbered voice preset.** — The host calls this natural-language voice design more intuitive and faster to iterate than preset selection. ([3:07](https://youtu.be/Lw7mrsG58KY?t=187))
- **The host's competitor ranking: ElevenLabs is still the best but costs money and the data leaves the machine. Chatterbox has good emotion. Vibe Voice is the best cloner. Qwen3 TTS wins for describing voices and iterating quickly.** — This is a single informal listening comparison with no shared test set or metrics. ([3:07](https://youtu.be/Lw7mrsG58KY?t=187))
- **Output quality depends on how specific the direction is. A vague instruction gives a vague voice, and the model is still maturing in some languages.** — The host also notes that a GPU is recommended. CPU works but is slower. ([4:19](https://youtu.be/Lw7mrsG58KY?t=259))
- **Setup is short and needs no cloud account. Clone the repo, install dependencies, launch the web UI and open localhost. No API keys or billing are involved.** — The host says it went from zero to a working demo in a few minutes. ([4:19](https://youtu.be/Lw7mrsG58KY?t=259))

## Techniques
- **Voice cloning in the Qwen3 TTS web UI** — Upload a short reference recording of the target voice. Type the exact words spoken in that recording into the reference-text field. Type the new line into the target-text field and generate. Expect the lighter model to sound generated at times. *When:* Quick voice cloning on a local machine with no external API, when clone fidelity matters less than privacy and cost.
- **Emotion and delivery via the instruct box** — Keep the spoken text in the target-text box. Describe the delivery in plain language in the separate instruct box, for example a narrator with a slow build-up and a relieved laugh at the end. Iterate by making the description more specific, since vague instructions produce vague output. *When:* Making TTS sound like a particular delivery (narration, a rant, a suspenseful read) without training or presets.
- **Persona voice design** — Write a character description in the instruct box (age, energy, attitude, for example a young enthusiastic developer who is a bit sarcastic but friendly). Generate the same text under several descriptions to compare. *When:* Prototyping an agent or assistant voice personality without choosing from a fixed preset list.
- **Local setup** — Clone the Qwen3 TTS repo, install its dependencies, launch the web UI, and open the localhost URL it prints. No API keys are needed. The speaker does not show exact commands, and the repo link is in the video description, not the transcript. *When:* Running open-weight TTS privately for prototyping or a local voice agent. A GPU is recommended.

## Numbers
- Claimed streaming latency of 97 ms for the 1.7B model (real-time streaming) ([0:55](https://youtu.be/Lw7mrsG58KY?t=55))
- Lighter model clones a voice from about 3 seconds of reference audio ([0:55](https://youtu.be/Lw7mrsG58KY?t=55))
- 10 supported languages with natural code switching, Apache 2.0 license ([0:55](https://youtu.be/Lw7mrsG58KY?t=55))
- Setup from zero to working demo in a few minutes, with no API keys or billing ([4:19](https://youtu.be/Lw7mrsG58KY?t=259))

## Hot takes
- Qwen3 TTS is the best open-source option for describing a voice in natural language and iterating quickly.
- Vibe Voice from Microsoft is the best voice cloner of those tried, better than the Qwen3 clone.
- ElevenLabs is still king on quality, but cost and sending data to a third party are its drawbacks.
- Emotion control in open-source TTS depends mostly on prompt quality.

## Tools mentioned
Qwen3 TTS (Alibaba open-source TTS; 1.7B variant and a lighter model, size not stated), Chatterbox (open-source TTS with emotion slider), Vibe Voice (Microsoft, voice cloning), ElevenLabs (commercial TTS)

## Relevance to our work
- **agentos** (1/3): Local TTS is a possible voice I/O add-on for agents, but voice is not one of the AgentOS pillars. A 1.7B TTS model would compete for the single RTX 5090 with vLLM. → *If voice I/O is ever added, benchmark TTS latency next to InferCraft's vLLM load on the single RTX 5090 before committing. No action needed now.*
