# I Haven't Typed in a Week (Thanks to This App)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `ZRsDQp9CrXc` · [watch](https://youtu.be/ZRsDQp9CrXc) · **date:** 2026-08-02 · **length:** 8:18 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Andres (Better Stack host) · **orgs:** Better Stack, Google, Wispr
- **topics:** local-ai, voice-multimodal, dev-tools · **tags:** speech-to-text, dictation, offline, whisper, parakeet, open-source, rust, tauri, silero-vad, push-to-talk, privacy

> Better Stack host tours Handy, an open-source, MIT-licensed, fully offline dictation app with user-chosen models, and compares its output against Google Docs voice typing and Wispr Flow on one passage.

## Summary
The host introduces Handy, a free and open-source speech-to-text dictation app that runs fully offline with no account or subscription, and says it has become his daily dictation tool. He explains the stack (Rust backend, React/TypeScript settings UI, whisper-family and Parakeet model backends, Silero VAD for silence gating) and the usage flow: a global shortcut in toggle or push-to-talk mode, with the transcribed text pasted into whatever input is focused. He highlights the ability to pick models by a speed/accuracy trade-off, including a CPU-only Parakeet model, and to drop in custom fine-tuned Whisper GGML files. To test accuracy, he dictates one passage with a tangent full of technical terms into Handy, Google Docs voice typing and Wispr Flow, one run each. Google's output is weakest (no punctuation, misheard terms), Handy adds punctuation and gets most technical terms, and Wispr Flow is best but only slightly ahead. The evidence is a single anecdotal test, and the video is an informal product review with no sponsorship segment.

## Key ideas
- **Handy is an MIT-licensed, offline dictation app with no account, no subscription, and no cloud, and the user picks the speech model.** — The host frames the appeal as privacy (audio stays on the machine, not used for training) and cost (free), contrasting it with commercial dictation tools. ([0:00](https://youtu.be/ZRsDQp9CrXc?t=0))
- **The architecture is a Rust core with a small web-tech settings UI, and each subsystem is a separate library.** — Rust backend; React and TypeScript for settings; whisper-family models (GGML/GGUF) via a transcribe-cpp runtime; Parakeet via transcribe-rs; cpal for audio input; rdev for global shortcuts; rubato for resampling. The host says this keeps it light enough for a laptop. ([0:37](https://youtu.be/ZRsDQp9CrXc?t=37))
- **Silero VAD gates the audio so silence is not transcribed, and the text is pasted into the focused field on release.** — While the shortcut is held, Silero VAD filters out silence. On release, the audio goes to the selected model and the result is pasted into whatever input has focus, so it works in any app. ([0:37](https://youtu.be/ZRsDQp9CrXc?t=37))
- **Model choice is a speed-versus-accuracy trade-off, and the app shows a meter for each model.** — The host compares it to choosing a character in Mario Kart. He uses Parakeet Unified (0.6B params) because it is CPU-only and fast; the project's stated speed is about 5x real time on a mid-range i5, and it runs unnoticed on an M2 Max. Language-specific models are also offered. ([2:04](https://youtu.be/ZRsDQp9CrXc?t=124))
- **The project's stated goal is to be the most forkable dictation app, not the best one.** — The host quotes the mission statement and treats it as an honest positioning choice. Custom models are supported: fine-tuned Whisper GGML files dropped into the models folder show up after a restart. ([2:04](https://youtu.be/ZRsDQp9CrXc?t=124))
- **On one dictated passage, Google Docs voice typing was clearly worst.** — It gave no punctuation or sentence breaks, misheard Cobol, SQLite and LLM, turned Grok into Rock, and rendered ChatGPT badly. ([4:30](https://youtu.be/ZRsDQp9CrXc?t=270))
- **Handy gets punctuation and most technical terms right, and Wispr Flow is best but only a little ahead.** — The host reran the same text in Wispr Flow (transcribed as Whisperflow), which split sentences correctly and got all the terms. He still prefers Handy because it is free, private and open source. ([5:43](https://youtu.be/ZRsDQp9CrXc?t=343))

## Techniques
- **Handy push-to-talk or toggle dictation setup** — Install Handy (open source, MIT). In its settings, set a custom global keyboard shortcut and choose either toggle mode (press once to start, again to stop) or push-to-talk (hold to speak, release to transcribe). Silero VAD trims silence while the key is held, and on release the audio goes to the selected model and the text is pasted into the focused input. The video does not show exact menu paths. *When:* Dictating prompts, notes or messages into any app on a laptop without sending audio to a cloud service.
- **Choosing a model by speed/accuracy trade-off** — Open the model section, where each model has a speed meter and an accuracy meter. For CPU-only machines, the host picks Parakeet Unified (0.6B params), which he says runs about 5x real time on a mid-range i5. Language-specific models are listed as well. *When:* Matching the dictation model to hardware and language: a fast CPU-only model for low latency, or a slower, more accurate one when accuracy matters more.
- **Adding a custom fine-tuned Whisper model** — Convert the fine-tuned Whisper model to GGML format, copy the file into the app's models folder (the path is not shown in the video), restart Handy, and select it from the model list. *When:* Using a domain-tuned Whisper model (for example, one fine-tuned on your vocabulary) with a local dictation app.
- **Side-by-side dictation accuracy check** — Dictate the same passage into each tool, with the same wording. Score the output on punctuation, sentence splitting and whether technical terms (product names, acronyms, model names) are correct. The host used one run per tool with a deliberately term-heavy tangent. This is a quick smoke test, not a benchmark. *When:* Choosing a speech-to-text tool for technical dictation where names and acronyms matter.

## Numbers
- Parakeet Unified is 0.6B parameters and, per the project's own numbers, runs at about 5x real time on a mid-range i5 CPU. The host says it runs unnoticed on an M2 Max. ([2:04](https://youtu.be/ZRsDQp9CrXc?t=124))
- The accuracy test used one dictated passage (about 90 words), run once per tool, with Google Docs voice typing, Handy and Wispr Flow compared. There is no repeated-run or statistical measure. ([4:30](https://youtu.be/ZRsDQp9CrXc?t=270))
- Google Docs voice typing produced no punctuation and mis-transcribed several terms, including Cobol, SQLite, LLM ("Rock" for Grok) and ChatGPT. ([4:30](https://youtu.be/ZRsDQp9CrXc?t=270))
- Wispr Flow (transcribed as Whisperflow) split sentences correctly and got every term right. The host says the gap to Handy is small. ([6:48](https://youtu.be/ZRsDQp9CrXc?t=408))

## Hot takes
- The project's mission is to be the most forkable dictation app, not the best one, and the host calls that honest positioning.
- Free, offline and private outweighs a small accuracy edge: the host prefers Handy over Wispr Flow even though Wispr Flow scored best in his test.
- Google Docs voice typing is clearly behind on punctuation and technical vocabulary.
- Single anecdotal test with one speaker and one passage. It shows the qualitative gap but is not a benchmark, and the video names no word-error-rate numbers.

## Tools mentioned
Handy (open-source offline dictation app, MIT, built by CJ Pace), Tauri (transcribed as "talk"; the Rust-plus-web-UI shell is implied by the description), React, TypeScript, Transcribe CPP (runtime for Whisper-family GGML/GGUF models), transcribe-rs (runs Parakeet), Parakeet Unified 0.6B (CPU-only speech model), Whisper (GGML models, including custom fine-tunes), Silero VAD (transcribed as "Cilero VAD"), cpal (cross-platform audio input), rdev (global keyboard shortcuts), rubato (real-time resampling), Google Docs voice typing (comparison), Wispr Flow (comparison, transcribed as "Whisperflow"), Grok (named as an LLM used in the scenario, not tested), ChatGPT (named in the scenario, not tested)

## Relevance to our work
- **prosharness** (1/3): A local push-to-talk tool could dictate long, spoken prompts into Claude Code sessions. It is a workflow convenience, not a harness feature. → *Optional: try a local push-to-talk dictation tool with the Claude Code CLI for spoken prompts; no ProsHarness code change needed.*
