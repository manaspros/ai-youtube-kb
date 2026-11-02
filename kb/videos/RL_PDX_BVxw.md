# I Tried the Open Source ElevenLabs Alternative (Voicebox)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `RL_PDX_BVxw` · [watch](https://youtu.be/RL_PDX_BVxw) · **date:** 2026-07-02 · **length:** 7:39 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack presenter (not named in transcript) · **orgs:** Better Stack, ElevenLabs
- **topics:** voice-multimodal, local-ai, mcp-and-tools · **tags:** voicebox, local-first, voice-cloning, text-to-speech, dictation, whisper, mcp, apple-silicon, open-source, elevenlabs-alternative

> Better Stack walkthrough of Voicebox, a free open-source local voice studio for cloning, TTS, system-wide dictation and agent speech. Works well on Apple Silicon, but the tool is early and the agent integration was not tested.

## Summary
The presenter tries Voicebox, an open-source desktop app pitched as a local alternative to ElevenLabs. It bundles voice cloning, text-to-speech, Whisper-based system-wide dictation, a multitrack editor, an MCP server and a local REST API. He installs the desktop app instead of using Docker, which he says took nearly 30 minutes, then clones his own voice on an M4 Mac and generates speech from it. He also demonstrates dictation into an editor through a global hotkey. He argues the main value is control over privacy, cost and integration rather than output quality, since ElevenLabs still sounds better and handles long-form content more consistently. He flags early-stage rough spots, mainly on Windows (GPU detection, model setup, exports), and says restarting the app fixed his own issue. The agent speech-back integration with Claude Code or Cursor is only described, not tested.

## Key ideas
- **Voicebox is pitched as a local runner for voice, comparable to Ollama for text models: one app for cloning, TTS, dictation, editing and agent integration.** — Positioned as free, local and unlimited, versus subscription cloud TTS. Features listed: voice cloning, Whisper dictation, multitrack editor, stories/timelines, MCP support and a local REST API. ([0:00](https://youtu.be/RL_PDX_BVxw?t=0))
- **The pitch is consolidation: it packages a workflow people otherwise stitch together from separate tools.** — The presenter contrasts it with running Piper, Whisper and assorted scripts for transcription, cloning, TTS and UI separately, which he says he had been smoothing together by hand. ([4:18](https://youtu.be/RL_PDX_BVxw?t=258))
- **Install the desktop app rather than Docker for speed.** — He says Docker container setup took nearly 30 minutes, while the desktop installer was much faster. Setup is download the installer from the website or GitHub releases, launch the app, then pull the local models you need. ([1:57](https://youtu.be/RL_PDX_BVxw?t=117))
- **Voice cloning needs a profile with a short audio sample plus its transcript, and generation runs locally with no API key.** — Profile fields: name, description and instructions on how the model should behave. Input is a recording or uploaded short file plus the transcription. Pick a profile and model, type text, hit generate. The first run downloads the model, so it is slow. ([1:57](https://youtu.be/RL_PDX_BVxw?t=117))
- **Global-hotkey dictation drops speech straight into the active editor, and the presenter suggests agents could speak back through Voicebox.** — The speech-back idea (Claude Code, Cursor or a local agent triggering speech through Voicebox via MCP or REST) is described but not tested in the video. ([3:03](https://youtu.be/RL_PDX_BVxw?t=183))
- **Local-first wins on privacy and cost; ElevenLabs still wins on output quality and long-form consistency.** — He says ElevenLabs remains better for heavy daily use. Voicebox's value is data control, no per-character cost and integration control, not the prettiest audio. ([4:18](https://youtu.be/RL_PDX_BVxw?t=258))
- **Expect rough edges: the tool dropped recently and Windows users may hit GPU detection, model setup and export problems.** — Workaround he offers: restart the app. Emotion control depends on the chosen model; the Chatterbox TTS Turbo model has emotions built in. ([5:22](https://youtu.be/RL_PDX_BVxw?t=322))

## Techniques
- **Desktop install instead of Docker** — Download the platform installer from the Voicebox website or GitHub releases, launch the app, then pull the local models needed. Docker was the slower path in his test (about 30 minutes). *When:* First-time setup on a dev laptop when you want fast onboarding over containerized deployment.
- **Clone a voice from a short sample** — Create a voice profile with a name, a description and instructions for how the model should act. Record yourself or upload a short audio file, add its transcription, then pick the profile and model and generate. *When:* Generating speech in your own voice locally, with no cloud API key or per-character costs.
- **System-wide dictation via global hotkey** — Press the global hotkey, speak, and the transcribed text lands in the focused app such as an editor. Whisper-based transcription runs locally. *When:* Capturing notes or comments by voice in any app where talking is faster than typing.
- **Restart to clear app-level glitches** — If GPU detection, model setup or export misbehaves, restart the Voicebox app. The presenter says this fixed his Mac issue. *When:* Early-release instability, especially on Windows.
- **Pick the model for emotion control** — Choose a model with built-in emotion support. The presenter names Chatterbox TTS Turbo (transcribed as Shatterbox). *When:* Needing expressive delivery; emotion control depends on the model selected.

## Numbers
- Voicebox has around 30,000 GitHub stars. ([0:00](https://youtu.be/RL_PDX_BVxw?t=0))
- Docker-based setup took nearly 30 minutes for the presenter; the desktop app was much faster. ([1:57](https://youtu.be/RL_PDX_BVxw?t=117))
- Test hardware was an M4 Mac. No latency, VRAM or price figures were given; the comparison with ElevenLabs is qualitative. ([1:07](https://youtu.be/RL_PDX_BVxw?t=67))

## Hot takes
- The tool is early (released this year), and Windows users will hit GPU detection, model setup and export issues.
- ElevenLabs still wins on quality and long-form consistency; Voicebox's advantage is local control, cost and integration.
- The agent speech-back use case (Claude Code or Cursor talking via Voicebox) is the most interesting pitch but was not tested in the video.
- Single-user anecdote with no benchmarks; the 30-minute Docker figure is one experience.

## Tools mentioned
Voicebox, ElevenLabs, Ollama, Docker, Piper, Whisper, Claude Code, Cursor, Chatterbox TTS Turbo, MCP

## Relevance to our work
- **agentos** (1/3): Local-first voice I/O with an MCP server and REST API could become a tool surface in the stack, but voice is not a current AgentOS layer. → *Note Voicebox's MCP/REST surface as a possible optional TTS tool. Revisit only if voice I/O enters the roadmap.*
- **prosharness** (1/3): ProsHarness already has phone-driven approvals; spoken status for long Claude Code runs or approval prompts could complement that. → *Prototype a spoken completion/approval notification from a local TTS MCP server on one long ProsHarness run and see whether it helps.*
