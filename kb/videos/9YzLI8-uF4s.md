# The Tiny TTS Everyone Loved Isn't Tiny Anymore (KittenTTS 2)

- **channel:** [Better Stack](../channels/betterstack.md) · **id:** `9YzLI8-uF4s` · [watch](https://youtu.be/9YzLI8-uF4s) · **date:** 2026-10-12 · **length:** 8:21 · **format:** review · **quality:** 3/5 · **depth:** practitioner
- **speakers:** Josh · **orgs:** Better Stack, Resemble AI, Stellon Labs, ElevenLabs, Hugging Face
- **topics:** voice-multimodal, local-ai, governance-compliance · **tags:** tts, voice-cloning, kittentts, open-weights, licensing, apple-silicon, cpu-inference, source-available, whisper, pytorch

> Hands-on review of KittenTTS 2: it has grown to 1.7B parameters, runs slower than real time on a Mac CPU, and ships source-available weights under a revocable, revenue-gated license, unlike the tiny Apache-2.0 original.

## Summary
Josh from Better Stack installs KittenTTS 2 and tests its voice cloning, then argues it is a different kind of project from the original Kitten TTS. The model is a 1.7B-parameter speech-language model that generates audio tokens, paired with a separately downloaded vocoder (S3 Gen from Resemble AI's Chatterbox Turbo). Ternary weights bring the default download to about 950 MB. Cloning from a short recording works reasonably well in his test, but on a Mac the code only detects NVIDIA GPUs, so generation runs on CPU at roughly 2-3x slower than real time even with the suggested 8 Torch threads. The speaker compares it with ElevenLabs, noting the local-only privacy and zero-cost upside. The main warning is the license: code and pip package are Apache 2.0, but the weights fall under the Stellon Labs Community License with revocable commercial terms, registration, attribution, and a free-commercial cutoff at $1M revenue or $1M raised. The speaker also notes unverified self-reported similarity scores, language and normalization caveats, an unproven CPU real-time port, and fast-moving, early-stage releases. His verdict: fine for prototypes, but use something else for production.

## Key ideas
- **KittenTTS 2 is not the tiny model the name implies: about 1.7B parameters, versus 15-80M parameters (25-80 MB) for the original Apache-2.0 Kitten.** — The original was small enough to run almost anywhere and had no voice cloning. The speaker says v2 is effectively a different class of model that kept the name. ([0:00](https://youtu.be/9YzLI8-uF4s?t=0))
- **Voice cloning is a two-stage pipeline: a speech-language model writes audio tokens from text plus a short reference voice, then a vocoder turns those tokens into sound.** — The speaker uses a sheet-music (composer) and orchestra (vocoder) analogy. KittenTTS 2 supplies the new composer, but the default vocoder is S3 Gen from Resemble AI's Chatterbox Turbo, which is downloaded on first run. ([0:58](https://youtu.be/9YzLI8-uF4s?t=58))
- **Model size is kept down by ternary weights at about 1.5 bits per weight. Build sizes are roughly 470 MB (small), 950 MB (default), and 3.5 GB (full), and there are 47 built-in voices.** — Installing also pulls in torch, transformers and diffusers, and the Chatterbox vocoder and a Whisper model are needed alongside the weights, so the total footprint is well above the model file alone. ([0:58](https://youtu.be/9YzLI8-uF4s?t=58))
- **Cloning works from a short reference clip. Kitten transcribes the clip with Whisper itself, and the speaker judges the output decent though not perfect. Emotion tags and laugh sounds are marked beta.** — The speaker recorded about 10 seconds of speech and generated a sentence he never recorded. The clip was not heard in an independent evaluation. ([2:21](https://youtu.be/9YzLI8-uF4s?t=141))
- **On a Mac, KittenTTS 2 never uses the Apple GPU. The code checks only for an NVIDIA card and otherwise falls back to CPU, which runs roughly 2-3x slower than real time per the project's own docs.** — Activity Monitor shows a pinned CPU and an idle GPU. The one documented speed-up is setting Torch to 8 threads, which helps but does not reach real time. ([3:31](https://youtu.be/9YzLI8-uF4s?t=211))
- **Local-first is the main reason to choose it over a hosted service like ElevenLabs: no account, no recurring cost, and the user's voice never leaves the machine.** — The speaker treats this as a good trade for some teams, but only after accepting the size, speed and license costs. ([3:31](https://youtu.be/9YzLI8-uF4s?t=211))
- **The license is the biggest practical catch. Code and pip package are Apache 2.0, but the weights are under the Stellon Labs Community License, which is revocable and gated by revenue, funding, branding and no-distillation terms.** — Commercial use requires contacting the vendor to register. The free commercial grant ends above $1M revenue or $1M total funding. You must show 'powered by Stellon Labs', ship the license and a notice file, and may not use the model to train or distill other models. The acceptable use policy is only available by contacting them. ([5:52](https://youtu.be/9YzLI8-uF4s?t=352))
- **Quality claims are the vendor's own numbers, and the project is brand new.** — Reported speaker similarity is 0.49-0.72, and 0.81 when cloning an unseen recording. The speaker says no one has independently verified them. The model is a few days old with about 130 Hugging Face downloads. ([4:32](https://youtu.be/9YzLI8-uF4s?t=272))
- **Real-time CPU claims are unproven. The one C++ port that claims it requires libtorch, has Metal turned off, has zero stars, and publishes no performance numbers.** — The speaker's advice is to treat CPU real-time as unverified until someone measures it. ([6:52](https://youtu.be/9YzLI8-uF4s?t=412))

## Techniques
- **Clone a voice from a short reference clip** — Record about 10 seconds of clean speech. Pass the clip as the reference to the generate call. The library transcribes the reference with Whisper automatically, so no transcript is needed. Then generate the target sentence. Emotion tags and laugh sounds are available but still in beta. *When:* Quick prototyping of voice-cloned narration where a hosted cloning service is not wanted for privacy or cost reasons.
- **Check that the GPU is actually used** — Open Activity Monitor during generation. On this build, CPU pinned plus idle GPU on Apple Silicon means the code has fallen back to CPU. Set Torch to 8 threads to get the best CPU speed the speaker found, but expect it to stay below real time. *When:* Before committing to a local TTS model on a Mac, to confirm the accelerator is in use.
- **Turn off text normalization for non-English text** — When generating non-English speech, disable the normalization option. Long inputs are split into chunks automatically because the model can cut off or repeat itself. *When:* Non-English TTS, or any long-form text that needs chunking.
- **License gate before shipping model weights** — Read the license for code and weights separately. Check revocability, revenue and funding thresholds, attribution wording, the notice file requirement, and any no-distillation clause. For this model, the acceptable use policy requires contacting the vendor. *When:* Before adding any open-weight or source-available model to a commercial product or internal platform.

## Numbers
- KittenTTS 2 is about 1.7B parameters; the original was 15-80M parameters (about 25-80 MB). ([0:00](https://youtu.be/9YzLI8-uF4s?t=0))
- Ternary weights at about 1.5 bits each. Builds: about 470 MB (small), 950 MB (default), 3.5 GB (full). 47 built-in voices. ([0:58](https://youtu.be/9YzLI8-uF4s?t=58))
- CPU generation on Mac runs about 2-3x slower than real time per the project docs; setting Torch to 8 threads helps but does not reach real time. ([3:31](https://youtu.be/9YzLI8-uF4s?t=211))
- Self-reported speaker similarity 0.49-0.72, and 0.81 on an unseen recording. Not independently tested. ([4:32](https://youtu.be/9YzLI8-uF4s?t=272))
- About 130 Hugging Face downloads at the time of review; the model was a few days old. ([4:32](https://youtu.be/9YzLI8-uF4s?t=272))
- Free commercial grant ends at more than $1M revenue or more than $1M total funding. ([5:52](https://youtu.be/9YzLI8-uF4s?t=352))
- Docs list 10 languages; the README says 20. ([5:52](https://youtu.be/9YzLI8-uF4s?t=352))
- Four PyPI releases in four days; about 120 open issues. ([6:52](https://youtu.be/9YzLI8-uF4s?t=412))
- Cloning from about 5 seconds of audio (per intro); about 10 seconds was recorded for the demo. ([0:00](https://youtu.be/9YzLI8-uF4s?t=0))

## Hot takes
- The name 'Tiny' no longer applies: KittenTTS 2 is a 1.7B model with weights that are source-available, not open source.
- The license makes the model a poor fit for commercial startups past the $1M thresholds, and revocability means it is not a stable foundation.
- Real-time CPU performance is a claim with no evidence yet. Treat it as unproven.
- Pick a hosted provider such as ElevenLabs or an alternative such as VoxCPM2 for anything beyond an MVP.

## Tools mentioned
KittenTTS 2 (Kitten TTS v2), Kitten TTS (original, Apache 2.0), S3 Gen vocoder (Resemble AI, Chatterbox Turbo), Whisper (reference-clip transcription), PyTorch (torch), transformers, diffusers, Activity Monitor, ElevenLabs, VoxCPM2, libtorch (C++ port), Hugging Face, PyPI

## Relevance to our work
- **agentos** (1/3): Local TTS for voice agents is adjacent to the stack, but this model does not touch the proxy, memory, inference or observability pillars. The license lesson applies to any open-weight model AgentOS might serve. → *When InferCraft or any model registry adds a new open-weight model, record its code and weight licenses separately, including revocation, revenue thresholds and attribution terms.*
