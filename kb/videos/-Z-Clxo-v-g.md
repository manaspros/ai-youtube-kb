# This Free Whisper App Runs Fully Offline (No Cloud, No API)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `-Z-Clxo-v-g` · [watch](https://youtu.be/-Z-Clxo-v-g) · **date:** 2026-02-02 · **length:** 4:48 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Better Stack, OpenAI
- **topics:** local-ai, dev-tools · **tags:** whisper, offline-transcription, speech-to-text, subtitles, desktop-app, cli, privacy, word-timestamps

> Quick walkthrough of Buzz, a free open-source desktop and CLI app that runs Whisper transcription and translation fully offline, with an honest list of its drawbacks.

## Summary
The presenter introduces Buzz, a free, MIT-licensed open-source app that wraps OpenAI's Whisper model to transcribe and translate audio locally, with no internet connection or API key. It accepts MP3, MP4, YouTube links and live microphone input, and outputs plain text, SRT or VTT, plus an interactive viewer for searching and replaying segments. The demo runs a shell script covering text and VTT outputs, sentence and word-level timestamps in JSON, and translating a French file to English through the CLI with explicit input and output languages. The presenter says a roughly one-hour podcast episode took a few minutes, which he calls quick for that length of audio. The main caveats are large model files (gigabytes of disk), slow CPU-only fallback without a GPU, and a sometimes tedious driver setup. The video is a short tool tour with no accuracy or speed benchmarks, so its speed and privacy claims are not measured.

## Key ideas
- **Buzz is a free, MIT-licensed open-source desktop app with a CLI that runs Whisper transcription and translation entirely on your machine.** — The presenter stresses privacy: audio stays local, no uploads, no API keys, and no per-use fees once models are downloaded. ([0:00](https://youtu.be/-Z-Clxo-v-g?t=0))
- **Input and output coverage is broad: local files, YouTube links and live mic in; plain text, SRT and VTT out, plus an interactive viewer for search and replay.** — Useful for notes and subtitle editing. The GUI lists previously run files and shows each transcript with its timestamps. ([0:00](https://youtu.be/-Z-Clxo-v-g?t=0))
- **The CLI can emit sentence-level and word-level timestamps, including JSON, from one run.** — Word-level timing is what the presenter finds most useful, for clip editing and alignment. A nearly one-hour episode finished in a few minutes. ([1:25](https://youtu.be/-Z-Clxo-v-g?t=85))
- **Non-English audio can be translated to English from the CLI by specifying the input and output languages.** — The French example produced clean English output. The same CLI can be called from Python scripts. ([2:21](https://youtu.be/-Z-Clxo-v-g?t=141))
- **The main cost is disk and hardware: the models are gigabytes in size, and without a GPU it falls back to the CPU, which is slow.** — The presenter names large models, CPU fallback and driver setup as the drawbacks, and says the tool may not suit low-disk machines. ([3:33](https://youtu.be/-Z-Clxo-v-g?t=213))
- **Buzz wraps Whisper with faster backends and normalizes audio before inference.** — The backends are not named in the video. The pipeline is: clean and normalize audio, run the model, then write the requested output format. ([3:33](https://youtu.be/-Z-Clxo-v-g?t=213))

## Techniques
- **Fully offline transcription with Buzz** — Install the desktop app (DMG on macOS) or use the CLI. Feed it a local MP3 or MP4, a YouTube link or the live mic. Choose plain text, SRT or VTT output. The commands and flags are not shown on screen; only the outputs are. *When:* Audio is private or sensitive, or you want free bulk transcription without a cloud ASR API. Assumes a GPU or patience for CPU runs and enough disk for the models.
- **Word-level timestamps from JSON output** — Run the CLI with word-level timestamp output alongside sentence timestamps, saving the result as JSON. The exact flag is not shown in the video. *When:* You need word-accurate timing for subtitle alignment, clip cutting or search-to-seek in a viewer.
- **Foreign-language audio to English from the CLI** — Run the CLI on the foreign-language file and set the input and output language explicitly. The video demonstrates French to English. Flag names are not shown. *When:* You need a translated transcript of non-English audio, such as an interview or podcast, without a translation API.
- **Scripted batch of transcription scenarios** — The presenter wraps several runs (text, VTT, word-level JSON, translation) in one shell file and runs it end to end. The script contents are not shown. *When:* You want reproducible comparisons of output formats or settings, or a repeatable local transcription job.

## Numbers
- The source audio was a roughly one-hour podcast episode, transcribed in a few minutes (wall-clock time not measured precisely). ([1:25](https://youtu.be/-Z-Clxo-v-g?t=85))
- Whisper model files are described as gigabytes in size. ([3:33](https://youtu.be/-Z-Clxo-v-g?t=213))
- Cost is zero after the models are downloaded; the app is free and MIT-licensed. ([0:00](https://youtu.be/-Z-Clxo-v-g?t=0))

## Hot takes
- Thin tool demo: no accuracy comparison against cloud ASR and no timing benchmark, so the 'quick' and 'private' claims are unmeasured. The 'blowing up on GitHub' claim gives no star count or date.
- The most useful part is the presenter's own caveats (gigabyte models, CPU fallback, driver setup). The CLI commands and flags are never shown on screen.
- Quality is capped at 2: it is a light overview with no reproducible steps and no novel insight, not a sales pitch.

## Tools mentioned
Buzz, OpenAI Whisper, Python, GitHub

## Relevance to our work
- **agentos** (1/3): Offline Whisper is a self-hosted speech-to-text option. It is peripheral to AgentOS's LLM proxy and InferCraft serving stack. → *Low priority: if AgentOS ever needs voice input, benchmark a local Whisper backend on the RTX 5090 against cloud ASR for latency and word accuracy. No change needed now.*
