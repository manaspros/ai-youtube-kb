# Granola, But Open Source and Local (Meetily)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `LCoF8dCVkIw` · [watch](https://youtu.be/LCoF8dCVkIw) · **date:** 2026-08-02 · **length:** 5:43 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, NVIDIA, Granola, Otter, Fireflies
- **topics:** local-ai, dev-tools · **tags:** meeting-notes, transcription, speech-to-text, local-first, privacy, open-source, offline, parakeet, whisper, macos, tauri, nextjs, rust, ollama

> Short walkthrough of Meetily, an open-source, local-first meeting transcriber that captures system audio without joining calls. Speech-to-text runs on-device; summaries can use a local model or a cloud API key.

## Summary
The speaker presents Meetily as an open-source alternative to cloud meeting notetakers like Granola, Otter and Fireflies. Instead of sending a bot into the call, it records the computer's audio locally, so it works with Zoom, Meet, Teams and Discord without a visible participant. A live demo with Wi-Fi turned off shows the transcript and speaker labels still updating, since speech-to-text runs on the machine. The stack is a Rust backend, a Tauri desktop shell (auto-captioned as "Tari") and a Next.js front end, with Whisper or NVIDIA Parakeet (now the default) for transcription. The speaker says Parakeet is about four times faster than Whisper on Apple Silicon, and notes are stored in a local database. Summaries are the weak spot: the user can run a local model or paste a cloud API key (Claude or Grok), which gives better summaries but sends the text off the machine while the audio stays local. Known gaps the speaker lists are weak handling of non-English meetings, no speaker separation yet, pre-1.0 instability and macOS permission friction. The video is short and anecdotal, with no benchmarks beyond one speed claim.

## Key ideas
- **Bot-free capture: Meetily does not join the meeting. It listens to the computer's audio the way a screen recorder would, so there is no visible participant or calendar access.** — Contrasts with Otter and Fireflies, which add a bot that needs calendar access and routes audio through a third party. Works with any app that plays sound. ([0:00](https://youtu.be/LCoF8dCVkIw?t=0))
- **Speech-to-text runs fully on-device. The demo turns off Wi-Fi and the transcript keeps updating, with punctuation and speaker labels.** — The speaker's argument is that audio never leaves the laptop, which gives privacy for sensitive meetings, offline operation and lower latency. Claimed extras include swapping models, custom vocabulary and embedding it in other apps. ([0:46](https://youtu.be/LCoF8dCVkIw?t=46))
- **Stack and model choice: Rust backend, Tauri desktop shell and Next.js front end. Transcription uses Whisper or NVIDIA Parakeet, and Parakeet is the default.** — The speaker runs it on Apple Silicon and says Parakeet is about 4x faster than Whisper. Notes are saved to a local database on disk. ([1:59](https://youtu.be/LCoF8dCVkIw?t=119))
- **Transcription is treated as solved, so summarization is the real gap versus paid tools. The fix is a pluggable summary backend: a local model, or a cloud API key set in settings.** — With a cloud key the summaries are cloud quality, but the audio still stays local while the text leaves the machine. The speaker calls this a trade of a little privacy for a much better summary. ([3:03](https://youtu.be/LCoF8dCVkIw?t=183))
- **Honest limitations: multi-language meetings come out poorly (Whisper tends to flatten everything to English), speaker separation is not in the open-source build yet, and the project is pre-1.0.** — Expect macOS microphone and screen-recording permission problems during setup. The speaker says none of this kills the tool. ([4:09](https://youtu.be/LCoF8dCVkIw?t=249))
- **Design stance: the tool does not pretend a local model matches the cloud one. It exposes the local-vs-cloud switch per meeting and leaves the decision to the user.** — The project has nearly 13,000 GitHub stars and ships updates often, according to the speaker. ([4:56](https://youtu.be/LCoF8dCVkIw?t=296))

## Techniques
- **Bot-free system-audio capture** — Capture the computer's output audio locally, as a screen recorder would, instead of joining the call as a participant. On macOS, grant the app microphone and screen-recording access. The speaker says this works across Zoom, Meet, Teams and Discord with no meeting setup. *When:* When you want no visible recorder in the attendee list, no calendar access for a bot, and no third party receiving the audio.
- **Split local-audio / optional-cloud-summary pipeline** — Run speech-to-text on the device with the default Parakeet model (or Whisper). For summaries, choose one of two options in settings: a locally hosted model (the speaker says a local llama-style model; the transcript is unclear, likely Ollama) for fully offline notes, or a pasted cloud API key (Claude or Grok) when summary quality matters. Decide per meeting. *When:* When the audio is sensitive but you still want better summaries for some meetings. The audio stays local and only the transcript text goes to the cloud, and only when you turn that on.
- **Setup on a Mac (Apple Silicon)** — Download the Apple Silicon build from the project. Grant microphone and screen-recording access in macOS privacy settings. In the app, pick the transcription model (Parakeet is the default) and the summary backend (local model or cloud key). The speaker says he fought the permission prompts before it worked. *When:* First-time install on macOS, when you want to reproduce the setup the speaker shows.
- **Offline-verification test** — Turn Wi-Fi off during a meeting or test call and confirm the live transcript keeps updating. This is how the speaker checks that speech-to-text really runs on the device. *When:* When you need to confirm a claimed local-only data path before trusting it with sensitive meetings.

## Numbers
- Cloud meeting-notetaker seats cost about $10-30 per month each (Granola, per the speaker). ([3:03](https://youtu.be/LCoF8dCVkIw?t=183))
- Parakeet runs about 4x faster than Whisper on Apple Silicon (speaker's own observation, not a benchmark). ([3:03](https://youtu.be/LCoF8dCVkIw?t=183))
- Meetily has almost 13,000 GitHub stars (speaker's figure). ([4:56](https://youtu.be/LCoF8dCVkIw?t=296))
- Demo: transcript keeps updating with Wi-Fi fully off, since speech-to-text runs locally. ([0:46](https://youtu.be/LCoF8dCVkIw?t=46))

## Hot takes
- The 'audio never leaves your laptop' claim is only true in fully local mode. With a cloud summary key, the transcript text leaves the machine, and the speaker says so.
- The speaker says the open-source build 'can't separate speakers yet', yet the demo shows speaker labels in the live transcript at 0:46. This conflicts and needs checking against the current release.
- The speaker treats summaries as the real moat for paid tools, and the cloud-key fallback is an admission that the local summary path is not good enough.
- Auto-caption errors: 'Meetedly' and 'Meet Elite' mean Meetily; 'Tari' means Tauri; 'clod' means Claude; 'Alamo' is probably Ollama.

## Tools mentioned
Meetily, Granola, Otter, Fireflies, OpenAI Whisper, NVIDIA Parakeet, Ollama (likely; transcript says 'llama'/'Alamo'), Claude (cloud API key), Grok (cloud API key), Zoom, Google Meet, Microsoft Teams, Discord, Rust, Tauri (auto-captioned as 'Tari'), Next.js, macOS / Apple Silicon

## Relevance to our work
- **agentos** (1/3): The local-audio / optional-cloud-summary split is a small example of per-task privacy routing, similar to what Govrix Scout's routing and PII scanning would need to handle. Not a direct change to AgentOS. → *Note the local-STT-then-cloud-summary split as a per-request routing example when designing a privacy-scoped route in Govrix Scout (for example, keep raw inputs on local models and send only redacted text to cloud models).*
