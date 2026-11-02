# This Tiny 82M Model Just Beat Most TTS APIs (Runs Locally)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `bdf6BxyxCnQ` · [watch](https://youtu.be/bdf6BxyxCnQ) · **date:** 2026-05-02 · **length:** 5:41 · **format:** review · **quality:** 3/5 · **depth:** intro
- **speakers:** Better Stack host (unnamed) · **orgs:** Better Stack, ElevenLabs, OpenAI
- **topics:** voice-multimodal, local-ai, infra-cost-scaling · **tags:** kokoro, tts, text-to-speech, local-ai, apple-silicon, voice-agents, open-weights, apache-2.0, privacy, latency, cpu-inference

> Better Stack tries Kokoro 82M, a small open TTS model, on a Mac M4 Pro and weighs its speed, privacy and cost against its missing voice cloning and emotion control.

## Summary
The host opens by claiming the 82M-parameter Kokoro model beats much larger TTS systems and runs locally faster than many paid APIs. He frames the usual choice as cloud TTS (easy to start, but recurring bills, latency spikes and an extra dependency) versus large open models (more memory and still slow). Kokoro is Apache 2.0, reportedly trained on under 100 hours of data, and runs on CPU and fast on Apple Silicon. On an M4 Pro he installs it with pip in a conda environment, runs the official repo's Python script without modification, and generates English and then French WAV files by choosing a voice and language. Architecturally it is StyleTTS2-based with a lightweight vocoder, offers 8 languages and 54 voices, and has no zero-shot voice cloning and no emotion control. He argues devs adopt it for low latency, offline operation, privacy and cheap scale, since many instances fit on one machine. His criticisms are neutral emotional range, weaker non-English voices and no cloning. The video measures no latency, cost or benchmark figures, so its speed and leaderboard claims are unverified.

## Key ideas
- **Cloud TTS is easy but adds recurring cost, latency spikes and a network dependency for every spoken response.** — The host frames the choice as cloud APIs versus large open TTS models, which need more memory and are still not fast. ([0:00](https://youtu.be/bdf6BxyxCnQ?t=0))
- **Kokoro 82M is pitched as a small model that ranks well despite little training data.** — Claims: under 100 hours of training data, Apache 2.0 license, runs on CPU and is very fast on Apple Silicon. The leaderboard claim is asserted, not shown. ([0:56](https://youtu.be/bdf6BxyxCnQ?t=56))
- **Setup is a pip install plus the official repo's Python script, with no code changes.** — He reports about 30 seconds of setup on a Mac M4 Pro inside a conda environment and runs the script as-is. ([0:56](https://youtu.be/bdf6BxyxCnQ?t=56))
- **Output is WAV, and voice and language are selectable, including French.** — The French run needed no special setup. The host says his French is rusty and judges quality by ear. ([2:09](https://youtu.be/bdf6BxyxCnQ?t=129))
- **The design trades voice cloning and emotion control for size and speed.** — Architecture is StyleTTS2-style with a lightweight vocoder. 8 languages and 54 voices, with Misaki named for text processing. No zero-shot cloning and no emotion control. Compared with XTTS, CosyVoice and F5-TTS (hundreds of millions to over a billion parameters) and with hosted ElevenLabs and OpenAI TTS, which send data out and charge per request. ([2:47](https://youtu.be/bdf6BxyxCnQ?t=167))
- **Developers adopt it for speed, offline use, privacy and cost at scale.** — No API keys or network needed, audio stays local, and the small footprint allows many instances per machine. The host says short pauses matter for voice agents to feel real. ([4:10](https://youtu.be/bdf6BxyxCnQ?t=250))
- **Its weak points are neutral delivery and non-English quality.** — Good for narration, poor for dramatic speech. Non-English voices are still improving. The host's verdict is that it solves cost, latency, privacy and deployment for most teams, but not every voice use case. ([4:10](https://youtu.be/bdf6BxyxCnQ?t=250))

## Techniques
- **Run a small local TTS model as a drop-in for cloud TTS** — Install with pip into a conda env (the exact package and command are not shown in the video; take them from the official Kokoro repo). Run the repo's Python script unmodified. Choose voice and language from the script's options. Output is saved as WAV files. *When:* When cloud TTS latency, per-request cost or sending audio to a third party is a problem, and you can accept no zero-shot voice cloning and no emotion control.
- **Pick a small TTS model when time-to-first-audio matters** — Prioritise a small model that starts quickly and fits many instances per machine, rather than a large model with better expressiveness. The host claims this lets one machine serve more concurrent voice streams, but shows no measurements. *When:* Real-time voice agents where long pauses break the conversation, or deployments with many concurrent speech requests.
- **Evaluate TTS by listening to your own text per language and voice** — Run the same script with the default English voice, then switch to another language and voice and rewrite the input text. Judge naturalness by ear. The host does this for French with a rusty speaker, which he admits limits the judgement. *When:* A quick smoke test before committing to a TTS model, especially for non-English output.

## Numbers
- Kokoro has 82M parameters. ([0:00](https://youtu.be/bdf6BxyxCnQ?t=0))
- Trained on under 100 hours of data (host's statement). ([0:56](https://youtu.be/bdf6BxyxCnQ?t=56))
- Setup takes about 30 seconds on an M4 Pro (anecdotal). ([0:56](https://youtu.be/bdf6BxyxCnQ?t=56))
- Supports 8 languages and 54 voices. ([2:47](https://youtu.be/bdf6BxyxCnQ?t=167))
- Comparison models: XTTS, CosyVoice and F5-TTS range from hundreds of millions to over a billion parameters. ([2:47](https://youtu.be/bdf6BxyxCnQ?t=167))
- No latency, throughput, cost or leaderboard numbers are shown in the video. ([0:00](https://youtu.be/bdf6BxyxCnQ?t=0))

## Hot takes
- The title and intro claim the 82M model beats much larger TTS systems and ranks at the top of leaderboards, but no leaderboard or benchmark appears in the video. The evidence is two listening tests on one Mac M4 Pro.
- Speed claims such as 'insanely fast' and 'cuts that delay way down' are never measured. No time-to-first-audio or real-time factor is shown.
- The host says a model with no emotion control still sounds like AI, and that neutral delivery suits narration but not drama.

## Tools mentioned
Kokoro 82M (TTS model, Apache 2.0), StyleTTS2 (architecture the model is based on), Misaki (text processing library named by the host), XTTS, CosyVoice, F5-TTS, ElevenLabs (cloud TTS), OpenAI TTS (cloud TTS), Python, pip, conda, Mac M4 Pro (test hardware)

## Relevance to our work
- **agentos** (1/3): Voice I/O is not one of the AgentOS pillars, and Kokoro is a CPU TTS model rather than an LLM served by vLLM. The only overlap is a possible local voice front end for agents. → *No change now. If voice I/O is ever added to AgentOS, benchmark Kokoro against a cloud TTS API on latency and cost before choosing.*
