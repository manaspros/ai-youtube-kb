# Open-Source Dictation Is Here… Goodbye Subscriptions

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `mIL4sZa8M0E` · [watch](https://youtu.be/mIL4sZa8M0E) · **date:** 2026-08-02 · **length:** 4:33 · **format:** review · **quality:** 2/5 · **depth:** intro
- **speakers:** ? · **orgs:** Apple
- **topics:** dev-tools, local-ai · **tags:** dictation, speech-to-text, parakeet, on-device, macos, open-source, privacy, voice-input, whisper-flow, superwhisper

> Better Stack demos Fluid Voice, a free open-source Mac dictation app that runs speech-to-text and LLM cleanup fully on-device. Its main pitch is no subscription and no cloud; it is Mac-only and needs a ~3.5 GB model.

## Summary
The host presents Fluid Voice, a free open-source macOS app that turns speech into text entirely on the local machine. Dictation runs in two local stages: Parakeet transcribes the audio, then a second local editor model called Fluid Intelligence fixes capitalization, punctuation and structure. A single hotkey inserts the cleaned text at the cursor in any app, and the demo dictates a request to check code for bug-prevention practices and gets back a properly formatted comment. The host argues for two benefits: voice and code stay on the Mac, and there is no monthly fee compared with cloud tools such as Wispr Flow or SuperWhisper. The built-in macOS dictation is free but judged weaker for technical text. The caveats are stated plainly: Mac only (iOS and Windows are waitlisted), a roughly 3.5 GB editor model, best on Apple Silicon with slower Intel support, and possible tuning for non-English dictation. The verdict is conditional: worth trying for Mac developers who do not want another subscription, and a cross-platform tool still needed off the Mac. The "four times faster" speed claim is not backed by any benchmark in the video.

## Key ideas
- **Fluid Voice is a free, open-source Mac app whose whole pipeline runs on the local machine, with no cloud server involved.** — The host frames this around the two complaints developers raise about dictation: code or private content leaking to a server, and a recurring subscription. ([0:00](https://youtu.be/mIL4sZa8M0E?t=0))
- **Dictation is a two-model local pipeline: Parakeet transcribes, then a local editor model cleans the text.** — Parakeet produces the raw transcript and Fluid Intelligence, a second local model, fixes capitalization, punctuation and structure before the text is inserted. ([0:00](https://youtu.be/mIL4sZa8M0E?t=0))
- **One global hotkey dictates into whatever field has the cursor, so it works across editors, chat, mail and notes.** — The host names Cursor, Claude, Slack, mail and notes as targets and says the app does not care which one receives the text. ([1:01](https://youtu.be/mIL4sZa8M0E?t=61))
- **Setup is one install line, then granting microphone and accessibility permissions, then choosing a hotkey.** — The host notes that the permission prompts are standard for any Mac app, so they are not a drawback specific to this tool. ([1:01](https://youtu.be/mIL4sZa8M0E?t=61))
- **The demo output is cleaned without manual edits: capitalization, punctuation, technical spelling and comment formatting were all applied.** — The host dictated a request to review code for bug-prevention practices and reports no spinner or wait, because there is no cloud round trip. ([1:01](https://youtu.be/mIL4sZa8M0E?t=61))
- **Compared with the free built-in Mac dictation, the local editor step is the differentiator; the paid cloud tools lack it on-device.** — The host says the built-in dictation is fine for commit messages or docs but weak for text people will read. Wispr Flow and SuperWhisper are described as subscription tools that send audio to the cloud, and they do not match the local cleanup quality. ([2:29](https://youtu.be/mIL4sZa8M0E?t=149))
- **The caveats are concrete: Mac only, a ~3.5 GB editor model, slower on Intel, and possible tuning for non-English speech.** — Apple Silicon is described as fast enough to forget about, while iOS and Windows are only on a waitlist. ([2:29](https://youtu.be/mIL4sZa8M0E?t=149))
- **The recommendation is conditional: use it as the everyday Mac dictation tool and keep a cross-platform tool for other machines.** — The host suggests using it for boring typing such as email, docs, code comments, Slack and prompting Claude, and says it does not help on Windows or iOS. ([3:45](https://youtu.be/mIL4sZa8M0E?t=225))

## Techniques
- **Local two-stage dictation with LLM cleanup** — Stage 1: a local ASR model (Parakeet) transcribes speech. Stage 2: a small local editor LLM (Fluid Intelligence) rewrites the raw transcript for capitalization, punctuation and structure. Bind one push-to-talk hotkey, and insert the result at the cursor of the focused app. Nothing leaves the machine. *When:* Dictating prompts, code comments or messages that may contain private code or data, and when you do not want a per-month dictation subscription. Useful when you dictate prompts into coding agents such as Claude or Cursor.
- **Install and permission setup for macOS dictation tools** — Install with the one-line command given in the video description (the command is not spoken in the transcript). Open the app, grant the microphone and accessibility permissions, then pick a hotkey, either a custom one or the default built-in one. *When:* First-time setup on a Mac. The accessibility permission is required for text to be inserted into other apps.

## Numbers
- Editor (cleanup) model is about 3.5 GB, a real download. ([2:29](https://youtu.be/mIL4sZa8M0E?t=149))
- Host says Fluid Voice is about four times faster than other dictation tools. No benchmark or method is given. ([1:01](https://youtu.be/mIL4sZa8M0E?t=61))
- Video length 4:33; the install is described as a one-line command. ([1:01](https://youtu.be/mIL4sZa8M0E?t=61))

## Hot takes
- The host says Fluid Voice is the only free, open-source, local option that does smart formatting, and that the free built-in Mac dictation is the weakest option.
- The speed claim (four times faster than alternatives) is asserted without any benchmark.
- The host explicitly declines to say the tool is worth it for everyone; the verdict is limited to Mac developers who want to avoid a subscription.

## Tools mentioned
Fluid Voice, Parakeet, Fluid Intelligence, Wispr Flow, SuperWhisper, Cursor, Claude, Slack, Homebrew (brew install mentioned, command not spoken)

## Relevance to our work
- **general** (1/3): A free, local, private dictation tool for prompting coding agents on a Mac could save time, but it is not an engineering practice. → *Optional: try Fluid Voice (free, Mac only) for dictating prompts to Claude Code; no project change needed.*
